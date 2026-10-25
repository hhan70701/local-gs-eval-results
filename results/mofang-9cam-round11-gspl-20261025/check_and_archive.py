import os,sys,json,csv,shutil,math
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parents[2];os.chdir(R);sys.path.insert(0,str(R))
from lgs.common import load_cfg,load_json,read_mask,setup_cams,chroma_fg,dilate,imread_rgb
from scripts.evaluate import read_alpha,paste_weight,load_rgb
w=R/'work/round11';a=R/'results/mofang-9cam-round11-gspl-20261025';a.mkdir(parents=True,exist_ok=True)
def cp(p,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
def cw(p,rr):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w') as f:
  d=csv.DictWriter(f,fieldnames=list(rr[0]));d.writeheader();d.writerows(rr)
for p in (w/'eval').glob('*/*_montage.png'):cp(p,a/'eval'/p.relative_to(w/'eval'))
for p in (w/'eval_jobs').glob('*/eval/*/*_montage.png'):cp(p,a/'eval'/p.parent.name/p.name)
for folder in ('gs','flow','poses','prepare'):
 for p in (w/folder).rglob('*.json'):cp(p,a/folder/p.relative_to(w/folder))
for p in (w/'logs').iterdir():
 if p.is_file():cp(p,a/'logs'/p.name)
cfg=load_cfg('configs/mofang_9cam.yaml');training=[];timings=[];checkpoint_times=[];boxes=[]
for s in cfg['setups']:
 p=w/'gs'/s/'gs_tok448_nat_dil_al/meta.json'
 if not p.exists():continue
 m=load_json(p);t=m['tto'];box=t['log'][0].get('box',{'w':t['res'],'h':t['res'],'area_frac':1.0,'xy':[(0,0)]*len(cfg['setups'][s]['context'])});
 for cam,xy in zip(cfg['setups'][s]['context'],box['xy']):boxes.append(dict(setup=s,camera=cam,x=xy[0],y=xy[1],w=box['w'],h=box['h'],full_res=t['res'],area_frac=box['area_frac']))
 for en in t['log']:
  if 'time_s' in en:checkpoint_times.append(dict(setup=s,iteration=en['iter'],cumulative_time_s=en['time_s'],input_psnr_mean=float(np.mean(en['ctx_psnr'])),box_w=box['w'],box_h=box['h'],area_frac=box['area_frac']))
 timings.append(dict(setup=s,total_tto_time_s=t['time_s'],train_gaussians=t['train_gaussians'],total_gaussians=m['num_gaussians'],supervision_res=t['res'],window=m['window'][2],checkpoints=str(cfg['gs']['tto']['checkpoints'])))
 for entry in t['log']:
  for camera,psnr in zip(cfg['setups'][s]['context'],entry['ctx_psnr']):training.append(dict(setup=s,camera=camera,iteration=entry['iter'],loss=entry['loss'],input_crop_psnr=psnr))
if training:
 cw(a/'eval/tto_training.csv',training);cw(a/'eval/tto_timing.csv',timings);cw(a/'eval/tto_checkpoint_timing.csv',checkpoint_times);cw(a/'eval/tto_supervision_boxes.csv',boxes)
if not (w/'eval/validation.json').exists():
 print(json.dumps({'complete':False,'training_setups':len(timings),'montages':len(list((a/'eval').glob('*/*_montage.png')))}));sys.exit()
for p in (w/'eval').iterdir():
 if p.is_file():cp(p,a/'eval'/p.name)
merge_counts={}
for name in ('metrics.csv','auc.csv','registration.csv','risk_sweep.csv','paste.csv','tokchk.csv','token_ringreg.csv'):
 with (w/'eval'/name).open(newline='') as f:combined=list(csv.reader(f))
 expected=[]
 for setup in ('cam3','cam5'):
  with (w/'eval_jobs'/setup/'eval'/name).open(newline='') as f:part=list(csv.reader(f))
  assert part[0]==combined[0]
  expected.extend(part[1:])
 assert combined[1:]==expected,name
 merge_counts[name]=len(expected)
(a/'eval/parallel_merge_validation.json').write_text(json.dumps(merge_counts,indent=2)+'\n')
rows=list(csv.DictReader((a/'eval/metrics.csv').open()));chk=list(csv.DictReader((a/'eval/tokchk.csv').open()));by={(r['setup'],r['target'],r['method'],r['region']):r for r in rows};ref=cfg['eval']['ref_flow'];support=[];checked=0
for s in cfg['setups']:
 ctx,targets=setup_cams(cfg,s)
 for src in ('al','alv'):
  for v in cfg['tokens']['variants']:
   bn=f'gs_tok{v}448_nat_dil_{src}_local';bm=load_json(w/'gs'/s/bn/'meta.json')
   for k in targets:
    valid=read_mask(w/'gs'/s/bn/f'cam{k}_valid.png');flow=load_rgb(w/'flow'/s/ref/f'cam{k}.png');near=dilate(chroma_fg(flow,cfg['chroma']),cfg['tokens']['paste_fg_dilate_px']);fg=read_mask(w/'prepare'/f'fg_aligned_{k:02d}.png')
    core=(read_alpha(w/'gs'/s/bn/f'cam{k}_alpha_core.png')>.5)&valid&near;ok=valid&(read_alpha(w/'gs'/s/bn/f'cam{k}_alpha.png')>.5);wb=paste_weight(core,ok,cfg['tokens']['paste_feather_px'])
    for it in cfg['gs']['tto']['checkpoints']:
     tn=bn.replace('_local',f'_tto{it}_local');tm=load_json(w/'gs'/s/tn/'meta.json')
     for key in ('num_gaussians','window','local_gaussians','ctx_self_psnr'):assert tm[key]==bm[key]
     assert tm['tto_iters']==it
     tv=read_mask(w/'gs'/s/tn/f'cam{k}_valid.png');assert np.array_equal(tv,valid)
     rgb=imread_rgb(w/'gs'/s/tn/f'cam{k}.png');assert rgb.shape==(1080,1920,3)
     alpha=read_alpha(w/'gs'/s/tn/f'cam{k}_alpha.png');ac=read_alpha(w/'gs'/s/tn/f'cam{k}_alpha_core.png');assert np.isfinite(alpha).all() and np.isfinite(ac).all()
     tc=(ac>.5)&tv&near;tw=paste_weight(tc,tv&(alpha>.5),cfg['tokens']['paste_feather_px']);inter=(core&tc).sum();union=(core|tc).sum()
     support.append(dict(setup=s,target=k,variant=v,pose_source=src,tto_steps=it,ff_core_px=int(core.sum()),tto_core_px=int(tc.sum()),core_masks_equal=bool(np.array_equal(core,tc)),core_iou=float(inter/max(union,1)) if union else 1.0,core_changed_px=int((core!=tc).sum()),ff_fg_covered=float((core&fg).sum()/fg.sum()),tto_fg_covered=float((tc&fg).sum()/fg.sum()),weight_max_abs_difference=float(np.max(np.abs(wb-tw))),weight_mean_abs_difference=float(np.mean(np.abs(wb-tw)))));checked+=1
cw(a/'eval/tto_paste_support.csv',support)
full_checked=0
for s in cfg['setups']:
 for src in ('al','alv'):
  for it in cfg['gs']['tto']['checkpoints']:
   folder=w/'gs'/s/f'gs_tok448_nat_dil_{src}_tto{it}'
   assert load_json(folder/'meta.json')['tto_iters']==it
   for k in setup_cams(cfg,s)[1]:
    assert imread_rgb(folder/f'cam{k}.png').shape==(1080,1920,3)
    aa=read_alpha(folder/f'cam{k}_alpha.png');assert np.isfinite(aa).all()
    full_checked+=1
zeros=[]
for r in chk:
 assert 0<=float(r['paste_frac_fg'])<=float(r['core_frac_fg'])+1e-12
 if float(r['paste_frac_fg'])==0:
  m=f"hyb_tokchk_{r['check']}[{r['local_variant']}]";dif={k:max(abs(float(by[r['setup'],r['target'],m,reg][k])-float(by[r['setup'],r['target'],ref,reg][k])) for reg in ('fg','object','rest','risk','edge','oracle_fail')) for k in ('psnr','ssim','lpips','area_px','coverage')};assert max(dif.values())==0
  zeros.append(dict(setup=r['setup'],target=r['target'],variant=r['local_variant'],check=r['check'],all_six_regions_equal_reference=True))
cw(a/'eval/zero_paste_identity_checks.csv',zeros)
per={}
for r in rows:per.setdefault(r['setup']+'/'+r['target'],set()).add((r['method'],r['region']))
old=list(csv.DictReader((R/'results/mofang-9cam-round10-gspl-20261025/eval/metrics.csv').open()));oldref=[r for r in old if r['method']==ref];delta={k:max(abs(float(r[k])-float(by[r['setup'],r['target'],r['method'],r['region']][k])) for r in oldref) for k in ('psnr','lpips','area_px')}
extra=dict(rows_per_target={k:len(v) for k,v in per.items()},tto_local_views_explicitly_checked=checked,tto_full_views_explicitly_checked=full_checked,tto_core_masks_unchanged_count=sum(r['core_masks_equal'] for r in support),parallel_csvs_equal_worker_concatenation=True,tto_core_masks_changed_count=sum(not r['core_masks_equal'] for r in support),max_core_changed_pixels=max(r['core_changed_px'] for r in support),gaussian_membership_counts_equal=True,target_camera_validity_equal=True,tokchk_rows=len(chk),zero_paste_identity_checks=len(zeros),hybrid_coverage_min=min(float(r['coverage']) for r in rows if r['method'].startswith('hyb')),reference_vs_round10_max_abs_difference=delta,gs_reprojection_disabled=not bool(cfg['gs']['reproject']['geometries']))
(a/'eval/extra_validation.json').write_text(json.dumps(extra,indent=2)+'\n');print(json.dumps({'complete':True,'extra':extra}))

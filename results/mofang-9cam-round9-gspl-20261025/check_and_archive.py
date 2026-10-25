import os,sys,json,csv,shutil,hashlib,math
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parents[2];os.chdir(R);sys.path.insert(0,str(R))
from lgs.common import load_cfg,load_json,read_mask,setup_cams
from scripts.evaluate import read_alpha,paste_weight
w=R/'work/round9';a=R/'results/mofang-9cam-round9-gspl-20261025';a.mkdir(parents=True,exist_ok=True)
def cp(p,q):q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
def cw(p,rr):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w') as f:
  d=csv.DictWriter(f,fieldnames=list(rr[0]));d.writeheader();d.writerows(rr)
for p in (w/'eval').glob('*/*_montage.png'):cp(p,a/'eval'/p.relative_to(w/'eval'))
for folder in ('gs','flow','poses','prepare'):
 for p in (w/folder).rglob('*.json'):cp(p,a/folder/p.relative_to(w/folder))
for p in (w/'logs').iterdir():
 if p.is_file():cp(p,a/'logs'/p.name)
if not (w/'eval/validation.json').exists():
 print(json.dumps({'complete':False,'montages':len(list((a/'eval').glob('*/*_montage.png')))}));sys.exit()
for p in (w/'eval').iterdir():
 if p.is_file():cp(p,a/'eval'/p.name)
cfg=load_cfg('configs/mofang_9cam.yaml');rows=list(csv.DictReader((a/'eval/metrics.csv').open()));chk=list(csv.DictReader((a/'eval/tokchk.csv').open()));by={(r['setup'],r['target'],r['method'],r['region']):r for r in rows};ref=cfg['eval']['ref_flow'];stats=[];support=[];cores=[];depths=[];valid_variants=0
for s in cfg['setups']:
 ctx,targets=setup_cams(cfg,s)
 base=load_json(w/'gs'/s/'gs_tok448_nat_dil_al/meta.json')
 depths += [dict(setup=s,camera=k,median_relative_depth_difference=d,plane_rms_px=base['pose_diag']['plane_rms_px'],num_gaussians=base['num_gaussians'],window=base['window'][2],ctx_self_psnr=base['ctx_self_psnr'][i]) for i,(k,d) in enumerate(zip(ctx,base['vggt_vs_gs_depth_rel']))]
 for geom in cfg['gs']['reproject']['geometries']:
  sample=load_json(w/'gs'/s/f'gs_tokrife448_nat_dil_al_rp{geom}_local/meta.json')
  for st in sample['reproject_stats']:
   assert all(math.isfinite(st[k]) and 0<=st[k]<=1 for k in ('seen_by_both','seen_by_one','seen_by_none'))
   assert abs(sum(st[k] for k in ('seen_by_both','seen_by_one','seen_by_none'))-1)<1e-8
   stats.append(dict(setup=s,geometry=geom,**st))
 for v in cfg['tokens']['variants']:
  bn=f'gs_tok{v}448_nat_dil_al_local';bm=load_json(w/'gs'/s/bn/'meta.json')
  for k in targets:
   core=read_alpha(w/'gs'/s/bn/f'cam{k}_alpha_core.png')>.5;valid=read_mask(w/'gs'/s/bn/f'cam{k}_valid.png');core &=valid
   # Source evaluator also restricts core to the predicted flow foreground.
   from lgs.common import chroma_fg,dilate
   from scripts.evaluate import load_rgb
   flow=load_rgb(w/'flow'/s/ref/f'cam{k}.png');core &=dilate(chroma_fg(flow,cfg['chroma']),cfg['tokens']['paste_fg_dilate_px'])
   fg=read_mask(w/'prepare'/f'fg_aligned_{k:02d}.png');gsok=valid&(read_alpha(w/'gs'/s/bn/f'cam{k}_alpha.png')>.5);wg=paste_weight(core,gsok,cfg['tokens']['paste_feather_px'])
   for geom in ('gs','vggt'):
    rn=bn.replace('_local',f'_rp{geom}_local');rm=load_json(w/'gs'/s/rn/'meta.json')
    for key in ('num_gaussians','window','time_encode_s','ctx_self_psnr','local_gaussians'):assert rm[key]==bm[key],(s,v,key)
    p=w/'gs'/s/bn/f'cam{k}_alpha_core.png';q=w/'gs'/s/rn/p.name;core_equal=p.read_bytes()==q.read_bytes();assert core_equal
    p=w/'gs'/s/bn/f'cam{k}_valid.png';q=w/'gs'/s/rn/p.name;valid_equal=p.read_bytes()==q.read_bytes();assert valid_equal
    # validate_results.py checks original variants only; explicitly decode every RP artifact.
    from lgs.common import imread_rgb
    rgb=imread_rgb(w/'gs'/s/rn/f'cam{k}.png');assert rgb.shape==(1080,1920,3)
    ar=read_alpha(w/'gs'/s/rn/f'cam{k}_alpha.png');assert np.isfinite(ar).all() and ar.min()>=0 and ar.max()<=1
    ok=read_mask(q)&(ar>.5);wr=paste_weight(core,ok,cfg['tokens']['paste_feather_px'])
    support.append(dict(setup=s,target=k,variant=v,geometry=geom,core_px=int(core.sum()),core_available_gs_fraction=float((core&gsok).sum()/max(core.sum(),1)),core_available_rp_fraction=float((core&ok).sum()/max(core.sum(),1)),gs_effective_fg_fraction=float(((wg>1e-6)&fg).sum()/fg.sum()),rp_effective_fg_fraction=float(((wr>1e-6)&fg).sum()/fg.sum()),weight_max_abs_difference=float(np.max(np.abs(wr-wg))),weight_mean_abs_difference=float(np.mean(np.abs(wr-wg)))))
    cores.append(dict(setup=s,target=k,variant=v,geometry=geom,alpha_core_byte_identical=core_equal,valid_byte_identical=valid_equal));valid_variants+=1
cw(a/'eval/depth_agreement.csv',depths);cw(a/'eval/reproject_visibility.csv',stats);cw(a/'eval/paste_support.csv',support);cw(a/'eval/core_identity_checks.csv',cores)
per={}
for r in rows:per.setdefault(r['setup']+'/'+r['target'],set()).add((r['method'],r['region']))
zeros=[]
for r in chk:
 assert 0<=float(r['paste_frac_fg'])<=float(r['core_frac_fg'])+1e-12
 if float(r['paste_frac_fg'])==0:
  m=f"hyb_tokchk_{r['check']}[{r['local_variant']}]";dif={k:max(abs(float(by[(r['setup'],r['target'],m,reg)][k])-float(by[(r['setup'],r['target'],ref,reg)][k])) for reg in ('fg','object','rest','risk','edge','oracle_fail')) for k in ('psnr','ssim','lpips','area_px','coverage')};assert max(dif.values())==0
  zeros.append(dict(setup=r['setup'],target=r['target'],variant=r['local_variant'],check=r['check'],all_six_regions_equal_reference=True))
cw(a/'eval/zero_paste_identity_checks.csv',zeros)
old=list(csv.DictReader((R/'results/mofang-9cam-round8-gspl-20261025/eval/metrics.csv').open()));oldref=[r for r in old if r['method']==ref];refdelta={k:max(abs(float(r[k])-float(by[r['setup'],r['target'],r['method'],r['region']][k])) for r in oldref) for k in ('psnr','lpips','area_px')}
extra=dict(rows_per_target={k:len(v) for k,v in per.items()},reprojection_views_explicitly_checked=valid_variants,core_identity_checks=len(cores),core_and_valid_png_byte_identical=True,tokchk_rows=len(chk),zero_paste_identity_checks=len(zeros),visibility_stats_rows=len(stats),hybrid_coverage_min=min(float(r['coverage']) for r in rows if r['method'].startswith('hyb')),reference_vs_round8_max_abs_difference=refdelta,actual_blend_weights_identical_for_all_pairs=all(r['weight_max_abs_difference']==0 for r in support),gs_rerun=True,tokens_rerun=False)
(a/'eval/extra_validation.json').write_text(json.dumps(extra,indent=2)+'\n');print(json.dumps({'complete':True,'extra':extra}))

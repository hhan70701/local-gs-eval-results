import os,sys,json,shutil,csv,math,tarfile,hashlib
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parents[2];os.chdir(R);sys.path.insert(0,str(R))
from lgs.common import load_cfg,read_mask,chroma_fg,dilate,imread_rgb,setup_cams
w=R/'work/round7';a=R/'results/mofang-9cam-round7-gspl-20261025';a.mkdir(parents=True,exist_ok=True)
def copy(p,q):
 q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
def csvwrite(path,rr):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('w') as f:
  d=csv.DictWriter(f,fieldnames=list(rr[0]));d.writeheader();d.writerows(rr)
for p in (w/'eval').glob('*/*_montage.png'):copy(p,a/'eval'/p.relative_to(w/'eval'))
for folder in ('gs','flow','poses','prepare'):
 for p in (w/folder).rglob('*'):
  if p.is_file() and (p.suffix=='.json' or (folder=='prepare' and p.suffix=='.npy')):copy(p,a/folder/p.relative_to(w/folder))
for p in (w/'logs').iterdir():
 if p.is_file():copy(p,a/'logs'/p.name)
tokfile=w/'tokens/tokens.json'
if tokfile.exists():
 copy(tokfile,a/'tokens/tokens.json')
 for p in (w/'tokens').glob('*/*/*_overlay.png'):copy(p,a/'tokens'/p.relative_to(w/'tokens'))
 archive=a/'tokens/all_masks.tar.gz'
 if not archive.exists():
  masks=sorted(p for p in (w/'tokens').rglob('*.png') if not p.name.endswith('_overlay.png'))
  with tarfile.open(archive,'w:gz') as tar:
   for p in masks:tar.add(p,arcname=str(p.relative_to(w/'tokens')),recursive=False)
  manifest=[dict(path=str(p.relative_to(w/'tokens')),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),size=p.stat().st_size) for p in masks]
  (a/'tokens/masks_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
  with tarfile.open(archive) as tar:
   assert all(hashlib.sha256(tar.extractfile(m['path']).read()).hexdigest()==m['sha256'] for m in manifest)
metas={s:{p.parent.name:json.loads(p.read_text()) for p in (w/'gs'/s).glob('*/meta.json')} for s in ('cam3','cam5')}
counts=[]
for s,mm in metas.items():
 for name,m in mm.items():
  if m.get('local') and m['pose_source']=='aligned_int':
   for pair,cc in m['local_gaussians'].items():
    assert 0<=cc['core']<=cc['recon']<=m['num_gaussians']
    counts.append(dict(setup=s,variant=m['token_variant'],pair=pair,window=m['window'][2],total=m['num_gaussians'],recon=cc['recon'],core=cc['core'],plane_rms_px=m['pose_diag']['plane_rms_px'],ctx_self_psnr=float(np.mean(m['ctx_self_psnr']))))
if counts:csvwrite(a/'eval/local_counts_and_plane.csv',counts)
if not (w/'eval/validation.json').exists():
 print(json.dumps({'complete':False,'encodings':{s:len({m['window'][2] for m in mm.values()}) for s,mm in metas.items()},'local_pair_rows':len(counts),'montages':len(list((a/'eval').glob('*/*_montage.png')))}));sys.exit()
for p in (w/'eval').iterdir():
 if p.is_file():copy(p,a/'eval'/p.name)
cfg=load_cfg('configs/mofang_9cam.yaml');geo=[];tok=json.loads(tokfile.read_text());gated=[]
metrics=list(csv.DictReader((a/'eval/metrics.csv').open()));paste=list(csv.DictReader((a/'eval/paste.csv').open()))
for s,mm in metas.items():
 ctx,targets=setup_cams(cfg,s)
 shared_keys=('window','num_gaussians','time_encode_s','ctx_self_psnr','sim3_scale')
 for key in shared_keys:assert all(m[key]==next(iter(mm.values()))[key] for m in mm.values()),(s,key)
 assert len({m['token_window'] for m in mm.values()})==1
 for k in targets:
  valid=np.ones((1080,1920),bool)
  for n,m in mm.items():
   if m['crop'] in ('center','fg'):valid &=read_mask(w/'gs'/s/n/f'cam{k}_valid.png')
  fg=read_mask(w/'prepare'/f'fg_aligned_{k:02d}.png')&valid
  ref=imread_rgb(w/'flow'/s/cfg['eval']['ref_flow']/f'cam{k}.png').astype(np.float32)/255
  pa,pb=max(c for c in ctx if c<k),min(c for c in ctx if c>k);pair=f'{pa}-{pb}'
  for n,m in mm.items():
   if not m.get('local'):continue
   core=read_mask(w/'gs'/s/n/f'cam{k}_alpha_core.png')&read_mask(w/'gs'/s/n/f'cam{k}_valid.png')
   core &=dilate(chroma_fg(ref,cfg['chroma']),cfg['tokens']['paste_fg_dilate_px'])
   v=m['token_variant'];info=tok['pairs'][v][s][pair]
   geo.append(dict(setup=s,target=k,variant=v,pair=pair,gated=info['gated'],pose_source=m['pose_source'],pair_input_core=info['core'],core_area_px=int(core.sum()),core_total_over_fg=core.sum()/fg.sum(),foreground_replaced_fraction=(core&fg).sum()/fg.sum(),outside_fg_fraction=(core&~fg).sum()/max(core.sum(),1)))
   if info['gated']:
    assert not core.any();assert m['local_gaussians'][pair]=={'recon':0,'core':0}
    for kind in ('hyb_token','hyb_token_ringreg'):
     meth=f'{kind}[{n}]'
     mr=[r for r in metrics if r['setup']==s and r['target']==str(k) and r['method']==meth]
     fr={r['region']:r for r in metrics if r['setup']==s and r['target']==str(k) and r['method']==cfg['eval']['ref_flow']}
     assert len(mr)==6
     assert all(all(float(r[key])==float(fr[r['region']][key]) for key in ('psnr','ssim','lpips','area_px','coverage')) for r in mr)
    gated.append(dict(setup=s,target=k,variant=v,pose_source=m['pose_source'],pair=pair,metrics_equal_reference=True,alpha_core_zero=True))
csvwrite(a/'eval/paste_geometry.csv',geo);csvwrite(a/'eval/gated_identity_checks.csv',gated)
for r in paste:
 for k in ('psnr','ssim','lpips','paste_area_frac_fg'):assert math.isfinite(float(r[k])),r
per={}
for r in metrics:per.setdefault(r['setup']+'/'+r['target'],set()).add((r['method'],r['region']))
old_metrics=list(csv.DictReader((R/'results/mofang-9cam-round6-gspl-20261025/eval/metrics.csv').open()));old_ref={(r['setup'],r['target'],r['region']):r for r in old_metrics if r['method']==cfg['eval']['ref_flow']};new_ref=[r for r in metrics if r['method']==cfg['eval']['ref_flow']]
extra=dict(rows_per_target={k:len(v) for k,v in per.items()},paste_rows=len(paste),ring_rows=sum(1 for _ in csv.DictReader((a/'eval/token_ringreg.csv').open())),hybrid_coverage_min=min(float(r['coverage']) for r in metrics if r['method'].startswith('hyb')),gated_identity_checks=len(gated),shared_encoding_metadata_equal=True,shared_t_exact=True,local_count_order='0 <= core <= recon <= total (count check only)',mask_archive_sha256=hashlib.sha256((a/'tokens/all_masks.tar.gz').read_bytes()).hexdigest(),reference_vs_round6_max_abs_difference={k:max(abs(float(r[k])-float(old_ref[r['setup'],r['target'],r['region']][k])) for r in new_ref) for k in ('psnr','lpips','area_px')})
for s in ('cam3','cam5'):
 p=json.loads((w/'poses'/f'{s}.json').read_text())
 for scale in ('1.0','0.5'):
  f=json.loads((w/'flow'/s/f'flow_s{scale}_pose/meta.json').read_text());assert all(v['t']==p['t_pose'][k] for k,v in f.items())
(a/'eval/extra_validation.json').write_text(json.dumps(extra,indent=2)+'\n')
print(json.dumps({'complete':True,'extra':extra}))

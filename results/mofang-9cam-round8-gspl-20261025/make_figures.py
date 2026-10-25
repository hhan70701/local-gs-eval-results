"""Render fixed-method scientific comparison panels from reused round7 predictions; no inference."""
import os,sys
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parents[2];os.chdir(R);sys.path.insert(0,str(R));os.environ['LGS_WORK_DIR']='work/round8'
from lgs.common import load_cfg,load_json,read_mask,chroma_fg,dilate,imread_rgb,imwrite,bbox,cube_mask,setup_cams,cam_path
from scripts.evaluate import load_rgb,read_alpha,risk_from_signals,paste_weight,blend_w,tile,grid
cfg=load_cfg('configs/mofang_9cam.yaml');w=Path(cfg['work_dir']);a=R/'results/mofang-9cam-round8-gspl-20261025';ref=cfg['eval']['ref_flow'];checks={c['name']:c for c in cfg['eval']['target_check']}
for s in cfg['setups']:
 gv='gs_tokrife448_nat_dil_al_local'
 for k in setup_cams(cfg,s)[1]:
  gt=load_rgb(cam_path(cfg,'aligned',k));flow=load_rgb(w/'flow'/s/ref/f'cam{k}.png');gs=load_rgb(w/'gs'/s/gv/f'cam{k}.png');ok=(read_alpha(w/'gs'/s/gv/f'cam{k}_alpha.png')>.5)&read_mask(w/'gs'/s/gv/f'cam{k}_valid.png')
  core=(read_alpha(w/'gs'/s/gv/f'cam{k}_alpha_core.png')>.5)&read_mask(w/'gs'/s/gv/f'cam{k}_valid.png');core &=dilate(chroma_fg(flow,cfg['chroma']),cfg['tokens']['paste_fg_dilate_px'])
  near=dilate(chroma_fg(flow,cfg['chroma']),cfg['risk']['fg_dilate_px'])
  with np.load(w/'flow'/s/ref/f'cam{k}_signals.npz') as z:sig={n:z[n].astype(np.float32) for n in ('r_warp','r_col')}
  preds={'flow':flow,'token':blend_w(flow,gs,paste_weight(core,ok,cfg['tokens']['paste_feather_px']))}
  sels={}
  for n in ('w08','w20'):
   c=checks[n];risk=risk_from_signals(sig,near,c['warp'],c['col'],dict(cfg['risk'],dilate_px=c['dilate_px']));sels[n]=core & risk;preds[n]=blend_w(flow,gs,paste_weight(sels[n],ok,cfg['tokens']['paste_feather_px']))
  box=bbox(cube_mask(gt,cfg['chroma']),100)
  if box is None:box=bbox(chroma_fg(gt,cfg['chroma']),20)
  panels=[tile('GT',gt,box,260)]+[tile(n+' (rife)',preds[n],box,260) for n in ('flow','token','w08','w20')]
  ov=gt.copy();ov[core]=.5*ov[core]+.5*np.array([0,.3,1],np.float32);ov[sels['w08']]=.5*ov[sels['w08']]+.5*np.array([1,0,0],np.float32)
  panels += [tile('blue=core red=w08 selection',ov,box,260)]+[tile('|err| '+n+' x3',np.repeat(np.abs(preds[n]-gt).mean(-1,keepdims=True)*3,3,-1),box,260) for n in ('flow','token','w08','w20')]
  out=a/'figures'/s/f'cam{k}_rife_w08_w20.png';imwrite(out,grid(panels,5));print(out.relative_to(a),flush=True)

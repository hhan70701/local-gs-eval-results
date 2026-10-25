"""Fixed rife scientific comparison panels from saved outputs; no new model inference."""
import os,sys
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parents[2];os.chdir(R);sys.path.insert(0,str(R));os.environ['LGS_WORK_DIR']='work/round9'
from lgs.common import load_cfg,read_mask,chroma_fg,dilate,imwrite,bbox,cube_mask,setup_cams,cam_path
from scripts.evaluate import load_rgb,read_alpha,paste_weight,blend_w,tile,grid
cfg=load_cfg('configs/mofang_9cam.yaml');w=Path(cfg['work_dir']);a=R/'results/mofang-9cam-round9-gspl-20261025';ref=cfg['eval']['ref_flow']
for s in cfg['setups']:
 base='gs_tokrife448_nat_dil_al_local'
 for k in setup_cams(cfg,s)[1]:
  gt=load_rgb(cam_path(cfg,'aligned',k));flow=load_rgb(w/'flow'/s/ref/f'cam{k}.png');core=(read_alpha(w/'gs'/s/base/f'cam{k}_alpha_core.png')>.5)&read_mask(w/'gs'/s/base/f'cam{k}_valid.png');core &=dilate(chroma_fg(flow,cfg['chroma']),cfg['tokens']['paste_fg_dilate_px'])
  preds={'flow':flow};availability={}
  for n,suf in [('GS color',''),('GS depth + input','_rpgs'),('VGGT depth + input','_rpvggt')]:
   gv=base.replace('_local',suf+'_local');p=load_rgb(w/'gs'/s/gv/f'cam{k}.png');ok=(read_alpha(w/'gs'/s/gv/f'cam{k}_alpha.png')>.5)&read_mask(w/'gs'/s/gv/f'cam{k}_valid.png');availability[n]=ok;preds[n]=blend_w(flow,p,paste_weight(core,ok,cfg['tokens']['paste_feather_px']))
  box=bbox(cube_mask(gt,cfg['chroma']),100) or bbox(chroma_fg(gt,cfg['chroma']),20)
  names=['flow','GS color','GS depth + input','VGGT depth + input'];panels=[tile('GT',gt,box,260)]+[tile(n,preds[n],box,260) for n in names]
  ov=gt.copy();ov[core]=.5*ov[core]+.5*np.array([0,.3,1],np.float32);holes=core & ~availability['GS depth + input'];ov[holes]=.5*ov[holes]+.5*np.array([1,0,0],np.float32)
  panels +=[tile('blue=core red=RP-GS unavailable',ov,box,260)]+[tile('|err| '+n+' x3',np.repeat(np.abs(preds[n]-gt).mean(-1,keepdims=True)*3,3,-1),box,260) for n in names]
  out=a/'figures'/s/f'cam{k}_rife_color_sources.png';imwrite(out,grid(panels,5));print(out.relative_to(a),flush=True)

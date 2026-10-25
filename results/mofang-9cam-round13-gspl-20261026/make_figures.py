"""Fixed rife panels for every configured checkpoint, using saved predictions only."""
import os,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];os.chdir(R);sys.path.insert(0,str(R));os.environ['LGS_WORK_DIR']='work/round13'
from lgs.common import load_cfg,read_mask,chroma_fg,dilate,imwrite,bbox,cube_mask,setup_cams,cam_path,load_json
from scripts.evaluate import load_rgb,read_alpha,paste_weight,blend_w,tile,grid
cfg=load_cfg('configs/mofang_9cam_lean.yaml');w=Path(cfg['work_dir']);a=R/'results/mofang-9cam-round13-gspl-20261026';ref=cfg['eval']['ref_flow']
for s in cfg['setups']:
 base='gs_tokrife448_nat_dil_al_local';meta=load_json(w/'gs'/s/'gs_tokrife448_nat_dil_al_local/meta.json');times={x['iter']:x['time_s'] for x in meta['tto']['log'] if 'time_s' in x}
 for k in setup_cams(cfg,s)[1]:
  gt=load_rgb(cam_path(cfg,'aligned',k));flow=load_rgb(w/'flow'/s/ref/f'cam{k}.png');near=dilate(chroma_fg(flow,cfg['chroma']),cfg['tokens']['paste_fg_dilate_px']);box=bbox(cube_mask(gt,cfg['chroma']),100) or bbox(chroma_fg(gt,cfg['chroma']),20)
  panels=[tile('GT',gt,box,260),tile('flow',flow,box,260)]
  for it in [0]+cfg['gs']['tto']['checkpoints']:
   gv=base.replace('_local',(f'_tto{it}' if it else '')+'_local');v=read_mask(w/'gs'/s/gv/f'cam{k}_valid.png');core=(read_alpha(w/'gs'/s/gv/f'cam{k}_alpha_core.png')>.5)&v&near;p=load_rgb(w/'gs'/s/gv/f'cam{k}.png');ok=(read_alpha(w/'gs'/s/gv/f'cam{k}_alpha.png')>.5)&v;pred=blend_w(flow,p,paste_weight(core,ok,cfg['tokens']['paste_feather_px']))
   name='FF' if not it else f'TTO {it} ({times[it]:.2f}s)';panels.append(tile(name,pred,box,260))
  out=a/'figures'/s/f'cam{k}_rife_checkpoints.png';imwrite(out,grid(panels,4));print(out.relative_to(a),flush=True)

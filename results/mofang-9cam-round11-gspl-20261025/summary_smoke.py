import csv,json,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT))
from scripts.evaluate import write_summary
from lgs.common import load_cfg
w=ROOT/'work/round10';cfg=load_cfg(ROOT/'configs/mofang_9cam.yaml')
def read(name,types):
 with (w/'eval'/name).open() as f:
  r=csv.reader(f);next(r);return [[t(v) for t,v in zip(types,row)] for row in r]
rows=read('metrics.csv',[str,int,str,str,float,float,float,int,float,float]);auc=read('auc.csv',[str,int,str,float,float]);paste=read('paste.csv',[str,int,str,str,float,float,float,float]);token=read('token_ringreg.csv',[str,int,str,float,float]);chk=read('tokchk.csv',[str,int,str,str,float,float]);sweep=read('risk_sweep.csv',[str,float,float,float,float,float,float]);reg=read('registration.csv',[str,int,str,float,lambda v:v=='True'])
tuned={s:max([r for r in sweep if r[0]==s],key=lambda r:r[5])[1:3] for s in ('cam3','cam5')}
info={s:json.loads((w/'gs'/s/'gs_tok448_nat_dil_al/meta.json').read_text())['tto'] for s in ('cam3','cam5')}
with tempfile.TemporaryDirectory() as d:
 p=Path(d)/'summary.md';write_summary(p,rows,auc,[],[],reg,sweep,tuned,cfg['risk'],cfg['eval']['ref_flow'],paste,token,json.loads((w/'tokens/tokens.json').read_text()),chk,info,'rife')
 assert '测试时优化：步数–耗时–质量' in p.read_text()
print('PASS: full summary renders from historical real CSVs with explicit TTO report arguments')

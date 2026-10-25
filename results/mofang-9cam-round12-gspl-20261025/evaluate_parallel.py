"""Evaluate independent setups concurrently, then merge raw CSVs and call upstream summary writer."""
import csv,json,os,re,shutil,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];os.chdir(ROOT);sys.path.insert(0,str(ROOT))
BASE=ROOT/'work/round12';jobs={};handles=[]
for setup in ('cam3','cam5'):
 work=BASE/'eval_jobs'/setup;work.mkdir(parents=True,exist_ok=True)
 for folder in ('prepare','flow','poses','tokens','gs','compat_packages'):
  p=work/folder
  if not p.exists():p.symlink_to(BASE/folder,target_is_directory=True)
 env=os.environ.copy();env['LGS_WORK_DIR']=str(work)
 log=(BASE/'logs'/f'3_evaluate_{setup}.log').open('w');handles.append(log)
 jobs[setup]=(subprocess.Popen([sys.executable,str(Path(__file__).with_name('evaluate_worker.py')),'--config',str(ROOT/'configs/mofang_9cam_lean.yaml'),'--setups',setup],env=env,stdout=log,stderr=subprocess.STDOUT),work)
while True:
 status={}
 for setup,(p,work) in jobs.items():
  text=(BASE/'logs'/f'3_evaluate_{setup}.log').read_text();lines=text.splitlines()
  status[setup]=dict(exit=p.poll(),completed_targets=sum(bool(re.match(r'^\[cam[35]\] cam\d+:',x)) for x in lines),last=lines[-1] if lines else '')
 print(json.dumps(status,ensure_ascii=False),flush=True)
 if all(p.poll() is not None for p,_ in jobs.values()):break
 time.sleep(20)
for h in handles:h.close()
assert all(p.returncode==0 for p,_ in jobs.values()),status
out=BASE/'eval';out.mkdir(exist_ok=True)
for name in ('metrics.csv','auc.csv','registration.csv','risk_sweep.csv','paste.csv','tokchk.csv','token_ringreg.csv'):
 with (out/name).open('w',newline='') as fd:
  writer=csv.writer(fd);header=None
  for setup,(p,work) in jobs.items():
   with (work/'eval'/name).open(newline='') as sf:
    rd=csv.reader(sf);h=next(rd)
    if header is None:header=h;writer.writerow(h)
    assert h==header,(name,setup)
    writer.writerows(rd)
for setup,(p,work) in jobs.items():shutil.copytree(work/'eval'/setup,out/setup,dirs_exist_ok=True)
payloads=[json.loads((work/'eval/summary_payload.json').read_text()) for _,work in jobs.values()]
merged=dict(payloads[0])
for key in ('rows','auc_rows','t_rows','gs_rows','reg_rows','sweep_rows','paste_rows','token_rows','chk_rows'):merged[key]=sum([p[key] for p in payloads],[])
for key in ('tuned','tto_info'):merged[key]={k:v for p in payloads for k,v in p[key].items()}
for key in ('rcfg','ref','token_report','tto_main_variant'):assert all(p[key]==payloads[0][key] for p in payloads),key
from scripts.evaluate import write_summary
write_summary(out/'summary.md',**merged)
print('Merged independent setup CSVs and upstream summary -> '+str(out),flush=True)

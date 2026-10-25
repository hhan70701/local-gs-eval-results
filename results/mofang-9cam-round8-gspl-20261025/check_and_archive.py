import os,sys,json,shutil,csv,math
from pathlib import Path
R=Path(__file__).resolve().parents[2];os.chdir(R);sys.path.insert(0,str(R))
from lgs.common import setup_cams
w=R/'work/round8';a=R/'results/mofang-9cam-round8-gspl-20261025';a.mkdir(parents=True,exist_ok=True)
def copy(p,q):
 q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
for p in (w/'eval').glob('*/*_montage.png'):copy(p,a/'eval'/p.relative_to(w/'eval'))
for p in (w/'logs').iterdir():
 if p.is_file():copy(p,a/'logs'/p.name)
if not (w/'eval/validation.json').exists():
 print(json.dumps({'complete':False,'montages':len(list((a/'eval').glob('*/*_montage.png')))}));sys.exit()
for p in (w/'eval').iterdir():
 if p.is_file():copy(p,a/'eval'/p.name)
rows=list(csv.DictReader((a/'eval/metrics.csv').open()));chk=list(csv.DictReader((a/'eval/tokchk.csv').open()));old=list(csv.DictReader((R/'results/mofang-9cam-round7-gspl-20261025/eval/metrics.csv').open()));cfg=json.loads((a/'environment.json').read_text())['config'];ref=cfg['eval']['ref_flow'];names={c['name'] for c in cfg['eval']['target_check']}|{'oracle'};variants=set(cfg['tokens']['variants']);per={}
def key(r):return r['setup'],r['target'],r['method'],r['region']
by={key(r):r for r in rows};assert len(by)==len(rows)
for r in rows:per.setdefault(r['setup']+'/'+r['target'],set()).add((r['method'],r['region']))
assert len(chk)==sum(len(setup_cams(cfg,s)[1]) for s in cfg['setups'])*len(variants)*len(names)
assert len({(r['setup'],r['target'],r['local_variant'],r['check']) for r in chk})==len(chk)
for r in chk:
 assert r['check'] in names and r['local_variant'].endswith('_al_local')
 assert 0<=float(r['paste_frac_fg'])<=float(r['core_frac_fg'])+1e-12
 assert all(math.isfinite(float(r[k])) for k in ('core_frac_fg','paste_frac_fg'))
old_delta={k:max(abs(float(r[k])-float(by[key(r)][k])) for r in old) for k in ('psnr','ssim','lpips','area_px','coverage')}
zeros=[]
for r in chk:
 m=f"hyb_tokchk_{r['check']}[{r['local_variant']}]"
 assert all(float(by[(r['setup'],r['target'],m,reg)]['coverage'])==1 for reg in ('fg','object','rest','risk','edge','oracle_fail'))
 if float(r['paste_frac_fg'])==0:
  dif={k:max(abs(float(by[(r['setup'],r['target'],m,reg)][k])-float(by[(r['setup'],r['target'],ref,reg)][k])) for reg in ('fg','object','rest','risk','edge','oracle_fail')) for k in ('psnr','ssim','lpips','area_px','coverage')}
  assert max(dif.values())==0,(r,dif)
  zeros.append(dict(setup=r['setup'],target=r['target'],variant=r['local_variant'],check=r['check'],all_six_regions_exact_reference=True))
with (a/'eval/zero_paste_identity_checks.csv').open('w') as f:
 d=csv.DictWriter(f,fieldnames=list(zeros[0]));d.writeheader();d.writerows(zeros)
extra=dict(rows_per_target={k:len(v) for k,v in per.items()},tokchk_rows=len(chk),tokchk_methods=len(variants)*len(names),zero_paste_identity_checks=len(zeros),old_round7_rows_compared=len(old),old_round7_max_abs_difference=old_delta,hybrid_coverage_min=min(float(r['coverage']) for r in rows if r['method'].startswith('hyb')),target_check_only_al_local=True,paste_area_bounded_by_core=True,source_code_modified=False,gs_or_tokens_rerun=False)
(a/'eval/extra_validation.json').write_text(json.dumps(extra,indent=2)+'\n')
print(json.dumps({'complete':True,'extra':extra}))

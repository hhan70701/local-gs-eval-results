from pathlib import Path
import csv,json,statistics
R=Path(__file__).resolve().parents[2];a=R/'results/mofang-9cam-round8-gspl-20261025';e=a/'eval'
rows=list(csv.DictReader((e/'metrics.csv').open()));chk=list(csv.DictReader((e/'tokchk.csv').open()));val=json.loads((e/'validation.json').read_text());extra=json.loads((e/'extra_validation.json').read_text());env=json.loads((a/'environment.json').read_text());cfg=env['config'];ref=cfg['eval']['ref_flow'];variants=list(cfg['tokens']['variants']);checks=['none']+[c['name'] for c in cfg['eval']['target_check']]+['oracle'];targets={s:sorted({int(r['target']) for r in rows if r['setup']==s}) for s in cfg['setups']}
by={(r['setup'],int(r['target']),r['method'],r['region']):r for r in rows};areas={(r['setup'],int(r['target']),r['local_variant'],r['check']):r for r in chk}
def meth(v,c):
 gv=f'gs_tok{v}448_nat_dil_al_local';return f'hyb_token[{gv}]' if c=='none' else f'hyb_tokchk_{c}[{gv}]'
def mean(s,m,reg,k):return statistics.mean(float(by[(s,t,m,reg)][k]) for t in targets[s])
def cw(p,rr):
 with p.open('w') as f:
  d=csv.DictWriter(f,fieldnames=list(rr[0]));d.writeheader();d.writerows(rr)
summ=[];per=[]
for s in targets:
 for v in variants:
  gv=f'gs_tok{v}448_nat_dil_al_local'
  for c in checks:
   m=meth(v,c);rr=[]
   for t in targets[s]:
    ar=areas[(s,t,gv,checks[1] if c=='none' else c)];r=dict(setup=s,target=t,variant=v,check=c,uses_gt=(c=='oracle'),paste_frac_fg=float(ar['core_frac_fg'] if c=='none' else ar['paste_frac_fg']))
    for reg in ('fg','object','rest'):
     for k in ('psnr','lpips'):
      r[f'{reg}_{k}']=float(by[s,t,m,reg][k]);r[f'{reg}_delta_{k}']=r[f'{reg}_{k}']-float(by[s,t,ref,reg][k])
    r['fg_not_worse']=r['fg_delta_psnr']>=-1e-6 and r['fg_delta_lpips']<=1e-6;r['fg_strict_both_better']=r['fg_delta_psnr']>1e-6 and r['fg_delta_lpips']<-1e-6;per.append(r);rr.append(r)
   q=dict(setup=s,variant=v,check=c,uses_gt=(c=='oracle'),mean_paste_frac_fg=statistics.mean(r['paste_frac_fg'] for r in rr),zero_paste_targets=sum(r['paste_frac_fg']==0 for r in rr),fg_not_worse_targets=sum(r['fg_not_worse'] for r in rr),fg_both_better_targets=sum(r['fg_strict_both_better'] for r in rr),targets=len(rr))
   for reg in ('fg','object','rest'):
    for k in ('psnr','lpips'):
     q[f'{reg}_{k}']=mean(s,m,reg,k);q[f'{reg}_delta_{k}']=q[f'{reg}_{k}']-mean(s,ref,reg,k)
   summ.append(q)
cw(e/'target_check_comparison.csv',summ);cw(e/'target_check_per_view.csv',per)
L=['# 第八轮实测：目标侧光流风险复核','',
'源代码：`luckyhan-mike/local-gs-eval@8d7cf85`。工作目录 `work/round8`，目录命名沿用主机启动日期20261025。本轮按上游默认配置**仅运行evaluate/validate和既有数值测试，未重新检测token、未重跑AnySplat或光流**，没有修改算法、阈值或评价代码。','',
'## 主结果','',
'**目标侧复核带来有限改善，但25组固定的非oracle候选没有同时满足cam3全部目标不差与cam5前景双指标均值不降。** 例如rife/w20的cam3为26.106 dB / 0.053360，5/6目标不差，仍未达到6/6；cam5为27.740 / 0.040921，仍低于光流28.000 / 0.039572。oracle在cam3达到6/6，但cam5的oracle也未超过光流，不能把剩余问题全部归因于风险阈值。','',
'各目标相机等权平均，PSNR↑、LPIPS↓；所有新方法固定使用 `_al_local`。none为第七轮直接token贴回；oracle使用目标真值，仅是诊断。新方法候选全部列出，不按每个视点选最优。','',
'### 重点：未加面积门限的 rife','',
'| 设置 | 复核 | 贴回区 / fg | fg PSNR | fg LPIPS | object PSNR | object LPIPS | rest PSNR | fg不差目标数 |','|---|---|---:|---:|---:|---:|---:|---:|---:|']
for s in targets:
 L.append(f'| {s} | 纯光流 | — | {mean(s,ref,"fg","psnr"):.6f} | {mean(s,ref,"fg","lpips"):.6f} | {mean(s,ref,"object","psnr"):.6f} | {mean(s,ref,"object","lpips"):.6f} | {mean(s,ref,"rest","psnr"):.6f} | — |')
 for q in summ:
  if q['setup']==s and q['variant']=='rife':L.append(f"| {s} | {q['check']} | {q['mean_paste_frac_fg']:.3%} | {q['fg_psnr']:.6f} | {q['fg_lpips']:.6f} | {q['object_psnr']:.6f} | {q['object_lpips']:.6f} | {q['rest_psnr']:.6f} | {q['fg_not_worse_targets']}/{q['targets']} |")
L+=['','## 对照 README 判据（Codex 分析）','',
'不差目标数沿用上游容差：每目标fg ΔPSNR≥−1e−6且ΔLPIPS≤1e−6。包含零贴回时的精确回退，所以必须同时看剩余收益和面积，不能只看不差个数。','']
for c in checks[1:-1]:
 q3=next(q for q in summ if q['setup']=='cam3' and q['variant']=='rife' and q['check']==c);q5=next(q for q in summ if q['setup']=='cam5' and q['variant']=='rife' and q['check']==c)
 ok=q3['fg_not_worse_targets']==q3['targets'] and q5['fg_delta_psnr']>=-1e-6 and q5['fg_delta_lpips']<=1e-6
 L.append(f"- rife / {c}：cam3 {q3['fg_psnr']:.6f} dB / {q3['fg_lpips']:.6f}，{q3['fg_not_worse_targets']}/6不差；cam5 ΔPSNR={q5['fg_delta_psnr']:+.6f}、ΔLPIPS={q5['fg_delta_lpips']:+.8f}。{'满足' if ok else '未同时满足'}cam3全部目标不差与cam5前景均值双指标不降。cam3是否保留约26 dB量级收益请结合实际数值判断。")
cross=[]
for v in variants:
 for c in checks[1:-1]:
  x=next(q for q in summ if q['setup']=='cam3' and q['variant']==v and q['check']==c);y=next(q for q in summ if q['setup']=='cam5' and q['variant']==v and q['check']==c)
  if x['fg_not_worse_targets']==x['targets'] and y['fg_delta_psnr']>=-1e-6 and y['fg_delta_lpips']<=1e-6:cross.append(f"{v}/{c}（cam3 {x['fg_psnr']:.4f} dB / {x['fg_lpips']:.6f}，cam5 {y['fg_psnr']:.4f} / {y['fg_lpips']:.6f}）")
L+=['','全部25组固定、非oracle候选中，满足上述逐目标/均值条件的候选：'+('；'.join(cross) if cross else '**无**')+'。这不是部署时的自适应选择规则；同一帧上扫描后的候选排序仍需独立数据验证。','',
'## 逐视点：rife 的 fg ΔPSNR / ΔLPIPS','',
'| 设置 | 目标 | '+ ' | '.join(checks)+' |','|---|---:|'+'---:|'*len(checks)]
for s in targets:
 for t in targets[s]:
  rr=[q for q in per if q['setup']==s and q['target']==t and q['variant']=='rife'];cells=[]
  for c in checks:
   q=next(x for x in rr if x['check']==c);cells.append(f"{q['fg_delta_psnr']:+.6f} / {q['fg_delta_lpips']:+.6f}"+(' (空)' if q['paste_frac_fg']==0 else ''))
  L.append(f'| {s} | {t} | '+' | '.join(cells)+' |')
L+=['','全部token变体的逐视点fg/object/rest及贴回面积见 [target_check_per_view.csv](eval/target_check_per_view.csv)，所有固定策略均值见 [target_check_comparison.csv](eval/target_check_comparison.csv)。','',
'## 全部目标侧复核表（上游输出）','']
summary=(e/'summary.md').read_text();L.append('### 目标侧光流风险复核'+summary.split('### 目标侧光流风险复核',1)[1].split('## 其余诊断',1)[0])
L+=['## 固定方法对比图','',
'上游cam*_montage.png仍只展示旧的token/ringreg分支，并未显示新tokchk方法。本报告另生成10张固定使用rife的对比图：GT、光流、none、w08、w20，下方为core/选择区及×3平均绝对误差。没有按真值选择要展示的阈值或token变体；真值仅用于定位展示裁片和误差图，不参与w08/w20决策。','',
'例如 [cam3/目标3](figures/cam3/cam3_rife_w08_w20.png)、[cam5/目标3](figures/cam5/cam3_rife_w08_w20.png)。其余图片在figures/cam3和figures/cam5中；图像只展示物体附近局部，完整fg/rest结论以数值表为准。','',
'## 运行与附加检查','',
f"- 12项既有数值测试通过。上游验证{val['status']}：{val['metric_rows']}行质量指标、{val['methods']}种方法、{val['auc_rows']}行AUC、{val['gs_renders']}张复用GS、{val['flow_renders']}张复用光流、{val['montages']}张主拼图；warnings={val['warnings']}。这些GS/光流均非本轮新推理。",
f"- {env['reused_from']['file_count']}个复制文件逐项SHA256相同，覆盖prepare/flow/poses/tokens/gs/compat_packages；见reused_files_manifest.json。输入原图哈希与共享t也重新核对。",
f"- 对第七轮全部{extra['old_round7_rows_compared']}行旧方法指标逐项比较，最大绝对差：`{extra['old_round7_max_abs_difference']}`。",
f"- tokchk.csv共{extra['tokchk_rows']}行、{extra['tokchk_methods']}种新增方法，目标/变体/复核键唯一、选区面积非负且不超过原core、仅对_al_local新增。混合最小coverage={extra['hybrid_coverage_min']}；{extra['zero_paste_identity_checks']}条零贴回记录在全部六区域精确等于光流（PSNR/SSIM/LPIPS/面积/覆盖率）。",
f"- 每目标方法×区域行数：`{extra['rows_per_target']}`。附加校验脚本check_and_archive.py和报告生成脚本build_report.py随归档提供。",
'- gspl：Python3.9.23、torch2.0.1/CUDA11.7、gsplat1.5.3、RTX3090；未替换环境包或外部源码。后台脚本current_stage.txt/runner_exit_code.txt记录完成状态。','',
'## 解释边界','',
'- 目标风险复核使用参考光流实际t对应的r_warp/r_col与光流结果抠像前景，不用当前目标真值。所用阈值见配置，w08d仅加大膨胀。oracle才使用core与真值失败区的交集，单独标记，不可部署。',
'- oracle按“光流误差超过阈值”选择，并未判断GS一定更好；也不是逐像素在GS/光流之间取最优，所以是诊断参照，不是所有可能融合策略的严格数学上限。',
'- tokchk.csv面积是羽化前sel总像素数/有效前景面积，分子可能含前景外像素，不是真正替换前景比例。paste_weight会膨胀/平滑并受GS alpha限制，最终受影响区域可以超出sel与原风险交集。',
'- _g分支的pair_gate先清空某对core；本轮只能进一步收紧已有core，不能恢复已被面积门限关闭的区域，所以未加面积门限的rife/strict是必要对照。',
'- 全部GS/相机/输入token固定复用，第八轮比较的是复核与贴回规则。H/t来自前序离线估计，t最初涉及目标图联合VGGT；_alv历史控制与相机预处理的边界见第七轮报告。当前主复核不使用目标误差，不代表整个前序协议完全无目标图信息。',
'- 旧+reg/oracle风险扫描及上游主拼图选优涉及真值，均不参与固定tokchk构造。当前扫描只覆盖一个场景单帧，没有统计显著性、泛化或自动阈值选择结论。SSIM沿用前景裁片实现，支撑域与PSNR/LPIPS并非完全相同。','',
'## 复现与归档','',
'```bash','cd /home/han/linux-han/local-gs-eval','export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH','export LGS_WORK_DIR=work/round8 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1','export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4','# 首次运行按README复制round7的prepare/flow/poses/tokens/gs/compat_packages','python -m unittest discover -s tests -v','python scripts/evaluate.py --config configs/mofang_9cam.yaml','python scripts/validate_results.py configs/mofang_9cam.yaml','```','',
'本轮上传配置/环境/复用文件哈希、全部评估CSV与summary、日志、10张上游主图和10张固定策略新图、复现/归档/绘图/报告脚本。GS/token元数据、40张输入叠加图和800张掩码归档沿用同一分支保留的 [第七轮](../mofang-9cam-round7-gspl-20261025/REPORT.md)，不重复上传原始数据/模型/所有GS渲染；完整评估复现仍需要本机work或这些外部数据。前七轮结果保留。','']
(a/'REPORT.md').write_text('\n'.join(L));readme=R/'README.md';text=readme.read_text();prefix='> 本机第八轮实测：[报告](results/mofang-9cam-round8-gspl-20261025/REPORT.md) · [完整汇总](results/mofang-9cam-round8-gspl-20261025/eval/summary.md) · [第七轮](results/mofang-9cam-round7-gspl-20261025/REPORT.md)。源提交8d7cf85，仅重跑评估。\n\n'
if not text.startswith('> 本机第八轮'):readme.write_text(prefix+text)
print(json.dumps({'rife':[q for q in summ if q['variant']=='rife'],'cross_setup_candidates':cross},indent=2,ensure_ascii=False))

from pathlib import Path
import csv,json,statistics
R=Path(__file__).resolve().parents[2];a=R/'results/mofang-9cam-round7-gspl-20261025';e=a/'eval'
rows=list(csv.DictReader((e/'metrics.csv').open()));tok=json.loads((a/'tokens/tokens.json').read_text());geo=list(csv.DictReader((e/'paste_geometry.csv').open()));counts=list(csv.DictReader((e/'local_counts_and_plane.csv').open()));val=json.loads((e/'validation.json').read_text());extra=json.loads((e/'extra_validation.json').read_text());variants=['r5','rife','strict','rife_g','strict_g'];ref='flow_s1.0_pose'
def method(v,src='al',kind='hyb_token'):return f'{kind}[gs_tok{v}448_nat_dil_{src}_local]'
def get(s,t,m,r):return next(x for x in rows if x['setup']==s and x['target']==str(t) and x['method']==m and x['region']==r)
def mean(s,m,r,k):return statistics.mean(float(x[k]) for x in rows if x['setup']==s and x['method']==m and x['region']==r)
def cw(path,rr):
 with path.open('w') as f:
  d=csv.DictWriter(f,fieldnames=list(rr[0]));d.writeheader();d.writerows(rr)
targets={s:sorted({int(x['target']) for x in rows if x['setup']==s}) for s in ('cam3','cam5')};target_rows=[];primary=[]
for s in ('cam3','cam5'):
 ctx=sorted(int(k) for k in tok['fractions']['r5'][s])
 for t in targets[s]:
  pair=f'{max(c for c in ctx if c<t)}-{min(c for c in ctx if c>t)}'
  for v in variants:
   for src,pose in [('al','aligned_int'),('alv','aligned_vggt')]:
    info=tok['pairs'][v][s][pair];m=method(v,src);r=dict(setup=s,target=t,pair=pair,variant=v,pose_source=pose,pair_core=info['core'],gated=info['gated'])
    for reg in ('fg','object','rest'):
     for k in ('psnr','lpips'):
      r[f'{reg}_{k}']=float(get(s,t,m,reg)[k]);r[f'{reg}_delta_{k}']=r[f'{reg}_{k}']-float(get(s,t,ref,reg)[k])
    target_rows.append(r)
 for v in variants:
  rr=[r for r in target_rows if r['setup']==s and r['variant']==v and r['pose_source']=='aligned_int'];gg=[x for x in geo if x['setup']==s and x['variant']==v and x['pose_source']=='aligned_int']
  r=dict(setup=s,variant=v,input_core=statistics.mean(x['core'] for x in tok['fractions'][v][s].values()),fg_replaced=statistics.mean(float(x['foreground_replaced_fraction']) for x in gg),core_over_fg=statistics.mean(float(x['core_total_over_fg']) for x in gg),gated_targets=sum(x['gated'] for x in rr),targets=len(rr),fg_strict_both_wins=sum(x['fg_delta_psnr']>1e-8 and x['fg_delta_lpips']<-1e-8 for x in rr),fg_neither_worse=sum(x['fg_delta_psnr']>=-1e-8 and x['fg_delta_lpips']<=1e-8 for x in rr))
  for reg in ('fg','object','rest'):
   for k in ('psnr','lpips'):
    r[f'{reg}_{k}']=mean(s,method(v),reg,k);r[f'{reg}_delta_{k}']=r[f'{reg}_{k}']-mean(s,ref,reg,k)
  primary.append(r)
cw(e/'primary_comparison.csv',primary);cw(e/'target_comparison.csv',target_rows)
L=['# 第七轮实测：逐对 token、固定编码窗口与门限','',
'源代码：`luckyhan-mike/local-gs-eval@c0e80b6`。工作目录 `work/round7`，归档名沿用主机启动日期 20261025。使用上游第七轮默认配置，**没有修改算法、评价代码或阈值**，没有根据本轮真值结果调整门限。','',
'## 主结果','',
'**cam3 的 rife_g/strict_g 在6个目标的前景PSNR、LPIPS上均不差于光流：目标1–3改善，5–7精确回退。cam5 strict_g 前景PSNR提高约0.229 dB，但LPIPS仍增加0.000090，未同时满足两项均值不降；关闭的3个目标与光流相同。** 未门限的cam3 rife有更高平均PSNR，但仅4/6个目标双指标均不差，反映收益与保护可靠视点之间的取舍。','',
'固定 `_al` 输入光心插值、直接贴回，各留出相机等权平均。PSNR↑，LPIPS↓。均值改善与全部视点不退化是不同判据；最后两列严格区分双指标改善与包含回退的“不变或更好”。','',
'| 设置 | token | fg PSNR | fg LPIPS | object PSNR | object LPIPS | rest PSNR | 回退目标数 | fg双指标改善 | fg双指标均不差 |','|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
for s in ('cam3','cam5'):
 L.append(f'| {s} | 纯光流 | {mean(s,ref,"fg","psnr"):.6f} | {mean(s,ref,"fg","lpips"):.6f} | {mean(s,ref,"object","psnr"):.6f} | {mean(s,ref,"object","lpips"):.6f} | {mean(s,ref,"rest","psnr"):.6f} | — | — | — |')
 for r in primary:
  if r['setup']==s:L.append(f"| {s} | {r['variant']} | {r['fg_psnr']:.6f} | {r['fg_lpips']:.6f} | {r['object_psnr']:.6f} | {r['object_lpips']:.6f} | {r['rest_psnr']:.6f} | {r['gated_targets']}/{r['targets']} | {r['fg_strict_both_wins']}/{r['targets']} | {r['fg_neither_worse']}/{r['targets']} |")
L+=['','## 对照 README 预期（Codex 分析）','']
for r in primary:
 if not r['variant'].endswith('_g'):continue
 ok=r['fg_delta_psnr']>=-1e-8 and r['fg_delta_lpips']<=1e-8
 L.append(f"- {r['setup']} / {r['variant']}：fg ΔPSNR={r['fg_delta_psnr']:+.6f} dB，ΔLPIPS={r['fg_delta_lpips']:+.6f}；{'达到' if ok else '未达到'}前景双指标均值不下降。逐目标双指标均不差为{r['fg_neither_worse']}/{r['targets']}，不应只用均值判断全部视点。")
L+=['','本轮固定窗口排除了第六轮“不同变体重新裁剪/编码”这个混杂因素；但第六→七轮还同时改变了逐对选择与触发方式，不能把跨轮总收益全部分配给某一个改动。门限0.03由上游根据同场景前序实验提出；本轮结果是继续验证，不是独立场景上的泛化评估。','',
'## 逐目标主对比','',
'下面为 `_al` 直接贴回的前景ΔPSNR / ΔLPIPS；* 表示该相机对被门限关闭。精确值与object/rest见 [target_comparison.csv](eval/target_comparison.csv)，该CSV还包含 `_alv` 控制。','',
'| 设置 | 目标 | 相机对 | '+ ' | '.join(variants)+' |','|---|---:|---|'+'---:|'*len(variants)]
for s in ('cam3','cam5'):
 for t in targets[s]:
  rr=[r for r in target_rows if r['setup']==s and r['target']==t and r['pose_source']=='aligned_int'];cells=[]
  for v in variants:
   r=next(x for x in rr if x['variant']==v);cells.append(f"{r['fg_delta_psnr']:+.6f} / {r['fg_delta_lpips']:+.6f}"+('*' if r['gated'] else ''))
  L.append(f"| {s} | {t} | {rr[0]['pair']} | "+' | '.join(cells)+' |')
L+=['','## 逐对检测与触发','',
'pair core 是门限前两台输入相机 core/前景的平均；关闭后写出的pair掩码全零。输入并集仍用于叠加图与固定窗口，不能用并集面积替代目标所属对的面积。','',
'| 设置 / 相机对 | '+ ' | '.join(variants)+' |','|---|'+'---:|'*len(variants)]
for s in ('cam3','cam5'):
 for pair in tok['pairs']['r5'][s]:
  cells=[]
  for v in variants:
   q=tok['pairs'][v][s][pair];cells.append(f"{q['core']:.4%}"+(' (关闭)' if q['gated'] else ''))
  L.append(f'| {s} / {pair} | '+' | '.join(cells)+' |')
L+=['','## 固定编码与局部高斯','',
'| 设置 | raw窗口边长 | 编码总高斯 | plane RMS px | 输入自渲染PSNR |','|---|---:|---:|---:|---:|']
for s in ('cam3','cam5'):
 r=next(x for x in counts if x['setup']==s);L.append(f"| {s} | {r['window']} | {r['total']} | {float(r['plane_rms_px']):.6f} | {float(r['ctx_self_psnr']):.6f} |")
L+=['','逐对recon/core数量见 [local_counts_and_plane.csv](eval/local_counts_and_plane.csv)。全部变体的window、编码高斯数、编码时间、自渲染和Sim3元数据逐项一致；日志每设置仅一次编码。局部选择按目标所属对进行，`_al`、`_alv`共享所选高斯。逐对限制的是token与高斯选择；编码器仍读取该设置全部context相机，不是每个相机对单独重建。数量关系检查为0≤core≤recon≤总数，并非逐元素集合证明。',
'','固定窗口仍对整个448×448输入编码，筛选在编码后，不能据保留高斯数量宣称稀疏Transformer或端到端加速。plane RMS 是输入几何与H的拟合诊断，不是目标视点误差；合成几何测试通过也不意味着真实阵列精确满足其假设。','',
'## 贴回范围','',
'配准/羽化前core，逐目标计算后平均；包含关闭目标的0面积。core总面积/fg包含前景外部分，不等于真正替换前景比例。','',
'| 设置 / token | 输入并集core / fg | core总面积 / fg | core覆盖fg |','|---|---:|---:|---:|']
for r in primary:L.append(f"| {r['setup']} / {r['variant']} | {r['input_core']:.2%} | {r['core_over_fg']:.2%} | {r['fg_replaced']:.2%} |")
L+=['','## 全部主表（上游输出）','',
'包括全部token、两种光心来源、直接/ringreg贴回。贴回区比较仅包括core非空的目标，门限均值与上面的全目标均值支撑不同；不同变体的core也不同。','']
summary=(e/'summary.md').read_text();L.append('### 贴回区内'+summary.split('### 贴回区内',1)[1].split('## 其余诊断',1)[0])
L+=['## 验证与可复现性','',
f"- 12项数值测试全部通过，包括新增的逐对选择测试。产物验证{val['status']}：{val['metric_rows']}行质量指标、{val['methods']}种方法、{val['auc_rows']}行AUC、{val['gs_renders']}张GS、{val['flow_renders']}张复用光流、{val['montages']}张主拼图；warnings={val['warnings']}。",
f"- 附加检查：{extra['paste_rows']}行非空贴回区指标全部有限，{extra['ring_rows']}条环带记录；混合最小coverage={extra['hybrid_coverage_min']}。关闭门限的{extra['gated_identity_checks']}条设置/目标/变体/位姿记录，core alpha为0、所选高斯数为0，直接/ringreg在全部6区域的PSNR/SSIM/LPIPS/面积/覆盖率逐项精确等于光流。详见gated_identity_checks.csv。",
f"- 每目标方法×区域行数：`{extra['rows_per_target']}`。参考光流相对第六轮的最大绝对差：`{extra['reference_vs_round6_max_abs_difference']}`。",
'- gspl：Python3.9.23、torch2.0.1/CUDA11.7、gsplat1.5.3、RTX3090。e3nn0.5.6仅在工作目录兼容包中，Python3.9 AnySplat注解转换使用工作副本；未替换共享环境或外部仓库。',
'- 从round6独立复制prepare、flow、poses、compat_packages，重新检测token、运行GS和评估。输入SHA256重新核对；两尺度pose光流的t与poses.t_pose逐项精确一致。模型/外部源码版本和配置见environment.json。',
'- 本轮脚本以独立后台进程运行，current_stage.txt、runner_exit_code.txt记录完成状态，避免聊天中断终止评估。没有为找更优结果调整阈值后重跑。','',
'## 解释边界','',
'- 已查看cam3 strict_g输入4叠加图，标记主要在魔方/手/前臂附近，重建外扩区仍延伸到头发和身体；这不是独立检测真值，不能只凭图或面积证明准确率。','',
'- 主检测、逐对门限、可见性选择、平面拟合、core前景限制、环带配准不使用当前目标真值误差作决策；H/t来自前序离线信息，t最初含目标图联合VGGT。`_alv`用目标图估计光心，历史联合VGGT代码仍执行。上游“可部署/全程不用真值”须限定到给定离线映射/相机信息后的主贴回决策，不代表完整端到端协议完全无目标图依赖。',
'- +reg使用真值ECC配准；oracle_fail、风险扫描和主拼图挑选展示变体涉及真值，是诊断/展示，不参与固定主方法构造。门限关闭时等于光流是回退成功，不是GS重建质量的提升。',
'- 环带位移0可能来自拟合失败或无需移动，>20px会回退，不能作为独立的几何正确性证明。SSIM沿用前景裁片实现，支撑域与PSNR/LPIPS并非完全相同。仅单场景单帧，无统计显著性或跨场景有效性结论。','',
'## 复现与归档','',
'```bash','cd /home/han/linux-han/local-gs-eval','export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH','export LGS_WORK_DIR=work/round7 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1','export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4','# 首次运行按README复制round6的prepare/flow/poses/compat_packages','python -m unittest discover -s tests -v','python scripts/detect_tokens.py --config configs/mofang_9cam.yaml','python scripts/run_anysplat.py --config configs/mofang_9cam.yaml','python scripts/evaluate.py --config configs/mofang_9cam.yaml','python scripts/validate_results.py configs/mofang_9cam.yaml','```','',
'上传：本报告、配置/环境/输入哈希、全部评估CSV与summary、10张主拼图、40张输入并集叠加图、token元数据、日志、GS/flow/pose元数据及运行脚本；前六轮结果保留。全部aligned/raw、并集/逐对二值掩码打包为 [all_masks.tar.gz](tokens/all_masks.tar.gz)，逐文件SHA256见 [masks_manifest.json](tokens/masks_manifest.json)，打包后已逐文件解压核对哈希。原始数据、模型、完整GS渲染和fullgs诊断拼图保留在本机work，未上传，完整推理复现仍需要外部数据和模型。','']
(a/'REPORT.md').write_text('\n'.join(L))
readme=R/'README.md';text=readme.read_text();prefix='> 本机第七轮实测：[报告](results/mofang-9cam-round7-gspl-20261025/REPORT.md) · [完整汇总](results/mofang-9cam-round7-gspl-20261025/eval/summary.md) · [第六轮](results/mofang-9cam-round6-gspl-20261025/REPORT.md)。源提交c0e80b6，固定窗口/逐对token/0.03门限，原配置运行。\n\n'
if not text.startswith('> 本机第七轮'):readme.write_text(prefix+text)
print(json.dumps(primary,indent=2,ensure_ascii=False))

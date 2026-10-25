from pathlib import Path
import csv,json,statistics
R=Path(__file__).resolve().parents[2];a=R/'results/mofang-9cam-round10-gspl-20261025';e=a/'eval'
rows=list(csv.DictReader((e/'metrics.csv').open()));val=json.loads((e/'validation.json').read_text());extra=json.loads((e/'extra_validation.json').read_text());env=json.loads((a/'environment.json').read_text());cfg=env['config'];ref=cfg['eval']['ref_flow'];variants=list(cfg['tokens']['variants']);targets={s:sorted({int(r['target']) for r in rows if r['setup']==s}) for s in cfg['setups']};by={(r['setup'],int(r['target']),r['method'],r['region']):r for r in rows}
def method(v,pose,it,how):
 gv=f'gs_tok{v}448_nat_dil_{pose}'+(f'_tto{it}' if it else '')+'_local';return f'hyb_token[{gv}]' if how=='direct' else f'hyb_tokchk_{how}[{gv}]'
def avg(s,m,reg,k):return statistics.mean(float(by[s,t,m,reg][k]) for t in targets[s])
def cw(p,rr):
 with p.open('w') as f:
  d=csv.DictWriter(f,fieldnames=list(rr[0]));d.writeheader();d.writerows(rr)
summ=[];per=[]
for s in targets:
 for v in variants:
  for pose in ('al','alv'):
   for it in (0,300,1000):
    for how in (('direct','w20','oracle') if pose=='al' else ('direct',)):
     m=method(v,pose,it,how);rr=[]
     for t in targets[s]:
      q=dict(setup=s,target=t,variant=v,pose_source=pose,tto_steps=it,how=how,uses_gt=(how=='oracle'))
      for reg in ('fg','object','rest'):
       for k in ('psnr','lpips'):
        q[f'{reg}_{k}']=float(by[s,t,m,reg][k]);q[f'{reg}_delta_flow_{k}']=q[f'{reg}_{k}']-float(by[s,t,ref,reg][k]);q[f'{reg}_delta_FF_{k}']=q[f'{reg}_{k}']-float(by[s,t,method(v,pose,0,how),reg][k])
      q['fg_not_worse']=q['fg_delta_flow_psnr']>=-1e-6 and q['fg_delta_flow_lpips']<=1e-6;rr.append(q);per.append(q)
     q=dict(setup=s,variant=v,pose_source=pose,tto_steps=it,how=how,uses_gt=(how=='oracle'),fg_not_worse_targets=sum(r['fg_not_worse'] for r in rr),targets=len(rr))
     for reg in ('fg','object','rest'):
      for k in ('psnr','lpips'):
       q[f'{reg}_{k}']=avg(s,m,reg,k);q[f'{reg}_delta_flow_{k}']=q[f'{reg}_{k}']-avg(s,ref,reg,k);q[f'{reg}_delta_FF_{k}']=q[f'{reg}_{k}']-avg(s,method(v,pose,0,how),reg,k)
     summ.append(q)
cw(e/'tto_quality_comparison.csv',summ);cw(e/'tto_quality_per_view.csv',per)
def get(s,it,how='direct'):return next(q for q in summ if q['setup']==s and q['variant']=='rife' and q['pose_source']=='al' and q['tto_steps']==it and q['how']==how)
L=['# 第十轮实测：局部 GS 测试时优化（TTO）','',
'源代码：`luckyhan-mike/local-gs-eval@dd3b6d0`。工作目录 `work/round10`，目录命名沿用主机启动日期20261025。按上游默认配置重新运行GS和TTO、评估、验证；prepare/flow/poses/tokens/compat_packages来自round7。未修改算法、阈值或评价代码；未根据本轮真值调参重跑。','',
'## 主结果','',
'**本帧300步TTO明显改善固定rife/_al分支，cam3与cam5的前景PSNR、LPIPS均值均优于纯光流；但并非所有cam5视点都同时改善。** 直接贴回的cam3为27.203 dB / 0.047043，object为20.057 / 0.092646；cam5为29.035 / 0.039030，object为22.626 / 0.055646。300步时cam3 6/6、cam5 3/4个视点前景双指标不差。1000步输入拟合继续增强，但两组留出LPIPS均比300步更差，cam5直接贴回LPIPS也不再优于光流。','',
'主表固定rife、`_al`输入光心插值，FF为前馈，300/1000为优化步数。direct为直接贴回，w20用光流信号复核，oracle使用目标真值，仅作诊断。PSNR↑、LPIPS↓，各留出相机等权平均。','',
'| 设置 | 步数 | 贴回 | fg PSNR | fg LPIPS | object PSNR | object LPIPS | rest PSNR | fg不差目标数 |','|---|---:|---|---:|---:|---:|---:|---:|---:|']
for s in targets:
 L.append(f'| {s} | 纯光流 | — | {avg(s,ref,"fg","psnr"):.6f} | {avg(s,ref,"fg","lpips"):.6f} | {avg(s,ref,"object","psnr"):.6f} | {avg(s,ref,"object","lpips"):.6f} | {avg(s,ref,"rest","psnr"):.6f} | — |')
 for it in (0,300,1000):
  for how in ('direct','w20','oracle'):
   q=get(s,it,how);L.append(f"| {s} | {it or 'FF'} | {how} | {q['fg_psnr']:.6f} | {q['fg_lpips']:.6f} | {q['object_psnr']:.6f} | {q['object_lpips']:.6f} | {q['rest_psnr']:.6f} | {q['fg_not_worse_targets']}/{q['targets']} |")
L+=['','## 对照 README 判据（Codex 分析）','']
for s in targets:
 for it in (300,1000):
  q=get(s,it);qo=get(s,it,'oracle');L.append(f"- {s} / {it}步直接贴回：相对本轮FF，fg ΔPSNR={q['fg_delta_FF_psnr']:+.6f} dB、ΔLPIPS={q['fg_delta_FF_lpips']:+.6f}；object ΔPSNR={q['object_delta_FF_psnr']:+.6f}、ΔLPIPS={q['object_delta_FF_lpips']:+.6f}。oracle相对光流：fg ΔPSNR={qo['fg_delta_flow_psnr']:+.6f}、ΔLPIPS={qo['fg_delta_flow_lpips']:+.6f}。")
L+=['','### 1000步与300步的留出视点比较','']
for s in targets:
 for how in ('direct','oracle'):
  x,y=get(s,1000,how),get(s,300,how);L.append(f"- {s} / {how}，1000−300：fg ΔPSNR={x['fg_psnr']-y['fg_psnr']:+.6f} dB，ΔLPIPS={x['fg_lpips']-y['fg_lpips']:+.6f}；object ΔPSNR={x['object_psnr']-y['object_psnr']:+.6f}，ΔLPIPS={x['object_lpips']-y['object_lpips']:+.6f}。")
L+=['','输入拟合继续变好而留出质量变差，支持过拟合的现象判断；但本轮同时优化了位置、协方差、不透明度和颜色，投影贴回范围也变化，不能只凭输入PSNR升高把全部退化归为颜色过拟合。','',
'## 输入拟合与时间代价','',
'| 设置 | 优化高斯 / 总数 | 监督分辨率 | 1000步总调用耗时 | it1输入PSNR | it300输入PSNR | it1000输入PSNR |','|---|---:|---:|---:|---:|---:|---:|']
tt=list(csv.DictReader((e/'tto_timing.csv').open()));train=list(csv.DictReader((e/'tto_training.csv').open()))
for r in tt:
 s=r['setup'];values=[statistics.mean(float(x['input_crop_psnr']) for x in train if x['setup']==s and int(x['iteration'])==it) for it in (1,300,1000)];L.append(f"| {s} | {r['train_gaussians']} / {r['total_gaussians']} | {r['supervision_res']}² | {float(r['total_tto_time_s']):.3f} s | "+' | '.join(f'{v:.6f}' for v in values)+' |')
L+=['','time_s是一次TTO优化器调用至1000步的墙钟时间，包含300和1000检查点构造，排除前馈编码、后续目标渲染和评估；不是端到端每帧耗时。源脚本未记录单独300步耗时，本报告不按比例估算成实测值。',
'','输入PSNR为全裁剪图均值，包含背景，不是foreground或object指标；分辨率911/917与原先448自渲染PSNR不同，不能直接相减。日志中的每步pred在该步参数更新前生成，而快照在该步更新后生成。完整损失和逐输入相机曲线数据见tto_training.csv。','',
'## 高斯选择与目标贴回范围','',
'固定的是优化前选定的高斯索引和数量。源码会用优化后的高斯重新渲染alpha_core；位置、协方差和不透明度变化可改变目标像素core。以下实际测量rife/_al的变化，不预设贴回区完全相同。','',
'| 设置 | 步数 | core平均IoU | 平均变化像素 | FF覆盖fg | TTO覆盖fg | 最大混合权重差 |','|---|---:|---:|---:|---:|---:|']
sp=list(csv.DictReader((e/'tto_paste_support.csv').open()))
for s in targets:
 for it in (300,1000):
  rr=[r for r in sp if r['setup']==s and r['variant']=='rife' and r['pose_source']=='al' and int(r['tto_steps'])==it];av=lambda k:statistics.mean(float(r[k]) for r in rr);L.append(f'| {s} | {it} | {av("core_iou"):.6f} | {av("core_changed_px"):.1f} | {av("ff_fg_covered"):.3%} | {av("tto_fg_covered"):.3%} | '+f"{max(float(r['weight_max_abs_difference']) for r in rr):.6f} |")
L+=['','IoU基于前景限制后的实际core；影响域还受羽化和各阶段alpha影响。因此本轮测量的是完整TTO管线，不是固定同一目标像素集合、只替换颜色的消融。数量不变也不代表几何或有效可见性不变。完整200条局部视图检查见tto_paste_support.csv。','',
'## 全部颜色来源表（上游输出）','',
'上游该表将_al和_alv都简写为同一个token名称，会出现同名行。本报告上方主表固定_al；下方上游表保留原样，精确区分pose_source请查看本报告的tto_quality_comparison.csv和tto_quality_per_view.csv。','']
sm=(e/'summary.md').read_text();L.append('### 颜色来源对比'+sm.split('### 颜色来源对比',1)[1].split('## 其余诊断',1)[0])
L+=['## 固定方法对比图','',
'10张固定rife、_al直接贴回对比图包含GT、光流、FF、TTO300、TTO1000与×3误差图；蓝色为FF core，红色为1000步相对FF改变的core像素。没有按真值选取token或检查点，GT仅用于裁片定位与误差图。','',
'例如 [cam3/目标3](figures/cam3/cam3_rife_ff_tto.png)、[cam5/目标3](figures/cam5/cam3_rife_ff_tto.png)。已查看cam3/目标3，TTO色块边缘更清楚，但局部观感不替代完整前景与所有目标视点的指标。','',
'## 验证与边界','',
f"- 15项测试通过，包括TTO协方差参数化/局部更新的可微mock测试。实际GPU TTO完成两组1000步。上游验证{val['status']}：{val['methods']}方法、{val['metric_rows']}行质量指标、{val['auc_rows']}行AUC、{val['gs_renders']}张原始GS分支、{val['flow_renders']}张复用光流、{val['montages']}张主拼图，warnings={val['warnings']}。",
f"- 原验证脚本只枚举FF分支；附加解码{extra['tto_local_views_explicitly_checked']}张局部TTO和{extra['tto_full_views_explicitly_checked']}张完整TTO视图，共360张RGB视图。局部高斯选择数量、相机valid相同；{extra['tto_core_masks_changed_count']}/200条TTO core发生变化，最大变化{extra['max_core_changed_pixels']}像素。",
f"- {extra['tokchk_rows']}行复核面积不超过core；{extra['zero_paste_identity_checks']}条零贴回在六个区域全部指标精确等于光流。混合最小coverage={extra['hybrid_coverage_min']}，光流相对第九轮最大绝对差：`{extra['reference_vs_round9_max_abs_difference']}`。",
f"- 每目标方法×区域行数：`{extra['rows_per_target']}`。{env['reused_from']['file_count']}个复用文件SHA256与round7相同；输入原图哈希和共享t也重新核对。",
'- gspl：Python3.9.23、torch2.0.1/CUDA11.7、gsplat1.5.3、RTX3090。未替换环境包或外部源码，未重新检测token。第九轮重投影默认关闭。',
'- 优化loss是整个输入裁剪的0.8·L1+0.2·(1−SSIM)，仅所选高斯可训练，其余仍渲染；没有加密/剪枝，也没有显式几何锚定惩罚。协方差因子有微小jitter、opacity有clamp，源码所谓首渲染完全相同在测试中只作数值容差验证，不当成已测的逐位相等。',
'- 主TTO只监督输入相机，不使用留出目标真值损失。H/t仍来自前序离线信息，t最初涉及目标图联合VGGT；_alv控制涉及目标图估计相机。oracle/+reg和展示选优涉及真值，作为诊断单列，不参与固定主方法构造。',
'- 本轮是同场景单帧、固定配置实验；未给统计显著性、泛化或自动停止步数结论。跨轮重新编码有轻微数值差异，TTO对照以本轮FF为基准。SSIM沿用前景裁片实现，支撑域与另外两个指标不同。','',
'## 复现与归档','',
'```bash','cd /home/han/linux-han/local-gs-eval','export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH','export LGS_WORK_DIR=work/round10 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1','export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4','# 首次按README复制round7的prepare/flow/poses/tokens/compat_packages','python -m unittest discover -s tests -v','python scripts/run_anysplat.py --config configs/mofang_9cam.yaml','python scripts/evaluate.py --config configs/mofang_9cam.yaml','python scripts/validate_results.py configs/mofang_9cam.yaml','```','',
'归档包含报告、全部CSV/summary、训练损失/输入PSNR和时间、支持域统计、配置/环境/复用哈希、元数据/日志、10张主拼图和10张固定检查点对比图、复现/归档/绘图/报告脚本。输入token及800张掩码沿用同分支保留的第七轮。全部FF/TTO RGB与alpha在本机work/round10/gs，未全部上传；源脚本快照仅在运算中保留，未保存优化后高斯参数或优化器状态文件。原始数据/模型未上传，完整复现需要这些外部数据。前九轮结果保留。','']
(a/'REPORT.md').write_text('\n'.join(L));p=R/'README.md';s=p.read_text();prefix='> 本机第十轮实测：[报告](results/mofang-9cam-round10-gspl-20261025/REPORT.md) · [完整汇总](results/mofang-9cam-round10-gspl-20261025/eval/summary.md) · [第九轮](results/mofang-9cam-round9-gspl-20261025/REPORT.md)。源提交dd3b6d0，重新运行GS与300/1000步TTO。\n\n'
if not s.startswith('> 本机第十轮'):p.write_text(prefix+s)
print(json.dumps({'rife_al':[q for q in summ if q['variant']=='rife' and q['pose_source']=='al']},indent=2,ensure_ascii=False))

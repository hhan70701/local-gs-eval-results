from pathlib import Path
import csv,json,statistics
R=Path(__file__).resolve().parents[2];a=R/'results/mofang-9cam-round11-gspl-20261025';e=a/'eval'
rows=list(csv.DictReader((e/'metrics.csv').open()));val=json.loads((e/'validation.json').read_text());extra=json.loads((e/'extra_validation.json').read_text());env=json.loads((a/'environment.json').read_text());cfg=env['config'];ref=cfg['eval']['ref_flow'];variants=list(cfg['tokens']['variants']);steps=[0]+cfg['gs']['tto']['checkpoints'];targets={s:sorted({int(r['target']) for r in rows if r['setup']==s}) for s in cfg['setups']};by={(r['setup'],int(r['target']),r['method'],r['region']):r for r in rows}
timing=list(csv.DictReader((e/'tto_checkpoint_timing.csv').open()));times={(r['setup'],int(r['iteration'])):r for r in timing}
old=list(csv.DictReader((R/'results/mofang-9cam-round10-gspl-20261025/eval/tto_quality_comparison.csv').open()));old_time=list(csv.DictReader((R/'results/mofang-9cam-round10-gspl-20261025/eval/tto_timing.csv').open()))
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
   for it in steps:
    for how in (('direct','w20','oracle') if pose=='al' else ('direct',)):
     m=method(v,pose,it,how);rr=[]
     for t in targets[s]:
      q=dict(setup=s,target=t,variant=v,pose_source=pose,tto_steps=it,how=how,uses_gt=(how=='oracle'))
      for reg in ('fg','object','rest'):
       for k in ('psnr','lpips'):
        q[f'{reg}_{k}']=float(by[s,t,m,reg][k]);q[f'{reg}_delta_flow_{k}']=q[f'{reg}_{k}']-float(by[s,t,ref,reg][k]);q[f'{reg}_delta_FF_{k}']=q[f'{reg}_{k}']-float(by[s,t,method(v,pose,0,how),reg][k])
      q['fg_not_worse']=q['fg_delta_flow_psnr']>=-1e-6 and q['fg_delta_flow_lpips']<=1e-6;rr.append(q);per.append(q)
     q=dict(setup=s,variant=v,pose_source=pose,tto_steps=it,how=how,uses_gt=(how=='oracle'),cumulative_tto_time_s=float(times[s,it]['cumulative_time_s']) if it else 0.0,fg_not_worse_targets=sum(r['fg_not_worse'] for r in rr),targets=len(rr))
     for reg in ('fg','object','rest'):
      for k in ('psnr','lpips'):
       q[f'{reg}_{k}']=avg(s,m,reg,k);q[f'{reg}_delta_flow_{k}']=q[f'{reg}_{k}']-avg(s,ref,reg,k);q[f'{reg}_delta_FF_{k}']=q[f'{reg}_{k}']-avg(s,method(v,pose,0,how),reg,k)
     summ.append(q)
cw(e/'tto_quality_comparison.csv',summ);cw(e/'tto_quality_per_view.csv',per)
def get(s,it,how='direct'):return next(q for q in summ if q['setup']==s and q['variant']=='rife' and q['pose_source']=='al' and q['tto_steps']==it and q['how']==how)
def old300(s):return next(q for q in old if q['setup']==s and q['variant']=='rife' and q['pose_source']=='al' and int(q['tto_steps'])==300 and q['how']=='direct')
earliest=None
for it in steps[1:]:
 if all(get(s,it)['fg_delta_flow_psnr']>=-1e-6 and get(s,it)['fg_delta_flow_lpips']<=1e-6 and get(s,it)['fg_not_worse_targets']>=int(old300(s)['fg_not_worse_targets']) for s in targets):earliest=it;break
L=['# 第十一轮实测：裁剪监督、早期检查点与TTO计时','',
'源代码：`luckyhan-mike/local-gs-eval@fa4bbbd`。工作目录 `work/round11`，目录名沿用主机启动日期20261025。重新运行GS及25/50/100/200/300步TTO，token/prepare/flow/poses/compat_packages复用round7。唯一上游源码修复是报告函数参数传递，补丁单列；优化、采样、指标算法及阈值未修改。','',
'## 主结果：步数—耗时—质量','',
'**本次已测检查点中，200步最早同时达到两组既定质量条件**：cam3累计14.108秒、前景27.334 dB / 0.046017 LPIPS、6/6视点不差；cam5累计24.536秒、29.149 / 0.038169、3/4不差。相对本轮300步，累计优化时间减少约34%；这不包含编码和目标渲染。300步的前景/物体均值相对第十轮略好，但监督框仍占96.38%/91.49%，缺少旧版300步实测时间，不能据此宣称已测得大幅纯裁剪加速。','',
'固定rife、_al、直接贴回；各留出相机等权平均，PSNR↑、LPIPS↓。累计时间是GPU同步后的额外TTO时间，不含编码、目标渲染或评估。FF的0仅表示没有TTO，编码本身不为0。','',
'| 设置 | 步数 | TTO累计秒 | 监督框 / 面积 | 输入PSNR | fg PSNR | fg LPIPS | object PSNR | object LPIPS | fg不差目标数 |','|---|---:|---:|---|---:|---:|---:|---:|---:|---:|']
training=list(csv.DictReader((e/'tto_training.csv').open()))
for s in targets:
 L.append(f'| {s} | 光流 | — | — | — | {avg(s,ref,"fg","psnr"):.6f} | {avg(s,ref,"fg","lpips"):.6f} | {avg(s,ref,"object","psnr"):.6f} | {avg(s,ref,"object","lpips"):.6f} | — |')
 for it in steps:
  q=get(s,it);t=times[s,it or steps[1]];ip=statistics.mean(float(x['input_crop_psnr']) for x in training if x['setup']==s and int(x['iteration'])==(it or 1));L.append(f"| {s} | {it or 'FF'} | {q['cumulative_tto_time_s']:.6f} | {t['box_w']}×{t['box_h']} / {float(t['area_frac']):.2%} | {ip:.6f} | {q['fg_psnr']:.6f} | {q['fg_lpips']:.6f} | {q['object_psnr']:.6f} | {q['object_lpips']:.6f} | {q['fg_not_worse_targets']}/{q['targets']} |")
L+=['','## 最早满足质量条件的已测检查点','',
'判据固定为：两组fg均值PSNR不低于且LPIPS不高于光流（1e−6容差），同时不差视点数至少达到第十轮rife/_al/300步的6/6、3/4。这并不要求完整复现第十轮每个质量数值；下节单独列300步跨轮差。','']
if earliest:
 L.append(f"本次已测检查点中最早为 **{earliest}步**：cam3 {float(times['cam3',earliest]['cumulative_time_s']):.6f}s，cam5 {float(times['cam5',earliest]['cumulative_time_s']):.6f}s。")
else:L.append('本次已测的25/50/100/200/300步中，**没有检查点同时满足上述两组条件**。')
L+=['','这是同一场景帧的事后验证结果，不是部署时自动停止策略，也没有验证所有更细步数或独立场景上的最小步数。完整逐视点和所有token/pose见tto_quality_per_view.csv、tto_quality_comparison.csv。','',
'## 300步与第十轮的质量比较','',
'| 设置 | 指标 | 第十轮300步 | 本轮300步 | 本轮−第十轮 |','|---|---|---:|---:|---:|']
for s in targets:
 x,y=get(s,300),old300(s)
 for key in ('fg_psnr','fg_lpips','object_psnr','object_lpips','rest_psnr'):
  d=x[key]-float(y[key]);L.append(f'| {s} | {key} | {float(y[key]):.6f} | {x[key]:.6f} | {d:+.6f} |')
L+=['','跨轮重新编码有轻微数值变化；裁剪监督也改变损失的像素集合、归一化及SSIM边界。主点平移保证子窗口的投影几何对应，不等于优化轨迹或最终质量逐位相同。当前测试验证了裁剪投影和mock优化，未作实际GPU整图/子图逐像素梯度等价证明。','',
'## 耗时与监督范围','',
'| 设置 | 第十轮1000步总调用秒（实测） | 第十轮300步线性推算秒（非实测） | 本轮300步累计秒（实测） | 监督面积 |','|---|---:|---:|---:|---:|']
for s in targets:
 oldt=float(next(t for t in old_time if t['setup']==s)['total_tto_time_s']);t=times[s,300];L.append(f"| {s} | {oldt:.6f} | {oldt*.3:.6f} | {float(t['cumulative_time_s']):.6f} | {float(t['area_frac']):.2%} |")
L+=['','第十轮没有单独记录300步耗时，因此不能从这张表给出实测的“纯裁剪加速倍率”。1000步与300步的总耗时下降同时包含减少迭代次数；早期检查点相对本轮300步的时间差是已测结果。',
'','本轮裁剪框仍覆盖约96%/91%的视图，宽度为整幅911/917像素。train_mask来自全部token变体recon并集，包含r5的较广区域，与接近全幅的投影外接框相符。源脚本按输入相机使用不同左上角、统一宽高，坐标见tto_supervision_boxes.csv。',
'','计时从optimize内部开始，包含参数及裁剪框准备，检查点GPU同步后记录，排除当次快照构造和后续渲染；之前的日志/快照开销已包含在后续累计值中。外层total_tto_time_s包含最后快照和返回，二者范围略有差异。',
'','输入PSNR仅在监督框内计算，不能直接与第十轮全裁剪PSNR相减；日志pred为当步更新前，保存的高斯快照为当步更新后。训练日志、逐检查点时间和框坐标均单独存CSV。','']
L+=['## 投影 core 与实际支持域','',
'高斯选择索引与数量在优化前固定，但优化位置、协方差和不透明度后会重新渲染alpha_core，因此目标像素贴回区仍可能变化。不能把同一组高斯等同于固定同一组目标像素。','',
'| 设置 | 步数 | rife/_al core平均IoU | 平均变化像素 | FF覆盖fg | TTO覆盖fg |','|---|---:|---:|---:|---:|---:|']
sp=list(csv.DictReader((e/'tto_paste_support.csv').open()))
for s in targets:
 for it in steps[1:]:
  rr=[r for r in sp if r['setup']==s and r['variant']=='rife' and r['pose_source']=='al' and int(r['tto_steps'])==it];av=lambda k:statistics.mean(float(r[k]) for r in rr);L.append(f'| {s} | {it} | {av("core_iou"):.6f} | {av("core_changed_px"):.1f} | {av("ff_fg_covered"):.3%} | {av("tto_fg_covered"):.3%} |')
L+=['','这是前景限制后的core；羽化和alpha还影响最终混合权重。完整支持域数据见tto_paste_support.csv，实际质量差是完整TTO与贴回流程的结果，不仅是颜色锐度变化。','',
'## 上游步数—耗时—质量表','']
sm=(e/'summary.md').read_text();L.append('### 测试时优化：步数–耗时–质量'+sm.split('### 测试时优化：步数–耗时–质量',1)[1].split('### 颜色来源对比',1)[0])
L+=['## 全部颜色来源对比（上游输出）','']
L.append('### 颜色来源对比'+sm.split('### 颜色来源对比',1)[1].split('## 其余诊断',1)[0])
L+=['## 固定检查点对比图','',
'10张图固定rife/_al直接贴回，按顺序展示GT、光流、FF、25、50、100、200、300步；标签中的时间为该设置的累计TTO时间。没有按真值选检查点或token。GT只用于展示裁片定位，不参与优化或主贴回决策。',
'','例如 [cam3/目标3](figures/cam3/cam3_rife_checkpoints.png)、[cam5/目标3](figures/cam5/cam3_rife_checkpoints.png)。已查看cam3/目标3，边缘随优化变清楚，但单个裁片的观感不替代全部目标的fg/object/rest指标。','',
'## 修复、执行与验证','',
'- 上游新报告函数引用了main局部变量tto_info和ecfg，却没有接收它们，会在写summary时报NameError。仅修复参数传递：向write_summary显式传入TTO元数据和主变体名称，未改优化或指标代码。见reporting_fix.patch。用第十轮真实CSV驱动的完整报告冒烟检查通过。',
'- TTO和全部阶段渲染结束后，cam3/cam5分别调用原evaluate.main(--setups ...)，各自使用独立输出目录，输入通过只读使用的目录链接共享。两组计算彼此独立，完成后拼接原始CSV、合并捕获的汇总参数，再调用上游write_summary一次。没有把质量计算换成简化版，TTO计时也未与并行评估重叠。',
f"- 16项数值测试通过，另有真实历史CSV报告冒烟检查。上游验证{val['status']}：{val['methods']}方法、{val['metric_rows']}行质量指标、{val['auc_rows']}行AUC、{val['gs_renders']}张FF分支、{val['flow_renders']}张复用光流、{val['montages']}张主拼图；warnings={val['warnings']}。",
f"- 七份合并CSV逐行等于cam3/cam5工作输出按固定顺序的拼接，键唯一性/指标有限性由最终验证检查；见parallel_merge_validation.json。附加解码{extra['tto_local_views_explicitly_checked']}张局部TTO和{extra['tto_full_views_explicitly_checked']}张完整TTO，连同120张FF共720张RGB视图。",
f"- 高斯成员选择数量、相机valid保持一致；局部TTO core有{extra['tto_core_masks_changed_count']}/{extra['tto_local_views_explicitly_checked']}条发生像素变化，最大{extra['max_core_changed_pixels']}像素。{extra['tokchk_rows']}条复核面积均不超过core；{extra['zero_paste_identity_checks']}条零贴回在六区域全部指标精确等于光流。",
f"- 混合最小coverage={extra['hybrid_coverage_min']}；参考光流相对第十轮最大绝对差：`{extra['reference_vs_round10_max_abs_difference']}`。每目标方法×区域行数：`{extra['rows_per_target']}`。",
f"- {env['reused_from']['file_count']}个prepare/flow/poses/tokens/compat_packages文件SHA256与round7相同，输入原图哈希和共享t也复核。GS/TTO重新运行，未重检测token，原图纹理重投影保持关闭。",
'- gspl：Python3.9.23、torch2.0.1/CUDA11.7、gsplat1.5.3、RTX3090；未替换共享环境包或外部源码。','',
'## 解释边界','',
'- 本轮仍优化同一类位置、协方差、不透明度、SH直流参数，不做加密/剪枝；但裁剪监督会改变目标函数实际支撑区域，框按优化开始时的投影计算并固定，分位数还会排除少量离群点。因此“只改速度”应理解为优化目标形式/参数化未换，不能视为与第十轮完全相同的数值迭代。',
'- 比较的300步跨轮质量含重新编码的轻微数值差异。当前只测试一个场景帧、五个预设步数，没有跨场景泛化、自动停止策略、统计显著性或实时系统结论。',
'- 主TTO只用输入视点监督；H/t来自前序离线信息，t最初涉及目标图联合VGGT；_alv控制使用目标图估计相机。oracle/+reg和上游拼图选优涉及真值，作为诊断单列，不参与固定主方法构造。',
'- 输入PSNR是监督框拟合程度，不是留出质量。几何/alpha/贴回区域同时变化，不能把所有损益只归为颜色拟合。SSIM沿用前景裁片实现，支撑域与PSNR/LPIPS不同。','',
'## 复现与归档','',
'```bash','cd /home/han/linux-han/local-gs-eval','export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH','export LGS_WORK_DIR=work/round11 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1','export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4','# 首次按README复制round7的prepare/flow/poses/tokens/compat_packages','python -m unittest discover -s tests -v','python scripts/run_anysplat.py --config configs/mofang_9cam.yaml','python scripts/evaluate.py --config configs/mofang_9cam.yaml','python scripts/validate_results.py configs/mofang_9cam.yaml','```','',
'上面为标准顺序执行方式。实际并行评估入口evaluate_parallel.py/evaluate_worker.py及run_experiment.sh、报告修复补丁、归档/绘图/报告脚本均随结果保存，可复查执行逻辑。',
'','上传：报告、全部CSV/summary、逐检查点计时/训练PSNR/监督框、支持域/合并校验、配置/环境/复用哈希、GS/flow/pose元数据/日志、10张主拼图和10张固定全部检查点对比图。输入token及800张掩码沿用同分支保留的第七轮。全部FF/TTO RGB和alpha在本机work/round11/gs，未全部上传；源脚本未保存优化高斯或优化器状态。原始数据/模型未上传，完整复现仍需要这些外部资源。前十轮结果保留。','']
(a/'REPORT.md').write_text('\n'.join(L));p=R/'README.md';s=p.read_text();prefix='> 本机第十一轮实测：[报告](results/mofang-9cam-round11-gspl-20261025/REPORT.md) · [完整汇总](results/mofang-9cam-round11-gspl-20261025/eval/summary.md) · [第十轮](results/mofang-9cam-round10-gspl-20261025/REPORT.md)。源提交fa4bbbd，裁剪监督与25/50/100/200/300步检查点。\n\n'
if not s.startswith('> 本机第十一轮'):p.write_text(prefix+s)
print(json.dumps({'rife_al':[q for q in summ if q['variant']=='rife' and q['pose_source']=='al'],'earliest_qualifying_step':earliest},indent=2,ensure_ascii=False))

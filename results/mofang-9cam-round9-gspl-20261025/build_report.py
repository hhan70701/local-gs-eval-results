from pathlib import Path
import csv,json,statistics
R=Path(__file__).resolve().parents[2];a=R/'results/mofang-9cam-round9-gspl-20261025';e=a/'eval'
rows=list(csv.DictReader((e/'metrics.csv').open()));val=json.loads((e/'validation.json').read_text());extra=json.loads((e/'extra_validation.json').read_text());env=json.loads((a/'environment.json').read_text());cfg=env['config'];ref=cfg['eval']['ref_flow'];variants=list(cfg['tokens']['variants']);how=['direct','w20','oracle'];sources={'GS_color':'','RP_GS':'_rpgs','RP_VGGT':'_rpvggt'};targets={s:sorted({int(r['target']) for r in rows if r['setup']==s}) for s in cfg['setups']};by={(r['setup'],int(r['target']),r['method'],r['region']):r for r in rows}
def meth(v,col,h):
 gv=f'gs_tok{v}448_nat_dil_al{sources[col]}_local';return f'hyb_token[{gv}]' if h=='direct' else f'hyb_tokchk_{h}[{gv}]'
def avg(s,m,reg,k):return statistics.mean(float(by[s,t,m,reg][k]) for t in targets[s])
def cw(p,rr):
 with p.open('w') as f:
  d=csv.DictWriter(f,fieldnames=list(rr[0]));d.writeheader();d.writerows(rr)
per=[];summ=[]
for s in targets:
 for v in variants:
  for col in sources:
   for h in how:
    m=meth(v,col,h);rr=[]
    for t in targets[s]:
     r=dict(setup=s,target=t,variant=v,color_source=col,how=h,uses_gt=(h=='oracle'))
     for reg in ('fg','object','rest'):
      for k in ('psnr','lpips'):
       r[f'{reg}_{k}']=float(by[s,t,m,reg][k]);r[f'{reg}_delta_flow_{k}']=r[f'{reg}_{k}']-float(by[s,t,ref,reg][k]);r[f'{reg}_delta_GS_color_{k}']=r[f'{reg}_{k}']-float(by[s,t,meth(v,'GS_color',h),reg][k])
     r['fg_not_worse']=r['fg_delta_flow_psnr']>=-1e-6 and r['fg_delta_flow_lpips']<=1e-6;rr.append(r);per.append(r)
    q=dict(setup=s,variant=v,color_source=col,how=h,uses_gt=(h=='oracle'),fg_not_worse_targets=sum(r['fg_not_worse'] for r in rr),targets=len(rr))
    for reg in ('fg','object','rest'):
     for k in ('psnr','lpips'):
      q[f'{reg}_{k}']=avg(s,m,reg,k);q[f'{reg}_delta_flow_{k}']=q[f'{reg}_{k}']-avg(s,ref,reg,k);q[f'{reg}_delta_GS_color_{k}']=q[f'{reg}_{k}']-avg(s,meth(v,'GS_color',h),reg,k)
    summ.append(q)
cw(e/'color_source_comparison.csv',summ);cw(e/'color_source_per_view.csv',per)
L=['# 第九轮实测：GS/VGGT 几何与输入原图纹理','',
'源代码：`luckyhan-mike/local-gs-eval@5987605`。工作目录 `work/round9`，归档名沿用主机启动日期20261025。本轮按默认配置重新运行GS/重投影、评估及验证，token/prepare/flow/poses/compat_packages来自round7。没有修改算法、阈值或评价代码，没有根据本轮真值调参重跑。','',
'## 主结果','',
'**固定rife主分支中，两种输入纹理重投影均未优于GS颜色，direct/w20/oracle下都明显退化。** cam3直接贴回：GS颜色26.376 dB / 0.053728，RP_GS为23.482 / 0.090784，RP_VGGT为24.516 / 0.099694。cam5连oracle重投影也未超过纯光流。RP_VGGT相对RP_GS虽然PSNR更高，但LPIPS更差，不支持两项质量均不差的替代结论。','',
'GS_color为局部高斯渲染颜色；RP_GS为全高斯期望深度+输入原图采样；RP_VGGT为内部VGGT深度前向投影+输入原图采样。direct为直接贴回，w20用光流实际t风险复核，oracle使用真值失败区，仅作诊断。各目标相机等权平均，PSNR↑、LPIPS↓。','',
'### 固定 rife token 的主对比','',
'| 设置 | 颜色来源 | 贴回 | fg PSNR | fg LPIPS | object PSNR | object LPIPS | rest PSNR | fg不差目标数 |','|---|---|---|---:|---:|---:|---:|---:|---:|']
for s in targets:
 L.append(f'| {s} | 纯光流 | — | {avg(s,ref,"fg","psnr"):.6f} | {avg(s,ref,"fg","lpips"):.6f} | {avg(s,ref,"object","psnr"):.6f} | {avg(s,ref,"object","lpips"):.6f} | {avg(s,ref,"rest","psnr"):.6f} | — |')
 for q in summ:
  if q['setup']==s and q['variant']=='rife':L.append(f"| {s} | {q['color_source']} | {q['how']} | {q['fg_psnr']:.6f} | {q['fg_lpips']:.6f} | {q['object_psnr']:.6f} | {q['object_lpips']:.6f} | {q['rest_psnr']:.6f} | {q['fg_not_worse_targets']}/{q['targets']} |")
L+=['','## 对照 README 判据（Codex 分析）','',
'以下先看固定rife的直接/oracle主分支；全部变体和w20不省略，见后面的原始表与CSV。不差目标数沿用上游1e−6容差，包含空贴回/门限关闭时的精确回退。','']
for s in targets:
 for col in ('RP_GS','RP_VGGT'):
  for h in ('direct','oracle'):
   q=next(q for q in summ if q['setup']==s and q['variant']=='rife' and q['color_source']==col and q['how']==h)
   L.append(f"- {s} / {col} / {h}：相对本轮GS颜色，fg ΔPSNR={q['fg_delta_GS_color_psnr']:+.6f} dB，ΔLPIPS={q['fg_delta_GS_color_lpips']:+.6f}；相对光流，fg ΔPSNR={q['fg_delta_flow_psnr']:+.6f}，ΔLPIPS={q['fg_delta_flow_lpips']:+.6f}。")
L+=['','### VGGT 几何与 GS 几何的输入纹理比较','']
for s in targets:
 for h in ('direct','oracle'):
  x=next(q for q in summ if q['setup']==s and q['variant']=='rife' and q['color_source']=='RP_VGGT' and q['how']==h);y=next(q for q in summ if q['setup']==s and q['variant']=='rife' and q['color_source']=='RP_GS' and q['how']==h)
  dp,dl=x['fg_psnr']-y['fg_psnr'],x['fg_lpips']-y['fg_lpips'];ok=dp>=-1e-6 and dl<=1e-6
  L.append(f'- {s} / {h}：RP_VGGT − RP_GS 的 fg ΔPSNR={dp:+.6f} dB，ΔLPIPS={dl:+.6f}；'+('两项均不差。' if ok else '两项未同时不差。'))
L+=['','## 全部纹理来源主表（上游输出）','']
summary=(e/'summary.md').read_text();L.append('### 纹理取自输入图'+summary.split('### 纹理取自输入图',1)[1].split('## 其余诊断',1)[0])
L+=['完整90组颜色来源/变体/贴回均值见 [color_source_comparison.csv](eval/color_source_comparison.csv)，逐视点见 [color_source_per_view.csv](eval/color_source_per_view.csv)，上游metrics.csv含原始全部方法/区域。','',
'## 输入深度与可见性诊断','',
'| 设置 | 输入相机 | VGGT与GS深度中位相对差 | plane RMS px | 编码高斯 | raw窗口边长 | 自渲染PSNR |','|---|---:|---:|---:|---:|---:|---:|']
for r in csv.DictReader((e/'depth_agreement.csv').open()):L.append(f"| {r['setup']} | {r['camera']} | {float(r['median_relative_depth_difference']):.4%} | {float(r['plane_rms_px']):.6f} | {r['num_gaussians']} | {r['window']} | {float(r['ctx_self_psnr']):.6f} |")
L+=['','这比较的是同一模型的VGGT深度与GS期望深度，二者有共同来源，且中位数可能掩盖边缘误差；不是与真实深度的精度比较。plane RMS/环带位移也不足以证明逐像素深度适合高频纹理反投影。','',
'[reproject_visibility.csv](eval/reproject_visibility.csv)保存每个目标的两侧/单侧/零侧可见比例，分母为warp前、带padding画布的有效深度像素，并非token core或有效前景；不同几何的分母也不同。不能直接把该表当成贴回区覆盖率。','',
'## 名义 core 与实际混合支持','',
'| 设置 / 几何（rife） | core中GS颜色可用比例 | core中重投影可用比例 | GS影响fg比例 | 重投影影响fg比例 | 最大权重差 |','|---|---:|---:|---:|---:|---:|']
sp=list(csv.DictReader((e/'paste_support.csv').open()))
for s in targets:
 for g in ('gs','vggt'):
  rr=[r for r in sp if r['setup']==s and r['variant']=='rife' and r['geometry']==g];keys=('core_available_gs_fraction','core_available_rp_fraction','gs_effective_fg_fraction','rp_effective_fg_fraction');vs=[statistics.mean(float(r[k]) for r in rr) for k in keys]
  L.append(f'| {s} / {g} | '+' | '.join(f'{v:.3%}' for v in vs)+f" | {max(float(r['weight_max_abs_difference']) for r in rr):.6f} |")
L+=['','名义core的PNG及valid在GS颜色与两种重投影分支中逐文件完全相同，但paste_weight还乘以各自alpha>0.5；缺失纹理会回退，羽化支持域也可能改变。上表影响比例以weight>1e−6统计，最大差取全部目标的最大值。全部变体见paste_support.csv。**同一个名义core不能单独证明有效混合权重相同**；颜色来源比较应结合支持差异阅读。',
'','RP_GS的虚拟深度来自全高斯期望深度，而GS颜色来自选出的局部高斯，两者还包含深度采样、可见性与合成规则的差异。当前比较测量的是这两条完整管线的结果，不能把所有差异只归因于纹理锐度。','',
'## 固定方法对比图','',
'新增10张固定rife、直接贴回对比图：GT、光流、GS颜色、GS深度+输入纹理、VGGT深度+输入纹理；第二行是core/重投影不可用区和×3平均绝对误差。没有按真值选最优变体。GT只用于展示裁片定位和误差图，不参与采样、可见性或贴回决策。','',
'例如 [cam3/目标3](figures/cam3/cam3_rife_color_sources.png)、[cam5/目标3](figures/cam5/cam3_rife_color_sources.png)。已检查cam3/目标3：输入纹理分支有明显错色/孔洞，VGGT分支可见网格状伪影。这是局部可见表现，完整质量以全部目标的数值为准，不据单图推断统一原因。','',
'## 运行与附加验证','',
f"- 14项数值测试通过，包括纹理平面反投影、遮挡可见性及虚拟相机对齐合成测试。上游验证{val['status']}：{val['metric_rows']}行指标、{val['methods']}方法、{val['auc_rows']}行AUC、{val['gs_renders']}张原始GS分支、{val['flow_renders']}张复用光流、{val['montages']}张主拼图；warnings={val['warnings']}。",
f"- 原验证脚本未枚举重投影目录；附加逐张解码并校验{extra['reprojection_views_explicitly_checked']}张RP RGB/alpha，连同原始120张，共220张RGB视图。{extra['core_identity_checks']}条core/valid与GS分支逐PNG字节相同，编码数、窗口、编码时间、自渲染和局部高斯统计也对应相同。",
f"- {extra['visibility_stats_rows']}条去重可见性记录三种比例均有限且和为1；{extra['tokchk_rows']}行复核面积非负且不超过core。{extra['zero_paste_identity_checks']}条零贴回在全部六区域的PSNR/SSIM/LPIPS/面积/覆盖率精确等于光流；混合最小coverage={extra['hybrid_coverage_min']}。",
f"- 每目标方法×区域行数：`{extra['rows_per_target']}`。参考光流相对第八轮最大绝对差：`{extra['reference_vs_round8_max_abs_difference']}`。",
f"- {env['reused_from']['file_count']}个prepare/flow/poses/tokens/compat_packages文件SHA256与round7逐项相同；输入原图哈希与两尺度pose光流的共享t也复核。token未重检测，GS重新编码/渲染。重新编码后点云数及几何会略有数值差异，颜色来源对照以本轮同次编码为基准，不把跨轮差直接当成算法变化。",
'- gspl：Python3.9.23、torch2.0.1/CUDA11.7、gsplat1.5.3、RTX3090。兼容e3nn0.5.6位于工作目录；未替换环境包或外部源码。后台current_stage.txt、runner_exit_code.txt记录完成状态。','',
'## 解释边界','',
'- 本轮VGGT深度直接来自AnySplat内部depth_dict，未单独跑一个去GS的VGGT系统。RP_VGGT虚拟深度虽不使用GS渲染，但core仍由GS生成，且相机/对齐流程及模型执行保留。若要证明可去掉GS，需要独立去除这些依赖并重新测量质量与时延。',
'- 输入原图重投影依赖逐像素深度、输入可见性、相机映射与采样一致性。合成平面测试通过未验证真实深度边缘；这里没有深度真值，也没有分离深度误差、遮挡筛选、填洞/近邻上采样、亚像素约定和alpha边界效应。当前伪影不能全部归因于GS或VGGT本身的几何。',
'- 主重投影只从真实输入图像采样，采用共享t的(1−t,t)权重，不使用目标真值误差作决策。H/t仍来自前序离线信息，t最初涉及目标图联合VGGT；_alv等历史控制与预处理边界沿用前轮。',
'- oracle使用core∩真值失败区，只是诊断参照；它未逐像素比较哪种补丁优于光流，不是所有融合策略的严格上限。+reg、风险扫描及上游拼图展示选优涉及真值，不参与固定主分支。',
'- 指标是单场景单帧、固定配置实测；没有统计显著性、跨场景有效性或端到端提速结论。SSIM沿用前景裁片实现，支撑域与PSNR/LPIPS不同。','',
'## 复现与归档','',
'```bash','cd /home/han/linux-han/local-gs-eval','export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH','export LGS_WORK_DIR=work/round9 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1','export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4','# 首次按README复制round7的prepare/flow/poses/tokens/compat_packages','python -m unittest discover -s tests -v','python scripts/run_anysplat.py --config configs/mofang_9cam.yaml','python scripts/evaluate.py --config configs/mofang_9cam.yaml','python scripts/validate_results.py configs/mofang_9cam.yaml','```','',
'上传本报告、完整评估CSV/summary、日志、配置/环境/复用哈希、GS/flow/pose元数据、10张上游主图和10张固定颜色来源对比图，以及归档/绘图/报告脚本。输入token图与800张掩码沿用保留在同分支的 [第七轮](../mofang-9cam-round7-gspl-20261025/REPORT.md)。全部GS/RP RGB与alpha保存在本机work/round9/gs，未全部上传；源脚本深度在运算中使用，未写出完整深度数组，归档提供深度差和可见性诊断。原图/模型未上传，完整复现需要这些外部数据。前八轮结果保留。','']
(a/'REPORT.md').write_text('\n'.join(L));readme=R/'README.md';text=readme.read_text();prefix='> 本机第九轮实测：[报告](results/mofang-9cam-round9-gspl-20261025/REPORT.md) · [完整汇总](results/mofang-9cam-round9-gspl-20261025/eval/summary.md) · [第八轮](results/mofang-9cam-round8-gspl-20261025/REPORT.md)。源提交5987605，重新运行GS和两种输入纹理重投影。\n\n'
if not text.startswith('> 本机第九轮'):readme.write_text(prefix+text)
print(json.dumps({'rife':[q for q in summ if q['variant']=='rife']},indent=2,ensure_ascii=False))

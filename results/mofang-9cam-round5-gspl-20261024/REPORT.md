# 第五轮实测：对齐域渲染与可见表面筛选

运行跨 2026-10-24–25（香港时间），沿用启动日期命名。上游 `luckyhan-mike/local-gs-eval@d193f7f`，工作目录 `work/round5`。两处必要兼容/报表修复见下文；没有调整阈值后挑选重跑。

## 结论

**对齐域渲染显著改善 cam3 的像素误差，但尚未全面优于纯光流。cam5 仍退化。** cam3 token `_al` 的 fg PSNR 从 22.604 提高到 25.266 dB，object PSNR 从 14.528 提高到 16.99 dB，object LPIPS 也降低；fg LPIPS 却变差，rest PSNR 下降。具体精确均值以下表为准。

| 设置 / 方法 | fg PSNR | fg LPIPS | object PSNR | object LPIPS | rest PSNR |
|---|---:|---:|---:|---:|---:|
| cam3 / `flow_s1.0_pose` | 22.603828 | 0.062884 | 14.528079 | 0.272433 | 33.533843 |
| cam3 / `flow_s0.5_pose` | 22.931311 | 0.061022 | 14.853054 | 0.238320 | 32.824745 |
| cam3 / `hyb_token[gs_token448_nat_dil_local]` | 18.910791 | 0.140952 | 14.578594 | 0.234323 | 23.792776 |
| cam3 / `hyb_token[gs_token448_nat_dil_al_local]` | 25.265661 | 0.082359 | 16.990215 | 0.176789 | 31.173408 |
| cam3 / `hyb_token[gs_token448_nat_dil_alv_local]` | 25.132611 | 0.082293 | 16.651547 | 0.181642 | 31.202229 |
| cam3 / `hyb_token_ringreg[gs_token448_nat_dil_al_local]` | 25.265661 | 0.082359 | 16.990215 | 0.176789 | 31.173408 |
| cam5 / `flow_s1.0_pose` | 28.000218 | 0.039572 | 20.413457 | 0.072142 | 31.455603 |
| cam5 / `flow_s0.5_pose` | 27.445607 | 0.041550 | 19.647693 | 0.081766 | 31.224452 |
| cam5 / `hyb_token[gs_token448_nat_dil_local]` | 23.614990 | 0.087933 | 16.236642 | 0.189990 | 26.986526 |
| cam5 / `hyb_token[gs_token448_nat_dil_al_local]` | 25.120254 | 0.077254 | 18.146779 | 0.155774 | 27.970760 |
| cam5 / `hyb_token[gs_token448_nat_dil_alv_local]` | 24.888870 | 0.077651 | 17.546739 | 0.158410 | 27.894915 |
| cam5 / `hyb_token_ringreg[gs_token448_nat_dil_al_local]` | 25.178999 | 0.076861 | 17.787146 | 0.158935 | 27.872404 |

## 两项关键诊断

| 设置 / 裁剪 | plane RMS (px) | 编码总高斯 | recon | core | 第四轮 core | core 减少 |
|---|---:|---:|---:|---:|---:|---:|
| cam3 / token | 2.211998 | 368407 | 143741 | 44542 | 82318 | 45.89% |
| cam3 / center | 2.778761 | 432956 | 116463 | 34484 | 66610 | 48.23% |
| cam5 / token | 2.297902 | 528340 | 207042 | 44185 | 89535 | 50.65% |
| cam5 / center | 2.451429 | 638686 | 171981 | 35490 | 72696 | 51.18% |

RMS 为约 2–3 px 的多像素拟合残差，说明输入几何/H 并非精确一致；没有预设合格阈值或独立标定，不能仅凭此宣称误差足够小，或把全部质量损失归因于此。合成几何测试通过不等于真实场景满足其假设。

core 减少约 46%–51%，recon 也减少约 24%–31%。这支持筛选更严格，但不证明保留的都是正确可见表面；两轮编码总高斯也略有变化，并非严格固定点云的单因素消融。AnySplat 仍编码整个 448×448 窗口，筛选发生在编码后；没有测量或声称端到端加速。

## 贴回范围

以下是配准和羽化前的 core，按每个目标相机先计算比例再等权平均。core 总面积 / fg 并非前景替换率。

| 设置 / 变体 | core 总面积 / fg | 真正替换 fg 比例 | core 位于有效 fg 外比例 |
|---|---:|---:|---:|
| cam3 / `gs_center448_nat_dil_al_local` | 51.33% | 49.32% | 3.85% |
| cam3 / `gs_center448_nat_dil_alv_local` | 51.31% | 49.34% | 3.78% |
| cam3 / `gs_center448_nat_dil_local` | 53.42% | 49.25% | 7.79% |
| cam3 / `gs_token448_nat_dil_al_local` | 50.60% | 48.72% | 3.69% |
| cam3 / `gs_token448_nat_dil_alv_local` | 50.60% | 48.75% | 3.63% |
| cam3 / `gs_token448_nat_dil_local` | 52.32% | 48.69% | 6.94% |
| cam5 / `gs_center448_nat_dil_al_local` | 38.94% | 37.22% | 4.32% |
| cam5 / `gs_center448_nat_dil_alv_local` | 38.97% | 37.23% | 4.37% |
| cam5 / `gs_center448_nat_dil_local` | 39.48% | 37.23% | 5.64% |
| cam5 / `gs_token448_nat_dil_al_local` | 38.57% | 37.04% | 3.90% |
| cam5 / `gs_token448_nat_dil_alv_local` | 38.56% | 37.04% | 3.88% |
| cam5 / `gs_token448_nat_dil_local` | 38.44% | 36.90% | 3.96% |

cam3 token `_al` 实际覆盖约 48.72% 前景，约 3.69% 的 core 在有效前景外；第四轮未插值 token 分别约 61.25% 和 41.87%。前景外贴回已明显收紧，但仍替换近一半前景，不能理解成只修补魔方。变化同时包含可见性筛选、对齐域渲染和光流前景限制，不能把收益拆分给单个因素。参考光流的 fg/object 均值与第四轮一致，主对比区域可核对。

已查看 cam3/目标3 的主拼图：魔方/手的部分形状得到改善，但局部 GS 仍有模糊、缺损，蓝色贴回区域延伸到头发、衣服与面部。主拼图按真值评分选择变体，仅作展示，不能替代固定方法全视点表格。

## README T1–T7 判断

- T1：复用第四轮输入 token，未重新检测；cam3 标记更多的面积趋势保留，检测正确性没有新增独立标签。
- T2：cam3 `_al`/`_alv` 贴回区 PSNR 提高，但 LPIPS 变差，未同时满足两个标准；cam5 两项都不如参考光流。
- T3：cam3 fg PSNR 与 object 两项改善，但 fg LPIPS/rest 退化，因此只能支持部分指标收益。cam5 不支持。
- T4：第五轮 `_al` 替代旧 `_int`。同一轮 token 的 cam3 fg：原 VGGT 18.91 dB、`_al` 25.27 dB、`_alv` 25.13 dB；坐标域修正改善明显，但 `_alv` 未进一步胜出，不能据此认定光心误差是唯一瓶颈。环带位移0也可能来自配准失败/回退，不是独立的对齐正确性证明。
- T5：cam3 对齐域直接贴回与 ringreg 完全相同；cam5 `_al` token 的 fg 略升、object 下降，不支持稳定收益。原 VGGT 控制的环带配准仍有部分作用。
- T6：cam3 token `_al` 优于 center `_al`；cam5 token 的 fg 更差、object 更好，无统一优胜者。两者都是编码整个裁剪窗口后筛选局部高斯。
- T7：cam5 `_al` token fg 25.12 vs 光流 28.00 dB，LPIPS 0.0773 vs 0.0396；不应直接在小基线启用这套替换规则。当前检测并没有自动避免负收益。

## 完整主表

以下复制上游 summary 的两张主表；均值为留出相机等权平均。PSNR↑、LPIPS↓。fg 指有效前景而非带绿幕的整张图；贴回区三种方法在同一变体的配准前 core 上比较，不同变体的 core 不同。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_center448_nat_dil_al_local | 51.3% | 20.24 / 0.0584 | 22.09 / 0.1002 | 22.09 / 0.1002 | 0.00 |
| cam3 | gs_center448_nat_dil_alv_local | 51.3% | 20.24 / 0.0584 | 22.07 / 0.0997 | 22.07 / 0.0997 | 0.00 |
| cam3 | gs_center448_nat_dil_local | 53.4% | 20.36 / 0.0576 | 15.22 / 0.1949 | 18.88 / 0.1350 | 7.98 |
| cam3 | gs_token448_nat_dil_al_local | 50.6% | 20.20 / 0.0585 | 22.78 / 0.0894 | 22.78 / 0.0894 | 0.00 |
| cam3 | gs_token448_nat_dil_alv_local | 50.6% | 20.21 / 0.0585 | 22.68 / 0.0890 | 22.68 / 0.0890 | 0.00 |
| cam3 | gs_token448_nat_dil_local | 52.3% | 20.44 / 0.0571 | 15.56 / 0.1848 | 18.69 / 0.1346 | 5.91 |
| cam5 | gs_center448_nat_dil_al_local | 38.9% | 25.64 / 0.0297 | 22.15 / 0.0783 | 21.57 / 0.0804 | 0.81 |
| cam5 | gs_center448_nat_dil_alv_local | 39.0% | 25.64 / 0.0295 | 22.18 / 0.0779 | 21.55 / 0.0808 | 0.83 |
| cam5 | gs_center448_nat_dil_local | 39.5% | 25.56 / 0.0297 | 20.41 / 0.0979 | 20.31 / 0.0929 | 2.55 |
| cam5 | gs_token448_nat_dil_al_local | 38.6% | 25.63 / 0.0295 | 21.86 / 0.0780 | 21.85 / 0.0757 | 0.34 |
| cam5 | gs_token448_nat_dil_alv_local | 38.6% | 25.64 / 0.0294 | 21.60 / 0.0784 | 22.10 / 0.0718 | 1.14 |
| cam5 | gs_token448_nat_dil_local | 38.4% | 25.69 / 0.0294 | 20.18 / 0.0946 | 21.01 / 0.0821 | 1.76 |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | flow_s0.5_pose | 22.93 / 0.0610 | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 |
| cam3 | hyb_token[gs_center448_nat_dil_al_local] | 24.63 / 0.0912 | 16.49 / 0.2117 | 17.29 / 0.0540 | 30.75 / 0.0418 |
| cam3 | hyb_token[gs_center448_nat_dil_alv_local] | 24.55 / 0.0913 | 16.38 / 0.2153 | 17.17 / 0.0541 | 30.75 / 0.0418 |
| cam3 | hyb_token[gs_center448_nat_dil_local] | 18.69 / 0.1486 | 14.19 / 0.2680 | 13.42 / 0.1035 | 23.31 / 0.1093 |
| cam3 | hyb_token[gs_token448_nat_dil_al_local] | 25.27 / 0.0824 | 16.99 / 0.1768 | 17.92 / 0.0481 | 31.17 / 0.0384 |
| cam3 | hyb_token[gs_token448_nat_dil_alv_local] | 25.13 / 0.0823 | 16.65 / 0.1816 | 17.70 / 0.0480 | 31.20 / 0.0381 |
| cam3 | hyb_token[gs_token448_nat_dil_local] | 18.91 / 0.1410 | 14.58 / 0.2343 | 13.59 / 0.0994 | 23.79 / 0.1081 |
| cam3 | hyb_token_ringreg[gs_center448_nat_dil_al_local] | 24.63 / 0.0912 | 16.49 / 0.2117 | 17.29 / 0.0540 | 30.75 / 0.0418 |
| cam3 | hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 24.55 / 0.0913 | 16.38 / 0.2153 | 17.17 / 0.0541 | 30.75 / 0.0418 |
| cam3 | hyb_token_ringreg[gs_center448_nat_dil_local] | 22.17 / 0.1184 | 14.49 / 0.2582 | 15.34 / 0.0790 | 28.05 / 0.0672 |
| cam3 | hyb_token_ringreg[gs_token448_nat_dil_al_local] | 25.27 / 0.0824 | 16.99 / 0.1768 | 17.92 / 0.0481 | 31.17 / 0.0384 |
| cam3 | hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 25.13 / 0.0823 | 16.65 / 0.1816 | 17.70 / 0.0480 | 31.20 / 0.0381 |
| cam3 | hyb_token_ringreg[gs_token448_nat_dil_local] | 21.76 / 0.1160 | 14.09 / 0.2396 | 14.69 / 0.0788 | 28.59 / 0.0712 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | flow_s0.5_pose | 27.45 / 0.0415 | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 |
| cam5 | hyb_token[gs_center448_nat_dil_al_local] | 25.49 / 0.0791 | 17.55 / 0.1887 | 16.87 / 0.0327 | 28.30 / 0.0568 |
| cam5 | hyb_token[gs_center448_nat_dil_alv_local] | 25.55 / 0.0786 | 17.56 / 0.1838 | 16.99 / 0.0324 | 28.36 / 0.0562 |
| cam5 | hyb_token[gs_center448_nat_dil_local] | 24.31 / 0.0891 | 16.74 / 0.1923 | 16.25 / 0.0401 | 26.98 / 0.0692 |
| cam5 | hyb_token[gs_token448_nat_dil_al_local] | 25.12 / 0.0773 | 18.15 / 0.1558 | 16.41 / 0.0338 | 27.97 / 0.0598 |
| cam5 | hyb_token[gs_token448_nat_dil_alv_local] | 24.89 / 0.0777 | 17.55 / 0.1584 | 15.94 / 0.0350 | 27.89 / 0.0598 |
| cam5 | hyb_token[gs_token448_nat_dil_local] | 23.61 / 0.0879 | 16.24 / 0.1900 | 14.50 / 0.0451 | 26.99 / 0.0742 |
| cam5 | hyb_token_ringreg[gs_center448_nat_dil_al_local] | 25.11 / 0.0817 | 16.93 / 0.1961 | 16.55 / 0.0361 | 27.93 / 0.0591 |
| cam5 | hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 25.12 / 0.0816 | 16.96 / 0.1905 | 16.67 / 0.0359 | 27.91 / 0.0590 |
| cam5 | hyb_token_ringreg[gs_center448_nat_dil_local] | 24.32 / 0.0898 | 15.81 / 0.2150 | 15.63 / 0.0431 | 27.31 / 0.0648 |
| cam5 | hyb_token_ringreg[gs_token448_nat_dil_al_local] | 25.18 / 0.0769 | 17.79 / 0.1589 | 16.58 / 0.0335 | 27.87 / 0.0594 |
| cam5 | hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 25.46 / 0.0760 | 17.81 / 0.1575 | 17.11 / 0.0319 | 28.07 / 0.0570 |
| cam5 | hyb_token_ringreg[gs_token448_nat_dil_local] | 24.55 / 0.0837 | 16.54 / 0.1906 | 15.82 / 0.0386 | 27.52 / 0.0665 |


## 运行、修复与验证

- gspl：Python 3.9.23、torch 2.0.1/CUDA 11.7、gsplat 1.5.3、RTX 3090。工作目录兼容包 e3nn 0.5.6 和 Python3.9 AnySplat 复制版本；未替换共享环境或外部仓库。
- 从 `work/round4` 独立复制 prepare、flow、poses、tokens、compat_packages。重跑 run_anysplat、evaluate、validate。输入 SHA256 保存在 environment.json；两尺度 pose flow 的每个 t 与 poses.t_pose 精确相同。
- 修复1：`lgs/anysplat_wrap.py` 的 RGB+ED 应传3通道 RGB background；本机 gsplat 自动附加 depth 通道。上游传4通道会得到5通道并触发断言。仅修正接口，不改变筛选参数。初始错误日志已保留。
- 修复2：`scripts/evaluate.py` 新 aligned pose_diag 只有 plane_rms_px，旧汇总直接读 ctx_rot_err_deg 导致 KeyError；改为缺失时读取原始编码器一致性诊断。它不是 aligned 位姿误差，plane RMS 另表保存。初始错误日志已保留。
- 修复后11项数值测试通过；产物验证 PASS、无 warnings：4320行质量指标、72方法、50行AUC、120张GS和60张光流、10张主拼图。光流复用不计为本轮新推理。
- 附加核对：每个目标432行（72方法×6区域）、180行贴回指标全部有限、60条环带记录；混合方法 coverage=1；局部高斯 core≤recon≤总数仅作数量检查。详见 extra_validation.json。

## 解释边界

- 输入 token、可见性筛选、零视差平面拟合、core前景限制与环带配准不使用目标真值误差作决策；主贴回参考为光流。共享 H/t 是前序离线信息，t 最初涉及目标图联合VGGT；原始VGGT与 `_alv` 控制仍涉及目标图估计光心。运行还保留联合VGGT的历史路径，不能把本实验称为完全无目标图依赖的端到端部署协议。
- 自动summary声称“全程不用真值”须以上述范围理解。其后半段 `pose_src` 旧逻辑把 `_al`/`_alv` 也归类为 vggt，分类选优文字不可信；主表/原始CSV变体名与meta.pose_source正确，本报告明确区分。
- +reg使用真值配准，oracle失败区/风险阈值扫描使用真值，属于独立诊断；不能据此判断可部署方法。主贴回未使用这些上限决策。
- SSIM沿用上游前景裁片实现，支撑域与PSNR/LPIPS并非完全相同；不据单一SSIM作结论。单场景单帧，未给统计显著性或跨场景结论。

## 复现与产物

```bash
cd /home/han/linux-han/local-gs-eval
export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH
export LGS_WORK_DIR=work/round5 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1
export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4
# 首次执行前按README复制round4的prepare/flow/poses/tokens/compat_packages
python scripts/run_anysplat.py --config configs/mofang_9cam.yaml
python scripts/evaluate.py --config configs/mofang_9cam.yaml
python scripts/validate_results.py configs/mofang_9cam.yaml
python -m unittest discover -s tests -v
```

上传：本报告、配置/环境/输入哈希、日志、全部评估CSV与summary、GS/flow/pose元数据、输入token图和掩码、10张主拼图、两处补丁及源代码；历史四轮结果保留。未上传原始数据/模型/全部GS渲染及fullgs诊断拼图，保留于本机work。此仓库是可审查的结果归档，复现完整推理仍需要原始数据与模型。

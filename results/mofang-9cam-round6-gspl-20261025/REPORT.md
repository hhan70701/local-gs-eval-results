# 第六轮实测：r5 / rife / strict token 对比

源代码：`luckyhan-mike/local-gs-eval@3e4177a35cab0efd2bcc1325f5728cf8e5b01532`。主工作目录 `work/round6`，归档名沿用主机启动日期 20261025。按第六轮默认配置运行，**本轮没有修改算法、阈值或评估源码**；第五轮两处兼容修复已由上游合入。

## 主结果

**cam3 的 rife/strict 在前景 PSNR、LPIPS 两项均值上都优于纯光流；但只有3/6个目标视点同时改善。cam5 仍没有收益，strict 反而明显退化。** cam3 strict 前景为26.305 dB / 0.055820，相对光流22.604 / 0.062884；rest仍下降0.237 dB。

各目标相机等权平均，PSNR↑、LPIPS↓。下表为固定 `_al`（输入光心按共享 t 插值）直接贴回结果；不是挑选目标相机最优变体。输入 core 和贴回区面积含义不同。

| 设置 | token | 输入 core / fg | core 覆盖 fg | fg PSNR | fg LPIPS | object PSNR | object LPIPS | rest PSNR | fg 双指标胜出视点 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| cam3 | 纯光流 | — | — | 22.603828 | 0.062884 | 14.528079 | 0.272433 | 33.533843 | — |
| cam3 | r5 | 30.69% | 48.81% | 25.323181 | 0.082607 | 17.086720 | 0.178896 | 31.217540 | 0/6 |
| cam3 | rife | 10.83% | 19.38% | 26.148063 | 0.057882 | 16.829629 | 0.178932 | 33.078350 | 3/6 |
| cam3 | strict | 8.40% | 15.59% | 26.305252 | 0.055820 | 17.008761 | 0.189074 | 33.296857 | 3/6 |
| cam5 | 纯光流 | — | — | 28.000218 | 0.039572 | 20.413457 | 0.072142 | 31.455603 | — |
| cam5 | r5 | 15.70% | 37.05% | 25.144088 | 0.077066 | 18.149376 | 0.152897 | 28.017209 | 0/4 |
| cam5 | rife | 3.89% | 14.51% | 27.812864 | 0.047412 | 19.154756 | 0.132247 | 30.582590 | 0/4 |
| cam5 | strict | 2.39% | 9.52% | 23.998078 | 0.061662 | 16.168331 | 0.185391 | 27.679858 | 0/4 |

## 对照 README 目标（Codex 分析）

- cam3 / rife：fg ΔPSNR=+3.544235 dB，ΔLPIPS=-0.005003；满足均值上 PSNR、LPIPS 同时优于纯光流。rest ΔPSNR=-0.455493 dB。
- cam3 / strict：fg ΔPSNR=+3.701424 dB，ΔLPIPS=-0.007065；满足均值上 PSNR、LPIPS 同时优于纯光流。rest ΔPSNR=-0.236986 dB。
- cam5 / rife：fg ΔPSNR=-0.187354 dB，ΔLPIPS=+0.007840；未满足均值上 PSNR、LPIPS 同时优于纯光流。rest ΔPSNR=-0.873013 dB。
- cam5 / strict：fg ΔPSNR=-4.002140 dB，ΔLPIPS=+0.022090；未满足均值上 PSNR、LPIPS 同时优于纯光流。rest ΔPSNR=-3.775744 dB。

上述是该场景该帧的实测判据，不构成跨场景有效性结论。较小贴回区本身不证明检测准确，需结合贴回区同像素比较、物体和可靠区域损益。README 的约27 dB / 0.057 是待比较的历史oracle诊断值，不是本轮自动获得的实测结论。

## 检测、裁剪和几何诊断

| 设置 / token | raw窗口边长 | 编码高斯 | recon | core | plane RMS px | 输入自渲染 PSNR |
|---|---:|---:|---:|---:|---:|---:|
| cam3 / r5 | 911 | 368633 | 143549 | 44563 | 2.215796 | 29.147508 |
| cam3 / rife | 726 | 312491 | 74386 | 23963 | 1.834537 | 28.281681 |
| cam3 / strict | 576 | 209627 | 50566 | 20521 | 1.778562 | 27.031722 |
| cam5 / r5 | 917 | 528485 | 207221 | 44256 | 2.312689 | 29.466884 |
| cam5 / rife | 617 | 357227 | 76823 | 26863 | 1.551147 | 27.816713 |
| cam5 / strict | 448 | 186830 | 54615 | 15447 | 3.052732 | 21.237815 |

每个 token 变体按其 recon 外接框重新裁剪、编码一次，再渲染 `_al`、`_alv` 的完整/局部版本。**因此这不是固定同一组高斯、仅缩小贴回掩码的消融**：掩码、输入窗口、重采样尺度、预测几何与纹理都会一起变化。尤其 cam5 strict 的输入自渲染约21.24 dB，窗口与旧29 dB基准不同，不能直接解释成同一输入上的模型退化。

合成几何测试通过只验证其构造假设。真实平面拟合仍有1.55–3.05 px残差，不能据此宣称真实输入几何精确一致；残差也不是目标视点误差。高斯筛选在完整窗口编码后执行，没有测量端到端加速。

已查看 cam3 strict 输入4叠加图：红色主要覆盖魔方、手和前臂/遮挡附近，右臂仍有小标记；蓝色重建外扩区也延伸至头发与身体。它不是独立的真值检测标签。24张输入叠加图和全部aligned/raw掩码均随报告保存。

## 目标贴回范围

配准/羽化前core；按目标视点先求比例再平均。core总面积/fg可以包含前景外像素，并不等于前景替换比例。

| 设置 / token (_al) | core总面积 / fg | core覆盖fg | core中有效fg外比例 |
|---|---:|---:|---:|
| cam3 / r5 | 50.71% | 48.81% | 3.71% |
| cam3 / rife | 19.87% | 19.38% | 2.30% |
| cam3 / strict | 15.90% | 15.59% | 1.74% |
| cam5 / r5 | 38.58% | 37.05% | 3.91% |
| cam5 / rife | 15.07% | 14.51% | 3.60% |
| cam5 / strict | 9.89% | 9.52% | 3.49% |

## 全部主表（上游输出）

包含所有 token 变体、`_al` / `_alv` 与 ringreg。贴回区表是每个变体配准前同一组core像素的比较；不同变体贴回区不同，不宜据其跨变体分数直接排名。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_tokr5448_nat_dil_al_local | 50.7% | 20.21 / 0.0585 | 22.84 / 0.0890 | 22.84 / 0.0890 | 0.00 |
| cam3 | gs_tokr5448_nat_dil_alv_local | 50.7% | 20.22 / 0.0586 | 22.76 / 0.0889 | 22.76 / 0.0889 | 0.00 |
| cam3 | gs_tokrife448_nat_dil_al_local | 19.9% | 16.71 / 0.0642 | 21.26 / 0.0588 | 21.16 / 0.0595 | 0.27 |
| cam3 | gs_tokrife448_nat_dil_alv_local | 19.8% | 16.72 / 0.0644 | 21.25 / 0.0589 | 21.13 / 0.0588 | 0.27 |
| cam3 | gs_tokstrict448_nat_dil_al_local | 15.9% | 15.87 / 0.0914 | 21.18 / 0.0727 | 20.95 / 0.0740 | 0.29 |
| cam3 | gs_tokstrict448_nat_dil_alv_local | 15.8% | 15.88 / 0.0913 | 20.77 / 0.0724 | 20.64 / 0.0737 | 0.36 |
| cam5 | gs_tokr5448_nat_dil_al_local | 38.6% | 25.63 / 0.0297 | 21.87 / 0.0770 | 22.14 / 0.0735 | 0.78 |
| cam5 | gs_tokr5448_nat_dil_alv_local | 38.6% | 25.64 / 0.0298 | 21.63 / 0.0775 | 22.15 / 0.0713 | 1.05 |
| cam5 | gs_tokrife448_nat_dil_al_local | 15.1% | 23.40 / 0.0375 | 22.41 / 0.0597 | 22.21 / 0.0611 | 1.44 |
| cam5 | gs_tokrife448_nat_dil_alv_local | 15.1% | 23.41 / 0.0379 | 22.24 / 0.0595 | 22.59 / 0.0582 | 0.61 |
| cam5 | gs_tokstrict448_nat_dil_al_local | 9.9% | 22.43 / 0.0668 | 15.64 / 0.2285 | 16.81 / 0.1982 | 10.27 |
| cam5 | gs_tokstrict448_nat_dil_alv_local | 9.9% | 22.43 / 0.0689 | 15.47 / 0.2287 | 17.54 / 0.1870 | 6.69 |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | flow_s0.5_pose | 22.93 / 0.0610 | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_local] | 25.32 / 0.0826 | 17.09 / 0.1789 | 18.00 / 0.0480 | 31.22 / 0.0383 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.21 / 0.0823 | 16.76 / 0.1825 | 17.80 / 0.0478 | 31.26 / 0.0380 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.15 / 0.0579 | 16.83 / 0.1789 | 18.20 / 0.0397 | 33.08 / 0.0265 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 26.10 / 0.0581 | 16.62 / 0.1863 | 18.16 / 0.0401 | 33.07 / 0.0266 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 26.31 / 0.0558 | 17.01 / 0.1891 | 18.36 / 0.0392 | 33.30 / 0.0252 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.98 / 0.0565 | 16.12 / 0.1983 | 17.91 / 0.0400 | 33.29 / 0.0253 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.32 / 0.0826 | 17.09 / 0.1789 | 18.00 / 0.0480 | 31.22 / 0.0383 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.21 / 0.0823 | 16.76 / 0.1825 | 17.80 / 0.0478 | 31.26 / 0.0380 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 26.06 / 0.0582 | 16.76 / 0.1805 | 18.12 / 0.0406 | 33.07 / 0.0266 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 26.04 / 0.0582 | 16.61 / 0.1859 | 18.11 / 0.0408 | 33.07 / 0.0266 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 26.11 / 0.0563 | 16.77 / 0.1915 | 18.12 / 0.0400 | 33.25 / 0.0253 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.87 / 0.0569 | 16.09 / 0.2010 | 17.81 / 0.0409 | 33.26 / 0.0254 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | flow_s0.5_pose | 27.45 / 0.0415 | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_local] | 25.14 / 0.0771 | 18.15 / 0.1529 | 16.39 / 0.0338 | 28.02 / 0.0597 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 24.94 / 0.0773 | 17.62 / 0.1566 | 15.97 / 0.0350 | 27.95 / 0.0595 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.81 / 0.0474 | 19.15 / 0.1322 | 18.67 / 0.0205 | 30.58 / 0.0361 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 27.76 / 0.0473 | 18.95 / 0.1341 | 18.54 / 0.0206 | 30.65 / 0.0359 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 24.00 / 0.0617 | 16.17 / 0.1854 | 14.83 / 0.0364 | 27.68 / 0.0463 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 23.89 / 0.0614 | 16.01 / 0.1860 | 14.70 / 0.0359 | 27.60 / 0.0465 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.51 / 0.0766 | 17.91 / 0.1553 | 17.05 / 0.0325 | 28.14 / 0.0580 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.54 / 0.0755 | 17.86 / 0.1554 | 17.12 / 0.0318 | 28.20 / 0.0565 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 27.65 / 0.0482 | 19.00 / 0.1307 | 18.62 / 0.0219 | 30.45 / 0.0361 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 27.84 / 0.0468 | 19.42 / 0.1275 | 18.91 / 0.0200 | 30.57 / 0.0356 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 24.68 / 0.0626 | 16.06 / 0.1864 | 15.69 / 0.0335 | 27.82 / 0.0476 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.43 / 0.0589 | 16.63 / 0.1788 | 15.78 / 0.0328 | 29.18 / 0.0433 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.2%） | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 |
| cam3 | r5 | 30.7% | 50.7% | 25.32 / 0.0826 | 17.09 / 0.1789 | 31.22 |
| cam3 | rife | 10.8% | 19.9% | 26.15 / 0.0579 | 16.83 / 0.1789 | 33.08 |
| cam3 | strict | 8.4% | 15.9% | 26.31 / 0.0558 | 17.01 / 0.1891 | 33.30 |
| cam5 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.2%） | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 |
| cam5 | r5 | 15.7% | 38.6% | 25.14 / 0.0771 | 18.15 / 0.1529 | 28.02 |
| cam5 | rife | 3.9% | 15.1% | 27.81 / 0.0474 | 19.15 / 0.1322 | 30.58 |
| cam5 | strict | 2.4% | 9.9% | 24.00 / 0.0617 | 16.17 / 0.1854 | 27.68 |


## 验证与运行记录

- 11项数值测试全部通过。产物验证 PASS：4320行指标、72种方法、50行AUC、120张GS、60张复用光流、10张主拼图。warnings=[]。
- 每目标方法/区域行数：`{'cam3/1': 432, 'cam3/2': 432, 'cam3/3': 432, 'cam3/5': 432, 'cam3/6': 432, 'cam3/7': 432, 'cam5/1': 432, 'cam5/3': 432, 'cam5/5': 432, 'cam5/7': 432}`；180行贴回指标均有限，60行环带记录；混合方法最小coverage=1.0。高斯 core≤recon≤编码数仅为数量关系检查。
- gspl：Python3.9.23、torch2.0.1/CUDA11.7、gsplat1.5.3、RTX3090。独立复制round5的prepare/flow/poses/compat_packages，重新检测全部token、重新编码GS。环境未替换；兼容e3nn0.5.6位于工作目录。
- 输入SHA256重新核对通过；两尺度pose光流的每个t与poses.t_pose精确相同；没有复跑光流。r5重新检测存在微小重复运行差异：输入aligned core每图相差2–32像素，详见r5_mask_repeatability.csv。GS编码总数也略有变化。
- 初次评估在cam3完成后中断，未写出最终CSV；保留3_evaluate_interrupted.log。随后完整重算评估和validate；最终CSV/summary来自完整成功运行，GS没有因此重跑。

## 解释边界

- 本轮仅有token裁剪，不再运行center/fg整窗口变体。evaluate.py的full_frame列表为空，valid交集在前景限制前为整幅图；第五轮有center等变体参与valid交集。已逐目标核对：两轮10个目标的fg像素集合相同（domain_comparison.csv新增前景比例均为0）；完整图的valid策略虽不同，本场景fg未受影响。另按逐目标/逐区域核对，参考光流的PSNR、LPIPS和区域面积与第五轮最大绝对差均为0（extra_validation.json）。object/其他区域仍按各自定义核对，优先比较本轮r5/rife/strict与本轮光流。所有混合方法在原始局部GS覆盖区外回退光流。
- 检测、局部可见性、平面拟合、core前景限制、环带配准不使用目标真值误差作决策；参考为输入相机或光流。共享H/t来自前序离线信息，t最初含目标图联合VGGT；`_alv`使用目标图估计光心，历史联合VGGT代码路径仍运行。上游“可部署/全程不用真值”须限定到给定这些离线映射和相机信息后的主贴回决策，不是完全无目标图依赖的端到端协议。
- +reg为用真值ECC配准的诊断；oracle_fail、风险阈值扫描以及主拼图挑选展示变体涉及真值。它们不参与固定hyb_token/ringreg构造，不能当成实际可部署选择器。环带位移0可能是ECC失败/无位移，超过20px回退，不能仅以位移推断几何正确。
- PSNR/LPIPS按代码的区域定义计算。SSIM沿用前景裁片支撑域，不应假定与另外两个指标完全相同。仅单场景单帧，没有统计显著性检验。

## 复现

```bash
cd /home/han/linux-han/local-gs-eval
export PATH=/home/han/anaconda3/envs/gspl/bin:$PATH
export LGS_WORK_DIR=work/round6 HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1
export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4
# 首次运行按README复制round5的prepare/flow/poses/compat_packages
python scripts/detect_tokens.py --config configs/mofang_9cam.yaml
python scripts/run_anysplat.py --config configs/mofang_9cam.yaml
python scripts/evaluate.py --config configs/mofang_9cam.yaml
python scripts/validate_results.py configs/mofang_9cam.yaml
python -m unittest discover -s tests -v
```

归档包含配置/环境/输入哈希、全部评估CSV和summary、输入token叠加图/全部掩码、10张主拼图、日志和GS/flow/pose元数据。保留前五轮历史结果。原始数据、模型、完整GS渲染与fullgs诊断拼图仍在本机work，未上传；复现推理需要这些外部数据和模型。

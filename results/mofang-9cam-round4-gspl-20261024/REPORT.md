# 第四轮实测：输入 token → 局部 GS → 虚拟视点贴回

日期：2026-10-24。源提交：`luckyhan-mike/local-gs-eval@0d506f0`。按上游默认配置运行，未修改算法、阈值或评价代码。本轮工作目录 `work/round4/`，前三轮结果保留。

## 结论

**当前实现未验证“局部 GS 贴回优于纯光流”。环带配准能缓解未插值 GS 的部分误差，但仍低于光流；`_int` 位姿插值明显退化。**

- cam3 token 窗口、不带 `_int`：直接贴回 fg **18.380 dB / 0.157061 LPIPS**，环带配准后 **20.538 / 0.132334**，仍低于参考光流 **22.604 / 0.062884**，也低于 scale0.5 光流 **22.931 / 0.061022**。
- object 区有局部改善：cam3 token 直接贴回为 **14.908 dB / 0.221763**，参考光流 **14.528 / 0.272433**。但 rest 从 **33.534 降至 21.860 dB**，抵消了物体局部收益；环带配准后 object 为 **14.778 / 0.224453**，rest 回升到 25.024 dB，仍不足以改善整体。
- `_int` 没有减少错位：cam3 token `_int_local` 直接贴回 fg 仅 **12.043 dB / 0.303839**。20 条 `_int` 环带记录中，18 条位移超过 20 px 被拒绝，另外 2 条位移为 0；环带配准结果的指标与直接贴回相同。
- 输入 core 比例确实较小，但投影贴回区明显扩大。cam3 未插值 token 变体平均替换约 **61.25% 的有效前景**，贴回区域约 **41.87% 在有效前景之外**。因此这次不是只替换魔方附近的一小块。
- cam5 同样退化：token＋环带配准 fg **22.188 / 0.103443**，参考光流 **28.000 / 0.039572**。现有结果不支持直接采用这套触发、投影与贴回规则。

## 运行与可复现性

- 使用既有 `gspl`：Python 3.9.23、torch 2.0.1/CUDA 11.7、gsplat 1.5.3、RTX 3090；e3nn 0.5.6 仅在工作目录局部覆盖，环境包和外部 AnySplat/Practical-RIFE 均未修改。
- 从第二轮独立复制 `prepare/`、6 种光流结果、`poses/` 和兼容包，依次运行 detect_tokens、run_anysplat、evaluate、validate。没有运行第三轮标定，也没有复用第三轮 cal/posecal。
- **逐项精确核对了 `poses/<setup>.json` 的 t 与两种尺度 `flow_*_pose/meta.json`，完全相等**；GS 脚本没有覆盖这些 pose 文件。所有输入 SHA256 也与第二轮一致。
- **10 项数值测试全部通过**；上游产物验证 PASS：**3000 行质量指标、50 种方法、50 行 AUC、80 张 GS、60 张光流、10 张主拼图**。
- 附加检查：每个目标相机都有 50 方法 × 6 区域；120 行贴回指标、40 行环带记录、40 行真值配准诊断、90 行风险扫描；所有混合方法覆盖率为 1，贴回指标均有限，局部高斯满足 core ⊆ recon ⊆ 编码总数（数量关系检查）。详见 [extra_validation.json](eval/extra_validation.json)。

## T1：输入相机上的 token

已查看 cam3 相机 4 的叠加图：魔方、手、前臂有明显标记，也包含头发/面部轮廓、衣服与身体边缘，不能理解为只标出了魔方。

| 设置 | 输入相机 | core / 前景 | recon / 前景 |
|---|---:|---:|---:|
| cam3 | 0 | 28.84% | 82.67% |
| cam3 | 4 | 37.57% | 97.29% |
| cam3 | 8 | 25.65% | 92.04% |
| cam5 | 0 | 18.06% | 75.12% |
| cam5 | 2 | 21.67% | 79.13% |
| cam5 | 4 | 16.31% | 70.04% |
| cam5 | 6 | 15.31% | 75.01% |
| cam5 | 8 | 7.16% | 68.11% |

cam3 平均 core 多于 cam5，支持“基线越大，标记越多”的现象；但 recon 已覆盖 cam3 前景的 82.7%–97.3%、cam5 的 68.1%–79.1%。检测是否准确仍需独立标签或更细粒度验证，不能只用面积趋势证明。

8 张输入叠加图及全部 fail/depth/core/recon 的 aligned/raw 掩码均已保存。例如 [cam3 输入 0](tokens/cam3/cam0_overlay.png)、[输入 4](tokens/cam3/cam4_overlay.png)、[输入 8](tokens/cam3/cam8_overlay.png)。颜色与代码一致：红为 failure，黄为 depth，蓝为 recon。

## T2：贴回区域内，同一组像素比较

下表来自 `paste.csv`，三种方法在每个变体的原始投影 core 上评价，然后对目标相机等权平均。不同变体的 core 不同，不能把跨变体的这张表当作完全相同的评价区域。

| 设置 | 局部变体 | 光流 PSNR / LPIPS | 直接贴回 | 环带配准贴回 | 平均环带位移 |
|---|---|---:|---:|---:|---:|
| cam3 | gs_center448_nat_dil_int_local | 22.760 / 0.060383 | 11.916 / 0.277944 | 11.916 / 0.277944 | 35.20 px |
| cam3 | gs_center448_nat_dil_local | 22.787 / 0.061416 | 17.840 / 0.164770 | 19.449 / 0.134282 | 11.10 px |
| cam3 | gs_token448_nat_dil_int_local | 22.688 / 0.061655 | 11.802 / 0.285200 | 11.802 / 0.285200 | 27.34 px |
| cam3 | gs_token448_nat_dil_local | 22.707 / 0.062240 | 17.884 / 0.165825 | 19.966 / 0.131057 | 7.76 px |
| cam5 | gs_center448_nat_dil_int_local | 28.164 / 0.037727 | 11.977 / 0.269268 | 11.977 / 0.269268 | 34.90 px |
| cam5 | gs_center448_nat_dil_local | 28.085 / 0.037459 | 20.857 / 0.111242 | 21.533 / 0.105683 | 1.25 px |
| cam5 | gs_token448_nat_dil_int_local | 28.103 / 0.037123 | 11.918 / 0.269064 | 11.918 / 0.269064 | 34.31 px |
| cam5 | gs_token448_nat_dil_local | 28.074 / 0.037856 | 20.952 / 0.107090 | 21.975 / 0.099368 | 0.99 px |

**T2 不成立**：所有局部变体在自己的贴回区里，直接贴回和环带配准都未同时优于光流的 PSNR/LPIPS。

## T3/T5/T6/T7：前景与物体区

PSNR 越高、LPIPS 越低越好。fg 是有效域内前景，object 是魔方附近区域，均不是整张 1920×1080 图包含背景的全像素平均。混合方法 fg 覆盖为 1；原始局部 GS 的 fg/rest 仅供诊断，局部点云本来就不负责整幅画面。

### cam3

| 方法 | fg PSNR | fg LPIPS | object PSNR | object LPIPS | rest PSNR |
|---|---:|---:|---:|---:|---:|
| flow_s1.0_pose | 22.604 | 0.062884 | 14.528 | 0.272433 | 33.534 |
| flow_s0.5_pose | 22.931 | 0.061022 | 14.853 | 0.238320 | 32.825 |
| hyb_token[gs_token448_nat_dil_local] | 18.380 | 0.157061 | 14.908 | 0.221763 | 21.860 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 20.538 | 0.132334 | 14.778 | 0.224453 | 25.024 |
| hyb_token[gs_center448_nat_dil_local] | 18.392 | 0.163068 | 14.852 | 0.243210 | 21.793 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 20.095 | 0.141242 | 13.180 | 0.286970 | 24.881 |
| hyb_token[gs_token448_nat_dil_int_local] | 12.043 | 0.303839 | 9.690 | 0.421964 | 13.844 |
| hyb_token[gs_center448_nat_dil_int_local] | 12.080 | 0.306652 | 9.913 | 0.424841 | 13.857 |

### cam5

| 方法 | fg PSNR | fg LPIPS | object PSNR | object LPIPS | rest PSNR |
|---|---:|---:|---:|---:|---:|
| flow_s1.0_pose | 28.000 | 0.039572 | 20.413 | 0.072142 | 31.456 |
| flow_s0.5_pose | 27.446 | 0.041550 | 19.648 | 0.081766 | 31.224 |
| hyb_token[gs_token448_nat_dil_local] | 21.296 | 0.109259 | 16.352 | 0.178998 | 23.003 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 22.188 | 0.103443 | 17.077 | 0.169886 | 23.756 |
| hyb_token[gs_center448_nat_dil_local] | 21.424 | 0.112062 | 16.912 | 0.179088 | 22.664 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 21.905 | 0.107996 | 17.384 | 0.174479 | 23.027 |
| hyb_token[gs_token448_nat_dil_int_local] | 12.997 | 0.275368 | 9.526 | 0.478932 | 13.879 |
| hyb_token[gs_center448_nat_dil_int_local] | 12.985 | 0.277782 | 9.635 | 0.491532 | 13.847 |


- **T3：整体没有变好。** cam3 object 的局部改善没有抵消 rest 的退化；cam5 object 和 fg 均不如参考光流。
- **T4：`_int` 失败。** token/center 两种窗口在 cam3/cam5 都显著退化。共享相同 t 的数值核对通过，但这不足以保证“对齐域光流插值”和“原图相机位姿/内参的 3D 插值”对应同一成像映射。确切原因尚未定位，不能把这一次插值实现的失败归结为所有统一相机方案不可行。
- **T5：环带配准对未插值 GS 有部分帮助。** cam3 token fg 从 18.380 提高到 20.538 dB（+2.158），cam5 从 21.296 提高到 22.188（+0.893），但均未追上纯光流。cam3 object 反而由 14.908 降到 14.778 dB，说明整体改善不等于物体区必然改善。
- **T6：token 窗口与 center 局部体积大体可比，但无绝对优势。** 未插值 ringreg 的 fg：cam3 token 20.538 vs center 20.095 dB；cam5 22.188 vs 21.905。cam5 object 却是 center 更好（17.384 vs token 17.077 dB），两者都不及光流。
- **T7：cam5 收益为负。** 最好 token ringreg 的 fg 比参考光流低 5.812 dB，LPIPS 更高。仅仅在小基线少标 token，尚未保证不破坏原本可靠的光流结果。

## 投影贴回范围为何不能用输入 core 比例代替

上游 `paste_area_frac_fg` 的分子是**整个投影 core 的面积，包括背景**，分母是有效前景面积，所以表里可以出现 103%/108%，不是“前景被替换超过 100%”。本次额外记录了 [paste_geometry.csv](eval/paste_geometry.csv)，分开统计真正被替换的前景与前景外部分。

| 设置 | 局部变体 | core 总面积 / fg | core 覆盖 fg 的比例 | core 中位于有效 fg 外的比例 |
|---|---|---:|---:|---:|
| cam3 | gs_center448_nat_dil_int_local | 103.08% | 60.01% | 41.51% |
| cam3 | gs_center448_nat_dil_local | 108.46% | 62.24% | 42.39% |
| cam3 | gs_token448_nat_dil_int_local | 101.11% | 59.18% | 41.25% |
| cam3 | gs_token448_nat_dil_local | 105.69% | 61.25% | 41.87% |
| cam5 | gs_center448_nat_dil_int_local | 81.11% | 47.88% | 40.83% |
| cam5 | gs_center448_nat_dil_local | 82.90% | 49.75% | 39.65% |
| cam5 | gs_token448_nat_dil_int_local | 79.28% | 47.08% | 40.51% |
| cam5 | gs_token448_nat_dil_local | 79.35% | 48.83% | 38.17% |

这些是配准前、羽化前的 core 统计；环带配准会移动 core，羽化也会扩展影响范围。前景外还可能包括窗口裁掉的像素，不能全部等同于纯绿幕背景。

本实现按“高斯中心在任一输入相机投影命中 core”选择高斯，再用这些高斯的累计 alpha 定义目标 core。它包含被保留的后方背景和高斯投影足迹，并不是把原输入二值 core 精确映射成目标视点的小块 mask。因此需优先检查投影贴回范围和可靠光流被替换的问题，而不能只看输入检测图的 26%–37%。

## 局部高斯与实际计算范围

| 设置 / 裁剪 | raw 窗口边长 | 编码总高斯 | recon 保留 | core 保留 | recon / 总数 |
|---|---:|---:|---:|---:|---:|
| cam3 / token | 911 | 368915 | 206323 | 82318 | 55.93% |
| cam3 / center | 1080 | 432937 | 169515 | 66610 | 39.15% |
| cam5 / token | 917 | 527784 | 271940 | 89535 | 51.52% |
| cam5 / center | 1080 | 639886 | 226345 | 72696 | 35.37% |

点云筛选保留了约 35%–56% 的编码高斯，但 **AnySplat 仍对完整 448×448 裁剪窗口编码，之后才筛选点云**。token 的 raw 窗口为 cam3 911×911、cam5 917×917；center 为 1080×1080。不能据此声称已实现仅对 token 的稀疏 Transformer 编码或端到端加速。`meta.num_gaussians` 是编码总数，实际局部数量应看 `local_gaussians.recon/core`。

## 解释边界

- token 检测只读取真实输入相机，局部高斯由输入图像生成；core 投影、直接贴回和环带对齐不使用目标真值误差作决策。环带 `register()` 的参考是光流结果，不是真值。
- **“只在最后用真值”应限定到这些局部决策。** 本轮控制分支 `vggt` 仍通过目标图像联合估计目标位姿；`_int` 只使用输入相机位姿插值，但共享的 t 和各相机单应 H 来自前序离线估计，t 最初使用了包含目标图像的 VGGT 位姿。当前实验是给定这些相机/映射信息的验证，不是完全不依赖目标相机离线信息的端到端协议。
- 自动 summary 后半段还保留用真值的 +reg、oracle_fail、risk 调参等诊断；它们不参与 `hyb_token` / `hyb_token_ringreg` 的构造，不能拿它们替代主结果。
- 主拼图逐相机用真值指标选择展示变体，属于展示选优，不能据此定义可部署选择器；本报告表格保留全部主变体。
- 环带位移 >20 px 会回退。40 条记录中有 18 条触发此限制，全部来自 `_int`；其余两条 `_int` 记录位移为 0，结果与直接贴回相同。CSV 位移是候选拟合位移，不是最终一定应用的位移，也不是对真实相机误差的独立测量。
- paste.csv 的三种方法在配准前 core 的同一像素集合上比较；ringreg 实际会移动 core，所以还必须检查 fg/object，不能只看贴回区分数。
- SSIM 按上游代码在前景附近裁片内计算后取区域平均；PSNR/LPIPS 与其支撑域定义并不完全相同，贴回区含前景外像素时尤其需注意。
- 上游第四轮 README 撤回了第三轮棋盘格间距和“RIFE 时间步非线性”的解释。本轮没有复跑 README 所称的独立视差检验，不将其数值当成本机新测结果。前三轮报告作为历史记录保留，应结合此次更正与原有标定不确定性阅读。
- 单场景、单帧、固定阈值，不构成跨场景有效性结论。下一步更有价值的是核对 `_int` 的实际投影一致性，并收紧目标 core 的贴回范围，减少把可靠光流替换成较软 GS；本轮没有修改阈值后挑选更好的结果。

## 复现与产物

```bash
conda activate gspl
export LGS_WORK_DIR=work/round4
export HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1 OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4
# 先独立复制 work/round2/{prepare,flow,poses,compat_packages}
python scripts/detect_tokens.py --config configs/mofang_9cam.yaml
python scripts/run_anysplat.py --config configs/mofang_9cam.yaml
python scripts/evaluate.py --config configs/mofang_9cam.yaml
python scripts/validate_results.py configs/mofang_9cam.yaml
python -m unittest discover -s tests -v
```

- [主结果汇总](eval/summary.md)、[质量指标](eval/metrics.csv)、[贴回区](eval/paste.csv)、[环带记录](eval/token_ringreg.csv)、[投影面积补充统计](eval/paste_geometry.csv)。
- [上游验证](eval/validation.json)、[附加检查](eval/extra_validation.json)、[测试日志](logs/numerics_tests.log)、[配置与环境](environment.json)，以及全部 CSV、GS meta、poses 和各步日志已保存。
- [输入 token 统计](tokens/tokens.json) 与 8 张 overlay、64 张 aligned/raw 掩码均在 `tokens/`；10 张主拼图均在 `eval/`，cam3 重点图：[1](eval/cam3/cam1_montage.png)、[2](eval/cam3/cam2_montage.png)、[3](eval/cam3/cam3_montage.png)、[5](eval/cam3/cam5_montage.png)。
- 全部原始渲染、alpha_core、mask、信号和自动 `_fullgs.png` 诊断拼图保留本机 `work/round4/`。轻量 Git 归档不包含 GB 级中间文件、模型权重或额外 `_fullgs.png`，README 要求回传的 CSV、日志与主拼图均已包含。
- [第三轮](../mofang-9cam-round3-gspl-20261024/REPORT.md)、[第二轮](../mofang-9cam-round2-gspl-20261024/REPORT.md)、[第一轮](../mofang-9cam-gspl-20261024/REPORT.md) 归档均保留在同一分支。

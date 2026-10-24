# 第三轮实测：阵列标定、cal/calK 位姿与修正后的 3D 滤波

日期：2026-10-24。源提交：`luckyhan-mike/local-gs-eval@9f3ed28`。按默认配置运行，推理、标定、滤波和评价代码均未修改。工作目录 `work/round3/`，前两轮归档与中间文件保留。

## 结论

**本轮没有验证“标定一次即可消除 GS 错位并优于最强光流”。标定位姿替换后错位和质量反而变差，应先定位标定与 AnySplat 几何之间的映射问题。**

- cam3 center nat_mip 的 ECC 平均位移：VGGT **10.62 px** → `_cal` **26.51 px** → `_calK` **57.38 px**，未达到 1–2 px 目标。ROI 分别为 **9.24 / 21.45 / 57.49 px**。
- cam3 最强光流 `flow_s0.5_pose` 的 object 为 **14.853 dB / 0.238320 LPIPS**；标定 GS 最好的 `_cal` 为 **11.389 / 0.358865**，最好的 `_calK` 为 **9.555 / 0.523279**，明显落后。未标定最佳 GS 为 **14.951 / 0.240206**，PSNR 只略高，LPIPS 略差，也没有形成多指标优势。
- 标定 GS 的非配准混合没有收益：cam3 最佳 `_cal` 变体的 tuned 混合 fg 为 **20.125 dB / 0.094222 LPIPS**，低于最强光流 **22.931 / 0.061022**。cam5 同样未成立。
- 修正后 `_nat_mip` 不再出现第二轮严重透明、条纹崩溃，但与 `_nat_dil` 的 object PSNR 差值普遍只有 **0.001–0.013 dB**，滤波收益很小。
- 标定 t 比 VGGT t 更差：同为 scale1.0，cam3 fg PSNR **22.604 → 21.956 dB**，cam5 **28.000 → 24.593 dB**。说明本次几何比例不能直接替代网络 t，但还不能排除标定、成像模型和匹配误差，不能把这单次实验当成“非线性响应”的独立证明。

## 标定实测与限制

9 台相机均检测到 88 个内角点，共 792 个；场景得到 26 对相机、4488 个双视图点。世界单位是一格棋盘格。

| 项目 | 本机实测 |
|---|---:|
| 棋盘格初始共享 K 标定 RMS | 0.209 px |
| 初始焦距 | 1835.7 px |
| BA 后棋盘格 RMS | 0.353 px |
| BA 后场景重投影中位数 / P90 | 0.15195 / 0.44766 px |
| BA 后共享焦距 | 1820.5 px |
| k1 / k2 | −0.1151 / 0.3475 |
| linear BA | nfev=600，status=0 |
| Huber BA | nfev=600，status=0 |

**两阶段 BA 都达到默认函数求值上限，未按求解器条件正式收敛。** 低重投影误差不能消除这一限制，也不等同于独立标定真值。本次保留默认结果完成实验，没有提高迭代上限或调整标定方法后另选一次结果。

相邻光心距离（格）：**2.188、2.148、1.910、0.946、1.768、2.341、1.689、2.549**。cam3–cam4 的距离明显较小，与上游 Windows 结果的趋势一致；数值没有照抄 Windows。完整 K、畸变、c2w 和误差见 [rig.json](calib/rig.json)。

标定位姿经输入相机 Sim(3) 对齐到 AnySplat 后，仍存在以下残差（同一裁剪的 cal/calK 相同）：

| 设置 / 裁剪 | 最大旋转残差 | 最大光心误差 / 基线 |
|---|---:|---:|
| cam3 center | 1.767° | 0.02867 |
| cam3 ROI | 1.134° | 0.11472 |
| cam5 center | 1.353° | 0.04466 |
| cam5 ROI | 0.865° | 0.13122 |

这是“标定阵列与 AnySplat 预测输入相机不完全一致”的直接证据，不是新标定误差的独立测量。可能涉及 AnySplat 相机几何失真、Sim(3) 不足以描述两者关系、内参与畸变不一致或标定优化问题；本轮尚未区分这些原因。

## 关键质量表

PSNR 越高、LPIPS 越低越好。object 对所有未配准方法均完整覆盖。ROI 的 fg 指标只在局部覆盖内计算，不应与整幅方法直接比较；混合方法在窗口外回退光流，fg 覆盖为 1，可比较。

### cam3

| 方法 | object PSNR | object LPIPS | fg PSNR | fg LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 14.528 | 0.272433 | 22.604 | 0.062884 |
| flow_s0.5_pose | 14.853 | 0.238320 | 22.931 | 0.061022 |
| flow_s1.0_posecal | 12.500 | 0.297172 | 21.956 | 0.070772 |
| flow_s0.5_posecal | 11.872 | 0.289174 | 21.895 | 0.071215 |
| gs_center448_nat_mip | 14.951 | 0.240206 | 17.341 | 0.181285 |
| gs_center448_nat_mip_cal | 10.699 | 0.421075 | 12.935 | 0.313468 |
| gs_center448_nat_mip_calK | 9.555 | 0.523279 | 10.015 | 0.385563 |
| gs_roi448_nat_mip_cal | 11.389 | 0.358865 | 12.041 | 0.324259 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 12.757 | 0.326790 | 20.770 | 0.100622 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 11.691 | 0.347940 | 20.125 | 0.094222 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 11.241 | 0.383544 | 19.534 | 0.112522 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 10.206 | 0.472444 | 18.098 | 0.127195 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 18.266 | 0.170607 | 26.749 | 0.061301 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 16.510 | 0.196369 | 25.588 | 0.060920 |

### cam5

| 方法 | object PSNR | object LPIPS | fg PSNR | fg LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.413 | 0.072142 | 28.000 | 0.039572 |
| flow_s0.5_pose | 19.648 | 0.081766 | 27.446 | 0.041550 |
| flow_s1.0_posecal | 14.327 | 0.196353 | 24.593 | 0.052837 |
| flow_s0.5_posecal | 13.867 | 0.196429 | 24.274 | 0.056009 |
| gs_center448_nat_mip | 17.130 | 0.174403 | 23.387 | 0.104022 |
| gs_center448_nat_mip_cal | 12.025 | 0.373039 | 14.826 | 0.260414 |
| gs_center448_nat_mip_calK | 9.790 | 0.514284 | 10.502 | 0.365392 |
| gs_roi448_nat_mip_cal | 10.721 | 0.349503 | 11.783 | 0.316707 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 14.054 | 0.278872 | 23.737 | 0.071019 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 14.730 | 0.239763 | 23.548 | 0.059454 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 16.277 | 0.218123 | 24.135 | 0.065662 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 13.777 | 0.314902 | 21.490 | 0.077698 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 19.443 | 0.142830 | 27.982 | 0.047716 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 20.189 | 0.113761 | 27.875 | 0.044660 |

## H1–H7

| 问题 | 本次回答 |
|---|---|
| H1：标定位姿是否消除错位 | **不成立**。cam3 center 位移约 10.6 → 26.5 → 57.4 px，cam5 center 约 2.65 → 18.53 → 49.10 px；cal/calK 均未降到 1–2 px。 |
| H2：标定 GS 是否优于最强光流 | **不成立**。cam3 最好 cal 为 ROI nat_mip，object 11.389 dB / 0.3589，低于最强光流 14.853 / 0.2383；calK 更差。 |
| H3：标定 GS 混合是否有效 | **未成立**。cam3 cal 最佳变体的 oracle/tuned 混合 fg 为 20.770/20.125 dB，均低于最强光流 22.931 dB，LPIPS 也更差。cam5 cal 最佳变体的 tuned 为 24.135 / 0.0657，低于最强光流 28.000 / 0.0396。oracle/tuned 本身使用真值，不能称为已验证的可部署系统。 |
| H4：标定内参与畸变是否改善 | **本次变差**。同为 center nat_mip，cam3 cal→calK 的 object 为 10.699→9.555 dB、LPIPS 0.4211→0.5233；cam5 为 12.025→9.790 dB、0.3730→0.5143。说明直接使用物理 K 与当前高斯表示不匹配，但不能据此证明物理 K 错误。 |
| H5：修正 3D 滤波是否有效 | **严重崩溃已修复，额外质量收益很小**。cam3 VGGT center nat_dil/nat_mip 为 14.9499/14.9515 dB；ROI 为 13.9718/13.9749。cam5 center 为 17.1163/17.1296。这些微小差值不能支撑显著改善结论。 |
| H6：标定 t 与网络响应 | **直接使用几何 t 较差**。相对 scale1.0 oracle t 的 MAE：cam3 VGGT 0.01549、calib 0.04244；cam5 0.01350、0.08148。cam3 相机 3 的 t 为 VGGT 0.802、calib 0.870、oracle 0.760。支持进一步校准网络 t，但还需要独立、收敛的标定或其他验证来分离原因。 |
| H7：小基线 | **光流仍更好**。cam5 最强光流 object 为 20.413 dB / 0.0721；所有未配准 GS 中最高 PSNR 约 17.171 dB（ROI nat_dil），对应 LPIPS 0.1534。当前 GS 不应作为小基线的默认替代。 |

配准诊断仍显示外观潜力，例如 cam3 VGGT center nat_mip 的 +reg object 为 17.54 dB / 0.1822；其 +reg+tuned 混合 fg 约 25.59 dB / 0.0609。但这用到了真值，不能用它掩盖标定条件下的失败。下一步应先检查标定与高斯坐标系、内参之间的兼容性，而不是把 oracle 上限当作部署收益。

## 完整性检查与必须保留的解释边界

- 上游 **8 项数值测试全部通过**，包含合成 BA、畸变映射和标定位姿坐标变换。上游产物验证 PASS：**6240 行指标、104 方法、50 行 AUC、120 张 GS、80 张光流、10 张拼图**。
- 附加检查确认每个目标相机均有 104 方法 × 6 区域，120 行配准记录、90 行风险扫描记录；所有未配准 GS 的 object 覆盖率与所有混合区域覆盖率均为 1。
- **上游 `validate_results.py` 的 warnings 只检查 meta 中的 VGGT 一致性字段，没有检查标定来源的 `pose_diag`。** 因此原始 validation 的 warnings=[] 不代表标定对齐通过。附加检查在 16 条 cal/calK 变体记录上发现旋转≥1°或光心/基线≥0.05，详见 [pose_alignment.csv](pose_alignment.csv) 和 [extra_validation.json](eval/extra_validation.json)。本轮保留上游原始 validation，并额外披露这一点，没有悄悄改验证逻辑。
- cam5 相机 7 的 ROI calK +reg 两种滤波在 object 的覆盖率约 **80.24% / 80.36%**。对应分数只评剩余覆盖区域，不能直接拿来证明完整 object 的配准上限；未配准 object 和混合结果没有这一覆盖缺口。
- 本轮 BA **使用全部 9 路魔方原图的场景匹配，包含留出的目标相机图像**；它不是完全独立于测试场景的纯棋盘格标定。`_cal` 还沿用联合 VGGT 估计的目标内参，因此不能严格声称目标图像从整个标定/渲染协议中完全消失。`_calK` 在 target_poses 阶段只使用 rig 参数，但该 rig 本次仍使用了目标场景图像。真正目标图像不可得的部署验证需要独立标定数据。
- “棋盘格与魔方拍摄之间阵列未移动”是上游协议的前提，本轮未独立验证。单平面棋盘格、共享焦距/径向畸变、固定主点等模型假设也需要后续复核。
- 两阶段 BA 的 status=0 与本次源代码的严格容差、max_nfev=600 一并保留；没有声称已正式收敛。
- 参考光流是 pose1.0，但按 README 使用 cam3 pose0.5、cam5 pose1.0 作为最强对照。第三轮和第二轮的 oracle_fail/risk/rest 定义不同，不能把这些区域的跨轮均值直接相减。自动 `summary.md` 标题仍沿用“第二轮”，其内容已经包含本轮 cal/calK/posecal；此报告以源提交与配置明确第三轮身份。
- uniform/pose/oracle 光流按 README 复用第二轮，仅 posecal 在本轮重算。GS 再编码有少量数值差异，新生成 VGGT poses 与复用 flow 的 t 可能略有不同；流的评价和 t 表来自保存的 flow meta，复用事实已记录。
- +reg、oracle_fail、oracle t 和同数据风险调阈值均使用真值，属于诊断或乐观上限；最佳 GS 按本场景 object PSNR 选出，拼图为逐相机选优，不是预先固定的部署选择规则。

## 运行方式与产物

```bash
conda activate gspl
export LGS_WORK_DIR=work/round3
export HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1 OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4
# 本次已独立复制 work/round2/{prepare,flow,poses,compat_packages}
python scripts/calibrate_rig.py --config configs/mofang_9cam.yaml
python scripts/run_anysplat.py --config configs/mofang_9cam.yaml
python scripts/run_flow.py --config configs/mofang_9cam.yaml --tmodes posecal
python scripts/evaluate.py --config configs/mofang_9cam.yaml
python scripts/validate_results.py configs/mofang_9cam.yaml
python -m unittest discover -s tests -v
```

本轮使用既有 gspl 的 Python 3.9.23、torch 2.0.1/CUDA 11.7、gsplat 1.5.3、RTX 3090；e3nn 0.5.6 仍仅在工作目录局部覆盖。未修改系统 CUDA、环境包或源 AnySplat/Practical-RIFE。配置、模型快照、数据 SHA256（额外包含 9 张棋盘格）与复用记录见 [environment.json](environment.json)。编码/渲染日志的计时不包括标定、模型加载、评价和完整 IO，不当作端到端基准。

- [完整汇总](eval/summary.md)、[质量 CSV](eval/metrics.csv)、[AUC](eval/auc.csv)、[配准](eval/registration.csv)、[风险扫描](eval/risk_sweep.csv)、[上游验证](eval/validation.json)、[附加检查](eval/extra_validation.json)。
- [rig.json](calib/rig.json)、[Sim(3) 残差](pose_alignment.csv)、[标定日志](logs/0b_calibrate.log)、[测试日志](logs/numerics_tests.log)，以及全部 GS/flow meta、poses 和运行日志均已保存。
- cam3 拼图：[1](eval/cam3/cam1_montage.png)、[2](eval/cam3/cam2_montage.png)、[3](eval/cam3/cam3_montage.png)、[5](eval/cam3/cam5_montage.png)，其余 6 张也已保存。
- [修正后 nat_mip 示例](diagnostics/cam3_cam1_center448_nat_mip_fixed.png) 可与 [第二轮异常图](../mofang-9cam-round2-gspl-20261024/diagnostics/cam3_cam1_center448_nat_mip.png) 对照。
- 全部中间渲染、alpha、mask、信号和模型缓存保留本机，未将 GB 级中间文件或模型权重加入 Git。[第二轮报告](../mofang-9cam-round2-gspl-20261024/REPORT.md) 和 [第一轮报告](../mofang-9cam-gspl-20261024/REPORT.md) 均保留在同一分支。

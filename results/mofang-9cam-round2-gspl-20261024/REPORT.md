# 第二轮验证：ROI、原生分辨率滤波与配准诊断

日期：2026-10-24。源代码：`luckyhan-mike/local-gs-eval@68c18e9`。本轮完整使用上游实现和默认配置，没有修改推理、配准或评价代码。

## 结论

**cam3 的物体级结果支持 GS 在坏掉的魔方区域有补全潜力，配准误差是明显的限制；当前可部署的混合方案仍未验证成功。**

- 在 object 区，未配准的 `gs_center448_nat_dil` 相比默认光流，PSNR **13.016 → 14.743 dB（+1.727 dB）**，LPIPS **0.290648 → 0.247807**，SSIM **0.4647 → 0.4896**。该区对所有未配准方法覆盖率都是 1，因此不是 ROI 只评容易区域造成的提升。
- 同一 GS 配准后，object PSNR **14.743 → 17.439 dB**；配准后的 oracle 混合全前景 PSNR **22.175 → 26.345 dB（+4.170 dB）**，LPIPS **0.069104 → 0.068404**，LPIPS 的改善幅度很小。ROI 配准后的 oracle 混合为 **25.756 dB / 0.063847 LPIPS**。这些都使用了真值，属于诊断上限。
- 更强的光流对照不能忽略：cam3 的 `flow_s0.5_pose` object 为 **14.853 dB / 0.238320 LPIPS**，已经优于未配准最佳 GS 的这两项指标。因此“GS 优于默认均匀 t 光流”不能直接推广为“GS 优于优化后的光流”。
- cam3 默认 risk 混合（center nat_dil）只有 **19.550 dB / 0.1426 LPIPS**；调阈值后为 **22.662 dB / 0.083477**，仍比默认光流的 LPIPS 差。现有风险检测器和未配准 GS 组合尚不足以部署。
- 完整 3D Mip 滤波 `_nat_mip` 明显异常退化；只有尺度匹配膨胀 `_nat_dil` 表现接近或略优于 `_in`，没有得到“完整 Mip 滤波显著提升”的证据。

## 运行与验证

- 本轮输出目录：`/home/han/linux-han/local-gs-eval/work/round2/`；第一轮 `work/` 保留。
- 使用 `gspl`：Python 3.9.23、torch 2.0.1/CUDA 11.7、RTX 3090、gsplat 1.5.3；环境及数据校验值见 [environment.json](environment.json)。数据 SHA256 与第一轮逐一核对一致。
- 复用第一轮 prepare 与 uniform/oracle 光流；重新运行所有 GS、两种尺度的 pose 光流和完整 evaluate。复用文件采用独立副本，未覆盖第一轮结果。
- 4 次 GS 编码，每次 5 种渲染：center 1080×1080、ROI 543×543，输入都为 448×448；共 **100 张 GS、60 张光流（其中 20 张 pose 本轮重算）**。
- center448 输入自渲染 PSNR：cam3 **29.28 dB**、cam5 **29.86 dB**，与第一轮 29.23/29.85 接近。ROI 自渲染为 26.63/27.36 dB。最大位姿旋转对齐误差 **0.514°**，最大光心误差/基线 **0.01878**，均在 README 的阈值内。
- 上游 **5 项数值测试通过**；上游产物验证 PASS、无警告：**3960 行质量指标、66 种方法、50 行 AUC、100 张 GS、60 张光流、10 张拼图**。
- 附加检查确认：每个目标相机都有 66 方法 × 6 区域，100 行配准记录，90 行阈值扫描记录；所有未配准方法的 object 覆盖率、所有混合方法的区域覆盖率均为 1。异常配准变体的覆盖问题另见下文和 [extra_validation.json](eval/extra_validation.json)。

## 关键数值

以下为目标相机等权平均，均来自本轮 CSV。PSNR 越高、LPIPS 越低越好。ROI 的 fg/rest 是局部覆盖指标，不能与整幅方法直接比较；混合方法在 ROI 外回退光流，fg 可比较。

### cam3

| 方法 | object PSNR | object LPIPS | fg PSNR | fg LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 13.016 | 0.290648 | 22.175 | 0.069104 |
| flow_s1.0_pose | 14.528 | 0.272433 | 22.604 | 0.062884 |
| flow_s0.5_pose | 14.853 | 0.238320 | 22.931 | 0.061022 |
| gs_center448_in | 14.735 | 0.249377 | 17.475 | 0.185423 |
| gs_center448_nat_dil | 14.743 | 0.247807 | 17.493 | 0.181812 |
| gs_center448_nat_dil+reg | 17.439 | 0.188237 | 24.892 | 0.109546 |
| gs_roi448_nat_dil | 13.963 | 0.247360 | 16.194 | 0.208657 |
| gs_roi448_nat_dil+reg | 17.601 | 0.166549 | 20.962 | 0.144191 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 17.968 | 0.184260 | 26.345 | 0.068404 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 18.039 | 0.170694 | 25.756 | 0.063847 |
| hyb_risktuned[gs_center448_nat_dil] | 14.350 | 0.265826 | 22.662 | 0.083477 |

### cam5

| 方法 | object PSNR | object LPIPS | fg PSNR | fg LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 16.390 | 0.112934 | 26.189 | 0.044024 |
| flow_s1.0_pose | 20.413 | 0.072142 | 28.000 | 0.039572 |
| flow_s0.5_pose | 19.648 | 0.081766 | 27.446 | 0.041550 |
| gs_center448_in | 16.976 | 0.179448 | 22.922 | 0.114813 |
| gs_center448_nat_dil | 16.972 | 0.177436 | 22.918 | 0.110690 |
| gs_center448_nat_dil+reg | 17.675 | 0.175432 | 25.612 | 0.096710 |
| gs_roi448_nat_dil | 17.491 | 0.151575 | 17.514 | 0.162848 |
| gs_roi448_nat_dil+reg | 18.999 | 0.137175 | 24.765 | 0.106355 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 18.113 | 0.168304 | 27.218 | 0.052642 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 19.373 | 0.134578 | 27.728 | 0.047333 |
| hyb_risktuned[gs_center448_nat_dil] | 17.289 | 0.164369 | 26.373 | 0.053948 |

## H1–H7

| 问题 | 本次判断 |
|---|---|
| H1：物体区 GS 是否优于默认光流 | **cam3 成立**：最佳未配准 GS 的 PSNR/SSIM/LPIPS 均改善；cam5 的 ROI GS 虽 PSNR +1.101 dB，但 LPIPS 0.151575 高于光流 0.112934，不满足多指标改善。cam3 更强的 pose+scale0.5 光流优于未配准最佳 GS，见上文。 |
| H2：滤波核是否有效 | **没有明显收益**。cam3 center：in 14.735 dB、nat 14.668、nat_dil 14.743、nat_mip2d 14.630；nat_dil 相对 in 仅 +0.007 dB。完整 nat_mip 降至 8.952 dB，LPIPS 0.6357，不能称为有效。 |
| H3：ROI 是否优于中心裁剪 | **依相机设置而定**。cam3 nat_dil：ROI 13.963 dB，低于 center 14.743；LPIPS 仅略低（0.24736 vs 0.24781）。cam5 ROI 17.491 dB / 0.15158，优于 center 16.972 / 0.17744，但仍不如默认光流的 LPIPS，更不如 pose 光流。 |
| H4：错位是否造成主要损失 | **cam3 对配准高度敏感**。center nat_dil 的平均拟合位移 10.49 px，object +2.696 dB；ROI nat_dil 平均位移 8.31 px，object +3.637 dB。支持继续检查位姿、内参、单应域残差，但 ECC 可吸收非刚性外观差异，不能把全部收益严格归因于相机位姿。 |
| H5：混合上限 | **cam3 达到 README 的数值标准**：配准后 center nat_dil oracle 混合 fg +4.170 dB，LPIPS 小幅下降；ROI oracle 混合 +3.581 dB 且 LPIPS 降幅更大。cam5 对应 ROI 混合 fg +1.539 dB，但 LPIPS 0.04733 高于基线 0.04402，不满足双指标标准。 |
| H6：现实检测器是否够用 | **还不够**。最佳风险 IoU：cam3 0.353（precision 0.458、recall 0.631），cam5 0.271（precision 0.338、recall 0.583）。调阈值改善了默认风险区，但未配准的 tuned 混合仍普遍损失 LPIPS。当前代码只给 +reg GS 构造 oracle 混合，没有 +reg 的 tuned/risk 混合，不能用两个不同配准条件的结果单独量化检测器损失。 |
| H7：光流侧改善 | **pose t 有效，scale0.5 不是普遍有效**。cam3 fg：uniform1.0 22.175 → pose1.0 22.604 → pose0.5 22.931 dB，LPIPS 0.06910 → 0.06288 → 0.06102。cam5：uniform1.0 26.189 → pose1.0 28.000 dB，pose0.5 反降到 27.446 dB，LPIPS 也退化。 |

## 必须保留的异常与解释边界

### 完整 3D Mip 滤波严重退化

已直接查看 [cam3 相机 1 的 nat_mip 渲染](diagnostics/cam3_cam1_center448_nat_mip.png)：有严重过度平滑和重复条纹，人物与魔方纹理基本丢失。该异常在本轮各设置中均反映为显著低分。本次没有修改算法重跑，也没有定位 3D 滤波的退化原因；5 项测试通过只说明测试覆盖的合成数值例子通过，不证明实际 AnySplat 高斯上的滤波适配正确。

`registration.csv` 中 center nat_mip 的平均位移高达 cam3 227.46 px / cam5 79.59 px。**这些异常图像上的 ECC 位移不能当作相机标定误差。** `ok=True` 只表示函数返回了矩阵，连 identity 回退也会被计入，不能等同于可靠配准。

补充覆盖检查还发现 5 条 `gs_center448_nat_mip+reg` 的 object 只被部分覆盖：最低为 cam3 相机 3 的 **15.30%**，cam3 相机 1 为 **31.46%**。这些 `+reg` 指标只在剩余覆盖区域计算，不应拿它们的分数直接判断配准上限。正常的最佳 center/ROI 变体在 object 上覆盖率都是 1。

### 与第一轮及部署场景的关系

- 本轮 object 是新增主区域；本轮整幅有效域由 center 裁剪定义，第一轮还与 fg 裁剪窗口取了交集。因此两轮原始 fg/oracle_fail 均值不能简单相减作为算法增益，以上判断使用同一轮的对照。
- `+reg` 用真值拟合，oracle_fail、oracle t、risk 调阈值也使用真值；同一数据上的选优与调参偏乐观。
- GS 最佳变体在本场景按 object PSNR 选出，拼图更是逐相机选优；这不是预先固定的部署选择规则。
- 内部位姿对齐误差通过阈值不等于真实标定精度；目标图像参与联合位姿估计，高斯仍只由输入相机产生。
- 单场景、单帧、启发式魔方检测。建议下一步优先用真实标定验证 GS 物体补全，并与 pose/scale 优化后的光流比较；同时排查完整 3D 滤波的异常，不能仅凭本轮上限宣称可部署方案已成立。

## 复现与产物

```bash
conda activate gspl
export LGS_WORK_DIR=work/round2
export HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1 OMP_NUM_THREADS=4
# 本次已复制第一轮 prepare、flow 和 compat_packages 到 $LGS_WORK_DIR
python scripts/run_anysplat.py --config configs/mofang_9cam.yaml
python scripts/run_flow.py --config configs/mofang_9cam.yaml --tmodes pose
python scripts/evaluate.py --config configs/mofang_9cam.yaml
python scripts/validate_results.py configs/mofang_9cam.yaml
python -m unittest discover -s tests -v
```

全新运行可在 gspl 中向所用工作目录的 `compat_packages` 安装 e3nn==0.5.6（`--no-deps --target`），然后执行 README 的完整流程。源 AnySplat 与环境包均未修改。

- [自动汇总与全部区域表](eval/summary.md)、[质量 CSV](eval/metrics.csv)、[AUC](eval/auc.csv)、[配准记录](eval/registration.csv)、[阈值扫描](eval/risk_sweep.csv)。
- [上游验证](eval/validation.json)、[附加完整性和覆盖诊断](eval/extra_validation.json)、[数值测试日志](logs/numerics_tests.log) 和各步运行日志均已保存。
- cam3 拼图：[相机 1](eval/cam3/cam1_montage.png)、[相机 2](eval/cam3/cam2_montage.png)、[相机 3](eval/cam3/cam3_montage.png)、[相机 5](eval/cam3/cam5_montage.png)。其余 6 张也已保存；黄色轮廓在重点图中覆盖魔方及其附近手部，人物其余部分不属于 object。
- H、prepare 报告、所有 GS/flow meta、poses、配置和环境记录包含在归档；全部渲染、alpha、mask、原始信号保留在本机 `work/round2/`，没有把 GB 级中间文件或模型权重加入 Git。
- [第一轮报告](../mofang-9cam-gspl-20261024/REPORT.md) 也保留在同一分支，便于查看历史。

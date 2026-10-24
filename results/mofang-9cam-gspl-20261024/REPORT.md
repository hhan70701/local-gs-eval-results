# 魔方 9 相机：gspl 实测报告

日期：2026-10-24。来源仓库：https://github.com/luckyhan-mike/local-gs-eval ，基线提交 `3aae940`。

## 结论

当前管线不足以支持直接采用“光流为主 + 局部 GS 补全”。cam3 的 `gs_center448` 在光流失败区域的平均 PSNR 仅比参考 RIFE 高 0.15 dB，SSIM 更低、LPIPS 更高；oracle 混合在全前景平均仅提升 0.13 dB，且 SSIM、LPIPS 均退化，没有达到 README 所述约 +0.5 dB 且 LPIPS 改善的标准。

存在明显的相机差异：cam3 的相机 1/2/3 上，oracle 混合前景 PSNR 提升 0.80/1.62/2.28 dB；相机 5/6/7 则下降 1.66/0.63/1.62 dB。因此不能用左侧三张成功图代替全组结论。更直接的改进信号是调整光流的 t：cam5 的位姿 t 相比均匀 t，全前景平均 PSNR 提升 1.79 dB、LPIPS 下降。

## 实验配置与可信度

- RTX 3090；`/home/han/anaconda3/envs/gspl/bin/python`；Python 3.9.23；torch 2.0.1/CUDA 11.7；gsplat 1.5.3。
- 配置：[config.yaml](config.yaml)。cam3 输入 0/4/8，目标 1/2/3/5/6/7；cam5 输入 0/2/4/6/8，目标 1/3/5/7。
- GS：center/fg 裁剪 × 448/518，共 8 组、40 张目标渲染。RIFE：scale 1.0/0.5 × uniform/pose/oracle，共 12 组、60 张图。
- 9 台相机的原图→对齐图 PSNR 为 52.99–55.88 dB，全部高于 30 dB。
- GS 最大旋转对齐误差 0.5672°，最大光心误差/基线 0.02061，全部通过 1° / 0.05 检查。这是联合估计和输入估计之间的一致性，**不是标定真值误差**。
- 已检查 cam3 的相机 1/2/3 拼图，未见整幅画面完全失配；GS 有局部位置、轮廓与纹理残差。内部位姿检查通过不能排除目标相机估计、内参和渲染重投影误差。
- 3 个数值测试通过（AUC 并列值、已知 Sim(3)、Python 3.9 类型兼容不改变位运算）；产物检查通过：1100 行质量指标、50 行 AUC、40 张 GS、60 张 RIFE、10 张拼图，所有评估值及保存的光流信号均有限。

## 主要指标

下表为各目标相机的算术平均；PSNR/SSIM 越高越好，LPIPS 越低越好。所有方法使用同一组 GS 有效窗口交集；这与 run_flow 日志中未限制窗口的 fgPSNR 有区别。完整数据见 [summary.md](eval/summary.md) 和 [metrics.csv](eval/metrics.csv)。

### cam3

| 区域 | 方法 | PSNR | SSIM | LPIPS |
|---|---|---:|---:|---:|
| oracle_fail | flow_s1.0_uniform | 13.082 | 0.5347 | 0.0647 |
| oracle_fail | gs_center448 | 13.233 | 0.4103 | 0.1377 |
| oracle_fail | gs_center518 | 11.234 | 0.2896 | 0.1740 |
| oracle_fail | gs_fg448 | 11.028 | 0.3013 | 0.1764 |
| oracle_fail | gs_fg518 | 10.351 | 0.2754 | 0.1917 |
| rest | flow_s1.0_uniform | 33.177 | 0.9535 | 0.0255 |
| rest | gs_center448 | 19.647 | 0.7383 | 0.1622 |
| rest | gs_center518 | 17.217 | 0.6925 | 0.2105 |
| rest | gs_fg448 | 15.665 | 0.6591 | 0.2442 |
| rest | gs_fg518 | 13.609 | 0.6254 | 0.2800 |
| fg | flow_s1.0_uniform | 21.904 | 0.8895 | 0.0744 |
| fg | gs_center448 | 17.303 | 0.6614 | 0.1922 |
| fg | gs_center518 | 14.721 | 0.5954 | 0.2612 |
| fg | gs_fg448 | 13.825 | 0.5746 | 0.2769 |
| fg | gs_fg518 | 12.205 | 0.5406 | 0.3392 |
| fg | hyb_oracle_fail[gs_center448] | 22.035 | 0.8599 | 0.1127 |
| fg | hyb_risk[gs_center448] | 19.328 | 0.7909 | 0.1497 |
| fg | flow_s0.5_uniform | 22.847 | 0.8910 | 0.0687 |
| fg | flow_s1.0_pose | 22.320 | 0.9084 | 0.0684 |
| fg | flow_s1.0_oracle | 22.609 | 0.9118 | 0.0676 |

### cam5

| 区域 | 方法 | PSNR | SSIM | LPIPS |
|---|---|---:|---:|---:|
| oracle_fail | flow_s1.0_uniform | 16.153 | 0.5673 | 0.0270 |
| oracle_fail | gs_center448 | 16.368 | 0.5858 | 0.0529 |
| oracle_fail | gs_center518 | 11.738 | 0.2978 | 0.1070 |
| oracle_fail | gs_fg448 | 12.293 | 0.3449 | 0.1018 |
| oracle_fail | gs_fg518 | 11.315 | 0.2662 | 0.1172 |
| rest | flow_s1.0_uniform | 31.182 | 0.9613 | 0.0325 |
| rest | gs_center448 | 24.565 | 0.8324 | 0.1010 |
| rest | gs_center518 | 19.295 | 0.7607 | 0.1861 |
| rest | gs_fg448 | 17.519 | 0.6851 | 0.2066 |
| rest | gs_fg518 | 15.002 | 0.6543 | 0.2645 |
| fg | flow_s1.0_uniform | 26.036 | 0.9309 | 0.0462 |
| fg | gs_center448 | 22.824 | 0.8046 | 0.1186 |
| fg | gs_center518 | 17.055 | 0.6991 | 0.2084 |
| fg | gs_fg448 | 16.270 | 0.6376 | 0.2098 |
| fg | gs_fg518 | 13.988 | 0.6025 | 0.2953 |
| fg | hyb_oracle_fail[gs_center448] | 26.373 | 0.9269 | 0.0604 |
| fg | hyb_risk[gs_center448] | 25.434 | 0.9091 | 0.0691 |
| fg | flow_s0.5_uniform | 25.936 | 0.9318 | 0.0484 |
| fg | flow_s1.0_pose | 27.831 | 0.9462 | 0.0414 |
| fg | flow_s1.0_oracle | 28.920 | 0.9542 | 0.0397 |

## H1–H7 的回答

| 问题 | 本次证据与判断 |
|---|---|
| H1：GS 在光流失败区是否更好 | **没有稳定的多指标优势。** cam3 最好的 GS 变体 center448：PSNR 13.233 vs 13.082，但 SSIM 0.4103 vs 0.5347，LPIPS 0.1377 vs 0.0647。相机 1/2/3 的失败区 PSNR 提升 1.00/1.79/2.50 dB，LPIPS 仍均退化。 |
| H2：其余前景中光流是否更好 | **成立。** cam3 rest：光流 33.177 dB vs center448 19.647 dB，SSIM 与 LPIPS 也明显更好。 |
| H3：混合是否同时优于两者 | **不成立。** cam3 oracle 混合 22.035 dB vs 光流 21.904 dB，但 LPIPS 0.1127 vs 0.0744；实际 risk 混合降到 19.328 dB。cam5 oracle 混合 +0.336 dB，LPIPS 同样退化；risk 混合 −0.602 dB。 |
| H4：基线影响 | cam3 的 oracle_fail 占前景 12.30%，cam5 为 6.60%；只比较共同目标相机 1/3/5/7 时，cam3 仍为 11.49%。大基线的失败区更大，但未观察到平均 GS 收益更大：oracle 混合增益 cam3 +0.131 dB，cam5 +0.336 dB。 |
| H5：分辨率与裁剪 | 本次 **center448 最好**，518 和 fg 裁剪均未带来优势。center448 输入自渲染 PSNR 为 cam3 29.23 / cam5 29.85 dB；center518 为 22.19 / 21.69 dB。518 有明显纹理、几何质量退化，原因尚未定位，不能概括为“提高分辨率必然更差”。 |
| H6：大位移是否主因 | cam3 scale0.5 uniform 在失败区由 13.082 提高到 14.343 dB，SSIM/LPIPS 同时改善；全前景 +0.943 dB。支持大位移/尺度敏感性是因素之一。cam5 失败区仅 +0.104 dB 且 LPIPS 变差，全前景 −0.100 dB，不能据此证明它是唯一主因。 |
| H7：位姿 t 是否有效 | **本场景支持。** scale1.0 下，相对网格搜索 t_oracle 的平均绝对误差：cam3 uniform 0.03333 → pose 0.01564；cam5 0.04750 → 0.01500。全前景 PSNR：cam3 +0.417 dB，cam5 +1.795 dB，SSIM/LPIPS 均改善；不是每个目标相机都改善。 |

### cam3 逐相机检查（center448）

| 相机 | 失败区光流 PSNR | 失败区 GS PSNR | 前景 oracle 混合相对光流 ΔPSNR | 前景光流 LPIPS | 前景 oracle 混合 LPIPS |
|---|---:|---:|---:|---:|---:|
| 1 | 11.892 | 12.896 | +0.801 | 0.1245 | 0.1542 |
| 2 | 11.654 | 13.441 | +1.622 | 0.0952 | 0.1156 |
| 3 | 12.563 | 15.068 | +2.278 | 0.0603 | 0.0735 |
| 5 | 14.495 | 12.881 | -1.661 | 0.0470 | 0.1084 |
| 6 | 13.840 | 13.341 | -0.628 | 0.0628 | 0.1235 |
| 7 | 14.051 | 11.771 | -1.624 | 0.0565 | 0.1012 |

## 执行修复与复现

本次没有改动外部 AnySplat/Practical-RIFE 源码，没有升级 gspl 的 Python、torch、CUDA 或现有依赖。以下实验仓库改动用于运行与统计：

1. Python 3.9 不支持 AnySplat 使用的 PEP 604 联合类型，新增 `lgs/compat.py`，复制 `AnySplat/src` 到 `work/anysplat_py39`，仅转换类型注解和配置类型别名；数值运算不变。
2. gspl 的 e3nn 0.6.0 调用了 torch 2.0.1 不存在的 `torch.compiler`。使用 `pip --no-deps --target work/compat_packages e3nn==0.5.6` 作局部覆盖，环境中的包不变。
3. 联合位姿 aggregator 使用与 AnySplat encoder 一致的 bfloat16 autocast，随后相机头在 autocast 关闭时运行。
4. AUC 使用平均秩处理并列值，修正 float16 信号并列时的顺序偏差。

```bash
conda activate gspl
python -m pip install --no-deps --target work/compat_packages e3nn==0.5.6
HF_HUB_OFFLINE=1 PYTHONUNBUFFERED=1 bash run_all.sh configs/mofang_9cam.yaml
python -m unittest discover -s tests -v
python scripts/validate_results.py configs/mofang_9cam.yaml
```

本次 prepare 使用原始脚本；其余步骤按以上兼容修复后分别执行。evaluate 使用 `OMP_NUM_THREADS=4`。已有模型缓存，因此推理采用离线加载。数据、模型缓存快照、源仓库提交、完整环境包版本和输入 SHA256 见 [environment.json](environment.json)。首次渲染的 148.4 ms/视点包含首次调用成本，其余多为 2–3 ms/视点；编码/渲染计时不包括模型加载、联合位姿估计、数据准备、RIFE 或评价，且未做重复计时，不作为端到端性能基准。

## 产物位置与解释边界

- [完整汇总](eval/summary.md)、[质量明细](eval/metrics.csv)、[AUC 明细](eval/auc.csv)、[完整性检查](eval/validation.json)。
- [prepare.json](prepare/prepare.json) 和 `prepare/check_warp_01~03.png`；H 矩阵、全部变体的 meta/poses 和各步日志也在本目录。
- cam3 重点拼图：[相机 1](eval/cam3/cam1_montage.png)、[相机 2](eval/cam3/cam2_montage.png)、[相机 3](eval/cam3/cam3_montage.png)。已保存全部 10 张拼图；拼图中的 GS 由该相机 oracle_fail PSNR 选择，并不总是 center448，标签给出实际变体。
- 完整中间渲染和原始信号仍在本机 `/home/han/linux-han/local-gs-eval/work/`，未将约 2.3 GB 的中间数据和模型权重写入 Git；所有 README 要求回传的指标、日志、prepare.json 和重点拼图均已归档。
- 实际混合方法名为 `hyb_oracle_fail[...]`。oracle_fail 的误差先 GaussianBlur(sigma=1) 后阈值化并膨胀 3 px；AUC 的正类是前景内模糊误差超过阈值，未膨胀，不完全等同于膨胀后的区域。
- evaluate 从量化信号和参考光流预测前景重建 risk；run_flow 保存的 risk PNG 使用两个 warp 的前景，因此两处 risk 占比可能不同。本文以 evaluate 的区域为准。
- t_pose 固定来自各设置的第一个变体 center448；t_oracle 是 21 个粗点和 11 个细点的有限网格搜索，属于真值辅助的近似上限。
- 目标图像只参与联合位姿估计；高斯由输入相机生成。oracle_fail 和 oracle t 使用目标真值，不能当作部署时的方法结果。
- 单场景、单帧；foreground 使用绿幕规则，评价局限于 GS 窗口交集；未用标定板真值校验相机，也未定位 518 退化原因。以上结论限于本次实现和协议，不等同于否定所有前馈 GS 或局部补全方法。

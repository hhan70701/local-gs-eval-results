# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 12.4% | 18.45 / 0.0292 | 17.62 / 0.0433 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 9.9% | 18.06 / 0.0285 | 17.41 / 0.0424 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 4.0% | 17.15 / 0.0195 | 15.73 / 0.0308 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.2% | 17.51 / 0.0376 | 17.38 / 0.0474 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 15.2% | 17.52 / 0.0375 | 17.43 / 0.0491 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 4.7% | 16.40 / 0.0230 | 15.83 / 0.0322 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 22.74 / 0.0688 | — / — | 14.97 / 0.0348 | 29.91 / 0.0341 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.63 / 0.0742 | — / — | 15.17 / 0.0371 | 29.68 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.57 / 0.0760 | — / — | 15.02 / 0.0384 | 29.79 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.57 / 0.0740 | — / — | 14.95 / 0.0382 | 29.81 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.67 / 0.0730 | — / — | 15.18 / 0.0373 | 29.79 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 22.71 / 0.0752 | — / — | 15.20 / 0.0375 | 29.80 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 22.69 / 0.0731 | — / — | 15.08 / 0.0379 | 29.79 / 0.0347 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 12.2%） | — | — | 22.74 / 0.0688 | — / — | 29.91 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 20.93 / 0.0680 | — | — | — |
| in035 | 2 | 0-3 | 19.48 / 0.0817 | — | — | — |
| in035 | 4 | 3-5 | 27.82 / 0.0567 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 22.74 / 0.0688 | — | 29.91 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 22.63 / 0.0742 | — | 29.68 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 4.8% | 22.80 / 0.0711 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 22.57 / 0.0760 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 4.2% | 22.71 / 0.0717 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 22.57 / 0.0740 | — | 29.81 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 2.2% | 22.68 / 0.0714 | — | 29.90 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 22.67 / 0.0730 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 6.6% | 22.78 / 0.0703 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 22.71 / 0.0752 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 6.6% | 22.81 / 0.0707 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 22.69 / 0.0731 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 2.7% | 22.77 / 0.0708 | — | 29.89 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 22.74 / 0.0688 | — / — | 29.91 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 22.63 / 0.0742 | — / — | 29.68 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 22.80 / 0.0711 | — / — | 29.88 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 14.97 / 0.0348 | 29.91 / 0.0341 | 22.74 / 0.0688 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 12.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 14.97 | 0.5468 | 0.0348 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.52 | 0.4282 | 0.1192 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.01 | 0.4279 | 0.0876 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.01 | 0.4279 | 0.0876 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.43 | 0.4566 | 0.0835 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.44 | 0.4477 | 0.0845 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.44 | 0.4477 | 0.0845 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 15.17 | 0.5803 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 15.03 | 0.5660 | 0.0383 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 14.96 | 0.5576 | 0.0381 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 15.18 | 0.5923 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 15.21 | 0.5935 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 15.08 | 0.5733 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 15.17 | 0.5799 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 15.02 | 0.5655 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 14.95 | 0.5572 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 15.18 | 0.5921 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 15.20 | 0.5930 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 15.08 | 0.5729 | 0.0379 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 33.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.58 | 0.7122 | 0.0379 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.76 | 0.4744 | 0.2268 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.01 | 0.3862 | 0.1847 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.01 | 0.3862 | 0.1847 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.16 | 0.4055 | 0.1770 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.17 | 0.4002 | 0.1807 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.17 | 0.4002 | 0.1807 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.70 | 0.7226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.55 | 0.7141 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.49 | 0.7109 | 0.0403 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.67 | 0.7247 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.71 | 0.7258 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.62 | 0.7178 | 0.0400 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.27 | 0.7089 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.27 | 0.7009 | 0.0473 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.27 | 0.7007 | 0.0449 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.48 | 0.7137 | 0.0444 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.49 | 0.7137 | 0.0456 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.48 | 0.7073 | 0.0445 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 73.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.91 | 0.7219 | 0.0341 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.58 | 0.3104 | 0.3672 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.43 | 0.1460 | 0.2747 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.43 | 0.1460 | 0.2747 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.57 | 0.1553 | 0.2680 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.56 | 0.1575 | 0.2710 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.56 | 0.1575 | 0.2710 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7217 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.89 | 0.7217 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.90 | 0.7217 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.88 | 0.7217 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.89 | 0.7217 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.89 | 0.7217 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.68 | 0.7213 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.79 | 0.7212 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.81 | 0.7211 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.79 | 0.7212 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.80 | 0.7218 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.79 | 0.7212 | 0.0347 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.74 | 0.7087 | 0.0688 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.38 | 0.3457 | 0.4414 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.47 | 0.2130 | 0.3802 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.47 | 0.2130 | 0.3802 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.61 | 0.2257 | 0.3654 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.62 | 0.2262 | 0.3719 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.62 | 0.2262 | 0.3719 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.80 | 0.7120 | 0.0711 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.71 | 0.7095 | 0.0717 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.68 | 0.7085 | 0.0714 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.78 | 0.7133 | 0.0703 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 22.81 | 0.7136 | 0.0707 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 22.77 | 0.7109 | 0.0708 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.63 | 0.7099 | 0.0742 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.57 | 0.7064 | 0.0760 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.57 | 0.7057 | 0.0740 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.67 | 0.7107 | 0.0730 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 22.71 | 0.7112 | 0.0752 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 22.69 | 0.7083 | 0.0731 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|

## 风险阈值扫描（风险区 vs oracle_fail，按 IoU 排序，前 8 名与配置默认值）

| 设置 | warp 阈值 | col 阈值 | 精确率 | 召回率 | IoU | 面积比 |
|---|---:|---:|---:|---:|---:|---:|

## t 估计对比（scale=1.0）

| 设置 | 目标相机 | t_uniform | t_pose (VGGT) | t_posecal (标定) | t_oracle |
|---|---:|---:|---:|---:|---:|
| in035 | 1 | — | 0.357 | — | — |
| in035 | 2 | — | 0.688 | — | — |
| in035 | 4 | — | 0.481 | — | — |

## AnySplat 运行统计

旋转/光心误差：vggt 行是联合估计与输入视点估计的一致性；calib/calibK 行是标定位姿经 Sim(3) 对齐到AnySplat 输入视点位姿后的残差（反映 AnySplat 自身预测的输入相机几何与真实阵列的偏差）。

| 设置 | 变体 | 位姿来源 | 窗口边长 | 渲染分辨率 | 模式 | eps2d | 3D 滤波 | 高斯数 | 编码 s | 渲染 ms/视点 | 输入视点自渲染 PSNR | 最大旋转误差° | 最大光心误差/基线 |
|---|---|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 877 | None | classic | 1.15 | False | 389297 | 0.660 | 113.2 | 27.94 | 0.12 | 0.030 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1298238 | 0.818 | 196.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1298238 | 0.818 | 196.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1013333 | 0.818 | 8.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1013333 | 0.818 | 8.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1013333 | 0.818 | 8.5 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.553 | 0.073 |
| in035 | mask_ent | 0.728 | 0.073 |
| in035 | mask_grad | 0.405 | 0.073 |
| in035 | r_col | 0.876 | 0.073 |
| in035 | r_warp | 0.854 | 0.073 |

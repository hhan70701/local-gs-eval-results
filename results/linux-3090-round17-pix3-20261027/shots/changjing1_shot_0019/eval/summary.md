# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.8% | 25.29 / 0.0098 | 23.30 / 0.0139 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 7.8% | 24.86 / 0.0096 | 21.77 / 0.0218 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 1.7% | 23.42 / 0.0052 | 16.60 / 0.0241 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.7% | 25.63 / 0.0109 | 23.85 / 0.0164 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.7% | 25.56 / 0.0109 | 23.31 / 0.0202 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 1.9% | 23.70 / 0.0037 | 18.45 / 0.0099 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.98 / 0.0463 | — / — | 20.50 / 0.0096 | 29.75 / 0.0330 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.87 / 0.0487 | — / — | 20.88 / 0.0093 | 29.65 / 0.0344 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.20 / 0.0519 | — / — | 20.11 / 0.0126 | 29.51 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.23 / 0.0498 | — / — | 20.00 / 0.0123 | 29.54 / 0.0337 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.36 / 0.0508 | — / — | 20.30 / 0.0120 | 29.71 / 0.0337 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.34 / 0.0519 | — / — | 20.37 / 0.0121 | 29.57 / 0.0344 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.35 / 0.0496 | — / — | 20.11 / 0.0121 | 29.67 / 0.0334 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.3%） | — | — | 27.98 / 0.0463 | — / — | 29.75 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.29 / 0.0442 | — | — | — |
| in035 | 2 | 0-3 | 27.74 / 0.0459 | — | — | — |
| in035 | 4 | 3-5 | 28.92 / 0.0487 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.98 / 0.0463 | — | 29.75 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.87 / 0.0487 | — | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.7% | 28.08 / 0.0460 | — | 29.75 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.20 / 0.0519 | — | 29.51 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.5% | 27.65 / 0.0491 | — | 29.73 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.23 / 0.0498 | — | 29.54 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.7% | 27.62 / 0.0486 | — | 29.73 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.36 / 0.0508 | — | 29.71 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.8% | 27.70 / 0.0484 | — | 29.75 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.34 / 0.0519 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 1.8% | 27.76 / 0.0488 | — | 29.73 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.35 / 0.0496 | — | 29.67 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.7% | 27.68 / 0.0484 | — | 29.73 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.98 / 0.0463 | — / — | 29.75 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.87 / 0.0487 | — / — | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.08 / 0.0460 | — / — | 29.75 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 20.50 / 0.0096 | 29.75 / 0.0330 | 27.98 / 0.0463 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.50 | 0.7050 | 0.0096 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.52 | 0.3482 | 0.0744 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.16 | 0.2886 | 0.0609 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.16 | 0.2886 | 0.0609 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.35 | 0.3201 | 0.0588 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.39 | 0.3071 | 0.0578 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 11.39 | 0.3071 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.89 | 0.7441 | 0.0092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.13 | 0.7134 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.02 | 0.7005 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.32 | 0.7305 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.39 | 0.7225 | 0.0120 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.13 | 0.6993 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.88 | 0.7436 | 0.0093 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.11 | 0.7127 | 0.0126 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.00 | 0.6997 | 0.0123 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.30 | 0.7294 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.37 | 0.7211 | 0.0121 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.11 | 0.6983 | 0.0121 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 27.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.28 | 0.7954 | 0.0173 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.27 | 0.4648 | 0.1650 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.30 | 0.3899 | 0.1449 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.30 | 0.3899 | 0.1449 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.46 | 0.4240 | 0.1332 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.50 | 0.4146 | 0.1371 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.50 | 0.4146 | 0.1371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.64 | 0.8064 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.77 | 0.7946 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.69 | 0.7908 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.88 | 0.7993 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.01 | 0.7977 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.80 | 0.7907 | 0.0194 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.69 | 0.7966 | 0.0205 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.78 | 0.7808 | 0.0261 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.91 | 0.7831 | 0.0215 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.10 | 0.7911 | 0.0214 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.06 | 0.7868 | 0.0232 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.98 | 0.7805 | 0.0213 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.75 | 0.7297 | 0.0330 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.95 | 0.2699 | 0.3205 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.46 | 0.1779 | 0.2648 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.46 | 0.1779 | 0.2648 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.76 | 0.2015 | 0.2531 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.75 | 0.2014 | 0.2564 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.75 | 0.2014 | 0.2564 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.75 | 0.7298 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.73 | 0.7297 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.73 | 0.7296 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.75 | 0.7299 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.73 | 0.7297 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.73 | 0.7297 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.65 | 0.7293 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.51 | 0.7287 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.54 | 0.7285 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.71 | 0.7301 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.57 | 0.7293 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.67 | 0.7293 | 0.0334 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.98 | 0.7399 | 0.0463 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.29 | 0.2963 | 0.3777 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.46 | 0.2108 | 0.3459 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.46 | 0.2108 | 0.3459 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.74 | 0.2355 | 0.3302 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.74 | 0.2343 | 0.3338 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.74 | 0.2343 | 0.3338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.08 | 0.7423 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.65 | 0.7393 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.62 | 0.7382 | 0.0486 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.70 | 0.7405 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.76 | 0.7399 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.68 | 0.7381 | 0.0484 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.87 | 0.7404 | 0.0487 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.20 | 0.7366 | 0.0519 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.23 | 0.7360 | 0.0498 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.36 | 0.7388 | 0.0508 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.34 | 0.7376 | 0.0519 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.35 | 0.7361 | 0.0496 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 685 | None | classic | 0.46 | False | 402154 | 0.974 | 168.3 | 31.62 | 0.27 | 0.017 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301917 | 0.800 | 194.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301917 | 0.800 | 194.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 983333 | 0.800 | 8.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 983333 | 0.800 | 8.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 983333 | 0.800 | 8.2 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.604 | 0.020 |
| in035 | mask_ent | 0.712 | 0.020 |
| in035 | mask_grad | 0.428 | 0.020 |
| in035 | r_col | 0.741 | 0.020 |
| in035 | r_warp | 0.840 | 0.020 |

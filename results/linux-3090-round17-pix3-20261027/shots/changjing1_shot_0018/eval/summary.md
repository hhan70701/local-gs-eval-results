# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.7% | 23.79 / 0.0101 | 21.32 / 0.0173 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 6.0% | 23.06 / 0.0089 | 19.74 / 0.0239 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.2% | 20.21 / 0.0061 | 16.17 / 0.0181 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 7.3% | 23.60 / 0.0101 | 20.75 / 0.0191 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 7.2% | 23.59 / 0.0098 | 20.69 / 0.0216 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.4% | 20.66 / 0.0064 | 16.74 / 0.0164 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.69 / 0.0527 | — / — | 20.05 / 0.0133 | 29.90 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.29 / 0.0580 | — / — | 19.87 / 0.0137 | 29.79 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.92 / 0.0599 | — / — | 19.68 / 0.0173 | 29.71 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.96 / 0.0581 | — / — | 19.66 / 0.0167 | 29.72 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.96 / 0.0598 | — / — | 19.86 / 0.0160 | 29.75 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.01 / 0.0612 | — / — | 19.85 / 0.0163 | 29.73 / 0.0391 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.00 / 0.0583 | — / — | 19.74 / 0.0162 | 29.73 / 0.0376 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 7.2%） | — | — | 27.69 / 0.0527 | — / — | 29.90 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.83 / 0.0538 | — | — | — |
| in035 | 2 | 0-3 | 27.52 / 0.0518 | — | — | — |
| in035 | 4 | 3-5 | 28.73 / 0.0526 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.69 / 0.0527 | — | 29.90 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.29 / 0.0580 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.6% | 27.57 / 0.0535 | — | 29.90 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 26.92 / 0.0599 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.4% | 27.38 / 0.0565 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.96 / 0.0581 | — | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.9% | 27.37 / 0.0559 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 26.96 / 0.0598 | — | 29.75 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.5% | 27.41 / 0.0551 | — | 29.90 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.01 / 0.0612 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 1.5% | 27.43 / 0.0553 | — | 29.90 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.00 / 0.0583 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.9% | 27.39 / 0.0552 | — | 29.89 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.69 / 0.0527 | — / — | 29.90 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.29 / 0.0580 | — / — | 29.79 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.57 / 0.0535 | — / — | 29.90 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 20.05 / 0.0133 | 29.90 / 0.0355 | 27.69 / 0.0527 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 7.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.05 | 0.6686 | 0.0133 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.20 | 0.3440 | 0.0898 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.82 | 0.3372 | 0.0684 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.82 | 0.3372 | 0.0684 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.83 | 0.4237 | 0.0611 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.76 | 0.3900 | 0.0623 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 11.76 | 0.3900 | 0.0623 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.90 | 0.6762 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.70 | 0.6639 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.69 | 0.6602 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.87 | 0.6820 | 0.0159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.87 | 0.6725 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.76 | 0.6624 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.87 | 0.6755 | 0.0137 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.68 | 0.6623 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.66 | 0.6583 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.86 | 0.6809 | 0.0160 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.85 | 0.6704 | 0.0163 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.74 | 0.6607 | 0.0162 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 28.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.63 | 0.7701 | 0.0216 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.67 | 0.4737 | 0.2202 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.99 | 0.3564 | 0.1843 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.99 | 0.3564 | 0.1843 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.32 | 0.3958 | 0.1699 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.31 | 0.3838 | 0.1753 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.31 | 0.3838 | 0.1753 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.27 | 0.7674 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.87 | 0.7624 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.88 | 0.7617 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.98 | 0.7681 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.03 | 0.7655 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.97 | 0.7627 | 0.0242 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.35 | 0.7505 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.94 | 0.7408 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.08 | 0.7458 | 0.0286 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.12 | 0.7518 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.10 | 0.7457 | 0.0294 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.14 | 0.7470 | 0.0276 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.90 | 0.7361 | 0.0355 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.23 | 0.3460 | 0.3764 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.20 | 0.1952 | 0.2920 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.20 | 0.1952 | 0.2920 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.66 | 0.2291 | 0.2730 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.66 | 0.2305 | 0.2786 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.66 | 0.2305 | 0.2786 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.90 | 0.7361 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.89 | 0.7361 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.89 | 0.7361 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.90 | 0.7362 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.90 | 0.7362 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.89 | 0.7361 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.79 | 0.7358 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.71 | 0.7355 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.72 | 0.7352 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.75 | 0.7351 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.73 | 0.7353 | 0.0391 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.73 | 0.7349 | 0.0376 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.69 | 0.7371 | 0.0527 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.74 | 0.3587 | 0.4402 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.23 | 0.2267 | 0.3845 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.23 | 0.2267 | 0.3845 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.72 | 0.2651 | 0.3541 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.72 | 0.2632 | 0.3644 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.72 | 0.2632 | 0.3644 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.57 | 0.7368 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.38 | 0.7351 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.37 | 0.7348 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.41 | 0.7365 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.43 | 0.7358 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.39 | 0.7350 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.29 | 0.7339 | 0.0580 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.92 | 0.7308 | 0.0599 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.96 | 0.7309 | 0.0581 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.96 | 0.7324 | 0.0598 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.01 | 0.7316 | 0.0612 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.00 | 0.7311 | 0.0583 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 804 | None | classic | 0.97 | False | 485988 | 1.039 | 163.7 | 27.87 | 0.29 | 0.011 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1276086 | 0.809 | 194.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1276086 | 0.809 | 194.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1018427 | 0.809 | 7.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1018427 | 0.809 | 8.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1018427 | 0.809 | 8.2 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.573 | 0.024 |
| in035 | mask_ent | 0.717 | 0.024 |
| in035 | mask_grad | 0.427 | 0.024 |
| in035 | r_col | 0.771 | 0.024 |
| in035 | r_warp | 0.847 | 0.024 |

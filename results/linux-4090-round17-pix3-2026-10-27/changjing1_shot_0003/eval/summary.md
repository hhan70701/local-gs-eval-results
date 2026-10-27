# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 29.5% | 28.30 / 0.0311 | 29.04 / 0.0632 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 26.7% | 28.27 / 0.0295 | 29.44 / 0.0420 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.7% | 23.67 / 0.0125 | 22.46 / 0.0207 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 28.0% | 28.53 / 0.0300 | 29.92 / 0.0413 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 27.9% | 28.50 / 0.0303 | 29.41 / 0.0443 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.9% | 23.98 / 0.0117 | 21.66 / 0.0212 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 30.70 / 0.0739 | — / — | 20.51 / 0.0185 | 32.23 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.35 / 0.1016 | — / — | 23.19 / 0.0155 | 32.03 / 0.0434 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.85 / 0.0821 | — / — | 23.71 / 0.0166 | 32.29 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.28 / 0.0749 | — / — | 22.34 / 0.0177 | 32.21 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 32.01 / 0.0821 | — / — | 24.25 / 0.0150 | 32.26 / 0.0398 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 31.93 / 0.0832 | — / — | 23.77 / 0.0151 | 32.26 / 0.0405 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 31.30 / 0.0746 | — / — | 22.40 / 0.0170 | 32.17 / 0.0380 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 3.4%） | — | — | 30.70 / 0.0739 | — / — | 32.23 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 29.08 / 0.0830 | — | — | — |
| in035 | 2 | 0-3 | 31.63 / 0.0694 | — | — | — |
| in035 | 4 | 3-5 | 31.39 / 0.0694 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 30.70 / 0.0739 | — | 32.23 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 31.35 / 0.1016 | — | 32.03 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 31.66 / 0.0736 | — | 32.24 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 31.85 / 0.0821 | — | 32.29 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.2% | 31.75 / 0.0736 | — | 32.24 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 31.28 / 0.0749 | — | 32.21 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.1% | 31.43 / 0.0733 | — | 32.23 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 32.01 / 0.0821 | — | 32.26 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.2% | 31.90 / 0.0731 | — | 32.25 | 2/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 31.93 / 0.0832 | — | 32.26 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.3% | 31.77 / 0.0729 | — | 32.25 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 31.30 / 0.0746 | — | 32.17 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.2% | 31.45 / 0.0728 | — | 32.23 | 1/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 30.70 / 0.0739 | — / — | 32.23 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 31.35 / 0.1016 | — / — | 32.03 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 31.66 / 0.0736 | — / — | 32.24 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 20.51 / 0.0185 | 32.23 / 0.0371 | 30.70 / 0.0739 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 3.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.51 | 0.6267 | 0.0185 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.77 | 0.6636 | 0.0418 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 17.05 | 0.6454 | 0.0405 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 17.05 | 0.6454 | 0.0405 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 17.66 | 0.6958 | 0.0367 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 17.78 | 0.6758 | 0.0374 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 17.78 | 0.6758 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.21 | 0.7357 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.71 | 0.7249 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.35 | 0.6834 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.27 | 0.7537 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 23.77 | 0.7407 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 22.41 | 0.6922 | 0.0170 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.19 | 0.7343 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.71 | 0.7230 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.34 | 0.6820 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.25 | 0.7521 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 23.77 | 0.7395 | 0.0151 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 22.40 | 0.6908 | 0.0170 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 60.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.14 | 0.8235 | 0.0440 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.10 | 0.6708 | 0.3103 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.58 | 0.5064 | 0.2875 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.58 | 0.5064 | 0.2875 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.88 | 0.5129 | 0.2807 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.83 | 0.5234 | 0.2839 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.83 | 0.5234 | 0.2839 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.55 | 0.8355 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.44 | 0.8321 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 30.06 | 0.8289 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 30.73 | 0.8348 | 0.0458 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 30.49 | 0.8338 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 30.09 | 0.8299 | 0.0447 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.51 | 0.8336 | 0.0699 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.57 | 0.8325 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.02 | 0.8211 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.82 | 0.8266 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.55 | 0.8368 | 0.0562 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.94 | 0.8224 | 0.0499 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 50.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 32.23 | 0.8147 | 0.0371 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.84 | 0.5990 | 0.3373 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.28 | 0.3734 | 0.2943 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.28 | 0.3734 | 0.2943 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.73 | 0.4081 | 0.2775 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.74 | 0.4218 | 0.2810 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 11.74 | 0.4218 | 0.2810 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.24 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 32.24 | 0.8149 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 32.25 | 0.8149 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 32.25 | 0.8149 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.03 | 0.8141 | 0.0434 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 32.29 | 0.8161 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 32.21 | 0.8144 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 32.26 | 0.8131 | 0.0398 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 32.26 | 0.8164 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 32.17 | 0.8142 | 0.0380 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.70 | 0.8223 | 0.0739 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.97 | 0.6669 | 0.4347 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.83 | 0.4769 | 0.3798 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.83 | 0.4769 | 0.3798 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.24 | 0.4910 | 0.3594 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.22 | 0.5097 | 0.3667 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.22 | 0.5097 | 0.3667 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.66 | 0.8279 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.75 | 0.8280 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.43 | 0.8261 | 0.0733 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 31.90 | 0.8287 | 0.0731 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 31.77 | 0.8289 | 0.0729 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 31.45 | 0.8266 | 0.0728 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.35 | 0.8321 | 0.1016 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.85 | 0.8357 | 0.0821 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.28 | 0.8251 | 0.0749 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 32.01 | 0.8271 | 0.0821 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 31.93 | 0.8381 | 0.0832 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 31.30 | 0.8255 | 0.0746 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1101 | None | classic | 1.81 | False | 189767 | 0.177 | 33.5 | 32.31 | 0.28 | 0.006 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1596720 | 0.794 | 95.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1596720 | 0.794 | 95.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301527 | 0.794 | 9.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301527 | 0.794 | 7.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301527 | 0.794 | 7.4 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.734 | 0.014 |
| in035 | mask_ent | 0.808 | 0.014 |
| in035 | mask_grad | 0.408 | 0.014 |
| in035 | r_col | 0.684 | 0.014 |
| in035 | r_warp | 0.860 | 0.014 |

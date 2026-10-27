# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.0% | 24.86 / 0.0110 | 22.66 / 0.0223 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 7.8% | 24.22 / 0.0106 | 21.11 / 0.0230 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.0% | 21.05 / 0.0055 | 16.70 / 0.0160 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.0% | 25.13 / 0.0123 | 22.88 / 0.0210 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.9% | 25.10 / 0.0119 | 22.64 / 0.0243 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.1% | 21.55 / 0.0056 | 17.65 / 0.0155 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.20 / 0.0540 | — / — | 20.68 / 0.0132 | 29.79 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.83 / 0.0614 | — / — | 20.88 / 0.0143 | 29.60 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.35 / 0.0618 | — / — | 20.02 / 0.0162 | 29.48 / 0.0396 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.37 / 0.0602 | — / — | 19.91 / 0.0160 | 29.52 / 0.0393 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.47 / 0.0596 | — / — | 20.38 / 0.0148 | 29.71 / 0.0398 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.47 / 0.0624 | — / — | 20.36 / 0.0154 | 29.57 / 0.0403 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.47 / 0.0602 | — / — | 20.09 / 0.0155 | 29.67 / 0.0393 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.0%） | — | — | 28.20 / 0.0540 | — / — | 29.79 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.63 / 0.0519 | — | — | — |
| in035 | 2 | 0-3 | 28.60 / 0.0537 | — | — | — |
| in035 | 4 | 3-5 | 28.39 / 0.0564 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.20 / 0.0540 | — | 29.79 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.83 / 0.0614 | — | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.8% | 28.19 / 0.0565 | — | 29.78 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.35 / 0.0618 | — | 29.48 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.7% | 27.87 / 0.0575 | — | 29.78 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.37 / 0.0602 | — | 29.52 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.7% | 27.83 / 0.0570 | — | 29.78 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.47 / 0.0596 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.0% | 28.01 / 0.0557 | — | 29.82 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.47 / 0.0624 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 1.9% | 27.99 / 0.0571 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.47 / 0.0602 | — | 29.67 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.7% | 27.89 / 0.0569 | — | 29.79 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.20 / 0.0540 | — / — | 29.79 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.83 / 0.0614 | — / — | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.19 / 0.0565 | — / — | 29.78 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 20.68 / 0.0132 | 29.79 / 0.0372 | 28.20 / 0.0540 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.68 | 0.7004 | 0.0132 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.81 | 0.3876 | 0.0978 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.12 | 0.3786 | 0.0648 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.12 | 0.3786 | 0.0648 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.59 | 0.4420 | 0.0595 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.55 | 0.4145 | 0.0609 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.55 | 0.4145 | 0.0609 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.90 | 0.7293 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.02 | 0.7076 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.91 | 0.6934 | 0.0159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.38 | 0.7324 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.37 | 0.7215 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.10 | 0.6979 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.88 | 0.7283 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.02 | 0.7072 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.91 | 0.6927 | 0.0160 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.38 | 0.7332 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.36 | 0.7208 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.09 | 0.6968 | 0.0155 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 27.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.10 | 0.7801 | 0.0202 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.31 | 0.5072 | 0.2078 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.68 | 0.3886 | 0.1591 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.68 | 0.3886 | 0.1591 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.79 | 0.4118 | 0.1527 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.79 | 0.4032 | 0.1558 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.79 | 0.4032 | 0.1558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.15 | 0.7867 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.47 | 0.7799 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.40 | 0.7757 | 0.0228 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.66 | 0.7858 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.68 | 0.7836 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.53 | 0.7769 | 0.0222 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.85 | 0.7730 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.45 | 0.7634 | 0.0289 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.51 | 0.7624 | 0.0262 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.64 | 0.7717 | 0.0255 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.63 | 0.7673 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.61 | 0.7630 | 0.0258 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.79 | 0.7321 | 0.0372 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.81 | 0.3279 | 0.3843 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.56 | 0.1804 | 0.2931 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.56 | 0.1804 | 0.2931 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.76 | 0.1967 | 0.2847 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.74 | 0.1951 | 0.2879 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.74 | 0.1951 | 0.2879 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.78 | 0.7320 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.78 | 0.7320 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.78 | 0.7320 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.82 | 0.7326 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.79 | 0.7322 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.79 | 0.7320 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.60 | 0.7308 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.48 | 0.7304 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.52 | 0.7303 | 0.0393 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.71 | 0.7319 | 0.0398 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.57 | 0.7312 | 0.0403 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.67 | 0.7311 | 0.0393 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.20 | 0.7401 | 0.0540 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.31 | 0.3531 | 0.4407 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.71 | 0.2227 | 0.3773 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.71 | 0.2227 | 0.3773 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.92 | 0.2421 | 0.3614 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.90 | 0.2387 | 0.3694 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.90 | 0.2387 | 0.3694 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.19 | 0.7414 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.87 | 0.7399 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.83 | 0.7388 | 0.0570 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.01 | 0.7421 | 0.0557 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.99 | 0.7412 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.89 | 0.7391 | 0.0569 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.83 | 0.7382 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.35 | 0.7355 | 0.0618 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.37 | 0.7346 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.47 | 0.7385 | 0.0596 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.47 | 0.7371 | 0.0624 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.47 | 0.7355 | 0.0602 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 956 | None | classic | 1.37 | False | 410737 | 0.348 | 61.5 | 28.18 | 0.20 | 0.037 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1317437 | 0.804 | 88.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1317437 | 0.804 | 88.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1010915 | 0.804 | 9.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1010915 | 0.804 | 8.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1010915 | 0.804 | 8.0 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.613 | 0.017 |
| in035 | mask_ent | 0.726 | 0.017 |
| in035 | mask_grad | 0.439 | 0.017 |
| in035 | r_col | 0.795 | 0.017 |
| in035 | r_warp | 0.836 | 0.017 |

# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 3.4% | 25.16 / 0.0045 | 18.20 / 0.0152 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.7% | 25.26 / 0.0047 | 19.31 / 0.0125 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.5% | 25.25 / 0.0046 | 18.95 / 0.0136 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.6% | 25.26 / 0.0047 | 19.02 / 0.0133 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.4% | 25.23 / 0.0042 | 19.90 / 0.0096 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.5% | 25.18 / 0.0044 | 20.76 / 0.0080 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.4% | 25.24 / 0.0044 | 21.11 / 0.0079 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.4% | 25.20 / 0.0044 | 21.18 / 0.0077 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 3.1% | 25.08 / 0.0045 | 23.42 / 0.0095 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 2.8% | 24.91 / 0.0043 | 20.12 / 0.0132 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 1.1% | 23.88 / 0.0028 | 16.90 / 0.0091 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 2.8% | 24.95 / 0.0044 | 18.95 / 0.0139 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 1.2% | 25.60 / 0.0027 | 14.94 / 0.0103 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 3.1% | 25.07 / 0.0044 | 22.77 / 0.0071 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 2.8% | 24.75 / 0.0045 | 19.66 / 0.0119 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 1.3% | 23.74 / 0.0030 | 16.94 / 0.0083 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 2.8% | 24.81 / 0.0045 | 18.70 / 0.0127 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 1.3% | 24.08 / 0.0030 | 16.27 / 0.0089 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 3.7% | 25.35 / 0.0047 | 20.49 / 0.0153 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 8.9% | 26.89 / 0.0078 | 19.01 / 0.0292 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.4% | 26.94 / 0.0080 | 19.58 / 0.0255 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.1% | 26.90 / 0.0078 | 19.31 / 0.0270 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.2% | 26.92 / 0.0080 | 19.39 / 0.0264 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 9.1% | 26.83 / 0.0075 | 20.15 / 0.0246 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.7% | 26.96 / 0.0079 | 21.09 / 0.0196 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.3% | 26.89 / 0.0077 | 21.41 / 0.0212 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.4% | 26.88 / 0.0077 | 21.54 / 0.0198 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 9.5% | 26.97 / 0.0079 | 20.59 / 0.0360 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 4.7% | 28.65 / 0.0072 | 22.81 / 0.0213 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 5.3% | 28.61 / 0.0077 | 24.27 / 0.0201 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 5.1% | 28.67 / 0.0074 | 24.09 / 0.0206 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 5.1% | 28.59 / 0.0073 | 24.37 / 0.0193 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 5.5% | 28.73 / 0.0078 | 23.55 / 0.0178 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 6.1% | 28.72 / 0.0079 | 23.76 / 0.0192 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 5.7% | 28.72 / 0.0082 | 24.18 / 0.0189 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 5.8% | 28.64 / 0.0080 | 23.97 / 0.0192 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.74 / 0.0512 | 28.61 / 0.0414 | 21.68 / 0.0095 | 29.73 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.92 / 0.0571 | 27.92 / 0.0682 | 20.78 / 0.0110 | 29.65 / 0.0381 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.12 / 0.0555 | 28.03 / 0.0639 | 20.94 / 0.0105 | 29.68 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.04 / 0.0564 | 27.84 / 0.0676 | 20.86 / 0.0107 | 29.68 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.04 / 0.0559 | 27.93 / 0.0682 | 20.82 / 0.0107 | 29.68 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.48 / 0.0538 | 28.89 / 0.0528 | 21.66 / 0.0092 | 29.69 / 0.0375 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.60 / 0.0524 | 28.89 / 0.0475 | 21.82 / 0.0089 | 29.71 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.62 / 0.0528 | 29.09 / 0.0499 | 21.83 / 0.0089 | 29.72 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.62 / 0.0525 | 29.04 / 0.0476 | 21.87 / 0.0089 | 29.71 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.58 / 0.0526 | 28.78 / 0.0692 | 21.40 / 0.0101 | 29.74 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.12 / 0.0552 | 29.10 / 0.0487 | 20.70 / 0.0116 | 29.72 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.14 / 0.0537 | 28.45 / 0.0451 | 20.63 / 0.0110 | 29.73 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.85 / 0.0559 | 28.72 / 0.0540 | 20.84 / 0.0113 | 29.67 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.86 / 0.0546 | 28.15 / 0.0487 | 20.74 / 0.0111 | 29.68 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.54 / 0.0518 | 29.11 / 0.0514 | 21.30 / 0.0096 | 29.73 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.03 / 0.0540 | 29.02 / 0.0491 | 20.38 / 0.0110 | 29.72 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.05 / 0.0531 | 28.40 / 0.0459 | 20.32 / 0.0107 | 29.73 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.78 / 0.0548 | 28.67 / 0.0518 | 20.46 / 0.0109 | 29.68 / 0.0375 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.79 / 0.0538 | 28.13 / 0.0485 | 20.42 / 0.0105 | 29.68 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.16 / 0.0546 | 27.98 / 0.0720 | 20.73 / 0.0108 | 29.71 / 0.0377 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.86 / 0.0661 | 25.93 / 0.1021 | 19.66 / 0.0138 | 29.16 / 0.0415 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.18 / 0.0620 | 27.09 / 0.0798 | 19.91 / 0.0124 | 29.29 / 0.0409 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.04 / 0.0637 | 26.66 / 0.0914 | 19.85 / 0.0129 | 29.25 / 0.0412 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.09 / 0.0629 | 26.86 / 0.0852 | 19.87 / 0.0127 | 29.29 / 0.0411 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.42 / 0.0615 | 24.21 / 0.0931 | 20.56 / 0.0126 | 29.36 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.02 / 0.0568 | 25.76 / 0.0726 | 21.37 / 0.0107 | 29.54 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.82 / 0.0596 | 25.44 / 0.0827 | 21.02 / 0.0115 | 29.51 / 0.0397 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.90 / 0.0585 | 25.77 / 0.0774 | 21.18 / 0.0112 | 29.51 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.77 / 0.0605 | 24.62 / 0.1587 | 20.37 / 0.0126 | 29.60 / 0.0390 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 28.12 / 0.0581 | 27.34 / 0.0785 | 21.28 / 0.0107 | 29.67 / 0.0382 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.40 / 0.0563 | 28.70 / 0.0583 | 21.59 / 0.0101 | 29.69 / 0.0380 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.31 / 0.0574 | 27.80 / 0.0737 | 21.47 / 0.0103 | 29.69 / 0.0382 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.36 / 0.0567 | 28.16 / 0.0668 | 21.53 / 0.0102 | 29.69 / 0.0381 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.45 / 0.0560 | 26.32 / 0.0681 | 21.53 / 0.0101 | 29.67 / 0.0383 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.48 / 0.0561 | 28.25 / 0.0474 | 21.71 / 0.0106 | 29.69 / 0.0383 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.43 / 0.0567 | 27.29 / 0.0599 | 21.63 / 0.0103 | 29.68 / 0.0384 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.46 / 0.0566 | 27.86 / 0.0543 | 21.73 / 0.0103 | 29.69 / 0.0383 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.5%） | — | — | 28.74 / 0.0512 | 28.61 / 0.0414 | 29.73 |
| in035 | rife | 1.8% | 4.7% | 28.12 / 0.0581 | 27.34 / 0.0785 | 29.67 |
| in035 | cnw_cnn | 1.7% | 3.4% | 27.92 / 0.0571 | 27.92 / 0.0682 | 29.65 |
| in035 | cnw_f5 | 5.0% | 8.9% | 26.86 / 0.0661 | 25.93 / 0.1021 | 29.16 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 28.09 / 0.0523 | -0.77 / +0.0084 (core 2.3%) | -0.75 / +0.0064 (core 2.2%) | -1.55 / +0.0166 (core 6.1%) |
| in035 | 2 | 0-3 | 28.83 / 0.0487 | -1.05 / +0.0109 (core 2.3%) | -1.47 / +0.0079 (core 2.2%) | -2.55 / +0.0203 (core 6.1%) |
| in035 | 4 | 3-5 | 29.29 / 0.0525 | -0.03 / +0.0014 (core 0.7%) | -0.24 / +0.0035 (core 0.4%) | -1.53 / +0.0078 (core 2.2%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.74 / 0.0512 | 28.61 | 29.73 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.92 / 0.0571 | 27.92 | 29.65 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.39 / 0.0528 | 28.91 | 29.73 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.12 / 0.0555 | 28.03 | 29.68 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.47 / 0.0522 | 29.07 | 29.73 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.04 / 0.0564 | 27.84 | 29.68 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.43 / 0.0526 | 28.91 | 29.73 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.04 / 0.0559 | 27.93 | 29.68 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.42 / 0.0524 | 28.98 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.48 / 0.0538 | 28.89 | 29.69 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.70 / 0.0513 | 29.08 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.60 / 0.0524 | 28.89 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.75 / 0.0509 | 29.07 | 29.73 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.62 / 0.0528 | 29.09 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.76 / 0.0510 | 29.21 | 29.73 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.62 / 0.0525 | 29.04 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.77 / 0.0510 | 29.17 | 29.73 | 2/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 28.58 / 0.0526 | 28.78 | 29.74 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 0.5% | 28.64 / 0.0516 | 29.34 | 29.74 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 28.12 / 0.0552 | 29.10 | 29.72 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 0.4% | 28.30 / 0.0532 | 29.06 | 29.74 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 28.14 / 0.0537 | 28.45 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 0.2% | 28.30 / 0.0524 | 28.45 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.85 / 0.0559 | 28.72 | 29.67 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 0.4% | 28.38 / 0.0530 | 28.71 | 29.74 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.86 / 0.0546 | 28.15 | 29.68 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 0.2% | 28.37 / 0.0527 | 28.19 | 29.73 | 1/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 28.54 / 0.0518 | 29.11 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 0.5% | 28.61 / 0.0512 | 29.21 | 29.74 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.03 / 0.0540 | 29.02 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 0.5% | 28.19 / 0.0525 | 28.93 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.05 / 0.0531 | 28.40 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.3% | 28.19 / 0.0521 | 28.42 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.78 / 0.0548 | 28.67 | 29.68 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 0.4% | 28.25 / 0.0526 | 28.60 | 29.74 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.79 / 0.0538 | 28.13 | 29.68 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 0.2% | 28.24 / 0.0521 | 28.16 | 29.74 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 28.16 / 0.0546 | 27.98 | 29.71 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 0.5% | 28.34 / 0.0522 | 28.58 | 29.73 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.86 / 0.0661 | 25.93 | 29.16 | 0/3 |
| in035 | cnw_f5 | oracle | 1.2% | 28.00 / 0.0555 | 27.41 | 29.71 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.18 / 0.0620 | 27.09 | 29.29 | 0/3 |
| in035 | cnw_f5 | oracle | 1.2% | 28.13 / 0.0543 | 27.96 | 29.71 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.04 / 0.0637 | 26.66 | 29.25 | 0/3 |
| in035 | cnw_f5 | oracle | 1.2% | 28.08 / 0.0547 | 27.66 | 29.72 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.09 / 0.0629 | 26.86 | 29.29 | 0/3 |
| in035 | cnw_f5 | oracle | 1.2% | 28.09 / 0.0543 | 27.79 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.42 / 0.0615 | 24.21 | 29.36 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.2% | 28.29 / 0.0541 | 26.35 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.02 / 0.0568 | 25.76 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.2% | 28.57 / 0.0524 | 27.16 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.82 / 0.0596 | 25.44 | 29.51 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.2% | 28.46 / 0.0535 | 26.86 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.90 / 0.0585 | 25.77 | 29.51 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.2% | 28.51 / 0.0530 | 27.12 | 29.73 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.77 / 0.0605 | 24.62 | 29.60 | 0/3 |
| in035 | cnw_f5_pix | oracle | 1.2% | 28.20 / 0.0542 | 28.44 | 29.73 | 0/3 |
| in035 | rife | 不复核 | —% | 28.12 / 0.0581 | 27.34 | 29.67 | 0/3 |
| in035 | rife | oracle | 0.4% | 28.57 / 0.0518 | 28.29 | 29.73 | 0/3 |
| in035 | rife | 不复核 | —% | 28.40 / 0.0563 | 28.70 | 29.69 | 0/3 |
| in035 | rife | oracle | 0.4% | 28.69 / 0.0514 | 28.65 | 29.73 | 1/3 |
| in035 | rife | 不复核 | —% | 28.31 / 0.0574 | 27.80 | 29.69 | 0/3 |
| in035 | rife | oracle | 0.4% | 28.64 / 0.0516 | 28.22 | 29.73 | 0/3 |
| in035 | rife | 不复核 | —% | 28.36 / 0.0567 | 28.16 | 29.69 | 0/3 |
| in035 | rife | oracle | 0.4% | 28.67 / 0.0515 | 28.33 | 29.73 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 28.45 / 0.0560 | 26.32 | 29.67 | 0/3 |
| in035 | rife_mw | oracle | 0.4% | 28.67 / 0.0514 | 27.50 | 29.72 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.48 / 0.0561 | 28.25 | 29.69 | 0/3 |
| in035 | rife_mw | oracle | 0.4% | 28.73 / 0.0517 | 28.41 | 29.73 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.43 / 0.0567 | 27.29 | 29.68 | 0/3 |
| in035 | rife_mw | oracle | 0.4% | 28.70 / 0.0515 | 27.73 | 29.72 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.46 / 0.0566 | 27.86 | 29.69 | 0/3 |
| in035 | rife_mw | oracle | 0.4% | 28.73 / 0.0516 | 28.14 | 29.73 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.74 / 0.0512 | 28.61 / 0.0414 | — |
| in035 | FF | 0（前馈） | 1008×587（55%） | 26.22 | 27.92 / 0.0571 | 27.92 / 0.0682 | 0/3 |
| in035 | 25 | 1.22 s | 1008×587（55%） | 26.67 | 28.04 / 0.0564 | 27.84 / 0.0676 | 0/3 |
| in035 | 50 | 2.42 s | 1008×587（55%） | 26.87 | 28.04 / 0.0559 | 27.93 / 0.0682 | 0/3 |
| in035 | 100 | 4.83 s | 1008×587（55%） | 27.06 | 28.12 / 0.0555 | 28.03 / 0.0639 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.74 / 0.0512 | 28.61 / 0.0414 | 29.73 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.92 / 0.0571 | 27.92 / 0.0682 | 29.65 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.39 / 0.0528 | 28.91 / 0.0471 | 29.73 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.04 / 0.0564 | 27.84 / 0.0676 | 29.68 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.43 / 0.0526 | 28.91 / 0.0461 | 29.73 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 28.04 / 0.0559 | 27.93 / 0.0682 | 29.68 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.42 / 0.0524 | 28.98 / 0.0451 | 29.73 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 28.12 / 0.0555 | 28.03 / 0.0639 | 29.68 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.47 / 0.0522 | 29.07 / 0.0439 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 28.48 / 0.0538 | 28.89 / 0.0528 | 29.69 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.70 / 0.0513 | 29.08 / 0.0400 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.62 / 0.0528 | 29.09 / 0.0499 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.76 / 0.0510 | 29.21 / 0.0381 | 29.73 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.62 / 0.0525 | 29.04 / 0.0476 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.77 / 0.0510 | 29.17 / 0.0377 | 29.73 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.60 / 0.0524 | 28.89 / 0.0475 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.75 / 0.0509 | 29.07 / 0.0368 | 29.73 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.86 / 0.0661 | 25.93 / 0.1021 | 29.16 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 28.00 / 0.0555 | 27.41 / 0.0588 | 29.71 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.04 / 0.0637 | 26.66 / 0.0914 | 29.25 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 28.08 / 0.0547 | 27.66 / 0.0553 | 29.72 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.09 / 0.0629 | 26.86 / 0.0852 | 29.29 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.09 / 0.0543 | 27.79 / 0.0521 | 29.71 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.18 / 0.0620 | 27.09 / 0.0798 | 29.29 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.13 / 0.0543 | 27.96 / 0.0502 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.42 / 0.0615 | 24.21 / 0.0931 | 29.36 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.29 / 0.0541 | 26.35 / 0.0554 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.82 / 0.0596 | 25.44 / 0.0827 | 29.51 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.46 / 0.0535 | 26.86 / 0.0515 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.90 / 0.0585 | 25.77 / 0.0774 | 29.51 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.51 / 0.0530 | 27.12 / 0.0479 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.02 / 0.0568 | 25.76 / 0.0726 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.57 / 0.0524 | 27.16 / 0.0453 | 29.73 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 28.12 / 0.0581 | 27.34 / 0.0785 | 29.67 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.57 / 0.0518 | 28.29 / 0.0444 | 29.73 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.31 / 0.0574 | 27.80 / 0.0737 | 29.69 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.64 / 0.0516 | 28.22 / 0.0444 | 29.73 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.36 / 0.0567 | 28.16 / 0.0668 | 29.69 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.67 / 0.0515 | 28.33 / 0.0429 | 29.73 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.40 / 0.0563 | 28.70 / 0.0583 | 29.69 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.69 / 0.0514 | 28.65 / 0.0408 | 29.73 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 28.45 / 0.0560 | 26.32 / 0.0681 | 29.67 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.67 / 0.0514 | 27.50 / 0.0422 | 29.72 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.43 / 0.0567 | 27.29 / 0.0599 | 29.68 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.70 / 0.0515 | 27.73 / 0.0430 | 29.72 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.46 / 0.0566 | 27.86 / 0.0543 | 29.69 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.73 / 0.0516 | 28.14 / 0.0437 | 29.73 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.48 / 0.0561 | 28.25 / 0.0474 | 29.69 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.73 / 0.0517 | 28.41 / 0.0407 | 29.73 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.61 / 0.0414 | 21.68 / 0.0095 | 29.73 / 0.0371 | 28.74 / 0.0512 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 3.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.61 | 0.8397 | 0.0414 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 13.78 | 0.6261 | 0.2909 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 15.59 | 0.6839 | 0.2379 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 14.06 | 0.6494 | 0.2718 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 14.62 | 0.6653 | 0.2550 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 13.44 | 0.6462 | 0.2650 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 14.80 | 0.6899 | 0.2275 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 13.60 | 0.6670 | 0.2582 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 13.94 | 0.6780 | 0.2470 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 25.06 | 0.7884 | 0.1301 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 24.90 | 0.8027 | 0.1169 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 24.90 | 0.8027 | 0.1169 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 24.58 | 0.7886 | 0.1231 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 24.58 | 0.7886 | 0.1231 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.23 | 0.6765 | 0.2438 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.77 | 0.6505 | 0.2984 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.77 | 0.6505 | 0.2984 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.73 | 0.6414 | 0.3029 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.73 | 0.6414 | 0.3029 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.33 | 0.6065 | 0.3095 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 24.17 | 0.7726 | 0.1411 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 25.88 | 0.8184 | 0.1009 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 25.05 | 0.8003 | 0.1244 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 25.36 | 0.8105 | 0.1144 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 23.38 | 0.7274 | 0.1223 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 24.62 | 0.7776 | 0.0901 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 24.57 | 0.7672 | 0.1065 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 24.85 | 0.7771 | 0.0980 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 22.70 | 0.7862 | 0.2120 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 25.22 | 0.7831 | 0.1249 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 26.67 | 0.8404 | 0.0837 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 25.96 | 0.8125 | 0.1089 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 26.33 | 0.8273 | 0.0974 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 24.59 | 0.7880 | 0.0881 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 26.19 | 0.8341 | 0.0608 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 25.78 | 0.8204 | 0.0732 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 26.14 | 0.8294 | 0.0667 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.91 | 0.8406 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.07 | 0.8460 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.91 | 0.8430 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.98 | 0.8448 | 0.0451 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.08 | 0.8454 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.07 | 0.8468 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.21 | 0.8462 | 0.0381 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.17 | 0.8462 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.34 | 0.8437 | 0.0493 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.06 | 0.8455 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.45 | 0.8382 | 0.0441 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.71 | 0.8426 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.19 | 0.8372 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.21 | 0.8448 | 0.0463 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.93 | 0.8444 | 0.0442 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.42 | 0.8380 | 0.0426 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.60 | 0.8423 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.16 | 0.8370 | 0.0463 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.58 | 0.8396 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.41 | 0.8242 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.96 | 0.8371 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.66 | 0.8298 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.79 | 0.8337 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.35 | 0.8054 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.16 | 0.8267 | 0.0453 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.86 | 0.8164 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.12 | 0.8226 | 0.0479 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.44 | 0.8385 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.29 | 0.8333 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.65 | 0.8454 | 0.0408 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.22 | 0.8360 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.33 | 0.8402 | 0.0429 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.50 | 0.8277 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.41 | 0.8440 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.73 | 0.8305 | 0.0430 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.14 | 0.8367 | 0.0437 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.92 | 0.8348 | 0.0682 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.03 | 0.8437 | 0.0639 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.84 | 0.8380 | 0.0676 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.93 | 0.8409 | 0.0682 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.89 | 0.8445 | 0.0528 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.89 | 0.8468 | 0.0475 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.09 | 0.8473 | 0.0499 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.04 | 0.8470 | 0.0476 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.78 | 0.8358 | 0.0692 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.10 | 0.8479 | 0.0487 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.45 | 0.8379 | 0.0451 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.72 | 0.8434 | 0.0540 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.15 | 0.8364 | 0.0487 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.11 | 0.8449 | 0.0514 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.02 | 0.8477 | 0.0491 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.40 | 0.8374 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.67 | 0.8448 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.13 | 0.8357 | 0.0485 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.98 | 0.8367 | 0.0720 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.93 | 0.8053 | 0.1021 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.09 | 0.8372 | 0.0798 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.66 | 0.8253 | 0.0914 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.86 | 0.8323 | 0.0852 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.21 | 0.7591 | 0.0931 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.76 | 0.8062 | 0.0726 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.44 | 0.7909 | 0.0827 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.77 | 0.8009 | 0.0774 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.62 | 0.8066 | 0.1587 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.34 | 0.8253 | 0.0785 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.70 | 0.8616 | 0.0583 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.80 | 0.8415 | 0.0737 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.16 | 0.8520 | 0.0668 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.32 | 0.8147 | 0.0681 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.25 | 0.8590 | 0.0474 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.29 | 0.8389 | 0.0599 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.86 | 0.8502 | 0.0543 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 21.68 | 0.7527 | 0.0095 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.31 | 0.1785 | 0.1186 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.37 | 0.2007 | 0.1166 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.32 | 0.1874 | 0.1182 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.34 | 0.1929 | 0.1176 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.31 | 0.2215 | 0.1173 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.35 | 0.2370 | 0.1157 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.32 | 0.2320 | 0.1164 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.33 | 0.2355 | 0.1162 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.02 | 0.2693 | 0.0509 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 12.71 | 0.2298 | 0.0540 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 12.71 | 0.2298 | 0.0540 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 12.65 | 0.2362 | 0.0538 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 12.65 | 0.2362 | 0.0538 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 10.35 | 0.1913 | 0.0691 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.22 | 0.1581 | 0.0715 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.22 | 0.1581 | 0.0715 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 10.20 | 0.1664 | 0.0714 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 10.20 | 0.1664 | 0.0714 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.23 | 0.1552 | 0.0710 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.69 | 0.2581 | 0.0940 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.79 | 0.2859 | 0.0909 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.73 | 0.2732 | 0.0926 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.76 | 0.2804 | 0.0919 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.76 | 0.2954 | 0.0931 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.85 | 0.3420 | 0.0884 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.77 | 0.3197 | 0.0908 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.80 | 0.3312 | 0.0898 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.31 | 0.2729 | 0.0571 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.85 | 0.1578 | 0.1276 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.93 | 0.1779 | 0.1257 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.88 | 0.1682 | 0.1270 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.90 | 0.1725 | 0.1266 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.54 | 0.1420 | 0.1165 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.56 | 0.1552 | 0.1155 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.55 | 0.1453 | 0.1162 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.55 | 0.1502 | 0.1161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.80 | 0.7339 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.95 | 0.7436 | 0.0105 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.87 | 0.7371 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.83 | 0.7395 | 0.0106 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.66 | 0.7611 | 0.0091 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.81 | 0.7654 | 0.0089 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.83 | 0.7640 | 0.0089 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.87 | 0.7657 | 0.0089 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 21.41 | 0.7547 | 0.0101 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.71 | 0.7370 | 0.0116 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.64 | 0.7329 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.87 | 0.7449 | 0.0113 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.77 | 0.7399 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 21.30 | 0.7524 | 0.0096 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.38 | 0.7332 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.33 | 0.7295 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.48 | 0.7417 | 0.0109 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.44 | 0.7388 | 0.0105 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.74 | 0.7351 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.71 | 0.6981 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.94 | 0.7138 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.87 | 0.7055 | 0.0128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.89 | 0.7093 | 0.0126 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.58 | 0.7237 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.38 | 0.7572 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.03 | 0.7397 | 0.0115 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.19 | 0.7484 | 0.0111 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.37 | 0.7167 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 21.29 | 0.7444 | 0.0106 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.60 | 0.7539 | 0.0100 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.47 | 0.7487 | 0.0102 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 21.54 | 0.7513 | 0.0101 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.54 | 0.7504 | 0.0101 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.72 | 0.7604 | 0.0104 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.63 | 0.7528 | 0.0103 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.73 | 0.7570 | 0.0103 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.78 | 0.7329 | 0.0110 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.94 | 0.7427 | 0.0105 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.86 | 0.7361 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.82 | 0.7385 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.66 | 0.7604 | 0.0092 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.82 | 0.7651 | 0.0089 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.83 | 0.7635 | 0.0089 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.87 | 0.7653 | 0.0089 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 21.40 | 0.7542 | 0.0101 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.70 | 0.7370 | 0.0116 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.63 | 0.7330 | 0.0110 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.84 | 0.7446 | 0.0113 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.74 | 0.7396 | 0.0111 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 21.30 | 0.7518 | 0.0096 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.38 | 0.7331 | 0.0110 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.32 | 0.7293 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.46 | 0.7413 | 0.0109 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.42 | 0.7384 | 0.0105 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.73 | 0.7336 | 0.0108 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.66 | 0.6943 | 0.0138 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.91 | 0.7111 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.85 | 0.7021 | 0.0129 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.87 | 0.7063 | 0.0127 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.56 | 0.7207 | 0.0126 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.37 | 0.7553 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.02 | 0.7372 | 0.0115 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.18 | 0.7462 | 0.0112 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.37 | 0.7141 | 0.0126 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.28 | 0.7428 | 0.0107 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.59 | 0.7533 | 0.0101 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.47 | 0.7478 | 0.0103 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 21.53 | 0.7505 | 0.0102 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.53 | 0.7492 | 0.0101 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.71 | 0.7598 | 0.0106 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.63 | 0.7522 | 0.0103 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.73 | 0.7563 | 0.0103 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 26.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.86 | 0.7939 | 0.0165 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.63 | 0.3817 | 0.2511 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.75 | 0.3981 | 0.2423 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.66 | 0.3920 | 0.2480 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.69 | 0.3943 | 0.2456 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.61 | 0.4091 | 0.2452 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.78 | 0.4210 | 0.2369 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.65 | 0.4219 | 0.2418 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.69 | 0.4215 | 0.2400 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.83 | 0.5569 | 0.1191 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.37 | 0.5299 | 0.1301 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.37 | 0.5299 | 0.1301 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.15 | 0.5255 | 0.1309 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.15 | 0.5255 | 0.1309 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.30 | 0.2931 | 0.1664 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.98 | 0.2401 | 0.1814 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.98 | 0.2401 | 0.1814 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.93 | 0.2376 | 0.1822 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.93 | 0.2376 | 0.1822 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.88 | 0.2110 | 0.1840 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.46 | 0.4650 | 0.2083 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.70 | 0.4875 | 0.1958 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.52 | 0.4832 | 0.2035 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.59 | 0.4849 | 0.2003 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.46 | 0.4821 | 0.2027 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.76 | 0.5210 | 0.1877 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.55 | 0.5128 | 0.1965 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.62 | 0.5170 | 0.1931 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.74 | 0.3399 | 0.1579 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.42 | 0.4049 | 0.2380 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.59 | 0.4235 | 0.2296 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.47 | 0.4182 | 0.2350 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.52 | 0.4210 | 0.2325 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.71 | 0.3546 | 0.2115 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.78 | 0.3632 | 0.2055 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.71 | 0.3619 | 0.2097 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.74 | 0.3627 | 0.2078 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.84 | 0.7868 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.05 | 0.7901 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.93 | 0.7883 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.92 | 0.7891 | 0.0184 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.64 | 0.7953 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.78 | 0.7966 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.81 | 0.7968 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.84 | 0.7969 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.60 | 0.7940 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.89 | 0.7886 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.87 | 0.7883 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.11 | 0.7902 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.06 | 0.7896 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.50 | 0.7938 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.67 | 0.7878 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.62 | 0.7871 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.80 | 0.7894 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.80 | 0.7893 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.83 | 0.7863 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.74 | 0.7747 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.00 | 0.7802 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.89 | 0.7780 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.90 | 0.7789 | 0.0207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.52 | 0.7799 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.25 | 0.7901 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.96 | 0.7859 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.07 | 0.7876 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.31 | 0.7775 | 0.0203 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.34 | 0.7908 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.62 | 0.7935 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.51 | 0.7922 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.58 | 0.7931 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.56 | 0.7931 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.70 | 0.7950 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.68 | 0.7940 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.74 | 0.7946 | 0.0176 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.17 | 0.7693 | 0.0238 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.59 | 0.7739 | 0.0222 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.44 | 0.7729 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.46 | 0.7732 | 0.0227 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.23 | 0.7847 | 0.0201 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.47 | 0.7872 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.66 | 0.7895 | 0.0190 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.68 | 0.7889 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.22 | 0.7878 | 0.0196 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.06 | 0.7757 | 0.0228 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.13 | 0.7786 | 0.0207 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.47 | 0.7741 | 0.0228 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.51 | 0.7770 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.14 | 0.7892 | 0.0181 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.02 | 0.7751 | 0.0215 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.04 | 0.7768 | 0.0198 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.36 | 0.7741 | 0.0218 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.43 | 0.7764 | 0.0206 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.81 | 0.7663 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.22 | 0.7307 | 0.0315 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.50 | 0.7426 | 0.0287 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.42 | 0.7404 | 0.0299 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.41 | 0.7412 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.01 | 0.7390 | 0.0284 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.96 | 0.7632 | 0.0240 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.82 | 0.7569 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.96 | 0.7602 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.55 | 0.7181 | 0.0403 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.84 | 0.7745 | 0.0259 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.11 | 0.7804 | 0.0262 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.20 | 0.7803 | 0.0259 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.28 | 0.7815 | 0.0255 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.34 | 0.7800 | 0.0237 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.02 | 0.7811 | 0.0259 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.43 | 0.7836 | 0.0243 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.30 | 0.7834 | 0.0250 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 40.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.74 | 0.7429 | 0.0256 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.04 | 0.3157 | 0.3961 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.09 | 0.3260 | 0.3895 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.06 | 0.3222 | 0.3939 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.07 | 0.3238 | 0.3920 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.02 | 0.3323 | 0.3931 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.06 | 0.3375 | 0.3874 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.03 | 0.3386 | 0.3908 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.04 | 0.3379 | 0.3896 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.85 | 0.5227 | 0.1927 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.66 | 0.5066 | 0.2010 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.66 | 0.5066 | 0.2010 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.64 | 0.5041 | 0.2021 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.64 | 0.5041 | 0.2021 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.83 | 0.1970 | 0.2449 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.81 | 0.1848 | 0.2502 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.81 | 0.1848 | 0.2502 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.81 | 0.1831 | 0.2521 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.81 | 0.1831 | 0.2521 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.78 | 0.1778 | 0.2503 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.31 | 0.3875 | 0.3551 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.39 | 0.4008 | 0.3434 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.33 | 0.3990 | 0.3508 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.36 | 0.4000 | 0.3477 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.35 | 0.4044 | 0.3480 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.44 | 0.4269 | 0.3348 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.36 | 0.4215 | 0.3431 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.39 | 0.4244 | 0.3396 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.60 | 0.3220 | 0.2168 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.09 | 0.3291 | 0.3899 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.18 | 0.3388 | 0.3829 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.12 | 0.3354 | 0.3875 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.14 | 0.3368 | 0.3856 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.75 | 0.2954 | 0.3332 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.64 | 0.2989 | 0.3300 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.70 | 0.2980 | 0.3333 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.67 | 0.2980 | 0.3321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.34 | 0.7399 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.48 | 0.7415 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.44 | 0.7408 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.44 | 0.7412 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.68 | 0.7432 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.76 | 0.7438 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.77 | 0.7438 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.77 | 0.7438 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.68 | 0.7434 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.22 | 0.7405 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.22 | 0.7404 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.32 | 0.7409 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.29 | 0.7407 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.61 | 0.7432 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.10 | 0.7405 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.08 | 0.7402 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.16 | 0.7410 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.16 | 0.7409 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.31 | 0.7410 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.84 | 0.7345 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.05 | 0.7376 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.00 | 0.7363 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.01 | 0.7368 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.97 | 0.7359 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.39 | 0.7413 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.26 | 0.7394 | 0.0277 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.30 | 0.7403 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.08 | 0.7373 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.55 | 0.7412 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.70 | 0.7428 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.64 | 0.7419 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.68 | 0.7424 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.66 | 0.7421 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.75 | 0.7437 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.71 | 0.7426 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.74 | 0.7431 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.73 | 0.7330 | 0.0304 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.96 | 0.7360 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.89 | 0.7349 | 0.0299 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.90 | 0.7354 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.32 | 0.7401 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.47 | 0.7412 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.52 | 0.7419 | 0.0269 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.51 | 0.7416 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.61 | 0.7423 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.94 | 0.7371 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.99 | 0.7379 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.96 | 0.7366 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.00 | 0.7375 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.52 | 0.7425 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.85 | 0.7375 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.87 | 0.7377 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.84 | 0.7372 | 0.0286 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.88 | 0.7375 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.04 | 0.7366 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.10 | 0.7113 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.59 | 0.7195 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.41 | 0.7175 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.47 | 0.7186 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.60 | 0.7180 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.45 | 0.7314 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.19 | 0.7268 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.24 | 0.7293 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.34 | 0.7243 | 0.0339 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.77 | 0.7341 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.20 | 0.7394 | 0.0301 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.06 | 0.7373 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.14 | 0.7385 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.29 | 0.7381 | 0.0299 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.35 | 0.7417 | 0.0299 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.29 | 0.7399 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.30 | 0.7408 | 0.0304 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 81.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.73 | 0.7129 | 0.0371 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.32 | 0.2812 | 0.4226 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.35 | 0.2837 | 0.4173 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.32 | 0.2838 | 0.4208 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.33 | 0.2838 | 0.4191 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.30 | 0.2828 | 0.4209 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.32 | 0.2841 | 0.4160 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.30 | 0.2860 | 0.4189 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.31 | 0.2851 | 0.4176 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.86 | 0.4848 | 0.2827 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.78 | 0.4808 | 0.2869 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.78 | 0.4808 | 0.2869 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.76 | 0.4794 | 0.2879 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.76 | 0.4794 | 0.2879 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.99 | 0.1044 | 0.3105 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.00 | 0.1043 | 0.3128 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.00 | 0.1043 | 0.3128 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.00 | 0.1030 | 0.3135 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.00 | 0.1030 | 0.3135 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.98 | 0.1008 | 0.3123 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.99 | 0.3267 | 0.3839 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.04 | 0.3315 | 0.3744 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.01 | 0.3325 | 0.3800 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.02 | 0.3322 | 0.3773 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.02 | 0.3322 | 0.3781 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.05 | 0.3367 | 0.3672 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.02 | 0.3380 | 0.3741 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.03 | 0.3375 | 0.3711 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.98 | 0.1978 | 0.2772 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.25 | 0.2774 | 0.4197 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.29 | 0.2796 | 0.4150 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.26 | 0.2792 | 0.4181 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.27 | 0.2792 | 0.4167 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.62 | 0.2174 | 0.3802 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.58 | 0.2174 | 0.3777 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.61 | 0.2184 | 0.3799 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.59 | 0.2179 | 0.3793 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.74 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.74 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.74 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.74 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.74 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.74 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.71 | 0.7127 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.71 | 0.7128 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.72 | 0.7128 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.71 | 0.7128 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.72 | 0.7127 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.73 | 0.7129 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.73 | 0.7128 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.73 | 0.7128 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.72 | 0.7128 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7129 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.72 | 0.7128 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.73 | 0.7128 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.65 | 0.7124 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.68 | 0.7125 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.68 | 0.7126 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.68 | 0.7125 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.69 | 0.7129 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7129 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.72 | 0.7131 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.71 | 0.7130 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.74 | 0.7131 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.72 | 0.7128 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.73 | 0.7129 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.67 | 0.7126 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.68 | 0.7126 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.73 | 0.7131 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.72 | 0.7129 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.73 | 0.7129 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.68 | 0.7127 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.68 | 0.7126 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.71 | 0.7130 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.16 | 0.7090 | 0.0415 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.29 | 0.7099 | 0.0409 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.25 | 0.7101 | 0.0412 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.29 | 0.7101 | 0.0411 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.36 | 0.7106 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.54 | 0.7123 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.51 | 0.7120 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.51 | 0.7122 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.60 | 0.7126 | 0.0390 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.67 | 0.7123 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.69 | 0.7127 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.69 | 0.7127 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.69 | 0.7127 | 0.0381 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.67 | 0.7126 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.69 | 0.7131 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.68 | 0.7130 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.69 | 0.7131 | 0.0383 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.74 | 0.7243 | 0.0512 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.63 | 0.2854 | 0.4939 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.67 | 0.2912 | 0.4852 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.64 | 0.2896 | 0.4908 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.65 | 0.2903 | 0.4882 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.61 | 0.2941 | 0.4874 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.64 | 0.2971 | 0.4805 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.62 | 0.2985 | 0.4851 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.63 | 0.2978 | 0.4831 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.01 | 0.4820 | 0.3775 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.89 | 0.4727 | 0.3869 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.89 | 0.4727 | 0.3869 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.84 | 0.4701 | 0.3884 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.84 | 0.4701 | 0.3884 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.03 | 0.1367 | 0.4035 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.02 | 0.1309 | 0.4090 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.02 | 0.1309 | 0.4090 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.01 | 0.1289 | 0.4110 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.01 | 0.1289 | 0.4110 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.00 | 0.1261 | 0.4097 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.43 | 0.3389 | 0.4482 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.49 | 0.3476 | 0.4319 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.45 | 0.3469 | 0.4424 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.47 | 0.3474 | 0.4376 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.46 | 0.3486 | 0.4359 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.50 | 0.3607 | 0.4177 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.46 | 0.3588 | 0.4292 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.47 | 0.3600 | 0.4241 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.14 | 0.2317 | 0.3558 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.52 | 0.2826 | 0.4879 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.57 | 0.2881 | 0.4793 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.53 | 0.2863 | 0.4850 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.55 | 0.2871 | 0.4827 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.76 | 0.2284 | 0.4528 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.73 | 0.2298 | 0.4486 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.74 | 0.2297 | 0.4525 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.74 | 0.2295 | 0.4512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.39 | 0.7225 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.47 | 0.7233 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.43 | 0.7229 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.42 | 0.7231 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.70 | 0.7244 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.75 | 0.7247 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.76 | 0.7248 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.77 | 0.7248 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.64 | 0.7242 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.30 | 0.7227 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.30 | 0.7226 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.38 | 0.7230 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.37 | 0.7229 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.61 | 0.7242 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.19 | 0.7226 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.19 | 0.7225 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.25 | 0.7229 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.24 | 0.7229 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.34 | 0.7229 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.00 | 0.7195 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.13 | 0.7209 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.08 | 0.7203 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.09 | 0.7206 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.29 | 0.7208 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.57 | 0.7236 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.46 | 0.7224 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.51 | 0.7230 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.20 | 0.7212 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.57 | 0.7233 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.69 | 0.7241 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.64 | 0.7237 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.67 | 0.7239 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.67 | 0.7238 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.73 | 0.7246 | 0.0517 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.70 | 0.7240 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.73 | 0.7243 | 0.0516 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.92 | 0.7187 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.12 | 0.7202 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.04 | 0.7197 | 0.0564 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.04 | 0.7199 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.48 | 0.7228 | 0.0538 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.60 | 0.7235 | 0.0524 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.62 | 0.7238 | 0.0528 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.62 | 0.7237 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.58 | 0.7236 | 0.0526 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.12 | 0.7210 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.14 | 0.7213 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.85 | 0.7199 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.86 | 0.7202 | 0.0546 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.54 | 0.7237 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.03 | 0.7210 | 0.0540 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.05 | 0.7212 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.78 | 0.7200 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.79 | 0.7201 | 0.0538 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.16 | 0.7209 | 0.0546 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.86 | 0.7075 | 0.0661 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.18 | 0.7113 | 0.0620 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.04 | 0.7104 | 0.0637 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.09 | 0.7109 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.42 | 0.7116 | 0.0615 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.02 | 0.7186 | 0.0568 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.82 | 0.7163 | 0.0596 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.90 | 0.7176 | 0.0585 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.77 | 0.7154 | 0.0605 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.12 | 0.7197 | 0.0581 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.40 | 0.7223 | 0.0563 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.31 | 0.7214 | 0.0574 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.36 | 0.7219 | 0.0567 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.45 | 0.7219 | 0.0560 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.48 | 0.7235 | 0.0561 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.43 | 0.7226 | 0.0567 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.46 | 0.7231 | 0.0566 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 250204 | 0.326 | 70.2 | 28.86 | 0.22 | 0.034 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 250204 | 0.326 | 51.7 | 28.86 | 0.22 | 0.034 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 250204 | 0.326 | 59.5 | 28.86 | 0.22 | 0.034 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 250204 | 0.326 | 63.7 | 28.86 | 0.22 | 0.034 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 667 | None | classic | 0.50 | False | 449316 | 0.994 | 200.4 | 26.35 | 0.12 | 0.010 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 667 | None | classic | 0.50 | False | 449316 | 0.994 | 196.7 | 26.35 | 0.12 | 0.010 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 667 | None | classic | 0.50 | False | 449316 | 0.994 | 188.4 | 26.35 | 0.12 | 0.010 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 667 | None | classic | 0.50 | False | 449316 | 0.994 | 172.9 | 26.35 | 0.12 | 0.010 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 664873 | 0.145 | 31.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 664873 | 0.812 | 36.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 664873 | 0.812 | 36.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 664873 | 0.541 | 31.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 664873 | 0.541 | 31.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 664873 | 0.145 | 39.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 664873 | 0.812 | 183.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 664873 | 0.812 | 183.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 664873 | 0.541 | 39.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 664873 | 0.541 | 39.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 662543 | 0.812 | 449.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 243249 | 0.330 | 62.5 | 28.71 | 0.15 | 0.034 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 243249 | 0.330 | 73.7 | 28.71 | 0.15 | 0.034 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 243249 | 0.330 | 47.8 | 28.71 | 0.15 | 0.034 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 243249 | 0.330 | 67.2 | 28.71 | 0.15 | 0.034 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 875 | None | classic | 0.50 | False | 458494 | 1.000 | 210.6 | 26.98 | 0.08 | 0.012 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 875 | None | classic | 0.50 | False | 458494 | 1.000 | 197.2 | 26.98 | 0.08 | 0.012 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 875 | None | classic | 0.50 | False | 458494 | 1.000 | 187.1 | 26.98 | 0.08 | 0.012 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 875 | None | classic | 0.50 | False | 458494 | 1.000 | 191.7 | 26.98 | 0.08 | 0.012 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1307470 | 0.812 | 98.7 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 251729 | 0.928 | 80.6 | 30.03 | 0.30 | 0.028 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 251729 | 0.928 | 73.7 | 30.03 | 0.30 | 0.028 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 251729 | 0.928 | 76.3 | 30.03 | 0.30 | 0.028 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 251729 | 0.928 | 55.0 | 30.03 | 0.30 | 0.028 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 683 | None | classic | 0.30 | False | 404678 | 0.981 | 158.7 | 25.73 | 0.11 | 0.018 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 683 | None | classic | 0.30 | False | 404678 | 0.981 | 135.9 | 25.73 | 0.11 | 0.018 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 683 | None | classic | 0.30 | False | 404678 | 0.981 | 144.0 | 25.73 | 0.11 | 0.018 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 683 | None | classic | 0.30 | False | 404678 | 0.981 | 171.5 | 25.73 | 0.11 | 0.018 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.581 | 0.011 |
| in035 | mask_ent | 0.755 | 0.011 |
| in035 | mask_grad | 0.431 | 0.011 |
| in035 | r_col | 0.687 | 0.011 |
| in035 | r_warp | 0.857 | 0.011 |

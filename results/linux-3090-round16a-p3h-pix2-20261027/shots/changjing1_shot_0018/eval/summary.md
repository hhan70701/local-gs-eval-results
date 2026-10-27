# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 7.1% | 23.85 / 0.0088 | 19.71 / 0.0239 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.5% | 23.94 / 0.0094 | 21.40 / 0.0185 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.4% | 23.91 / 0.0090 | 20.75 / 0.0202 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.4% | 23.91 / 0.0092 | 21.07 / 0.0192 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.2% | 23.71 / 0.0099 | 20.21 / 0.0223 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.7% | 23.79 / 0.0101 | 21.32 / 0.0173 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.5% | 23.77 / 0.0098 | 20.98 / 0.0188 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.5% | 23.77 / 0.0098 | 21.17 / 0.0172 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 6.6% | 23.31 / 0.0100 | 21.32 / 0.0239 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 6.0% | 23.03 / 0.0089 | 19.86 / 0.0250 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.1% | 20.13 / 0.0068 | 16.01 / 0.0185 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 6.0% | 23.16 / 0.0094 | 20.08 / 0.0274 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.2% | 20.26 / 0.0075 | 16.55 / 0.0218 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 6.6% | 23.32 / 0.0100 | 21.44 / 0.0181 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 6.0% | 23.06 / 0.0089 | 19.74 / 0.0239 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.2% | 20.21 / 0.0061 | 16.17 / 0.0181 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 6.1% | 23.33 / 0.0096 | 20.07 / 0.0250 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.5% | 20.74 / 0.0075 | 17.06 / 0.0209 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 8.0% | 23.89 / 0.0102 | 19.26 / 0.0370 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 13.2% | 24.52 / 0.0129 | 20.23 / 0.0388 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 13.8% | 24.58 / 0.0133 | 22.24 / 0.0268 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 13.7% | 24.58 / 0.0132 | 21.32 / 0.0329 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 13.7% | 24.56 / 0.0132 | 21.81 / 0.0296 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 13.1% | 24.50 / 0.0127 | 20.18 / 0.0360 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.1% | 24.64 / 0.0134 | 21.98 / 0.0274 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 13.7% | 24.60 / 0.0131 | 21.37 / 0.0319 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 13.9% | 24.63 / 0.0131 | 21.72 / 0.0288 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 14.2% | 24.56 / 0.0136 | 19.54 / 0.0525 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 4.6% | 23.14 / 0.0060 | 18.86 / 0.0197 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 6.2% | 24.02 / 0.0076 | 20.70 / 0.0241 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 5.1% | 23.37 / 0.0062 | 20.32 / 0.0183 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 5.6% | 23.76 / 0.0072 | 20.79 / 0.0205 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 5.8% | 23.92 / 0.0068 | 19.68 / 0.0209 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 6.8% | 24.32 / 0.0072 | 20.73 / 0.0213 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 6.0% | 24.02 / 0.0068 | 19.97 / 0.0204 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 6.2% | 24.09 / 0.0068 | 20.19 / 0.0198 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.69 / 0.0527 | 24.90 / 0.0535 | 20.05 / 0.0133 | 29.90 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.69 / 0.0645 | 24.12 / 0.0841 | 18.99 / 0.0162 | 29.76 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.28 / 0.0591 | 24.82 / 0.0650 | 19.65 / 0.0139 | 29.85 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.03 / 0.0617 | 24.38 / 0.0747 | 19.35 / 0.0145 | 29.82 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.16 / 0.0603 | 24.67 / 0.0685 | 19.50 / 0.0141 | 29.84 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.94 / 0.0623 | 24.11 / 0.0808 | 19.37 / 0.0165 | 29.74 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.29 / 0.0580 | 24.71 / 0.0656 | 19.87 / 0.0137 | 29.79 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.11 / 0.0601 | 24.50 / 0.0748 | 19.59 / 0.0148 | 29.79 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.21 / 0.0587 | 24.66 / 0.0698 | 19.73 / 0.0140 | 29.80 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.35 / 0.0611 | 24.68 / 0.0693 | 19.60 / 0.0191 | 29.91 / 0.0358 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.98 / 0.0608 | 25.04 / 0.0682 | 19.82 / 0.0176 | 29.73 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.97 / 0.0579 | 24.97 / 0.0647 | 19.72 / 0.0167 | 29.71 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.14 / 0.0624 | 24.83 / 0.0705 | 19.74 / 0.0182 | 29.80 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.16 / 0.0595 | 24.81 / 0.0649 | 19.68 / 0.0170 | 29.79 / 0.0364 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.38 / 0.0573 | 24.56 / 0.0677 | 19.72 / 0.0161 | 29.89 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.92 / 0.0599 | 24.78 / 0.0690 | 19.68 / 0.0173 | 29.71 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.96 / 0.0581 | 24.84 / 0.0652 | 19.66 / 0.0167 | 29.72 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.07 / 0.0613 | 24.53 / 0.0724 | 19.60 / 0.0178 | 29.78 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.11 / 0.0596 | 24.59 / 0.0682 | 19.61 / 0.0173 | 29.79 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.64 / 0.0635 | 23.63 / 0.1000 | 19.26 / 0.0186 | 29.58 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.25 / 0.0744 | 23.28 / 0.1227 | 18.78 / 0.0186 | 29.37 / 0.0415 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.13 / 0.0642 | 24.80 / 0.0818 | 19.76 / 0.0148 | 29.74 / 0.0387 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.73 / 0.0695 | 24.02 / 0.1050 | 19.27 / 0.0164 | 29.65 / 0.0399 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.94 / 0.0664 | 24.53 / 0.0916 | 19.52 / 0.0154 | 29.71 / 0.0392 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.16 / 0.0731 | 23.26 / 0.1206 | 18.82 / 0.0192 | 29.35 / 0.0415 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.94 / 0.0645 | 24.50 / 0.0856 | 19.77 / 0.0159 | 29.55 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.65 / 0.0695 | 23.90 / 0.1051 | 19.42 / 0.0174 | 29.54 / 0.0405 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.79 / 0.0667 | 24.32 / 0.0942 | 19.57 / 0.0164 | 29.54 / 0.0399 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.08 / 0.0697 | 22.98 / 0.1233 | 19.29 / 0.0198 | 29.19 / 0.0406 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.86 / 0.0630 | 23.84 / 0.0846 | 19.20 / 0.0158 | 29.58 / 0.0374 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.99 / 0.0651 | 24.46 / 0.0709 | 19.83 / 0.0148 | 28.94 / 0.0411 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.18 / 0.0618 | 24.26 / 0.0779 | 19.67 / 0.0149 | 29.67 / 0.0372 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.14 / 0.0634 | 24.32 / 0.0743 | 19.67 / 0.0148 | 29.50 / 0.0393 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.95 / 0.0628 | 23.67 / 0.0865 | 19.55 / 0.0148 | 29.48 / 0.0386 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.25 / 0.0605 | 24.41 / 0.0683 | 20.03 / 0.0138 | 29.57 / 0.0378 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.01 / 0.0622 | 24.06 / 0.0776 | 19.75 / 0.0144 | 29.52 / 0.0383 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.10 / 0.0618 | 24.23 / 0.0719 | 19.87 / 0.0142 | 29.55 / 0.0380 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 7.2%） | — | — | 27.69 / 0.0527 | 24.90 / 0.0535 | 29.90 |
| in035 | rife | 2.2% | 4.6% | 26.86 / 0.0630 | 23.84 / 0.0846 | 29.58 |
| in035 | cnw_cnn | 4.9% | 7.1% | 26.69 / 0.0645 | 24.12 / 0.0841 | 29.76 |
| in035 | cnw_f5 | 7.7% | 13.2% | 26.25 / 0.0744 | 23.28 / 0.1227 | 29.37 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.83 / 0.0538 | -0.76 / +0.0121 (core 1.5%) | -0.99 / +0.0131 (core 3.8%) | -1.31 / +0.0233 (core 7.8%) |
| in035 | 2 | 0-3 | 27.52 / 0.0518 | -1.20 / +0.0122 (core 1.5%) | -1.30 / +0.0138 (core 3.8%) | -1.81 / +0.0287 (core 7.8%) |
| in035 | 4 | 3-5 | 28.73 / 0.0526 | -0.55 / +0.0066 (core 1.8%) | -0.71 / +0.0085 (core 4.0%) | -1.23 / +0.0131 (core 5.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.69 / 0.0527 | 24.90 | 29.90 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.69 / 0.0645 | 24.12 | 29.76 | 0/3 |
| in035 | cnw_cnn | oracle | 1.5% | 27.05 / 0.0569 | 24.56 | 29.89 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.28 / 0.0591 | 24.82 | 29.85 | 0/3 |
| in035 | cnw_cnn | oracle | 1.5% | 27.46 / 0.0542 | 25.02 | 29.90 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.03 / 0.0617 | 24.38 | 29.82 | 0/3 |
| in035 | cnw_cnn | oracle | 1.5% | 27.29 / 0.0552 | 24.79 | 29.90 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.16 / 0.0603 | 24.67 | 29.84 | 0/3 |
| in035 | cnw_cnn | oracle | 1.5% | 27.37 / 0.0546 | 24.93 | 29.90 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.94 / 0.0623 | 24.11 | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.5% | 27.31 / 0.0564 | 24.70 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.29 / 0.0580 | 24.71 | 29.79 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.6% | 27.57 / 0.0535 | 25.15 | 29.90 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.11 / 0.0601 | 24.50 | 29.79 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.5% | 27.42 / 0.0549 | 25.02 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.21 / 0.0587 | 24.66 | 29.80 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.6% | 27.50 / 0.0539 | 25.12 | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 27.35 / 0.0611 | 24.68 | 29.91 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 1.5% | 27.44 / 0.0587 | 24.83 | 29.90 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 26.98 / 0.0608 | 25.04 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 1.5% | 27.43 / 0.0572 | 25.39 | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 26.97 / 0.0579 | 24.97 | 29.71 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 0.9% | 27.39 / 0.0561 | 25.20 | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.14 / 0.0624 | 24.83 | 29.80 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 1.5% | 27.46 / 0.0579 | 25.16 | 29.90 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.16 / 0.0595 | 24.81 | 29.79 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 0.9% | 27.44 / 0.0566 | 24.99 | 29.89 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.38 / 0.0573 | 24.56 | 29.89 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 1.5% | 27.49 / 0.0556 | 24.78 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 26.92 / 0.0599 | 24.78 | 29.71 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.4% | 27.38 / 0.0565 | 25.16 | 29.89 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.96 / 0.0581 | 24.84 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.9% | 27.37 / 0.0559 | 25.09 | 29.89 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.07 / 0.0613 | 24.53 | 29.78 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 1.4% | 27.40 / 0.0573 | 24.90 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.11 / 0.0596 | 24.59 | 29.79 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 1.0% | 27.40 / 0.0567 | 24.83 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.64 / 0.0635 | 23.63 | 29.58 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.7% | 27.20 / 0.0577 | 24.55 | 29.88 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.25 / 0.0744 | 23.28 | 29.37 | 0/3 |
| in035 | cnw_f5 | oracle | 2.5% | 26.92 / 0.0605 | 24.13 | 29.82 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.13 / 0.0642 | 24.80 | 29.74 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 27.49 / 0.0556 | 25.14 | 29.89 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.73 / 0.0695 | 24.02 | 29.65 | 0/3 |
| in035 | cnw_f5 | oracle | 2.5% | 27.22 / 0.0582 | 24.67 | 29.86 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.94 / 0.0664 | 24.53 | 29.71 | 0/3 |
| in035 | cnw_f5 | oracle | 2.5% | 27.35 / 0.0567 | 24.96 | 29.88 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.16 / 0.0731 | 23.26 | 29.35 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.5% | 26.88 / 0.0602 | 24.12 | 29.82 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.94 / 0.0645 | 24.50 | 29.55 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.6% | 27.43 / 0.0561 | 25.13 | 29.86 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.65 / 0.0695 | 23.90 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.5% | 27.24 / 0.0584 | 24.76 | 29.85 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.79 / 0.0667 | 24.32 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.5% | 27.32 / 0.0570 | 25.00 | 29.85 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.08 / 0.0697 | 22.98 | 29.19 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.7% | 27.11 / 0.0591 | 24.26 | 29.75 | 0/3 |
| in035 | rife | 不复核 | —% | 26.86 / 0.0630 | 23.84 | 29.58 | 0/3 |
| in035 | rife | oracle | 1.0% | 27.22 / 0.0562 | 24.39 | 29.85 | 0/3 |
| in035 | rife | 不复核 | —% | 26.99 / 0.0651 | 24.46 | 28.94 | 0/3 |
| in035 | rife | oracle | 1.2% | 27.53 / 0.0547 | 24.74 | 29.85 | 0/3 |
| in035 | rife | 不复核 | —% | 27.18 / 0.0618 | 24.26 | 29.67 | 0/3 |
| in035 | rife | oracle | 1.1% | 27.46 / 0.0551 | 24.66 | 29.86 | 0/3 |
| in035 | rife | 不复核 | —% | 27.14 / 0.0634 | 24.32 | 29.50 | 0/3 |
| in035 | rife | oracle | 1.1% | 27.47 / 0.0547 | 24.64 | 29.86 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.95 / 0.0628 | 23.67 | 29.48 | 0/3 |
| in035 | rife_mw | oracle | 1.0% | 27.37 / 0.0548 | 24.63 | 29.85 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.25 / 0.0605 | 24.41 | 29.57 | 0/3 |
| in035 | rife_mw | oracle | 1.1% | 27.59 / 0.0537 | 25.04 | 29.85 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.01 / 0.0622 | 24.06 | 29.52 | 0/3 |
| in035 | rife_mw | oracle | 1.1% | 27.46 / 0.0543 | 24.86 | 29.86 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.10 / 0.0618 | 24.23 | 29.55 | 0/3 |
| in035 | rife_mw | oracle | 1.1% | 27.52 / 0.0541 | 24.96 | 29.86 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.69 / 0.0527 | 24.90 / 0.0535 | — |
| in035 | FF | 0（前馈） | 980×647（59%） | 27.06 | 26.69 / 0.0645 | 24.12 / 0.0841 | 0/3 |
| in035 | 25 | 1.35 s | 980×647（59%） | 27.90 | 27.03 / 0.0617 | 24.38 / 0.0747 | 0/3 |
| in035 | 50 | 2.70 s | 980×647（59%） | 28.28 | 27.16 / 0.0603 | 24.67 / 0.0685 | 0/3 |
| in035 | 100 | 5.42 s | 980×647（59%） | 28.60 | 27.28 / 0.0591 | 24.82 / 0.0650 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.69 / 0.0527 | 24.90 / 0.0535 | 29.90 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.69 / 0.0645 | 24.12 / 0.0841 | 29.76 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.05 / 0.0569 | 24.56 / 0.0663 | 29.89 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.03 / 0.0617 | 24.38 / 0.0747 | 29.82 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.29 / 0.0552 | 24.79 / 0.0612 | 29.90 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.16 / 0.0603 | 24.67 / 0.0685 | 29.84 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.37 / 0.0546 | 24.93 / 0.0580 | 29.90 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.28 / 0.0591 | 24.82 / 0.0650 | 29.85 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.46 / 0.0542 | 25.02 / 0.0561 | 29.90 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 26.94 / 0.0623 | 24.11 / 0.0808 | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.31 / 0.0564 | 24.70 / 0.0619 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.11 / 0.0601 | 24.50 / 0.0748 | 29.79 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.42 / 0.0549 | 25.02 / 0.0587 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.21 / 0.0587 | 24.66 / 0.0698 | 29.80 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.50 / 0.0539 | 25.12 / 0.0559 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.29 / 0.0580 | 24.71 / 0.0656 | 29.79 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.57 / 0.0535 | 25.15 / 0.0535 | 29.90 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.25 / 0.0744 | 23.28 / 0.1227 | 29.37 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 26.92 / 0.0605 | 24.13 / 0.0849 | 29.82 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.73 / 0.0695 | 24.02 / 0.1050 | 29.65 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.22 / 0.0582 | 24.67 / 0.0778 | 29.86 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.94 / 0.0664 | 24.53 / 0.0916 | 29.71 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.35 / 0.0567 | 24.96 / 0.0707 | 29.88 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.13 / 0.0642 | 24.80 / 0.0818 | 29.74 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.49 / 0.0556 | 25.14 / 0.0654 | 29.89 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.16 / 0.0731 | 23.26 / 0.1206 | 29.35 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 26.88 / 0.0602 | 24.12 / 0.0859 | 29.82 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.65 / 0.0695 | 23.90 / 0.1051 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.24 / 0.0584 | 24.76 / 0.0778 | 29.85 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.79 / 0.0667 | 24.32 / 0.0942 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.32 / 0.0570 | 25.00 / 0.0710 | 29.85 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 26.94 / 0.0645 | 24.50 / 0.0856 | 29.55 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.43 / 0.0561 | 25.13 / 0.0657 | 29.86 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.86 / 0.0630 | 23.84 / 0.0846 | 29.58 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.22 / 0.0562 | 24.39 / 0.0657 | 29.85 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.18 / 0.0618 | 24.26 / 0.0779 | 29.67 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.46 / 0.0551 | 24.66 / 0.0625 | 29.86 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.14 / 0.0634 | 24.32 / 0.0743 | 29.50 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.47 / 0.0547 | 24.64 / 0.0610 | 29.86 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.99 / 0.0651 | 24.46 / 0.0709 | 28.94 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.53 / 0.0547 | 24.74 / 0.0595 | 29.85 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.95 / 0.0628 | 23.67 / 0.0865 | 29.48 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.37 / 0.0548 | 24.63 / 0.0621 | 29.85 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.01 / 0.0622 | 24.06 / 0.0776 | 29.52 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.46 / 0.0543 | 24.86 / 0.0602 | 29.86 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.10 / 0.0618 | 24.23 / 0.0719 | 29.55 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.52 / 0.0541 | 24.96 / 0.0582 | 29.86 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.25 / 0.0605 | 24.41 / 0.0683 | 29.57 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.59 / 0.0537 | 25.04 / 0.0564 | 29.85 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.90 / 0.0535 | 20.05 / 0.0133 | 29.90 / 0.0355 | 27.69 / 0.0527 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 12.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.90 | 0.8138 | 0.0535 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 10.49 | 0.4790 | 0.4041 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.25 | 0.5638 | 0.3382 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 10.85 | 0.5297 | 0.3728 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.05 | 0.5500 | 0.3528 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.79 | 0.4628 | 0.3808 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.60 | 0.5258 | 0.3276 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.23 | 0.5035 | 0.3568 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.42 | 0.5160 | 0.3410 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 19.42 | 0.6705 | 0.2504 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 19.11 | 0.6604 | 0.2436 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 19.11 | 0.6604 | 0.2436 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 18.99 | 0.6517 | 0.2503 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 18.99 | 0.6517 | 0.2503 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 10.68 | 0.5076 | 0.3373 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.03 | 0.5086 | 0.3503 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.03 | 0.5086 | 0.3503 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 10.99 | 0.4972 | 0.3603 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 10.99 | 0.4972 | 0.3603 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.65 | 0.4665 | 0.3625 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 11.76 | 0.5363 | 0.3320 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.37 | 0.6552 | 0.2523 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.06 | 0.6060 | 0.2964 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.21 | 0.6353 | 0.2720 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 11.89 | 0.5378 | 0.3159 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 12.46 | 0.6288 | 0.2472 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 12.19 | 0.5939 | 0.2831 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 12.32 | 0.6152 | 0.2640 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.04 | 0.5869 | 0.2787 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.07 | 0.4210 | 0.4776 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.37 | 0.4779 | 0.4311 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.23 | 0.4538 | 0.4612 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.29 | 0.4677 | 0.4485 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 8.12 | 0.4191 | 0.4506 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.40 | 0.4683 | 0.4102 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 8.16 | 0.4497 | 0.4356 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.23 | 0.4605 | 0.4246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.56 | 0.8087 | 0.0663 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.02 | 0.8195 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.79 | 0.8140 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.93 | 0.8173 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.70 | 0.8059 | 0.0619 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.15 | 0.8155 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.02 | 0.8121 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.12 | 0.8145 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.83 | 0.8115 | 0.0641 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.39 | 0.8219 | 0.0586 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.20 | 0.8172 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.16 | 0.8185 | 0.0605 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.99 | 0.8142 | 0.0599 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.78 | 0.8107 | 0.0619 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.16 | 0.8173 | 0.0592 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.09 | 0.8155 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.90 | 0.8132 | 0.0625 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.83 | 0.8119 | 0.0619 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.55 | 0.8121 | 0.0653 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.13 | 0.7925 | 0.0849 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.14 | 0.8204 | 0.0654 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.67 | 0.8083 | 0.0778 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.96 | 0.8152 | 0.0707 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.12 | 0.7944 | 0.0859 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.13 | 0.8183 | 0.0657 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.76 | 0.8075 | 0.0778 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.00 | 0.8138 | 0.0710 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.26 | 0.8115 | 0.0742 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.39 | 0.8046 | 0.0657 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.74 | 0.8126 | 0.0595 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.66 | 0.8089 | 0.0625 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.64 | 0.8107 | 0.0610 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 24.63 | 0.8052 | 0.0621 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.04 | 0.8149 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.86 | 0.8112 | 0.0602 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.96 | 0.8134 | 0.0582 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.12 | 0.7910 | 0.0841 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.82 | 0.8145 | 0.0650 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.38 | 0.8036 | 0.0747 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.67 | 0.8102 | 0.0685 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.11 | 0.7855 | 0.0808 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.71 | 0.8025 | 0.0656 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.50 | 0.7970 | 0.0748 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.66 | 0.8012 | 0.0698 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.68 | 0.8070 | 0.0693 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.04 | 0.8143 | 0.0682 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.97 | 0.8125 | 0.0647 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.83 | 0.8095 | 0.0705 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.81 | 0.8100 | 0.0649 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.56 | 0.8050 | 0.0677 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.78 | 0.8072 | 0.0690 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.84 | 0.8095 | 0.0652 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.53 | 0.8024 | 0.0724 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.59 | 0.8063 | 0.0682 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.63 | 0.7875 | 0.1000 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.28 | 0.7540 | 0.1227 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.80 | 0.8117 | 0.0818 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.02 | 0.7880 | 0.1050 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.53 | 0.8024 | 0.0916 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.26 | 0.7565 | 0.1206 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.50 | 0.8010 | 0.0856 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.90 | 0.7827 | 0.1051 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.32 | 0.7939 | 0.0942 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.98 | 0.7759 | 0.1233 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.84 | 0.7870 | 0.0846 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.46 | 0.8052 | 0.0709 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.26 | 0.7973 | 0.0779 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.32 | 0.8018 | 0.0743 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.67 | 0.7793 | 0.0865 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.41 | 0.8021 | 0.0683 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.06 | 0.7939 | 0.0776 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.23 | 0.7992 | 0.0719 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 7.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.05 | 0.6686 | 0.0133 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.15 | 0.3006 | 0.0940 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.57 | 0.3520 | 0.0875 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.33 | 0.3286 | 0.0911 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.44 | 0.3411 | 0.0895 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.05 | 0.2938 | 0.0950 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.20 | 0.3440 | 0.0898 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.11 | 0.3204 | 0.0922 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.16 | 0.3350 | 0.0907 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.87 | 0.4078 | 0.0548 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.83 | 0.4167 | 0.0548 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.83 | 0.4167 | 0.0548 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.76 | 0.4013 | 0.0557 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.76 | 0.4013 | 0.0557 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 10.73 | 0.3341 | 0.0657 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.82 | 0.3372 | 0.0684 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.82 | 0.3372 | 0.0684 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 10.80 | 0.3257 | 0.0690 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 10.80 | 0.3257 | 0.0690 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.59 | 0.3042 | 0.0704 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.49 | 0.3824 | 0.0789 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.95 | 0.4546 | 0.0712 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.70 | 0.4226 | 0.0753 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.83 | 0.4409 | 0.0732 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.56 | 0.3828 | 0.0788 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.65 | 0.4591 | 0.0721 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.64 | 0.4288 | 0.0753 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.63 | 0.4460 | 0.0741 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.19 | 0.4389 | 0.0555 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.09 | 0.2549 | 0.1167 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.37 | 0.3013 | 0.1113 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.25 | 0.2779 | 0.1143 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.33 | 0.2900 | 0.1129 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.06 | 0.2663 | 0.1136 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.22 | 0.2992 | 0.1104 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.11 | 0.2847 | 0.1128 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.16 | 0.2931 | 0.1117 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.01 | 0.6503 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.66 | 0.6661 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.37 | 0.6581 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.51 | 0.6623 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.44 | 0.6558 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.90 | 0.6762 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.64 | 0.6686 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.78 | 0.6737 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.60 | 0.6520 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.84 | 0.6716 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.74 | 0.6623 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.75 | 0.6622 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.69 | 0.6574 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.72 | 0.6532 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.70 | 0.6639 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.69 | 0.6602 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.61 | 0.6541 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.61 | 0.6545 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.27 | 0.6459 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.80 | 0.6339 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.78 | 0.6716 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.29 | 0.6552 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.53 | 0.6640 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.84 | 0.6381 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.79 | 0.6786 | 0.0159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.45 | 0.6625 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.60 | 0.6710 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.31 | 0.6499 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.21 | 0.6566 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.84 | 0.6719 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.68 | 0.6650 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.68 | 0.6684 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.57 | 0.6617 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.04 | 0.6785 | 0.0138 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.76 | 0.6705 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.88 | 0.6746 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.99 | 0.6490 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.65 | 0.6659 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.35 | 0.6583 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.50 | 0.6623 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.37 | 0.6538 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.87 | 0.6755 | 0.0137 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.59 | 0.6674 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.73 | 0.6728 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.60 | 0.6516 | 0.0191 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.82 | 0.6701 | 0.0176 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.72 | 0.6603 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.74 | 0.6616 | 0.0182 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.68 | 0.6569 | 0.0170 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.72 | 0.6525 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.68 | 0.6623 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.66 | 0.6583 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.60 | 0.6531 | 0.0178 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.61 | 0.6536 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.26 | 0.6436 | 0.0186 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.78 | 0.6312 | 0.0186 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.76 | 0.6709 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.27 | 0.6541 | 0.0164 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.52 | 0.6631 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.82 | 0.6353 | 0.0192 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.77 | 0.6768 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.42 | 0.6607 | 0.0174 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.57 | 0.6692 | 0.0164 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.29 | 0.6463 | 0.0198 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.20 | 0.6552 | 0.0158 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.83 | 0.6708 | 0.0148 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.67 | 0.6639 | 0.0149 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.67 | 0.6672 | 0.0148 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.55 | 0.6597 | 0.0148 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.03 | 0.6775 | 0.0138 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.75 | 0.6693 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.87 | 0.6735 | 0.0142 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 28.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.63 | 0.7701 | 0.0216 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.53 | 0.4482 | 0.2382 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.78 | 0.4814 | 0.2241 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.63 | 0.4723 | 0.2311 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.69 | 0.4766 | 0.2280 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.45 | 0.4452 | 0.2320 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.67 | 0.4737 | 0.2202 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.52 | 0.4721 | 0.2255 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.58 | 0.4752 | 0.2230 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.51 | 0.6057 | 0.1068 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.84 | 0.5743 | 0.1176 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.84 | 0.5743 | 0.1176 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.97 | 0.5717 | 0.1185 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.97 | 0.5717 | 0.1185 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.32 | 0.4155 | 0.1664 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.99 | 0.3564 | 0.1843 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.99 | 0.3564 | 0.1843 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.01 | 0.3554 | 0.1851 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.01 | 0.3554 | 0.1851 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.74 | 0.2926 | 0.1953 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.51 | 0.5028 | 0.1974 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.78 | 0.5468 | 0.1798 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.61 | 0.5322 | 0.1892 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.68 | 0.5397 | 0.1845 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.56 | 0.5044 | 0.1934 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.73 | 0.5443 | 0.1767 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.63 | 0.5351 | 0.1850 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.67 | 0.5411 | 0.1810 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.30 | 0.3562 | 0.1720 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.25 | 0.4045 | 0.2554 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.48 | 0.4331 | 0.2429 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.33 | 0.4255 | 0.2499 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.39 | 0.4309 | 0.2465 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.26 | 0.4021 | 0.2519 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.49 | 0.4243 | 0.2402 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.31 | 0.4196 | 0.2475 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.37 | 0.4225 | 0.2445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.34 | 0.7557 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.09 | 0.7657 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.75 | 0.7613 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.92 | 0.7638 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.73 | 0.7579 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.27 | 0.7674 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.04 | 0.7646 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.17 | 0.7665 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.97 | 0.7614 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.99 | 0.7641 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.93 | 0.7618 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.03 | 0.7610 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.03 | 0.7608 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.07 | 0.7623 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.87 | 0.7624 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.88 | 0.7617 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.90 | 0.7587 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.95 | 0.7600 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.27 | 0.7502 | 0.0277 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.21 | 0.7497 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.14 | 0.7658 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.67 | 0.7595 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.91 | 0.7631 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.13 | 0.7489 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.15 | 0.7664 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.81 | 0.7606 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.99 | 0.7638 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.11 | 0.7438 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.69 | 0.7630 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.37 | 0.7699 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.19 | 0.7675 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.21 | 0.7689 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.09 | 0.7655 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.48 | 0.7717 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.29 | 0.7694 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.36 | 0.7704 | 0.0229 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.39 | 0.7357 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.35 | 0.7513 | 0.0284 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.00 | 0.7479 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.21 | 0.7499 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.68 | 0.7367 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.35 | 0.7505 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.15 | 0.7491 | 0.0282 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.28 | 0.7511 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.60 | 0.7461 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.03 | 0.7423 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.13 | 0.7466 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.19 | 0.7394 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.37 | 0.7477 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.66 | 0.7507 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.94 | 0.7408 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.08 | 0.7458 | 0.0286 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.07 | 0.7377 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.25 | 0.7458 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.62 | 0.7059 | 0.0435 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.83 | 0.7131 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.05 | 0.7434 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.42 | 0.7345 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.77 | 0.7396 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.75 | 0.7128 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.92 | 0.7422 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.49 | 0.7352 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.75 | 0.7397 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.62 | 0.6653 | 0.0574 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.94 | 0.7440 | 0.0333 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.59 | 0.7531 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.57 | 0.7533 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.58 | 0.7551 | 0.0313 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.06 | 0.7390 | 0.0328 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.37 | 0.7490 | 0.0337 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.20 | 0.7465 | 0.0321 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.25 | 0.7489 | 0.0320 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 40.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.44 | 0.7455 | 0.0283 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.23 | 0.3670 | 0.3654 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.32 | 0.3929 | 0.3533 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.27 | 0.3840 | 0.3600 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.29 | 0.3891 | 0.3570 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.19 | 0.3747 | 0.3597 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.26 | 0.3961 | 0.3488 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.22 | 0.3911 | 0.3552 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.24 | 0.3944 | 0.3523 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.07 | 0.5942 | 0.1605 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.62 | 0.5622 | 0.1730 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.62 | 0.5622 | 0.1730 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.72 | 0.5605 | 0.1747 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.72 | 0.5605 | 0.1747 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.76 | 0.3015 | 0.2341 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.67 | 0.2771 | 0.2448 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.67 | 0.2771 | 0.2448 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.70 | 0.2752 | 0.2474 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.70 | 0.2752 | 0.2474 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.59 | 0.2593 | 0.2470 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.95 | 0.4143 | 0.3285 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.03 | 0.4477 | 0.3130 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.98 | 0.4362 | 0.3218 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.00 | 0.4426 | 0.3176 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.97 | 0.4153 | 0.3261 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.04 | 0.4454 | 0.3119 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.00 | 0.4379 | 0.3198 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.02 | 0.4426 | 0.3161 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.58 | 0.3306 | 0.2181 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.67 | 0.3309 | 0.3860 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.81 | 0.3549 | 0.3752 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.73 | 0.3467 | 0.3814 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.77 | 0.3515 | 0.3786 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.65 | 0.3410 | 0.3821 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.72 | 0.3537 | 0.3754 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.67 | 0.3497 | 0.3810 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.69 | 0.3514 | 0.3789 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.17 | 0.7372 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.92 | 0.7427 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.58 | 0.7401 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.75 | 0.7415 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.65 | 0.7391 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.13 | 0.7443 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.87 | 0.7426 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.01 | 0.7438 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.97 | 0.7410 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.06 | 0.7428 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.01 | 0.7416 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.03 | 0.7408 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.02 | 0.7406 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.09 | 0.7415 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.01 | 0.7420 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.03 | 0.7417 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.95 | 0.7398 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.98 | 0.7402 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.54 | 0.7377 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.10 | 0.7345 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.00 | 0.7432 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.55 | 0.7398 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.77 | 0.7416 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.00 | 0.7335 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.93 | 0.7432 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.60 | 0.7399 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.75 | 0.7417 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.48 | 0.7364 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.62 | 0.7426 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.28 | 0.7465 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.10 | 0.7450 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.12 | 0.7458 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.16 | 0.7449 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.60 | 0.7483 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.33 | 0.7470 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.45 | 0.7476 | 0.0289 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.62 | 0.7267 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.60 | 0.7374 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.13 | 0.7339 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.39 | 0.7361 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.08 | 0.7299 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.68 | 0.7384 | 0.0321 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.37 | 0.7363 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.53 | 0.7378 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.80 | 0.7382 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.34 | 0.7338 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.37 | 0.7342 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.54 | 0.7327 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.64 | 0.7349 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.88 | 0.7387 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.29 | 0.7330 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.38 | 0.7340 | 0.0334 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.46 | 0.7322 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.56 | 0.7342 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.69 | 0.7248 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.12 | 0.7139 | 0.0432 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.41 | 0.7337 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.74 | 0.7270 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.09 | 0.7306 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.02 | 0.7135 | 0.0430 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.21 | 0.7325 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.70 | 0.7270 | 0.0398 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.96 | 0.7303 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.94 | 0.7112 | 0.0437 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.12 | 0.7354 | 0.0364 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.77 | 0.7416 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.70 | 0.7398 | 0.0352 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.70 | 0.7409 | 0.0355 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.51 | 0.7351 | 0.0363 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.08 | 0.7420 | 0.0342 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.62 | 0.7388 | 0.0360 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.80 | 0.7403 | 0.0356 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.90 | 0.7361 | 0.0355 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.20 | 0.3399 | 0.3901 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.27 | 0.3514 | 0.3789 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.23 | 0.3488 | 0.3850 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.25 | 0.3508 | 0.3818 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.17 | 0.3378 | 0.3861 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.23 | 0.3460 | 0.3764 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.19 | 0.3458 | 0.3825 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.21 | 0.3461 | 0.3795 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.31 | 0.5895 | 0.2343 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.11 | 0.5753 | 0.2445 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.11 | 0.5753 | 0.2445 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.16 | 0.5766 | 0.2444 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.16 | 0.5766 | 0.2444 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.13 | 0.1974 | 0.2855 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.20 | 0.1952 | 0.2920 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.20 | 0.1952 | 0.2920 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.21 | 0.1949 | 0.2920 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.21 | 0.1949 | 0.2920 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.15 | 0.1883 | 0.2900 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.77 | 0.3821 | 0.3564 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.83 | 0.3974 | 0.3423 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.79 | 0.3943 | 0.3501 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.81 | 0.3966 | 0.3459 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.79 | 0.3803 | 0.3546 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.85 | 0.3917 | 0.3413 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.81 | 0.3910 | 0.3486 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.83 | 0.3919 | 0.3449 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.97 | 0.2599 | 0.2568 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.97 | 0.3151 | 0.4111 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.11 | 0.3240 | 0.4038 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.03 | 0.3224 | 0.4072 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.07 | 0.3238 | 0.4055 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.92 | 0.3177 | 0.4066 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.98 | 0.3186 | 0.4002 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.94 | 0.3213 | 0.4046 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.96 | 0.3203 | 0.4027 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.89 | 0.7359 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.90 | 0.7362 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.90 | 0.7361 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.90 | 0.7361 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.89 | 0.7359 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.90 | 0.7361 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.89 | 0.7360 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.89 | 0.7360 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.90 | 0.7362 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.89 | 0.7362 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.89 | 0.7361 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.90 | 0.7362 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.89 | 0.7361 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.90 | 0.7362 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.89 | 0.7361 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.89 | 0.7361 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.90 | 0.7361 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.90 | 0.7361 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.88 | 0.7360 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.82 | 0.7352 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.89 | 0.7360 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.86 | 0.7357 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.88 | 0.7359 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.82 | 0.7352 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.86 | 0.7358 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.85 | 0.7356 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.85 | 0.7357 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.75 | 0.7356 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.85 | 0.7357 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.85 | 0.7359 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.86 | 0.7358 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.86 | 0.7359 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.85 | 0.7356 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.85 | 0.7358 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.86 | 0.7357 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.86 | 0.7358 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.76 | 0.7344 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.85 | 0.7361 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.82 | 0.7357 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.84 | 0.7360 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.74 | 0.7346 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.79 | 0.7358 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.79 | 0.7358 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.80 | 0.7359 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.91 | 0.7368 | 0.0358 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.73 | 0.7356 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.71 | 0.7351 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.80 | 0.7358 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.79 | 0.7354 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.89 | 0.7367 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.71 | 0.7355 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.72 | 0.7352 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.78 | 0.7358 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.79 | 0.7356 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.58 | 0.7350 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.37 | 0.7304 | 0.0415 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.74 | 0.7354 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.65 | 0.7342 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.71 | 0.7351 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.35 | 0.7299 | 0.0415 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.55 | 0.7340 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.54 | 0.7332 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.54 | 0.7338 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.19 | 0.7333 | 0.0406 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.58 | 0.7339 | 0.0374 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.94 | 0.7341 | 0.0411 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.67 | 0.7348 | 0.0372 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.50 | 0.7347 | 0.0393 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.48 | 0.7332 | 0.0386 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.57 | 0.7341 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.52 | 0.7341 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.55 | 0.7342 | 0.0380 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.69 | 0.7371 | 0.0527 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.72 | 0.3447 | 0.4672 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.81 | 0.3642 | 0.4486 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.75 | 0.3578 | 0.4596 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.78 | 0.3615 | 0.4540 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.68 | 0.3447 | 0.4564 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.74 | 0.3587 | 0.4402 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.71 | 0.3560 | 0.4504 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.72 | 0.3579 | 0.4458 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.40 | 0.5762 | 0.3364 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.14 | 0.5546 | 0.3453 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.14 | 0.5546 | 0.3453 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.20 | 0.5548 | 0.3483 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.20 | 0.5548 | 0.3483 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.18 | 0.2382 | 0.3755 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.23 | 0.2267 | 0.3845 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.23 | 0.2267 | 0.3845 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.24 | 0.2263 | 0.3877 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.24 | 0.2263 | 0.3877 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.15 | 0.2160 | 0.3851 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.35 | 0.3925 | 0.4254 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.42 | 0.4181 | 0.3997 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.37 | 0.4098 | 0.4151 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.40 | 0.4146 | 0.4074 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.37 | 0.3911 | 0.4196 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.43 | 0.4123 | 0.3954 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.39 | 0.4076 | 0.4099 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.41 | 0.4107 | 0.4027 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.24 | 0.2934 | 0.3388 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.35 | 0.3147 | 0.4893 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.49 | 0.3302 | 0.4769 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.41 | 0.3254 | 0.4848 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.46 | 0.3285 | 0.4815 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.31 | 0.3186 | 0.4784 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.37 | 0.3250 | 0.4686 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.33 | 0.3246 | 0.4762 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.35 | 0.3251 | 0.4729 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.05 | 0.7333 | 0.0569 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.46 | 0.7361 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.29 | 0.7348 | 0.0552 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.37 | 0.7355 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.31 | 0.7342 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.57 | 0.7368 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.42 | 0.7359 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.50 | 0.7365 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.44 | 0.7352 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.43 | 0.7355 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.39 | 0.7348 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.46 | 0.7348 | 0.0579 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.44 | 0.7345 | 0.0566 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.49 | 0.7353 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.38 | 0.7351 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.37 | 0.7348 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.40 | 0.7344 | 0.0573 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.40 | 0.7344 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.20 | 0.7336 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.92 | 0.7308 | 0.0605 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.49 | 0.7360 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.22 | 0.7339 | 0.0582 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.35 | 0.7350 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.88 | 0.7303 | 0.0602 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.43 | 0.7358 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.24 | 0.7338 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.32 | 0.7349 | 0.0570 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.11 | 0.7330 | 0.0591 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.22 | 0.7349 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.53 | 0.7367 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.46 | 0.7360 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.47 | 0.7364 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.37 | 0.7352 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.59 | 0.7371 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.46 | 0.7363 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.52 | 0.7367 | 0.0541 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.69 | 0.7279 | 0.0645 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.28 | 0.7337 | 0.0591 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.03 | 0.7319 | 0.0617 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.16 | 0.7330 | 0.0603 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.94 | 0.7292 | 0.0623 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.29 | 0.7339 | 0.0580 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.11 | 0.7328 | 0.0601 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.21 | 0.7336 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.35 | 0.7344 | 0.0611 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.98 | 0.7313 | 0.0608 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.97 | 0.7309 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.14 | 0.7310 | 0.0624 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.16 | 0.7315 | 0.0595 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.38 | 0.7345 | 0.0573 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.92 | 0.7308 | 0.0599 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.96 | 0.7309 | 0.0581 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.07 | 0.7307 | 0.0613 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.11 | 0.7313 | 0.0596 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.64 | 0.7277 | 0.0635 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.25 | 0.7189 | 0.0744 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.13 | 0.7313 | 0.0642 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.73 | 0.7270 | 0.0695 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.94 | 0.7294 | 0.0664 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.16 | 0.7181 | 0.0731 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.94 | 0.7294 | 0.0645 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.65 | 0.7261 | 0.0695 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.79 | 0.7281 | 0.0667 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.08 | 0.7209 | 0.0697 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.86 | 0.7306 | 0.0630 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.99 | 0.7334 | 0.0651 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.18 | 0.7330 | 0.0618 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.14 | 0.7335 | 0.0634 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.95 | 0.7296 | 0.0628 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.25 | 0.7333 | 0.0605 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.01 | 0.7317 | 0.0622 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.10 | 0.7325 | 0.0618 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 315909 | 0.343 | 75.8 | 29.79 | 0.39 | 0.039 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 315909 | 0.343 | 78.7 | 29.79 | 0.39 | 0.039 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 315909 | 0.343 | 51.9 | 29.79 | 0.39 | 0.039 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 315909 | 0.343 | 64.2 | 29.79 | 0.39 | 0.039 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 804 | None | classic | 0.97 | False | 485988 | 1.039 | 192.1 | 27.87 | 0.29 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 804 | None | classic | 0.97 | False | 485988 | 1.039 | 163.7 | 27.87 | 0.29 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 804 | None | classic | 0.97 | False | 485988 | 1.039 | 151.8 | 27.87 | 0.29 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 804 | None | classic | 0.97 | False | 485988 | 1.039 | 169.7 | 27.87 | 0.29 | 0.011 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1276395 | 0.182 | 43.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1276086 | 0.809 | 49.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1276086 | 0.809 | 49.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1276086 | 0.591 | 43.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1276086 | 0.591 | 43.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1276395 | 0.182 | 51.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1276086 | 0.809 | 193.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1276086 | 0.809 | 193.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1276086 | 0.591 | 51.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1276086 | 0.591 | 51.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1273722 | 0.809 | 473.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 314050 | 0.331 | 60.8 | 29.68 | 0.33 | 0.036 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 314050 | 0.331 | 72.8 | 29.68 | 0.33 | 0.036 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 314050 | 0.331 | 63.8 | 29.68 | 0.33 | 0.036 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 314050 | 0.331 | 61.0 | 29.68 | 0.33 | 0.036 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1129 | None | classic | 1.91 | False | 432619 | 0.683 | 126.5 | 29.03 | 0.10 | 0.021 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1129 | None | classic | 1.91 | False | 432619 | 0.683 | 131.5 | 29.03 | 0.10 | 0.021 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1129 | None | classic | 1.91 | False | 432619 | 0.683 | 117.1 | 29.03 | 0.10 | 0.021 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1129 | None | classic | 1.91 | False | 432619 | 0.683 | 143.1 | 29.03 | 0.10 | 0.021 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1821654 | 0.809 | 112.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 292125 | 0.964 | 89.1 | 29.89 | 0.25 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 292125 | 0.964 | 76.2 | 29.89 | 0.25 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 292125 | 0.964 | 92.2 | 29.89 | 0.25 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 292125 | 0.964 | 56.2 | 29.89 | 0.25 | 0.027 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 808 | None | classic | 0.98 | False | 645102 | 1.352 | 248.6 | 27.71 | 0.27 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 808 | None | classic | 0.98 | False | 645102 | 1.352 | 206.6 | 27.71 | 0.27 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 808 | None | classic | 0.98 | False | 645102 | 1.352 | 227.4 | 27.71 | 0.27 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 808 | None | classic | 0.98 | False | 645102 | 1.352 | 249.2 | 27.71 | 0.27 | 0.010 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.573 | 0.024 |
| in035 | mask_ent | 0.717 | 0.024 |
| in035 | mask_grad | 0.427 | 0.024 |
| in035 | r_col | 0.771 | 0.024 |
| in035 | r_warp | 0.847 | 0.024 |

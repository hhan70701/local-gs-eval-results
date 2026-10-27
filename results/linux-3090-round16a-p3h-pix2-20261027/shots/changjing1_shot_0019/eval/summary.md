# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 9.3% | 25.15 / 0.0096 | 20.74 / 0.0252 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.5% | 25.24 / 0.0099 | 21.80 / 0.0203 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.3% | 25.15 / 0.0098 | 21.45 / 0.0227 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.3% | 25.18 / 0.0098 | 21.59 / 0.0213 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.4% | 25.18 / 0.0097 | 22.17 / 0.0176 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.8% | 25.29 / 0.0098 | 23.30 / 0.0139 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.5% | 25.27 / 0.0098 | 23.10 / 0.0140 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.6% | 25.29 / 0.0098 | 23.18 / 0.0133 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 9.3% | 25.03 / 0.0100 | 22.66 / 0.0265 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 7.8% | 24.83 / 0.0095 | 21.98 / 0.0218 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 1.6% | 20.19 / 0.0085 | 16.45 / 0.0142 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 7.8% | 24.80 / 0.0097 | 21.88 / 0.0230 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 1.6% | 22.38 / 0.0040 | 16.74 / 0.0111 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 9.2% | 25.15 / 0.0101 | 22.64 / 0.0192 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 7.8% | 24.86 / 0.0096 | 21.77 / 0.0218 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 1.7% | 23.42 / 0.0052 | 16.60 / 0.0241 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 7.9% | 24.85 / 0.0098 | 21.77 / 0.0223 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 1.8% | 23.63 / 0.0070 | 16.89 / 0.0332 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 10.9% | 25.54 / 0.0110 | 20.22 / 0.0411 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 14.2% | 25.44 / 0.0119 | 21.10 / 0.0336 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.3% | 25.51 / 0.0120 | 21.99 / 0.0267 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 14.2% | 25.45 / 0.0118 | 21.63 / 0.0298 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.2% | 25.46 / 0.0118 | 21.81 / 0.0281 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 14.1% | 25.50 / 0.0117 | 20.82 / 0.0297 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.6% | 25.58 / 0.0119 | 22.10 / 0.0253 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.2% | 25.52 / 0.0116 | 21.88 / 0.0257 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.2% | 25.55 / 0.0117 | 22.13 / 0.0243 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 15.6% | 25.71 / 0.0126 | 19.45 / 0.0547 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 8.4% | 25.13 / 0.0091 | 21.03 / 0.0217 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 8.9% | 25.42 / 0.0084 | 21.81 / 0.0165 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 8.7% | 25.34 / 0.0085 | 21.63 / 0.0185 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 8.8% | 25.39 / 0.0084 | 21.77 / 0.0173 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 8.8% | 25.36 / 0.0084 | 20.84 / 0.0202 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 9.5% | 25.54 / 0.0086 | 23.03 / 0.0154 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 9.3% | 25.50 / 0.0086 | 22.25 / 0.0175 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 9.4% | 25.54 / 0.0085 | 22.74 / 0.0162 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.98 / 0.0463 | 25.87 / 0.0553 | 20.50 / 0.0096 | 29.75 / 0.0330 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.01 / 0.0590 | 23.54 / 0.1250 | 20.02 / 0.0135 | 29.29 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.31 / 0.0539 | 24.38 / 0.0917 | 20.30 / 0.0116 | 29.45 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.21 / 0.0566 | 24.06 / 0.1080 | 20.17 / 0.0125 | 29.42 / 0.0358 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.24 / 0.0552 | 24.19 / 0.0981 | 20.20 / 0.0120 | 29.44 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.45 / 0.0523 | 24.50 / 0.0922 | 20.37 / 0.0112 | 29.50 / 0.0352 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.87 / 0.0487 | 26.33 / 0.0651 | 20.88 / 0.0093 | 29.65 / 0.0344 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.68 / 0.0505 | 25.54 / 0.0790 | 20.60 / 0.0102 | 29.61 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.76 / 0.0495 | 25.96 / 0.0720 | 20.69 / 0.0097 | 29.65 / 0.0346 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.91 / 0.0531 | 25.31 / 0.0907 | 20.55 / 0.0134 | 29.76 / 0.0331 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.21 / 0.0535 | 25.82 / 0.0677 | 20.14 / 0.0135 | 29.45 / 0.0338 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.15 / 0.0509 | 25.40 / 0.0678 | 19.91 / 0.0132 | 29.44 / 0.0337 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.27 / 0.0546 | 25.79 / 0.0730 | 20.10 / 0.0133 | 29.55 / 0.0345 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.22 / 0.0512 | 25.45 / 0.0689 | 19.86 / 0.0129 | 29.54 / 0.0336 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.88 / 0.0488 | 25.26 / 0.0736 | 20.57 / 0.0109 | 29.72 / 0.0333 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.20 / 0.0519 | 25.67 / 0.0708 | 20.11 / 0.0126 | 29.51 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.23 / 0.0498 | 25.70 / 0.0652 | 20.00 / 0.0123 | 29.54 / 0.0337 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.26 / 0.0522 | 25.62 / 0.0729 | 20.10 / 0.0123 | 29.57 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.28 / 0.0501 | 25.64 / 0.0659 | 19.96 / 0.0120 | 29.59 / 0.0335 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.99 / 0.0556 | 23.78 / 0.1136 | 20.22 / 0.0128 | 29.19 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.65 / 0.0661 | 23.29 / 0.1520 | 19.78 / 0.0145 | 29.11 / 0.0383 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.00 / 0.0587 | 24.01 / 0.1115 | 20.10 / 0.0123 | 29.34 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.90 / 0.0629 | 23.69 / 0.1312 | 19.92 / 0.0136 | 29.30 / 0.0375 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.93 / 0.0607 | 23.82 / 0.1205 | 20.00 / 0.0130 | 29.33 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.47 / 0.0601 | 23.09 / 0.1318 | 19.50 / 0.0141 | 29.06 / 0.0375 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.15 / 0.0544 | 24.73 / 0.0900 | 20.38 / 0.0112 | 29.27 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.87 / 0.0582 | 23.99 / 0.1156 | 19.94 / 0.0127 | 29.22 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.02 / 0.0566 | 24.40 / 0.1022 | 20.17 / 0.0121 | 29.24 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.95 / 0.0614 | 23.57 / 0.1266 | 19.28 / 0.0151 | 28.86 / 0.0383 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.23 / 0.0568 | 23.51 / 0.1203 | 20.26 / 0.0116 | 29.15 / 0.0359 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.38 / 0.0528 | 24.03 / 0.0975 | 20.31 / 0.0105 | 29.25 / 0.0350 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.34 / 0.0554 | 23.82 / 0.1102 | 20.34 / 0.0111 | 29.19 / 0.0357 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.36 / 0.0541 | 23.92 / 0.1042 | 20.32 / 0.0108 | 29.21 / 0.0353 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.21 / 0.0547 | 23.39 / 0.1099 | 20.28 / 0.0111 | 29.15 / 0.0353 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.78 / 0.0499 | 25.22 / 0.0757 | 20.95 / 0.0091 | 29.37 / 0.0348 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.55 / 0.0525 | 24.38 / 0.0959 | 20.65 / 0.0101 | 29.27 / 0.0351 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.67 / 0.0512 | 24.82 / 0.0857 | 20.83 / 0.0096 | 29.32 / 0.0350 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.3%） | — | — | 27.98 / 0.0463 | 25.87 / 0.0553 | 29.75 |
| in035 | rife | 3.3% | 8.4% | 27.23 / 0.0568 | 23.51 / 0.1203 | 29.15 |
| in035 | cnw_cnn | 5.4% | 9.3% | 27.01 / 0.0590 | 23.54 / 0.1250 | 29.29 |
| in035 | cnw_f5 | 8.1% | 14.2% | 26.65 / 0.0661 | 23.29 / 0.1520 | 29.11 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.29 / 0.0442 | -0.88 / +0.0127 (core 3.8%) | -1.09 / +0.0154 (core 6.6%) | -1.25 / +0.0229 (core 9.7%) |
| in035 | 2 | 0-3 | 27.74 / 0.0459 | -1.00 / +0.0142 (core 3.8%) | -1.07 / +0.0158 (core 6.6%) | -1.55 / +0.0247 (core 9.7%) |
| in035 | 4 | 3-5 | 28.92 / 0.0487 | -0.39 / +0.0047 (core 1.4%) | -0.75 / +0.0072 (core 2.5%) | -1.21 / +0.0119 (core 4.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.98 / 0.0463 | 25.87 | 29.75 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.01 / 0.0590 | 23.54 | 29.29 | 0/3 |
| in035 | cnw_cnn | oracle | 1.7% | 27.64 / 0.0515 | 25.03 | 29.70 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.31 / 0.0539 | 24.38 | 29.45 | 0/3 |
| in035 | cnw_cnn | oracle | 1.7% | 27.80 / 0.0489 | 25.44 | 29.72 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.21 / 0.0566 | 24.06 | 29.42 | 0/3 |
| in035 | cnw_cnn | oracle | 1.6% | 27.73 / 0.0503 | 25.27 | 29.72 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.24 / 0.0552 | 24.19 | 29.44 | 0/3 |
| in035 | cnw_cnn | oracle | 1.6% | 27.75 / 0.0495 | 25.31 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.45 / 0.0523 | 24.50 | 29.50 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.7% | 27.81 / 0.0478 | 25.61 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.87 / 0.0487 | 26.33 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.7% | 28.08 / 0.0460 | 26.85 | 29.75 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.68 / 0.0505 | 25.54 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.7% | 27.94 / 0.0468 | 26.29 | 29.74 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.76 / 0.0495 | 25.96 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.7% | 27.99 / 0.0463 | 26.55 | 29.75 | 1/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 27.91 / 0.0531 | 25.31 | 29.76 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 1.6% | 28.00 / 0.0505 | 25.86 | 29.75 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 27.21 / 0.0535 | 25.82 | 29.45 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 1.5% | 27.65 / 0.0504 | 26.44 | 29.72 | 1/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 27.15 / 0.0509 | 25.40 | 29.44 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 0.6% | 27.55 / 0.0497 | 25.88 | 29.72 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.27 / 0.0546 | 25.79 | 29.55 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 1.5% | 27.65 / 0.0504 | 26.31 | 29.74 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.22 / 0.0512 | 25.45 | 29.54 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 0.6% | 27.56 / 0.0496 | 25.82 | 29.73 | 1/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.88 / 0.0488 | 25.26 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 1.6% | 28.01 / 0.0476 | 25.98 | 29.75 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.20 / 0.0519 | 25.67 | 29.51 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.5% | 27.65 / 0.0491 | 26.32 | 29.73 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.23 / 0.0498 | 25.70 | 29.54 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.7% | 27.62 / 0.0486 | 26.05 | 29.73 | 1/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.26 / 0.0522 | 25.62 | 29.57 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 1.5% | 27.65 / 0.0490 | 26.25 | 29.73 | 1/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.28 / 0.0501 | 25.64 | 29.59 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 0.7% | 27.61 / 0.0485 | 25.97 | 29.73 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.99 / 0.0556 | 23.78 | 29.19 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.7% | 27.65 / 0.0498 | 25.84 | 29.68 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.65 / 0.0661 | 23.29 | 29.11 | 0/3 |
| in035 | cnw_f5 | oracle | 2.5% | 27.53 / 0.0535 | 24.97 | 29.70 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.00 / 0.0587 | 24.01 | 29.34 | 0/3 |
| in035 | cnw_f5 | oracle | 2.5% | 27.71 / 0.0503 | 25.39 | 29.72 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.90 / 0.0629 | 23.69 | 29.30 | 0/3 |
| in035 | cnw_f5 | oracle | 2.5% | 27.63 / 0.0522 | 25.16 | 29.72 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.93 / 0.0607 | 23.82 | 29.33 | 0/3 |
| in035 | cnw_f5 | oracle | 2.5% | 27.66 / 0.0512 | 25.26 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.47 / 0.0601 | 23.09 | 29.06 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.4% | 27.37 / 0.0508 | 24.93 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.15 / 0.0544 | 24.73 | 29.27 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.4% | 27.80 / 0.0480 | 26.12 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.87 / 0.0582 | 23.99 | 29.22 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.4% | 27.59 / 0.0495 | 25.58 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.02 / 0.0566 | 24.40 | 29.24 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.4% | 27.70 / 0.0490 | 25.88 | 29.73 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 25.95 / 0.0614 | 23.57 | 28.86 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.5% | 27.10 / 0.0519 | 25.69 | 29.61 | 0/3 |
| in035 | rife | 不复核 | —% | 27.23 / 0.0568 | 23.51 | 29.15 | 0/3 |
| in035 | rife | oracle | 1.3% | 27.78 / 0.0497 | 25.29 | 29.70 | 0/3 |
| in035 | rife | 不复核 | —% | 27.38 / 0.0528 | 24.03 | 29.25 | 0/3 |
| in035 | rife | oracle | 1.3% | 27.84 / 0.0481 | 25.54 | 29.71 | 0/3 |
| in035 | rife | 不复核 | —% | 27.34 / 0.0554 | 23.82 | 29.19 | 0/3 |
| in035 | rife | oracle | 1.3% | 27.83 / 0.0490 | 25.45 | 29.70 | 0/3 |
| in035 | rife | 不复核 | —% | 27.36 / 0.0541 | 23.92 | 29.21 | 0/3 |
| in035 | rife | oracle | 1.3% | 27.83 / 0.0486 | 25.48 | 29.70 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.21 / 0.0547 | 23.39 | 29.15 | 0/3 |
| in035 | rife_mw | oracle | 1.4% | 27.78 / 0.0484 | 25.15 | 29.70 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.78 / 0.0499 | 25.22 | 29.37 | 0/3 |
| in035 | rife_mw | oracle | 1.4% | 28.10 / 0.0459 | 26.52 | 29.71 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 27.55 / 0.0525 | 24.38 | 29.27 | 0/3 |
| in035 | rife_mw | oracle | 1.4% | 27.96 / 0.0474 | 25.87 | 29.71 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.67 / 0.0512 | 24.82 | 29.32 | 0/3 |
| in035 | rife_mw | oracle | 1.4% | 28.05 / 0.0466 | 26.22 | 29.71 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.98 / 0.0463 | 25.87 / 0.0553 | — |
| in035 | FF | 0（前馈） | 1008×644（61%） | 27.24 | 27.01 / 0.0590 | 23.54 / 0.1250 | 0/3 |
| in035 | 25 | 1.30 s | 1008×644（61%） | 27.85 | 27.21 / 0.0566 | 24.06 / 0.1080 | 0/3 |
| in035 | 50 | 2.60 s | 1008×644（61%） | 28.14 | 27.24 / 0.0552 | 24.19 / 0.0981 | 0/3 |
| in035 | 100 | 5.19 s | 1008×644（61%） | 28.41 | 27.31 / 0.0539 | 24.38 / 0.0917 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.98 / 0.0463 | 25.87 / 0.0553 | 29.75 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.01 / 0.0590 | 23.54 / 0.1250 | 29.29 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.64 / 0.0515 | 25.03 / 0.0874 | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.21 / 0.0566 | 24.06 / 0.1080 | 29.42 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.73 / 0.0503 | 25.27 / 0.0788 | 29.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.24 / 0.0552 | 24.19 / 0.0981 | 29.44 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.75 / 0.0495 | 25.31 / 0.0744 | 29.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.31 / 0.0539 | 24.38 / 0.0917 | 29.45 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.80 / 0.0489 | 25.44 / 0.0716 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.45 / 0.0523 | 24.50 / 0.0922 | 29.50 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.81 / 0.0478 | 25.61 / 0.0693 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.68 / 0.0505 | 25.54 / 0.0790 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.94 / 0.0468 | 26.29 / 0.0610 | 29.74 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.76 / 0.0495 | 25.96 / 0.0720 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.99 / 0.0463 | 26.55 / 0.0578 | 29.75 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.87 / 0.0487 | 26.33 / 0.0651 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.08 / 0.0460 | 26.85 / 0.0546 | 29.75 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.65 / 0.0661 | 23.29 / 0.1520 | 29.11 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.53 / 0.0535 | 24.97 / 0.0962 | 29.70 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.90 / 0.0629 | 23.69 / 0.1312 | 29.30 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.63 / 0.0522 | 25.16 / 0.0862 | 29.72 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.93 / 0.0607 | 23.82 / 0.1205 | 29.33 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.66 / 0.0512 | 25.26 / 0.0818 | 29.72 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.00 / 0.0587 | 24.01 / 0.1115 | 29.34 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.71 / 0.0503 | 25.39 / 0.0767 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.47 / 0.0601 | 23.09 / 0.1318 | 29.06 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.37 / 0.0508 | 24.93 / 0.0861 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.87 / 0.0582 | 23.99 / 0.1156 | 29.22 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.59 / 0.0495 | 25.58 / 0.0763 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.02 / 0.0566 | 24.40 / 0.1022 | 29.24 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.70 / 0.0490 | 25.88 / 0.0711 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.15 / 0.0544 | 24.73 / 0.0900 | 29.27 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.80 / 0.0480 | 26.12 / 0.0650 | 29.73 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.23 / 0.0568 | 23.51 / 0.1203 | 29.15 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.78 / 0.0497 | 25.29 / 0.0811 | 29.70 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.34 / 0.0554 | 23.82 / 0.1102 | 29.19 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.83 / 0.0490 | 25.45 / 0.0763 | 29.70 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.36 / 0.0541 | 23.92 / 0.1042 | 29.21 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.83 / 0.0486 | 25.48 / 0.0731 | 29.70 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.38 / 0.0528 | 24.03 / 0.0975 | 29.25 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.84 / 0.0481 | 25.54 / 0.0702 | 29.71 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.21 / 0.0547 | 23.39 / 0.1099 | 29.15 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.78 / 0.0484 | 25.15 / 0.0748 | 29.70 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.55 / 0.0525 | 24.38 / 0.0959 | 29.27 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.96 / 0.0474 | 25.87 / 0.0681 | 29.71 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.67 / 0.0512 | 24.82 / 0.0857 | 29.32 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.05 / 0.0466 | 26.22 / 0.0623 | 29.71 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.78 / 0.0499 | 25.22 / 0.0757 | 29.37 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.10 / 0.0459 | 26.52 / 0.0573 | 29.71 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.87 / 0.0553 | 20.50 / 0.0096 | 29.75 / 0.0330 | 27.98 / 0.0463 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 12.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.87 | 0.8310 | 0.0553 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 15.13 | 0.5206 | 0.3021 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 15.48 | 0.5959 | 0.2362 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 15.34 | 0.5693 | 0.2734 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 15.41 | 0.5855 | 0.2532 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 15.21 | 0.5848 | 0.2309 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 15.88 | 0.6810 | 0.1766 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 15.62 | 0.6474 | 0.2049 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 15.76 | 0.6662 | 0.1895 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 23.45 | 0.7684 | 0.1376 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 23.29 | 0.7972 | 0.1226 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 23.29 | 0.7972 | 0.1226 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 23.24 | 0.7879 | 0.1218 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 23.24 | 0.7879 | 0.1218 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.80 | 0.7057 | 0.1737 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 16.03 | 0.7151 | 0.1776 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 16.03 | 0.7151 | 0.1776 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 16.00 | 0.7070 | 0.1769 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 16.00 | 0.7070 | 0.1769 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.43 | 0.6713 | 0.2240 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 17.40 | 0.5420 | 0.2730 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 17.61 | 0.6196 | 0.2055 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 17.64 | 0.5922 | 0.2406 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 17.64 | 0.6088 | 0.2227 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 17.39 | 0.5723 | 0.2188 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 17.90 | 0.6663 | 0.1575 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 17.71 | 0.6282 | 0.1928 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 17.75 | 0.6458 | 0.1753 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.01 | 0.7309 | 0.1902 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 11.81 | 0.4828 | 0.3496 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.16 | 0.5491 | 0.2907 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 11.96 | 0.5241 | 0.3265 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.06 | 0.5383 | 0.3092 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.00 | 0.5099 | 0.3062 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 12.62 | 0.6152 | 0.2386 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 12.26 | 0.5671 | 0.2806 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 12.41 | 0.5896 | 0.2605 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.03 | 0.8106 | 0.0874 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.44 | 0.8275 | 0.0716 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.27 | 0.8195 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.31 | 0.8229 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.61 | 0.8299 | 0.0693 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.85 | 0.8549 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.29 | 0.8444 | 0.0610 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.55 | 0.8497 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.86 | 0.8292 | 0.0781 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.44 | 0.8505 | 0.0596 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.88 | 0.8360 | 0.0620 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.31 | 0.8461 | 0.0630 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.82 | 0.8345 | 0.0636 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.98 | 0.8380 | 0.0637 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.32 | 0.8473 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.05 | 0.8385 | 0.0606 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.25 | 0.8433 | 0.0626 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.97 | 0.8364 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.84 | 0.8397 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.97 | 0.8081 | 0.0962 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.39 | 0.8257 | 0.0767 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.16 | 0.8177 | 0.0862 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.26 | 0.8211 | 0.0818 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.93 | 0.8157 | 0.0861 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.12 | 0.8458 | 0.0650 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.58 | 0.8310 | 0.0763 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.88 | 0.8385 | 0.0711 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.69 | 0.8390 | 0.0798 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.29 | 0.8151 | 0.0811 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.54 | 0.8281 | 0.0702 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.45 | 0.8211 | 0.0763 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.48 | 0.8241 | 0.0731 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.15 | 0.8181 | 0.0748 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.52 | 0.8491 | 0.0573 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.87 | 0.8343 | 0.0681 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.22 | 0.8422 | 0.0623 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.54 | 0.7572 | 0.1250 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.38 | 0.7941 | 0.0917 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.06 | 0.7794 | 0.1080 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.19 | 0.7866 | 0.0981 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.50 | 0.7966 | 0.0922 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.33 | 0.8445 | 0.0651 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.54 | 0.8272 | 0.0790 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.96 | 0.8371 | 0.0720 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.31 | 0.8164 | 0.0907 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.82 | 0.8420 | 0.0677 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.40 | 0.8284 | 0.0678 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.79 | 0.8361 | 0.0730 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.45 | 0.8274 | 0.0689 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.26 | 0.8263 | 0.0736 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.67 | 0.8346 | 0.0708 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.70 | 0.8320 | 0.0652 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.62 | 0.8297 | 0.0729 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.64 | 0.8300 | 0.0659 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.78 | 0.8072 | 0.1136 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.29 | 0.7362 | 0.1520 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.01 | 0.7774 | 0.1115 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.69 | 0.7625 | 0.1312 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.82 | 0.7697 | 0.1205 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.09 | 0.7495 | 0.1318 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.73 | 0.8087 | 0.0900 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.99 | 0.7827 | 0.1156 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.40 | 0.7960 | 0.1022 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.57 | 0.7999 | 0.1266 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.51 | 0.7489 | 0.1203 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.03 | 0.7812 | 0.0975 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.82 | 0.7665 | 0.1102 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.92 | 0.7742 | 0.1042 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.39 | 0.7609 | 0.1099 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.22 | 0.8223 | 0.0757 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.38 | 0.7946 | 0.0959 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.82 | 0.8092 | 0.0857 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.50 | 0.7050 | 0.0096 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.76 | 0.2747 | 0.0909 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.82 | 0.3088 | 0.0875 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.78 | 0.2927 | 0.0897 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.79 | 0.2995 | 0.0887 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.44 | 0.3042 | 0.0767 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.52 | 0.3482 | 0.0744 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.46 | 0.3287 | 0.0759 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.48 | 0.3372 | 0.0752 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.72 | 0.3801 | 0.0508 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 13.33 | 0.3470 | 0.0535 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 13.33 | 0.3470 | 0.0535 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 13.35 | 0.3492 | 0.0534 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 13.35 | 0.3492 | 0.0534 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.38 | 0.3314 | 0.0565 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.16 | 0.2886 | 0.0609 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.16 | 0.2886 | 0.0609 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.20 | 0.2936 | 0.0604 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.20 | 0.2936 | 0.0604 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.11 | 0.2744 | 0.0605 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.97 | 0.3731 | 0.0757 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.20 | 0.4157 | 0.0710 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.03 | 0.3973 | 0.0738 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.10 | 0.4063 | 0.0725 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.93 | 0.3508 | 0.0748 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.99 | 0.4144 | 0.0705 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.96 | 0.3870 | 0.0732 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.96 | 0.4019 | 0.0720 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.44 | 0.3618 | 0.0508 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.67 | 0.2723 | 0.0933 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.77 | 0.3041 | 0.0896 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.70 | 0.2908 | 0.0916 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.74 | 0.2956 | 0.0905 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.59 | 0.2774 | 0.0918 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.67 | 0.3338 | 0.0876 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.61 | 0.3087 | 0.0900 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.63 | 0.3203 | 0.0891 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.03 | 0.6840 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.30 | 0.7063 | 0.0115 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.18 | 0.6957 | 0.0124 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.20 | 0.6998 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.38 | 0.7143 | 0.0112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.89 | 0.7441 | 0.0092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.61 | 0.7302 | 0.0102 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.70 | 0.7365 | 0.0097 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.55 | 0.7099 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.16 | 0.7183 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.92 | 0.6979 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.11 | 0.7117 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.88 | 0.6932 | 0.0128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.56 | 0.7171 | 0.0109 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.13 | 0.7134 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.02 | 0.7005 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.11 | 0.7089 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.98 | 0.6968 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.23 | 0.7096 | 0.0127 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.79 | 0.6834 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.10 | 0.7075 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.93 | 0.6985 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.01 | 0.7025 | 0.0128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.52 | 0.6809 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.39 | 0.7321 | 0.0111 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.96 | 0.7070 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.18 | 0.7199 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.33 | 0.6769 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.27 | 0.6982 | 0.0116 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.32 | 0.7128 | 0.0105 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.35 | 0.7065 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.33 | 0.7091 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.30 | 0.7019 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.95 | 0.7395 | 0.0091 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.66 | 0.7218 | 0.0100 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.83 | 0.7315 | 0.0095 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.02 | 0.6819 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.30 | 0.7050 | 0.0116 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.17 | 0.6940 | 0.0125 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.20 | 0.6984 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.37 | 0.7131 | 0.0112 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.88 | 0.7436 | 0.0093 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.60 | 0.7296 | 0.0102 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.69 | 0.7359 | 0.0097 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.55 | 0.7088 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.14 | 0.7174 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.91 | 0.6971 | 0.0132 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.10 | 0.7110 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.86 | 0.6924 | 0.0129 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.57 | 0.7159 | 0.0109 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.11 | 0.7127 | 0.0126 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.00 | 0.6997 | 0.0123 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.10 | 0.7084 | 0.0123 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.96 | 0.6961 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.22 | 0.7069 | 0.0128 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.78 | 0.6800 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.10 | 0.7056 | 0.0123 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.92 | 0.6956 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.00 | 0.6998 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.50 | 0.6772 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.38 | 0.7302 | 0.0112 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.94 | 0.7042 | 0.0127 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.17 | 0.7176 | 0.0121 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.28 | 0.6713 | 0.0151 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.26 | 0.6958 | 0.0116 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.31 | 0.7115 | 0.0105 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.34 | 0.7047 | 0.0111 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.32 | 0.7074 | 0.0108 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.28 | 0.6986 | 0.0111 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.95 | 0.7385 | 0.0091 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.65 | 0.7198 | 0.0101 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.83 | 0.7300 | 0.0096 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 27.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.28 | 0.7954 | 0.0173 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.31 | 0.4651 | 0.1969 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.44 | 0.4899 | 0.1862 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.35 | 0.4811 | 0.1923 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.38 | 0.4853 | 0.1893 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.15 | 0.4364 | 0.1736 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.27 | 0.4648 | 0.1650 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.17 | 0.4618 | 0.1698 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.20 | 0.4648 | 0.1675 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.24 | 0.5468 | 0.1066 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.56 | 0.5444 | 0.1105 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.56 | 0.5444 | 0.1105 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.56 | 0.5330 | 0.1119 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.56 | 0.5330 | 0.1119 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.64 | 0.4202 | 0.1332 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.30 | 0.3899 | 0.1449 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.30 | 0.3899 | 0.1449 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.31 | 0.3821 | 0.1460 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.31 | 0.3821 | 0.1460 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.89 | 0.3042 | 0.1655 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.82 | 0.5297 | 0.1652 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.07 | 0.5647 | 0.1522 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.89 | 0.5561 | 0.1592 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.96 | 0.5606 | 0.1556 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.69 | 0.5148 | 0.1651 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.00 | 0.5625 | 0.1505 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.75 | 0.5487 | 0.1596 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.84 | 0.5559 | 0.1560 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.57 | 0.3850 | 0.1484 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.32 | 0.4663 | 0.1974 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.53 | 0.4917 | 0.1869 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.39 | 0.4838 | 0.1933 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.45 | 0.4879 | 0.1902 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.34 | 0.4666 | 0.1937 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.58 | 0.5094 | 0.1830 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.40 | 0.4975 | 0.1893 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.47 | 0.5040 | 0.1867 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.62 | 0.7812 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.99 | 0.7912 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.83 | 0.7867 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.89 | 0.7888 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.09 | 0.7944 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.64 | 0.8064 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.37 | 0.8017 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.47 | 0.8040 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.09 | 0.7903 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.81 | 0.7963 | 0.0212 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.60 | 0.7897 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.76 | 0.7927 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.56 | 0.7877 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.14 | 0.7951 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.77 | 0.7946 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.69 | 0.7908 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.74 | 0.7919 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.65 | 0.7888 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.41 | 0.7831 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.30 | 0.7788 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.73 | 0.7899 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.50 | 0.7856 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.62 | 0.7876 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.11 | 0.7780 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.98 | 0.7970 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.56 | 0.7885 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.79 | 0.7931 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.42 | 0.7683 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.85 | 0.7861 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.04 | 0.7929 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.01 | 0.7903 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.05 | 0.7918 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.84 | 0.7878 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.59 | 0.8028 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.29 | 0.7965 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.47 | 0.8002 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.34 | 0.7547 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.80 | 0.7688 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.68 | 0.7646 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.73 | 0.7668 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.12 | 0.7781 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.69 | 0.7966 | 0.0205 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.52 | 0.7938 | 0.0209 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.57 | 0.7959 | 0.0204 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.24 | 0.7619 | 0.0304 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.93 | 0.7854 | 0.0263 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.90 | 0.7836 | 0.0220 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.91 | 0.7783 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.86 | 0.7789 | 0.0222 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.23 | 0.7753 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.78 | 0.7808 | 0.0261 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.91 | 0.7831 | 0.0215 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.77 | 0.7749 | 0.0269 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.88 | 0.7780 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.80 | 0.7291 | 0.0438 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.70 | 0.7399 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.20 | 0.7599 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.05 | 0.7564 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.10 | 0.7585 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.40 | 0.7361 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.20 | 0.7680 | 0.0269 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.07 | 0.7596 | 0.0275 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.19 | 0.7650 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.13 | 0.6780 | 0.0547 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.72 | 0.7614 | 0.0286 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.99 | 0.7744 | 0.0253 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.00 | 0.7720 | 0.0270 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.08 | 0.7748 | 0.0257 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.50 | 0.7567 | 0.0279 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.52 | 0.7866 | 0.0235 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.26 | 0.7778 | 0.0255 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.48 | 0.7835 | 0.0242 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 44.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.66 | 0.7411 | 0.0260 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.70 | 0.3441 | 0.3441 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.74 | 0.3610 | 0.3353 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.71 | 0.3555 | 0.3403 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.72 | 0.3581 | 0.3379 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.89 | 0.3226 | 0.2954 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.91 | 0.3373 | 0.2893 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.88 | 0.3344 | 0.2925 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.89 | 0.3363 | 0.2910 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.86 | 0.4980 | 0.1804 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.36 | 0.4789 | 0.1896 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.36 | 0.4789 | 0.1896 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.39 | 0.4722 | 0.1901 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.39 | 0.4722 | 0.1901 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.58 | 0.2711 | 0.2229 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.40 | 0.2515 | 0.2309 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.40 | 0.2515 | 0.2309 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.43 | 0.2486 | 0.2311 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.43 | 0.2486 | 0.2311 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.37 | 0.2378 | 0.2354 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.54 | 0.4060 | 0.3121 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.60 | 0.4291 | 0.3013 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.56 | 0.4233 | 0.3072 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.58 | 0.4262 | 0.3043 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.56 | 0.4099 | 0.3075 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.62 | 0.4388 | 0.2973 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.58 | 0.4298 | 0.3039 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.60 | 0.4347 | 0.3011 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.71 | 0.3264 | 0.2107 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.57 | 0.3431 | 0.3433 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.64 | 0.3612 | 0.3343 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.60 | 0.3556 | 0.3398 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.62 | 0.3586 | 0.3372 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.58 | 0.3474 | 0.3390 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.64 | 0.3725 | 0.3307 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.60 | 0.3644 | 0.3354 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.62 | 0.3685 | 0.3334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.11 | 0.7328 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.39 | 0.7383 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.27 | 0.7357 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.31 | 0.7369 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.42 | 0.7398 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.89 | 0.7465 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.64 | 0.7437 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.74 | 0.7451 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.69 | 0.7406 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.23 | 0.7414 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.06 | 0.7378 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.19 | 0.7394 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.04 | 0.7367 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.70 | 0.7427 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.18 | 0.7406 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.12 | 0.7383 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.17 | 0.7392 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.10 | 0.7374 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.12 | 0.7390 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.00 | 0.7318 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.34 | 0.7380 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.17 | 0.7355 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.25 | 0.7367 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.82 | 0.7321 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.44 | 0.7428 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.14 | 0.7379 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.29 | 0.7405 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.49 | 0.7324 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.43 | 0.7376 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.57 | 0.7415 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.54 | 0.7398 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.56 | 0.7406 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.39 | 0.7384 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.98 | 0.7464 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.72 | 0.7427 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.87 | 0.7447 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.23 | 0.7179 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.65 | 0.7276 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.51 | 0.7239 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.55 | 0.7255 | 0.0334 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.93 | 0.7333 | 0.0304 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.53 | 0.7436 | 0.0274 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.24 | 0.7407 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.34 | 0.7424 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.50 | 0.7361 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.78 | 0.7387 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.71 | 0.7357 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.78 | 0.7348 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.73 | 0.7339 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.44 | 0.7391 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.67 | 0.7370 | 0.0311 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.73 | 0.7359 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.70 | 0.7342 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.75 | 0.7341 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.43 | 0.7312 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.74 | 0.7084 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.23 | 0.7217 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.07 | 0.7180 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.12 | 0.7197 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.58 | 0.7112 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.54 | 0.7313 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.14 | 0.7236 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.36 | 0.7278 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.99 | 0.7106 | 0.0402 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.83 | 0.7263 | 0.0335 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.10 | 0.7345 | 0.0304 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.05 | 0.7319 | 0.0323 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.08 | 0.7335 | 0.0313 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.73 | 0.7269 | 0.0320 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.62 | 0.7413 | 0.0281 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.28 | 0.7361 | 0.0299 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.48 | 0.7388 | 0.0290 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.75 | 0.7297 | 0.0330 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.85 | 0.3135 | 0.3587 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.89 | 0.3233 | 0.3525 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.86 | 0.3215 | 0.3557 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.87 | 0.3230 | 0.3541 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.94 | 0.2621 | 0.3255 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.95 | 0.2699 | 0.3205 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.95 | 0.2693 | 0.3235 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.95 | 0.2700 | 0.3219 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.33 | 0.4968 | 0.2345 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.28 | 0.4889 | 0.2400 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.28 | 0.4889 | 0.2400 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.28 | 0.4866 | 0.2401 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.28 | 0.4866 | 0.2401 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.46 | 0.1817 | 0.2624 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.46 | 0.1779 | 0.2648 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.46 | 0.1779 | 0.2648 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.47 | 0.1775 | 0.2652 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.47 | 0.1775 | 0.2652 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.42 | 0.1728 | 0.2657 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.36 | 0.3522 | 0.3300 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.42 | 0.3649 | 0.3210 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.38 | 0.3628 | 0.3257 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.40 | 0.3646 | 0.3232 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.37 | 0.3554 | 0.3244 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.39 | 0.3646 | 0.3164 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.38 | 0.3644 | 0.3211 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.38 | 0.3648 | 0.3186 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.31 | 0.2437 | 0.2369 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.72 | 0.3017 | 0.3646 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.77 | 0.3103 | 0.3587 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.73 | 0.3084 | 0.3623 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.75 | 0.3099 | 0.3605 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.71 | 0.3032 | 0.3601 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.75 | 0.3134 | 0.3557 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.72 | 0.3112 | 0.3582 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.74 | 0.3124 | 0.3570 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.70 | 0.7291 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.72 | 0.7294 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.72 | 0.7293 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.72 | 0.7294 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.73 | 0.7295 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.75 | 0.7298 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.74 | 0.7297 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.75 | 0.7298 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.75 | 0.7298 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.72 | 0.7296 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.72 | 0.7295 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.74 | 0.7297 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.73 | 0.7296 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.75 | 0.7298 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.73 | 0.7297 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.73 | 0.7296 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.73 | 0.7297 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.73 | 0.7296 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.68 | 0.7294 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.70 | 0.7291 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.72 | 0.7294 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.72 | 0.7293 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.72 | 0.7293 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.71 | 0.7292 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7296 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.73 | 0.7295 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.73 | 0.7296 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.61 | 0.7291 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.70 | 0.7293 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.71 | 0.7294 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.70 | 0.7293 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.70 | 0.7294 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.70 | 0.7293 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7296 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.71 | 0.7294 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.71 | 0.7295 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.29 | 0.7249 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.45 | 0.7270 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.42 | 0.7265 | 0.0358 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.44 | 0.7268 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.50 | 0.7274 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.65 | 0.7293 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.61 | 0.7291 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.65 | 0.7294 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.76 | 0.7301 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.45 | 0.7287 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.44 | 0.7281 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.55 | 0.7288 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.54 | 0.7285 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.72 | 0.7298 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.51 | 0.7287 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.54 | 0.7285 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.57 | 0.7288 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.59 | 0.7287 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.19 | 0.7277 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.11 | 0.7222 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.34 | 0.7254 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.30 | 0.7248 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.33 | 0.7252 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.06 | 0.7228 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.27 | 0.7261 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.22 | 0.7254 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.24 | 0.7258 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.86 | 0.7258 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.15 | 0.7233 | 0.0359 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.25 | 0.7254 | 0.0350 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.19 | 0.7247 | 0.0357 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.21 | 0.7252 | 0.0353 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.15 | 0.7240 | 0.0353 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.37 | 0.7272 | 0.0348 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.27 | 0.7261 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.32 | 0.7267 | 0.0350 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.98 | 0.7399 | 0.0463 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.31 | 0.3229 | 0.4242 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.35 | 0.3370 | 0.4106 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.32 | 0.3328 | 0.4187 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.33 | 0.3353 | 0.4148 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.28 | 0.2833 | 0.3877 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.29 | 0.2963 | 0.3777 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.28 | 0.2937 | 0.3835 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.29 | 0.2954 | 0.3805 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.38 | 0.4933 | 0.3240 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.17 | 0.4780 | 0.3311 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.17 | 0.4780 | 0.3311 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.19 | 0.4749 | 0.3315 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.19 | 0.4749 | 0.3315 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.53 | 0.2238 | 0.3398 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.46 | 0.2108 | 0.3459 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.46 | 0.2108 | 0.3459 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.47 | 0.2100 | 0.3466 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.47 | 0.2100 | 0.3466 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.42 | 0.2019 | 0.3507 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.91 | 0.3710 | 0.3880 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.98 | 0.3901 | 0.3702 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.93 | 0.3853 | 0.3802 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.95 | 0.3883 | 0.3751 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.91 | 0.3725 | 0.3743 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.94 | 0.3914 | 0.3600 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.93 | 0.3864 | 0.3697 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.93 | 0.3892 | 0.3656 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.45 | 0.2769 | 0.3100 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.17 | 0.3146 | 0.4258 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.24 | 0.3280 | 0.4125 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.20 | 0.3239 | 0.4206 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.22 | 0.3263 | 0.4166 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.17 | 0.3183 | 0.4152 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.22 | 0.3362 | 0.4044 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.18 | 0.3304 | 0.4107 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.20 | 0.3332 | 0.4079 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.64 | 0.7352 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.80 | 0.7381 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.73 | 0.7368 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.75 | 0.7374 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.81 | 0.7387 | 0.0478 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.08 | 0.7423 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.94 | 0.7408 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.99 | 0.7415 | 0.0463 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.00 | 0.7399 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.65 | 0.7395 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.55 | 0.7377 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.65 | 0.7388 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.56 | 0.7374 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.01 | 0.7407 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.65 | 0.7393 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.62 | 0.7382 | 0.0486 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.65 | 0.7387 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.61 | 0.7377 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.65 | 0.7385 | 0.0498 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.53 | 0.7343 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.71 | 0.7376 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.63 | 0.7363 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.66 | 0.7369 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.37 | 0.7339 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.80 | 0.7397 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.59 | 0.7371 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.70 | 0.7385 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.10 | 0.7339 | 0.0519 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.78 | 0.7371 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.84 | 0.7391 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.83 | 0.7382 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.83 | 0.7386 | 0.0486 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.78 | 0.7376 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.10 | 0.7419 | 0.0459 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.96 | 0.7399 | 0.0474 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.05 | 0.7410 | 0.0466 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.01 | 0.7255 | 0.0590 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.31 | 0.7314 | 0.0539 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.21 | 0.7293 | 0.0566 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.24 | 0.7303 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.45 | 0.7339 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.87 | 0.7404 | 0.0487 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.68 | 0.7386 | 0.0505 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.76 | 0.7397 | 0.0495 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.91 | 0.7378 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.21 | 0.7372 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.15 | 0.7354 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.27 | 0.7358 | 0.0546 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.22 | 0.7350 | 0.0512 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.88 | 0.7390 | 0.0488 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.20 | 0.7366 | 0.0519 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.23 | 0.7360 | 0.0498 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.26 | 0.7355 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.28 | 0.7353 | 0.0501 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.99 | 0.7334 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.65 | 0.7192 | 0.0661 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.00 | 0.7273 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.90 | 0.7251 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.93 | 0.7262 | 0.0607 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.47 | 0.7201 | 0.0601 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.15 | 0.7317 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.87 | 0.7272 | 0.0582 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.02 | 0.7297 | 0.0566 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.95 | 0.7214 | 0.0614 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.23 | 0.7276 | 0.0568 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.38 | 0.7326 | 0.0528 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.34 | 0.7308 | 0.0554 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.36 | 0.7318 | 0.0541 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.21 | 0.7284 | 0.0547 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.78 | 0.7377 | 0.0499 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.55 | 0.7341 | 0.0525 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.67 | 0.7360 | 0.0512 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 298366 | 0.327 | 91.0 | 29.83 | 0.26 | 0.017 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 298366 | 0.327 | 84.6 | 29.83 | 0.26 | 0.017 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 298366 | 0.327 | 57.4 | 29.83 | 0.26 | 0.017 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 298366 | 0.327 | 63.8 | 29.83 | 0.26 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 685 | None | classic | 0.46 | False | 402154 | 0.974 | 174.5 | 31.62 | 0.27 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 685 | None | classic | 0.46 | False | 402154 | 0.974 | 168.3 | 31.62 | 0.27 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 685 | None | classic | 0.46 | False | 402154 | 0.974 | 192.0 | 31.62 | 0.27 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 685 | None | classic | 0.46 | False | 402154 | 0.974 | 189.9 | 31.62 | 0.27 | 0.017 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1301917 | 0.193 | 44.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1301917 | 0.800 | 47.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1301917 | 0.800 | 47.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1301917 | 0.651 | 44.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1301917 | 0.651 | 44.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301917 | 0.193 | 52.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301917 | 0.800 | 193.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301917 | 0.800 | 193.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301917 | 0.651 | 51.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1301917 | 0.651 | 51.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1299911 | 0.800 | 467.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 266127 | 0.323 | 118.8 | 29.64 | 0.15 | 0.022 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 266127 | 0.323 | 70.6 | 29.64 | 0.15 | 0.022 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 266127 | 0.323 | 64.1 | 29.64 | 0.15 | 0.022 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 266127 | 0.323 | 58.0 | 29.64 | 0.15 | 0.022 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 851 | None | classic | 0.60 | False | 462489 | 1.013 | 189.2 | 31.50 | 0.06 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 851 | None | classic | 0.60 | False | 462489 | 1.013 | 216.3 | 31.50 | 0.06 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 851 | None | classic | 0.60 | False | 462489 | 1.013 | 211.1 | 31.50 | 0.06 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 851 | None | classic | 0.60 | False | 462489 | 1.013 | 228.9 | 31.50 | 0.06 | 0.009 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1708418 | 0.800 | 110.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 284605 | 0.921 | 80.6 | 29.95 | 0.21 | 0.019 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 284605 | 0.921 | 77.7 | 29.95 | 0.21 | 0.019 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 284605 | 0.921 | 86.5 | 29.95 | 0.21 | 0.019 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 284605 | 0.921 | 57.0 | 29.95 | 0.21 | 0.019 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 882 | None | classic | 1.16 | False | 435597 | 0.974 | 141.7 | 28.59 | 0.14 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 882 | None | classic | 1.16 | False | 435597 | 0.974 | 149.3 | 28.59 | 0.14 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 882 | None | classic | 1.16 | False | 435597 | 0.974 | 142.5 | 28.59 | 0.14 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 882 | None | classic | 1.16 | False | 435597 | 0.974 | 154.4 | 28.59 | 0.14 | 0.009 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.604 | 0.020 |
| in035 | mask_ent | 0.712 | 0.020 |
| in035 | mask_grad | 0.428 | 0.020 |
| in035 | r_col | 0.741 | 0.020 |
| in035 | r_warp | 0.840 | 0.020 |

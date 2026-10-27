# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 3.3% | 22.88 / 0.0142 | 22.78 / 0.0268 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.3% | 22.86 / 0.0155 | 22.99 / 0.0218 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.3% | 22.94 / 0.0142 | 23.67 / 0.0216 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.3% | 22.90 / 0.0151 | 23.25 / 0.0206 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.9% | 22.48 / 0.0134 | 21.39 / 0.0276 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.4% | 22.90 / 0.0157 | 20.73 / 0.0371 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.0% | 22.52 / 0.0136 | 21.71 / 0.0285 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.1% | 22.62 / 0.0151 | 20.92 / 0.0353 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 3.2% | 22.72 / 0.0156 | 22.22 / 0.0393 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 3.0% | 22.63 / 0.0165 | 22.43 / 0.0449 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 1.0% | 19.28 / 0.0140 | 19.79 / 0.0349 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 3.0% | 22.60 / 0.0170 | 21.04 / 0.0657 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 1.2% | 19.60 / 0.0150 | 18.28 / 0.0564 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 3.1% | 22.68 / 0.0156 | 21.98 / 0.0245 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 3.0% | 22.63 / 0.0171 | 21.87 / 0.0422 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 1.2% | 19.98 / 0.0139 | 19.74 / 0.0306 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 3.0% | 22.61 / 0.0170 | 21.16 / 0.0527 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 1.2% | 20.00 / 0.0136 | 18.85 / 0.0419 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 3.6% | 22.97 / 0.0166 | 21.01 / 0.0486 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 7.8% | 24.42 / 0.0092 | 21.53 / 0.0236 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.0% | 24.42 / 0.0095 | 22.87 / 0.0186 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.8% | 24.42 / 0.0092 | 22.67 / 0.0212 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.9% | 24.40 / 0.0095 | 22.83 / 0.0195 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 7.5% | 24.35 / 0.0094 | 23.73 / 0.0163 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.0% | 24.56 / 0.0095 | 23.76 / 0.0148 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.5% | 24.40 / 0.0094 | 23.89 / 0.0148 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.7% | 24.49 / 0.0096 | 23.75 / 0.0145 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 8.1% | 24.45 / 0.0094 | 21.92 / 0.0313 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 2.7% | 25.70 / 0.0158 | 25.20 / 0.0221 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 2.8% | 25.72 / 0.0156 | 25.64 / 0.0194 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 2.7% | 25.67 / 0.0154 | 25.47 / 0.0199 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 2.7% | 25.68 / 0.0156 | 25.71 / 0.0193 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 2.5% | 25.33 / 0.0155 | 24.84 / 0.0225 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 2.6% | 25.51 / 0.0154 | 25.07 / 0.0217 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 2.5% | 25.36 / 0.0153 | 25.08 / 0.0215 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 2.5% | 25.40 / 0.0153 | 25.29 / 0.0211 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.06 / 0.0495 | 36.83 / 0.0224 | 20.52 / 0.0092 | 29.80 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.07 / 0.0524 | 36.83 / 0.0224 | 20.96 / 0.0094 | 29.78 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.07 / 0.0510 | 36.83 / 0.0224 | 21.02 / 0.0092 | 29.76 / 0.0377 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.16 / 0.0513 | 36.83 / 0.0224 | 21.12 / 0.0089 | 29.79 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.11 / 0.0510 | 36.83 / 0.0224 | 21.07 / 0.0090 | 29.78 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.01 / 0.0518 | 36.83 / 0.0224 | 21.00 / 0.0096 | 29.77 / 0.0377 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.00 / 0.0506 | 36.83 / 0.0224 | 20.97 / 0.0092 | 29.77 / 0.0375 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.06 / 0.0512 | 36.83 / 0.0224 | 21.06 / 0.0093 | 29.77 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.04 / 0.0508 | 36.83 / 0.0224 | 21.03 / 0.0092 | 29.77 / 0.0375 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.03 / 0.0535 | 36.83 / 0.0224 | 20.53 / 0.0127 | 29.81 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.06 / 0.0539 | 36.83 / 0.0224 | 20.81 / 0.0120 | 29.80 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.08 / 0.0524 | 36.83 / 0.0224 | 20.82 / 0.0114 | 29.80 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.91 / 0.0566 | 36.83 / 0.0224 | 20.62 / 0.0132 | 29.80 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.94 / 0.0548 | 36.83 / 0.0224 | 20.62 / 0.0126 | 29.80 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.99 / 0.0515 | 36.83 / 0.0224 | 20.54 / 0.0107 | 29.80 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.00 / 0.0534 | 36.83 / 0.0224 | 20.76 / 0.0113 | 29.79 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.06 / 0.0522 | 36.83 / 0.0224 | 20.81 / 0.0109 | 29.80 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.91 / 0.0545 | 36.83 / 0.0224 | 20.64 / 0.0122 | 29.79 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.97 / 0.0533 | 36.83 / 0.0224 | 20.66 / 0.0116 | 29.80 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.94 / 0.0528 | 36.83 / 0.0224 | 20.66 / 0.0112 | 29.79 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.37 / 0.0602 | 36.83 / 0.0224 | 20.31 / 0.0119 | 29.58 / 0.0396 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.68 / 0.0561 | 36.83 / 0.0224 | 20.82 / 0.0107 | 29.59 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.67 / 0.0585 | 36.83 / 0.0224 | 20.72 / 0.0111 | 29.62 / 0.0392 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.69 / 0.0571 | 36.83 / 0.0224 | 20.81 / 0.0108 | 29.60 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.02 / 0.0537 | 36.83 / 0.0224 | 21.21 / 0.0092 | 29.73 / 0.0385 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.08 / 0.0509 | 36.83 / 0.0224 | 21.38 / 0.0086 | 29.71 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.09 / 0.0520 | 36.83 / 0.0224 | 21.39 / 0.0086 | 29.72 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.08 / 0.0513 | 36.83 / 0.0224 | 21.40 / 0.0086 | 29.71 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.74 / 0.0575 | 36.83 / 0.0224 | 20.69 / 0.0123 | 29.70 / 0.0383 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.99 / 0.0515 | 36.91 / 0.0241 | 20.63 / 0.0091 | 29.80 / 0.0372 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.07 / 0.0502 | 36.91 / 0.0239 | 20.85 / 0.0086 | 29.80 / 0.0372 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.03 / 0.0511 | 36.92 / 0.0240 | 20.77 / 0.0089 | 29.80 / 0.0373 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.05 / 0.0506 | 36.92 / 0.0240 | 20.81 / 0.0087 | 29.80 / 0.0373 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.05 / 0.0516 | 36.91 / 0.0236 | 20.87 / 0.0088 | 29.78 / 0.0374 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.12 / 0.0508 | 36.90 / 0.0233 | 20.94 / 0.0086 | 29.79 / 0.0373 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.09 / 0.0512 | 36.91 / 0.0234 | 20.93 / 0.0086 | 29.77 / 0.0375 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.10 / 0.0509 | 36.90 / 0.0234 | 20.94 / 0.0085 | 29.78 / 0.0374 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.4%） | — | — | 28.06 / 0.0495 | 36.83 / 0.0224 | 29.80 |
| in035 | rife | 1.4% | 2.7% | 27.99 / 0.0515 | 36.91 / 0.0241 | 29.80 |
| in035 | cnw_cnn | 2.2% | 3.3% | 28.07 / 0.0524 | 36.83 / 0.0224 | 29.78 |
| in035 | cnw_f5 | 5.1% | 7.8% | 27.37 / 0.0602 | 36.83 / 0.0224 | 29.58 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.36 / 0.0502 | -0.01 / +0.0022 (core 1.3%) | -0.01 / +0.0034 (core 1.9%) | -0.74 / +0.0124 (core 5.5%) |
| in035 | 2 | 0-3 | 28.55 / 0.0486 | +0.01 / +0.0023 (core 1.3%) | +0.01 / +0.0026 (core 1.9%) | -0.87 / +0.0136 (core 5.5%) |
| in035 | 4 | 3-5 | 28.27 / 0.0497 | -0.19 / +0.0015 (core 0.9%) | +0.03 / +0.0028 (core 1.8%) | -0.47 / +0.0062 (core 3.4%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.06 / 0.0495 | — | 29.80 | — |
| in035 | cnw_cnn | 不复核 | —% | 28.07 / 0.0524 | — | 29.78 | 0/3 |
| in035 | cnw_cnn | oracle | 0.8% | 28.18 / 0.0502 | — | 29.80 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.07 / 0.0510 | — | 29.76 | 0/3 |
| in035 | cnw_cnn | oracle | 0.8% | 28.20 / 0.0496 | — | 29.80 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.16 / 0.0513 | — | 29.79 | 0/3 |
| in035 | cnw_cnn | oracle | 0.8% | 28.23 / 0.0497 | — | 29.80 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.11 / 0.0510 | — | 29.78 | 0/3 |
| in035 | cnw_cnn | oracle | 0.8% | 28.22 / 0.0496 | — | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.01 / 0.0518 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.8% | 28.17 / 0.0500 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.00 / 0.0506 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.8% | 28.17 / 0.0495 | — | 29.80 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.06 / 0.0512 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.8% | 28.20 / 0.0497 | — | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.04 / 0.0508 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.8% | 28.19 / 0.0496 | — | 29.80 | 1/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 28.03 / 0.0535 | — | 29.81 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 0.9% | 28.04 / 0.0528 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 28.06 / 0.0539 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 0.8% | 28.12 / 0.0523 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 28.08 / 0.0524 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 0.5% | 28.13 / 0.0516 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.91 / 0.0566 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 0.8% | 28.02 / 0.0538 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.94 / 0.0548 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 0.6% | 28.03 / 0.0532 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.99 / 0.0515 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 0.9% | 28.03 / 0.0510 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.00 / 0.0534 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 0.8% | 28.10 / 0.0517 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.06 / 0.0522 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.6% | 28.12 / 0.0513 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.91 / 0.0545 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 0.8% | 28.03 / 0.0524 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.97 / 0.0533 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 0.6% | 28.04 / 0.0520 | — | 29.80 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.94 / 0.0528 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 0.9% | 28.05 / 0.0513 | — | 29.80 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.37 / 0.0602 | — | 29.58 | 0/3 |
| in035 | cnw_f5 | oracle | 1.4% | 27.87 / 0.0528 | — | 29.79 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.68 / 0.0561 | — | 29.59 | 0/3 |
| in035 | cnw_f5 | oracle | 1.4% | 28.08 / 0.0512 | — | 29.80 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.67 / 0.0585 | — | 29.62 | 0/3 |
| in035 | cnw_f5 | oracle | 1.4% | 28.05 / 0.0521 | — | 29.80 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.69 / 0.0571 | — | 29.60 | 0/3 |
| in035 | cnw_f5 | oracle | 1.4% | 28.08 / 0.0515 | — | 29.80 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.02 / 0.0537 | — | 29.73 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.4% | 28.24 / 0.0498 | — | 29.80 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.08 / 0.0509 | — | 29.71 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.4% | 28.30 / 0.0490 | — | 29.80 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.09 / 0.0520 | — | 29.72 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.4% | 28.31 / 0.0492 | — | 29.80 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.08 / 0.0513 | — | 29.71 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.4% | 28.31 / 0.0490 | — | 29.80 | 2/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.74 / 0.0575 | — | 29.70 | 0/3 |
| in035 | cnw_f5_pix | oracle | 1.5% | 28.05 / 0.0526 | — | 29.80 | 0/3 |
| in035 | rife | 不复核 | —% | 27.99 / 0.0515 | — | 29.80 | 0/3 |
| in035 | rife | oracle | 0.4% | 28.07 / 0.0495 | — | 29.80 | 2/3 |
| in035 | rife | 不复核 | —% | 28.07 / 0.0502 | — | 29.80 | 0/3 |
| in035 | rife | oracle | 0.4% | 28.14 / 0.0490 | — | 29.80 | 3/3 |
| in035 | rife | 不复核 | —% | 28.03 / 0.0511 | — | 29.80 | 0/3 |
| in035 | rife | oracle | 0.4% | 28.12 / 0.0493 | — | 29.80 | 2/3 |
| in035 | rife | 不复核 | —% | 28.05 / 0.0506 | — | 29.80 | 0/3 |
| in035 | rife | oracle | 0.4% | 28.13 / 0.0491 | — | 29.80 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.05 / 0.0516 | — | 29.78 | 0/3 |
| in035 | rife_mw | oracle | 0.4% | 28.16 / 0.0494 | — | 29.80 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.12 / 0.0508 | — | 29.79 | 0/3 |
| in035 | rife_mw | oracle | 0.4% | 28.19 / 0.0490 | — | 29.80 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.09 / 0.0512 | — | 29.77 | 0/3 |
| in035 | rife_mw | oracle | 0.4% | 28.19 / 0.0492 | — | 29.80 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.10 / 0.0509 | — | 29.78 | 0/3 |
| in035 | rife_mw | oracle | 0.4% | 28.19 / 0.0490 | — | 29.80 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.06 / 0.0495 | — / — | — |
| in035 | FF | 0（前馈） | 643×729（62%） | 27.74 | 28.07 / 0.0524 | — / — | 0/3 |
| in035 | 25 | 0.84 s | 643×729（62%） | 28.52 | 28.16 / 0.0513 | — / — | 0/3 |
| in035 | 50 | 1.68 s | 643×729（62%） | 28.82 | 28.11 / 0.0510 | — / — | 0/3 |
| in035 | 100 | 3.35 s | 643×729（62%） | 29.08 | 28.07 / 0.0510 | — / — | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.06 / 0.0495 | — / — | 29.80 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 28.07 / 0.0524 | — / — | 29.78 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.18 / 0.0502 | — / — | 29.80 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.16 / 0.0513 | — / — | 29.79 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.23 / 0.0497 | — / — | 29.80 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 28.11 / 0.0510 | — / — | 29.78 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.22 / 0.0496 | — / — | 29.80 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 28.07 / 0.0510 | — / — | 29.76 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.20 / 0.0496 | — / — | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 28.01 / 0.0518 | — / — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.17 / 0.0500 | — / — | 29.80 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.06 / 0.0512 | — / — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.20 / 0.0497 | — / — | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.04 / 0.0508 | — / — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.19 / 0.0496 | — / — | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.00 / 0.0506 | — / — | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.17 / 0.0495 | — / — | 29.80 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 27.37 / 0.0602 | — / — | 29.58 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.87 / 0.0528 | — / — | 29.79 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.67 / 0.0585 | — / — | 29.62 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 28.05 / 0.0521 | — / — | 29.80 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.69 / 0.0571 | — / — | 29.60 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.08 / 0.0515 | — / — | 29.80 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.68 / 0.0561 | — / — | 29.59 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.08 / 0.0512 | — / — | 29.80 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 28.02 / 0.0537 | — / — | 29.73 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.24 / 0.0498 | — / — | 29.80 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 28.09 / 0.0520 | — / — | 29.72 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.31 / 0.0492 | — / — | 29.80 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 28.08 / 0.0513 | — / — | 29.71 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.31 / 0.0490 | — / — | 29.80 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.08 / 0.0509 | — / — | 29.71 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.30 / 0.0490 | — / — | 29.80 | 3/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.99 / 0.0515 | — / — | 29.80 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.07 / 0.0495 | — / — | 29.80 | 2/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.03 / 0.0511 | — / — | 29.80 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.12 / 0.0493 | — / — | 29.80 | 2/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.05 / 0.0506 | — / — | 29.80 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.13 / 0.0491 | — / — | 29.80 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.07 / 0.0502 | — / — | 29.80 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.14 / 0.0490 | — / — | 29.80 | 3/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 28.05 / 0.0516 | — / — | 29.78 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.16 / 0.0494 | — / — | 29.80 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.09 / 0.0512 | — / — | 29.77 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.19 / 0.0492 | — / — | 29.80 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.10 / 0.0509 | — / — | 29.78 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.19 / 0.0490 | — / — | 29.80 | 2/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.12 / 0.0508 | — / — | 29.79 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.19 / 0.0490 | — / — | 29.80 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 36.83 / 0.0224 | 20.52 / 0.0092 | 29.80 / 0.0369 | 28.06 / 0.0495 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 3.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 36.83 | 0.9211 | 0.0224 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 9.03 | 0.2140 | 0.5840 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 9.00 | 0.2083 | 0.5855 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 9.00 | 0.2083 | 0.5855 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 8.99 | 0.2078 | 0.5855 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 8.99 | 0.2078 | 0.5855 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.20 | 0.5455 | 0.7057 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 7.90 | 0.0006 | 0.6119 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.24 | 0.6301 | 0.4767 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.52 | 0.6368 | 0.4681 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.34 | 0.6402 | 0.4743 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.43 | 0.6399 | 0.4697 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.77 | 0.6258 | 0.5056 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.00 | 0.6283 | 0.4794 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.85 | 0.6296 | 0.4981 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.91 | 0.6294 | 0.4878 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 36.83 | 0.9211 | 0.0224 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 36.91 | 0.9222 | 0.0241 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 36.91 | 0.9220 | 0.0239 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 36.92 | 0.9223 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 36.92 | 0.9221 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 36.91 | 0.9223 | 0.0236 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 36.90 | 0.9218 | 0.0233 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 36.91 | 0.9221 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 36.90 | 0.9220 | 0.0234 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.52 | 0.7206 | 0.0092 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.31 | 0.1972 | 0.1074 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.31 | 0.2076 | 0.1069 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.31 | 0.2093 | 0.1069 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.31 | 0.2093 | 0.1068 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.45 | 0.1570 | 0.0785 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.46 | 0.1617 | 0.0779 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.46 | 0.1614 | 0.0781 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.46 | 0.1621 | 0.0779 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 9.13 | 0.1332 | 0.0685 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 9.15 | 0.1427 | 0.0682 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 9.15 | 0.1427 | 0.0682 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 9.13 | 0.1263 | 0.0700 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 9.13 | 0.1263 | 0.0700 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 8.89 | 0.1205 | 0.0708 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 8.91 | 0.1269 | 0.0718 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 8.91 | 0.1269 | 0.0718 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 8.90 | 0.1169 | 0.0727 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 8.90 | 0.1169 | 0.0727 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 8.90 | 0.1175 | 0.0714 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.38 | 0.2594 | 0.0865 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.42 | 0.2881 | 0.0840 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.40 | 0.2858 | 0.0852 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.41 | 0.2897 | 0.0846 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.43 | 0.3245 | 0.0831 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.44 | 0.3243 | 0.0818 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.43 | 0.3284 | 0.0823 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.43 | 0.3273 | 0.0820 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 9.94 | 0.2449 | 0.0564 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.71 | 0.1192 | 0.1104 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.74 | 0.1411 | 0.1076 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.72 | 0.1305 | 0.1097 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.72 | 0.1361 | 0.1091 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.71 | 0.1414 | 0.1102 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.72 | 0.1482 | 0.1089 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.71 | 0.1482 | 0.1096 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.72 | 0.1491 | 0.1092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.97 | 0.7401 | 0.0093 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.03 | 0.7488 | 0.0092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.12 | 0.7501 | 0.0089 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.08 | 0.7502 | 0.0090 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.00 | 0.7449 | 0.0096 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.98 | 0.7473 | 0.0092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.07 | 0.7482 | 0.0093 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.04 | 0.7483 | 0.0092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.52 | 0.7242 | 0.0127 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.82 | 0.7370 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.83 | 0.7377 | 0.0113 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.62 | 0.7234 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.62 | 0.7244 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.54 | 0.7221 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.77 | 0.7322 | 0.0112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.81 | 0.7350 | 0.0108 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.64 | 0.7217 | 0.0121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.67 | 0.7232 | 0.0116 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.67 | 0.7236 | 0.0112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 20.32 | 0.7159 | 0.0118 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.82 | 0.7400 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.72 | 0.7355 | 0.0111 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.81 | 0.7398 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.21 | 0.7594 | 0.0092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.38 | 0.7700 | 0.0086 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.39 | 0.7719 | 0.0086 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.40 | 0.7720 | 0.0086 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.69 | 0.7281 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.63 | 0.7321 | 0.0092 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.85 | 0.7474 | 0.0086 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.77 | 0.7402 | 0.0089 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.81 | 0.7442 | 0.0087 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.87 | 0.7486 | 0.0088 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.94 | 0.7518 | 0.0086 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.93 | 0.7528 | 0.0086 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.93 | 0.7529 | 0.0086 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.96 | 0.7392 | 0.0094 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.02 | 0.7481 | 0.0092 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.12 | 0.7495 | 0.0089 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.07 | 0.7495 | 0.0090 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.00 | 0.7442 | 0.0096 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.97 | 0.7465 | 0.0092 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.06 | 0.7476 | 0.0093 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.03 | 0.7477 | 0.0092 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.53 | 0.7240 | 0.0127 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.81 | 0.7359 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.82 | 0.7370 | 0.0114 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.62 | 0.7226 | 0.0132 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.62 | 0.7239 | 0.0126 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.54 | 0.7216 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.76 | 0.7310 | 0.0113 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.81 | 0.7343 | 0.0109 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.64 | 0.7209 | 0.0122 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.66 | 0.7227 | 0.0116 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.66 | 0.7223 | 0.0112 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 20.31 | 0.7139 | 0.0119 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.82 | 0.7388 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.72 | 0.7343 | 0.0111 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.81 | 0.7386 | 0.0108 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.21 | 0.7592 | 0.0092 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.38 | 0.7699 | 0.0086 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.39 | 0.7718 | 0.0086 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.40 | 0.7719 | 0.0086 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.69 | 0.7269 | 0.0123 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.63 | 0.7318 | 0.0091 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.85 | 0.7475 | 0.0086 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.77 | 0.7402 | 0.0089 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.81 | 0.7443 | 0.0087 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.87 | 0.7485 | 0.0088 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.94 | 0.7520 | 0.0086 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.93 | 0.7529 | 0.0086 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.94 | 0.7531 | 0.0085 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 20.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.49 | 0.7628 | 0.0153 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.67 | 0.4214 | 0.2072 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.71 | 0.4287 | 0.2041 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.69 | 0.4340 | 0.2052 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.70 | 0.4318 | 0.2045 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.44 | 0.2691 | 0.1735 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.61 | 0.2847 | 0.1672 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.49 | 0.2770 | 0.1716 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.56 | 0.2795 | 0.1700 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 12.72 | 0.3526 | 0.1337 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 12.69 | 0.3369 | 0.1395 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 12.69 | 0.3369 | 0.1395 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 12.65 | 0.3214 | 0.1447 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 12.65 | 0.3214 | 0.1447 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.78 | 0.2650 | 0.1447 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.75 | 0.2436 | 0.1523 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.75 | 0.2436 | 0.1523 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.74 | 0.2336 | 0.1542 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.74 | 0.2336 | 0.1542 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.67 | 0.2168 | 0.1542 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.38 | 0.4776 | 0.1685 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.45 | 0.5024 | 0.1618 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.41 | 0.5038 | 0.1658 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.43 | 0.5056 | 0.1636 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.34 | 0.5175 | 0.1642 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.45 | 0.5246 | 0.1574 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.37 | 0.5271 | 0.1614 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.40 | 0.5268 | 0.1592 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.61 | 0.3468 | 0.1311 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.48 | 0.3730 | 0.2040 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.64 | 0.3928 | 0.1961 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.50 | 0.3882 | 0.2020 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.53 | 0.3906 | 0.2001 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.43 | 0.3824 | 0.2058 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.51 | 0.3907 | 0.1992 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.45 | 0.3945 | 0.2032 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.47 | 0.3938 | 0.2014 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.89 | 0.7690 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.96 | 0.7726 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.08 | 0.7738 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.03 | 0.7736 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.79 | 0.7666 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.81 | 0.7692 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.94 | 0.7699 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.90 | 0.7699 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.39 | 0.7610 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.65 | 0.7642 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.69 | 0.7660 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.35 | 0.7570 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.38 | 0.7585 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.39 | 0.7603 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.60 | 0.7622 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.67 | 0.7643 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.39 | 0.7564 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.44 | 0.7581 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.41 | 0.7572 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.06 | 0.7555 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.71 | 0.7679 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.58 | 0.7660 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.71 | 0.7681 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.09 | 0.7750 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.31 | 0.7808 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.32 | 0.7811 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.33 | 0.7816 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.36 | 0.7558 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.50 | 0.7651 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.76 | 0.7731 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.68 | 0.7700 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.72 | 0.7720 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.84 | 0.7728 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.95 | 0.7754 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.95 | 0.7759 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.96 | 0.7760 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.49 | 0.7580 | 0.0178 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.52 | 0.7620 | 0.0169 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.76 | 0.7661 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.62 | 0.7641 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.05 | 0.7478 | 0.0189 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.60 | 0.7493 | 0.0192 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.15 | 0.7524 | 0.0186 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.76 | 0.7502 | 0.0195 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.29 | 0.7565 | 0.0204 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.35 | 0.7535 | 0.0219 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.53 | 0.7625 | 0.0189 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.88 | 0.7404 | 0.0256 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.08 | 0.7514 | 0.0218 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.23 | 0.7554 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.17 | 0.7482 | 0.0214 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.40 | 0.7574 | 0.0193 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.86 | 0.7388 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.09 | 0.7499 | 0.0202 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.31 | 0.7304 | 0.0232 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.92 | 0.7241 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.81 | 0.7455 | 0.0215 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.72 | 0.7442 | 0.0235 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.83 | 0.7466 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.22 | 0.7557 | 0.0209 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.20 | 0.7631 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.30 | 0.7643 | 0.0196 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.19 | 0.7641 | 0.0191 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.46 | 0.7037 | 0.0325 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.23 | 0.7613 | 0.0183 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.47 | 0.7715 | 0.0183 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.40 | 0.7697 | 0.0184 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.44 | 0.7716 | 0.0180 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.57 | 0.7711 | 0.0179 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.68 | 0.7735 | 0.0184 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.71 | 0.7767 | 0.0175 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.72 | 0.7759 | 0.0177 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 38.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.02 | 0.7079 | 0.0258 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.84 | 0.3070 | 0.3717 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.86 | 0.3112 | 0.3680 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.85 | 0.3144 | 0.3698 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.85 | 0.3131 | 0.3688 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.18 | 0.2060 | 0.2996 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.09 | 0.2062 | 0.2980 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.17 | 0.2082 | 0.2987 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.13 | 0.2072 | 0.2979 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.03 | 0.3062 | 0.2155 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.02 | 0.3011 | 0.2200 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.02 | 0.3011 | 0.2200 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.00 | 0.2951 | 0.2246 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.00 | 0.2951 | 0.2246 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.09 | 0.1758 | 0.2419 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.08 | 0.1706 | 0.2468 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.08 | 0.1706 | 0.2468 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.08 | 0.1676 | 0.2479 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.08 | 0.1676 | 0.2479 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.07 | 0.1658 | 0.2456 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.08 | 0.3829 | 0.3327 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.11 | 0.3956 | 0.3242 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.09 | 0.3975 | 0.3290 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.09 | 0.3977 | 0.3264 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.11 | 0.4122 | 0.3241 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.18 | 0.4122 | 0.3165 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.12 | 0.4158 | 0.3219 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.14 | 0.4138 | 0.3193 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.59 | 0.2988 | 0.2137 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.75 | 0.2796 | 0.3742 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.83 | 0.2894 | 0.3683 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.76 | 0.2869 | 0.3724 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.78 | 0.2883 | 0.3709 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.74 | 0.2843 | 0.3755 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.75 | 0.2885 | 0.3718 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.74 | 0.2899 | 0.3739 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.74 | 0.2895 | 0.3729 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.25 | 0.7103 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.29 | 0.7117 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.36 | 0.7123 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.34 | 0.7122 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.23 | 0.7103 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.22 | 0.7107 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.31 | 0.7112 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.28 | 0.7111 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.96 | 0.7075 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.08 | 0.7084 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.09 | 0.7088 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.87 | 0.7052 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.88 | 0.7057 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.95 | 0.7070 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.03 | 0.7075 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.07 | 0.7081 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.90 | 0.7050 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.92 | 0.7055 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.96 | 0.7060 | 0.0278 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.66 | 0.7037 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.09 | 0.7090 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.02 | 0.7084 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.10 | 0.7092 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.35 | 0.7133 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.50 | 0.7155 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.49 | 0.7159 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.50 | 0.7159 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.94 | 0.7062 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.05 | 0.7096 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.21 | 0.7127 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.16 | 0.7116 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.19 | 0.7123 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.25 | 0.7125 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.33 | 0.7136 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.32 | 0.7138 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.33 | 0.7138 | 0.0254 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.02 | 0.7073 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.08 | 0.7094 | 0.0269 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.22 | 0.7112 | 0.0269 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.14 | 0.7104 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.91 | 0.7062 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.92 | 0.7066 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.03 | 0.7078 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.99 | 0.7075 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.93 | 0.7069 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.95 | 0.7067 | 0.0304 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.00 | 0.7077 | 0.0289 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.66 | 0.7020 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.73 | 0.7038 | 0.0309 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.87 | 0.7059 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.84 | 0.7047 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.95 | 0.7064 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.68 | 0.7017 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.78 | 0.7036 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.74 | 0.7027 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.82 | 0.6910 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.45 | 0.7007 | 0.0311 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.40 | 0.7003 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.47 | 0.7014 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.93 | 0.7095 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.10 | 0.7119 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.10 | 0.7138 | 0.0274 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.09 | 0.7130 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.40 | 0.6974 | 0.0336 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.89 | 0.7088 | 0.0278 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.06 | 0.7134 | 0.0264 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.98 | 0.7121 | 0.0273 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.01 | 0.7130 | 0.0268 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.04 | 0.7118 | 0.0280 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.18 | 0.7134 | 0.0272 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.12 | 0.7138 | 0.0276 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.15 | 0.7137 | 0.0273 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 82.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.80 | 0.7219 | 0.0369 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.39 | 0.2809 | 0.4257 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.40 | 0.2804 | 0.4224 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.39 | 0.2827 | 0.4243 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.40 | 0.2817 | 0.4234 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.39 | 0.1540 | 0.3669 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.34 | 0.1522 | 0.3652 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.37 | 0.1537 | 0.3665 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.35 | 0.1526 | 0.3658 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.02 | 0.2988 | 0.3078 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 13.02 | 0.2976 | 0.3091 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 13.02 | 0.2976 | 0.3091 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 13.02 | 0.2968 | 0.3103 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 13.02 | 0.2968 | 0.3103 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.71 | 0.1020 | 0.3228 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.70 | 0.1014 | 0.3239 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.70 | 0.1014 | 0.3239 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.70 | 0.1009 | 0.3242 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.70 | 0.1009 | 0.3242 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.68 | 0.0974 | 0.3233 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.14 | 0.3380 | 0.3936 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.16 | 0.3383 | 0.3841 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.15 | 0.3424 | 0.3895 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.15 | 0.3404 | 0.3868 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.16 | 0.3424 | 0.3875 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.28 | 0.3423 | 0.3800 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.17 | 0.3431 | 0.3847 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.20 | 0.3421 | 0.3818 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.39 | 0.1881 | 0.2933 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.24 | 0.2665 | 0.4291 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.29 | 0.2691 | 0.4245 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.25 | 0.2687 | 0.4281 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.26 | 0.2689 | 0.4268 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.23 | 0.2672 | 0.4293 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.24 | 0.2679 | 0.4267 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.23 | 0.2687 | 0.4283 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.23 | 0.2684 | 0.4274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.79 | 0.7218 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.80 | 0.7219 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.80 | 0.7219 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.80 | 0.7219 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.78 | 0.7221 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.76 | 0.7220 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.79 | 0.7223 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.78 | 0.7221 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.77 | 0.7219 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7218 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.77 | 0.7220 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.77 | 0.7219 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.81 | 0.7221 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.80 | 0.7222 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.80 | 0.7220 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.80 | 0.7219 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.80 | 0.7221 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.79 | 0.7221 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.80 | 0.7219 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.79 | 0.7220 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.80 | 0.7219 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.79 | 0.7222 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.58 | 0.7209 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.59 | 0.7212 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.62 | 0.7217 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.60 | 0.7214 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.73 | 0.7220 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7219 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.72 | 0.7223 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.71 | 0.7222 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.70 | 0.7219 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.80 | 0.7219 | 0.0372 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.80 | 0.7220 | 0.0372 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.80 | 0.7220 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.80 | 0.7220 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.78 | 0.7219 | 0.0374 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.79 | 0.7218 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.77 | 0.7218 | 0.0375 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.78 | 0.7218 | 0.0374 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.06 | 0.7258 | 0.0495 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.64 | 0.2858 | 0.4823 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.65 | 0.2866 | 0.4753 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.64 | 0.2893 | 0.4788 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.64 | 0.2881 | 0.4769 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.43 | 0.1704 | 0.4350 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.37 | 0.1695 | 0.4311 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.41 | 0.1709 | 0.4335 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.39 | 0.1699 | 0.4321 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 12.72 | 0.2965 | 0.3884 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 12.71 | 0.2941 | 0.3924 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 12.71 | 0.2941 | 0.3924 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 12.71 | 0.2914 | 0.3971 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 12.71 | 0.2914 | 0.3971 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.59 | 0.1230 | 0.3984 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.58 | 0.1208 | 0.4031 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.58 | 0.1208 | 0.4031 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.58 | 0.1193 | 0.4040 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.58 | 0.1193 | 0.4040 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.56 | 0.1163 | 0.4019 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.47 | 0.3441 | 0.4421 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.49 | 0.3486 | 0.4260 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.48 | 0.3521 | 0.4351 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.48 | 0.3508 | 0.4304 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.48 | 0.3581 | 0.4276 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.59 | 0.3580 | 0.4163 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.49 | 0.3596 | 0.4226 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.53 | 0.3583 | 0.4184 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.42 | 0.2152 | 0.3521 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.46 | 0.2626 | 0.4904 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.52 | 0.2675 | 0.4825 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.47 | 0.2664 | 0.4883 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.48 | 0.2670 | 0.4861 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.45 | 0.2647 | 0.4903 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.46 | 0.2666 | 0.4858 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.45 | 0.2674 | 0.4884 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.45 | 0.2672 | 0.4869 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.18 | 0.7267 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.20 | 0.7271 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.23 | 0.7274 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.22 | 0.7273 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.17 | 0.7266 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.17 | 0.7268 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.20 | 0.7270 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.19 | 0.7270 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.04 | 0.7257 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.12 | 0.7262 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.13 | 0.7263 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.02 | 0.7250 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.03 | 0.7251 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.03 | 0.7255 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.10 | 0.7258 | 0.0517 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.12 | 0.7260 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.03 | 0.7249 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.04 | 0.7250 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.05 | 0.7251 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.87 | 0.7240 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.08 | 0.7260 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.05 | 0.7258 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.08 | 0.7261 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.24 | 0.7281 | 0.0498 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.30 | 0.7288 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.31 | 0.7291 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.31 | 0.7290 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.05 | 0.7252 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.07 | 0.7266 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.14 | 0.7276 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.12 | 0.7272 | 0.0493 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.13 | 0.7275 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.16 | 0.7275 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.19 | 0.7279 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.19 | 0.7280 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.19 | 0.7280 | 0.0490 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.07 | 0.7255 | 0.0524 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.07 | 0.7261 | 0.0510 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.16 | 0.7270 | 0.0513 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.11 | 0.7266 | 0.0510 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.01 | 0.7250 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.00 | 0.7250 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.06 | 0.7257 | 0.0512 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.04 | 0.7254 | 0.0508 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.03 | 0.7255 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.06 | 0.7255 | 0.0539 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.08 | 0.7259 | 0.0524 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.91 | 0.7237 | 0.0566 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.94 | 0.7243 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.99 | 0.7251 | 0.0515 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.00 | 0.7247 | 0.0534 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.06 | 0.7254 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.91 | 0.7235 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.97 | 0.7242 | 0.0533 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.94 | 0.7238 | 0.0528 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.37 | 0.7184 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.68 | 0.7221 | 0.0561 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.67 | 0.7223 | 0.0585 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.69 | 0.7225 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.02 | 0.7264 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.08 | 0.7272 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.09 | 0.7282 | 0.0520 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.08 | 0.7278 | 0.0513 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.74 | 0.7216 | 0.0575 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.99 | 0.7263 | 0.0515 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.07 | 0.7280 | 0.0502 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.03 | 0.7276 | 0.0511 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.05 | 0.7278 | 0.0506 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.05 | 0.7273 | 0.0516 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.12 | 0.7279 | 0.0508 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.09 | 0.7280 | 0.0512 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.10 | 0.7280 | 0.0509 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 813 | None | classic | 0.99 | False | 138635 | 0.323 | 61.7 | 29.21 | 0.48 | 0.011 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 813 | None | classic | 0.99 | False | 138635 | 0.323 | 60.8 | 29.21 | 0.48 | 0.011 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 813 | None | classic | 0.99 | False | 138635 | 0.323 | 58.2 | 29.21 | 0.48 | 0.011 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 813 | None | classic | 0.99 | False | 138635 | 0.323 | 54.3 | 29.21 | 0.48 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 628 | None | classic | 0.30 | False | 532902 | 1.009 | 169.1 | 30.29 | 0.25 | 0.026 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 628 | None | classic | 0.30 | False | 532902 | 1.009 | 155.1 | 30.29 | 0.25 | 0.026 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 628 | None | classic | 0.30 | False | 532902 | 1.009 | 157.8 | 30.29 | 0.25 | 0.026 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 628 | None | classic | 0.30 | False | 532902 | 1.009 | 141.0 | 30.29 | 0.25 | 0.026 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 434477 | 0.187 | 29.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 432993 | 0.791 | 32.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 432993 | 0.791 | 32.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 432993 | 0.599 | 26.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 432993 | 0.599 | 26.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 434477 | 0.187 | 34.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 432993 | 0.791 | 179.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 432993 | 0.791 | 179.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 432993 | 0.599 | 34.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 432993 | 0.599 | 34.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 433083 | 0.791 | 436.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1123 | None | classic | 1.89 | False | 243435 | 0.324 | 70.2 | 29.86 | 0.07 | 0.013 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1123 | None | classic | 1.89 | False | 243435 | 0.324 | 46.0 | 29.86 | 0.07 | 0.013 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1123 | None | classic | 1.89 | False | 243435 | 0.324 | 74.6 | 29.86 | 0.07 | 0.013 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1123 | None | classic | 1.89 | False | 243435 | 0.324 | 53.5 | 29.86 | 0.07 | 0.013 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 646 | None | classic | 0.53 | False | 411372 | 0.986 | 176.7 | 30.69 | 0.24 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 646 | None | classic | 0.53 | False | 411372 | 0.986 | 164.3 | 30.69 | 0.24 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 646 | None | classic | 0.53 | False | 411372 | 0.986 | 162.3 | 30.69 | 0.24 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 646 | None | classic | 0.53 | False | 411372 | 0.986 | 182.9 | 30.69 | 0.24 | 0.008 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 865499 | 0.791 | 87.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 827 | None | classic | 1.02 | False | 167009 | 0.907 | 82.2 | 28.67 | 0.09 | 0.015 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 827 | None | classic | 1.02 | False | 167009 | 0.907 | 73.3 | 28.67 | 0.09 | 0.015 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 827 | None | classic | 1.02 | False | 167009 | 0.907 | 82.4 | 28.67 | 0.09 | 0.015 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 827 | None | classic | 1.02 | False | 167009 | 0.907 | 60.5 | 28.67 | 0.09 | 0.015 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 629 | None | classic | 0.59 | False | 467540 | 0.648 | 100.7 | 31.39 | 0.32 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 629 | None | classic | 0.59 | False | 467540 | 0.648 | 97.2 | 31.39 | 0.32 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 629 | None | classic | 0.59 | False | 467540 | 0.648 | 113.1 | 31.39 | 0.32 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 629 | None | classic | 0.59 | False | 467540 | 0.648 | 100.5 | 31.39 | 0.32 | 0.007 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.691 | 0.020 |
| in035 | mask_ent | 0.772 | 0.020 |
| in035 | mask_grad | 0.438 | 0.020 |
| in035 | r_col | 0.742 | 0.020 |
| in035 | r_warp | 0.815 | 0.020 |

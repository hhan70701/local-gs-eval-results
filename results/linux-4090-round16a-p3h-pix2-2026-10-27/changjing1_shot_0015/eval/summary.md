# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 6.0% | 24.82 / 0.0059 | 20.12 / 0.0152 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.3% | 24.89 / 0.0064 | 21.42 / 0.0128 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.1% | 24.84 / 0.0062 | 21.03 / 0.0139 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.2% | 24.86 / 0.0061 | 21.23 / 0.0132 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.8% | 24.61 / 0.0060 | 20.70 / 0.0129 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.0% | 24.75 / 0.0060 | 21.76 / 0.0099 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.8% | 24.66 / 0.0060 | 21.29 / 0.0107 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.9% | 24.68 / 0.0059 | 21.42 / 0.0102 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 5.4% | 24.28 / 0.0062 | 23.09 / 0.0171 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 5.0% | 24.17 / 0.0064 | 20.65 / 0.0175 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.1% | 20.91 / 0.0048 | 17.20 / 0.0134 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 5.0% | 24.25 / 0.0065 | 20.26 / 0.0196 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.1% | 21.80 / 0.0041 | 17.17 / 0.0131 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 5.4% | 24.24 / 0.0062 | 23.25 / 0.0113 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 5.0% | 24.07 / 0.0068 | 20.84 / 0.0159 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 1.9% | 20.50 / 0.0047 | 17.15 / 0.0106 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 5.0% | 24.16 / 0.0064 | 20.31 / 0.0176 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.1% | 21.46 / 0.0046 | 17.20 / 0.0124 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 6.7% | 24.94 / 0.0074 | 20.15 / 0.0264 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 11.9% | 25.64 / 0.0103 | 20.63 / 0.0336 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.4% | 25.71 / 0.0107 | 21.64 / 0.0281 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.1% | 25.68 / 0.0105 | 21.37 / 0.0313 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.2% | 25.69 / 0.0106 | 21.47 / 0.0297 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 11.8% | 25.61 / 0.0104 | 22.02 / 0.0236 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 12.1% | 25.69 / 0.0105 | 23.34 / 0.0181 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 11.8% | 25.63 / 0.0102 | 22.82 / 0.0201 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 11.9% | 25.65 / 0.0103 | 22.91 / 0.0191 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 12.4% | 25.67 / 0.0121 | 20.73 / 0.0440 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 6.1% | 25.41 / 0.0080 | 22.04 / 0.0214 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 6.8% | 25.64 / 0.0087 | 23.09 / 0.0207 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 6.5% | 25.60 / 0.0082 | 22.93 / 0.0204 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 6.6% | 25.60 / 0.0085 | 23.08 / 0.0202 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 6.9% | 25.66 / 0.0087 | 23.56 / 0.0183 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 7.5% | 25.90 / 0.0088 | 23.89 / 0.0190 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 7.2% | 25.80 / 0.0088 | 24.38 / 0.0182 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 7.3% | 25.82 / 0.0088 | 24.48 / 0.0171 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.08 / 0.0539 | 27.87 / 0.0483 | 20.66 / 0.0139 | 29.61 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.59 / 0.0602 | 28.77 / 0.0737 | 20.59 / 0.0148 | 29.49 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.88 / 0.0585 | 29.42 / 0.0588 | 20.82 / 0.0139 | 29.54 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.81 / 0.0594 | 29.42 / 0.0653 | 20.73 / 0.0143 | 29.55 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.84 / 0.0589 | 29.43 / 0.0616 | 20.75 / 0.0141 | 29.55 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.63 / 0.0568 | 27.48 / 0.0600 | 21.04 / 0.0135 | 29.43 / 0.0377 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 / 0.0552 | 28.92 / 0.0500 | 21.33 / 0.0131 | 29.49 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.79 / 0.0561 | 28.46 / 0.0573 | 21.13 / 0.0133 | 29.48 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.83 / 0.0559 | 28.73 / 0.0540 | 21.19 / 0.0133 | 29.48 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.06 / 0.0582 | 27.36 / 0.0819 | 20.63 / 0.0168 | 29.62 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.58 / 0.0594 | 27.78 / 0.0550 | 20.16 / 0.0168 | 29.58 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.59 / 0.0583 | 27.64 / 0.0525 | 20.14 / 0.0166 | 29.57 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.60 / 0.0600 | 27.68 / 0.0556 | 20.08 / 0.0168 | 29.59 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.61 / 0.0584 | 27.61 / 0.0523 | 20.10 / 0.0166 | 29.59 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.10 / 0.0545 | 27.55 / 0.0594 | 20.74 / 0.0140 | 29.61 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.61 / 0.0579 | 27.79 / 0.0544 | 20.14 / 0.0155 | 29.59 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.62 / 0.0562 | 27.68 / 0.0499 | 20.15 / 0.0153 | 29.58 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.61 / 0.0583 | 27.75 / 0.0610 | 20.05 / 0.0159 | 29.60 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.62 / 0.0568 | 27.64 / 0.0523 | 20.07 / 0.0158 | 29.60 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.77 / 0.0591 | 26.49 / 0.1094 | 20.60 / 0.0150 | 29.58 / 0.0375 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.83 / 0.0736 | 26.43 / 0.1165 | 20.21 / 0.0182 | 29.13 / 0.0422 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.14 / 0.0683 | 27.97 / 0.0836 | 20.45 / 0.0168 | 29.33 / 0.0402 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.06 / 0.0710 | 27.80 / 0.0999 | 20.38 / 0.0174 | 29.28 / 0.0410 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.09 / 0.0696 | 27.87 / 0.0923 | 20.39 / 0.0172 | 29.32 / 0.0405 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.38 / 0.0643 | 25.46 / 0.0891 | 20.67 / 0.0157 | 29.29 / 0.0397 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.88 / 0.0592 | 29.01 / 0.0614 | 21.38 / 0.0136 | 29.45 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.69 / 0.0621 | 27.54 / 0.0776 | 20.99 / 0.0147 | 29.42 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.79 / 0.0607 | 28.40 / 0.0693 | 21.21 / 0.0141 | 29.44 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.29 / 0.0650 | 24.96 / 0.1595 | 20.35 / 0.0176 | 29.47 / 0.0389 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.85 / 0.0613 | 27.49 / 0.1065 | 20.93 / 0.0147 | 29.53 / 0.0371 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.02 / 0.0591 | 28.71 / 0.0771 | 21.14 / 0.0136 | 29.56 / 0.0368 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.96 / 0.0608 | 28.47 / 0.0899 | 21.06 / 0.0144 | 29.57 / 0.0370 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.99 / 0.0600 | 28.54 / 0.0834 | 21.08 / 0.0141 | 29.57 / 0.0369 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.22 / 0.0578 | 25.64 / 0.0997 | 21.53 / 0.0130 | 29.56 / 0.0371 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.24 / 0.0558 | 28.06 / 0.0778 | 21.66 / 0.0125 | 29.56 / 0.0367 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.23 / 0.0573 | 26.98 / 0.0978 | 21.66 / 0.0128 | 29.57 / 0.0370 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.23 / 0.0566 | 27.69 / 0.0872 | 21.70 / 0.0126 | 29.57 / 0.0369 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.7%） | — | — | 28.08 / 0.0539 | 27.87 / 0.0483 | 29.61 |
| in035 | rife | 2.8% | 6.1% | 27.85 / 0.0613 | 27.49 / 0.1065 | 29.53 |
| in035 | cnw_cnn | 3.4% | 6.0% | 27.59 / 0.0602 | 28.77 / 0.0737 | 29.49 |
| in035 | cnw_f5 | 6.9% | 11.9% | 26.83 / 0.0736 | 26.43 / 0.1165 | 29.13 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.40 / 0.0537 | -0.31 / +0.0089 (core 3.3%) | -0.33 / +0.0064 (core 4.0%) | -1.15 / +0.0232 (core 8.1%) |
| in035 | 2 | 0-3 | 27.60 / 0.0563 | -0.19 / +0.0089 (core 3.3%) | -0.59 / +0.0073 (core 4.0%) | -1.69 / +0.0256 (core 8.1%) |
| in035 | 4 | 3-5 | 29.23 / 0.0517 | -0.19 / +0.0042 (core 1.1%) | -0.53 / +0.0053 (core 1.5%) | -0.90 / +0.0102 (core 3.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.08 / 0.0539 | 27.87 | 29.61 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.59 / 0.0602 | 28.77 | 29.49 | 0/3 |
| in035 | cnw_cnn | oracle | 1.0% | 27.99 / 0.0549 | 29.23 | 29.60 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.88 / 0.0585 | 29.42 | 29.54 | 0/3 |
| in035 | cnw_cnn | oracle | 1.0% | 28.15 / 0.0541 | 29.38 | 29.61 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.81 / 0.0594 | 29.42 | 29.55 | 0/3 |
| in035 | cnw_cnn | oracle | 1.0% | 28.09 / 0.0546 | 29.33 | 29.61 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.84 / 0.0589 | 29.43 | 29.55 | 0/3 |
| in035 | cnw_cnn | oracle | 1.0% | 28.11 / 0.0545 | 29.34 | 29.61 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.63 / 0.0568 | 27.48 | 29.43 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.0% | 28.17 / 0.0533 | 28.33 | 29.60 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.95 / 0.0552 | 28.92 | 29.49 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.0% | 28.30 / 0.0529 | 29.09 | 29.61 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.79 / 0.0561 | 28.46 | 29.48 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.0% | 28.23 / 0.0530 | 28.83 | 29.60 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.83 / 0.0559 | 28.73 | 29.48 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.0% | 28.26 / 0.0530 | 28.97 | 29.60 | 2/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 28.06 / 0.0582 | 27.36 | 29.62 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 1.0% | 28.09 / 0.0567 | 28.02 | 29.61 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 27.58 / 0.0594 | 27.78 | 29.58 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 0.9% | 27.79 / 0.0564 | 27.80 | 29.61 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 27.59 / 0.0583 | 27.64 | 29.57 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 0.7% | 27.78 / 0.0561 | 27.69 | 29.61 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.60 / 0.0600 | 27.68 | 29.59 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 0.9% | 27.81 / 0.0565 | 27.80 | 29.61 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.61 / 0.0584 | 27.61 | 29.59 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 0.7% | 27.81 / 0.0562 | 27.76 | 29.61 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 28.10 / 0.0545 | 27.55 | 29.61 | 1/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 1.0% | 28.13 / 0.0537 | 28.15 | 29.61 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.61 / 0.0579 | 27.79 | 29.59 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 0.9% | 27.78 / 0.0551 | 27.81 | 29.61 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.62 / 0.0562 | 27.68 | 29.58 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.7% | 27.78 / 0.0548 | 27.72 | 29.61 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.61 / 0.0583 | 27.75 | 29.60 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 0.9% | 27.78 / 0.0554 | 27.82 | 29.61 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.62 / 0.0568 | 27.64 | 29.60 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 0.7% | 27.79 / 0.0552 | 27.78 | 29.61 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.77 / 0.0591 | 26.49 | 29.58 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.1% | 28.00 / 0.0546 | 28.16 | 29.61 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.83 / 0.0736 | 26.43 | 29.13 | 0/3 |
| in035 | cnw_f5 | oracle | 1.9% | 27.75 / 0.0595 | 27.30 | 29.58 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.14 / 0.0683 | 27.97 | 29.33 | 0/3 |
| in035 | cnw_f5 | oracle | 2.0% | 27.91 / 0.0575 | 27.98 | 29.59 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.06 / 0.0710 | 27.80 | 29.28 | 0/3 |
| in035 | cnw_f5 | oracle | 1.9% | 27.87 / 0.0587 | 27.83 | 29.59 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.09 / 0.0696 | 27.87 | 29.32 | 0/3 |
| in035 | cnw_f5 | oracle | 1.9% | 27.88 / 0.0582 | 27.83 | 29.59 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.38 / 0.0643 | 25.46 | 29.29 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.9% | 28.04 / 0.0558 | 26.75 | 29.57 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.88 / 0.0592 | 29.01 | 29.45 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.9% | 28.30 / 0.0537 | 29.55 | 29.60 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.69 / 0.0621 | 27.54 | 29.42 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.9% | 28.19 / 0.0550 | 28.12 | 29.59 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.79 / 0.0607 | 28.40 | 29.44 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.9% | 28.25 / 0.0544 | 28.94 | 29.59 | 1/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.29 / 0.0650 | 24.96 | 29.47 | 0/3 |
| in035 | cnw_f5_pix | oracle | 1.9% | 27.83 / 0.0571 | 27.88 | 29.60 | 0/3 |
| in035 | rife | 不复核 | —% | 27.85 / 0.0613 | 27.49 | 29.53 | 0/3 |
| in035 | rife | oracle | 1.1% | 28.17 / 0.0550 | 28.11 | 29.60 | 0/3 |
| in035 | rife | 不复核 | —% | 28.02 / 0.0591 | 28.71 | 29.56 | 0/3 |
| in035 | rife | oracle | 1.2% | 28.28 / 0.0536 | 28.70 | 29.60 | 2/3 |
| in035 | rife | 不复核 | —% | 27.96 / 0.0608 | 28.47 | 29.57 | 0/3 |
| in035 | rife | oracle | 1.2% | 28.24 / 0.0547 | 28.45 | 29.60 | 1/3 |
| in035 | rife | 不复核 | —% | 27.99 / 0.0600 | 28.54 | 29.57 | 0/3 |
| in035 | rife | oracle | 1.2% | 28.26 / 0.0541 | 28.47 | 29.60 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 28.22 / 0.0578 | 25.64 | 29.56 | 0/3 |
| in035 | rife_mw | oracle | 1.2% | 28.38 / 0.0532 | 27.32 | 29.59 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.24 / 0.0558 | 28.06 | 29.56 | 0/3 |
| in035 | rife_mw | oracle | 1.2% | 28.42 / 0.0524 | 29.20 | 29.61 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 28.23 / 0.0573 | 26.98 | 29.57 | 0/3 |
| in035 | rife_mw | oracle | 1.2% | 28.42 / 0.0529 | 28.11 | 29.60 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.23 / 0.0566 | 27.69 | 29.57 | 0/3 |
| in035 | rife_mw | oracle | 1.2% | 28.44 / 0.0526 | 28.80 | 29.60 | 3/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.08 / 0.0539 | 27.87 / 0.0483 | — |
| in035 | FF | 0（前馈） | 1008×691（65%） | 26.62 | 27.59 / 0.0602 | 28.77 / 0.0737 | 0/3 |
| in035 | 25 | 0.65 s | 1008×691（65%） | 26.98 | 27.81 / 0.0594 | 29.42 / 0.0653 | 0/3 |
| in035 | 50 | 1.28 s | 1008×691（65%） | 27.15 | 27.84 / 0.0589 | 29.43 / 0.0616 | 0/3 |
| in035 | 100 | 2.54 s | 1008×691（65%） | 27.33 | 27.88 / 0.0585 | 29.42 / 0.0588 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.08 / 0.0539 | 27.87 / 0.0483 | 29.61 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.59 / 0.0602 | 28.77 / 0.0737 | 29.49 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.99 / 0.0549 | 29.23 / 0.0454 | 29.60 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.81 / 0.0594 | 29.42 / 0.0653 | 29.55 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.09 / 0.0546 | 29.33 / 0.0442 | 29.61 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.84 / 0.0589 | 29.43 / 0.0616 | 29.55 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.11 / 0.0545 | 29.34 / 0.0434 | 29.61 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.88 / 0.0585 | 29.42 / 0.0588 | 29.54 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.15 / 0.0541 | 29.38 / 0.0428 | 29.61 | 2/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.63 / 0.0568 | 27.48 / 0.0600 | 29.43 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.17 / 0.0533 | 28.33 / 0.0448 | 29.60 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.79 / 0.0561 | 28.46 / 0.0573 | 29.48 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.23 / 0.0530 | 28.83 / 0.0440 | 29.60 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.83 / 0.0559 | 28.73 / 0.0540 | 29.48 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.26 / 0.0530 | 28.97 / 0.0435 | 29.60 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.95 / 0.0552 | 28.92 / 0.0500 | 29.49 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.30 / 0.0529 | 29.09 / 0.0423 | 29.61 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.83 / 0.0736 | 26.43 / 0.1165 | 29.13 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.75 / 0.0595 | 27.30 / 0.0697 | 29.58 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.06 / 0.0710 | 27.80 / 0.0999 | 29.28 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.87 / 0.0587 | 27.83 / 0.0676 | 29.59 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.09 / 0.0696 | 27.87 / 0.0923 | 29.32 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.88 / 0.0582 | 27.83 / 0.0658 | 29.59 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.14 / 0.0683 | 27.97 / 0.0836 | 29.33 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.91 / 0.0575 | 27.98 / 0.0581 | 29.59 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.38 / 0.0643 | 25.46 / 0.0891 | 29.29 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.04 / 0.0558 | 26.75 / 0.0541 | 29.57 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.69 / 0.0621 | 27.54 / 0.0776 | 29.42 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.19 / 0.0550 | 28.12 / 0.0491 | 29.59 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.79 / 0.0607 | 28.40 / 0.0693 | 29.44 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.25 / 0.0544 | 28.94 / 0.0454 | 29.59 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.88 / 0.0592 | 29.01 / 0.0614 | 29.45 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.30 / 0.0537 | 29.55 / 0.0427 | 29.60 | 2/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.85 / 0.0613 | 27.49 / 0.1065 | 29.53 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.17 / 0.0550 | 28.11 / 0.0604 | 29.60 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.96 / 0.0608 | 28.47 / 0.0899 | 29.57 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.24 / 0.0547 | 28.45 / 0.0539 | 29.60 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.99 / 0.0600 | 28.54 / 0.0834 | 29.57 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.26 / 0.0541 | 28.47 / 0.0515 | 29.60 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.02 / 0.0591 | 28.71 / 0.0771 | 29.56 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.28 / 0.0536 | 28.70 / 0.0491 | 29.60 | 2/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 28.22 / 0.0578 | 25.64 / 0.0997 | 29.56 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.38 / 0.0532 | 27.32 / 0.0537 | 29.59 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.23 / 0.0573 | 26.98 / 0.0978 | 29.57 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.42 / 0.0529 | 28.11 / 0.0551 | 29.60 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.23 / 0.0566 | 27.69 / 0.0872 | 29.57 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.44 / 0.0526 | 28.80 / 0.0496 | 29.60 | 3/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.24 / 0.0558 | 28.06 / 0.0778 | 29.56 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.42 / 0.0524 | 29.20 / 0.0480 | 29.61 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.87 / 0.0483 | 20.66 / 0.0139 | 29.61 / 0.0359 | 28.08 / 0.0539 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 2.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.87 | 0.8166 | 0.0483 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 19.92 | 0.7475 | 0.2101 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 21.46 | 0.7959 | 0.1647 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 20.86 | 0.7810 | 0.1941 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 21.09 | 0.7895 | 0.1839 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 19.33 | 0.7211 | 0.1827 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 21.61 | 0.7756 | 0.1359 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 20.50 | 0.7597 | 0.1654 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 21.13 | 0.7692 | 0.1499 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 26.35 | 0.7726 | 0.1191 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 26.90 | 0.8294 | 0.0882 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 26.90 | 0.8294 | 0.0882 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 27.04 | 0.8202 | 0.0818 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 27.04 | 0.8202 | 0.0818 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 22.29 | 0.7623 | 0.1620 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 23.27 | 0.7871 | 0.1609 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 23.27 | 0.7871 | 0.1609 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 23.43 | 0.7844 | 0.1611 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 23.43 | 0.7844 | 0.1611 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 21.34 | 0.7278 | 0.2382 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 25.32 | 0.7944 | 0.1483 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 27.51 | 0.8425 | 0.1040 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 27.12 | 0.8294 | 0.1293 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 27.29 | 0.8376 | 0.1198 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 24.29 | 0.7857 | 0.1145 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 27.90 | 0.8398 | 0.0743 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 26.38 | 0.8202 | 0.0935 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 27.27 | 0.8325 | 0.0821 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 24.54 | 0.7920 | 0.1835 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 25.84 | 0.8054 | 0.1371 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 27.75 | 0.8427 | 0.0969 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 27.34 | 0.8346 | 0.1166 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 27.58 | 0.8404 | 0.1079 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 23.93 | 0.7732 | 0.1295 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 26.78 | 0.8219 | 0.0897 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 25.51 | 0.8035 | 0.1177 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 26.34 | 0.8167 | 0.1025 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.23 | 0.8262 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.38 | 0.8297 | 0.0428 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.33 | 0.8279 | 0.0442 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.34 | 0.8288 | 0.0434 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.33 | 0.8185 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.09 | 0.8277 | 0.0423 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.83 | 0.8236 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.97 | 0.8257 | 0.0435 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.02 | 0.8132 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.80 | 0.8184 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.69 | 0.8151 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.80 | 0.8180 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.76 | 0.8152 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.15 | 0.8185 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.81 | 0.8206 | 0.0482 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.72 | 0.8165 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.82 | 0.8199 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.78 | 0.8166 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.16 | 0.8183 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.30 | 0.8057 | 0.0697 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.98 | 0.8211 | 0.0581 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.83 | 0.8139 | 0.0676 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.83 | 0.8179 | 0.0658 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.75 | 0.8097 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.55 | 0.8303 | 0.0427 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.12 | 0.8188 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.94 | 0.8251 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.88 | 0.8168 | 0.0652 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.11 | 0.8154 | 0.0604 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.70 | 0.8260 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.45 | 0.8209 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.47 | 0.8229 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.32 | 0.8062 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.20 | 0.8273 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.11 | 0.8137 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.80 | 0.8219 | 0.0496 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.77 | 0.8329 | 0.0737 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.42 | 0.8439 | 0.0588 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.42 | 0.8428 | 0.0653 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.43 | 0.8437 | 0.0616 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.48 | 0.8153 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.92 | 0.8402 | 0.0500 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.46 | 0.8335 | 0.0573 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.73 | 0.8376 | 0.0540 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.36 | 0.7949 | 0.0819 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.78 | 0.8265 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.64 | 0.8147 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.68 | 0.8213 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.61 | 0.8137 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.55 | 0.8156 | 0.0594 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.79 | 0.8304 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.68 | 0.8165 | 0.0499 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.75 | 0.8271 | 0.0610 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.64 | 0.8156 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.49 | 0.8125 | 0.1094 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.43 | 0.8136 | 0.1165 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.97 | 0.8438 | 0.0836 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.80 | 0.8370 | 0.0999 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.87 | 0.8416 | 0.0923 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.46 | 0.8058 | 0.0891 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.01 | 0.8485 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.54 | 0.8331 | 0.0776 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.40 | 0.8425 | 0.0693 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.96 | 0.7966 | 0.1595 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.49 | 0.8224 | 0.1065 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.71 | 0.8468 | 0.0771 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.47 | 0.8429 | 0.0899 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.54 | 0.8453 | 0.0834 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.64 | 0.7951 | 0.0997 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.06 | 0.8366 | 0.0778 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.98 | 0.8192 | 0.0978 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.69 | 0.8308 | 0.0872 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.66 | 0.6326 | 0.0139 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.26 | 0.2132 | 0.1394 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.31 | 0.2301 | 0.1358 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.27 | 0.2243 | 0.1382 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.29 | 0.2266 | 0.1373 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.25 | 0.2197 | 0.1389 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.30 | 0.2461 | 0.1362 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.26 | 0.2346 | 0.1378 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.28 | 0.2407 | 0.1373 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.16 | 0.2530 | 0.0693 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 12.93 | 0.2342 | 0.0711 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 12.93 | 0.2342 | 0.0711 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 12.94 | 0.2359 | 0.0710 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 12.94 | 0.2359 | 0.0710 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.05 | 0.1820 | 0.0843 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.92 | 0.1578 | 0.0887 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.92 | 0.1578 | 0.0887 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 10.93 | 0.1588 | 0.0890 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 10.93 | 0.1588 | 0.0890 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.94 | 0.1574 | 0.0871 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.91 | 0.3348 | 0.1048 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.02 | 0.3606 | 0.0997 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.97 | 0.3535 | 0.1025 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.99 | 0.3576 | 0.1013 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.06 | 0.3488 | 0.1021 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.11 | 0.3954 | 0.0975 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.09 | 0.3761 | 0.0994 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.10 | 0.3873 | 0.0984 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.16 | 0.3364 | 0.0644 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.28 | 0.2170 | 0.1413 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.35 | 0.2281 | 0.1384 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.31 | 0.2242 | 0.1404 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.33 | 0.2256 | 0.1396 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.28 | 0.2233 | 0.1393 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.36 | 0.2437 | 0.1370 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.30 | 0.2343 | 0.1386 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.32 | 0.2405 | 0.1378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.60 | 0.6394 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.82 | 0.6454 | 0.0138 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.73 | 0.6439 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.75 | 0.6440 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.06 | 0.6486 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.35 | 0.6642 | 0.0130 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.16 | 0.6577 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.21 | 0.6612 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.63 | 0.6266 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.17 | 0.6250 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.15 | 0.6245 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.08 | 0.6227 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.11 | 0.6220 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.74 | 0.6385 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.15 | 0.6298 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.16 | 0.6298 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.05 | 0.6279 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.08 | 0.6269 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.61 | 0.6325 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 20.22 | 0.6191 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.45 | 0.6321 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.39 | 0.6265 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.39 | 0.6286 | 0.0171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.71 | 0.6443 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.41 | 0.6763 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.06 | 0.6611 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.25 | 0.6698 | 0.0138 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.36 | 0.6210 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.94 | 0.6457 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.14 | 0.6519 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.07 | 0.6502 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 21.09 | 0.6505 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.53 | 0.6571 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.66 | 0.6694 | 0.0124 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.66 | 0.6659 | 0.0127 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.70 | 0.6696 | 0.0125 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.59 | 0.6385 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.82 | 0.6450 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.73 | 0.6433 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.75 | 0.6437 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.04 | 0.6469 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.33 | 0.6628 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.13 | 0.6562 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.19 | 0.6596 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.63 | 0.6259 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.16 | 0.6247 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.14 | 0.6243 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.08 | 0.6224 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.10 | 0.6215 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.74 | 0.6378 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.14 | 0.6293 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.15 | 0.6293 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.05 | 0.6271 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.07 | 0.6261 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.60 | 0.6303 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 20.21 | 0.6164 | 0.0182 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.45 | 0.6304 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.38 | 0.6245 | 0.0174 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.39 | 0.6269 | 0.0172 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.67 | 0.6414 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.38 | 0.6754 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.99 | 0.6589 | 0.0147 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.21 | 0.6684 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.35 | 0.6172 | 0.0176 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.93 | 0.6446 | 0.0147 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.14 | 0.6512 | 0.0136 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.06 | 0.6493 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 21.08 | 0.6498 | 0.0141 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.53 | 0.6554 | 0.0130 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.66 | 0.6686 | 0.0125 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.66 | 0.6646 | 0.0128 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.70 | 0.6686 | 0.0126 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 28.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.66 | 0.7605 | 0.0213 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.49 | 0.3919 | 0.2503 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.57 | 0.4004 | 0.2427 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.51 | 0.4016 | 0.2474 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.54 | 0.4011 | 0.2456 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.46 | 0.3891 | 0.2464 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.57 | 0.4076 | 0.2385 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.48 | 0.4052 | 0.2434 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.51 | 0.4070 | 0.2415 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.17 | 0.5120 | 0.1347 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.83 | 0.4941 | 0.1425 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.83 | 0.4941 | 0.1425 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.81 | 0.4880 | 0.1447 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.81 | 0.4880 | 0.1447 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.86 | 0.3052 | 0.1688 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.54 | 0.2588 | 0.1833 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.54 | 0.2588 | 0.1833 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.49 | 0.2524 | 0.1852 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.49 | 0.2524 | 0.1852 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.38 | 0.2202 | 0.1900 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.63 | 0.4796 | 0.2034 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.79 | 0.4952 | 0.1895 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.69 | 0.4956 | 0.1973 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.74 | 0.4960 | 0.1936 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.65 | 0.4937 | 0.1932 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.84 | 0.5316 | 0.1793 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.71 | 0.5255 | 0.1870 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.76 | 0.5298 | 0.1836 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.79 | 0.3629 | 0.1559 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.45 | 0.3969 | 0.2435 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.56 | 0.4090 | 0.2337 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.48 | 0.4084 | 0.2398 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.51 | 0.4095 | 0.2370 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.43 | 0.3905 | 0.2412 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.55 | 0.4082 | 0.2308 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.45 | 0.4067 | 0.2371 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.48 | 0.4080 | 0.2345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.39 | 0.7613 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.69 | 0.7648 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.58 | 0.7636 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.61 | 0.7640 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.84 | 0.7642 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.09 | 0.7693 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.95 | 0.7676 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.98 | 0.7685 | 0.0212 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.63 | 0.7596 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.13 | 0.7576 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.11 | 0.7569 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.10 | 0.7566 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.09 | 0.7562 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.73 | 0.7633 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.12 | 0.7587 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.11 | 0.7581 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.04 | 0.7578 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.06 | 0.7576 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.28 | 0.7554 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.86 | 0.7496 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.16 | 0.7562 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.08 | 0.7539 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.10 | 0.7550 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.58 | 0.7606 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.14 | 0.7709 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.86 | 0.7664 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.02 | 0.7692 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.90 | 0.7458 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.82 | 0.7642 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.01 | 0.7676 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.96 | 0.7666 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.98 | 0.7671 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.30 | 0.7679 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.39 | 0.7714 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.41 | 0.7705 | 0.0212 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.42 | 0.7714 | 0.0207 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.84 | 0.7488 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.38 | 0.7521 | 0.0264 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.25 | 0.7536 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.30 | 0.7531 | 0.0269 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.13 | 0.7474 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.63 | 0.7567 | 0.0240 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.40 | 0.7552 | 0.0246 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.43 | 0.7562 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.22 | 0.7487 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.21 | 0.7457 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.31 | 0.7483 | 0.0279 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.98 | 0.7406 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.06 | 0.7439 | 0.0284 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.31 | 0.7564 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.27 | 0.7474 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.43 | 0.7504 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.01 | 0.7423 | 0.0304 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.14 | 0.7449 | 0.0278 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.91 | 0.7233 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.66 | 0.7150 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.07 | 0.7237 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.00 | 0.7241 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.02 | 0.7244 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.58 | 0.7311 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.41 | 0.7526 | 0.0282 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.10 | 0.7475 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.20 | 0.7509 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.65 | 0.6807 | 0.0531 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.47 | 0.7478 | 0.0326 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.65 | 0.7533 | 0.0315 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.65 | 0.7537 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.69 | 0.7542 | 0.0313 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.08 | 0.7505 | 0.0287 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.97 | 0.7570 | 0.0293 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.26 | 0.7580 | 0.0280 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.24 | 0.7592 | 0.0279 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 40.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.37 | 0.7127 | 0.0300 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.07 | 0.3150 | 0.3820 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.12 | 0.3249 | 0.3760 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.09 | 0.3246 | 0.3798 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.10 | 0.3253 | 0.3783 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.07 | 0.3212 | 0.3773 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.11 | 0.3342 | 0.3712 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.08 | 0.3310 | 0.3756 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.09 | 0.3327 | 0.3738 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.74 | 0.4855 | 0.1919 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.59 | 0.4729 | 0.1953 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.59 | 0.4729 | 0.1953 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.55 | 0.4678 | 0.1976 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.55 | 0.4678 | 0.1976 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.58 | 0.2242 | 0.2353 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.64 | 0.2132 | 0.2404 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.64 | 0.2132 | 0.2404 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.63 | 0.2105 | 0.2415 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.63 | 0.2105 | 0.2415 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.62 | 0.2072 | 0.2406 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.48 | 0.3979 | 0.3310 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.55 | 0.4126 | 0.3205 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.51 | 0.4121 | 0.3265 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.53 | 0.4133 | 0.3237 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.51 | 0.4213 | 0.3216 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.55 | 0.4441 | 0.3111 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.52 | 0.4397 | 0.3170 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.54 | 0.4429 | 0.3142 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.60 | 0.3420 | 0.1976 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.17 | 0.3244 | 0.3756 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.23 | 0.3335 | 0.3690 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.19 | 0.3324 | 0.3733 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.21 | 0.3333 | 0.3715 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.17 | 0.3314 | 0.3701 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.21 | 0.3381 | 0.3645 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.18 | 0.3380 | 0.3685 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.19 | 0.3382 | 0.3668 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.41 | 0.7132 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.60 | 0.7153 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.53 | 0.7147 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.55 | 0.7149 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.64 | 0.7147 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.78 | 0.7173 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.71 | 0.7167 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.72 | 0.7170 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.48 | 0.7119 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.07 | 0.7108 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.06 | 0.7105 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.01 | 0.7102 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.01 | 0.7098 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.53 | 0.7142 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.18 | 0.7120 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.18 | 0.7117 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.10 | 0.7115 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.11 | 0.7111 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.40 | 0.7125 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.98 | 0.7057 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.17 | 0.7098 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.12 | 0.7084 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.12 | 0.7090 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.46 | 0.7127 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.83 | 0.7187 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.65 | 0.7160 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.75 | 0.7176 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.07 | 0.7074 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.66 | 0.7145 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.79 | 0.7165 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.77 | 0.7160 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.78 | 0.7162 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.90 | 0.7162 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.04 | 0.7188 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.01 | 0.7178 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.04 | 0.7185 | 0.0284 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.84 | 0.7068 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.20 | 0.7100 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.13 | 0.7107 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.15 | 0.7107 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.07 | 0.7084 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.39 | 0.7135 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.23 | 0.7126 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.26 | 0.7132 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.43 | 0.7101 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.80 | 0.7080 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.84 | 0.7081 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.73 | 0.7060 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.75 | 0.7058 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.48 | 0.7138 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.94 | 0.7099 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.00 | 0.7097 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.87 | 0.7083 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.90 | 0.7076 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.10 | 0.7085 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.57 | 0.6848 | 0.0456 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.95 | 0.6928 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.87 | 0.6923 | 0.0438 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.90 | 0.6932 | 0.0427 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.56 | 0.7017 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.29 | 0.7145 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.03 | 0.7111 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.18 | 0.7133 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.27 | 0.6941 | 0.0396 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.11 | 0.7092 | 0.0361 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.35 | 0.7133 | 0.0344 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.27 | 0.7124 | 0.0358 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.30 | 0.7129 | 0.0352 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.61 | 0.7128 | 0.0327 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.78 | 0.7176 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.72 | 0.7161 | 0.0323 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.77 | 0.7171 | 0.0318 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.61 | 0.7063 | 0.0359 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.28 | 0.2772 | 0.4051 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.32 | 0.2798 | 0.4001 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.29 | 0.2804 | 0.4027 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.30 | 0.2805 | 0.4012 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.27 | 0.2772 | 0.4034 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.29 | 0.2794 | 0.3992 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.27 | 0.2804 | 0.4018 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.28 | 0.2799 | 0.4008 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.30 | 0.4391 | 0.2656 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.26 | 0.4340 | 0.2704 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.26 | 0.4340 | 0.2704 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.25 | 0.4328 | 0.2716 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.25 | 0.4328 | 0.2716 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.32 | 0.1158 | 0.2932 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.40 | 0.1176 | 0.2957 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.40 | 0.1176 | 0.2957 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.40 | 0.1178 | 0.2951 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.40 | 0.1178 | 0.2951 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.38 | 0.1135 | 0.2950 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.10 | 0.3359 | 0.3588 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.14 | 0.3417 | 0.3493 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.11 | 0.3430 | 0.3540 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.13 | 0.3431 | 0.3512 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.08 | 0.3385 | 0.3529 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.11 | 0.3452 | 0.3451 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.09 | 0.3469 | 0.3493 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.10 | 0.3466 | 0.3472 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.24 | 0.2144 | 0.2564 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.30 | 0.2809 | 0.4017 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.33 | 0.2840 | 0.3968 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.31 | 0.2841 | 0.3996 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.32 | 0.2844 | 0.3982 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.29 | 0.2834 | 0.3994 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.31 | 0.2828 | 0.3962 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.30 | 0.2848 | 0.3983 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.30 | 0.2838 | 0.3973 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.60 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.60 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.60 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.60 | 0.7063 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.61 | 0.7063 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.61 | 0.7063 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.61 | 0.7064 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.58 | 0.7060 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.59 | 0.7062 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.59 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.59 | 0.7062 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.57 | 0.7060 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.60 | 0.7062 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.59 | 0.7062 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.59 | 0.7062 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.60 | 0.7063 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.60 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.60 | 0.7063 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.60 | 0.7063 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.60 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.59 | 0.7061 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.60 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.60 | 0.7063 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.49 | 0.7055 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.54 | 0.7059 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.55 | 0.7062 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.55 | 0.7062 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.43 | 0.7052 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.49 | 0.7059 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.48 | 0.7060 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.48 | 0.7060 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.62 | 0.7067 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.58 | 0.7065 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.57 | 0.7060 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.59 | 0.7064 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.59 | 0.7061 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.61 | 0.7068 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.59 | 0.7065 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.58 | 0.7061 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.60 | 0.7065 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.60 | 0.7062 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.58 | 0.7067 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.13 | 0.7028 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.33 | 0.7046 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.28 | 0.7047 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.32 | 0.7049 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.29 | 0.7048 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.45 | 0.7064 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.42 | 0.7064 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.44 | 0.7064 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.47 | 0.7066 | 0.0389 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.53 | 0.7058 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.56 | 0.7065 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.57 | 0.7065 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.57 | 0.7066 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.56 | 0.7065 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.56 | 0.7069 | 0.0367 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.57 | 0.7069 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.57 | 0.7070 | 0.0369 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.08 | 0.7093 | 0.0539 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.60 | 0.2839 | 0.4834 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.64 | 0.2887 | 0.4758 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.61 | 0.2889 | 0.4806 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.62 | 0.2892 | 0.4783 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.58 | 0.2845 | 0.4751 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.61 | 0.2910 | 0.4685 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.59 | 0.2899 | 0.4729 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.60 | 0.2904 | 0.4709 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.51 | 0.4414 | 0.3816 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.43 | 0.4328 | 0.3863 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.43 | 0.4328 | 0.3863 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.43 | 0.4315 | 0.3880 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.43 | 0.4315 | 0.3880 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.41 | 0.1508 | 0.3996 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.45 | 0.1455 | 0.4059 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.45 | 0.1455 | 0.4059 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.44 | 0.1458 | 0.4064 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.44 | 0.1458 | 0.4064 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.43 | 0.1409 | 0.4057 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.59 | 0.3534 | 0.4269 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.64 | 0.3624 | 0.4112 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.61 | 0.3630 | 0.4202 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.63 | 0.3635 | 0.4159 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.59 | 0.3600 | 0.4109 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.62 | 0.3745 | 0.3962 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.60 | 0.3731 | 0.4046 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.61 | 0.3745 | 0.4006 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.62 | 0.2555 | 0.3408 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.60 | 0.2874 | 0.4765 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.63 | 0.2925 | 0.4663 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.61 | 0.2921 | 0.4728 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.62 | 0.2927 | 0.4698 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.59 | 0.2902 | 0.4687 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.61 | 0.2924 | 0.4607 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.60 | 0.2930 | 0.4662 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.60 | 0.2926 | 0.4636 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.99 | 0.7092 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.15 | 0.7102 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.09 | 0.7099 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.11 | 0.7100 | 0.0545 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.17 | 0.7098 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.30 | 0.7114 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.23 | 0.7108 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.26 | 0.7111 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.09 | 0.7089 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.79 | 0.7081 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.78 | 0.7079 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.81 | 0.7080 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.81 | 0.7078 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.13 | 0.7099 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.78 | 0.7086 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.78 | 0.7084 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.78 | 0.7085 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.79 | 0.7083 | 0.0552 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.00 | 0.7090 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.75 | 0.7058 | 0.0595 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.91 | 0.7078 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.87 | 0.7071 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.88 | 0.7074 | 0.0582 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.04 | 0.7086 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.30 | 0.7118 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.19 | 0.7104 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.25 | 0.7112 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.83 | 0.7068 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.17 | 0.7100 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.28 | 0.7110 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.24 | 0.7107 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.26 | 0.7108 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.38 | 0.7108 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.42 | 0.7119 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.42 | 0.7115 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.44 | 0.7118 | 0.0526 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.59 | 0.7060 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.88 | 0.7076 | 0.0585 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.81 | 0.7079 | 0.0594 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.84 | 0.7079 | 0.0589 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.63 | 0.7063 | 0.0568 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 | 0.7091 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.79 | 0.7084 | 0.0561 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.83 | 0.7088 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.06 | 0.7083 | 0.0582 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.58 | 0.7067 | 0.0594 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.59 | 0.7064 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.60 | 0.7062 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.61 | 0.7059 | 0.0584 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.10 | 0.7099 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.61 | 0.7074 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.62 | 0.7071 | 0.0562 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.61 | 0.7071 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.62 | 0.7065 | 0.0568 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.77 | 0.7071 | 0.0591 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.83 | 0.6957 | 0.0736 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.14 | 0.6997 | 0.0683 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.06 | 0.6994 | 0.0710 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.09 | 0.6998 | 0.0696 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.38 | 0.7024 | 0.0643 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.88 | 0.7092 | 0.0592 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.69 | 0.7073 | 0.0621 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.79 | 0.7084 | 0.0607 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.29 | 0.7010 | 0.0650 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.85 | 0.7073 | 0.0613 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.02 | 0.7095 | 0.0591 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.96 | 0.7090 | 0.0608 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.99 | 0.7093 | 0.0600 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.22 | 0.7094 | 0.0578 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.24 | 0.7112 | 0.0558 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.23 | 0.7107 | 0.0573 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.23 | 0.7110 | 0.0566 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 301421 | 0.168 | 39.1 | 28.85 | 0.45 | 0.038 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 301421 | 0.168 | 39.4 | 28.85 | 0.45 | 0.038 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 301421 | 0.168 | 41.0 | 28.85 | 0.45 | 0.038 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 301421 | 0.168 | 37.3 | 28.85 | 0.45 | 0.038 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 676 | None | classic | 0.30 | False | 660446 | 0.687 | 124.7 | 31.39 | 0.37 | 0.021 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 676 | None | classic | 0.30 | False | 660446 | 0.687 | 120.1 | 31.39 | 0.37 | 0.021 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 676 | None | classic | 0.30 | False | 660446 | 0.687 | 118.7 | 31.39 | 0.37 | 0.021 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 676 | None | classic | 0.30 | False | 660446 | 0.687 | 114.6 | 31.39 | 0.37 | 0.021 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 836647 | 0.162 | 21.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 836425 | 0.821 | 47.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 836425 | 0.821 | 47.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 836425 | 0.646 | 21.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 836425 | 0.646 | 21.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 836647 | 0.162 | 28.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 836425 | 0.821 | 70.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 836425 | 0.821 | 70.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 836425 | 0.646 | 28.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 836425 | 0.646 | 28.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 833833 | 0.821 | 154.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 301421 | 0.167 | 36.4 | 28.85 | 0.45 | 0.038 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 301421 | 0.167 | 33.4 | 28.85 | 0.45 | 0.038 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 301421 | 0.167 | 35.1 | 28.85 | 0.45 | 0.038 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 301421 | 0.167 | 33.1 | 28.85 | 0.45 | 0.038 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 792 | None | classic | 0.66 | False | 496387 | 0.519 | 86.9 | 28.39 | 0.06 | 0.014 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 792 | None | classic | 0.66 | False | 496387 | 0.519 | 94.2 | 28.39 | 0.06 | 0.014 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 792 | None | classic | 0.66 | False | 496387 | 0.519 | 85.7 | 28.39 | 0.06 | 0.014 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 792 | None | classic | 0.66 | False | 496387 | 0.519 | 83.8 | 28.39 | 0.06 | 0.014 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1564149 | 0.821 | 71.0 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 280103 | 0.327 | 42.4 | 29.65 | 0.24 | 0.038 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 280103 | 0.327 | 30.1 | 29.65 | 0.24 | 0.038 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 280103 | 0.327 | 31.7 | 29.65 | 0.24 | 0.038 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 280103 | 0.327 | 32.1 | 29.65 | 0.24 | 0.038 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 856 | None | classic | 0.30 | False | 393564 | 0.503 | 84.6 | 30.57 | 0.17 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 856 | None | classic | 0.30 | False | 393564 | 0.503 | 91.7 | 30.57 | 0.17 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 856 | None | classic | 0.30 | False | 393564 | 0.503 | 90.9 | 30.57 | 0.17 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 856 | None | classic | 0.30 | False | 393564 | 0.503 | 86.4 | 30.57 | 0.17 | 0.009 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.691 | 0.018 |
| in035 | mask_ent | 0.756 | 0.018 |
| in035 | mask_grad | 0.475 | 0.018 |
| in035 | r_col | 0.701 | 0.018 |
| in035 | r_warp | 0.861 | 0.018 |

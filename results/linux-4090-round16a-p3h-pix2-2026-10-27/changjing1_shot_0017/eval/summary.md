# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 10.5% | 23.28 / 0.0141 | 20.79 / 0.0294 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 10.9% | 23.32 / 0.0143 | 22.53 / 0.0221 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 10.6% | 23.29 / 0.0140 | 21.91 / 0.0253 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 10.7% | 23.30 / 0.0140 | 22.14 / 0.0235 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.3% | 23.20 / 0.0136 | 21.00 / 0.0242 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.6% | 23.27 / 0.0137 | 22.71 / 0.0175 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.4% | 23.24 / 0.0135 | 22.01 / 0.0205 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 10.5% | 23.26 / 0.0136 | 22.34 / 0.0192 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 10.0% | 23.10 / 0.0140 | 22.36 / 0.0297 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 8.9% | 22.74 / 0.0137 | 21.37 / 0.0264 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 3.3% | 20.30 / 0.0091 | 17.61 / 0.0200 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 8.9% | 22.78 / 0.0134 | 20.95 / 0.0277 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 3.5% | 20.85 / 0.0098 | 17.43 / 0.0220 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 10.0% | 23.09 / 0.0140 | 22.21 / 0.0207 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 8.8% | 22.72 / 0.0140 | 21.07 / 0.0259 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 3.2% | 21.10 / 0.0086 | 17.16 / 0.0178 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 8.7% | 22.73 / 0.0136 | 20.96 / 0.0262 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 3.2% | 20.48 / 0.0088 | 17.01 / 0.0188 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 11.8% | 23.46 / 0.0150 | 20.65 / 0.0418 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 15.5% | 23.94 / 0.0170 | 20.68 / 0.0462 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 16.1% | 23.95 / 0.0174 | 22.22 / 0.0370 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 15.7% | 23.90 / 0.0171 | 21.56 / 0.0425 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 15.8% | 23.92 / 0.0171 | 21.83 / 0.0397 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 15.5% | 23.87 / 0.0170 | 20.49 / 0.0418 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 16.0% | 23.94 / 0.0169 | 21.82 / 0.0324 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 15.6% | 23.89 / 0.0169 | 21.38 / 0.0373 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 15.7% | 23.91 / 0.0167 | 21.48 / 0.0349 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 16.6% | 23.94 / 0.0187 | 20.43 / 0.0533 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 8.3% | 23.06 / 0.0123 | 20.74 / 0.0281 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 9.0% | 23.14 / 0.0130 | 22.05 / 0.0252 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 8.4% | 23.05 / 0.0123 | 21.63 / 0.0252 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 8.5% | 23.09 / 0.0126 | 21.96 / 0.0243 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 9.0% | 22.80 / 0.0132 | 21.38 / 0.0262 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 10.0% | 23.03 / 0.0137 | 22.04 / 0.0244 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 9.3% | 22.88 / 0.0132 | 21.93 / 0.0234 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 9.5% | 22.93 / 0.0135 | 22.00 / 0.0234 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.22 / 0.0554 | 23.65 / 0.0720 | 19.68 / 0.0157 | 29.88 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.74 / 0.0683 | 23.50 / 0.1222 | 20.04 / 0.0183 | 29.40 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.38 / 0.0611 | 25.29 / 0.0846 | 20.78 / 0.0153 | 29.61 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.16 / 0.0647 | 24.51 / 0.1047 | 20.48 / 0.0166 | 29.56 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.25 / 0.0629 | 24.93 / 0.0941 | 20.59 / 0.0162 | 29.58 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.79 / 0.0635 | 22.47 / 0.1194 | 19.97 / 0.0170 | 29.43 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.38 / 0.0579 | 24.34 / 0.0823 | 20.86 / 0.0140 | 29.57 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.15 / 0.0605 | 23.52 / 0.1024 | 20.49 / 0.0156 | 29.53 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.27 / 0.0590 | 23.96 / 0.0911 | 20.66 / 0.0148 | 29.56 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.35 / 0.0637 | 24.40 / 0.1234 | 20.09 / 0.0214 | 29.90 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.83 / 0.0641 | 24.30 / 0.0902 | 19.93 / 0.0197 | 29.52 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.78 / 0.0622 | 24.01 / 0.0883 | 19.72 / 0.0192 | 29.51 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.74 / 0.0643 | 23.65 / 0.0994 | 19.65 / 0.0208 | 29.56 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.70 / 0.0626 | 23.38 / 0.0997 | 19.49 / 0.0206 | 29.55 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.29 / 0.0573 | 24.22 / 0.0868 | 20.02 / 0.0165 | 29.86 / 0.0352 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.78 / 0.0629 | 24.11 / 0.0885 | 19.85 / 0.0182 | 29.57 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.80 / 0.0610 | 24.10 / 0.0831 | 19.70 / 0.0177 | 29.59 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.78 / 0.0627 | 23.74 / 0.0917 | 19.63 / 0.0194 | 29.69 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.82 / 0.0605 | 23.71 / 0.0870 | 19.53 / 0.0189 | 29.72 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.77 / 0.0657 | 23.09 / 0.1278 | 20.11 / 0.0192 | 29.49 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.15 / 0.0786 | 22.93 / 0.1436 | 19.38 / 0.0216 | 29.12 / 0.0415 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.87 / 0.0703 | 24.41 / 0.1021 | 20.35 / 0.0185 | 29.40 / 0.0397 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.60 / 0.0758 | 23.83 / 0.1235 | 19.85 / 0.0205 | 29.39 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.72 / 0.0732 | 24.18 / 0.1115 | 20.07 / 0.0198 | 29.41 / 0.0398 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.00 / 0.0745 | 21.53 / 0.1490 | 19.05 / 0.0218 | 29.12 / 0.0406 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.65 / 0.0659 | 22.87 / 0.1079 | 19.80 / 0.0180 | 29.39 / 0.0387 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.41 / 0.0709 | 22.37 / 0.1335 | 19.50 / 0.0200 | 29.32 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.49 / 0.0687 | 22.61 / 0.1218 | 19.59 / 0.0193 | 29.37 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.39 / 0.0691 | 23.27 / 0.1298 | 19.56 / 0.0205 | 29.46 / 0.0393 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.04 / 0.0670 | 23.76 / 0.1172 | 20.14 / 0.0167 | 29.64 / 0.0377 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.46 / 0.0618 | 25.11 / 0.0864 | 20.73 / 0.0147 | 29.75 / 0.0368 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.27 / 0.0650 | 24.43 / 0.1036 | 20.44 / 0.0159 | 29.71 / 0.0373 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.35 / 0.0635 | 24.75 / 0.0951 | 20.55 / 0.0154 | 29.73 / 0.0371 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.29 / 0.0627 | 23.68 / 0.1115 | 20.69 / 0.0144 | 29.38 / 0.0381 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.58 / 0.0581 | 24.75 / 0.0840 | 21.04 / 0.0125 | 29.53 / 0.0374 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.49 / 0.0602 | 24.38 / 0.0961 | 20.95 / 0.0131 | 29.46 / 0.0377 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.53 / 0.0592 | 24.62 / 0.0887 | 21.01 / 0.0127 | 29.49 / 0.0375 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 8.3%） | — | — | 27.22 / 0.0554 | 23.65 / 0.0720 | 29.88 |
| in035 | rife | 4.1% | 8.3% | 27.04 / 0.0670 | 23.76 / 0.1172 | 29.64 |
| in035 | cnw_cnn | 6.5% | 10.5% | 26.74 / 0.0683 | 23.50 / 0.1222 | 29.40 |
| in035 | cnw_f5 | 9.7% | 15.5% | 26.15 / 0.0786 | 22.93 / 0.1436 | 29.12 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.34 / 0.0552 | -0.06 / +0.0121 (core 5.6%) | -0.29 / +0.0128 (core 7.8%) | -0.95 / +0.0254 (core 11.7%) |
| in035 | 2 | 0-3 | 26.62 / 0.0580 | -0.04 / +0.0174 (core 5.6%) | -0.39 / +0.0178 (core 7.8%) | -1.02 / +0.0302 (core 11.7%) |
| in035 | 4 | 3-5 | 28.71 / 0.0530 | -0.44 / +0.0051 (core 1.0%) | -0.76 / +0.0080 (core 2.9%) | -1.25 / +0.0139 (core 4.6%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.22 / 0.0554 | 23.65 | 29.88 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.74 / 0.0683 | 23.50 | 29.40 | 0/3 |
| in035 | cnw_cnn | oracle | 2.8% | 27.30 / 0.0601 | 24.24 | 29.84 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.38 / 0.0611 | 25.29 | 29.61 | 0/3 |
| in035 | cnw_cnn | oracle | 2.9% | 27.72 / 0.0563 | 25.62 | 29.87 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.16 / 0.0647 | 24.51 | 29.56 | 0/3 |
| in035 | cnw_cnn | oracle | 2.8% | 27.55 / 0.0583 | 25.01 | 29.86 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.25 / 0.0629 | 24.93 | 29.58 | 0/3 |
| in035 | cnw_cnn | oracle | 2.8% | 27.62 / 0.0574 | 25.34 | 29.86 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.79 / 0.0635 | 22.47 | 29.43 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 27.27 / 0.0576 | 23.31 | 29.82 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.38 / 0.0579 | 24.34 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 27.77 / 0.0541 | 24.92 | 29.86 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.15 / 0.0605 | 23.52 | 29.53 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 27.56 / 0.0559 | 24.21 | 29.84 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.27 / 0.0590 | 23.96 | 29.56 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 27.66 / 0.0550 | 24.58 | 29.85 | 2/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 27.35 / 0.0637 | 24.40 | 29.90 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 2.8% | 27.42 / 0.0616 | 24.68 | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 26.83 / 0.0641 | 24.30 | 29.52 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 2.7% | 27.23 / 0.0591 | 24.51 | 29.83 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 26.78 / 0.0622 | 24.01 | 29.51 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 1.7% | 27.14 / 0.0588 | 24.16 | 29.83 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 26.74 / 0.0643 | 23.65 | 29.56 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 2.6% | 27.07 / 0.0599 | 23.91 | 29.74 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 26.70 / 0.0626 | 23.38 | 29.55 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 1.7% | 26.99 / 0.0597 | 23.60 | 29.74 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.29 / 0.0573 | 24.22 | 29.86 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 2.8% | 27.39 / 0.0560 | 24.56 | 29.88 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 26.78 / 0.0629 | 24.11 | 29.57 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.6% | 27.19 / 0.0580 | 24.42 | 29.84 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.80 / 0.0610 | 24.10 | 29.59 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.6% | 27.14 / 0.0575 | 24.23 | 29.84 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 26.78 / 0.0627 | 23.74 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 2.6% | 27.10 / 0.0585 | 24.02 | 29.84 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 26.82 / 0.0605 | 23.71 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 1.5% | 27.07 / 0.0578 | 23.84 | 29.84 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.77 / 0.0657 | 23.09 | 29.49 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 3.0% | 27.30 / 0.0584 | 24.05 | 29.79 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.15 / 0.0786 | 22.93 | 29.12 | 0/3 |
| in035 | cnw_f5 | oracle | 3.6% | 26.96 / 0.0642 | 23.85 | 29.77 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.87 / 0.0703 | 24.41 | 29.40 | 0/3 |
| in035 | cnw_f5 | oracle | 3.6% | 27.46 / 0.0600 | 24.97 | 29.83 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.60 / 0.0758 | 23.83 | 29.39 | 0/3 |
| in035 | cnw_f5 | oracle | 3.6% | 27.22 / 0.0630 | 24.52 | 29.81 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.72 / 0.0732 | 24.18 | 29.41 | 0/3 |
| in035 | cnw_f5 | oracle | 3.6% | 27.32 / 0.0617 | 24.79 | 29.82 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.00 / 0.0745 | 21.53 | 29.12 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.6% | 26.72 / 0.0626 | 22.53 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.65 / 0.0659 | 22.87 | 29.39 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.6% | 27.19 / 0.0580 | 23.65 | 29.79 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.41 / 0.0709 | 22.37 | 29.32 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.6% | 27.00 / 0.0609 | 23.19 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.49 / 0.0687 | 22.61 | 29.37 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.6% | 27.06 / 0.0598 | 23.40 | 29.78 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.39 / 0.0691 | 23.27 | 29.46 | 0/3 |
| in035 | cnw_f5_pix | oracle | 3.7% | 27.07 / 0.0598 | 24.28 | 29.83 | 0/3 |
| in035 | rife | 不复核 | —% | 27.04 / 0.0670 | 23.76 | 29.64 | 0/3 |
| in035 | rife | oracle | 2.2% | 27.42 / 0.0580 | 24.34 | 29.83 | 0/3 |
| in035 | rife | 不复核 | —% | 27.46 / 0.0618 | 25.11 | 29.75 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.73 / 0.0553 | 25.38 | 29.87 | 2/3 |
| in035 | rife | 不复核 | —% | 27.27 / 0.0650 | 24.43 | 29.71 | 0/3 |
| in035 | rife | oracle | 2.2% | 27.58 / 0.0569 | 24.86 | 29.85 | 0/3 |
| in035 | rife | 不复核 | —% | 27.35 / 0.0635 | 24.75 | 29.73 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.63 / 0.0563 | 25.10 | 29.86 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.29 / 0.0627 | 23.68 | 29.38 | 0/3 |
| in035 | rife_mw | oracle | 2.5% | 27.65 / 0.0552 | 24.46 | 29.71 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 27.58 / 0.0581 | 24.75 | 29.53 | 0/3 |
| in035 | rife_mw | oracle | 2.6% | 27.85 / 0.0524 | 25.35 | 29.77 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 27.49 / 0.0602 | 24.38 | 29.46 | 0/3 |
| in035 | rife_mw | oracle | 2.5% | 27.80 / 0.0537 | 25.03 | 29.74 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 27.53 / 0.0592 | 24.62 | 29.49 | 0/3 |
| in035 | rife_mw | oracle | 2.6% | 27.83 / 0.0530 | 25.22 | 29.76 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.22 / 0.0554 | 23.65 / 0.0720 | — |
| in035 | FF | 0（前馈） | 1000×645（60%） | 26.86 | 26.74 / 0.0683 | 23.50 / 0.1222 | 0/3 |
| in035 | 25 | 0.67 s | 1000×645（60%） | 27.58 | 27.16 / 0.0647 | 24.51 / 0.1047 | 0/3 |
| in035 | 50 | 1.31 s | 1000×645（60%） | 27.92 | 27.25 / 0.0629 | 24.93 / 0.0941 | 0/3 |
| in035 | 100 | 2.59 s | 1000×645（60%） | 28.21 | 27.38 / 0.0611 | 25.29 / 0.0846 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.22 / 0.0554 | 23.65 / 0.0720 | 29.88 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.74 / 0.0683 | 23.50 / 0.1222 | 29.40 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.30 / 0.0601 | 24.24 / 0.0942 | 29.84 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.16 / 0.0647 | 24.51 / 0.1047 | 29.56 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.55 / 0.0583 | 25.01 / 0.0847 | 29.86 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.25 / 0.0629 | 24.93 / 0.0941 | 29.58 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.62 / 0.0574 | 25.34 / 0.0786 | 29.86 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.38 / 0.0611 | 25.29 / 0.0846 | 29.61 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.72 / 0.0563 | 25.62 / 0.0726 | 29.87 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 26.79 / 0.0635 | 22.47 / 0.1194 | 29.43 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.27 / 0.0576 | 23.31 / 0.0956 | 29.82 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.15 / 0.0605 | 23.52 / 0.1024 | 29.53 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.56 / 0.0559 | 24.21 / 0.0844 | 29.84 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.27 / 0.0590 | 23.96 / 0.0911 | 29.56 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.66 / 0.0550 | 24.58 / 0.0765 | 29.85 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.38 / 0.0579 | 24.34 / 0.0823 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.77 / 0.0541 | 24.92 / 0.0703 | 29.86 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.15 / 0.0786 | 22.93 / 0.1436 | 29.12 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 26.96 / 0.0642 | 23.85 / 0.1068 | 29.77 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.60 / 0.0758 | 23.83 / 0.1235 | 29.39 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.22 / 0.0630 | 24.52 / 0.0957 | 29.81 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.72 / 0.0732 | 24.18 / 0.1115 | 29.41 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.32 / 0.0617 | 24.79 / 0.0889 | 29.82 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.87 / 0.0703 | 24.41 / 0.1021 | 29.40 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.46 / 0.0600 | 24.97 / 0.0829 | 29.83 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.00 / 0.0745 | 21.53 / 0.1490 | 29.12 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 26.72 / 0.0626 | 22.53 / 0.1148 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.41 / 0.0709 | 22.37 / 0.1335 | 29.32 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.00 / 0.0609 | 23.19 / 0.1050 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.49 / 0.0687 | 22.61 / 0.1218 | 29.37 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.06 / 0.0598 | 23.40 / 0.0960 | 29.78 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 26.65 / 0.0659 | 22.87 / 0.1079 | 29.39 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.19 / 0.0580 | 23.65 / 0.0861 | 29.79 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.04 / 0.0670 | 23.76 / 0.1172 | 29.64 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.42 / 0.0580 | 24.34 / 0.0928 | 29.83 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.27 / 0.0650 | 24.43 / 0.1036 | 29.71 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.58 / 0.0569 | 24.86 / 0.0847 | 29.85 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.35 / 0.0635 | 24.75 / 0.0951 | 29.73 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.63 / 0.0563 | 25.10 / 0.0794 | 29.86 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.46 / 0.0618 | 25.11 / 0.0864 | 29.75 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.73 / 0.0553 | 25.38 / 0.0733 | 29.87 | 2/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.29 / 0.0627 | 23.68 / 0.1115 | 29.38 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.65 / 0.0552 | 24.46 / 0.0809 | 29.71 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.49 / 0.0602 | 24.38 / 0.0961 | 29.46 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.80 / 0.0537 | 25.03 / 0.0722 | 29.74 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.53 / 0.0592 | 24.62 / 0.0887 | 29.49 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.83 / 0.0530 | 25.22 / 0.0671 | 29.76 | 2/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.58 / 0.0581 | 24.75 / 0.0840 | 29.53 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.85 / 0.0524 | 25.35 / 0.0633 | 29.77 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.65 / 0.0720 | 19.68 / 0.0157 | 29.88 / 0.0349 | 27.22 / 0.0554 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 13.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.65 | 0.7887 | 0.0720 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 14.48 | 0.5753 | 0.3002 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 15.86 | 0.7170 | 0.2163 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 15.08 | 0.6544 | 0.2642 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 15.40 | 0.6899 | 0.2412 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 13.61 | 0.4995 | 0.2863 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 15.12 | 0.6289 | 0.2129 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 14.17 | 0.5716 | 0.2508 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 14.54 | 0.6027 | 0.2317 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 22.54 | 0.7615 | 0.1821 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 22.48 | 0.7829 | 0.1461 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 22.48 | 0.7829 | 0.1461 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 22.02 | 0.7717 | 0.1557 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 22.02 | 0.7717 | 0.1557 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.47 | 0.6861 | 0.2143 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.45 | 0.6785 | 0.2291 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.45 | 0.6785 | 0.2291 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 15.65 | 0.6744 | 0.2296 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 15.65 | 0.6744 | 0.2296 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.02 | 0.6359 | 0.2498 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 16.76 | 0.5738 | 0.2824 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 18.09 | 0.6957 | 0.2010 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 17.47 | 0.6438 | 0.2452 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 17.77 | 0.6732 | 0.2217 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 15.25 | 0.4992 | 0.2795 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 16.36 | 0.6072 | 0.2093 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 15.82 | 0.5620 | 0.2525 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 16.05 | 0.5861 | 0.2322 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.16 | 0.6797 | 0.2199 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.37 | 0.5353 | 0.3451 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.87 | 0.6531 | 0.2707 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.63 | 0.6022 | 0.3130 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.76 | 0.6308 | 0.2921 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.35 | 0.5478 | 0.3013 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 12.95 | 0.6481 | 0.2418 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 12.67 | 0.6155 | 0.2721 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 12.83 | 0.6380 | 0.2547 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.24 | 0.7906 | 0.0942 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.62 | 0.8275 | 0.0726 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.01 | 0.8115 | 0.0847 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.34 | 0.8206 | 0.0786 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.31 | 0.7699 | 0.0956 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.92 | 0.8103 | 0.0703 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.21 | 0.7916 | 0.0844 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.58 | 0.8015 | 0.0765 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.68 | 0.7991 | 0.1110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.51 | 0.8140 | 0.0832 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.16 | 0.8030 | 0.0846 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 23.91 | 0.8037 | 0.0923 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 23.60 | 0.7928 | 0.0936 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.56 | 0.8063 | 0.0800 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.42 | 0.8110 | 0.0795 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.23 | 0.8037 | 0.0791 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.02 | 0.8036 | 0.0843 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 23.84 | 0.7958 | 0.0831 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.05 | 0.7958 | 0.0980 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 23.85 | 0.7772 | 0.1068 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.97 | 0.8107 | 0.0829 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.52 | 0.7960 | 0.0957 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.79 | 0.8043 | 0.0889 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.53 | 0.7495 | 0.1148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.65 | 0.7865 | 0.0861 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.19 | 0.7695 | 0.1050 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.40 | 0.7780 | 0.0960 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.28 | 0.8001 | 0.0960 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.34 | 0.7917 | 0.0928 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.38 | 0.8220 | 0.0733 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.86 | 0.8076 | 0.0847 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.10 | 0.8151 | 0.0794 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 24.46 | 0.7985 | 0.0809 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.35 | 0.8271 | 0.0633 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.03 | 0.8179 | 0.0722 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.22 | 0.8238 | 0.0671 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.50 | 0.7545 | 0.1222 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.29 | 0.8178 | 0.0846 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.51 | 0.7910 | 0.1047 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.93 | 0.8068 | 0.0941 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.47 | 0.7268 | 0.1194 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.34 | 0.7903 | 0.0823 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.52 | 0.7625 | 0.1024 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.96 | 0.7782 | 0.0911 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.40 | 0.7880 | 0.1234 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.30 | 0.8063 | 0.0902 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.01 | 0.7989 | 0.0883 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 23.65 | 0.7965 | 0.0994 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 23.38 | 0.7877 | 0.0997 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.22 | 0.7966 | 0.0868 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.11 | 0.7994 | 0.0885 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.10 | 0.7992 | 0.0831 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 23.74 | 0.7941 | 0.0917 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 23.71 | 0.7922 | 0.0870 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.09 | 0.7696 | 0.1278 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.93 | 0.7280 | 0.1436 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.41 | 0.7898 | 0.1021 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.83 | 0.7638 | 0.1235 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.18 | 0.7793 | 0.1115 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.53 | 0.6913 | 0.1490 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.87 | 0.7564 | 0.1079 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.37 | 0.7293 | 0.1335 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.61 | 0.7435 | 0.1218 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.27 | 0.7703 | 0.1298 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.76 | 0.7629 | 0.1172 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.11 | 0.8132 | 0.0864 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.43 | 0.7899 | 0.1036 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.75 | 0.8023 | 0.0951 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.68 | 0.7626 | 0.1115 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.75 | 0.8090 | 0.0840 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.38 | 0.7954 | 0.0961 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.62 | 0.8049 | 0.0887 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 8.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.68 | 0.6581 | 0.0157 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.73 | 0.3698 | 0.0955 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.94 | 0.4487 | 0.0886 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.85 | 0.4148 | 0.0923 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.92 | 0.4326 | 0.0906 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.63 | 0.3467 | 0.0938 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.76 | 0.4258 | 0.0877 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.70 | 0.3912 | 0.0911 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.73 | 0.4093 | 0.0896 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.43 | 0.4783 | 0.0568 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.19 | 0.4712 | 0.0562 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.19 | 0.4712 | 0.0562 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.06 | 0.4517 | 0.0574 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.06 | 0.4517 | 0.0574 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.50 | 0.4287 | 0.0612 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.34 | 0.4057 | 0.0659 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.34 | 0.4057 | 0.0659 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.35 | 0.3924 | 0.0665 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.35 | 0.3924 | 0.0665 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.30 | 0.3879 | 0.0661 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.55 | 0.3963 | 0.0834 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.77 | 0.4749 | 0.0758 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.66 | 0.4377 | 0.0805 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.72 | 0.4558 | 0.0784 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.39 | 0.3415 | 0.0820 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.50 | 0.4014 | 0.0765 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.44 | 0.3703 | 0.0799 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.46 | 0.3849 | 0.0786 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.12 | 0.4305 | 0.0574 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.15 | 0.2816 | 0.1085 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.41 | 0.3450 | 0.1038 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.24 | 0.3134 | 0.1069 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.32 | 0.3287 | 0.1057 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.14 | 0.3160 | 0.1057 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.21 | 0.3641 | 0.1021 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.17 | 0.3476 | 0.1040 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.19 | 0.3574 | 0.1031 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.06 | 0.6723 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.79 | 0.7066 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.49 | 0.6923 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.61 | 0.6992 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.98 | 0.6682 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.88 | 0.7088 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.50 | 0.6908 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.68 | 0.6995 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.09 | 0.6663 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.94 | 0.6804 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.73 | 0.6653 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.65 | 0.6690 | 0.0207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.49 | 0.6559 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.01 | 0.6743 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.86 | 0.6787 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.70 | 0.6651 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.64 | 0.6687 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.54 | 0.6580 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.12 | 0.6741 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.40 | 0.6525 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.36 | 0.6866 | 0.0184 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.87 | 0.6729 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.08 | 0.6790 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.08 | 0.6368 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.83 | 0.6771 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.53 | 0.6591 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.62 | 0.6667 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.57 | 0.6537 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.15 | 0.6713 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.74 | 0.7002 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.45 | 0.6849 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.55 | 0.6913 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.71 | 0.6972 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.06 | 0.7228 | 0.0124 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.96 | 0.7152 | 0.0130 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.01 | 0.7202 | 0.0127 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.04 | 0.6693 | 0.0183 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.78 | 0.7055 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.48 | 0.6904 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.59 | 0.6976 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.97 | 0.6650 | 0.0170 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.86 | 0.7073 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.49 | 0.6887 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.66 | 0.6977 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.09 | 0.6654 | 0.0214 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.93 | 0.6798 | 0.0197 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.72 | 0.6648 | 0.0192 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.65 | 0.6681 | 0.0208 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.49 | 0.6554 | 0.0206 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.02 | 0.6733 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.85 | 0.6775 | 0.0182 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.70 | 0.6643 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.63 | 0.6672 | 0.0194 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.53 | 0.6568 | 0.0189 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.11 | 0.6714 | 0.0192 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.38 | 0.6501 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.35 | 0.6852 | 0.0185 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.85 | 0.6709 | 0.0205 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.07 | 0.6774 | 0.0198 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.05 | 0.6325 | 0.0218 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.80 | 0.6740 | 0.0180 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.50 | 0.6559 | 0.0200 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.59 | 0.6637 | 0.0193 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.56 | 0.6508 | 0.0205 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.14 | 0.6702 | 0.0167 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.73 | 0.6999 | 0.0147 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.44 | 0.6841 | 0.0159 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.55 | 0.6906 | 0.0154 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.69 | 0.6952 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.04 | 0.7217 | 0.0125 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.95 | 0.7138 | 0.0131 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.01 | 0.7190 | 0.0127 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 27.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.06 | 0.7560 | 0.0229 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.06 | 0.4433 | 0.2225 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.27 | 0.4867 | 0.2098 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.14 | 0.4718 | 0.2168 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.20 | 0.4797 | 0.2137 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.06 | 0.4507 | 0.2175 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.18 | 0.4870 | 0.2077 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.09 | 0.4797 | 0.2130 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.12 | 0.4844 | 0.2107 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.88 | 0.5845 | 0.1138 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.39 | 0.5730 | 0.1190 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.39 | 0.5730 | 0.1190 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.36 | 0.5682 | 0.1203 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.36 | 0.5682 | 0.1203 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.21 | 0.4178 | 0.1478 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.77 | 0.3664 | 0.1661 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.77 | 0.3664 | 0.1661 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.80 | 0.3669 | 0.1666 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.80 | 0.3669 | 0.1666 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.53 | 0.3103 | 0.1778 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.19 | 0.4785 | 0.1957 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.47 | 0.5150 | 0.1818 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.29 | 0.5032 | 0.1906 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.36 | 0.5090 | 0.1868 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.21 | 0.4776 | 0.1919 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.45 | 0.5200 | 0.1782 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.27 | 0.5092 | 0.1865 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.33 | 0.5152 | 0.1832 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.58 | 0.3692 | 0.1630 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.69 | 0.4243 | 0.2234 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.04 | 0.4583 | 0.2123 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.78 | 0.4445 | 0.2194 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.88 | 0.4513 | 0.2164 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.68 | 0.4406 | 0.2164 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.90 | 0.4669 | 0.2063 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.74 | 0.4651 | 0.2118 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.80 | 0.4673 | 0.2092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.16 | 0.7523 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.02 | 0.7711 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.66 | 0.7633 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.80 | 0.7670 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.26 | 0.7553 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.25 | 0.7745 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.84 | 0.7665 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.03 | 0.7705 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.16 | 0.7523 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.17 | 0.7602 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.02 | 0.7561 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.95 | 0.7556 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.86 | 0.7525 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.16 | 0.7590 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.03 | 0.7586 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.94 | 0.7553 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.87 | 0.7551 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.85 | 0.7531 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.89 | 0.7455 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.53 | 0.7450 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.53 | 0.7617 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.01 | 0.7545 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.22 | 0.7577 | 0.0278 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.28 | 0.7402 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.17 | 0.7597 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.86 | 0.7529 | 0.0278 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.93 | 0.7559 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.13 | 0.7341 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.49 | 0.7578 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.08 | 0.7717 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.78 | 0.7648 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.88 | 0.7676 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.17 | 0.7706 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.55 | 0.7830 | 0.0199 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.47 | 0.7797 | 0.0212 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.52 | 0.7819 | 0.0206 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.95 | 0.7268 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.94 | 0.7548 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.62 | 0.7454 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.71 | 0.7501 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.19 | 0.7302 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.22 | 0.7576 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.86 | 0.7491 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.02 | 0.7539 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.68 | 0.7319 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.28 | 0.7413 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.26 | 0.7445 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.03 | 0.7367 | 0.0323 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.06 | 0.7404 | 0.0297 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.67 | 0.7436 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.07 | 0.7371 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.17 | 0.7423 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 23.99 | 0.7357 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.15 | 0.7419 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.80 | 0.6972 | 0.0458 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.02 | 0.7054 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.08 | 0.7318 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.55 | 0.7226 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.75 | 0.7270 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.90 | 0.7022 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.84 | 0.7342 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.61 | 0.7253 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.61 | 0.7298 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.88 | 0.6681 | 0.0541 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.32 | 0.7280 | 0.0349 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.69 | 0.7458 | 0.0331 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.71 | 0.7411 | 0.0332 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.77 | 0.7442 | 0.0329 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.01 | 0.7474 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.05 | 0.7613 | 0.0297 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.28 | 0.7625 | 0.0287 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.23 | 0.7637 | 0.0285 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 42.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.82 | 0.7382 | 0.0317 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.02 | 0.3679 | 0.3670 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.08 | 0.3998 | 0.3556 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.05 | 0.3889 | 0.3623 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.07 | 0.3950 | 0.3594 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.03 | 0.3772 | 0.3608 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.06 | 0.4030 | 0.3507 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.04 | 0.3970 | 0.3561 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.04 | 0.4010 | 0.3537 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.17 | 0.5523 | 0.1818 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.99 | 0.5460 | 0.1924 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.99 | 0.5460 | 0.1924 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.00 | 0.5434 | 0.1948 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.00 | 0.5434 | 0.1948 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.79 | 0.2985 | 0.2370 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.74 | 0.2805 | 0.2461 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.74 | 0.2805 | 0.2461 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.78 | 0.2826 | 0.2470 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.78 | 0.2826 | 0.2470 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.70 | 0.2676 | 0.2470 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.06 | 0.4229 | 0.3381 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.13 | 0.4498 | 0.3243 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.08 | 0.4430 | 0.3334 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.10 | 0.4475 | 0.3296 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.06 | 0.4241 | 0.3320 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.15 | 0.4552 | 0.3183 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.09 | 0.4469 | 0.3269 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.11 | 0.4518 | 0.3233 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.95 | 0.3603 | 0.2215 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.63 | 0.3451 | 0.3761 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.76 | 0.3654 | 0.3660 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.66 | 0.3583 | 0.3726 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.70 | 0.3623 | 0.3698 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.62 | 0.3593 | 0.3693 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.65 | 0.3759 | 0.3607 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.63 | 0.3738 | 0.3658 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.64 | 0.3761 | 0.3633 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.97 | 0.7349 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.71 | 0.7455 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.40 | 0.7410 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.52 | 0.7433 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.02 | 0.7363 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.87 | 0.7470 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.51 | 0.7426 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.68 | 0.7449 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.13 | 0.7370 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.00 | 0.7405 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.89 | 0.7382 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.77 | 0.7380 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.71 | 0.7362 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.08 | 0.7399 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.93 | 0.7399 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.87 | 0.7381 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.77 | 0.7378 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.76 | 0.7367 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.03 | 0.7372 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.56 | 0.7313 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.33 | 0.7406 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.96 | 0.7364 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.11 | 0.7384 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.12 | 0.7280 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.93 | 0.7394 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.61 | 0.7347 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.70 | 0.7367 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.73 | 0.7338 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.28 | 0.7387 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.79 | 0.7464 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.53 | 0.7426 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.60 | 0.7442 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.86 | 0.7461 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.16 | 0.7524 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.12 | 0.7509 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.16 | 0.7520 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.12 | 0.7180 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.12 | 0.7365 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.76 | 0.7297 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.90 | 0.7334 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.31 | 0.7221 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.26 | 0.7394 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.89 | 0.7338 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.06 | 0.7370 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.97 | 0.7329 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.43 | 0.7327 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.41 | 0.7326 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.34 | 0.7307 | 0.0393 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.35 | 0.7309 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.88 | 0.7360 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.32 | 0.7310 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.41 | 0.7320 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.32 | 0.7302 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.47 | 0.7321 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.22 | 0.7239 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.36 | 0.7057 | 0.0475 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.36 | 0.7237 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.00 | 0.7182 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.15 | 0.7214 | 0.0443 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.12 | 0.7052 | 0.0453 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.12 | 0.7271 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.75 | 0.7200 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.85 | 0.7235 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.70 | 0.7158 | 0.0437 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.68 | 0.7275 | 0.0410 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.33 | 0.7405 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.02 | 0.7351 | 0.0394 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.13 | 0.7377 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.38 | 0.7379 | 0.0366 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.81 | 0.7487 | 0.0326 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.73 | 0.7467 | 0.0344 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.78 | 0.7484 | 0.0335 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 77.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.88 | 0.7314 | 0.0349 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.96 | 0.3305 | 0.3833 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.99 | 0.3451 | 0.3736 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.97 | 0.3409 | 0.3791 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.98 | 0.3436 | 0.3765 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.94 | 0.3255 | 0.3800 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.96 | 0.3371 | 0.3727 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.95 | 0.3350 | 0.3769 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.95 | 0.3368 | 0.3750 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.28 | 0.5374 | 0.2416 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.50 | 0.5459 | 0.2529 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.50 | 0.5459 | 0.2529 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.50 | 0.5465 | 0.2530 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.50 | 0.5465 | 0.2530 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.36 | 0.1908 | 0.2833 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.39 | 0.1858 | 0.2870 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.39 | 0.1858 | 0.2870 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.42 | 0.1877 | 0.2865 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.42 | 0.1877 | 0.2865 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.35 | 0.1791 | 0.2864 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.56 | 0.3692 | 0.3549 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.61 | 0.3826 | 0.3423 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.58 | 0.3801 | 0.3498 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.59 | 0.3820 | 0.3460 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.56 | 0.3650 | 0.3498 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.61 | 0.3772 | 0.3376 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.58 | 0.3759 | 0.3448 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.59 | 0.3774 | 0.3412 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.09 | 0.2516 | 0.2590 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.72 | 0.3086 | 0.3940 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.84 | 0.3202 | 0.3870 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.75 | 0.3161 | 0.3912 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.79 | 0.3186 | 0.3891 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.68 | 0.3090 | 0.3906 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.70 | 0.3171 | 0.3855 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.69 | 0.3161 | 0.3884 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.69 | 0.3175 | 0.3869 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.84 | 0.7306 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.87 | 0.7314 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.86 | 0.7311 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.86 | 0.7313 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.82 | 0.7305 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.86 | 0.7312 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.84 | 0.7309 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.85 | 0.7311 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.89 | 0.7317 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.83 | 0.7312 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.83 | 0.7310 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.74 | 0.7308 | 0.0353 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.74 | 0.7306 | 0.0353 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.88 | 0.7316 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.84 | 0.7312 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.84 | 0.7311 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.84 | 0.7311 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.84 | 0.7310 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.79 | 0.7311 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.77 | 0.7298 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.83 | 0.7309 | 0.0353 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.81 | 0.7304 | 0.0354 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.82 | 0.7308 | 0.0353 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.72 | 0.7296 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.79 | 0.7305 | 0.0354 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.77 | 0.7301 | 0.0354 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.78 | 0.7304 | 0.0354 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.83 | 0.7312 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.83 | 0.7307 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.87 | 0.7313 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.85 | 0.7311 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.86 | 0.7312 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.71 | 0.7303 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7309 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.74 | 0.7307 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.76 | 0.7308 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.40 | 0.7259 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.61 | 0.7296 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.56 | 0.7285 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.58 | 0.7292 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.43 | 0.7264 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.57 | 0.7296 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.53 | 0.7288 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.56 | 0.7294 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.90 | 0.7322 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.52 | 0.7303 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.51 | 0.7298 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.56 | 0.7301 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.55 | 0.7297 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.86 | 0.7318 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.57 | 0.7304 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.59 | 0.7301 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.69 | 0.7304 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.72 | 0.7302 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.49 | 0.7291 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.12 | 0.7227 | 0.0415 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.40 | 0.7273 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.39 | 0.7265 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.41 | 0.7273 | 0.0398 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.12 | 0.7229 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.39 | 0.7280 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.32 | 0.7268 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.37 | 0.7277 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.46 | 0.7293 | 0.0393 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.64 | 0.7288 | 0.0377 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.75 | 0.7308 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.71 | 0.7301 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.73 | 0.7305 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.38 | 0.7269 | 0.0381 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.53 | 0.7291 | 0.0374 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.46 | 0.7286 | 0.0377 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.49 | 0.7290 | 0.0375 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.22 | 0.7317 | 0.0554 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.47 | 0.3412 | 0.4640 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.53 | 0.3665 | 0.4441 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.50 | 0.3575 | 0.4562 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.51 | 0.3626 | 0.4506 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.46 | 0.3382 | 0.4532 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.48 | 0.3591 | 0.4369 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.47 | 0.3533 | 0.4456 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.47 | 0.3570 | 0.4414 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.55 | 0.5385 | 0.3420 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.67 | 0.5395 | 0.3536 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.67 | 0.5395 | 0.3536 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.66 | 0.5377 | 0.3562 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.66 | 0.5377 | 0.3562 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.59 | 0.2389 | 0.3704 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.59 | 0.2272 | 0.3794 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.59 | 0.2272 | 0.3794 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.61 | 0.2282 | 0.3808 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.61 | 0.2282 | 0.3808 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.54 | 0.2182 | 0.3797 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.14 | 0.3807 | 0.4305 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.19 | 0.4036 | 0.4075 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.16 | 0.3965 | 0.4226 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.17 | 0.4006 | 0.4156 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.13 | 0.3750 | 0.4184 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.18 | 0.3957 | 0.3979 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.15 | 0.3899 | 0.4111 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.16 | 0.3935 | 0.4051 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.36 | 0.2895 | 0.3385 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.18 | 0.3157 | 0.4743 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.31 | 0.3351 | 0.4603 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.22 | 0.3273 | 0.4691 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.26 | 0.3315 | 0.4651 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.15 | 0.3220 | 0.4607 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.17 | 0.3361 | 0.4484 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.16 | 0.3333 | 0.4559 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.17 | 0.3356 | 0.4520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.30 | 0.7295 | 0.0601 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.72 | 0.7354 | 0.0563 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.55 | 0.7329 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.62 | 0.7342 | 0.0574 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.27 | 0.7296 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.77 | 0.7356 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.56 | 0.7331 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.66 | 0.7344 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.42 | 0.7319 | 0.0616 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.23 | 0.7323 | 0.0591 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.14 | 0.7307 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.07 | 0.7308 | 0.0599 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.99 | 0.7295 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.39 | 0.7330 | 0.0560 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.19 | 0.7322 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.14 | 0.7310 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.10 | 0.7311 | 0.0585 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.07 | 0.7303 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.30 | 0.7312 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.96 | 0.7263 | 0.0642 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.46 | 0.7321 | 0.0600 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.22 | 0.7295 | 0.0630 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.32 | 0.7308 | 0.0617 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.72 | 0.7245 | 0.0626 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.19 | 0.7309 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.00 | 0.7281 | 0.0609 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.06 | 0.7294 | 0.0598 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.07 | 0.7293 | 0.0598 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.42 | 0.7310 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.73 | 0.7354 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.58 | 0.7332 | 0.0569 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.63 | 0.7342 | 0.0563 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.65 | 0.7340 | 0.0552 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.85 | 0.7379 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.80 | 0.7368 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.83 | 0.7375 | 0.0530 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.74 | 0.7200 | 0.0683 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.38 | 0.7308 | 0.0611 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.16 | 0.7269 | 0.0647 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.25 | 0.7290 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.79 | 0.7210 | 0.0635 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.38 | 0.7311 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.15 | 0.7276 | 0.0605 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.27 | 0.7297 | 0.0590 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.35 | 0.7303 | 0.0637 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.83 | 0.7283 | 0.0641 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.78 | 0.7273 | 0.0622 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.74 | 0.7270 | 0.0643 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.70 | 0.7264 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.29 | 0.7314 | 0.0573 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.78 | 0.7276 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.80 | 0.7276 | 0.0610 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.78 | 0.7271 | 0.0627 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.82 | 0.7275 | 0.0605 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.77 | 0.7245 | 0.0657 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.15 | 0.7119 | 0.0786 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.87 | 0.7231 | 0.0703 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.60 | 0.7195 | 0.0758 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.72 | 0.7216 | 0.0732 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.00 | 0.7109 | 0.0745 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.65 | 0.7237 | 0.0659 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.41 | 0.7193 | 0.0709 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.49 | 0.7216 | 0.0687 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.39 | 0.7204 | 0.0691 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.04 | 0.7245 | 0.0670 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.46 | 0.7320 | 0.0618 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.27 | 0.7289 | 0.0650 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.35 | 0.7304 | 0.0635 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.29 | 0.7279 | 0.0627 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.58 | 0.7346 | 0.0581 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.49 | 0.7331 | 0.0602 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.53 | 0.7342 | 0.0592 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 327077 | 0.170 | 33.3 | 29.50 | 0.21 | 0.037 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 327077 | 0.170 | 35.1 | 29.50 | 0.21 | 0.037 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 327077 | 0.170 | 34.9 | 29.50 | 0.21 | 0.037 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 327077 | 0.170 | 38.4 | 29.50 | 0.21 | 0.037 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 850 | None | classic | 1.08 | False | 363650 | 0.356 | 64.8 | 28.19 | 0.11 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 850 | None | classic | 1.08 | False | 363650 | 0.356 | 68.0 | 28.19 | 0.11 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 850 | None | classic | 1.08 | False | 363650 | 0.356 | 59.6 | 28.19 | 0.11 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 850 | None | classic | 1.08 | False | 363650 | 0.356 | 63.8 | 28.19 | 0.11 | 0.019 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1311182 | 0.148 | 27.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1311100 | 0.810 | 52.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1311100 | 0.810 | 52.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1311182 | 0.639 | 27.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1311182 | 0.639 | 27.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1311182 | 0.148 | 34.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1311100 | 0.810 | 75.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1311100 | 0.810 | 75.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1311182 | 0.639 | 34.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1311182 | 0.639 | 34.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1309568 | 0.810 | 160.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 314717 | 0.170 | 35.4 | 29.37 | 0.22 | 0.031 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 314717 | 0.170 | 32.4 | 29.37 | 0.22 | 0.031 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 314717 | 0.170 | 31.2 | 29.37 | 0.22 | 0.031 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 314717 | 0.170 | 35.2 | 29.37 | 0.22 | 0.031 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 967 | None | classic | 1.40 | False | 498741 | 0.524 | 84.2 | 27.96 | 0.20 | 0.042 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 967 | None | classic | 1.40 | False | 498741 | 0.524 | 83.5 | 27.96 | 0.20 | 0.042 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 967 | None | classic | 1.40 | False | 498741 | 0.524 | 84.7 | 27.96 | 0.20 | 0.042 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 967 | None | classic | 1.40 | False | 498741 | 0.524 | 97.3 | 27.96 | 0.20 | 0.042 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1671125 | 0.810 | 76.3 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 304220 | 0.322 | 43.6 | 29.76 | 0.05 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 304220 | 0.322 | 29.0 | 29.76 | 0.05 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 304220 | 0.322 | 29.6 | 29.76 | 0.05 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 304220 | 0.322 | 29.9 | 29.76 | 0.05 | 0.027 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 705 | None | classic | 0.54 | False | 738069 | 0.688 | 121.9 | 28.25 | 0.11 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 705 | None | classic | 0.54 | False | 738069 | 0.688 | 112.8 | 28.25 | 0.11 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 705 | None | classic | 0.54 | False | 738069 | 0.688 | 116.0 | 28.25 | 0.11 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 705 | None | classic | 0.54 | False | 738069 | 0.688 | 114.6 | 28.25 | 0.11 | 0.013 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.589 | 0.030 |
| in035 | mask_ent | 0.728 | 0.030 |
| in035 | mask_grad | 0.416 | 0.030 |
| in035 | r_col | 0.777 | 0.030 |
| in035 | r_warp | 0.850 | 0.030 |

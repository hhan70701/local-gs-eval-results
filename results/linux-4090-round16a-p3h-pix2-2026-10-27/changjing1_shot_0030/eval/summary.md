# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 10.0% | 23.99 / 0.0120 | 20.81 / 0.0281 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 10.6% | 24.11 / 0.0122 | 21.31 / 0.0253 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 10.4% | 24.06 / 0.0122 | 21.35 / 0.0261 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 10.5% | 24.10 / 0.0122 | 21.37 / 0.0252 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.0% | 23.97 / 0.0115 | 23.41 / 0.0191 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.3% | 24.01 / 0.0115 | 23.75 / 0.0169 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.1% | 23.99 / 0.0114 | 24.18 / 0.0173 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 10.2% | 24.00 / 0.0115 | 24.10 / 0.0168 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 9.1% | 23.77 / 0.0117 | 22.85 / 0.0239 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 8.4% | 23.48 / 0.0114 | 24.33 / 0.0199 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.6% | 20.55 / 0.0075 | 19.62 / 0.0138 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 8.5% | 23.49 / 0.0116 | 24.53 / 0.0198 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.4% | 20.34 / 0.0073 | 19.70 / 0.0132 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 9.1% | 23.74 / 0.0120 | 22.81 / 0.0176 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 8.4% | 23.41 / 0.0116 | 24.07 / 0.0195 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.6% | 20.77 / 0.0079 | 19.51 / 0.0133 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 8.5% | 23.43 / 0.0119 | 24.23 / 0.0197 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.3% | 20.52 / 0.0079 | 19.48 / 0.0129 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 10.1% | 23.68 / 0.0128 | 21.18 / 0.0326 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 13.9% | 25.17 / 0.0144 | 21.42 / 0.0383 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.7% | 25.33 / 0.0147 | 22.65 / 0.0300 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 14.6% | 25.28 / 0.0147 | 22.54 / 0.0342 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.6% | 25.32 / 0.0148 | 22.60 / 0.0317 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 13.9% | 25.21 / 0.0137 | 22.20 / 0.0320 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.6% | 25.22 / 0.0141 | 23.30 / 0.0271 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.4% | 25.24 / 0.0140 | 23.23 / 0.0289 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.5% | 25.24 / 0.0141 | 23.29 / 0.0278 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 14.3% | 24.93 / 0.0149 | 21.09 / 0.0455 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 10.5% | 23.76 / 0.0146 | 20.54 / 0.0366 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 12.1% | 24.08 / 0.0160 | 21.91 / 0.0337 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 11.5% | 23.93 / 0.0151 | 21.41 / 0.0349 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 11.7% | 23.98 / 0.0152 | 21.73 / 0.0342 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 10.5% | 23.85 / 0.0147 | 22.36 / 0.0309 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 11.7% | 24.06 / 0.0162 | 22.70 / 0.0292 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 11.3% | 23.98 / 0.0152 | 22.89 / 0.0290 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 11.4% | 24.00 / 0.0155 | 22.80 / 0.0284 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.35 / 0.0570 | 23.55 / 0.0797 | 20.01 / 0.0168 | 29.98 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.44 / 0.0703 | 22.26 / 0.1339 | 19.58 / 0.0198 | 29.49 / 0.0396 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.65 / 0.0669 | 22.74 / 0.1193 | 19.78 / 0.0184 | 29.44 / 0.0394 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.68 / 0.0690 | 22.79 / 0.1267 | 19.78 / 0.0191 | 29.56 / 0.0396 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.69 / 0.0680 | 22.81 / 0.1224 | 19.81 / 0.0188 | 29.52 / 0.0394 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.33 / 0.0644 | 24.15 / 0.1006 | 20.65 / 0.0171 | 29.83 / 0.0381 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.49 / 0.0610 | 24.50 / 0.0870 | 20.78 / 0.0168 | 29.82 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.53 / 0.0627 | 24.65 / 0.0923 | 20.84 / 0.0167 | 29.88 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.53 / 0.0615 | 24.64 / 0.0869 | 20.83 / 0.0168 | 29.87 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.49 / 0.0635 | 24.45 / 0.1074 | 20.91 / 0.0193 | 29.87 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.67 / 0.0603 | 25.86 / 0.0770 | 21.14 / 0.0165 | 29.96 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.53 / 0.0589 | 25.13 / 0.0766 | 20.73 / 0.0171 | 29.94 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.65 / 0.0618 | 25.62 / 0.0796 | 21.04 / 0.0176 | 29.96 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.53 / 0.0604 | 24.99 / 0.0772 | 20.64 / 0.0181 | 29.96 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.50 / 0.0599 | 24.35 / 0.0932 | 20.89 / 0.0172 | 29.89 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.64 / 0.0603 | 25.49 / 0.0813 | 21.06 / 0.0164 | 29.95 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.54 / 0.0583 | 25.09 / 0.0744 | 20.72 / 0.0168 | 29.94 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.61 / 0.0616 | 25.21 / 0.0861 | 20.98 / 0.0173 | 29.96 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.50 / 0.0596 | 24.77 / 0.0782 | 20.60 / 0.0177 | 29.95 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.30 / 0.0653 | 23.88 / 0.1169 | 20.77 / 0.0177 | 29.87 / 0.0388 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.17 / 0.0792 | 22.47 / 0.1321 | 19.65 / 0.0204 | 29.36 / 0.0450 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.64 / 0.0721 | 23.52 / 0.1117 | 20.11 / 0.0183 | 29.51 / 0.0432 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.64 / 0.0758 | 23.38 / 0.1210 | 20.10 / 0.0189 | 29.50 / 0.0440 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.65 / 0.0740 | 23.53 / 0.1160 | 20.14 / 0.0188 | 29.50 / 0.0435 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.42 / 0.0752 | 22.47 / 0.1300 | 19.77 / 0.0200 | 29.57 / 0.0418 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.89 / 0.0683 | 23.36 / 0.1120 | 20.29 / 0.0176 | 29.71 / 0.0399 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.82 / 0.0720 | 23.16 / 0.1221 | 20.18 / 0.0186 | 29.71 / 0.0409 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.85 / 0.0702 | 23.21 / 0.1177 | 20.24 / 0.0182 | 29.71 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.73 / 0.0730 | 23.32 / 0.1304 | 20.31 / 0.0197 | 29.63 / 0.0420 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.46 / 0.0748 | 21.78 / 0.1499 | 19.91 / 0.0193 | 29.45 / 0.0407 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.80 / 0.0712 | 22.83 / 0.1267 | 20.16 / 0.0188 | 29.55 / 0.0400 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.72 / 0.0735 | 22.40 / 0.1411 | 20.10 / 0.0190 | 29.53 / 0.0404 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.78 / 0.0724 | 22.65 / 0.1363 | 20.16 / 0.0189 | 29.54 / 0.0402 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.96 / 0.0716 | 23.44 / 0.1258 | 20.42 / 0.0185 | 29.60 / 0.0405 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.07 / 0.0676 | 23.69 / 0.1102 | 20.54 / 0.0168 | 29.59 / 0.0406 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.13 / 0.0696 | 23.81 / 0.1158 | 20.60 / 0.0174 | 29.64 / 0.0406 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.10 / 0.0684 | 23.80 / 0.1113 | 20.60 / 0.0170 | 29.60 / 0.0405 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 8.8%） | — | — | 27.35 / 0.0570 | 23.55 / 0.0797 | 29.98 |
| in035 | rife | 4.3% | 10.5% | 26.46 / 0.0748 | 21.78 / 0.1499 | 29.45 |
| in035 | cnw_cnn | 5.4% | 10.0% | 26.44 / 0.0703 | 22.26 / 0.1339 | 29.49 |
| in035 | cnw_f5 | 7.9% | 13.9% | 26.17 / 0.0792 | 22.47 / 0.1321 | 29.36 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.12 / 0.0564 | -0.63 / +0.0239 (core 4.9%) | -0.15 / +0.0128 (core 5.4%) | -0.60 / +0.0221 (core 8.2%) |
| in035 | 2 | 0-3 | 27.51 / 0.0564 | -1.15 / +0.0189 (core 4.9%) | -1.16 / +0.0165 (core 5.4%) | -1.35 / +0.0247 (core 8.2%) |
| in035 | 4 | 3-5 | 28.44 / 0.0582 | -0.90 / +0.0105 (core 2.2%) | -1.41 / +0.0108 (core 3.2%) | -1.60 / +0.0199 (core 4.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.35 / 0.0570 | 23.55 | 29.98 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.44 / 0.0703 | 22.26 | 29.49 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 27.06 / 0.0621 | 23.27 | 29.82 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.65 / 0.0669 | 22.74 | 29.44 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 27.19 / 0.0602 | 23.71 | 29.82 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.68 / 0.0690 | 22.79 | 29.56 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 27.17 / 0.0614 | 23.64 | 29.83 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.69 / 0.0680 | 22.81 | 29.52 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 27.19 / 0.0609 | 23.70 | 29.82 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.33 / 0.0644 | 24.15 | 29.83 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 27.64 / 0.0586 | 24.70 | 29.95 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.49 / 0.0610 | 24.50 | 29.82 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 27.70 / 0.0576 | 24.97 | 29.94 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.53 / 0.0627 | 24.65 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 27.73 / 0.0582 | 25.03 | 29.95 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.53 / 0.0615 | 24.64 | 29.87 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 27.73 / 0.0578 | 25.02 | 29.95 | 1/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 27.49 / 0.0635 | 24.45 | 29.87 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 2.3% | 27.70 / 0.0598 | 24.91 | 29.97 | 1/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 27.67 / 0.0603 | 25.86 | 29.96 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 2.3% | 27.85 / 0.0569 | 25.88 | 29.98 | 1/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 27.53 / 0.0589 | 25.13 | 29.94 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 1.3% | 27.69 / 0.0572 | 25.19 | 29.98 | 1/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.65 / 0.0618 | 25.62 | 29.96 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 2.3% | 27.80 / 0.0582 | 25.64 | 29.98 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.53 / 0.0604 | 24.99 | 29.96 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 1.3% | 27.65 / 0.0585 | 24.99 | 29.98 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.50 / 0.0599 | 24.35 | 29.89 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 2.3% | 27.71 / 0.0575 | 24.83 | 29.97 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.64 / 0.0603 | 25.49 | 29.95 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.3% | 27.83 / 0.0567 | 25.61 | 29.98 | 2/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.54 / 0.0583 | 25.09 | 29.94 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.3% | 27.70 / 0.0567 | 25.14 | 29.98 | 2/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.61 / 0.0616 | 25.21 | 29.96 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 2.3% | 27.78 / 0.0580 | 25.35 | 29.98 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.50 / 0.0596 | 24.77 | 29.95 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 1.2% | 27.63 / 0.0579 | 24.81 | 29.98 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.30 / 0.0653 | 23.88 | 29.87 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.6% | 27.67 / 0.0581 | 24.91 | 29.98 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.17 / 0.0792 | 22.47 | 29.36 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 27.02 / 0.0627 | 23.53 | 29.89 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.64 / 0.0721 | 23.52 | 29.51 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 27.31 / 0.0603 | 24.19 | 29.92 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.64 / 0.0758 | 23.38 | 29.50 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 27.30 / 0.0615 | 24.09 | 29.90 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.65 / 0.0740 | 23.53 | 29.50 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 27.33 / 0.0610 | 24.20 | 29.92 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.42 / 0.0752 | 22.47 | 29.57 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.5% | 27.13 / 0.0621 | 23.48 | 29.95 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.89 / 0.0683 | 23.36 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 27.40 / 0.0595 | 24.14 | 29.96 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.82 / 0.0720 | 23.16 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.6% | 27.34 / 0.0610 | 23.95 | 29.96 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.85 / 0.0702 | 23.21 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.6% | 27.38 / 0.0603 | 24.04 | 29.96 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.73 / 0.0730 | 23.32 | 29.63 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.8% | 27.42 / 0.0601 | 24.52 | 29.97 | 0/3 |
| in035 | rife | 不复核 | —% | 26.46 / 0.0748 | 21.78 | 29.45 | 0/3 |
| in035 | rife | oracle | 2.4% | 27.18 / 0.0617 | 23.16 | 29.87 | 0/3 |
| in035 | rife | 不复核 | —% | 26.80 / 0.0712 | 22.83 | 29.55 | 0/3 |
| in035 | rife | oracle | 2.6% | 27.37 / 0.0607 | 23.96 | 29.89 | 0/3 |
| in035 | rife | 不复核 | —% | 26.72 / 0.0735 | 22.40 | 29.53 | 0/3 |
| in035 | rife | oracle | 2.5% | 27.32 / 0.0615 | 23.64 | 29.89 | 0/3 |
| in035 | rife | 不复核 | —% | 26.78 / 0.0724 | 22.65 | 29.54 | 0/3 |
| in035 | rife | oracle | 2.6% | 27.36 / 0.0612 | 23.85 | 29.89 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.96 / 0.0716 | 23.44 | 29.60 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 27.48 / 0.0601 | 24.43 | 29.92 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.07 / 0.0676 | 23.69 | 29.59 | 0/3 |
| in035 | rife_mw | oracle | 2.5% | 27.57 / 0.0584 | 24.70 | 29.89 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.13 / 0.0696 | 23.81 | 29.64 | 0/3 |
| in035 | rife_mw | oracle | 2.4% | 27.58 / 0.0593 | 24.73 | 29.91 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.10 / 0.0684 | 23.80 | 29.60 | 0/3 |
| in035 | rife_mw | oracle | 2.4% | 27.58 / 0.0586 | 24.76 | 29.89 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.35 / 0.0570 | 23.55 / 0.0797 | — |
| in035 | FF | 0（前馈） | 1008×670（64%） | 26.41 | 26.44 / 0.0703 | 22.26 / 0.1339 | 0/3 |
| in035 | 25 | 0.63 s | 1008×670（64%） | 27.20 | 26.68 / 0.0690 | 22.79 / 0.1267 | 0/3 |
| in035 | 50 | 1.26 s | 1008×670（64%） | 27.56 | 26.69 / 0.0680 | 22.81 / 0.1224 | 0/3 |
| in035 | 100 | 2.50 s | 1008×670（64%） | 27.93 | 26.65 / 0.0669 | 22.74 / 0.1193 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.35 / 0.0570 | 23.55 / 0.0797 | 29.98 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.44 / 0.0703 | 22.26 / 0.1339 | 29.49 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.06 / 0.0621 | 23.27 / 0.1092 | 29.82 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 26.68 / 0.0690 | 22.79 / 0.1267 | 29.56 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.17 / 0.0614 | 23.64 / 0.1055 | 29.83 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 26.69 / 0.0680 | 22.81 / 0.1224 | 29.52 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.19 / 0.0609 | 23.70 / 0.1023 | 29.82 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 26.65 / 0.0669 | 22.74 / 0.1193 | 29.44 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.19 / 0.0602 | 23.71 / 0.0998 | 29.82 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.33 / 0.0644 | 24.15 / 0.1006 | 29.83 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.64 / 0.0586 | 24.70 / 0.0855 | 29.95 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.53 / 0.0627 | 24.65 / 0.0923 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.73 / 0.0582 | 25.03 / 0.0812 | 29.95 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.53 / 0.0615 | 24.64 / 0.0869 | 29.87 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.73 / 0.0578 | 25.02 / 0.0781 | 29.95 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.49 / 0.0610 | 24.50 / 0.0870 | 29.82 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.70 / 0.0576 | 24.97 / 0.0771 | 29.94 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.17 / 0.0792 | 22.47 / 0.1321 | 29.36 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.02 / 0.0627 | 23.53 / 0.1015 | 29.89 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.64 / 0.0758 | 23.38 / 0.1210 | 29.50 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.30 / 0.0615 | 24.09 / 0.0951 | 29.90 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.65 / 0.0740 | 23.53 / 0.1160 | 29.50 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.33 / 0.0610 | 24.20 / 0.0926 | 29.92 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.64 / 0.0721 | 23.52 / 0.1117 | 29.51 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.31 / 0.0603 | 24.19 / 0.0908 | 29.92 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.42 / 0.0752 | 22.47 / 0.1300 | 29.57 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.13 / 0.0621 | 23.48 / 0.1006 | 29.95 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.82 / 0.0720 | 23.16 / 0.1221 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.34 / 0.0610 | 23.95 / 0.0951 | 29.96 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.85 / 0.0702 | 23.21 / 0.1177 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.38 / 0.0603 | 24.04 / 0.0913 | 29.96 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 26.89 / 0.0683 | 23.36 / 0.1120 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.40 / 0.0595 | 24.14 / 0.0877 | 29.96 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.46 / 0.0748 | 21.78 / 0.1499 | 29.45 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.18 / 0.0617 | 23.16 / 0.1073 | 29.87 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 26.72 / 0.0735 | 22.40 / 0.1411 | 29.53 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.32 / 0.0615 | 23.64 / 0.1020 | 29.89 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 26.78 / 0.0724 | 22.65 / 0.1363 | 29.54 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.36 / 0.0612 | 23.85 / 0.0997 | 29.89 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.80 / 0.0712 | 22.83 / 0.1267 | 29.55 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.37 / 0.0607 | 23.96 / 0.0951 | 29.89 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.96 / 0.0716 | 23.44 / 0.1258 | 29.60 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.48 / 0.0601 | 24.43 / 0.0917 | 29.92 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.13 / 0.0696 | 23.81 / 0.1158 | 29.64 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.58 / 0.0593 | 24.73 / 0.0861 | 29.91 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.10 / 0.0684 | 23.80 / 0.1113 | 29.60 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.58 / 0.0586 | 24.76 / 0.0833 | 29.89 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.07 / 0.0676 | 23.69 / 0.1102 | 29.59 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.57 / 0.0584 | 24.70 / 0.0828 | 29.89 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.55 / 0.0797 | 20.01 / 0.0168 | 29.98 / 0.0357 | 27.35 / 0.0570 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 12.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.55 | 0.7212 | 0.0797 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 16.96 | 0.5427 | 0.2565 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 17.69 | 0.5785 | 0.2135 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 17.91 | 0.5839 | 0.2341 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 17.92 | 0.5855 | 0.2229 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 16.98 | 0.6436 | 0.1999 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 17.51 | 0.6701 | 0.1678 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 17.50 | 0.6788 | 0.1829 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 17.51 | 0.6804 | 0.1718 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 24.62 | 0.7769 | 0.1279 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 25.56 | 0.8135 | 0.1018 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 25.56 | 0.8135 | 0.1018 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 25.24 | 0.7972 | 0.1046 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 25.24 | 0.7972 | 0.1046 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 18.21 | 0.7186 | 0.1711 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 18.95 | 0.7374 | 0.1687 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 18.95 | 0.7374 | 0.1687 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 18.77 | 0.7240 | 0.1746 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 18.77 | 0.7240 | 0.1746 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.84 | 0.6728 | 0.2073 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 13.93 | 0.5433 | 0.2899 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.97 | 0.6032 | 0.2300 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 14.48 | 0.5954 | 0.2592 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.65 | 0.6032 | 0.2445 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 14.03 | 0.5485 | 0.2653 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.59 | 0.6175 | 0.2277 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.45 | 0.6046 | 0.2476 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.52 | 0.6144 | 0.2392 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.69 | 0.6244 | 0.2493 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.07 | 0.5096 | 0.2781 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 15.54 | 0.5822 | 0.2290 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 15.06 | 0.5614 | 0.2589 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 15.40 | 0.5783 | 0.2475 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 13.59 | 0.5869 | 0.2570 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 14.80 | 0.6166 | 0.2186 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 14.03 | 0.6193 | 0.2392 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 14.37 | 0.6217 | 0.2281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 23.27 | 0.6998 | 0.1092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.71 | 0.7130 | 0.0998 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.64 | 0.7130 | 0.1055 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.70 | 0.7151 | 0.1023 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.70 | 0.7432 | 0.0855 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.97 | 0.7571 | 0.0771 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.03 | 0.7549 | 0.0812 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.02 | 0.7573 | 0.0781 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.91 | 0.7652 | 0.0931 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.88 | 0.7874 | 0.0712 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.19 | 0.7668 | 0.0738 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.64 | 0.7792 | 0.0737 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.99 | 0.7600 | 0.0761 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.83 | 0.7656 | 0.0865 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.61 | 0.7813 | 0.0738 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.14 | 0.7658 | 0.0718 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.35 | 0.7734 | 0.0766 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.81 | 0.7554 | 0.0761 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.91 | 0.7724 | 0.0863 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 23.53 | 0.7129 | 0.1015 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.19 | 0.7315 | 0.0908 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.09 | 0.7284 | 0.0951 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.20 | 0.7316 | 0.0926 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.48 | 0.7111 | 0.1006 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.14 | 0.7315 | 0.0877 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.95 | 0.7238 | 0.0951 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.04 | 0.7279 | 0.0913 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.52 | 0.7576 | 0.0881 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.16 | 0.7016 | 0.1073 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 23.96 | 0.7246 | 0.0951 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 23.64 | 0.7176 | 0.1020 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 23.85 | 0.7235 | 0.0997 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 24.43 | 0.7404 | 0.0917 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.70 | 0.7542 | 0.0828 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.73 | 0.7521 | 0.0861 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.76 | 0.7546 | 0.0833 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.26 | 0.6552 | 0.1339 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.74 | 0.6682 | 0.1193 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.79 | 0.6736 | 0.1267 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.81 | 0.6729 | 0.1224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.15 | 0.7245 | 0.1006 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.50 | 0.7428 | 0.0870 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.65 | 0.7434 | 0.0923 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.64 | 0.7462 | 0.0869 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.45 | 0.7513 | 0.1074 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.86 | 0.7866 | 0.0770 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.13 | 0.7655 | 0.0766 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.62 | 0.7750 | 0.0796 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.99 | 0.7594 | 0.0772 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.35 | 0.7543 | 0.0932 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.49 | 0.7770 | 0.0813 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.09 | 0.7640 | 0.0744 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.21 | 0.7671 | 0.0861 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.77 | 0.7534 | 0.0782 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.88 | 0.7460 | 0.1169 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.47 | 0.6688 | 0.1321 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.52 | 0.7017 | 0.1117 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.38 | 0.6957 | 0.1210 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.53 | 0.7012 | 0.1160 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.47 | 0.6684 | 0.1300 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.36 | 0.7012 | 0.1120 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.16 | 0.6932 | 0.1221 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.21 | 0.6980 | 0.1177 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.32 | 0.7238 | 0.1304 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.78 | 0.6411 | 0.1499 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.83 | 0.6787 | 0.1267 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.40 | 0.6658 | 0.1411 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.65 | 0.6759 | 0.1363 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.44 | 0.7032 | 0.1258 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.69 | 0.7192 | 0.1102 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.81 | 0.7201 | 0.1158 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.80 | 0.7220 | 0.1113 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 8.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.01 | 0.5857 | 0.0168 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.10 | 0.2995 | 0.1102 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.37 | 0.3306 | 0.1028 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.24 | 0.3281 | 0.1069 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.32 | 0.3330 | 0.1052 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.28 | 0.4016 | 0.1068 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.45 | 0.4412 | 0.1013 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.35 | 0.4314 | 0.1042 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.39 | 0.4397 | 0.1028 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.72 | 0.5561 | 0.0524 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.63 | 0.5607 | 0.0514 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.63 | 0.5607 | 0.0514 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.59 | 0.5440 | 0.0529 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.59 | 0.5440 | 0.0529 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.14 | 0.4856 | 0.0660 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.23 | 0.4768 | 0.0679 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.23 | 0.4768 | 0.0679 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.17 | 0.4631 | 0.0699 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.17 | 0.4631 | 0.0699 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.06 | 0.4518 | 0.0678 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.02 | 0.3259 | 0.0993 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.49 | 0.3735 | 0.0909 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.23 | 0.3619 | 0.0950 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.35 | 0.3691 | 0.0933 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.16 | 0.3516 | 0.0961 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.30 | 0.3968 | 0.0901 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.25 | 0.3854 | 0.0935 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.27 | 0.3924 | 0.0921 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.53 | 0.4013 | 0.0668 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.80 | 0.2408 | 0.1254 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.15 | 0.2776 | 0.1191 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.93 | 0.2641 | 0.1228 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.03 | 0.2736 | 0.1212 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.71 | 0.3064 | 0.1228 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.90 | 0.3359 | 0.1172 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.80 | 0.3309 | 0.1206 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.85 | 0.3362 | 0.1190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.60 | 0.5570 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.81 | 0.5688 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.80 | 0.5677 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.82 | 0.5696 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.65 | 0.6119 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.78 | 0.6322 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.83 | 0.6256 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.82 | 0.6301 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.90 | 0.6412 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.10 | 0.6589 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.71 | 0.6316 | 0.0171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 21.01 | 0.6506 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.63 | 0.6240 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.89 | 0.6419 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.04 | 0.6540 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.71 | 0.6299 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.96 | 0.6455 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.59 | 0.6186 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.77 | 0.6448 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.67 | 0.5722 | 0.0203 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.11 | 0.5951 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.09 | 0.5896 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.12 | 0.5934 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.80 | 0.5812 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.30 | 0.6079 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.19 | 0.5977 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.25 | 0.6032 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.32 | 0.6193 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.94 | 0.5703 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.20 | 0.5884 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.13 | 0.5823 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.20 | 0.5873 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.44 | 0.6097 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.55 | 0.6276 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.61 | 0.6232 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.61 | 0.6274 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.58 | 0.5544 | 0.0198 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.78 | 0.5665 | 0.0184 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.78 | 0.5658 | 0.0191 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.81 | 0.5673 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.65 | 0.6108 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.78 | 0.6314 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.84 | 0.6250 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.83 | 0.6296 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.91 | 0.6410 | 0.0193 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.14 | 0.6596 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.73 | 0.6320 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 21.04 | 0.6511 | 0.0176 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.64 | 0.6240 | 0.0181 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.89 | 0.6415 | 0.0172 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.06 | 0.6540 | 0.0164 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.72 | 0.6298 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.98 | 0.6457 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.60 | 0.6185 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.77 | 0.6430 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.65 | 0.5694 | 0.0204 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.11 | 0.5945 | 0.0183 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.10 | 0.5885 | 0.0189 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.14 | 0.5925 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.77 | 0.5791 | 0.0200 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.29 | 0.6065 | 0.0176 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.18 | 0.5965 | 0.0186 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.24 | 0.6020 | 0.0182 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.31 | 0.6170 | 0.0197 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.91 | 0.5674 | 0.0193 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.16 | 0.5856 | 0.0188 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.10 | 0.5791 | 0.0190 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.16 | 0.5843 | 0.0189 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.42 | 0.6078 | 0.0185 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.54 | 0.6261 | 0.0168 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.60 | 0.6218 | 0.0174 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.60 | 0.6260 | 0.0170 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 31.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.19 | 0.7561 | 0.0254 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.91 | 0.4426 | 0.2376 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.30 | 0.4680 | 0.2207 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.07 | 0.4653 | 0.2308 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.18 | 0.4672 | 0.2263 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.93 | 0.4808 | 0.2282 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.26 | 0.5043 | 0.2134 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.02 | 0.5021 | 0.2229 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.11 | 0.5044 | 0.2189 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 19.12 | 0.6329 | 0.1105 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 18.73 | 0.6343 | 0.1158 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 18.73 | 0.6343 | 0.1158 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 18.81 | 0.6272 | 0.1166 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 18.81 | 0.6272 | 0.1166 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.47 | 0.4523 | 0.1606 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.31 | 0.4225 | 0.1779 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.31 | 0.4225 | 0.1779 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.28 | 0.4153 | 0.1786 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.28 | 0.4153 | 0.1786 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.04 | 0.3718 | 0.1853 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.96 | 0.4904 | 0.2121 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.45 | 0.5326 | 0.1909 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.18 | 0.5247 | 0.2022 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.29 | 0.5298 | 0.1971 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.20 | 0.5172 | 0.2026 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.62 | 0.5552 | 0.1840 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.35 | 0.5488 | 0.1950 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.45 | 0.5529 | 0.1907 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.44 | 0.4120 | 0.1723 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.64 | 0.4352 | 0.2358 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.99 | 0.4681 | 0.2190 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.78 | 0.4595 | 0.2289 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.88 | 0.4660 | 0.2245 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.66 | 0.4681 | 0.2303 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.92 | 0.4885 | 0.2166 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.74 | 0.4909 | 0.2235 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.81 | 0.4917 | 0.2203 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.00 | 0.7512 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.27 | 0.7576 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.20 | 0.7565 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.23 | 0.7573 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.64 | 0.7634 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.83 | 0.7697 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.85 | 0.7682 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.85 | 0.7694 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.61 | 0.7657 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.83 | 0.7743 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.57 | 0.7673 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.74 | 0.7708 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.50 | 0.7647 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.64 | 0.7685 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.79 | 0.7733 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.61 | 0.7677 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.70 | 0.7699 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.51 | 0.7639 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.26 | 0.7632 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.56 | 0.7462 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.13 | 0.7576 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.07 | 0.7550 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.12 | 0.7564 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.65 | 0.7474 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.25 | 0.7582 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.11 | 0.7549 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.19 | 0.7568 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.75 | 0.7513 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.98 | 0.7478 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.39 | 0.7568 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.24 | 0.7542 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.35 | 0.7564 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.52 | 0.7603 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.74 | 0.7681 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.73 | 0.7664 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.76 | 0.7679 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.81 | 0.7247 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.19 | 0.7335 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.13 | 0.7336 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.13 | 0.7335 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.99 | 0.7499 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.20 | 0.7576 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.36 | 0.7587 | 0.0311 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.32 | 0.7591 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.77 | 0.7422 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.27 | 0.7621 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.10 | 0.7585 | 0.0304 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.29 | 0.7593 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.13 | 0.7574 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.79 | 0.7515 | 0.0312 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.26 | 0.7605 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.19 | 0.7583 | 0.0299 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.28 | 0.7583 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.19 | 0.7561 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.31 | 0.7265 | 0.0448 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.09 | 0.7072 | 0.0445 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.84 | 0.7281 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.83 | 0.7246 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.84 | 0.7268 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.39 | 0.7162 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.13 | 0.7322 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.08 | 0.7314 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.12 | 0.7328 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.32 | 0.6938 | 0.0570 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.61 | 0.7144 | 0.0421 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.24 | 0.7308 | 0.0397 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.06 | 0.7269 | 0.0403 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.22 | 0.7307 | 0.0397 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.61 | 0.7405 | 0.0377 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.82 | 0.7504 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.92 | 0.7521 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.92 | 0.7531 | 0.0344 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 42.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.19 | 0.7416 | 0.0316 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.37 | 0.3861 | 0.3616 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.58 | 0.4049 | 0.3487 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.46 | 0.4010 | 0.3560 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.52 | 0.4034 | 0.3525 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.37 | 0.4079 | 0.3533 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.46 | 0.4165 | 0.3446 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.40 | 0.4169 | 0.3497 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.42 | 0.4174 | 0.3474 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.64 | 0.6023 | 0.1740 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 18.47 | 0.5983 | 0.1782 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 18.47 | 0.5983 | 0.1782 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 18.43 | 0.5895 | 0.1818 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 18.43 | 0.5895 | 0.1818 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.53 | 0.3140 | 0.2311 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.54 | 0.3072 | 0.2362 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.54 | 0.3072 | 0.2362 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.54 | 0.3003 | 0.2383 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.54 | 0.3003 | 0.2383 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.47 | 0.2906 | 0.2400 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.47 | 0.4418 | 0.3329 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.65 | 0.4717 | 0.3155 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.57 | 0.4680 | 0.3245 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.60 | 0.4711 | 0.3202 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.53 | 0.4587 | 0.3257 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.66 | 0.4855 | 0.3120 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.58 | 0.4807 | 0.3197 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.61 | 0.4838 | 0.3165 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.71 | 0.3801 | 0.2189 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.20 | 0.3756 | 0.3696 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.39 | 0.4019 | 0.3537 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.28 | 0.3947 | 0.3621 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.34 | 0.3996 | 0.3580 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.24 | 0.3987 | 0.3607 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.32 | 0.4094 | 0.3516 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.27 | 0.4110 | 0.3570 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.29 | 0.4109 | 0.3545 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.19 | 0.7398 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.40 | 0.7438 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.36 | 0.7432 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.38 | 0.7437 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.83 | 0.7475 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.89 | 0.7497 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.93 | 0.7493 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.92 | 0.7497 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.71 | 0.7485 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.22 | 0.7549 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.99 | 0.7508 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.10 | 0.7523 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.89 | 0.7488 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.76 | 0.7500 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.15 | 0.7540 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.97 | 0.7503 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.01 | 0.7515 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.81 | 0.7474 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.87 | 0.7513 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.67 | 0.7356 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.29 | 0.7430 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.23 | 0.7414 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.28 | 0.7424 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.78 | 0.7365 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.36 | 0.7437 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.21 | 0.7413 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.29 | 0.7427 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.60 | 0.7471 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.32 | 0.7391 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.74 | 0.7447 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.64 | 0.7433 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.72 | 0.7446 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.72 | 0.7468 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.07 | 0.7518 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.06 | 0.7509 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.08 | 0.7517 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.17 | 0.7274 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.53 | 0.7328 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.50 | 0.7330 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.51 | 0.7331 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.38 | 0.7423 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.53 | 0.7459 | 0.0334 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.59 | 0.7462 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.59 | 0.7467 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.24 | 0.7414 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.89 | 0.7507 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.69 | 0.7475 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.83 | 0.7477 | 0.0358 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.67 | 0.7458 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.30 | 0.7449 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.81 | 0.7497 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.68 | 0.7467 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.73 | 0.7471 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.59 | 0.7442 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.23 | 0.7420 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.22 | 0.7129 | 0.0476 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.07 | 0.7269 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.04 | 0.7249 | 0.0443 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.08 | 0.7263 | 0.0432 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.59 | 0.7188 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.47 | 0.7312 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.29 | 0.7291 | 0.0430 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.37 | 0.7305 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.43 | 0.7294 | 0.0457 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.04 | 0.7196 | 0.0445 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.86 | 0.7322 | 0.0404 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.71 | 0.7291 | 0.0421 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.82 | 0.7315 | 0.0414 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.95 | 0.7357 | 0.0413 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.45 | 0.7429 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.44 | 0.7429 | 0.0388 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.46 | 0.7437 | 0.0379 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 73.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.98 | 0.7261 | 0.0357 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.83 | 0.3197 | 0.3928 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.92 | 0.3248 | 0.3835 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.86 | 0.3255 | 0.3885 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.89 | 0.3257 | 0.3861 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.83 | 0.3244 | 0.3878 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.86 | 0.3240 | 0.3808 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.83 | 0.3277 | 0.3846 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.84 | 0.3265 | 0.3824 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.56 | 0.5434 | 0.2511 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.49 | 0.5371 | 0.2563 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.49 | 0.5371 | 0.2563 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.48 | 0.5365 | 0.2573 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.48 | 0.5365 | 0.2573 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.37 | 0.1682 | 0.2890 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.37 | 0.1647 | 0.2923 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.37 | 0.1647 | 0.2923 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.37 | 0.1644 | 0.2923 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.37 | 0.1644 | 0.2923 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.33 | 0.1584 | 0.2932 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.53 | 0.3619 | 0.3692 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.62 | 0.3725 | 0.3552 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.57 | 0.3726 | 0.3623 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.59 | 0.3732 | 0.3588 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.50 | 0.3685 | 0.3603 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.55 | 0.3736 | 0.3483 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.52 | 0.3762 | 0.3550 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.53 | 0.3754 | 0.3520 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.71 | 0.2225 | 0.2749 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.60 | 0.2961 | 0.4032 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.75 | 0.3065 | 0.3936 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.66 | 0.3033 | 0.3988 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.71 | 0.3054 | 0.3964 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.59 | 0.3023 | 0.3973 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.63 | 0.3030 | 0.3919 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.61 | 0.3057 | 0.3952 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.63 | 0.3047 | 0.3934 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.82 | 0.7245 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.82 | 0.7245 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.83 | 0.7246 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.82 | 0.7246 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.95 | 0.7257 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.94 | 0.7257 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.95 | 0.7258 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.95 | 0.7258 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.97 | 0.7262 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.98 | 0.7263 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.98 | 0.7260 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.98 | 0.7262 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.98 | 0.7260 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.97 | 0.7261 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.98 | 0.7262 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.98 | 0.7260 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.98 | 0.7262 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.98 | 0.7260 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.98 | 0.7261 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.89 | 0.7252 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.92 | 0.7255 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.90 | 0.7254 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.92 | 0.7255 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.95 | 0.7256 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.96 | 0.7259 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.96 | 0.7259 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.96 | 0.7259 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.97 | 0.7260 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.87 | 0.7251 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.89 | 0.7251 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.89 | 0.7252 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.89 | 0.7252 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.92 | 0.7256 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.89 | 0.7255 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.91 | 0.7256 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.89 | 0.7255 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.49 | 0.7227 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.44 | 0.7224 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.56 | 0.7234 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.52 | 0.7231 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.83 | 0.7254 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.82 | 0.7252 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.88 | 0.7261 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.87 | 0.7259 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.87 | 0.7263 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.96 | 0.7262 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.94 | 0.7255 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.96 | 0.7262 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.96 | 0.7256 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.89 | 0.7264 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.95 | 0.7262 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.94 | 0.7256 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.96 | 0.7262 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.95 | 0.7256 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.87 | 0.7253 | 0.0388 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.36 | 0.7232 | 0.0450 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.51 | 0.7250 | 0.0432 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.50 | 0.7252 | 0.0440 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.50 | 0.7252 | 0.0435 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.57 | 0.7249 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7257 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.71 | 0.7265 | 0.0409 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.71 | 0.7262 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.63 | 0.7244 | 0.0420 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.45 | 0.7211 | 0.0407 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.55 | 0.7219 | 0.0400 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.53 | 0.7220 | 0.0404 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.54 | 0.7220 | 0.0402 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.60 | 0.7227 | 0.0405 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.59 | 0.7224 | 0.0406 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.64 | 0.7233 | 0.0406 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.60 | 0.7230 | 0.0405 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.35 | 0.7266 | 0.0570 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.63 | 0.3427 | 0.4629 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.75 | 0.3542 | 0.4453 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.68 | 0.3540 | 0.4556 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.71 | 0.3551 | 0.4505 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.63 | 0.3597 | 0.4468 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.68 | 0.3654 | 0.4339 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.64 | 0.3679 | 0.4415 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.66 | 0.3679 | 0.4375 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.08 | 0.5608 | 0.3393 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.97 | 0.5526 | 0.3428 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.97 | 0.5526 | 0.3428 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.97 | 0.5490 | 0.3465 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.97 | 0.5490 | 0.3465 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.59 | 0.2466 | 0.3705 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.62 | 0.2399 | 0.3753 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.62 | 0.2399 | 0.3753 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.62 | 0.2369 | 0.3776 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.62 | 0.2369 | 0.3776 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.55 | 0.2278 | 0.3789 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.32 | 0.3820 | 0.4424 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.46 | 0.4021 | 0.4166 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.39 | 0.3999 | 0.4311 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.42 | 0.4020 | 0.4240 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.32 | 0.3935 | 0.4277 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.39 | 0.4078 | 0.4065 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.35 | 0.4074 | 0.4191 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.37 | 0.4083 | 0.4135 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.81 | 0.2805 | 0.3573 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.34 | 0.3168 | 0.4792 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.51 | 0.3341 | 0.4609 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.41 | 0.3293 | 0.4712 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.47 | 0.3327 | 0.4665 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.34 | 0.3329 | 0.4652 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.40 | 0.3382 | 0.4536 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.37 | 0.3404 | 0.4610 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.39 | 0.3400 | 0.4575 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.06 | 0.7221 | 0.0621 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.19 | 0.7240 | 0.0602 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.17 | 0.7240 | 0.0614 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.19 | 0.7242 | 0.0609 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.64 | 0.7285 | 0.0586 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.70 | 0.7306 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.73 | 0.7303 | 0.0582 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.73 | 0.7306 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.70 | 0.7313 | 0.0598 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.85 | 0.7337 | 0.0569 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.69 | 0.7309 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.80 | 0.7325 | 0.0582 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.65 | 0.7300 | 0.0585 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.71 | 0.7318 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.83 | 0.7333 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.70 | 0.7309 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.78 | 0.7322 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.63 | 0.7295 | 0.0579 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.67 | 0.7319 | 0.0581 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.02 | 0.7225 | 0.0627 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.31 | 0.7261 | 0.0603 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.30 | 0.7255 | 0.0615 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.33 | 0.7260 | 0.0610 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.13 | 0.7234 | 0.0621 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.40 | 0.7270 | 0.0595 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.34 | 0.7258 | 0.0610 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.38 | 0.7265 | 0.0603 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.42 | 0.7286 | 0.0601 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.18 | 0.7229 | 0.0617 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.37 | 0.7253 | 0.0607 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.32 | 0.7248 | 0.0615 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.36 | 0.7254 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.48 | 0.7276 | 0.0601 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.57 | 0.7297 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.58 | 0.7294 | 0.0593 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.58 | 0.7298 | 0.0586 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.44 | 0.7152 | 0.0703 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.65 | 0.7177 | 0.0669 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.68 | 0.7185 | 0.0690 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.69 | 0.7184 | 0.0680 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.33 | 0.7253 | 0.0644 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.49 | 0.7282 | 0.0610 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.53 | 0.7285 | 0.0627 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.53 | 0.7289 | 0.0615 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.49 | 0.7286 | 0.0635 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.67 | 0.7315 | 0.0603 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.53 | 0.7290 | 0.0589 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.65 | 0.7302 | 0.0618 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.53 | 0.7283 | 0.0604 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.50 | 0.7298 | 0.0599 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.64 | 0.7311 | 0.0603 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.54 | 0.7288 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.61 | 0.7299 | 0.0616 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.50 | 0.7277 | 0.0596 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.30 | 0.7269 | 0.0653 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.17 | 0.7121 | 0.0792 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.64 | 0.7193 | 0.0721 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.64 | 0.7186 | 0.0758 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.65 | 0.7192 | 0.0740 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.42 | 0.7151 | 0.0752 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.89 | 0.7210 | 0.0683 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.82 | 0.7203 | 0.0720 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.85 | 0.7209 | 0.0702 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.73 | 0.7198 | 0.0730 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.46 | 0.7121 | 0.0748 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.80 | 0.7173 | 0.0712 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.72 | 0.7161 | 0.0735 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.78 | 0.7172 | 0.0724 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.96 | 0.7207 | 0.0716 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.07 | 0.7232 | 0.0676 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.13 | 0.7239 | 0.0696 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.10 | 0.7240 | 0.0684 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 254186 | 0.172 | 34.1 | 28.79 | 0.27 | 0.015 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 254186 | 0.172 | 34.5 | 28.79 | 0.27 | 0.015 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 254186 | 0.172 | 37.8 | 28.79 | 0.27 | 0.015 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 254186 | 0.172 | 33.0 | 28.79 | 0.27 | 0.015 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 735 | None | classic | 0.81 | False | 616870 | 0.660 | 125.1 | 29.81 | 0.11 | 0.010 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 735 | None | classic | 0.81 | False | 616870 | 0.660 | 133.0 | 29.81 | 0.11 | 0.010 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 735 | None | classic | 0.81 | False | 616870 | 0.660 | 132.8 | 29.81 | 0.11 | 0.010 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 735 | None | classic | 0.81 | False | 616870 | 0.660 | 134.2 | 29.81 | 0.11 | 0.010 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1349493 | 0.143 | 27.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1349493 | 0.795 | 54.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1349493 | 0.795 | 54.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1349493 | 0.534 | 28.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1349493 | 0.534 | 28.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1349493 | 0.143 | 35.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1349493 | 0.795 | 75.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1349493 | 0.795 | 75.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1349493 | 0.534 | 35.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1349493 | 0.534 | 35.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1347305 | 0.795 | 165.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 268825 | 0.161 | 38.4 | 28.68 | 0.09 | 0.020 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 268825 | 0.161 | 38.2 | 28.68 | 0.09 | 0.020 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 268825 | 0.161 | 37.5 | 28.68 | 0.09 | 0.020 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 268825 | 0.161 | 38.0 | 28.68 | 0.09 | 0.020 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1024 | None | classic | 1.57 | False | 516412 | 0.499 | 95.5 | 29.07 | 0.23 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1024 | None | classic | 1.57 | False | 516412 | 0.499 | 94.5 | 29.07 | 0.23 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1024 | None | classic | 1.57 | False | 516412 | 0.499 | 109.6 | 29.07 | 0.23 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1024 | None | classic | 1.57 | False | 516412 | 0.499 | 103.6 | 29.07 | 0.23 | 0.006 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1810727 | 0.795 | 80.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 265289 | 0.318 | 43.5 | 28.62 | 0.10 | 0.033 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 265289 | 0.318 | 31.4 | 28.62 | 0.10 | 0.033 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 265289 | 0.318 | 30.5 | 28.62 | 0.10 | 0.033 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 265289 | 0.318 | 33.3 | 28.62 | 0.10 | 0.033 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 842 | None | classic | 1.06 | False | 629316 | 0.654 | 123.1 | 30.19 | 0.19 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 842 | None | classic | 1.06 | False | 629316 | 0.654 | 119.2 | 30.19 | 0.19 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 842 | None | classic | 1.06 | False | 629316 | 0.654 | 120.7 | 30.19 | 0.19 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 842 | None | classic | 1.06 | False | 629316 | 0.654 | 120.8 | 30.19 | 0.19 | 0.007 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.574 | 0.032 |
| in035 | mask_ent | 0.713 | 0.032 |
| in035 | mask_grad | 0.405 | 0.032 |
| in035 | r_col | 0.847 | 0.032 |
| in035 | r_warp | 0.812 | 0.032 |

# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 8.4% | 23.09 / 0.0118 | 21.50 / 0.0247 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.9% | 23.19 / 0.0125 | 22.52 / 0.0211 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.6% | 23.15 / 0.0117 | 22.56 / 0.0221 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.7% | 23.16 / 0.0120 | 22.51 / 0.0212 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.5% | 23.07 / 0.0124 | 22.79 / 0.0192 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.8% | 23.17 / 0.0127 | 23.60 / 0.0164 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.6% | 23.12 / 0.0124 | 23.63 / 0.0168 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.6% | 23.14 / 0.0125 | 23.79 / 0.0162 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 7.9% | 23.02 / 0.0112 | 21.17 / 0.0302 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 7.0% | 22.55 / 0.0118 | 22.94 / 0.0178 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.2% | 19.42 / 0.0074 | 19.86 / 0.0104 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 6.9% | 22.51 / 0.0120 | 22.39 / 0.0196 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.2% | 19.17 / 0.0083 | 18.99 / 0.0111 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 7.8% | 22.96 / 0.0112 | 21.25 / 0.0214 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 6.8% | 22.50 / 0.0118 | 22.52 / 0.0186 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.2% | 19.17 / 0.0082 | 19.33 / 0.0112 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 6.8% | 22.42 / 0.0118 | 22.03 / 0.0206 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.4% | 19.17 / 0.0088 | 18.80 / 0.0122 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 8.9% | 23.18 / 0.0132 | 21.33 / 0.0278 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 14.3% | 24.15 / 0.0132 | 21.55 / 0.0335 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.8% | 24.25 / 0.0133 | 22.43 / 0.0274 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 14.5% | 24.19 / 0.0133 | 22.19 / 0.0302 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.6% | 24.20 / 0.0133 | 22.24 / 0.0283 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 14.3% | 24.12 / 0.0129 | 22.53 / 0.0262 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.8% | 24.17 / 0.0134 | 24.02 / 0.0206 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.6% | 24.16 / 0.0132 | 23.83 / 0.0229 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.6% | 24.15 / 0.0132 | 24.01 / 0.0212 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 14.9% | 24.21 / 0.0141 | 20.91 / 0.0419 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 9.7% | 23.27 / 0.0120 | 21.55 / 0.0276 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 11.3% | 23.67 / 0.0132 | 23.06 / 0.0249 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 10.6% | 23.56 / 0.0125 | 22.73 / 0.0257 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 10.8% | 23.60 / 0.0127 | 22.76 / 0.0257 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 10.4% | 23.57 / 0.0113 | 22.39 / 0.0221 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 12.0% | 24.02 / 0.0119 | 22.70 / 0.0228 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 11.0% | 23.77 / 0.0115 | 22.71 / 0.0221 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 11.3% | 23.87 / 0.0116 | 22.67 / 0.0216 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.80 / 0.0480 | 24.99 / 0.0600 | 19.50 / 0.0114 | 29.86 / 0.0326 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.29 / 0.0589 | 24.14 / 0.1072 | 19.49 / 0.0146 | 29.60 / 0.0353 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.50 / 0.0552 | 24.68 / 0.0884 | 20.08 / 0.0131 | 29.54 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.55 / 0.0576 | 24.77 / 0.0985 | 19.97 / 0.0137 | 29.66 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.54 / 0.0563 | 24.75 / 0.0918 | 20.04 / 0.0133 | 29.62 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.70 / 0.0534 | 24.86 / 0.0853 | 20.45 / 0.0121 | 29.63 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 / 0.0516 | 25.69 / 0.0718 | 20.75 / 0.0113 | 29.71 / 0.0343 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.91 / 0.0525 | 25.42 / 0.0807 | 20.68 / 0.0117 | 29.72 / 0.0345 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.95 / 0.0521 | 25.58 / 0.0755 | 20.72 / 0.0115 | 29.74 / 0.0343 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.67 / 0.0568 | 24.71 / 0.1045 | 19.69 / 0.0160 | 29.87 / 0.0329 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.81 / 0.0517 | 26.39 / 0.0677 | 19.99 / 0.0134 | 29.73 / 0.0337 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.78 / 0.0505 | 26.11 / 0.0651 | 19.87 / 0.0132 | 29.73 / 0.0335 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.75 / 0.0522 | 25.94 / 0.0684 | 19.73 / 0.0142 | 29.78 / 0.0334 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.72 / 0.0509 | 25.69 / 0.0671 | 19.59 / 0.0138 | 29.77 / 0.0332 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.73 / 0.0513 | 24.75 / 0.0774 | 19.72 / 0.0133 | 29.86 / 0.0329 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.76 / 0.0517 | 26.18 / 0.0669 | 19.89 / 0.0135 | 29.73 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.77 / 0.0502 | 26.04 / 0.0641 | 19.80 / 0.0131 | 29.74 / 0.0335 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.71 / 0.0521 | 25.80 / 0.0681 | 19.66 / 0.0139 | 29.78 / 0.0335 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.72 / 0.0505 | 25.71 / 0.0658 | 19.59 / 0.0134 | 29.78 / 0.0332 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.91 / 0.0520 | 25.89 / 0.0794 | 20.25 / 0.0129 | 29.82 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.78 / 0.0672 | 23.25 / 0.1326 | 19.34 / 0.0152 | 29.30 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.06 / 0.0607 | 23.99 / 0.1028 | 19.96 / 0.0131 | 29.31 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.06 / 0.0648 | 23.92 / 0.1201 | 19.74 / 0.0142 | 29.43 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.05 / 0.0624 | 23.97 / 0.1089 | 19.81 / 0.0136 | 29.39 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.17 / 0.0603 | 24.25 / 0.1052 | 19.92 / 0.0135 | 29.49 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.65 / 0.0543 | 25.03 / 0.0807 | 20.65 / 0.0113 | 29.54 / 0.0352 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.58 / 0.0579 | 24.91 / 0.0972 | 20.56 / 0.0121 | 29.58 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.63 / 0.0560 | 24.95 / 0.0883 | 20.62 / 0.0116 | 29.58 / 0.0354 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.26 / 0.0570 | 25.09 / 0.1043 | 19.93 / 0.0137 | 29.45 / 0.0357 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.27 / 0.0615 | 23.43 / 0.1381 | 19.78 / 0.0142 | 29.42 / 0.0366 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.60 / 0.0570 | 24.32 / 0.1137 | 20.40 / 0.0118 | 29.33 / 0.0365 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.50 / 0.0599 | 24.03 / 0.1301 | 20.11 / 0.0130 | 29.41 / 0.0367 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.52 / 0.0587 | 24.00 / 0.1252 | 20.20 / 0.0126 | 29.38 / 0.0366 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.41 / 0.0569 | 24.14 / 0.1014 | 20.31 / 0.0119 | 29.20 / 0.0369 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.52 / 0.0547 | 24.49 / 0.0847 | 20.55 / 0.0111 | 29.15 / 0.0371 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.51 / 0.0560 | 24.53 / 0.0944 | 20.46 / 0.0115 | 29.21 / 0.0369 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.49 / 0.0556 | 24.59 / 0.0892 | 20.48 / 0.0114 | 29.16 / 0.0369 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.0%） | — | — | 27.80 / 0.0480 | 24.99 / 0.0600 | 29.86 |
| in035 | rife | 4.1% | 9.7% | 27.27 / 0.0615 | 23.43 / 0.1381 | 29.42 |
| in035 | cnw_cnn | 4.8% | 8.4% | 27.29 / 0.0589 | 24.14 / 0.1072 | 29.60 |
| in035 | cnw_f5 | 8.2% | 14.3% | 26.78 / 0.0672 | 23.25 / 0.1326 | 29.30 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.35 / 0.0458 | -0.80 / +0.0165 (core 4.2%) | -0.61 / +0.0125 (core 4.8%) | -0.88 / +0.0198 (core 8.8%) |
| in035 | 2 | 0-3 | 27.76 / 0.0467 | -0.77 / +0.0144 (core 4.2%) | -0.51 / +0.0128 (core 4.8%) | -1.14 / +0.0226 (core 8.8%) |
| in035 | 4 | 3-5 | 28.29 / 0.0515 | -0.03 / +0.0096 (core 2.6%) | -0.40 / +0.0073 (core 3.1%) | -1.06 / +0.0152 (core 4.9%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.80 / 0.0480 | 24.99 | 29.86 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.29 / 0.0589 | 24.14 | 29.60 | 0/3 |
| in035 | cnw_cnn | oracle | 1.8% | 27.68 / 0.0526 | 24.86 | 29.84 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.50 / 0.0552 | 24.68 | 29.54 | 0/3 |
| in035 | cnw_cnn | oracle | 1.9% | 27.90 / 0.0505 | 25.49 | 29.84 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.55 / 0.0576 | 24.77 | 29.66 | 0/3 |
| in035 | cnw_cnn | oracle | 1.9% | 27.87 / 0.0517 | 25.43 | 29.85 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.54 / 0.0563 | 24.75 | 29.62 | 0/3 |
| in035 | cnw_cnn | oracle | 1.9% | 27.89 / 0.0511 | 25.47 | 29.85 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.70 / 0.0534 | 24.86 | 29.63 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.9% | 28.04 / 0.0492 | 25.80 | 29.85 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.95 / 0.0516 | 25.69 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.9% | 28.19 / 0.0481 | 26.22 | 29.86 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.91 / 0.0525 | 25.42 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.9% | 28.15 / 0.0486 | 26.08 | 29.86 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.95 / 0.0521 | 25.58 | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.9% | 28.18 / 0.0484 | 26.16 | 29.86 | 1/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 27.67 / 0.0568 | 24.71 | 29.87 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 1.8% | 27.81 / 0.0530 | 25.22 | 29.86 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 27.81 / 0.0517 | 26.39 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 1.7% | 27.93 / 0.0500 | 26.53 | 29.84 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 27.78 / 0.0505 | 26.11 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 1.0% | 27.89 / 0.0496 | 26.20 | 29.84 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.75 / 0.0522 | 25.94 | 29.78 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 1.7% | 27.85 / 0.0505 | 26.13 | 29.85 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.72 / 0.0509 | 25.69 | 29.77 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 1.1% | 27.79 / 0.0501 | 25.84 | 29.85 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.73 / 0.0513 | 24.75 | 29.86 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 1.8% | 27.84 / 0.0499 | 25.27 | 29.86 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.76 / 0.0517 | 26.18 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.7% | 27.89 / 0.0498 | 26.35 | 29.84 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.77 / 0.0502 | 26.04 | 29.74 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.1% | 27.87 / 0.0492 | 26.13 | 29.84 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.71 / 0.0521 | 25.80 | 29.78 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 1.7% | 27.82 / 0.0502 | 26.03 | 29.86 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.72 / 0.0505 | 25.71 | 29.78 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 1.1% | 27.80 / 0.0497 | 25.88 | 29.86 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.91 / 0.0520 | 25.89 | 29.82 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.9% | 28.04 / 0.0492 | 26.59 | 29.87 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.78 / 0.0672 | 23.25 | 29.30 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 27.54 / 0.0541 | 24.58 | 29.81 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.06 / 0.0607 | 23.99 | 29.31 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 27.80 / 0.0513 | 25.40 | 29.82 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.06 / 0.0648 | 23.92 | 29.43 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 27.74 / 0.0530 | 25.19 | 29.83 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.05 / 0.0624 | 23.97 | 29.39 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 27.75 / 0.0520 | 25.30 | 29.83 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.17 / 0.0603 | 24.25 | 29.49 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.6% | 27.79 / 0.0514 | 25.47 | 29.85 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.65 / 0.0543 | 25.03 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 28.09 / 0.0487 | 26.17 | 29.85 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.58 / 0.0579 | 24.91 | 29.58 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.6% | 28.06 / 0.0501 | 26.06 | 29.86 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.63 / 0.0560 | 24.95 | 29.58 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.6% | 28.08 / 0.0493 | 26.09 | 29.86 | 1/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.26 / 0.0570 | 25.09 | 29.45 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.7% | 27.87 / 0.0499 | 26.51 | 29.86 | 0/3 |
| in035 | rife | 不复核 | —% | 27.27 / 0.0615 | 23.43 | 29.42 | 0/3 |
| in035 | rife | oracle | 2.0% | 27.78 / 0.0521 | 24.87 | 29.85 | 0/3 |
| in035 | rife | 不复核 | —% | 27.60 / 0.0570 | 24.32 | 29.33 | 0/3 |
| in035 | rife | oracle | 2.1% | 28.04 / 0.0496 | 25.71 | 29.85 | 1/3 |
| in035 | rife | 不复核 | —% | 27.50 / 0.0599 | 24.03 | 29.41 | 0/3 |
| in035 | rife | oracle | 2.0% | 27.93 / 0.0510 | 25.32 | 29.85 | 0/3 |
| in035 | rife | 不复核 | —% | 27.52 / 0.0587 | 24.00 | 29.38 | 0/3 |
| in035 | rife | oracle | 2.1% | 27.96 / 0.0505 | 25.38 | 29.85 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.41 / 0.0569 | 24.14 | 29.20 | 0/3 |
| in035 | rife_mw | oracle | 1.9% | 28.01 / 0.0490 | 25.80 | 29.84 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.52 / 0.0547 | 24.49 | 29.15 | 0/3 |
| in035 | rife_mw | oracle | 2.0% | 28.11 / 0.0476 | 26.04 | 29.85 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.51 / 0.0560 | 24.53 | 29.21 | 0/3 |
| in035 | rife_mw | oracle | 2.0% | 28.09 / 0.0483 | 26.03 | 29.85 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.49 / 0.0556 | 24.59 | 29.16 | 0/3 |
| in035 | rife_mw | oracle | 2.0% | 28.10 / 0.0481 | 26.07 | 29.85 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.80 / 0.0480 | 24.99 / 0.0600 | — |
| in035 | FF | 0（前馈） | 1008×593（56%） | 26.30 | 27.29 / 0.0589 | 24.14 / 0.1072 | 0/3 |
| in035 | 25 | 0.49 s | 1008×593（56%） | 26.80 | 27.55 / 0.0576 | 24.77 / 0.0985 | 0/3 |
| in035 | 50 | 0.97 s | 1008×593（56%） | 27.03 | 27.54 / 0.0563 | 24.75 / 0.0918 | 0/3 |
| in035 | 100 | 1.92 s | 1008×593（56%） | 27.26 | 27.50 / 0.0552 | 24.68 / 0.0884 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.80 / 0.0480 | 24.99 / 0.0600 | 29.86 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.29 / 0.0589 | 24.14 / 0.1072 | 29.60 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.68 / 0.0526 | 24.86 / 0.0823 | 29.84 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.55 / 0.0576 | 24.77 / 0.0985 | 29.66 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.87 / 0.0517 | 25.43 / 0.0759 | 29.85 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.54 / 0.0563 | 24.75 / 0.0918 | 29.62 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.89 / 0.0511 | 25.47 / 0.0723 | 29.85 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.50 / 0.0552 | 24.68 / 0.0884 | 29.54 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.90 / 0.0505 | 25.49 / 0.0709 | 29.84 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.70 / 0.0534 | 24.86 / 0.0853 | 29.63 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.04 / 0.0492 | 25.80 / 0.0671 | 29.85 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.91 / 0.0525 | 25.42 / 0.0807 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.15 / 0.0486 | 26.08 / 0.0635 | 29.86 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.95 / 0.0521 | 25.58 / 0.0755 | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.18 / 0.0484 | 26.16 / 0.0603 | 29.86 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.95 / 0.0516 | 25.69 / 0.0718 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.19 / 0.0481 | 26.22 / 0.0584 | 29.86 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.78 / 0.0672 | 23.25 / 0.1326 | 29.30 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.54 / 0.0541 | 24.58 / 0.0876 | 29.81 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.06 / 0.0648 | 23.92 / 0.1201 | 29.43 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.74 / 0.0530 | 25.19 / 0.0802 | 29.83 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.05 / 0.0624 | 23.97 / 0.1089 | 29.39 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.75 / 0.0520 | 25.30 / 0.0751 | 29.83 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.06 / 0.0607 | 23.99 / 0.1028 | 29.31 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.80 / 0.0513 | 25.40 / 0.0724 | 29.82 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.17 / 0.0603 | 24.25 / 0.1052 | 29.49 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.79 / 0.0514 | 25.47 / 0.0731 | 29.85 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.58 / 0.0579 | 24.91 / 0.0972 | 29.58 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.06 / 0.0501 | 26.06 / 0.0671 | 29.86 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.63 / 0.0560 | 24.95 / 0.0883 | 29.58 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.08 / 0.0493 | 26.09 / 0.0637 | 29.86 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.65 / 0.0543 | 25.03 / 0.0807 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.09 / 0.0487 | 26.17 / 0.0598 | 29.85 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.27 / 0.0615 | 23.43 / 0.1381 | 29.42 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.78 / 0.0521 | 24.87 / 0.0841 | 29.85 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.50 / 0.0599 | 24.03 / 0.1301 | 29.41 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.93 / 0.0510 | 25.32 / 0.0769 | 29.85 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.52 / 0.0587 | 24.00 / 0.1252 | 29.38 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.96 / 0.0505 | 25.38 / 0.0741 | 29.85 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.60 / 0.0570 | 24.32 / 0.1137 | 29.33 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.04 / 0.0496 | 25.71 / 0.0692 | 29.85 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.41 / 0.0569 | 24.14 / 0.1014 | 29.20 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.01 / 0.0490 | 25.80 / 0.0629 | 29.84 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.51 / 0.0560 | 24.53 / 0.0944 | 29.21 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.09 / 0.0483 | 26.03 / 0.0597 | 29.85 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.49 / 0.0556 | 24.59 / 0.0892 | 29.16 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.10 / 0.0481 | 26.07 / 0.0577 | 29.85 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.52 / 0.0547 | 24.49 / 0.0847 | 29.15 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.11 / 0.0476 | 26.04 / 0.0548 | 29.85 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.99 / 0.0600 | 19.50 / 0.0114 | 29.86 / 0.0326 | 27.80 / 0.0480 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 12.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.99 | 0.7955 | 0.0600 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.04 | 0.4904 | 0.3719 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.29 | 0.4947 | 0.3297 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.20 | 0.5082 | 0.3543 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.25 | 0.5038 | 0.3400 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.14 | 0.5076 | 0.3277 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.54 | 0.5612 | 0.2934 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.33 | 0.5436 | 0.3139 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.45 | 0.5541 | 0.3038 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 19.44 | 0.6346 | 0.2618 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 19.34 | 0.6781 | 0.2260 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 19.34 | 0.6781 | 0.2260 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 19.21 | 0.6691 | 0.2277 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 19.21 | 0.6691 | 0.2277 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.29 | 0.4918 | 0.2695 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.27 | 0.5204 | 0.2736 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.27 | 0.5204 | 0.2736 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.25 | 0.5143 | 0.2707 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.25 | 0.5143 | 0.2707 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.20 | 0.4951 | 0.2816 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 16.37 | 0.6094 | 0.2549 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 16.97 | 0.6111 | 0.1984 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 16.66 | 0.6302 | 0.2327 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 16.81 | 0.6244 | 0.2119 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 16.85 | 0.6327 | 0.2046 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 17.75 | 0.6849 | 0.1540 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 17.28 | 0.6721 | 0.1852 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 17.52 | 0.6819 | 0.1682 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.35 | 0.7044 | 0.1772 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 15.44 | 0.5890 | 0.2857 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 16.24 | 0.6167 | 0.2230 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 15.86 | 0.6170 | 0.2631 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 15.99 | 0.6173 | 0.2451 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 15.96 | 0.6183 | 0.2092 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 16.51 | 0.6657 | 0.1708 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 16.16 | 0.6564 | 0.1939 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 16.24 | 0.6635 | 0.1820 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.86 | 0.7913 | 0.0823 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.49 | 0.7948 | 0.0709 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.43 | 0.7980 | 0.0759 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.47 | 0.7965 | 0.0723 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.80 | 0.8064 | 0.0671 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.22 | 0.8205 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.08 | 0.8150 | 0.0635 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.16 | 0.8183 | 0.0603 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.22 | 0.7951 | 0.0839 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.53 | 0.8231 | 0.0615 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.20 | 0.8160 | 0.0610 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.13 | 0.8186 | 0.0629 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.84 | 0.8123 | 0.0630 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.27 | 0.8014 | 0.0686 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.35 | 0.8224 | 0.0609 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.13 | 0.8175 | 0.0596 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.03 | 0.8186 | 0.0624 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.88 | 0.8148 | 0.0620 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.59 | 0.8206 | 0.0632 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.58 | 0.7889 | 0.0876 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.40 | 0.7947 | 0.0724 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.19 | 0.7967 | 0.0802 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.30 | 0.7961 | 0.0751 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.47 | 0.7989 | 0.0731 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.17 | 0.8174 | 0.0598 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.06 | 0.8103 | 0.0671 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.09 | 0.8140 | 0.0637 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.51 | 0.8194 | 0.0685 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.87 | 0.7859 | 0.0841 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.71 | 0.8050 | 0.0692 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.32 | 0.7956 | 0.0769 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.38 | 0.7987 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.80 | 0.8033 | 0.0629 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.04 | 0.8205 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.03 | 0.8128 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.07 | 0.8167 | 0.0577 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.14 | 0.7625 | 0.1072 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.68 | 0.7642 | 0.0884 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.77 | 0.7713 | 0.0985 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.75 | 0.7685 | 0.0918 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.86 | 0.7751 | 0.0853 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.69 | 0.8074 | 0.0718 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.42 | 0.7950 | 0.0807 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.58 | 0.8027 | 0.0755 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.71 | 0.7772 | 0.1045 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.39 | 0.8194 | 0.0677 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.11 | 0.8141 | 0.0651 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.94 | 0.8140 | 0.0684 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.69 | 0.8091 | 0.0671 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.75 | 0.7859 | 0.0774 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.18 | 0.8181 | 0.0669 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.04 | 0.8149 | 0.0641 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.80 | 0.8127 | 0.0681 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.71 | 0.8109 | 0.0658 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.89 | 0.8075 | 0.0794 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.25 | 0.7379 | 0.1326 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.99 | 0.7435 | 0.1028 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.92 | 0.7520 | 0.1201 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.97 | 0.7497 | 0.1089 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.25 | 0.7507 | 0.1052 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.03 | 0.7856 | 0.0807 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.91 | 0.7741 | 0.0972 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.95 | 0.7810 | 0.0883 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.09 | 0.7909 | 0.1043 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.43 | 0.7262 | 0.1381 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.32 | 0.7517 | 0.1137 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.03 | 0.7422 | 0.1301 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.00 | 0.7452 | 0.1252 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.14 | 0.7402 | 0.1014 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.49 | 0.7707 | 0.0847 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.53 | 0.7603 | 0.0944 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.59 | 0.7663 | 0.0892 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.50 | 0.6235 | 0.0114 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.22 | 0.2653 | 0.1004 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.30 | 0.2856 | 0.0973 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.28 | 0.2820 | 0.0989 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.30 | 0.2839 | 0.0980 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.26 | 0.3258 | 0.0975 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.28 | 0.3501 | 0.0956 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.26 | 0.3416 | 0.0969 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.26 | 0.3465 | 0.0964 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.37 | 0.3458 | 0.0496 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.21 | 0.3588 | 0.0485 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.21 | 0.3588 | 0.0485 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.12 | 0.3468 | 0.0491 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.12 | 0.3468 | 0.0491 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.72 | 0.2977 | 0.0600 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.74 | 0.3025 | 0.0615 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.74 | 0.3025 | 0.0615 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.66 | 0.2906 | 0.0622 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.66 | 0.2906 | 0.0622 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.74 | 0.2933 | 0.0613 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.25 | 0.3845 | 0.0725 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.45 | 0.4142 | 0.0682 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.37 | 0.4085 | 0.0705 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.41 | 0.4129 | 0.0693 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.32 | 0.4099 | 0.0699 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.37 | 0.4642 | 0.0667 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.34 | 0.4440 | 0.0684 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.35 | 0.4555 | 0.0676 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.37 | 0.4195 | 0.0465 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.32 | 0.2802 | 0.0912 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.48 | 0.3239 | 0.0867 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.37 | 0.3035 | 0.0893 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.42 | 0.3119 | 0.0881 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.24 | 0.3001 | 0.0892 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.28 | 0.3295 | 0.0870 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.25 | 0.3195 | 0.0886 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.26 | 0.3266 | 0.0880 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.51 | 0.6233 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.09 | 0.6417 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.98 | 0.6389 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.05 | 0.6405 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.46 | 0.6696 | 0.0121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.76 | 0.6898 | 0.0113 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.68 | 0.6829 | 0.0116 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.73 | 0.6881 | 0.0115 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.69 | 0.6261 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.00 | 0.6688 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.88 | 0.6567 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.74 | 0.6564 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.59 | 0.6466 | 0.0138 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.72 | 0.6356 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.89 | 0.6662 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.81 | 0.6576 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.66 | 0.6553 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.60 | 0.6500 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.25 | 0.6656 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.34 | 0.6268 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.96 | 0.6474 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.75 | 0.6443 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.82 | 0.6463 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.92 | 0.6457 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.66 | 0.6858 | 0.0113 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.56 | 0.6735 | 0.0121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.63 | 0.6816 | 0.0116 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.94 | 0.6533 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.79 | 0.6251 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.41 | 0.6641 | 0.0117 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.12 | 0.6449 | 0.0130 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.20 | 0.6532 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.32 | 0.6579 | 0.0118 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.56 | 0.6817 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.47 | 0.6727 | 0.0114 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.49 | 0.6788 | 0.0113 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.49 | 0.6218 | 0.0146 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.08 | 0.6405 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.97 | 0.6377 | 0.0137 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.04 | 0.6392 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.45 | 0.6684 | 0.0121 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.75 | 0.6895 | 0.0113 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.68 | 0.6823 | 0.0117 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.72 | 0.6876 | 0.0115 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.69 | 0.6250 | 0.0160 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.99 | 0.6680 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.87 | 0.6566 | 0.0132 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.73 | 0.6558 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.59 | 0.6466 | 0.0138 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.72 | 0.6345 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.89 | 0.6655 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.80 | 0.6571 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.66 | 0.6547 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.59 | 0.6496 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.25 | 0.6634 | 0.0129 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.34 | 0.6251 | 0.0152 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.96 | 0.6460 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.74 | 0.6429 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.81 | 0.6449 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.92 | 0.6441 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.65 | 0.6851 | 0.0113 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.56 | 0.6723 | 0.0121 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.62 | 0.6806 | 0.0116 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.93 | 0.6498 | 0.0137 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.78 | 0.6237 | 0.0142 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.40 | 0.6627 | 0.0118 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.11 | 0.6437 | 0.0130 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.20 | 0.6520 | 0.0126 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.31 | 0.6558 | 0.0119 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.55 | 0.6806 | 0.0111 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.46 | 0.6714 | 0.0115 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.48 | 0.6778 | 0.0114 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 29.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.78 | 0.7696 | 0.0209 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.49 | 0.4233 | 0.2240 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.65 | 0.4359 | 0.2153 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.56 | 0.4374 | 0.2206 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.61 | 0.4369 | 0.2179 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.52 | 0.4377 | 0.2161 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.61 | 0.4570 | 0.2100 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.55 | 0.4569 | 0.2129 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.57 | 0.4574 | 0.2116 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.28 | 0.5512 | 0.1203 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.23 | 0.5744 | 0.1147 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.23 | 0.5744 | 0.1147 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.19 | 0.5641 | 0.1170 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.19 | 0.5641 | 0.1170 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.73 | 0.3398 | 0.1601 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.67 | 0.3316 | 0.1645 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.67 | 0.3316 | 0.1645 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.65 | 0.3225 | 0.1662 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.65 | 0.3225 | 0.1662 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.50 | 0.2763 | 0.1745 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.01 | 0.5212 | 0.1696 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.26 | 0.5393 | 0.1556 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.12 | 0.5404 | 0.1640 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.17 | 0.5400 | 0.1598 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.04 | 0.5262 | 0.1619 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.22 | 0.5692 | 0.1473 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.08 | 0.5628 | 0.1548 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.12 | 0.5675 | 0.1512 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.98 | 0.4136 | 0.1421 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.36 | 0.4642 | 0.1986 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.63 | 0.4934 | 0.1865 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.45 | 0.4860 | 0.1934 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.53 | 0.4897 | 0.1904 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.28 | 0.4644 | 0.1906 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.43 | 0.4831 | 0.1821 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.31 | 0.4825 | 0.1875 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.36 | 0.4837 | 0.1853 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.70 | 0.7625 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.22 | 0.7687 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.10 | 0.7680 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.16 | 0.7683 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.43 | 0.7759 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.70 | 0.7824 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.65 | 0.7807 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.69 | 0.7819 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.81 | 0.7632 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.19 | 0.7776 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.09 | 0.7751 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.93 | 0.7731 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.81 | 0.7711 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.84 | 0.7677 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.08 | 0.7768 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.02 | 0.7752 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.87 | 0.7729 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.83 | 0.7720 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.01 | 0.7703 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.45 | 0.7614 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.02 | 0.7687 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.81 | 0.7679 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.85 | 0.7681 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.03 | 0.7683 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.72 | 0.7825 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.59 | 0.7786 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.67 | 0.7809 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.55 | 0.7613 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.95 | 0.7640 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.49 | 0.7764 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.26 | 0.7713 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.33 | 0.7734 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.40 | 0.7734 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.51 | 0.7795 | 0.0207 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.53 | 0.7783 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.52 | 0.7792 | 0.0212 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.02 | 0.7472 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.62 | 0.7521 | 0.0265 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.53 | 0.7546 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.55 | 0.7535 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.79 | 0.7594 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.06 | 0.7711 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.09 | 0.7707 | 0.0243 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.11 | 0.7718 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.02 | 0.7313 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.04 | 0.7702 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.02 | 0.7720 | 0.0231 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.75 | 0.7636 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.72 | 0.7675 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.08 | 0.7454 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.87 | 0.7665 | 0.0258 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.95 | 0.7713 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.61 | 0.7600 | 0.0284 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.68 | 0.7663 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.50 | 0.7336 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.19 | 0.7261 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.80 | 0.7323 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.58 | 0.7361 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.62 | 0.7344 | 0.0334 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.87 | 0.7332 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.77 | 0.7606 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.69 | 0.7575 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.78 | 0.7609 | 0.0279 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.07 | 0.6850 | 0.0502 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.12 | 0.7441 | 0.0326 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.79 | 0.7600 | 0.0302 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.70 | 0.7571 | 0.0309 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.67 | 0.7584 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.65 | 0.7503 | 0.0278 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.67 | 0.7612 | 0.0267 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.85 | 0.7607 | 0.0269 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.79 | 0.7626 | 0.0267 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 42.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.91 | 0.7336 | 0.0268 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.43 | 0.3256 | 0.3576 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.48 | 0.3342 | 0.3497 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.46 | 0.3339 | 0.3544 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.47 | 0.3346 | 0.3520 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.45 | 0.3395 | 0.3498 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.49 | 0.3497 | 0.3462 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.46 | 0.3478 | 0.3483 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.48 | 0.3491 | 0.3475 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.25 | 0.5432 | 0.1830 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.06 | 0.5418 | 0.1831 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.06 | 0.5418 | 0.1831 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.04 | 0.5370 | 0.1834 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.04 | 0.5370 | 0.1834 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.32 | 0.2390 | 0.2344 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.27 | 0.2347 | 0.2383 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.27 | 0.2347 | 0.2383 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.27 | 0.2317 | 0.2386 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.27 | 0.2317 | 0.2386 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.25 | 0.2246 | 0.2393 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.06 | 0.4270 | 0.3051 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.13 | 0.4404 | 0.2931 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.09 | 0.4403 | 0.3002 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.11 | 0.4411 | 0.2963 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.08 | 0.4393 | 0.2971 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.13 | 0.4587 | 0.2868 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.09 | 0.4562 | 0.2929 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.10 | 0.4591 | 0.2897 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.27 | 0.3737 | 0.1972 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.85 | 0.3634 | 0.3382 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.98 | 0.3810 | 0.3265 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.89 | 0.3760 | 0.3337 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.93 | 0.3787 | 0.3304 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.83 | 0.3702 | 0.3302 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.89 | 0.3821 | 0.3242 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.85 | 0.3794 | 0.3283 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.87 | 0.3812 | 0.3267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.82 | 0.7303 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.25 | 0.7332 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.18 | 0.7330 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.22 | 0.7331 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.45 | 0.7371 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.64 | 0.7405 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.58 | 0.7393 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.62 | 0.7401 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.99 | 0.7320 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.32 | 0.7395 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.23 | 0.7379 | 0.0278 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.15 | 0.7376 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.04 | 0.7362 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.99 | 0.7338 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.28 | 0.7392 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.21 | 0.7380 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.13 | 0.7377 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.07 | 0.7368 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.41 | 0.7380 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.64 | 0.7296 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.13 | 0.7333 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.00 | 0.7331 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.03 | 0.7332 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.13 | 0.7326 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.57 | 0.7399 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.51 | 0.7377 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.55 | 0.7391 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.30 | 0.7369 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.99 | 0.7308 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.44 | 0.7377 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.23 | 0.7346 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.28 | 0.7360 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.41 | 0.7361 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.63 | 0.7408 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.53 | 0.7388 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.56 | 0.7399 | 0.0262 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.30 | 0.7204 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.73 | 0.7232 | 0.0314 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.73 | 0.7242 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.73 | 0.7239 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.97 | 0.7289 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.27 | 0.7355 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.20 | 0.7338 | 0.0294 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.26 | 0.7351 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.74 | 0.7261 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.18 | 0.7373 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.13 | 0.7363 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.03 | 0.7356 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.97 | 0.7349 | 0.0287 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.78 | 0.7292 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.11 | 0.7367 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.11 | 0.7363 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.98 | 0.7352 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.98 | 0.7351 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.18 | 0.7327 | 0.0304 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.52 | 0.7072 | 0.0409 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.06 | 0.7129 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.95 | 0.7137 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.97 | 0.7136 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.19 | 0.7136 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.87 | 0.7281 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.75 | 0.7246 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.84 | 0.7272 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.39 | 0.7216 | 0.0349 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.39 | 0.7171 | 0.0363 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.04 | 0.7280 | 0.0318 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.77 | 0.7239 | 0.0345 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.85 | 0.7259 | 0.0334 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.81 | 0.7228 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.13 | 0.7302 | 0.0297 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.00 | 0.7276 | 0.0309 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.03 | 0.7290 | 0.0306 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.86 | 0.7338 | 0.0326 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.64 | 0.2954 | 0.3783 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.67 | 0.2948 | 0.3745 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.65 | 0.2986 | 0.3766 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.66 | 0.2974 | 0.3755 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.64 | 0.2976 | 0.3734 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.66 | 0.3020 | 0.3696 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.65 | 0.3026 | 0.3718 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.66 | 0.3028 | 0.3706 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.47 | 0.5339 | 0.2458 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.40 | 0.5271 | 0.2490 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.40 | 0.5271 | 0.2490 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.40 | 0.5268 | 0.2489 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.40 | 0.5268 | 0.2489 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.94 | 0.1398 | 0.2769 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.95 | 0.1373 | 0.2794 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.95 | 0.1373 | 0.2794 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.95 | 0.1371 | 0.2787 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.95 | 0.1371 | 0.2787 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.91 | 0.1330 | 0.2789 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.54 | 0.3622 | 0.3313 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.59 | 0.3639 | 0.3237 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.56 | 0.3688 | 0.3281 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.57 | 0.3672 | 0.3257 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.55 | 0.3685 | 0.3248 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.58 | 0.3699 | 0.3154 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.56 | 0.3733 | 0.3211 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.57 | 0.3723 | 0.3182 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.88 | 0.2387 | 0.2397 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.78 | 0.3060 | 0.3635 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.90 | 0.3091 | 0.3575 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.81 | 0.3107 | 0.3613 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.85 | 0.3103 | 0.3595 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.77 | 0.3083 | 0.3582 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.83 | 0.3110 | 0.3536 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.78 | 0.3128 | 0.3564 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.81 | 0.3123 | 0.3551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.84 | 0.7335 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.84 | 0.7334 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.85 | 0.7336 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.85 | 0.7335 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.85 | 0.7337 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.86 | 0.7339 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.86 | 0.7338 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.86 | 0.7339 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.86 | 0.7339 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.84 | 0.7337 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.84 | 0.7336 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.85 | 0.7337 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.85 | 0.7337 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.86 | 0.7339 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.84 | 0.7337 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.84 | 0.7337 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.86 | 0.7338 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.86 | 0.7338 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.87 | 0.7340 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.81 | 0.7333 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.82 | 0.7332 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.83 | 0.7334 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.83 | 0.7333 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.85 | 0.7336 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.85 | 0.7337 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.86 | 0.7338 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.86 | 0.7338 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.86 | 0.7339 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.85 | 0.7336 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.85 | 0.7335 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.85 | 0.7336 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.85 | 0.7336 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.84 | 0.7336 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.85 | 0.7337 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.85 | 0.7338 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.85 | 0.7338 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.60 | 0.7307 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.54 | 0.7303 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.66 | 0.7313 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.62 | 0.7310 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.63 | 0.7308 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7323 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.72 | 0.7321 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.74 | 0.7324 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.87 | 0.7342 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.73 | 0.7329 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.73 | 0.7326 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.78 | 0.7331 | 0.0334 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.77 | 0.7329 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.86 | 0.7342 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.73 | 0.7330 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.74 | 0.7328 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.78 | 0.7332 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.78 | 0.7329 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.82 | 0.7341 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.30 | 0.7286 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.31 | 0.7285 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.43 | 0.7300 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.39 | 0.7295 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.49 | 0.7301 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.54 | 0.7308 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.58 | 0.7313 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.58 | 0.7312 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.45 | 0.7324 | 0.0357 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.42 | 0.7279 | 0.0366 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.33 | 0.7271 | 0.0365 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.41 | 0.7281 | 0.0367 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.38 | 0.7278 | 0.0366 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.20 | 0.7265 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.15 | 0.7261 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.21 | 0.7271 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.16 | 0.7267 | 0.0369 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.80 | 0.7373 | 0.0480 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.06 | 0.3055 | 0.4488 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.09 | 0.3072 | 0.4379 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.07 | 0.3103 | 0.4454 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.08 | 0.3094 | 0.4415 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.06 | 0.3125 | 0.4350 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.08 | 0.3201 | 0.4278 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.07 | 0.3196 | 0.4326 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.07 | 0.3202 | 0.4303 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.55 | 0.5233 | 0.3467 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.46 | 0.5174 | 0.3452 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.46 | 0.5174 | 0.3452 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.46 | 0.5157 | 0.3459 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.46 | 0.5157 | 0.3459 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.08 | 0.1792 | 0.3636 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.08 | 0.1752 | 0.3677 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.08 | 0.1752 | 0.3677 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.08 | 0.1738 | 0.3684 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.08 | 0.1738 | 0.3684 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.05 | 0.1683 | 0.3681 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.12 | 0.3821 | 0.3907 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.18 | 0.3873 | 0.3730 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.15 | 0.3910 | 0.3846 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.16 | 0.3899 | 0.3785 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.14 | 0.3898 | 0.3751 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.17 | 0.4003 | 0.3587 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.15 | 0.4000 | 0.3692 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.16 | 0.4010 | 0.3637 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.22 | 0.2835 | 0.3057 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.26 | 0.3213 | 0.4310 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.40 | 0.3304 | 0.4165 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.30 | 0.3293 | 0.4259 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.35 | 0.3300 | 0.4215 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.25 | 0.3245 | 0.4158 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.31 | 0.3317 | 0.4068 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.26 | 0.3314 | 0.4127 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.29 | 0.3320 | 0.4104 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.68 | 0.7353 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.90 | 0.7363 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.87 | 0.7365 | 0.0517 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.89 | 0.7364 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.04 | 0.7386 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.19 | 0.7407 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.15 | 0.7401 | 0.0486 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.18 | 0.7405 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.81 | 0.7368 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.93 | 0.7392 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.89 | 0.7384 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.85 | 0.7385 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.79 | 0.7378 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.84 | 0.7377 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.89 | 0.7392 | 0.0498 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.87 | 0.7387 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.82 | 0.7386 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.80 | 0.7382 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.04 | 0.7393 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.54 | 0.7347 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.80 | 0.7360 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.74 | 0.7363 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.75 | 0.7362 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.79 | 0.7361 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.09 | 0.7398 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.06 | 0.7389 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.08 | 0.7395 | 0.0493 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.87 | 0.7380 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.78 | 0.7356 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.04 | 0.7386 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.93 | 0.7374 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.96 | 0.7379 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.01 | 0.7380 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.11 | 0.7402 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.09 | 0.7395 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.10 | 0.7400 | 0.0481 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.29 | 0.7292 | 0.0589 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.50 | 0.7297 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.55 | 0.7311 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.54 | 0.7306 | 0.0563 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.70 | 0.7331 | 0.0534 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 | 0.7376 | 0.0516 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.91 | 0.7366 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.95 | 0.7374 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.67 | 0.7342 | 0.0568 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.81 | 0.7376 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.78 | 0.7370 | 0.0505 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.75 | 0.7370 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.72 | 0.7366 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.73 | 0.7357 | 0.0513 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.76 | 0.7375 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.77 | 0.7373 | 0.0502 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.71 | 0.7369 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.72 | 0.7368 | 0.0505 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.91 | 0.7371 | 0.0520 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.78 | 0.7227 | 0.0672 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.06 | 0.7244 | 0.0607 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.06 | 0.7260 | 0.0648 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.05 | 0.7254 | 0.0624 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.17 | 0.7257 | 0.0603 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.65 | 0.7332 | 0.0543 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.58 | 0.7316 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.63 | 0.7328 | 0.0560 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.26 | 0.7304 | 0.0570 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.27 | 0.7264 | 0.0615 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.60 | 0.7302 | 0.0570 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.50 | 0.7291 | 0.0599 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.52 | 0.7296 | 0.0587 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.41 | 0.7276 | 0.0569 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.52 | 0.7310 | 0.0547 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.51 | 0.7305 | 0.0560 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.49 | 0.7310 | 0.0556 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 214204 | 0.166 | 34.1 | 29.04 | 0.08 | 0.021 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 214204 | 0.166 | 35.5 | 29.04 | 0.08 | 0.021 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 214204 | 0.166 | 36.5 | 29.04 | 0.08 | 0.021 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 214204 | 0.166 | 31.8 | 29.04 | 0.08 | 0.021 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 792 | None | classic | 0.30 | False | 515713 | 0.489 | 117.8 | 27.49 | 0.21 | 0.027 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 792 | None | classic | 0.30 | False | 515713 | 0.489 | 114.1 | 27.49 | 0.21 | 0.027 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 792 | None | classic | 0.30 | False | 515713 | 0.489 | 108.7 | 27.49 | 0.21 | 0.027 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 792 | None | classic | 0.30 | False | 515713 | 0.489 | 100.1 | 27.49 | 0.21 | 0.027 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1043504 | 0.163 | 23.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1042606 | 0.800 | 49.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1042606 | 0.800 | 49.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1042606 | 0.698 | 23.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1042606 | 0.698 | 23.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1043504 | 0.163 | 31.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1042606 | 0.800 | 72.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1042606 | 0.800 | 72.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1042606 | 0.698 | 30.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1042606 | 0.698 | 30.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1041738 | 0.800 | 154.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 218924 | 0.168 | 33.4 | 28.89 | 0.09 | 0.025 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 218924 | 0.168 | 35.2 | 28.89 | 0.09 | 0.025 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 218924 | 0.168 | 34.8 | 28.89 | 0.09 | 0.025 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 218924 | 0.168 | 31.3 | 28.89 | 0.09 | 0.025 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 924 | None | classic | 0.54 | False | 464849 | 0.495 | 97.9 | 32.52 | 0.20 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 924 | None | classic | 0.54 | False | 464849 | 0.495 | 96.7 | 32.52 | 0.20 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 924 | None | classic | 0.54 | False | 464849 | 0.495 | 93.4 | 32.52 | 0.20 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 924 | None | classic | 0.54 | False | 464849 | 0.495 | 98.0 | 32.52 | 0.20 | 0.007 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1748134 | 0.800 | 75.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 227662 | 0.322 | 42.0 | 29.42 | 0.16 | 0.022 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 227662 | 0.322 | 31.1 | 29.42 | 0.16 | 0.022 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 227662 | 0.322 | 29.6 | 29.42 | 0.16 | 0.022 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 227662 | 0.322 | 31.2 | 29.42 | 0.16 | 0.022 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 709 | None | classic | 0.57 | False | 453351 | 0.493 | 99.1 | 28.23 | 0.10 | 0.006 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 709 | None | classic | 0.57 | False | 453351 | 0.493 | 101.1 | 28.23 | 0.10 | 0.006 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 709 | None | classic | 0.57 | False | 453351 | 0.493 | 88.0 | 28.23 | 0.10 | 0.006 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 709 | None | classic | 0.57 | False | 453351 | 0.493 | 105.2 | 28.23 | 0.10 | 0.006 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.687 | 0.021 |
| in035 | mask_ent | 0.670 | 0.021 |
| in035 | mask_grad | 0.468 | 0.021 |
| in035 | r_col | 0.802 | 0.021 |
| in035 | r_warp | 0.848 | 0.021 |

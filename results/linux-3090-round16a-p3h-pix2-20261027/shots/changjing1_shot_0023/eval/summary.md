# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 11.5% | 24.72 / 0.0116 | 21.65 / 0.0277 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.9% | 24.77 / 0.0119 | 24.22 / 0.0189 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.8% | 24.77 / 0.0115 | 23.16 / 0.0230 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.8% | 24.77 / 0.0116 | 23.83 / 0.0207 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 11.7% | 24.92 / 0.0111 | 20.88 / 0.0278 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.9% | 24.94 / 0.0110 | 22.04 / 0.0221 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.8% | 24.97 / 0.0110 | 21.59 / 0.0245 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.8% | 24.98 / 0.0109 | 21.84 / 0.0226 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 11.5% | 24.58 / 0.0122 | 23.01 / 0.0302 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 9.8% | 24.27 / 0.0110 | 22.22 / 0.0249 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.4% | 20.67 / 0.0061 | 17.53 / 0.0142 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 9.8% | 24.32 / 0.0107 | 21.55 / 0.0252 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.5% | 20.97 / 0.0060 | 16.70 / 0.0161 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.6% | 24.60 / 0.0122 | 22.93 / 0.0214 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 9.7% | 24.23 / 0.0111 | 22.02 / 0.0237 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.5% | 20.75 / 0.0063 | 17.57 / 0.0136 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 9.7% | 24.29 / 0.0106 | 21.44 / 0.0247 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.6% | 21.15 / 0.0058 | 16.92 / 0.0153 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 12.3% | 24.77 / 0.0122 | 20.78 / 0.0383 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 17.9% | 25.45 / 0.0156 | 21.60 / 0.0457 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 18.5% | 25.45 / 0.0159 | 23.87 / 0.0324 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 18.1% | 25.43 / 0.0158 | 23.05 / 0.0391 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 18.3% | 25.44 / 0.0158 | 23.55 / 0.0353 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 17.6% | 25.45 / 0.0152 | 22.34 / 0.0430 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 18.2% | 25.46 / 0.0157 | 24.18 / 0.0319 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 17.8% | 25.45 / 0.0155 | 23.58 / 0.0366 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 18.0% | 25.44 / 0.0156 | 23.93 / 0.0336 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 18.1% | 25.32 / 0.0165 | 21.10 / 0.0517 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 9.8% | 24.59 / 0.0121 | 22.65 / 0.0295 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 10.8% | 24.73 / 0.0130 | 24.67 / 0.0231 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 10.2% | 24.73 / 0.0126 | 24.13 / 0.0260 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 10.5% | 24.72 / 0.0127 | 24.53 / 0.0241 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 11.4% | 24.97 / 0.0122 | 21.95 / 0.0275 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 12.7% | 25.28 / 0.0127 | 22.38 / 0.0261 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 12.1% | 25.15 / 0.0127 | 22.52 / 0.0269 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 12.4% | 25.25 / 0.0128 | 22.29 / 0.0259 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.85 / 0.0518 | 25.99 / 0.0578 | 19.90 / 0.0125 | 29.89 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.98 / 0.0661 | 23.90 / 0.1173 | 19.88 / 0.0155 | 29.29 / 0.0397 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.79 / 0.0593 | 25.74 / 0.0794 | 20.83 / 0.0129 | 29.65 / 0.0381 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.48 / 0.0628 | 24.75 / 0.0980 | 20.49 / 0.0140 | 29.45 / 0.0388 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.68 / 0.0610 | 25.36 / 0.0876 | 20.69 / 0.0134 | 29.60 / 0.0383 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.59 / 0.0654 | 22.71 / 0.1199 | 19.73 / 0.0167 | 28.99 / 0.0402 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.99 / 0.0606 | 24.11 / 0.0926 | 20.22 / 0.0146 | 29.10 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.86 / 0.0634 | 23.39 / 0.1126 | 20.06 / 0.0154 | 29.09 / 0.0400 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.93 / 0.0618 | 23.76 / 0.1034 | 20.15 / 0.0150 | 29.11 / 0.0396 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.71 / 0.0612 | 24.89 / 0.1047 | 20.02 / 0.0180 | 29.92 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.27 / 0.0588 | 25.82 / 0.0650 | 19.67 / 0.0163 | 29.64 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.27 / 0.0565 | 25.67 / 0.0620 | 19.57 / 0.0158 | 29.62 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.09 / 0.0593 | 25.61 / 0.0690 | 19.50 / 0.0163 | 29.61 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.10 / 0.0571 | 25.59 / 0.0634 | 19.39 / 0.0159 | 29.60 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.69 / 0.0558 | 24.78 / 0.0815 | 20.12 / 0.0144 | 29.88 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.25 / 0.0578 | 25.87 / 0.0645 | 19.63 / 0.0157 | 29.69 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.30 / 0.0558 | 25.89 / 0.0602 | 19.59 / 0.0154 | 29.70 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.04 / 0.0586 | 25.48 / 0.0709 | 19.40 / 0.0158 | 29.61 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.09 / 0.0565 | 25.59 / 0.0637 | 19.33 / 0.0156 | 29.62 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.95 / 0.0613 | 23.82 / 0.1170 | 19.59 / 0.0161 | 29.46 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.41 / 0.0774 | 23.07 / 0.1469 | 19.73 / 0.0165 | 28.91 / 0.0442 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.42 / 0.0666 | 25.39 / 0.0924 | 20.76 / 0.0136 | 29.47 / 0.0413 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.07 / 0.0722 | 24.31 / 0.1212 | 20.34 / 0.0149 | 29.28 / 0.0424 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.29 / 0.0692 | 24.93 / 0.1060 | 20.58 / 0.0141 | 29.42 / 0.0416 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.75 / 0.0756 | 23.96 / 0.1417 | 20.11 / 0.0164 | 29.12 / 0.0428 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.52 / 0.0646 | 25.57 / 0.0922 | 21.19 / 0.0131 | 29.41 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.26 / 0.0705 | 24.85 / 0.1184 | 20.83 / 0.0145 | 29.29 / 0.0416 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.41 / 0.0671 | 25.22 / 0.1043 | 21.03 / 0.0136 | 29.35 / 0.0408 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.42 / 0.0667 | 23.80 / 0.1245 | 19.54 / 0.0170 | 29.35 / 0.0412 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.26 / 0.0656 | 24.16 / 0.1187 | 20.32 / 0.0144 | 29.45 / 0.0393 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.77 / 0.0590 | 25.95 / 0.0825 | 20.98 / 0.0124 | 29.66 / 0.0382 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.61 / 0.0625 | 25.15 / 0.1025 | 20.81 / 0.0131 | 29.57 / 0.0387 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.70 / 0.0609 | 25.52 / 0.0934 | 20.92 / 0.0126 | 29.61 / 0.0384 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.93 / 0.0653 | 22.94 / 0.1213 | 20.08 / 0.0147 | 29.03 / 0.0414 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.21 / 0.0616 | 24.44 / 0.0949 | 20.67 / 0.0126 | 28.98 / 0.0418 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.15 / 0.0638 | 23.84 / 0.1096 | 20.44 / 0.0137 | 29.07 / 0.0417 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.14 / 0.0630 | 24.20 / 0.1025 | 20.56 / 0.0132 | 28.97 / 0.0418 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.4%） | — | — | 27.85 / 0.0518 | 25.99 / 0.0578 | 29.89 |
| in035 | rife | 4.7% | 9.8% | 27.26 / 0.0656 | 24.16 / 0.1187 | 29.45 |
| in035 | cnw_cnn | 6.9% | 11.5% | 26.98 / 0.0661 | 23.90 / 0.1173 | 29.29 |
| in035 | cnw_f5 | 11.1% | 17.9% | 26.41 / 0.0774 | 23.07 / 0.1469 | 28.91 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.43 / 0.0485 | -0.98 / +0.0171 (core 5.1%) | -1.00 / +0.0165 (core 8.0%) | -1.49 / +0.0299 (core 12.9%) |
| in035 | 2 | 0-3 | 27.51 / 0.0505 | -0.76 / +0.0184 (core 5.1%) | -1.03 / +0.0188 (core 8.0%) | -1.74 / +0.0331 (core 12.9%) |
| in035 | 4 | 3-5 | 28.62 / 0.0565 | -0.03 / +0.0058 (core 2.8%) | -0.58 / +0.0074 (core 3.6%) | -1.09 / +0.0136 (core 6.1%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.85 / 0.0518 | 25.99 | 29.89 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.98 / 0.0661 | 23.90 | 29.29 | 0/3 |
| in035 | cnw_cnn | oracle | 2.0% | 27.64 / 0.0570 | 25.62 | 29.81 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.79 / 0.0593 | 25.74 | 29.65 | 0/3 |
| in035 | cnw_cnn | oracle | 2.0% | 28.09 / 0.0539 | 26.68 | 29.87 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.48 / 0.0628 | 24.75 | 29.45 | 0/3 |
| in035 | cnw_cnn | oracle | 2.0% | 27.93 / 0.0556 | 26.25 | 29.85 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.68 / 0.0610 | 25.36 | 29.60 | 0/3 |
| in035 | cnw_cnn | oracle | 2.0% | 28.02 / 0.0548 | 26.50 | 29.86 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.59 / 0.0654 | 22.71 | 28.99 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.9% | 27.48 / 0.0567 | 24.81 | 29.79 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.99 / 0.0606 | 24.11 | 29.10 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 27.75 / 0.0542 | 25.94 | 29.81 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.86 / 0.0634 | 23.39 | 29.09 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 27.65 / 0.0555 | 25.30 | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.93 / 0.0618 | 23.76 | 29.11 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 27.71 / 0.0547 | 25.65 | 29.80 | 1/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 27.71 / 0.0612 | 24.89 | 29.92 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 2.0% | 27.84 / 0.0578 | 25.53 | 29.90 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 27.27 / 0.0588 | 25.82 | 29.64 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 1.9% | 27.61 / 0.0553 | 26.45 | 29.86 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 27.27 / 0.0565 | 25.67 | 29.62 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 1.1% | 27.57 / 0.0548 | 26.18 | 29.86 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.09 / 0.0593 | 25.61 | 29.61 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 1.8% | 27.53 / 0.0552 | 26.35 | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.10 / 0.0571 | 25.59 | 29.60 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 1.0% | 27.48 / 0.0549 | 26.17 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.69 / 0.0558 | 24.78 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 2.0% | 27.86 / 0.0538 | 25.58 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.25 / 0.0578 | 25.87 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.9% | 27.57 / 0.0547 | 26.38 | 29.86 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.30 / 0.0558 | 25.89 | 29.70 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.1% | 27.56 / 0.0543 | 26.21 | 29.86 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.04 / 0.0586 | 25.48 | 29.61 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 1.8% | 27.48 / 0.0546 | 26.24 | 29.87 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.09 / 0.0565 | 25.59 | 29.62 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 1.0% | 27.46 / 0.0544 | 26.10 | 29.87 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.95 / 0.0613 | 23.82 | 29.46 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.1% | 27.51 / 0.0554 | 25.64 | 29.85 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.41 / 0.0774 | 23.07 | 28.91 | 0/3 |
| in035 | cnw_f5 | oracle | 2.7% | 27.49 / 0.0597 | 25.32 | 29.78 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.42 / 0.0666 | 25.39 | 29.47 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 28.03 / 0.0553 | 26.76 | 29.87 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.07 / 0.0722 | 24.31 | 29.28 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.84 / 0.0577 | 26.16 | 29.84 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.29 / 0.0692 | 24.93 | 29.42 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.95 / 0.0565 | 26.49 | 29.86 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.75 / 0.0756 | 23.96 | 29.12 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 27.67 / 0.0590 | 25.85 | 29.83 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.52 / 0.0646 | 25.57 | 29.41 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 28.15 / 0.0544 | 26.96 | 29.87 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.26 / 0.0705 | 24.85 | 29.29 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 27.99 / 0.0568 | 26.56 | 29.86 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.41 / 0.0671 | 25.22 | 29.35 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 28.08 / 0.0556 | 26.78 | 29.87 | 1/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.42 / 0.0667 | 23.80 | 29.35 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.8% | 27.36 / 0.0566 | 25.66 | 29.81 | 0/3 |
| in035 | rife | 不复核 | —% | 27.26 / 0.0656 | 24.16 | 29.45 | 0/3 |
| in035 | rife | oracle | 1.7% | 27.83 / 0.0559 | 25.80 | 29.86 | 0/3 |
| in035 | rife | 不复核 | —% | 27.77 / 0.0590 | 25.95 | 29.66 | 0/3 |
| in035 | rife | oracle | 1.8% | 28.12 / 0.0530 | 26.90 | 29.88 | 1/3 |
| in035 | rife | 不复核 | —% | 27.61 / 0.0625 | 25.15 | 29.57 | 0/3 |
| in035 | rife | oracle | 1.7% | 28.03 / 0.0544 | 26.49 | 29.87 | 1/3 |
| in035 | rife | 不复核 | —% | 27.70 / 0.0609 | 25.52 | 29.61 | 0/3 |
| in035 | rife | oracle | 1.7% | 28.08 / 0.0537 | 26.72 | 29.88 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 26.93 / 0.0653 | 22.94 | 29.03 | 0/3 |
| in035 | rife_mw | oracle | 1.8% | 27.68 / 0.0550 | 25.20 | 29.80 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.21 / 0.0616 | 24.44 | 28.98 | 0/3 |
| in035 | rife_mw | oracle | 1.8% | 27.96 / 0.0526 | 26.41 | 29.83 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.15 / 0.0638 | 23.84 | 29.07 | 0/3 |
| in035 | rife_mw | oracle | 1.8% | 27.85 / 0.0538 | 25.86 | 29.82 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.14 / 0.0630 | 24.20 | 28.97 | 0/3 |
| in035 | rife_mw | oracle | 1.8% | 27.90 / 0.0533 | 26.18 | 29.83 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.85 / 0.0518 | 25.99 / 0.0578 | — |
| in035 | FF | 0（前馈） | 1008×596（58%） | 27.23 | 26.98 / 0.0661 | 23.90 / 0.1173 | 0/3 |
| in035 | 25 | 1.13 s | 1008×596（58%） | 27.95 | 27.48 / 0.0628 | 24.75 / 0.0980 | 0/3 |
| in035 | 50 | 2.25 s | 1008×596（58%） | 28.25 | 27.68 / 0.0610 | 25.36 / 0.0876 | 0/3 |
| in035 | 100 | 4.50 s | 1008×596（58%） | 28.48 | 27.79 / 0.0593 | 25.74 / 0.0794 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.85 / 0.0518 | 25.99 / 0.0578 | 29.89 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.98 / 0.0661 | 23.90 / 0.1173 | 29.29 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.64 / 0.0570 | 25.62 / 0.0776 | 29.81 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.48 / 0.0628 | 24.75 / 0.0980 | 29.45 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.93 / 0.0556 | 26.25 / 0.0704 | 29.85 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.68 / 0.0610 | 25.36 / 0.0876 | 29.60 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.02 / 0.0548 | 26.50 / 0.0656 | 29.86 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.79 / 0.0593 | 25.74 / 0.0794 | 29.65 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.09 / 0.0539 | 26.68 / 0.0620 | 29.87 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 26.59 / 0.0654 | 22.71 / 0.1199 | 28.99 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.48 / 0.0567 | 24.81 / 0.0775 | 29.79 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 26.86 / 0.0634 | 23.39 / 0.1126 | 29.09 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.65 / 0.0555 | 25.30 / 0.0726 | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 26.93 / 0.0618 | 23.76 / 0.1034 | 29.11 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.71 / 0.0547 | 25.65 / 0.0681 | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 26.99 / 0.0606 | 24.11 / 0.0926 | 29.10 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.75 / 0.0542 | 25.94 / 0.0635 | 29.81 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.41 / 0.0774 | 23.07 / 0.1469 | 28.91 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.49 / 0.0597 | 25.32 / 0.0871 | 29.78 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.07 / 0.0722 | 24.31 / 0.1212 | 29.28 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.84 / 0.0577 | 26.16 / 0.0756 | 29.84 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.29 / 0.0692 | 24.93 / 0.1060 | 29.42 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.95 / 0.0565 | 26.49 / 0.0688 | 29.86 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.42 / 0.0666 | 25.39 / 0.0924 | 29.47 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.03 / 0.0553 | 26.76 / 0.0631 | 29.87 | 1/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.75 / 0.0756 | 23.96 / 0.1417 | 29.12 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.67 / 0.0590 | 25.85 / 0.0822 | 29.83 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.26 / 0.0705 | 24.85 / 0.1184 | 29.29 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.99 / 0.0568 | 26.56 / 0.0731 | 29.86 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.41 / 0.0671 | 25.22 / 0.1043 | 29.35 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.08 / 0.0556 | 26.78 / 0.0677 | 29.87 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.52 / 0.0646 | 25.57 / 0.0922 | 29.41 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.15 / 0.0544 | 26.96 / 0.0633 | 29.87 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.26 / 0.0656 | 24.16 / 0.1187 | 29.45 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.83 / 0.0559 | 25.80 / 0.0766 | 29.86 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.61 / 0.0625 | 25.15 / 0.1025 | 29.57 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.03 / 0.0544 | 26.49 / 0.0686 | 29.87 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.70 / 0.0609 | 25.52 / 0.0934 | 29.61 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.08 / 0.0537 | 26.72 / 0.0640 | 29.88 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.77 / 0.0590 | 25.95 / 0.0825 | 29.66 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.12 / 0.0530 | 26.90 / 0.0598 | 29.88 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.93 / 0.0653 | 22.94 / 0.1213 | 29.03 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.68 / 0.0550 | 25.20 / 0.0751 | 29.80 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.15 / 0.0638 | 23.84 / 0.1096 | 29.07 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.85 / 0.0538 | 25.86 / 0.0671 | 29.82 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.14 / 0.0630 | 24.20 / 0.1025 | 28.97 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.90 / 0.0533 | 26.18 / 0.0634 | 29.83 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.21 / 0.0616 | 24.44 / 0.0949 | 28.98 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.96 / 0.0526 | 26.41 / 0.0594 | 29.83 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.99 / 0.0578 | 19.90 / 0.0125 | 29.89 / 0.0356 | 27.85 / 0.0518 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 12.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.99 | 0.8274 | 0.0578 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 14.96 | 0.5787 | 0.2820 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 16.23 | 0.6960 | 0.1988 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 15.59 | 0.6481 | 0.2419 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 15.88 | 0.6750 | 0.2193 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 14.45 | 0.5076 | 0.2673 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 15.68 | 0.5984 | 0.2152 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 15.20 | 0.5608 | 0.2486 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 15.45 | 0.5806 | 0.2326 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 23.10 | 0.7397 | 0.1547 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 23.84 | 0.7981 | 0.1171 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 23.84 | 0.7981 | 0.1171 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 23.62 | 0.7866 | 0.1232 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 23.62 | 0.7866 | 0.1232 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 16.21 | 0.6747 | 0.1924 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 16.22 | 0.6999 | 0.1932 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 16.22 | 0.6999 | 0.1932 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 16.11 | 0.6874 | 0.2024 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 16.11 | 0.6874 | 0.2024 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.60 | 0.6448 | 0.2340 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 18.75 | 0.6094 | 0.2461 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 21.15 | 0.7490 | 0.1507 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 20.11 | 0.6880 | 0.2015 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 20.65 | 0.7220 | 0.1743 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 18.85 | 0.6362 | 0.2355 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 21.24 | 0.7679 | 0.1490 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 20.17 | 0.7105 | 0.1936 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 20.70 | 0.7415 | 0.1704 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.09 | 0.7230 | 0.1869 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.15 | 0.5689 | 0.2931 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 15.11 | 0.6846 | 0.2086 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 14.63 | 0.6341 | 0.2560 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 14.84 | 0.6616 | 0.2327 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 13.72 | 0.5242 | 0.2730 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 14.59 | 0.6168 | 0.2162 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 14.23 | 0.5847 | 0.2509 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 14.44 | 0.6058 | 0.2319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.62 | 0.8134 | 0.0776 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.68 | 0.8373 | 0.0620 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.25 | 0.8267 | 0.0704 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.50 | 0.8325 | 0.0656 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.81 | 0.7998 | 0.0775 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.94 | 0.8230 | 0.0635 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.30 | 0.8102 | 0.0726 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.65 | 0.8171 | 0.0681 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.53 | 0.8105 | 0.0890 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.45 | 0.8422 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.18 | 0.8360 | 0.0569 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.35 | 0.8398 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.17 | 0.8357 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.58 | 0.8180 | 0.0710 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.38 | 0.8390 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.21 | 0.8344 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.24 | 0.8359 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.10 | 0.8337 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.64 | 0.8259 | 0.0746 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.32 | 0.8074 | 0.0871 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.76 | 0.8389 | 0.0631 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.16 | 0.8248 | 0.0756 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.49 | 0.8326 | 0.0688 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.85 | 0.8170 | 0.0822 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.96 | 0.8450 | 0.0633 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.56 | 0.8334 | 0.0731 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.78 | 0.8401 | 0.0677 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.66 | 0.8282 | 0.0750 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.80 | 0.8191 | 0.0766 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.90 | 0.8447 | 0.0598 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.49 | 0.8339 | 0.0686 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.72 | 0.8399 | 0.0640 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.20 | 0.8086 | 0.0751 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.41 | 0.8327 | 0.0594 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.86 | 0.8216 | 0.0671 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.18 | 0.8281 | 0.0634 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.90 | 0.7629 | 0.1173 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.74 | 0.8207 | 0.0794 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.75 | 0.7974 | 0.0980 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.36 | 0.8109 | 0.0876 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.71 | 0.7262 | 0.1199 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.11 | 0.7739 | 0.0926 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.39 | 0.7502 | 0.1126 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.76 | 0.7625 | 0.1034 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.89 | 0.7909 | 0.1047 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.82 | 0.8351 | 0.0650 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.67 | 0.8296 | 0.0620 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.61 | 0.8286 | 0.0690 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.59 | 0.8291 | 0.0634 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.78 | 0.8020 | 0.0815 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.87 | 0.8308 | 0.0645 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.89 | 0.8292 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.48 | 0.8220 | 0.0709 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.59 | 0.8271 | 0.0637 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.82 | 0.7913 | 0.1170 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.07 | 0.7339 | 0.1469 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.39 | 0.8141 | 0.0924 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.31 | 0.7806 | 0.1212 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.93 | 0.7994 | 0.1060 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.96 | 0.7560 | 0.1417 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.57 | 0.8294 | 0.0922 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.85 | 0.7987 | 0.1184 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.22 | 0.8165 | 0.1043 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.80 | 0.7908 | 0.1245 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.16 | 0.7720 | 0.1187 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.95 | 0.8286 | 0.0825 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.15 | 0.8031 | 0.1025 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.52 | 0.8166 | 0.0934 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.94 | 0.7361 | 0.1213 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.44 | 0.7855 | 0.0949 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.84 | 0.7663 | 0.1096 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.20 | 0.7781 | 0.1025 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.90 | 0.6748 | 0.0125 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.51 | 0.3360 | 0.0934 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.68 | 0.4049 | 0.0886 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.57 | 0.3794 | 0.0912 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.62 | 0.3934 | 0.0899 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.42 | 0.3070 | 0.0944 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.42 | 0.3321 | 0.0917 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.43 | 0.3248 | 0.0930 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.42 | 0.3300 | 0.0924 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.33 | 0.3880 | 0.0543 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.25 | 0.4034 | 0.0539 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.25 | 0.4034 | 0.0539 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.09 | 0.3947 | 0.0546 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.09 | 0.3947 | 0.0546 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.95 | 0.3516 | 0.0562 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.86 | 0.3432 | 0.0598 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.86 | 0.3432 | 0.0598 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.81 | 0.3343 | 0.0606 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.81 | 0.3343 | 0.0606 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.82 | 0.3228 | 0.0599 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.15 | 0.4168 | 0.0739 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.42 | 0.4968 | 0.0680 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.29 | 0.4661 | 0.0713 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.36 | 0.4836 | 0.0697 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.09 | 0.4241 | 0.0741 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.23 | 0.5009 | 0.0686 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.15 | 0.4757 | 0.0716 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.18 | 0.4907 | 0.0702 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.14 | 0.4150 | 0.0499 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.32 | 0.3071 | 0.0947 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.64 | 0.3715 | 0.0895 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.48 | 0.3477 | 0.0924 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.57 | 0.3611 | 0.0911 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.14 | 0.3088 | 0.0948 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.23 | 0.3564 | 0.0907 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.19 | 0.3360 | 0.0930 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.21 | 0.3477 | 0.0921 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.89 | 0.6745 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.84 | 0.7244 | 0.0128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.50 | 0.7048 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.69 | 0.7158 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.76 | 0.6614 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.25 | 0.6928 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.08 | 0.6777 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.18 | 0.6860 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.02 | 0.6624 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.68 | 0.6875 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.59 | 0.6787 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.53 | 0.6830 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.42 | 0.6742 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.12 | 0.6781 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.64 | 0.6818 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.60 | 0.6764 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.44 | 0.6745 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.36 | 0.6699 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.60 | 0.6706 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.73 | 0.6683 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.75 | 0.7246 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.34 | 0.7019 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.57 | 0.7150 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.12 | 0.6796 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.18 | 0.7397 | 0.0130 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.82 | 0.7172 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.03 | 0.7309 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.53 | 0.6666 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.35 | 0.6881 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.00 | 0.7287 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.83 | 0.7145 | 0.0130 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.93 | 0.7227 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.12 | 0.6815 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.68 | 0.7158 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.47 | 0.7012 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.57 | 0.7094 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.88 | 0.6727 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.83 | 0.7234 | 0.0129 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.49 | 0.7037 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.69 | 0.7149 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.73 | 0.6582 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.22 | 0.6904 | 0.0146 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.06 | 0.6749 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.15 | 0.6833 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.02 | 0.6611 | 0.0180 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.67 | 0.6856 | 0.0163 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.57 | 0.6770 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.50 | 0.6806 | 0.0163 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.39 | 0.6722 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.12 | 0.6763 | 0.0144 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.63 | 0.6795 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.59 | 0.6746 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.40 | 0.6714 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.33 | 0.6676 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.59 | 0.6664 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.73 | 0.6655 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.76 | 0.7236 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.34 | 0.7000 | 0.0149 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.58 | 0.7134 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.11 | 0.6773 | 0.0164 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.19 | 0.7387 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.83 | 0.7156 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.03 | 0.7296 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.54 | 0.6625 | 0.0170 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.32 | 0.6850 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.98 | 0.7271 | 0.0124 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.81 | 0.7120 | 0.0131 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.92 | 0.7208 | 0.0126 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.08 | 0.6780 | 0.0147 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.67 | 0.7140 | 0.0126 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.44 | 0.6988 | 0.0137 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.56 | 0.7074 | 0.0132 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 28.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.64 | 0.7776 | 0.0201 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.41 | 0.4843 | 0.2146 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.59 | 0.5310 | 0.2008 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.48 | 0.5173 | 0.2084 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.53 | 0.5255 | 0.2047 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.39 | 0.4626 | 0.2117 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.53 | 0.4881 | 0.2014 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.43 | 0.4851 | 0.2065 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.47 | 0.4884 | 0.2042 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.68 | 0.6012 | 0.1081 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 18.20 | 0.6101 | 0.1086 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 18.20 | 0.6101 | 0.1086 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 18.02 | 0.6002 | 0.1093 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 18.02 | 0.6002 | 0.1093 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.01 | 0.4364 | 0.1416 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.72 | 0.4066 | 0.1526 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.72 | 0.4066 | 0.1526 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.63 | 0.3956 | 0.1536 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.63 | 0.3956 | 0.1536 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.45 | 0.3441 | 0.1643 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.01 | 0.5304 | 0.1821 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.32 | 0.5813 | 0.1656 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.13 | 0.5664 | 0.1747 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.20 | 0.5751 | 0.1703 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.04 | 0.5397 | 0.1825 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.32 | 0.5915 | 0.1655 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.12 | 0.5769 | 0.1753 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.19 | 0.5855 | 0.1707 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.51 | 0.4397 | 0.1389 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.86 | 0.5000 | 0.2037 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.13 | 0.5436 | 0.1889 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.95 | 0.5303 | 0.1975 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.02 | 0.5380 | 0.1935 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.81 | 0.5006 | 0.1980 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.05 | 0.5292 | 0.1859 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.90 | 0.5250 | 0.1927 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.97 | 0.5289 | 0.1893 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.40 | 0.7714 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.35 | 0.7897 | 0.0220 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.01 | 0.7830 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.21 | 0.7870 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.19 | 0.7642 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.79 | 0.7774 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.56 | 0.7715 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.69 | 0.7749 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.53 | 0.7665 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.30 | 0.7788 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.22 | 0.7755 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.03 | 0.7755 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.94 | 0.7728 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.61 | 0.7738 | 0.0228 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.21 | 0.7761 | 0.0228 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.18 | 0.7743 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.93 | 0.7728 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.89 | 0.7716 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.73 | 0.7612 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.11 | 0.7665 | 0.0277 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.21 | 0.7880 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.78 | 0.7803 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.03 | 0.7849 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.47 | 0.7700 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.57 | 0.7928 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.21 | 0.7849 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.41 | 0.7896 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.49 | 0.7560 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.84 | 0.7770 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.56 | 0.7926 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.35 | 0.7871 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.47 | 0.7903 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.66 | 0.7748 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.24 | 0.7871 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.01 | 0.7820 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.13 | 0.7847 | 0.0215 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.27 | 0.7485 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.66 | 0.7797 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.17 | 0.7701 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.48 | 0.7761 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.71 | 0.7292 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.53 | 0.7514 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.26 | 0.7448 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.42 | 0.7495 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.81 | 0.7361 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.69 | 0.7634 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.75 | 0.7654 | 0.0262 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.18 | 0.7569 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.23 | 0.7605 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.77 | 0.7514 | 0.0274 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.53 | 0.7586 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.69 | 0.7637 | 0.0256 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.05 | 0.7517 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.17 | 0.7581 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.77 | 0.7136 | 0.0429 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.38 | 0.7215 | 0.0403 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.85 | 0.7604 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.41 | 0.7492 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.70 | 0.7560 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.86 | 0.7282 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.09 | 0.7674 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.82 | 0.7568 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.03 | 0.7639 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.89 | 0.6790 | 0.0518 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.77 | 0.7528 | 0.0338 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.61 | 0.7804 | 0.0291 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.48 | 0.7727 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.61 | 0.7778 | 0.0295 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.49 | 0.7481 | 0.0303 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.14 | 0.7663 | 0.0280 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.97 | 0.7623 | 0.0287 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.07 | 0.7655 | 0.0281 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 42.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.33 | 0.7434 | 0.0295 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.06 | 0.3986 | 0.3505 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.13 | 0.4298 | 0.3382 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.09 | 0.4209 | 0.3451 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.11 | 0.4264 | 0.3418 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.09 | 0.3907 | 0.3473 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.12 | 0.4053 | 0.3387 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.11 | 0.4030 | 0.3433 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.11 | 0.4051 | 0.3411 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.27 | 0.5870 | 0.1686 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.96 | 0.5779 | 0.1727 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.96 | 0.5779 | 0.1727 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.90 | 0.5714 | 0.1747 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.90 | 0.5714 | 0.1747 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.99 | 0.3177 | 0.2228 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.84 | 0.2991 | 0.2314 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.84 | 0.2991 | 0.2314 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.80 | 0.2934 | 0.2333 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.80 | 0.2934 | 0.2333 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.78 | 0.2853 | 0.2339 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.27 | 0.4595 | 0.3090 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.35 | 0.4958 | 0.2937 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.31 | 0.4859 | 0.3023 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.33 | 0.4921 | 0.2983 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.27 | 0.4687 | 0.3082 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.34 | 0.5053 | 0.2922 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.30 | 0.4954 | 0.3011 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.32 | 0.5018 | 0.2968 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.07 | 0.4070 | 0.1998 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.28 | 0.4040 | 0.3461 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.42 | 0.4338 | 0.3325 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.33 | 0.4240 | 0.3406 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.37 | 0.4292 | 0.3369 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.26 | 0.4109 | 0.3417 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.37 | 0.4285 | 0.3297 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.31 | 0.4240 | 0.3368 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.35 | 0.4271 | 0.3333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.18 | 0.7386 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.98 | 0.7491 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.72 | 0.7452 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.87 | 0.7475 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.90 | 0.7347 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.34 | 0.7415 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.18 | 0.7385 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.28 | 0.7403 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.29 | 0.7381 | 0.0354 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.09 | 0.7430 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.03 | 0.7416 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.95 | 0.7421 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.88 | 0.7410 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.35 | 0.7414 | 0.0314 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.04 | 0.7419 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.01 | 0.7410 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.88 | 0.7410 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.83 | 0.7404 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.87 | 0.7384 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.98 | 0.7362 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.91 | 0.7486 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.60 | 0.7441 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.78 | 0.7468 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.18 | 0.7386 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.07 | 0.7515 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.79 | 0.7470 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.96 | 0.7498 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.72 | 0.7369 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.46 | 0.7423 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.98 | 0.7506 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.84 | 0.7477 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.93 | 0.7494 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.37 | 0.7422 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.89 | 0.7487 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.68 | 0.7462 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.79 | 0.7476 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.25 | 0.7238 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.50 | 0.7435 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.02 | 0.7375 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.33 | 0.7412 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.75 | 0.7152 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.35 | 0.7273 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.14 | 0.7232 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.25 | 0.7257 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.01 | 0.7310 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.63 | 0.7373 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.65 | 0.7369 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.46 | 0.7349 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.50 | 0.7361 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.01 | 0.7358 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.58 | 0.7360 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.66 | 0.7363 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.39 | 0.7334 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.47 | 0.7352 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.08 | 0.7267 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.49 | 0.7081 | 0.0480 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.92 | 0.7333 | 0.0400 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.46 | 0.7261 | 0.0439 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.75 | 0.7307 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.01 | 0.7150 | 0.0469 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.19 | 0.7408 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.79 | 0.7328 | 0.0427 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.03 | 0.7381 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.26 | 0.7129 | 0.0435 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.77 | 0.7310 | 0.0402 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.60 | 0.7475 | 0.0348 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.36 | 0.7421 | 0.0375 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.50 | 0.7453 | 0.0362 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.64 | 0.7307 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.13 | 0.7402 | 0.0355 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.07 | 0.7380 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.96 | 0.7391 | 0.0364 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.89 | 0.7333 | 0.0356 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.93 | 0.3371 | 0.3761 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.98 | 0.3504 | 0.3673 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.94 | 0.3466 | 0.3722 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.96 | 0.3491 | 0.3696 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.94 | 0.3279 | 0.3732 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.96 | 0.3353 | 0.3677 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.95 | 0.3349 | 0.3708 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.96 | 0.3357 | 0.3690 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.56 | 0.5570 | 0.2351 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.51 | 0.5518 | 0.2403 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.51 | 0.5518 | 0.2403 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.51 | 0.5504 | 0.2405 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.51 | 0.5504 | 0.2405 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.66 | 0.2020 | 0.2727 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.65 | 0.1978 | 0.2763 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.65 | 0.1978 | 0.2763 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.65 | 0.1970 | 0.2768 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.65 | 0.1970 | 0.2768 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.60 | 0.1914 | 0.2764 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.74 | 0.3905 | 0.3354 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.80 | 0.4086 | 0.3212 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.76 | 0.4041 | 0.3286 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.78 | 0.4073 | 0.3245 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.73 | 0.3915 | 0.3320 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.77 | 0.4069 | 0.3190 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.74 | 0.4039 | 0.3260 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.75 | 0.4060 | 0.3223 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.87 | 0.2909 | 0.2381 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.90 | 0.3248 | 0.3781 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.01 | 0.3387 | 0.3687 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.94 | 0.3332 | 0.3745 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.98 | 0.3360 | 0.3715 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.89 | 0.3235 | 0.3752 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.97 | 0.3323 | 0.3667 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.93 | 0.3306 | 0.3721 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.96 | 0.3324 | 0.3691 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.81 | 0.7326 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.87 | 0.7331 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.85 | 0.7329 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.86 | 0.7330 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.79 | 0.7324 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.81 | 0.7325 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.80 | 0.7325 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.80 | 0.7325 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.90 | 0.7334 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.86 | 0.7332 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.86 | 0.7331 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.88 | 0.7332 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.88 | 0.7332 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.90 | 0.7333 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.86 | 0.7331 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.86 | 0.7331 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.87 | 0.7331 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.87 | 0.7331 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.85 | 0.7330 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.78 | 0.7323 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.87 | 0.7332 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.84 | 0.7328 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.86 | 0.7330 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.83 | 0.7325 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.87 | 0.7331 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.86 | 0.7329 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.87 | 0.7330 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.81 | 0.7327 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.86 | 0.7329 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.88 | 0.7332 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.87 | 0.7330 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.88 | 0.7331 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.80 | 0.7325 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.83 | 0.7327 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.82 | 0.7326 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.83 | 0.7327 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.29 | 0.7280 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.65 | 0.7317 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.45 | 0.7309 | 0.0388 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.60 | 0.7316 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.99 | 0.7254 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.10 | 0.7274 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.09 | 0.7270 | 0.0400 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.11 | 0.7273 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.92 | 0.7339 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.64 | 0.7328 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.62 | 0.7322 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.61 | 0.7327 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.60 | 0.7322 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.88 | 0.7338 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.69 | 0.7328 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.70 | 0.7323 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.61 | 0.7326 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.62 | 0.7323 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.46 | 0.7314 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.91 | 0.7246 | 0.0442 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.47 | 0.7307 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.28 | 0.7292 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.42 | 0.7304 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.12 | 0.7255 | 0.0428 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.41 | 0.7305 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.29 | 0.7292 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.35 | 0.7302 | 0.0408 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.35 | 0.7301 | 0.0412 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.45 | 0.7291 | 0.0393 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.66 | 0.7318 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.57 | 0.7306 | 0.0387 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.61 | 0.7312 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.03 | 0.7264 | 0.0414 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.98 | 0.7268 | 0.0418 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.07 | 0.7272 | 0.0417 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.97 | 0.7270 | 0.0418 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.85 | 0.7391 | 0.0518 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.43 | 0.3516 | 0.4403 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.49 | 0.3751 | 0.4218 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.45 | 0.3675 | 0.4326 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.47 | 0.3720 | 0.4274 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.45 | 0.3408 | 0.4321 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.47 | 0.3519 | 0.4198 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.46 | 0.3504 | 0.4270 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.46 | 0.3519 | 0.4234 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.82 | 0.5530 | 0.3260 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.70 | 0.5451 | 0.3294 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.70 | 0.5451 | 0.3294 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.67 | 0.5413 | 0.3313 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.67 | 0.5413 | 0.3313 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.81 | 0.2462 | 0.3520 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.76 | 0.2357 | 0.3596 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.76 | 0.2357 | 0.3596 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.74 | 0.2328 | 0.3615 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.74 | 0.2328 | 0.3615 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.70 | 0.2263 | 0.3618 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.34 | 0.4083 | 0.3927 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.41 | 0.4373 | 0.3670 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.37 | 0.4284 | 0.3821 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.39 | 0.4338 | 0.3746 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.33 | 0.4118 | 0.3890 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.37 | 0.4384 | 0.3632 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.35 | 0.4312 | 0.3780 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.36 | 0.4356 | 0.3709 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.13 | 0.3270 | 0.3062 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.44 | 0.3418 | 0.4386 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.57 | 0.3645 | 0.4208 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.48 | 0.3559 | 0.4313 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.52 | 0.3604 | 0.4263 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.42 | 0.3418 | 0.4294 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.51 | 0.3559 | 0.4149 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.46 | 0.3522 | 0.4240 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.49 | 0.3550 | 0.4195 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.64 | 0.7360 | 0.0570 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.09 | 0.7414 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.93 | 0.7394 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.02 | 0.7406 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.48 | 0.7340 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.75 | 0.7375 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.65 | 0.7360 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.71 | 0.7369 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.84 | 0.7371 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.61 | 0.7385 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.57 | 0.7376 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.53 | 0.7382 | 0.0552 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.48 | 0.7374 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.86 | 0.7385 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.57 | 0.7379 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.56 | 0.7374 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.48 | 0.7376 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.46 | 0.7371 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.51 | 0.7365 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.49 | 0.7342 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.03 | 0.7409 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.84 | 0.7383 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.95 | 0.7398 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.67 | 0.7356 | 0.0590 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.15 | 0.7423 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.99 | 0.7398 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.08 | 0.7413 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.36 | 0.7350 | 0.0566 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.83 | 0.7377 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.12 | 0.7419 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.03 | 0.7403 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.08 | 0.7412 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.68 | 0.7366 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.96 | 0.7401 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.85 | 0.7387 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.90 | 0.7394 | 0.0533 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.98 | 0.7266 | 0.0661 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.79 | 0.7379 | 0.0593 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.48 | 0.7344 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.68 | 0.7366 | 0.0610 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.59 | 0.7210 | 0.0654 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.99 | 0.7280 | 0.0606 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.86 | 0.7256 | 0.0634 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.93 | 0.7271 | 0.0618 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.71 | 0.7341 | 0.0612 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.27 | 0.7356 | 0.0588 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.27 | 0.7348 | 0.0565 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.09 | 0.7342 | 0.0593 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.10 | 0.7343 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.69 | 0.7360 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.25 | 0.7349 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.30 | 0.7348 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.04 | 0.7334 | 0.0586 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.09 | 0.7339 | 0.0565 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.95 | 0.7304 | 0.0613 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.41 | 0.7170 | 0.0774 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.42 | 0.7327 | 0.0666 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.07 | 0.7277 | 0.0722 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.29 | 0.7308 | 0.0692 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.75 | 0.7202 | 0.0756 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.52 | 0.7353 | 0.0646 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.26 | 0.7303 | 0.0705 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.41 | 0.7335 | 0.0671 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.42 | 0.7231 | 0.0667 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.26 | 0.7295 | 0.0656 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.77 | 0.7390 | 0.0590 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.61 | 0.7355 | 0.0625 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.70 | 0.7374 | 0.0609 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.93 | 0.7261 | 0.0653 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.21 | 0.7316 | 0.0616 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.15 | 0.7302 | 0.0638 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.14 | 0.7311 | 0.0630 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 301918 | 0.330 | 60.4 | 30.07 | 0.27 | 0.019 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 301918 | 0.330 | 86.5 | 30.07 | 0.27 | 0.019 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 301918 | 0.330 | 62.3 | 30.07 | 0.27 | 0.019 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 301918 | 0.330 | 95.9 | 30.07 | 0.27 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 859 | None | classic | 1.10 | False | 470251 | 1.011 | 213.4 | 28.38 | 0.32 | 0.034 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 859 | None | classic | 1.10 | False | 470251 | 1.011 | 203.6 | 28.38 | 0.32 | 0.034 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 859 | None | classic | 1.10 | False | 470251 | 1.011 | 180.3 | 28.38 | 0.32 | 0.034 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 859 | None | classic | 1.10 | False | 470251 | 1.011 | 174.5 | 28.38 | 0.32 | 0.034 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1423073 | 0.248 | 45.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1422992 | 0.801 | 51.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1422992 | 0.801 | 51.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1422992 | 0.514 | 46.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1422992 | 0.514 | 46.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1423073 | 0.248 | 56.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1422992 | 0.801 | 194.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1422992 | 0.801 | 194.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1422992 | 0.514 | 53.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1422992 | 0.514 | 53.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1421493 | 0.801 | 466.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 294362 | 0.322 | 66.5 | 29.77 | 0.12 | 0.021 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 294362 | 0.322 | 49.6 | 29.77 | 0.12 | 0.021 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 294362 | 0.322 | 69.4 | 29.77 | 0.12 | 0.021 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 294362 | 0.322 | 61.7 | 29.77 | 0.12 | 0.021 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1259 | None | classic | 2.37 | False | 523154 | 0.676 | 127.1 | 30.21 | 0.08 | 0.026 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1259 | None | classic | 2.37 | False | 523154 | 0.676 | 111.9 | 30.21 | 0.08 | 0.026 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1259 | None | classic | 2.37 | False | 523154 | 0.676 | 134.7 | 30.21 | 0.08 | 0.026 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1259 | None | classic | 2.37 | False | 523154 | 0.676 | 121.4 | 30.21 | 0.08 | 0.026 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1941166 | 0.801 | 114.2 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 313249 | 0.913 | 86.9 | 30.44 | 0.36 | 0.032 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 313249 | 0.913 | 66.7 | 30.44 | 0.36 | 0.032 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 313249 | 0.913 | 89.5 | 30.44 | 0.36 | 0.032 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 313249 | 0.913 | 72.6 | 30.44 | 0.36 | 0.032 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 773 | None | classic | 0.60 | False | 532574 | 0.986 | 139.4 | 28.17 | 0.27 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 773 | None | classic | 0.60 | False | 532574 | 0.986 | 200.1 | 28.17 | 0.27 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 773 | None | classic | 0.60 | False | 532574 | 0.986 | 175.4 | 28.17 | 0.27 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 773 | None | classic | 0.60 | False | 532574 | 0.986 | 156.2 | 28.17 | 0.27 | 0.005 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.651 | 0.021 |
| in035 | mask_ent | 0.710 | 0.021 |
| in035 | mask_grad | 0.479 | 0.021 |
| in035 | r_col | 0.798 | 0.021 |
| in035 | r_warp | 0.827 | 0.021 |

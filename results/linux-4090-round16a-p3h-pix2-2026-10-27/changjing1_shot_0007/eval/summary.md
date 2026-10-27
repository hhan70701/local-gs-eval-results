# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 6.1% | 25.06 / 0.0066 | 18.41 / 0.0201 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.5% | 25.10 / 0.0071 | 19.78 / 0.0159 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.3% | 25.10 / 0.0069 | 19.17 / 0.0180 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.4% | 25.11 / 0.0069 | 19.40 / 0.0169 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.6% | 24.82 / 0.0065 | 20.72 / 0.0132 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.9% | 24.88 / 0.0066 | 22.21 / 0.0097 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.8% | 24.86 / 0.0065 | 21.93 / 0.0104 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.8% | 24.86 / 0.0065 | 22.17 / 0.0098 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 5.3% | 24.58 / 0.0063 | 23.62 / 0.0154 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 4.8% | 24.53 / 0.0062 | 20.17 / 0.0206 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.1% | 23.50 / 0.0055 | 16.55 / 0.0198 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 4.8% | 24.59 / 0.0062 | 19.78 / 0.0224 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.2% | 23.35 / 0.0050 | 16.51 / 0.0196 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 5.3% | 24.56 / 0.0065 | 23.26 / 0.0106 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 4.7% | 24.28 / 0.0063 | 19.87 / 0.0180 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.2% | 23.68 / 0.0059 | 16.43 / 0.0182 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 4.7% | 24.34 / 0.0063 | 19.54 / 0.0203 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.3% | 23.53 / 0.0051 | 16.54 / 0.0188 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 6.7% | 25.32 / 0.0068 | 20.48 / 0.0233 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 9.7% | 25.59 / 0.0080 | 18.86 / 0.0293 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.2% | 25.64 / 0.0086 | 19.94 / 0.0235 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.9% | 25.61 / 0.0084 | 19.44 / 0.0260 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.0% | 25.62 / 0.0085 | 19.62 / 0.0247 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 9.8% | 25.54 / 0.0082 | 20.82 / 0.0222 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.4% | 25.63 / 0.0085 | 21.77 / 0.0178 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.9% | 25.57 / 0.0082 | 21.94 / 0.0182 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.1% | 25.55 / 0.0082 | 21.95 / 0.0172 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 10.4% | 25.72 / 0.0090 | 20.46 / 0.0321 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 5.3% | 27.27 / 0.0054 | 22.36 / 0.0139 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 6.1% | 27.11 / 0.0063 | 23.39 / 0.0133 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 5.7% | 27.13 / 0.0059 | 23.09 / 0.0131 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 5.9% | 27.10 / 0.0058 | 23.22 / 0.0127 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 6.5% | 26.95 / 0.0064 | 22.96 / 0.0149 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 7.4% | 27.21 / 0.0070 | 24.66 / 0.0164 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 7.0% | 27.02 / 0.0064 | 24.27 / 0.0149 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 7.2% | 27.11 / 0.0067 | 24.76 / 0.0151 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.35 / 0.0496 | 27.96 / 0.0390 | 20.68 / 0.0107 | 29.69 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.92 / 0.0591 | 24.34 / 0.1051 | 19.01 / 0.0143 | 29.35 / 0.0383 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.38 / 0.0557 | 25.92 / 0.0725 | 19.76 / 0.0124 | 29.38 / 0.0383 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.23 / 0.0573 | 25.28 / 0.0870 | 19.44 / 0.0134 | 29.39 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.29 / 0.0565 | 25.62 / 0.0778 | 19.59 / 0.0130 | 29.39 / 0.0383 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.85 / 0.0542 | 24.93 / 0.0872 | 20.43 / 0.0120 | 29.55 / 0.0377 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.22 / 0.0511 | 25.96 / 0.0654 | 21.10 / 0.0102 | 29.61 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.10 / 0.0523 | 25.39 / 0.0764 | 20.76 / 0.0110 | 29.61 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.16 / 0.0518 | 25.73 / 0.0708 | 20.93 / 0.0106 | 29.61 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.29 / 0.0545 | 27.20 / 0.0779 | 20.68 / 0.0139 | 29.69 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.63 / 0.0576 | 28.38 / 0.0757 | 19.70 / 0.0145 | 29.66 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.67 / 0.0552 | 28.08 / 0.0535 | 19.67 / 0.0136 | 29.66 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.50 / 0.0587 | 27.99 / 0.0719 | 19.72 / 0.0150 | 29.63 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.53 / 0.0571 | 27.86 / 0.0569 | 19.70 / 0.0142 | 29.63 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.25 / 0.0517 | 26.92 / 0.0660 | 20.66 / 0.0119 | 29.69 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.62 / 0.0563 | 27.93 / 0.0698 | 19.66 / 0.0137 | 29.65 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.67 / 0.0541 | 27.92 / 0.0494 | 19.65 / 0.0130 | 29.65 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.46 / 0.0574 | 27.94 / 0.0673 | 19.51 / 0.0144 | 29.63 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.49 / 0.0559 | 27.97 / 0.0513 | 19.51 / 0.0139 | 29.63 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.71 / 0.0595 | 26.06 / 0.1100 | 19.94 / 0.0141 | 29.64 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.62 / 0.0656 | 24.20 / 0.1079 | 18.96 / 0.0166 | 29.20 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.00 / 0.0598 | 25.67 / 0.0788 | 19.43 / 0.0144 | 29.34 / 0.0401 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.88 / 0.0626 | 24.95 / 0.0934 | 19.20 / 0.0157 | 29.33 / 0.0407 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.93 / 0.0611 | 25.33 / 0.0874 | 19.28 / 0.0152 | 29.35 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.43 / 0.0595 | 24.19 / 0.0987 | 20.14 / 0.0138 | 29.42 / 0.0394 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.82 / 0.0537 | 25.41 / 0.0716 | 20.64 / 0.0119 | 29.50 / 0.0384 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.69 / 0.0564 | 24.94 / 0.0829 | 20.35 / 0.0126 | 29.50 / 0.0390 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.75 / 0.0551 | 25.22 / 0.0761 | 20.48 / 0.0122 | 29.50 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.37 / 0.0609 | 25.90 / 0.1076 | 19.57 / 0.0159 | 29.59 / 0.0385 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.77 / 0.0554 | 25.61 / 0.0937 | 19.86 / 0.0125 | 29.62 / 0.0379 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.81 / 0.0547 | 25.95 / 0.0788 | 19.89 / 0.0119 | 29.60 / 0.0383 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.82 / 0.0551 | 25.88 / 0.0876 | 19.87 / 0.0121 | 29.62 / 0.0381 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.81 / 0.0549 | 25.87 / 0.0823 | 19.84 / 0.0123 | 29.60 / 0.0383 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.96 / 0.0546 | 24.17 / 0.0950 | 20.49 / 0.0114 | 29.59 / 0.0386 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.07 / 0.0530 | 26.65 / 0.0697 | 20.95 / 0.0106 | 29.55 / 0.0384 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.08 / 0.0536 | 25.43 / 0.0866 | 20.75 / 0.0110 | 29.58 / 0.0385 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.12 / 0.0531 | 25.97 / 0.0805 | 20.87 / 0.0108 | 29.57 / 0.0384 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.3%） | — | — | 28.35 / 0.0496 | 27.96 / 0.0390 | 29.69 |
| in035 | rife | 2.6% | 5.3% | 27.77 / 0.0554 | 25.61 / 0.0937 | 29.62 |
| in035 | cnw_cnn | 3.1% | 6.1% | 26.92 / 0.0591 | 24.34 / 0.1051 | 29.35 |
| in035 | cnw_f5 | 5.3% | 9.7% | 26.62 / 0.0656 | 24.20 / 0.1079 | 29.20 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.79 / 0.0481 | -0.75 / +0.0075 (core 3.0%) | -1.48 / +0.0103 (core 3.9%) | -1.65 / +0.0186 (core 7.1%) |
| in035 | 2 | 0-3 | 28.33 / 0.0483 | -0.91 / +0.0075 (core 3.0%) | -1.98 / +0.0146 (core 3.9%) | -2.45 / +0.0240 (core 7.1%) |
| in035 | 4 | 3-5 | 28.93 / 0.0523 | -0.07 / +0.0027 (core 1.2%) | -0.81 / +0.0037 (core 1.2%) | -1.09 / +0.0055 (core 1.6%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.35 / 0.0496 | 27.96 | 29.69 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.92 / 0.0591 | 24.34 | 29.35 | 0/3 |
| in035 | cnw_cnn | oracle | 1.1% | 27.50 / 0.0538 | 25.30 | 29.67 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.38 / 0.0557 | 25.92 | 29.38 | 0/3 |
| in035 | cnw_cnn | oracle | 1.2% | 27.88 / 0.0516 | 26.35 | 29.67 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.23 / 0.0573 | 25.28 | 29.39 | 0/3 |
| in035 | cnw_cnn | oracle | 1.2% | 27.73 / 0.0528 | 25.88 | 29.68 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.29 / 0.0565 | 25.62 | 29.39 | 0/3 |
| in035 | cnw_cnn | oracle | 1.2% | 27.80 / 0.0522 | 26.11 | 29.68 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.85 / 0.0542 | 24.93 | 29.55 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.1% | 28.16 / 0.0506 | 26.18 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.22 / 0.0511 | 25.96 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.2% | 28.43 / 0.0491 | 26.69 | 29.67 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.10 / 0.0523 | 25.39 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.2% | 28.32 / 0.0497 | 26.26 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.16 / 0.0518 | 25.73 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.2% | 28.37 / 0.0494 | 26.53 | 29.67 | 0/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 28.29 / 0.0545 | 27.20 | 29.69 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 1.2% | 28.32 / 0.0530 | 27.52 | 29.69 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 27.63 / 0.0576 | 28.38 | 29.66 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 1.1% | 27.87 / 0.0536 | 28.87 | 29.69 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 27.67 / 0.0552 | 28.08 | 29.66 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 0.7% | 27.88 / 0.0526 | 28.24 | 29.69 | 1/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.50 / 0.0587 | 27.99 | 29.63 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 1.0% | 27.85 / 0.0546 | 28.50 | 29.68 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.53 / 0.0571 | 27.86 | 29.63 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 0.6% | 27.85 / 0.0537 | 28.11 | 29.68 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 28.25 / 0.0517 | 26.92 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 1.2% | 28.31 / 0.0508 | 27.28 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.62 / 0.0563 | 27.93 | 29.65 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.1% | 27.86 / 0.0527 | 28.41 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.67 / 0.0541 | 27.92 | 29.65 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.7% | 27.88 / 0.0518 | 28.05 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.46 / 0.0574 | 27.94 | 29.63 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 1.0% | 27.78 / 0.0537 | 28.47 | 29.68 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.49 / 0.0559 | 27.97 | 29.63 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 0.7% | 27.79 / 0.0531 | 28.23 | 29.68 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.71 / 0.0595 | 26.06 | 29.64 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.2% | 28.00 / 0.0529 | 27.79 | 29.69 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.62 / 0.0656 | 24.20 | 29.20 | 0/3 |
| in035 | cnw_f5 | oracle | 1.8% | 27.45 / 0.0558 | 25.44 | 29.64 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.00 / 0.0598 | 25.67 | 29.34 | 0/3 |
| in035 | cnw_f5 | oracle | 1.8% | 27.70 / 0.0530 | 26.54 | 29.65 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.88 / 0.0626 | 24.95 | 29.33 | 0/3 |
| in035 | cnw_f5 | oracle | 1.8% | 27.60 / 0.0545 | 25.81 | 29.65 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.93 / 0.0611 | 25.33 | 29.35 | 0/3 |
| in035 | cnw_f5 | oracle | 1.8% | 27.64 / 0.0537 | 26.17 | 29.65 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.43 / 0.0595 | 24.19 | 29.42 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.8% | 28.01 / 0.0526 | 25.82 | 29.65 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.82 / 0.0537 | 25.41 | 29.50 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.9% | 28.21 / 0.0504 | 26.56 | 29.66 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.69 / 0.0564 | 24.94 | 29.50 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.8% | 28.11 / 0.0513 | 26.16 | 29.66 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.75 / 0.0551 | 25.22 | 29.50 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.8% | 28.17 / 0.0508 | 26.35 | 29.66 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.37 / 0.0609 | 25.90 | 29.59 | 0/3 |
| in035 | cnw_f5_pix | oracle | 1.8% | 27.78 / 0.0542 | 27.68 | 29.68 | 0/3 |
| in035 | rife | 不复核 | —% | 27.77 / 0.0554 | 25.61 | 29.62 | 0/3 |
| in035 | rife | oracle | 0.7% | 27.96 / 0.0516 | 26.49 | 29.68 | 0/3 |
| in035 | rife | 不复核 | —% | 27.81 / 0.0547 | 25.95 | 29.60 | 0/3 |
| in035 | rife | oracle | 0.7% | 27.99 / 0.0507 | 26.50 | 29.68 | 1/3 |
| in035 | rife | 不复核 | —% | 27.82 / 0.0551 | 25.88 | 29.62 | 0/3 |
| in035 | rife | oracle | 0.7% | 27.98 / 0.0512 | 26.40 | 29.68 | 0/3 |
| in035 | rife | 不复核 | —% | 27.81 / 0.0549 | 25.87 | 29.60 | 0/3 |
| in035 | rife | oracle | 0.7% | 27.97 / 0.0511 | 26.36 | 29.68 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.96 / 0.0546 | 24.17 | 29.59 | 0/3 |
| in035 | rife_mw | oracle | 0.8% | 28.23 / 0.0500 | 25.89 | 29.67 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.07 / 0.0530 | 26.65 | 29.55 | 0/3 |
| in035 | rife_mw | oracle | 0.8% | 28.38 / 0.0494 | 27.42 | 29.68 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 28.08 / 0.0536 | 25.43 | 29.58 | 0/3 |
| in035 | rife_mw | oracle | 0.8% | 28.33 / 0.0496 | 26.45 | 29.67 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 28.12 / 0.0531 | 25.97 | 29.57 | 0/3 |
| in035 | rife_mw | oracle | 0.8% | 28.37 / 0.0494 | 26.86 | 29.68 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.35 / 0.0496 | 27.96 / 0.0390 | — |
| in035 | FF | 0（前馈） | 1008×672（64%） | 27.08 | 26.92 / 0.0591 | 24.34 / 0.1051 | 0/3 |
| in035 | 25 | 0.57 s | 1008×672（64%） | 27.50 | 27.23 / 0.0573 | 25.28 / 0.0870 | 0/3 |
| in035 | 50 | 1.12 s | 1008×672（64%） | 27.70 | 27.29 / 0.0565 | 25.62 / 0.0778 | 0/3 |
| in035 | 100 | 2.20 s | 1008×672（64%） | 27.91 | 27.38 / 0.0557 | 25.92 / 0.0725 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.35 / 0.0496 | 27.96 / 0.0390 | 29.69 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.92 / 0.0591 | 24.34 / 0.1051 | 29.35 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.50 / 0.0538 | 25.30 / 0.0729 | 29.67 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.23 / 0.0573 | 25.28 / 0.0870 | 29.39 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.73 / 0.0528 | 25.88 / 0.0655 | 29.68 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.29 / 0.0565 | 25.62 / 0.0778 | 29.39 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.80 / 0.0522 | 26.11 / 0.0604 | 29.68 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.38 / 0.0557 | 25.92 / 0.0725 | 29.38 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.88 / 0.0516 | 26.35 / 0.0579 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.85 / 0.0542 | 24.93 / 0.0872 | 29.55 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.16 / 0.0506 | 26.18 / 0.0599 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.10 / 0.0523 | 25.39 / 0.0764 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.32 / 0.0497 | 26.26 / 0.0565 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.16 / 0.0518 | 25.73 / 0.0708 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.37 / 0.0494 | 26.53 / 0.0552 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.22 / 0.0511 | 25.96 / 0.0654 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.43 / 0.0491 | 26.69 / 0.0513 | 29.67 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.62 / 0.0656 | 24.20 / 0.1079 | 29.20 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.45 / 0.0558 | 25.44 / 0.0685 | 29.64 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.88 / 0.0626 | 24.95 / 0.0934 | 29.33 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.60 / 0.0545 | 25.81 / 0.0623 | 29.65 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.93 / 0.0611 | 25.33 / 0.0874 | 29.35 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.64 / 0.0537 | 26.17 / 0.0592 | 29.65 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.00 / 0.0598 | 25.67 / 0.0788 | 29.34 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.70 / 0.0530 | 26.54 / 0.0534 | 29.65 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.43 / 0.0595 | 24.19 / 0.0987 | 29.42 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.01 / 0.0526 | 25.82 / 0.0675 | 29.65 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.69 / 0.0564 | 24.94 / 0.0829 | 29.50 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.11 / 0.0513 | 26.16 / 0.0591 | 29.66 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.75 / 0.0551 | 25.22 / 0.0761 | 29.50 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.17 / 0.0508 | 26.35 / 0.0533 | 29.66 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.82 / 0.0537 | 25.41 / 0.0716 | 29.50 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.21 / 0.0504 | 26.56 / 0.0493 | 29.66 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.77 / 0.0554 | 25.61 / 0.0937 | 29.62 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.96 / 0.0516 | 26.49 / 0.0596 | 29.68 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.82 / 0.0551 | 25.88 / 0.0876 | 29.62 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.98 / 0.0512 | 26.40 / 0.0600 | 29.68 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.81 / 0.0549 | 25.87 / 0.0823 | 29.60 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.97 / 0.0511 | 26.36 / 0.0577 | 29.68 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.81 / 0.0547 | 25.95 / 0.0788 | 29.60 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.99 / 0.0507 | 26.50 / 0.0558 | 29.68 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.96 / 0.0546 | 24.17 / 0.0950 | 29.59 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.23 / 0.0500 | 25.89 / 0.0583 | 29.67 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.08 / 0.0536 | 25.43 / 0.0866 | 29.58 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.33 / 0.0496 | 26.45 / 0.0566 | 29.67 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.12 / 0.0531 | 25.97 / 0.0805 | 29.57 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.37 / 0.0494 | 26.86 / 0.0533 | 29.68 | 2/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.07 / 0.0530 | 26.65 / 0.0697 | 29.55 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.38 / 0.0494 | 27.42 / 0.0457 | 29.68 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.96 / 0.0390 | 20.68 / 0.0107 | 29.69 / 0.0366 | 28.35 / 0.0496 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 3.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.96 | 0.8283 | 0.0390 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 15.27 | 0.6817 | 0.2271 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 16.02 | 0.7295 | 0.1738 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 15.45 | 0.7092 | 0.2056 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 15.55 | 0.7194 | 0.1911 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 15.55 | 0.6432 | 0.1973 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 16.41 | 0.7080 | 0.1565 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 15.77 | 0.6837 | 0.1811 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 16.01 | 0.6978 | 0.1702 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 25.33 | 0.7873 | 0.1133 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 25.30 | 0.7860 | 0.1316 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 25.30 | 0.7860 | 0.1316 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 25.20 | 0.7772 | 0.1251 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 25.20 | 0.7772 | 0.1251 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 16.81 | 0.7260 | 0.1805 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 16.97 | 0.7202 | 0.2120 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 16.97 | 0.7202 | 0.2120 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 17.24 | 0.7189 | 0.2104 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 17.24 | 0.7189 | 0.2104 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 16.34 | 0.6671 | 0.2480 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 18.59 | 0.6853 | 0.2146 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 19.92 | 0.7323 | 0.1578 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 19.18 | 0.7109 | 0.1958 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 19.51 | 0.7215 | 0.1802 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 18.53 | 0.6589 | 0.2017 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.60 | 0.6966 | 0.1648 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 19.09 | 0.6852 | 0.1850 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 19.25 | 0.6916 | 0.1754 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 20.35 | 0.6980 | 0.2138 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 23.08 | 0.7397 | 0.1580 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 22.97 | 0.7629 | 0.1241 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 23.19 | 0.7571 | 0.1410 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 22.98 | 0.7606 | 0.1319 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 22.65 | 0.7174 | 0.1265 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 24.53 | 0.7904 | 0.0942 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 23.86 | 0.7626 | 0.1154 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 24.17 | 0.7790 | 0.1066 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.30 | 0.8028 | 0.0729 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.35 | 0.8215 | 0.0579 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.88 | 0.8106 | 0.0655 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.11 | 0.8160 | 0.0604 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.18 | 0.8013 | 0.0599 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.69 | 0.8168 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.26 | 0.8091 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.53 | 0.8137 | 0.0552 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.52 | 0.8264 | 0.0670 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.87 | 0.8380 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.24 | 0.8313 | 0.0442 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.50 | 0.8342 | 0.0589 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.11 | 0.8288 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.28 | 0.8237 | 0.0563 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.41 | 0.8328 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.05 | 0.8285 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.47 | 0.8333 | 0.0519 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.23 | 0.8299 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.79 | 0.8248 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.44 | 0.7968 | 0.0685 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.54 | 0.8143 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.81 | 0.8038 | 0.0623 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.17 | 0.8088 | 0.0592 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.82 | 0.7976 | 0.0675 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.56 | 0.8083 | 0.0493 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.16 | 0.8007 | 0.0591 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.35 | 0.8041 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.68 | 0.8221 | 0.0589 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.49 | 0.8152 | 0.0596 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.50 | 0.8188 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.40 | 0.8157 | 0.0600 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.36 | 0.8165 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.89 | 0.7985 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.42 | 0.8245 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.45 | 0.8087 | 0.0566 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.86 | 0.8167 | 0.0533 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.34 | 0.7833 | 0.1051 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.92 | 0.8137 | 0.0725 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.28 | 0.7995 | 0.0870 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.62 | 0.8072 | 0.0778 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.93 | 0.7734 | 0.0872 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.96 | 0.8053 | 0.0654 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.39 | 0.7922 | 0.0764 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.73 | 0.7995 | 0.0708 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.20 | 0.8193 | 0.0779 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.38 | 0.8293 | 0.0757 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.08 | 0.8264 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.99 | 0.8252 | 0.0719 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.86 | 0.8251 | 0.0569 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.92 | 0.8195 | 0.0660 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.93 | 0.8254 | 0.0698 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.92 | 0.8245 | 0.0494 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.94 | 0.8252 | 0.0673 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.97 | 0.8255 | 0.0513 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.06 | 0.7985 | 0.1100 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.20 | 0.7588 | 0.1079 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.67 | 0.7852 | 0.0788 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.95 | 0.7741 | 0.0934 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.33 | 0.7806 | 0.0874 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.19 | 0.7631 | 0.0987 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.41 | 0.7840 | 0.0716 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.94 | 0.7754 | 0.0829 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.22 | 0.7801 | 0.0761 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.90 | 0.7967 | 0.1076 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.61 | 0.7984 | 0.0937 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.95 | 0.8126 | 0.0788 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.88 | 0.8076 | 0.0876 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.87 | 0.8103 | 0.0823 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.17 | 0.7583 | 0.0950 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.65 | 0.8172 | 0.0697 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.43 | 0.7903 | 0.0866 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.97 | 0.8051 | 0.0805 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.68 | 0.6783 | 0.0107 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.69 | 0.1860 | 0.1160 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.81 | 0.2178 | 0.1123 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.73 | 0.2020 | 0.1147 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.77 | 0.2082 | 0.1137 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.82 | 0.2226 | 0.1016 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.85 | 0.2571 | 0.0982 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.84 | 0.2421 | 0.0998 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.84 | 0.2492 | 0.0993 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.21 | 0.2761 | 0.0582 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 12.69 | 0.2370 | 0.0604 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 12.69 | 0.2370 | 0.0604 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 12.68 | 0.2339 | 0.0616 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 12.68 | 0.2339 | 0.0616 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.02 | 0.2190 | 0.0687 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.78 | 0.1842 | 0.0724 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.78 | 0.1842 | 0.0724 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 10.77 | 0.1808 | 0.0735 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 10.77 | 0.1808 | 0.0735 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.76 | 0.1772 | 0.0723 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.03 | 0.2746 | 0.0974 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.22 | 0.3162 | 0.0929 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.10 | 0.2951 | 0.0957 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.15 | 0.3040 | 0.0947 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.81 | 0.3326 | 0.0831 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.86 | 0.3621 | 0.0797 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.62 | 0.3435 | 0.0818 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.60 | 0.3523 | 0.0808 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.07 | 0.2837 | 0.0607 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.93 | 0.1580 | 0.1244 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.03 | 0.1794 | 0.1211 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.98 | 0.1702 | 0.1230 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.01 | 0.1740 | 0.1222 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.99 | 0.1738 | 0.1236 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.10 | 0.2021 | 0.1198 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.02 | 0.1842 | 0.1222 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.06 | 0.1925 | 0.1211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.03 | 0.6522 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.78 | 0.6786 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.46 | 0.6674 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.62 | 0.6721 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.44 | 0.6898 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.12 | 0.7144 | 0.0101 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.77 | 0.7008 | 0.0108 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.95 | 0.7076 | 0.0105 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.68 | 0.6804 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.71 | 0.6619 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.68 | 0.6600 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.73 | 0.6572 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.71 | 0.6568 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.65 | 0.6785 | 0.0120 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.66 | 0.6617 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.66 | 0.6625 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.51 | 0.6546 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.52 | 0.6548 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.95 | 0.6652 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.98 | 0.6248 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.45 | 0.6527 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.22 | 0.6397 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.31 | 0.6454 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.18 | 0.6780 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.66 | 0.7024 | 0.0118 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.37 | 0.6893 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.50 | 0.6954 | 0.0121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.57 | 0.6399 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.87 | 0.6697 | 0.0125 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.89 | 0.6822 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.87 | 0.6774 | 0.0121 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.85 | 0.6793 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.50 | 0.6881 | 0.0112 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.96 | 0.7076 | 0.0104 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.77 | 0.6966 | 0.0108 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.90 | 0.7034 | 0.0106 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.01 | 0.6508 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.76 | 0.6767 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.44 | 0.6657 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.59 | 0.6703 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.43 | 0.6886 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.10 | 0.7133 | 0.0102 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.76 | 0.6999 | 0.0110 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.93 | 0.7067 | 0.0106 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.68 | 0.6800 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.70 | 0.6618 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.67 | 0.6602 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.72 | 0.6564 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.70 | 0.6558 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.66 | 0.6783 | 0.0119 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.66 | 0.6619 | 0.0137 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.65 | 0.6628 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.51 | 0.6539 | 0.0144 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.51 | 0.6539 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.94 | 0.6641 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.96 | 0.6213 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.43 | 0.6500 | 0.0144 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.20 | 0.6367 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.28 | 0.6425 | 0.0152 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.14 | 0.6753 | 0.0138 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.64 | 0.7007 | 0.0119 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.35 | 0.6870 | 0.0126 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.48 | 0.6934 | 0.0122 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.57 | 0.6380 | 0.0159 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.86 | 0.6687 | 0.0125 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.89 | 0.6819 | 0.0119 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.87 | 0.6766 | 0.0121 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.84 | 0.6786 | 0.0123 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.49 | 0.6867 | 0.0114 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.95 | 0.7069 | 0.0106 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.75 | 0.6952 | 0.0110 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.87 | 0.7022 | 0.0108 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 26.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.61 | 0.7804 | 0.0174 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.50 | 0.4202 | 0.2200 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.69 | 0.4424 | 0.2103 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.55 | 0.4365 | 0.2164 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.60 | 0.4384 | 0.2140 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.58 | 0.3664 | 0.1954 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.74 | 0.3938 | 0.1865 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.60 | 0.3870 | 0.1921 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.64 | 0.3902 | 0.1902 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.96 | 0.5312 | 0.1130 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.09 | 0.4961 | 0.1254 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.09 | 0.4961 | 0.1254 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.03 | 0.4846 | 0.1286 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.03 | 0.4846 | 0.1286 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.02 | 0.3594 | 0.1446 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.57 | 0.2995 | 0.1642 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.57 | 0.2995 | 0.1642 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.55 | 0.2900 | 0.1664 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.55 | 0.2900 | 0.1664 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.47 | 0.2710 | 0.1665 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.07 | 0.4676 | 0.1953 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.36 | 0.4957 | 0.1802 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.15 | 0.4885 | 0.1892 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.23 | 0.4906 | 0.1857 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.81 | 0.4375 | 0.1712 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.07 | 0.4614 | 0.1567 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.79 | 0.4580 | 0.1658 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.83 | 0.4594 | 0.1626 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.98 | 0.3628 | 0.1456 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.05 | 0.4267 | 0.2149 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.19 | 0.4450 | 0.2054 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.11 | 0.4443 | 0.2104 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.14 | 0.4451 | 0.2083 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.10 | 0.4359 | 0.2092 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.27 | 0.4557 | 0.2012 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.16 | 0.4526 | 0.2065 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.21 | 0.4551 | 0.2040 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.86 | 0.7650 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.59 | 0.7755 | 0.0203 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.30 | 0.7715 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.44 | 0.7734 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.10 | 0.7784 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.76 | 0.7879 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.46 | 0.7836 | 0.0184 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.60 | 0.7857 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.49 | 0.7772 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.66 | 0.7705 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.66 | 0.7715 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.56 | 0.7671 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.58 | 0.7686 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.47 | 0.7777 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.63 | 0.7708 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.66 | 0.7724 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.44 | 0.7677 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.47 | 0.7687 | 0.0212 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.73 | 0.7693 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.77 | 0.7569 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.28 | 0.7679 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.05 | 0.7634 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.14 | 0.7654 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.81 | 0.7731 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.33 | 0.7817 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.09 | 0.7784 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.21 | 0.7801 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.26 | 0.7584 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.70 | 0.7736 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.80 | 0.7792 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.76 | 0.7771 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.76 | 0.7780 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.25 | 0.7803 | 0.0184 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.59 | 0.7859 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.50 | 0.7834 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.58 | 0.7848 | 0.0178 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.39 | 0.7465 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.21 | 0.7601 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.90 | 0.7568 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.02 | 0.7580 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.64 | 0.7641 | 0.0233 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.49 | 0.7779 | 0.0205 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.31 | 0.7747 | 0.0212 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.44 | 0.7766 | 0.0208 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.16 | 0.7687 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.41 | 0.7517 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.52 | 0.7582 | 0.0263 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.25 | 0.7453 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.37 | 0.7522 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.14 | 0.7715 | 0.0206 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.40 | 0.7529 | 0.0278 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.56 | 0.7596 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.17 | 0.7469 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.28 | 0.7519 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.96 | 0.7381 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.71 | 0.7194 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.36 | 0.7352 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.12 | 0.7316 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.20 | 0.7329 | 0.0315 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.88 | 0.7436 | 0.0287 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.64 | 0.7597 | 0.0244 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.50 | 0.7571 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.57 | 0.7585 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.16 | 0.7115 | 0.0394 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.90 | 0.7645 | 0.0241 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.01 | 0.7735 | 0.0239 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.05 | 0.7726 | 0.0237 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.04 | 0.7738 | 0.0232 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.05 | 0.7681 | 0.0237 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.36 | 0.7774 | 0.0237 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.46 | 0.7769 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.54 | 0.7788 | 0.0234 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 39.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.88 | 0.7365 | 0.0255 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.61 | 0.3458 | 0.3606 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.69 | 0.3586 | 0.3532 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.63 | 0.3549 | 0.3585 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.66 | 0.3563 | 0.3564 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.91 | 0.3083 | 0.3093 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.93 | 0.3243 | 0.3014 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.91 | 0.3201 | 0.3068 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.91 | 0.3220 | 0.3049 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.41 | 0.5064 | 0.1717 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.05 | 0.4874 | 0.1784 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.05 | 0.4874 | 0.1784 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.02 | 0.4811 | 0.1808 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.02 | 0.4811 | 0.1808 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.62 | 0.2608 | 0.2208 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.54 | 0.2436 | 0.2274 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.54 | 0.2436 | 0.2274 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.54 | 0.2386 | 0.2302 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.54 | 0.2386 | 0.2302 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.49 | 0.2346 | 0.2283 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.58 | 0.3983 | 0.3321 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.65 | 0.4150 | 0.3192 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.60 | 0.4114 | 0.3274 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.62 | 0.4133 | 0.3238 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.44 | 0.3783 | 0.2795 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.43 | 0.3890 | 0.2687 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.32 | 0.3886 | 0.2755 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.34 | 0.3890 | 0.2727 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.65 | 0.3220 | 0.2022 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.48 | 0.3453 | 0.3560 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.55 | 0.3583 | 0.3478 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.51 | 0.3560 | 0.3527 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.53 | 0.3573 | 0.3506 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.51 | 0.3617 | 0.3495 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.57 | 0.3726 | 0.3423 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.53 | 0.3699 | 0.3469 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.54 | 0.3711 | 0.3446 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.70 | 0.7290 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.32 | 0.7347 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.09 | 0.7327 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.21 | 0.7336 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.65 | 0.7356 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.07 | 0.7406 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.90 | 0.7385 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.98 | 0.7396 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.82 | 0.7352 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.17 | 0.7315 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.19 | 0.7322 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.17 | 0.7301 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.20 | 0.7309 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.78 | 0.7350 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.22 | 0.7320 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.26 | 0.7328 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.18 | 0.7309 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.22 | 0.7314 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.29 | 0.7320 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.52 | 0.7233 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.88 | 0.7289 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.73 | 0.7267 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.79 | 0.7278 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.34 | 0.7327 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.66 | 0.7367 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.54 | 0.7356 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.60 | 0.7363 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.87 | 0.7261 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.41 | 0.7339 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.62 | 0.7371 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.55 | 0.7360 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.57 | 0.7364 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.76 | 0.7364 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.92 | 0.7393 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.93 | 0.7381 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.96 | 0.7388 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.01 | 0.7201 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.77 | 0.7282 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.51 | 0.7261 | 0.0321 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.62 | 0.7271 | 0.0314 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.24 | 0.7308 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.74 | 0.7377 | 0.0265 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.58 | 0.7354 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.66 | 0.7366 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.74 | 0.7336 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.89 | 0.7265 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.98 | 0.7285 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.77 | 0.7232 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.84 | 0.7254 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.66 | 0.7338 | 0.0275 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.96 | 0.7275 | 0.0317 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.08 | 0.7295 | 0.0297 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.82 | 0.7248 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.91 | 0.7263 | 0.0312 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.95 | 0.7251 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.38 | 0.7056 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.98 | 0.7151 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.76 | 0.7128 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.86 | 0.7141 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.43 | 0.7208 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.03 | 0.7285 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.85 | 0.7272 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.92 | 0.7281 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.36 | 0.7155 | 0.0356 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.11 | 0.7288 | 0.0306 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.32 | 0.7338 | 0.0296 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.30 | 0.7327 | 0.0301 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.29 | 0.7332 | 0.0299 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.27 | 0.7302 | 0.0298 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.45 | 0.7362 | 0.0282 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.53 | 0.7344 | 0.0288 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.58 | 0.7358 | 0.0282 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 80.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.69 | 0.7096 | 0.0366 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.41 | 0.2811 | 0.4017 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.46 | 0.2828 | 0.3972 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.43 | 0.2831 | 0.4001 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.44 | 0.2829 | 0.3988 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.69 | 0.2195 | 0.3640 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.71 | 0.2225 | 0.3601 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.69 | 0.2232 | 0.3631 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.70 | 0.2229 | 0.3617 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.92 | 0.4592 | 0.2687 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.83 | 0.4550 | 0.2718 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.83 | 0.4550 | 0.2718 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.83 | 0.4522 | 0.2725 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.83 | 0.4522 | 0.2725 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.44 | 0.1265 | 0.2934 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.43 | 0.1243 | 0.2955 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.43 | 0.1243 | 0.2955 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.43 | 0.1219 | 0.2968 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.43 | 0.1219 | 0.2968 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.41 | 0.1205 | 0.2951 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.90 | 0.3185 | 0.3733 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 2.95 | 0.3214 | 0.3652 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 2.92 | 0.3231 | 0.3697 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 2.93 | 0.3227 | 0.3674 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.03 | 0.2667 | 0.3382 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.00 | 0.2655 | 0.3310 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.97 | 0.2694 | 0.3361 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.00 | 0.2677 | 0.3336 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.93 | 0.1824 | 0.2721 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.27 | 0.2732 | 0.3986 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.31 | 0.2761 | 0.3931 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.28 | 0.2759 | 0.3965 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.29 | 0.2760 | 0.3950 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.27 | 0.2793 | 0.3941 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.28 | 0.2805 | 0.3894 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.27 | 0.2813 | 0.3927 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.28 | 0.2810 | 0.3911 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.67 | 0.7094 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.67 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.67 | 0.7094 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.67 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.67 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.67 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.68 | 0.7096 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.69 | 0.7096 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.64 | 0.7091 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.65 | 0.7093 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.65 | 0.7093 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.65 | 0.7093 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.65 | 0.7093 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.66 | 0.7094 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.66 | 0.7094 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.66 | 0.7094 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.68 | 0.7096 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.67 | 0.7094 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.67 | 0.7095 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.68 | 0.7095 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.35 | 0.7083 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.38 | 0.7086 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.39 | 0.7087 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.39 | 0.7087 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.55 | 0.7090 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.61 | 0.7095 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.61 | 0.7095 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.61 | 0.7096 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.69 | 0.7100 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.66 | 0.7098 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.66 | 0.7094 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.63 | 0.7094 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.63 | 0.7092 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.69 | 0.7100 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.65 | 0.7098 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.65 | 0.7094 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.63 | 0.7095 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.63 | 0.7092 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.64 | 0.7096 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.20 | 0.7069 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.34 | 0.7077 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.33 | 0.7079 | 0.0407 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.35 | 0.7080 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.42 | 0.7084 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.50 | 0.7088 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.50 | 0.7091 | 0.0390 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.50 | 0.7090 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.59 | 0.7097 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.62 | 0.7090 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.60 | 0.7091 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.62 | 0.7092 | 0.0381 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.60 | 0.7091 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.59 | 0.7089 | 0.0386 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.55 | 0.7092 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.58 | 0.7092 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.57 | 0.7092 | 0.0384 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.35 | 0.7204 | 0.0496 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.85 | 0.2941 | 0.4628 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.91 | 0.3009 | 0.4534 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.87 | 0.2990 | 0.4595 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.89 | 0.2996 | 0.4568 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.00 | 0.2417 | 0.4302 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.02 | 0.2499 | 0.4210 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.00 | 0.2483 | 0.4273 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.00 | 0.2489 | 0.4246 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.08 | 0.4605 | 0.3612 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.91 | 0.4491 | 0.3677 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.91 | 0.4491 | 0.3677 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.90 | 0.4447 | 0.3700 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.90 | 0.4447 | 0.3700 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.51 | 0.1706 | 0.3796 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.47 | 0.1611 | 0.3864 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.47 | 0.1611 | 0.3864 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.46 | 0.1572 | 0.3893 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.46 | 0.1572 | 0.3893 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.44 | 0.1557 | 0.3873 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.45 | 0.3372 | 0.4300 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.51 | 0.3458 | 0.4135 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.47 | 0.3452 | 0.4240 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.49 | 0.3456 | 0.4193 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.42 | 0.2975 | 0.3952 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.40 | 0.3013 | 0.3809 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.36 | 0.3027 | 0.3902 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.37 | 0.3021 | 0.3855 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.15 | 0.2263 | 0.3503 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.62 | 0.2839 | 0.4576 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.67 | 0.2903 | 0.4479 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.64 | 0.2891 | 0.4541 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.66 | 0.2897 | 0.4513 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.63 | 0.2924 | 0.4494 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.66 | 0.2974 | 0.4411 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.64 | 0.2964 | 0.4464 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.65 | 0.2969 | 0.4437 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.50 | 0.7161 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.88 | 0.7187 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.73 | 0.7178 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.80 | 0.7182 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.16 | 0.7195 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.43 | 0.7221 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.32 | 0.7210 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.37 | 0.7215 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.32 | 0.7200 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.87 | 0.7179 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.88 | 0.7182 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.85 | 0.7170 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.85 | 0.7172 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.31 | 0.7199 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.86 | 0.7181 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.88 | 0.7184 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.78 | 0.7172 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.79 | 0.7174 | 0.0531 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.00 | 0.7183 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.45 | 0.7136 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.70 | 0.7163 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.60 | 0.7153 | 0.0545 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.64 | 0.7158 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.01 | 0.7181 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.21 | 0.7201 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.11 | 0.7193 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.17 | 0.7198 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.78 | 0.7157 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.96 | 0.7187 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.99 | 0.7199 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.98 | 0.7194 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.97 | 0.7196 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.23 | 0.7199 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.38 | 0.7215 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.33 | 0.7207 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.37 | 0.7211 | 0.0494 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.92 | 0.7113 | 0.0591 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.38 | 0.7150 | 0.0557 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.23 | 0.7141 | 0.0573 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.29 | 0.7145 | 0.0565 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.85 | 0.7170 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.22 | 0.7206 | 0.0511 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.10 | 0.7195 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.16 | 0.7201 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.29 | 0.7194 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.63 | 0.7155 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.67 | 0.7161 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.50 | 0.7135 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.53 | 0.7142 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.25 | 0.7195 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.62 | 0.7159 | 0.0563 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.67 | 0.7165 | 0.0541 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.46 | 0.7141 | 0.0574 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.49 | 0.7145 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.71 | 0.7149 | 0.0595 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.62 | 0.7044 | 0.0656 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.00 | 0.7088 | 0.0598 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.88 | 0.7080 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.93 | 0.7086 | 0.0611 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.43 | 0.7123 | 0.0595 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.82 | 0.7162 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.69 | 0.7154 | 0.0564 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.75 | 0.7159 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.37 | 0.7110 | 0.0609 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.77 | 0.7163 | 0.0554 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.81 | 0.7183 | 0.0547 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.82 | 0.7179 | 0.0551 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.81 | 0.7181 | 0.0549 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.96 | 0.7172 | 0.0546 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.07 | 0.7199 | 0.0530 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.08 | 0.7189 | 0.0536 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.12 | 0.7196 | 0.0531 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 265244 | 0.165 | 41.3 | 29.36 | 0.15 | 0.041 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 265244 | 0.165 | 40.5 | 29.36 | 0.15 | 0.041 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 265244 | 0.165 | 38.5 | 29.36 | 0.15 | 0.041 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 265244 | 0.165 | 37.0 | 29.36 | 0.15 | 0.041 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 648 | None | classic | 0.30 | False | 401359 | 0.520 | 108.5 | 28.72 | 0.36 | 0.015 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 648 | None | classic | 0.30 | False | 401359 | 0.520 | 97.4 | 28.72 | 0.36 | 0.015 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 648 | None | classic | 0.30 | False | 401359 | 0.520 | 100.0 | 28.72 | 0.36 | 0.015 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 648 | None | classic | 0.30 | False | 401359 | 0.520 | 92.2 | 28.72 | 0.36 | 0.015 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 825543 | 0.178 | 21.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 825350 | 0.797 | 47.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 825350 | 0.797 | 47.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 825350 | 0.635 | 21.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 825350 | 0.635 | 21.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 825543 | 0.178 | 28.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 825350 | 0.797 | 71.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 825350 | 0.797 | 71.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 825350 | 0.635 | 28.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 825350 | 0.635 | 28.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 822346 | 0.797 | 150.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 252557 | 0.171 | 44.1 | 29.26 | 0.12 | 0.043 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 252557 | 0.171 | 43.9 | 29.26 | 0.12 | 0.043 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 252557 | 0.171 | 48.5 | 29.26 | 0.12 | 0.043 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 252557 | 0.171 | 45.5 | 29.26 | 0.12 | 0.043 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 834 | None | classic | 0.41 | False | 446566 | 0.524 | 104.3 | 30.77 | 0.13 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 834 | None | classic | 0.41 | False | 446566 | 0.524 | 106.0 | 30.77 | 0.13 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 834 | None | classic | 0.41 | False | 446566 | 0.524 | 112.1 | 30.77 | 0.13 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 834 | None | classic | 0.41 | False | 446566 | 0.524 | 105.3 | 30.77 | 0.13 | 0.015 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1232417 | 0.797 | 69.6 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 264806 | 0.322 | 40.3 | 29.73 | 0.15 | 0.033 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 264806 | 0.322 | 38.5 | 29.73 | 0.15 | 0.033 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 264806 | 0.322 | 42.4 | 29.73 | 0.15 | 0.033 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 264806 | 0.322 | 38.9 | 29.73 | 0.15 | 0.033 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 725 | None | classic | 0.56 | False | 413782 | 0.519 | 112.7 | 27.20 | 0.12 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 725 | None | classic | 0.56 | False | 413782 | 0.519 | 99.3 | 27.20 | 0.12 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 725 | None | classic | 0.56 | False | 413782 | 0.519 | 106.1 | 27.20 | 0.12 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 725 | None | classic | 0.56 | False | 413782 | 0.519 | 102.1 | 27.20 | 0.12 | 0.013 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.689 | 0.017 |
| in035 | mask_ent | 0.784 | 0.017 |
| in035 | mask_grad | 0.442 | 0.017 |
| in035 | r_col | 0.752 | 0.017 |
| in035 | r_warp | 0.887 | 0.017 |

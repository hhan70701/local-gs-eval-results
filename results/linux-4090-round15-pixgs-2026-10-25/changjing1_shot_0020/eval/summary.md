# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 9.3% | 24.65 / 0.0100 | 21.22 / 0.0285 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.8% | 24.78 / 0.0102 | 22.73 / 0.0224 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.5% | 24.69 / 0.0101 | 22.25 / 0.0240 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.6% | 24.72 / 0.0101 | 22.53 / 0.0226 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.5% | 24.79 / 0.0106 | 20.65 / 0.0287 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.0% | 24.86 / 0.0110 | 22.66 / 0.0223 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.7% | 24.83 / 0.0108 | 21.86 / 0.0247 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.8% | 24.80 / 0.0109 | 22.22 / 0.0226 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 11.0% | 25.20 / 0.0119 | 20.34 / 0.0429 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 15.2% | 25.48 / 0.0143 | 21.25 / 0.0457 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 15.8% | 25.57 / 0.0146 | 22.55 / 0.0344 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 15.4% | 25.50 / 0.0145 | 22.31 / 0.0390 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 15.5% | 25.53 / 0.0146 | 22.48 / 0.0365 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 15.3% | 25.55 / 0.0143 | 21.04 / 0.0434 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 15.9% | 25.60 / 0.0149 | 22.64 / 0.0348 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 15.4% | 25.59 / 0.0145 | 22.16 / 0.0387 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 15.6% | 25.59 / 0.0145 | 22.40 / 0.0365 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 16.9% | 25.78 / 0.0158 | 20.56 / 0.0554 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 8.1% | 24.51 / 0.0094 | 21.01 / 0.0242 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 8.7% | 24.72 / 0.0101 | 22.08 / 0.0199 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 8.3% | 24.57 / 0.0093 | 21.77 / 0.0212 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 8.4% | 24.62 / 0.0097 | 22.02 / 0.0203 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 9.3% | 24.75 / 0.0100 | 21.30 / 0.0247 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 10.5% | 25.02 / 0.0111 | 21.40 / 0.0263 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 9.7% | 24.88 / 0.0103 | 21.58 / 0.0239 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 9.9% | 24.93 / 0.0103 | 21.66 / 0.0240 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.20 / 0.0540 | 25.53 / 0.0613 | 20.68 / 0.0132 | 29.79 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.39 / 0.0687 | 23.81 / 0.1291 | 20.42 / 0.0162 | 29.41 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.83 / 0.0628 | 25.08 / 0.0869 | 20.86 / 0.0145 | 29.60 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.73 / 0.0656 | 24.61 / 0.1095 | 20.69 / 0.0152 | 29.56 / 0.0396 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.81 / 0.0641 | 24.88 / 0.0976 | 20.81 / 0.0148 | 29.59 / 0.0394 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.10 / 0.0678 | 22.75 / 0.1300 | 19.97 / 0.0172 | 29.33 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.83 / 0.0614 | 24.90 / 0.0866 | 20.88 / 0.0143 | 29.60 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.49 / 0.0652 | 23.70 / 0.1129 | 20.40 / 0.0161 | 29.50 / 0.0401 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.62 / 0.0633 | 24.23 / 0.0998 | 20.54 / 0.0153 | 29.57 / 0.0397 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.30 / 0.0661 | 23.57 / 0.1229 | 20.62 / 0.0166 | 29.28 / 0.0428 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.74 / 0.0791 | 23.03 / 0.1626 | 19.98 / 0.0183 | 29.01 / 0.0445 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.36 / 0.0692 | 24.54 / 0.1031 | 20.47 / 0.0157 | 29.39 / 0.0422 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.24 / 0.0743 | 24.00 / 0.1373 | 20.34 / 0.0167 | 29.30 / 0.0430 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.33 / 0.0717 | 24.32 / 0.1191 | 20.45 / 0.0162 | 29.36 / 0.0425 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.56 / 0.0768 | 22.40 / 0.1611 | 19.60 / 0.0193 | 28.93 / 0.0442 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.32 / 0.0681 | 24.36 / 0.1066 | 20.51 / 0.0159 | 29.33 / 0.0419 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.05 / 0.0731 | 23.42 / 0.1387 | 20.07 / 0.0176 | 29.19 / 0.0429 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.19 / 0.0707 | 23.88 / 0.1218 | 20.26 / 0.0168 | 29.27 / 0.0425 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.63 / 0.0710 | 23.65 / 0.1284 | 20.43 / 0.0181 | 29.04 / 0.0449 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.50 / 0.0676 | 24.01 / 0.1309 | 20.46 / 0.0148 | 29.51 / 0.0406 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.83 / 0.0627 | 25.05 / 0.0928 | 20.94 / 0.0135 | 29.60 / 0.0394 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.71 / 0.0654 | 24.55 / 0.1140 | 20.79 / 0.0141 | 29.58 / 0.0400 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.77 / 0.0640 | 24.78 / 0.1030 | 20.88 / 0.0138 | 29.59 / 0.0397 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.38 / 0.0661 | 23.16 / 0.1261 | 20.69 / 0.0143 | 28.99 / 0.0432 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.39 / 0.0641 | 23.21 / 0.1079 | 20.64 / 0.0136 | 28.93 / 0.0439 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.42 / 0.0660 | 23.48 / 0.1168 | 20.72 / 0.0137 | 28.97 / 0.0435 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.42 / 0.0651 | 23.40 / 0.1117 | 20.71 / 0.0135 | 28.97 / 0.0436 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.0%） | — | — | 28.20 / 0.0540 | 25.53 / 0.0613 | 29.79 |
| in035 | rife | 4.0% | 8.1% | 27.50 / 0.0676 | 24.01 / 0.1309 | 29.51 |
| in035 | cnw_cnn | 6.1% | 9.3% | 27.39 / 0.0687 | 23.81 / 0.1291 | 29.41 |
| in035 | cnw_f5 | 9.9% | 15.2% | 26.74 / 0.0791 | 23.03 / 0.1626 | 29.01 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.63 / 0.0519 | -0.63 / +0.0153 (core 4.2%) | -0.70 / +0.0168 (core 6.1%) | -1.25 / +0.0290 (core 10.9%) |
| in035 | 2 | 0-3 | 28.60 / 0.0537 | -1.16 / +0.0181 (core 4.2%) | -1.09 / +0.0170 (core 6.1%) | -1.99 / +0.0316 (core 10.9%) |
| in035 | 4 | 3-5 | 28.39 / 0.0564 | -0.31 / +0.0073 (core 2.3%) | -0.66 / +0.0103 (core 4.2%) | -1.14 / +0.0146 (core 6.1%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.20 / 0.0540 | 25.53 | 29.79 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.39 / 0.0687 | 23.81 | 29.41 | 0/3 |
| in035 | cnw_cnn | oracle | 1.8% | 27.98 / 0.0595 | 25.11 | 29.76 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.83 / 0.0628 | 25.08 | 29.60 | 0/3 |
| in035 | cnw_cnn | oracle | 1.8% | 28.20 / 0.0567 | 25.93 | 29.78 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.73 / 0.0656 | 24.61 | 29.56 | 0/3 |
| in035 | cnw_cnn | oracle | 1.8% | 28.12 / 0.0582 | 25.61 | 29.77 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.81 / 0.0641 | 24.88 | 29.59 | 0/3 |
| in035 | cnw_cnn | oracle | 1.8% | 28.18 / 0.0574 | 25.78 | 29.78 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.10 / 0.0678 | 22.75 | 29.33 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.8% | 27.74 / 0.0600 | 24.18 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.83 / 0.0614 | 24.90 | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.8% | 28.19 / 0.0565 | 25.68 | 29.78 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.49 / 0.0652 | 23.70 | 29.50 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.8% | 27.96 / 0.0587 | 24.82 | 29.76 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.62 / 0.0633 | 24.23 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.8% | 28.03 / 0.0577 | 25.18 | 29.77 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.30 / 0.0661 | 23.57 | 29.28 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.9% | 28.02 / 0.0580 | 25.40 | 29.75 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.74 / 0.0791 | 23.03 | 29.01 | 0/3 |
| in035 | cnw_f5 | oracle | 2.4% | 27.75 / 0.0621 | 24.71 | 29.70 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.36 / 0.0692 | 24.54 | 29.39 | 0/3 |
| in035 | cnw_f5 | oracle | 2.4% | 28.02 / 0.0581 | 25.72 | 29.75 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.24 / 0.0743 | 24.00 | 29.30 | 0/3 |
| in035 | cnw_f5 | oracle | 2.4% | 27.95 / 0.0603 | 25.34 | 29.74 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.33 / 0.0717 | 24.32 | 29.36 | 0/3 |
| in035 | cnw_f5 | oracle | 2.4% | 28.01 / 0.0593 | 25.55 | 29.75 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.56 / 0.0768 | 22.40 | 28.93 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.4% | 27.51 / 0.0625 | 24.09 | 29.68 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.32 / 0.0681 | 24.36 | 29.33 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.5% | 28.00 / 0.0583 | 25.49 | 29.75 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.05 / 0.0731 | 23.42 | 29.19 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.4% | 27.77 / 0.0608 | 24.75 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.19 / 0.0707 | 23.88 | 29.27 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.4% | 27.87 / 0.0596 | 25.13 | 29.74 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.63 / 0.0710 | 23.65 | 29.04 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.5% | 27.86 / 0.0593 | 25.41 | 29.73 | 0/3 |
| in035 | rife | 不复核 | —% | 27.50 / 0.0676 | 24.01 | 29.51 | 0/3 |
| in035 | rife | oracle | 1.4% | 28.03 / 0.0575 | 25.23 | 29.77 | 0/3 |
| in035 | rife | 不复核 | —% | 27.83 / 0.0627 | 25.05 | 29.60 | 0/3 |
| in035 | rife | oracle | 1.5% | 28.23 / 0.0554 | 25.97 | 29.79 | 0/3 |
| in035 | rife | 不复核 | —% | 27.71 / 0.0654 | 24.55 | 29.58 | 0/3 |
| in035 | rife | oracle | 1.4% | 28.17 / 0.0564 | 25.64 | 29.78 | 0/3 |
| in035 | rife | 不复核 | —% | 27.77 / 0.0640 | 24.78 | 29.59 | 0/3 |
| in035 | rife | oracle | 1.4% | 28.21 / 0.0559 | 25.77 | 29.78 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.38 / 0.0661 | 23.16 | 28.99 | 0/3 |
| in035 | rife_mw | oracle | 1.5% | 28.07 / 0.0562 | 25.09 | 29.71 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.39 / 0.0641 | 23.21 | 28.93 | 0/3 |
| in035 | rife_mw | oracle | 1.6% | 28.04 / 0.0553 | 25.09 | 29.70 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.42 / 0.0660 | 23.48 | 28.97 | 0/3 |
| in035 | rife_mw | oracle | 1.5% | 28.09 / 0.0558 | 25.33 | 29.72 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.42 / 0.0651 | 23.40 | 28.97 | 0/3 |
| in035 | rife_mw | oracle | 1.5% | 28.08 / 0.0555 | 25.23 | 29.71 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.20 / 0.0540 | 25.53 / 0.0613 | — |
| in035 | FF | 0（前馈） | 1008×597（57%） | 26.81 | 27.39 / 0.0687 | 23.81 / 0.1291 | 0/3 |
| in035 | 25 | 0.62 s | 1008×597（57%） | 27.47 | 27.73 / 0.0656 | 24.61 / 0.1095 | 0/3 |
| in035 | 50 | 1.22 s | 1008×597（57%） | 27.76 | 27.81 / 0.0641 | 24.88 / 0.0976 | 0/3 |
| in035 | 100 | 2.40 s | 1008×597（57%） | 28.01 | 27.83 / 0.0628 | 25.08 / 0.0869 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.20 / 0.0540 | 25.53 / 0.0613 | 29.79 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.39 / 0.0687 | 23.81 / 0.1291 | 29.41 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.98 / 0.0595 | 25.11 / 0.0857 | 29.76 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.73 / 0.0656 | 24.61 / 0.1095 | 29.56 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.12 / 0.0582 | 25.61 / 0.0762 | 29.77 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.81 / 0.0641 | 24.88 / 0.0976 | 29.59 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.18 / 0.0574 | 25.78 / 0.0710 | 29.78 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.83 / 0.0628 | 25.08 / 0.0869 | 29.60 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.20 / 0.0567 | 25.93 / 0.0664 | 29.78 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.10 / 0.0678 | 22.75 / 0.1300 | 29.33 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.74 / 0.0600 | 24.18 / 0.0916 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.49 / 0.0652 | 23.70 / 0.1129 | 29.50 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.96 / 0.0587 | 24.82 / 0.0821 | 29.76 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.62 / 0.0633 | 24.23 / 0.0998 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.03 / 0.0577 | 25.18 / 0.0739 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.83 / 0.0614 | 24.90 / 0.0866 | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.19 / 0.0565 | 25.68 / 0.0666 | 29.78 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.74 / 0.0791 | 23.03 / 0.1626 | 29.01 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.75 / 0.0621 | 24.71 / 0.0990 | 29.70 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.24 / 0.0743 | 24.00 / 0.1373 | 29.30 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.95 / 0.0603 | 25.34 / 0.0873 | 29.74 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.33 / 0.0717 | 24.32 / 0.1191 | 29.36 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.01 / 0.0593 | 25.55 / 0.0796 | 29.75 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.36 / 0.0692 | 24.54 / 0.1031 | 29.39 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.02 / 0.0581 | 25.72 / 0.0725 | 29.75 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.56 / 0.0768 | 22.40 / 0.1611 | 28.93 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.51 / 0.0625 | 24.09 / 0.1004 | 29.68 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.05 / 0.0731 | 23.42 / 0.1387 | 29.19 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.77 / 0.0608 | 24.75 / 0.0907 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.19 / 0.0707 | 23.88 / 0.1218 | 29.27 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.87 / 0.0596 | 25.13 / 0.0820 | 29.74 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.32 / 0.0681 | 24.36 / 0.1066 | 29.33 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.00 / 0.0583 | 25.49 / 0.0743 | 29.75 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.50 / 0.0676 | 24.01 / 0.1309 | 29.51 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.03 / 0.0575 | 25.23 / 0.0859 | 29.77 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.71 / 0.0654 | 24.55 / 0.1140 | 29.58 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.17 / 0.0564 | 25.64 / 0.0774 | 29.78 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.77 / 0.0640 | 24.78 / 0.1030 | 29.59 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.21 / 0.0559 | 25.77 / 0.0722 | 29.78 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.83 / 0.0627 | 25.05 / 0.0928 | 29.60 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.23 / 0.0554 | 25.97 / 0.0670 | 29.79 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.38 / 0.0661 | 23.16 / 0.1261 | 28.99 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.07 / 0.0562 | 25.09 / 0.0782 | 29.71 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.42 / 0.0660 | 23.48 / 0.1168 | 28.97 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.09 / 0.0558 | 25.33 / 0.0730 | 29.72 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.42 / 0.0651 | 23.40 / 0.1117 | 28.97 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.08 / 0.0555 | 25.23 / 0.0715 | 29.71 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.39 / 0.0641 | 23.21 / 0.1079 | 28.93 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.04 / 0.0553 | 25.09 / 0.0691 | 29.70 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.53 / 0.0613 | 20.68 / 0.0132 | 29.79 / 0.0372 | 28.20 / 0.0540 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 11.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.53 | 0.8221 | 0.0613 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 16.46 | 0.5812 | 0.2963 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 17.20 | 0.6821 | 0.2025 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 16.91 | 0.6419 | 0.2577 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 17.01 | 0.6641 | 0.2291 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 16.13 | 0.5483 | 0.2716 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 17.76 | 0.6862 | 0.1873 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 16.86 | 0.6183 | 0.2413 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 17.30 | 0.6534 | 0.2136 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.01 | 0.6874 | 0.2099 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 18.56 | 0.5991 | 0.2722 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 19.58 | 0.7001 | 0.1810 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 19.38 | 0.6611 | 0.2319 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 19.52 | 0.6834 | 0.2045 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 17.84 | 0.5765 | 0.2570 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.76 | 0.7032 | 0.1797 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 18.85 | 0.6441 | 0.2226 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 19.29 | 0.6742 | 0.2002 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.37 | 0.7227 | 0.1836 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 13.96 | 0.5657 | 0.3177 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 14.51 | 0.6704 | 0.2311 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 14.20 | 0.6233 | 0.2812 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 14.32 | 0.6472 | 0.2578 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 13.81 | 0.5594 | 0.2789 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 14.35 | 0.6001 | 0.2330 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 14.13 | 0.5962 | 0.2566 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 14.23 | 0.6003 | 0.2447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.11 | 0.8044 | 0.0857 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.93 | 0.8287 | 0.0664 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.61 | 0.8177 | 0.0762 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.78 | 0.8236 | 0.0710 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.18 | 0.7917 | 0.0916 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.68 | 0.8260 | 0.0666 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.82 | 0.8066 | 0.0821 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.18 | 0.8159 | 0.0739 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.40 | 0.8234 | 0.0776 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.71 | 0.7961 | 0.0990 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.72 | 0.8266 | 0.0725 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.34 | 0.8131 | 0.0873 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.55 | 0.8205 | 0.0796 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.09 | 0.7866 | 0.1004 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.49 | 0.8245 | 0.0743 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.75 | 0.8041 | 0.0907 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.13 | 0.8145 | 0.0820 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.41 | 0.8238 | 0.0817 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.23 | 0.8079 | 0.0859 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.97 | 0.8326 | 0.0670 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.64 | 0.8198 | 0.0774 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.77 | 0.8259 | 0.0722 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.09 | 0.8078 | 0.0782 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.09 | 0.8133 | 0.0691 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.33 | 0.8135 | 0.0730 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.23 | 0.8131 | 0.0715 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.81 | 0.7548 | 0.1291 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.08 | 0.8078 | 0.0869 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.61 | 0.7856 | 0.1095 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.88 | 0.7978 | 0.0976 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.75 | 0.7357 | 0.1300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.90 | 0.8084 | 0.0866 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.70 | 0.7703 | 0.1129 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.23 | 0.7898 | 0.0998 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.57 | 0.7878 | 0.1229 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.03 | 0.7254 | 0.1626 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.54 | 0.7955 | 0.1031 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.00 | 0.7668 | 0.1373 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.32 | 0.7831 | 0.1191 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.40 | 0.7089 | 0.1611 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.36 | 0.7969 | 0.1066 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.42 | 0.7538 | 0.1387 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.88 | 0.7768 | 0.1218 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.65 | 0.7852 | 0.1284 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.01 | 0.7599 | 0.1309 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.05 | 0.8113 | 0.0928 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.55 | 0.7877 | 0.1140 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.78 | 0.7997 | 0.1030 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.16 | 0.7418 | 0.1261 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.21 | 0.7573 | 0.1079 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.48 | 0.7575 | 0.1168 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.40 | 0.7585 | 0.1117 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.68 | 0.7004 | 0.0132 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.73 | 0.3280 | 0.1026 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.89 | 0.3841 | 0.0973 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.79 | 0.3598 | 0.1002 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.84 | 0.3728 | 0.0990 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.67 | 0.3106 | 0.1036 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.81 | 0.3876 | 0.0978 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.74 | 0.3521 | 0.1016 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.77 | 0.3709 | 0.1000 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.10 | 0.3670 | 0.0650 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.23 | 0.3912 | 0.0822 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.51 | 0.4613 | 0.0756 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.36 | 0.4322 | 0.0790 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.43 | 0.4479 | 0.0774 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.20 | 0.3866 | 0.0826 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.37 | 0.4706 | 0.0763 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.28 | 0.4333 | 0.0795 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.32 | 0.4527 | 0.0783 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.29 | 0.4543 | 0.0538 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.92 | 0.2846 | 0.1101 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.15 | 0.3495 | 0.1048 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.99 | 0.3172 | 0.1080 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.05 | 0.3324 | 0.1067 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.85 | 0.2847 | 0.1102 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.05 | 0.3184 | 0.1058 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.90 | 0.3043 | 0.1086 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.95 | 0.3111 | 0.1076 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.44 | 0.6900 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.86 | 0.7182 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.70 | 0.7066 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.81 | 0.7133 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.98 | 0.6791 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.90 | 0.7293 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.42 | 0.7046 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.55 | 0.7172 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.62 | 0.7064 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 20.01 | 0.6705 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.49 | 0.7057 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.36 | 0.6925 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.47 | 0.7005 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.62 | 0.6683 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.54 | 0.7245 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.09 | 0.6979 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.28 | 0.7122 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.43 | 0.6990 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.47 | 0.6869 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.95 | 0.7184 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.80 | 0.7044 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.89 | 0.7115 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.72 | 0.6971 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.64 | 0.7049 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.74 | 0.7030 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.72 | 0.7036 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.42 | 0.6872 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.86 | 0.7170 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.69 | 0.7048 | 0.0152 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.81 | 0.7120 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.97 | 0.6765 | 0.0172 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.88 | 0.7283 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.40 | 0.7029 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.54 | 0.7160 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.62 | 0.7035 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.98 | 0.6664 | 0.0183 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.47 | 0.7037 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.34 | 0.6896 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.45 | 0.6980 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.60 | 0.6650 | 0.0193 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.51 | 0.7222 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.07 | 0.6951 | 0.0176 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.26 | 0.7096 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.43 | 0.6953 | 0.0181 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.46 | 0.6841 | 0.0148 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.94 | 0.7172 | 0.0135 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.79 | 0.7022 | 0.0141 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.88 | 0.7098 | 0.0138 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.69 | 0.6938 | 0.0143 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.64 | 0.7030 | 0.0136 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.72 | 0.7003 | 0.0137 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.71 | 0.7013 | 0.0135 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 27.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.10 | 0.7801 | 0.0202 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.15 | 0.4645 | 0.2219 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.35 | 0.4976 | 0.2099 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.21 | 0.4870 | 0.2167 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.26 | 0.4927 | 0.2136 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.12 | 0.4598 | 0.2198 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.31 | 0.5072 | 0.2078 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.17 | 0.4913 | 0.2146 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.22 | 0.5007 | 0.2115 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.44 | 0.3282 | 0.1746 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.64 | 0.5132 | 0.1941 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.93 | 0.5511 | 0.1788 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.74 | 0.5408 | 0.1876 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.81 | 0.5468 | 0.1837 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.68 | 0.5205 | 0.1892 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.96 | 0.5683 | 0.1741 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.76 | 0.5521 | 0.1829 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.83 | 0.5609 | 0.1791 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.58 | 0.3959 | 0.1587 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.90 | 0.4551 | 0.2233 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.14 | 0.4883 | 0.2123 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.95 | 0.4768 | 0.2189 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.02 | 0.4823 | 0.2160 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.83 | 0.4608 | 0.2196 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.08 | 0.4775 | 0.2096 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.87 | 0.4782 | 0.2155 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.94 | 0.4786 | 0.2130 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.57 | 0.7696 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.01 | 0.7815 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.84 | 0.7767 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.94 | 0.7795 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.33 | 0.7677 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.15 | 0.7867 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.73 | 0.7776 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.86 | 0.7819 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.36 | 0.7665 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.28 | 0.7638 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.71 | 0.7772 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.61 | 0.7727 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.68 | 0.7754 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.00 | 0.7643 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.91 | 0.7858 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.49 | 0.7761 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.66 | 0.7811 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.04 | 0.7609 | 0.0278 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.69 | 0.7711 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.14 | 0.7831 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.02 | 0.7782 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.08 | 0.7805 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.10 | 0.7782 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.00 | 0.7806 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.14 | 0.7812 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.12 | 0.7817 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.24 | 0.7443 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.92 | 0.7644 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.83 | 0.7590 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.95 | 0.7632 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.01 | 0.7420 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.85 | 0.7730 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.62 | 0.7618 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.73 | 0.7683 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.62 | 0.7161 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.41 | 0.7204 | 0.0411 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.07 | 0.7460 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.11 | 0.7413 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.17 | 0.7450 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.30 | 0.7243 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.14 | 0.7612 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.03 | 0.7487 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.10 | 0.7556 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.81 | 0.6812 | 0.0548 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.46 | 0.7436 | 0.0349 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.87 | 0.7640 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.88 | 0.7583 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.95 | 0.7620 | 0.0318 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.87 | 0.7556 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.64 | 0.7597 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.00 | 0.7643 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.98 | 0.7644 | 0.0301 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 40.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.83 | 0.7456 | 0.0288 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.84 | 0.3712 | 0.3652 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.89 | 0.3953 | 0.3541 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.86 | 0.3871 | 0.3607 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.87 | 0.3912 | 0.3579 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.84 | 0.3693 | 0.3636 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.88 | 0.3990 | 0.3534 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.85 | 0.3884 | 0.3597 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.86 | 0.3945 | 0.3569 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.91 | 0.2699 | 0.2340 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.90 | 0.4291 | 0.3336 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.97 | 0.4579 | 0.3192 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.93 | 0.4499 | 0.3276 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.95 | 0.4545 | 0.3238 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.93 | 0.4368 | 0.3299 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.00 | 0.4686 | 0.3156 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.95 | 0.4583 | 0.3246 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.97 | 0.4643 | 0.3208 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.16 | 0.3635 | 0.2106 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.69 | 0.3574 | 0.3725 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.80 | 0.3823 | 0.3632 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.72 | 0.3728 | 0.3689 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.75 | 0.3774 | 0.3664 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.67 | 0.3675 | 0.3675 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.73 | 0.3771 | 0.3604 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.68 | 0.3754 | 0.3652 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.70 | 0.3764 | 0.3631 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.49 | 0.7396 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.76 | 0.7455 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.69 | 0.7431 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.75 | 0.7444 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.17 | 0.7384 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.84 | 0.7482 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.48 | 0.7433 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.56 | 0.7457 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.56 | 0.7434 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.27 | 0.7365 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.58 | 0.7437 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.53 | 0.7412 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.58 | 0.7427 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.95 | 0.7363 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.67 | 0.7477 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.34 | 0.7427 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.48 | 0.7453 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.35 | 0.7413 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.63 | 0.7413 | 0.0314 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.99 | 0.7478 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.90 | 0.7450 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.95 | 0.7465 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.90 | 0.7451 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.84 | 0.7465 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.91 | 0.7464 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.92 | 0.7467 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.60 | 0.7250 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.16 | 0.7375 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.09 | 0.7334 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.17 | 0.7359 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.30 | 0.7246 | 0.0393 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.29 | 0.7430 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.82 | 0.7351 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.98 | 0.7393 | 0.0358 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.58 | 0.7308 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.85 | 0.7116 | 0.0473 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.61 | 0.7295 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.54 | 0.7245 | 0.0437 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.61 | 0.7277 | 0.0421 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.69 | 0.7132 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.74 | 0.7378 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.38 | 0.7285 | 0.0429 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.55 | 0.7339 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.53 | 0.7151 | 0.0438 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.83 | 0.7287 | 0.0391 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.36 | 0.7420 | 0.0355 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.17 | 0.7368 | 0.0375 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.26 | 0.7396 | 0.0365 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.27 | 0.7360 | 0.0362 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.28 | 0.7398 | 0.0348 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.31 | 0.7394 | 0.0360 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.34 | 0.7401 | 0.0351 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.79 | 0.7321 | 0.0372 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.81 | 0.3201 | 0.3941 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.87 | 0.3309 | 0.3854 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.83 | 0.3278 | 0.3906 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.85 | 0.3297 | 0.3881 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.79 | 0.3156 | 0.3917 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.81 | 0.3279 | 0.3843 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.79 | 0.3241 | 0.3886 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.80 | 0.3266 | 0.3864 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.51 | 0.1735 | 0.2923 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.45 | 0.3655 | 0.3608 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.50 | 0.3778 | 0.3478 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.47 | 0.3759 | 0.3551 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.48 | 0.3774 | 0.3513 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.47 | 0.3652 | 0.3561 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.50 | 0.3771 | 0.3449 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.48 | 0.3754 | 0.3516 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.49 | 0.3767 | 0.3483 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.33 | 0.2519 | 0.2642 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.64 | 0.3026 | 0.4016 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.71 | 0.3139 | 0.3936 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.66 | 0.3093 | 0.3985 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.68 | 0.3115 | 0.3963 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.62 | 0.3034 | 0.3990 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.64 | 0.3060 | 0.3936 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.63 | 0.3075 | 0.3969 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.63 | 0.3072 | 0.3953 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.76 | 0.7316 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.78 | 0.7320 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.77 | 0.7318 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.78 | 0.7319 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.73 | 0.7314 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.78 | 0.7320 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.76 | 0.7317 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.77 | 0.7318 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.75 | 0.7318 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.70 | 0.7309 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.75 | 0.7317 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.74 | 0.7314 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.75 | 0.7316 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.68 | 0.7307 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.75 | 0.7316 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.72 | 0.7312 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.74 | 0.7314 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.73 | 0.7318 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.77 | 0.7317 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.79 | 0.7320 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.78 | 0.7319 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.78 | 0.7320 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.71 | 0.7312 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.70 | 0.7312 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.72 | 0.7313 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.71 | 0.7313 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.41 | 0.7279 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.60 | 0.7307 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.56 | 0.7299 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.59 | 0.7305 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.33 | 0.7271 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.60 | 0.7308 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.50 | 0.7293 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.57 | 0.7303 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.28 | 0.7287 | 0.0428 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.01 | 0.7243 | 0.0445 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.39 | 0.7291 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.30 | 0.7278 | 0.0430 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.36 | 0.7287 | 0.0425 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.93 | 0.7234 | 0.0442 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.33 | 0.7289 | 0.0419 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.19 | 0.7269 | 0.0429 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.27 | 0.7282 | 0.0425 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.04 | 0.7273 | 0.0449 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.51 | 0.7288 | 0.0406 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.60 | 0.7310 | 0.0394 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.58 | 0.7302 | 0.0400 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.59 | 0.7307 | 0.0397 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.99 | 0.7253 | 0.0432 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.93 | 0.7252 | 0.0439 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.97 | 0.7261 | 0.0435 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.97 | 0.7259 | 0.0436 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.20 | 0.7401 | 0.0540 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.30 | 0.3355 | 0.4634 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.37 | 0.3539 | 0.4460 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.33 | 0.3474 | 0.4565 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.35 | 0.3510 | 0.4516 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.28 | 0.3307 | 0.4573 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.31 | 0.3531 | 0.4407 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.29 | 0.3450 | 0.4514 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.30 | 0.3497 | 0.4463 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.66 | 0.2143 | 0.3776 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.04 | 0.3840 | 0.4269 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.10 | 0.4056 | 0.4028 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.06 | 0.3994 | 0.4170 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.08 | 0.4031 | 0.4102 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.05 | 0.3847 | 0.4180 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.10 | 0.4070 | 0.3962 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.07 | 0.4004 | 0.4100 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.08 | 0.4042 | 0.4037 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.56 | 0.2927 | 0.3363 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.11 | 0.3167 | 0.4720 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.18 | 0.3352 | 0.4572 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.13 | 0.3275 | 0.4660 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.15 | 0.3312 | 0.4619 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.08 | 0.3189 | 0.4612 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.11 | 0.3254 | 0.4517 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.09 | 0.3253 | 0.4578 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.10 | 0.3256 | 0.4549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.98 | 0.7370 | 0.0595 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.20 | 0.7404 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.12 | 0.7390 | 0.0582 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.18 | 0.7398 | 0.0574 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.74 | 0.7358 | 0.0600 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.19 | 0.7414 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.96 | 0.7387 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.03 | 0.7400 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.02 | 0.7392 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.75 | 0.7345 | 0.0621 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.02 | 0.7389 | 0.0581 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.95 | 0.7373 | 0.0603 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.01 | 0.7383 | 0.0593 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.51 | 0.7336 | 0.0625 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.00 | 0.7400 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.77 | 0.7371 | 0.0608 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.87 | 0.7387 | 0.0596 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.86 | 0.7380 | 0.0593 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.03 | 0.7375 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.23 | 0.7408 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.17 | 0.7394 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.21 | 0.7401 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.07 | 0.7381 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.04 | 0.7389 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.09 | 0.7389 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.08 | 0.7389 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.39 | 0.7283 | 0.0687 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.83 | 0.7360 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.73 | 0.7334 | 0.0656 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.81 | 0.7350 | 0.0641 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.10 | 0.7269 | 0.0678 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.83 | 0.7382 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.49 | 0.7333 | 0.0652 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.62 | 0.7360 | 0.0633 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.30 | 0.7320 | 0.0661 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.74 | 0.7194 | 0.0791 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.36 | 0.7307 | 0.0692 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.24 | 0.7272 | 0.0743 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.33 | 0.7294 | 0.0717 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.56 | 0.7188 | 0.0768 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.32 | 0.7333 | 0.0681 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.05 | 0.7275 | 0.0731 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.19 | 0.7309 | 0.0707 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.63 | 0.7244 | 0.0710 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.50 | 0.7298 | 0.0676 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.83 | 0.7372 | 0.0627 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.71 | 0.7343 | 0.0654 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.77 | 0.7358 | 0.0640 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.38 | 0.7296 | 0.0661 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.39 | 0.7314 | 0.0641 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.42 | 0.7316 | 0.0660 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.42 | 0.7318 | 0.0651 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 295984 | 0.167 | 32.8 | 29.68 | 0.25 | 0.032 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 295984 | 0.167 | 33.1 | 29.68 | 0.25 | 0.032 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 295984 | 0.167 | 35.2 | 29.68 | 0.25 | 0.032 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 295984 | 0.167 | 32.6 | 29.68 | 0.25 | 0.032 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 956 | None | classic | 1.37 | False | 410737 | 0.348 | 58.0 | 28.18 | 0.20 | 0.037 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 956 | None | classic | 1.37 | False | 410737 | 0.348 | 61.5 | 28.18 | 0.20 | 0.037 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 956 | None | classic | 1.37 | False | 410737 | 0.348 | 56.2 | 28.18 | 0.20 | 0.037 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 956 | None | classic | 1.37 | False | 410737 | 0.348 | 60.1 | 28.18 | 0.20 | 0.037 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1316025 | 0.804 | 159.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 295984 | 0.170 | 33.0 | 29.68 | 0.25 | 0.032 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 295984 | 0.170 | 44.1 | 29.68 | 0.25 | 0.032 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 295984 | 0.170 | 36.2 | 29.68 | 0.25 | 0.032 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 295984 | 0.170 | 36.4 | 29.68 | 0.25 | 0.032 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1131 | None | classic | 1.91 | False | 429393 | 0.354 | 63.0 | 28.64 | 0.07 | 0.029 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1131 | None | classic | 1.91 | False | 429393 | 0.354 | 64.6 | 28.64 | 0.07 | 0.029 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1131 | None | classic | 1.91 | False | 429393 | 0.354 | 72.5 | 28.64 | 0.07 | 0.029 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1131 | None | classic | 1.91 | False | 429393 | 0.354 | 63.5 | 28.64 | 0.07 | 0.029 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1777169 | 0.804 | 74.0 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 298057 | 0.325 | 43.2 | 30.45 | 0.24 | 0.023 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 298057 | 0.325 | 30.2 | 30.45 | 0.24 | 0.023 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 298057 | 0.325 | 29.7 | 30.45 | 0.24 | 0.023 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 298057 | 0.325 | 32.2 | 30.45 | 0.24 | 0.023 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 743 | None | classic | 0.71 | False | 458188 | 0.514 | 78.8 | 28.10 | 0.21 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 743 | None | classic | 0.71 | False | 458188 | 0.514 | 79.6 | 28.10 | 0.21 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 743 | None | classic | 0.71 | False | 458188 | 0.514 | 82.1 | 28.10 | 0.21 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 743 | None | classic | 0.71 | False | 458188 | 0.514 | 79.5 | 28.10 | 0.21 | 0.007 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.613 | 0.017 |
| in035 | mask_ent | 0.726 | 0.017 |
| in035 | mask_grad | 0.439 | 0.017 |
| in035 | r_col | 0.795 | 0.017 |
| in035 | r_warp | 0.836 | 0.017 |

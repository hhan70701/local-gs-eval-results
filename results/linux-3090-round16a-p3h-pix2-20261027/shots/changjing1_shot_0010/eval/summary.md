# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 7.7% | 24.80 / 0.0081 | 19.60 / 0.0287 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.0% | 24.91 / 0.0084 | 19.89 / 0.0256 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.8% | 24.82 / 0.0081 | 19.93 / 0.0261 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.9% | 24.86 / 0.0082 | 19.81 / 0.0249 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.6% | 24.84 / 0.0080 | 19.96 / 0.0262 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.9% | 25.01 / 0.0082 | 20.48 / 0.0225 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.7% | 24.92 / 0.0082 | 20.41 / 0.0233 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.7% | 24.94 / 0.0082 | 20.35 / 0.0221 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 6.9% | 24.38 / 0.0081 | 22.97 / 0.0219 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 6.6% | 24.49 / 0.0080 | 21.61 / 0.0253 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.1% | 20.81 / 0.0042 | 17.99 / 0.0148 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 6.7% | 24.42 / 0.0079 | 21.00 / 0.0283 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.1% | 20.74 / 0.0039 | 17.79 / 0.0140 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 6.9% | 24.49 / 0.0080 | 22.69 / 0.0157 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 6.5% | 24.52 / 0.0079 | 21.10 / 0.0242 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.4% | 21.51 / 0.0043 | 17.69 / 0.0162 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 6.4% | 24.57 / 0.0080 | 20.98 / 0.0283 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.2% | 21.34 / 0.0044 | 17.82 / 0.0168 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 8.1% | 25.25 / 0.0085 | 19.31 / 0.0393 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 12.1% | 26.21 / 0.0091 | 19.48 / 0.0370 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.8% | 26.34 / 0.0094 | 20.17 / 0.0315 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.4% | 26.28 / 0.0092 | 20.03 / 0.0343 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.5% | 26.30 / 0.0094 | 20.12 / 0.0329 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 12.1% | 26.22 / 0.0092 | 19.48 / 0.0371 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 12.7% | 26.33 / 0.0094 | 20.17 / 0.0313 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 12.3% | 26.28 / 0.0093 | 20.07 / 0.0339 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 12.5% | 26.30 / 0.0094 | 20.11 / 0.0325 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 12.0% | 26.36 / 0.0099 | 19.48 / 0.0451 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 6.2% | 25.50 / 0.0057 | 20.24 / 0.0204 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 7.3% | 25.96 / 0.0060 | 20.77 / 0.0240 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 6.5% | 25.63 / 0.0057 | 20.90 / 0.0193 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 6.7% | 25.72 / 0.0058 | 20.89 / 0.0207 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 6.5% | 25.64 / 0.0058 | 22.44 / 0.0167 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 7.3% | 26.00 / 0.0061 | 21.70 / 0.0191 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 6.5% | 25.65 / 0.0058 | 22.48 / 0.0170 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 6.7% | 25.71 / 0.0058 | 22.26 / 0.0179 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.23 / 0.0449 | 27.13 / 0.0600 | 20.25 / 0.0094 | 29.72 / 0.0305 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.78 / 0.0569 | 23.95 / 0.1227 | 18.99 / 0.0129 | 29.41 / 0.0333 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.84 / 0.0548 | 24.13 / 0.1201 | 18.85 / 0.0123 | 29.45 / 0.0328 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.93 / 0.0558 | 24.31 / 0.1192 | 18.97 / 0.0125 | 29.51 / 0.0330 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.88 / 0.0549 | 24.24 / 0.1182 | 18.85 / 0.0124 | 29.49 / 0.0328 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.03 / 0.0553 | 24.82 / 0.1136 | 19.10 / 0.0121 | 29.58 / 0.0325 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.22 / 0.0523 | 24.85 / 0.1058 | 19.16 / 0.0108 | 29.57 / 0.0323 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.24 / 0.0538 | 25.08 / 0.1105 | 19.23 / 0.0113 | 29.61 / 0.0323 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.20 / 0.0529 | 24.91 / 0.1088 | 19.17 / 0.0109 | 29.60 / 0.0323 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.15 / 0.0502 | 25.52 / 0.1368 | 20.42 / 0.0122 | 29.74 / 0.0306 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.82 / 0.0509 | 26.64 / 0.1015 | 20.26 / 0.0124 | 29.73 / 0.0307 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.86 / 0.0486 | 26.86 / 0.0831 | 20.25 / 0.0118 | 29.72 / 0.0305 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.70 / 0.0517 | 26.42 / 0.1026 | 20.18 / 0.0130 | 29.73 / 0.0307 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.79 / 0.0484 | 26.79 / 0.0765 | 20.22 / 0.0121 | 29.72 / 0.0305 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.12 / 0.0481 | 25.70 / 0.0997 | 20.37 / 0.0109 | 29.73 / 0.0307 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.76 / 0.0506 | 26.37 / 0.0999 | 20.11 / 0.0120 | 29.72 / 0.0308 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.82 / 0.0482 | 26.66 / 0.0800 | 20.11 / 0.0115 | 29.71 / 0.0306 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.68 / 0.0510 | 26.23 / 0.1048 | 20.14 / 0.0124 | 29.73 / 0.0308 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.78 / 0.0480 | 26.67 / 0.0806 | 20.17 / 0.0115 | 29.72 / 0.0305 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.40 / 0.0523 | 23.94 / 0.1087 | 19.55 / 0.0133 | 29.69 / 0.0311 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.05 / 0.0640 | 23.39 / 0.1411 | 18.66 / 0.0146 | 29.09 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.34 / 0.0600 | 23.49 / 0.1340 | 18.92 / 0.0136 | 29.26 / 0.0342 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.33 / 0.0625 | 23.88 / 0.1353 | 18.81 / 0.0139 | 29.26 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.34 / 0.0612 | 23.65 / 0.1347 | 18.85 / 0.0136 | 29.28 / 0.0345 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.07 / 0.0639 | 23.59 / 0.1399 | 18.73 / 0.0145 | 29.10 / 0.0354 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.35 / 0.0599 | 23.63 / 0.1339 | 18.98 / 0.0135 | 29.26 / 0.0341 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.37 / 0.0621 | 24.01 / 0.1331 | 18.89 / 0.0138 | 29.29 / 0.0346 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.37 / 0.0609 | 23.79 / 0.1315 | 18.92 / 0.0135 | 29.30 / 0.0343 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.78 / 0.0554 | 23.83 / 0.1174 | 18.86 / 0.0147 | 29.52 / 0.0319 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.35 / 0.0558 | 24.66 / 0.1400 | 19.62 / 0.0115 | 29.61 / 0.0325 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.60 / 0.0534 | 25.06 / 0.1271 | 19.85 / 0.0105 | 29.63 / 0.0319 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.56 / 0.0549 | 25.03 / 0.1355 | 19.73 / 0.0108 | 29.65 / 0.0321 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.58 / 0.0541 | 25.03 / 0.1274 | 19.79 / 0.0107 | 29.65 / 0.0320 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.89 / 0.0501 | 25.31 / 0.0927 | 20.33 / 0.0101 | 29.69 / 0.0314 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.98 / 0.0491 | 25.46 / 0.0812 | 20.51 / 0.0096 | 29.67 / 0.0315 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.93 / 0.0499 | 25.51 / 0.0843 | 20.40 / 0.0097 | 29.70 / 0.0313 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.96 / 0.0493 | 25.50 / 0.0811 | 20.46 / 0.0097 | 29.69 / 0.0314 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.2%） | — | — | 28.23 / 0.0449 | 27.13 / 0.0600 | 29.72 |
| in035 | rife | 3.3% | 6.2% | 27.35 / 0.0558 | 24.66 / 0.1400 | 29.61 |
| in035 | cnw_cnn | 4.4% | 7.7% | 26.78 / 0.0569 | 23.95 / 0.1227 | 29.41 |
| in035 | cnw_f5 | 6.6% | 12.1% | 26.05 / 0.0640 | 23.39 / 0.1411 | 29.09 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.83 / 0.0439 | -1.09 / +0.0149 (core 4.0%) | -1.73 / +0.0146 (core 4.3%) | -2.22 / +0.0229 (core 7.6%) |
| in035 | 2 | 0-3 | 28.26 / 0.0426 | -1.24 / +0.0152 (core 4.0%) | -1.84 / +0.0135 (core 4.3%) | -2.70 / +0.0244 (core 7.6%) |
| in035 | 4 | 3-5 | 28.59 / 0.0483 | -0.29 / +0.0025 (core 1.1%) | -0.78 / +0.0078 (core 2.7%) | -1.63 / +0.0097 (core 3.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.23 / 0.0449 | 27.13 | 29.72 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.78 / 0.0569 | 23.95 | 29.41 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 27.56 / 0.0494 | 25.22 | 29.72 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.84 / 0.0548 | 24.13 | 29.45 | 0/3 |
| in035 | cnw_cnn | oracle | 1.4% | 27.55 / 0.0483 | 25.38 | 29.71 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.93 / 0.0558 | 24.31 | 29.51 | 0/3 |
| in035 | cnw_cnn | oracle | 1.4% | 27.60 / 0.0490 | 25.46 | 29.72 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.88 / 0.0549 | 24.24 | 29.49 | 0/3 |
| in035 | cnw_cnn | oracle | 1.4% | 27.56 / 0.0485 | 25.46 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.03 / 0.0553 | 24.82 | 29.58 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 27.66 / 0.0483 | 25.70 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.22 / 0.0523 | 24.85 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.4% | 27.76 / 0.0469 | 25.72 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.24 / 0.0538 | 25.08 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 27.76 / 0.0476 | 25.84 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.20 / 0.0529 | 24.91 | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 27.74 / 0.0473 | 25.74 | 29.72 | 0/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 28.15 / 0.0502 | 25.52 | 29.74 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 1.4% | 28.23 / 0.0480 | 25.94 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 27.82 / 0.0509 | 26.64 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 1.2% | 28.10 / 0.0476 | 27.07 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 27.86 / 0.0486 | 26.86 | 29.72 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 0.8% | 28.10 / 0.0469 | 27.10 | 29.72 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.70 / 0.0517 | 26.42 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 1.3% | 28.04 / 0.0480 | 26.92 | 29.73 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.79 / 0.0484 | 26.79 | 29.72 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 0.8% | 28.07 / 0.0470 | 27.04 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 28.12 / 0.0481 | 25.70 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 1.3% | 28.22 / 0.0465 | 26.13 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.76 / 0.0506 | 26.37 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.2% | 28.07 / 0.0470 | 26.89 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.82 / 0.0482 | 26.66 | 29.71 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.9% | 28.07 / 0.0466 | 26.93 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.68 / 0.0510 | 26.23 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 1.2% | 28.05 / 0.0475 | 26.81 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.78 / 0.0480 | 26.67 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 0.8% | 28.07 / 0.0466 | 26.94 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.40 / 0.0523 | 23.94 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.3% | 27.83 / 0.0483 | 25.16 | 29.72 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.05 / 0.0640 | 23.39 | 29.09 | 0/3 |
| in035 | cnw_f5 | oracle | 1.8% | 27.38 / 0.0511 | 25.05 | 29.70 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.34 / 0.0600 | 23.49 | 29.26 | 0/3 |
| in035 | cnw_f5 | oracle | 1.9% | 27.53 / 0.0498 | 24.98 | 29.70 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.33 / 0.0625 | 23.88 | 29.26 | 0/3 |
| in035 | cnw_f5 | oracle | 1.8% | 27.49 / 0.0505 | 25.21 | 29.70 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.34 / 0.0612 | 23.65 | 29.28 | 0/3 |
| in035 | cnw_f5 | oracle | 1.8% | 27.51 / 0.0500 | 25.07 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.07 / 0.0639 | 23.59 | 29.10 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.8% | 27.39 / 0.0511 | 25.17 | 29.69 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.35 / 0.0599 | 23.63 | 29.26 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.9% | 27.55 / 0.0497 | 25.10 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.37 / 0.0621 | 24.01 | 29.29 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.8% | 27.52 / 0.0504 | 25.29 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.37 / 0.0609 | 23.79 | 29.30 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.8% | 27.53 / 0.0499 | 25.14 | 29.70 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.78 / 0.0554 | 23.83 | 29.52 | 0/3 |
| in035 | cnw_f5_pix | oracle | 1.8% | 27.50 / 0.0495 | 25.14 | 29.72 | 0/3 |
| in035 | rife | 不复核 | —% | 27.35 / 0.0558 | 24.66 | 29.61 | 0/3 |
| in035 | rife | oracle | 1.0% | 27.89 / 0.0475 | 25.78 | 29.72 | 0/3 |
| in035 | rife | 不复核 | —% | 27.60 / 0.0534 | 25.06 | 29.63 | 0/3 |
| in035 | rife | oracle | 1.0% | 28.00 / 0.0466 | 25.88 | 29.72 | 0/3 |
| in035 | rife | 不复核 | —% | 27.56 / 0.0549 | 25.03 | 29.65 | 0/3 |
| in035 | rife | oracle | 1.0% | 27.95 / 0.0471 | 25.80 | 29.72 | 0/3 |
| in035 | rife | 不复核 | —% | 27.58 / 0.0541 | 25.03 | 29.65 | 0/3 |
| in035 | rife | oracle | 1.0% | 27.98 / 0.0468 | 25.81 | 29.72 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.89 / 0.0501 | 25.31 | 29.69 | 0/3 |
| in035 | rife_mw | oracle | 1.0% | 28.18 / 0.0454 | 26.20 | 29.72 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.98 / 0.0491 | 25.46 | 29.67 | 0/3 |
| in035 | rife_mw | oracle | 1.0% | 28.25 / 0.0451 | 26.19 | 29.72 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.93 / 0.0499 | 25.51 | 29.70 | 0/3 |
| in035 | rife_mw | oracle | 1.0% | 28.21 / 0.0452 | 26.20 | 29.72 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.96 / 0.0493 | 25.50 | 29.69 | 0/3 |
| in035 | rife_mw | oracle | 1.0% | 28.23 / 0.0452 | 26.18 | 29.72 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.23 / 0.0449 | 27.13 / 0.0600 | — |
| in035 | FF | 0（前馈） | 1008×630（59%） | 25.73 | 26.78 / 0.0569 | 23.95 / 0.1227 | 0/3 |
| in035 | 25 | 1.29 s | 1008×630（59%） | 26.39 | 26.93 / 0.0558 | 24.31 / 0.1192 | 0/3 |
| in035 | 50 | 2.58 s | 1008×630（59%） | 26.74 | 26.88 / 0.0549 | 24.24 / 0.1182 | 0/3 |
| in035 | 100 | 5.13 s | 1008×630（59%） | 27.07 | 26.84 / 0.0548 | 24.13 / 0.1201 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.23 / 0.0449 | 27.13 / 0.0600 | 29.72 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.78 / 0.0569 | 23.95 / 0.1227 | 29.41 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.56 / 0.0494 | 25.22 / 0.0858 | 29.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 26.93 / 0.0558 | 24.31 / 0.1192 | 29.51 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.60 / 0.0490 | 25.46 / 0.0832 | 29.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 26.88 / 0.0549 | 24.24 / 0.1182 | 29.49 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.56 / 0.0485 | 25.46 / 0.0816 | 29.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 26.84 / 0.0548 | 24.13 / 0.1201 | 29.45 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.55 / 0.0483 | 25.38 / 0.0822 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.03 / 0.0553 | 24.82 / 0.1136 | 29.58 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.66 / 0.0483 | 25.70 / 0.0844 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.24 / 0.0538 | 25.08 / 0.1105 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.76 / 0.0476 | 25.84 / 0.0819 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.20 / 0.0529 | 24.91 / 0.1088 | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.74 / 0.0473 | 25.74 / 0.0811 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.22 / 0.0523 | 24.85 / 0.1058 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.76 / 0.0469 | 25.72 / 0.0799 | 29.73 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.05 / 0.0640 | 23.39 / 0.1411 | 29.09 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.38 / 0.0511 | 25.05 / 0.0925 | 29.70 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.33 / 0.0625 | 23.88 / 0.1353 | 29.26 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.49 / 0.0505 | 25.21 / 0.0889 | 29.70 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.34 / 0.0612 | 23.65 / 0.1347 | 29.28 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.51 / 0.0500 | 25.07 / 0.0892 | 29.70 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.34 / 0.0600 | 23.49 / 0.1340 | 29.26 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.53 / 0.0498 | 24.98 / 0.0869 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.07 / 0.0639 | 23.59 / 0.1399 | 29.10 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.39 / 0.0511 | 25.17 / 0.0927 | 29.69 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.37 / 0.0621 | 24.01 / 0.1331 | 29.29 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.52 / 0.0504 | 25.29 / 0.0889 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.37 / 0.0609 | 23.79 / 0.1315 | 29.30 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.53 / 0.0499 | 25.14 / 0.0883 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 26.35 / 0.0599 | 23.63 / 0.1339 | 29.26 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.55 / 0.0497 | 25.10 / 0.0878 | 29.70 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.35 / 0.0558 | 24.66 / 0.1400 | 29.61 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.89 / 0.0475 | 25.78 / 0.0852 | 29.72 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.56 / 0.0549 | 25.03 / 0.1355 | 29.65 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.95 / 0.0471 | 25.80 / 0.0843 | 29.72 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.58 / 0.0541 | 25.03 / 0.1274 | 29.65 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.98 / 0.0468 | 25.81 / 0.0824 | 29.72 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.60 / 0.0534 | 25.06 / 0.1271 | 29.63 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.00 / 0.0466 | 25.88 / 0.0823 | 29.72 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.89 / 0.0501 | 25.31 / 0.0927 | 29.69 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.18 / 0.0454 | 26.20 / 0.0721 | 29.72 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.93 / 0.0499 | 25.51 / 0.0843 | 29.70 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.21 / 0.0452 | 26.20 / 0.0671 | 29.72 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.96 / 0.0493 | 25.50 / 0.0811 | 29.69 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.23 / 0.0452 | 26.18 / 0.0666 | 29.72 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.98 / 0.0491 | 25.46 / 0.0812 | 29.67 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.25 / 0.0451 | 26.19 / 0.0667 | 29.72 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.13 / 0.0600 | 20.25 / 0.0094 | 29.72 / 0.0305 | 28.23 / 0.0449 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 8.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.13 | 0.7311 | 0.0600 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 9.86 | 0.5378 | 0.4073 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 10.22 | 0.5312 | 0.3934 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 10.03 | 0.5506 | 0.4027 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 10.11 | 0.5430 | 0.3985 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.94 | 0.5712 | 0.3991 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.23 | 0.5580 | 0.3725 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.07 | 0.5800 | 0.3921 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.11 | 0.5694 | 0.3842 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 24.28 | 0.6977 | 0.2377 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 24.27 | 0.7091 | 0.2227 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 24.27 | 0.7091 | 0.2227 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 24.23 | 0.7034 | 0.2231 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 24.23 | 0.7034 | 0.2231 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 19.79 | 0.5966 | 0.2657 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 20.24 | 0.6075 | 0.2739 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.24 | 0.6075 | 0.2739 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 20.11 | 0.6027 | 0.2778 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 20.11 | 0.6027 | 0.2778 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 19.09 | 0.5666 | 0.2810 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 14.55 | 0.5995 | 0.3308 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 15.85 | 0.5908 | 0.3073 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 15.07 | 0.6164 | 0.3188 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 15.34 | 0.6044 | 0.3153 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 14.63 | 0.6052 | 0.3289 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 15.79 | 0.5984 | 0.3045 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 15.12 | 0.6226 | 0.3157 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 15.40 | 0.6123 | 0.3108 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 21.92 | 0.6374 | 0.2206 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 16.91 | 0.6080 | 0.3014 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 17.13 | 0.6109 | 0.2672 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 17.12 | 0.6240 | 0.2876 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 17.04 | 0.6187 | 0.2747 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 15.98 | 0.6069 | 0.2303 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 16.88 | 0.5900 | 0.2136 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 16.34 | 0.6108 | 0.2206 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 16.51 | 0.6015 | 0.2159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.22 | 0.7076 | 0.0858 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.38 | 0.7071 | 0.0822 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.46 | 0.7103 | 0.0832 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.46 | 0.7092 | 0.0816 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.70 | 0.7139 | 0.0844 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.72 | 0.7137 | 0.0799 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.84 | 0.7167 | 0.0819 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.74 | 0.7152 | 0.0811 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.94 | 0.7140 | 0.1108 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.07 | 0.7290 | 0.0831 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.10 | 0.7289 | 0.0762 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.92 | 0.7256 | 0.0816 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.04 | 0.7278 | 0.0716 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.13 | 0.7171 | 0.0871 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.89 | 0.7274 | 0.0802 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.93 | 0.7282 | 0.0737 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.81 | 0.7252 | 0.0831 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.94 | 0.7283 | 0.0727 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.16 | 0.7131 | 0.0841 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.05 | 0.7021 | 0.0925 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.98 | 0.7016 | 0.0869 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.21 | 0.7062 | 0.0889 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.07 | 0.7036 | 0.0892 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.17 | 0.7038 | 0.0927 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.10 | 0.7040 | 0.0878 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.29 | 0.7069 | 0.0889 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.14 | 0.7049 | 0.0883 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.14 | 0.7127 | 0.0851 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.78 | 0.7127 | 0.0852 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.88 | 0.7150 | 0.0823 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.80 | 0.7153 | 0.0843 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.81 | 0.7151 | 0.0824 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.20 | 0.7201 | 0.0721 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.19 | 0.7204 | 0.0667 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.20 | 0.7215 | 0.0671 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.18 | 0.7208 | 0.0666 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.95 | 0.6727 | 0.1227 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.13 | 0.6668 | 0.1201 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.31 | 0.6767 | 0.1192 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.24 | 0.6730 | 0.1182 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.82 | 0.6922 | 0.1136 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.85 | 0.6885 | 0.1058 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.08 | 0.6974 | 0.1105 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.91 | 0.6923 | 0.1088 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.52 | 0.6987 | 0.1368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.64 | 0.7190 | 0.1015 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.86 | 0.7239 | 0.0831 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.42 | 0.7136 | 0.1026 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.79 | 0.7224 | 0.0765 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.70 | 0.7067 | 0.0997 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.37 | 0.7168 | 0.0999 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.66 | 0.7230 | 0.0800 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.23 | 0.7131 | 0.1048 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.67 | 0.7220 | 0.0806 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.94 | 0.6940 | 0.1087 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.39 | 0.6549 | 0.1411 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.49 | 0.6551 | 0.1340 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.88 | 0.6690 | 0.1353 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.65 | 0.6618 | 0.1347 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.59 | 0.6591 | 0.1399 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.63 | 0.6601 | 0.1339 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.01 | 0.6727 | 0.1331 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.79 | 0.6665 | 0.1315 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.83 | 0.6936 | 0.1174 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.66 | 0.6945 | 0.1400 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.06 | 0.6973 | 0.1271 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.03 | 0.7036 | 0.1355 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.03 | 0.7015 | 0.1274 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.31 | 0.7051 | 0.0927 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.46 | 0.6986 | 0.0812 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.51 | 0.7081 | 0.0843 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.50 | 0.7040 | 0.0811 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.25 | 0.6700 | 0.0094 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.78 | 0.2780 | 0.0863 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.82 | 0.2685 | 0.0845 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.81 | 0.2767 | 0.0855 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.81 | 0.2692 | 0.0851 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.19 | 0.2982 | 0.0771 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.24 | 0.3060 | 0.0749 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.21 | 0.3116 | 0.0764 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.22 | 0.3090 | 0.0759 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.33 | 0.4376 | 0.0343 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.88 | 0.4050 | 0.0373 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.88 | 0.4050 | 0.0373 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.87 | 0.3990 | 0.0381 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.87 | 0.3990 | 0.0381 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.23 | 0.3611 | 0.0487 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.14 | 0.3318 | 0.0513 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.14 | 0.3318 | 0.0513 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.09 | 0.3333 | 0.0522 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.09 | 0.3333 | 0.0522 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.91 | 0.2998 | 0.0531 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.82 | 0.3263 | 0.0717 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.02 | 0.3605 | 0.0684 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.90 | 0.3447 | 0.0705 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.95 | 0.3524 | 0.0695 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.85 | 0.3305 | 0.0716 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.02 | 0.3639 | 0.0681 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.92 | 0.3483 | 0.0702 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.96 | 0.3558 | 0.0691 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.90 | 0.3401 | 0.0426 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.85 | 0.2134 | 0.1006 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.89 | 0.2307 | 0.0984 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.87 | 0.2231 | 0.0996 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.88 | 0.2280 | 0.0990 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.79 | 0.2374 | 0.1004 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.87 | 0.2524 | 0.0989 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.82 | 0.2462 | 0.0999 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.84 | 0.2507 | 0.0994 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.02 | 0.6258 | 0.0127 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.87 | 0.6198 | 0.0121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.99 | 0.6227 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.88 | 0.6190 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.15 | 0.6458 | 0.0120 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.19 | 0.6405 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.26 | 0.6480 | 0.0112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.19 | 0.6448 | 0.0109 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.42 | 0.6806 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.28 | 0.6759 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.28 | 0.6735 | 0.0116 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.19 | 0.6720 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.22 | 0.6738 | 0.0120 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.37 | 0.6726 | 0.0109 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.13 | 0.6664 | 0.0118 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.13 | 0.6654 | 0.0114 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.14 | 0.6681 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.18 | 0.6704 | 0.0115 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.56 | 0.6469 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.69 | 0.6053 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.95 | 0.6205 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.84 | 0.6133 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.88 | 0.6161 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.76 | 0.6080 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.00 | 0.6220 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 18.92 | 0.6146 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 18.95 | 0.6174 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 18.87 | 0.6163 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.63 | 0.6602 | 0.0114 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.87 | 0.6677 | 0.0104 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.74 | 0.6657 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.80 | 0.6668 | 0.0106 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.34 | 0.6879 | 0.0100 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.52 | 0.6966 | 0.0096 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.41 | 0.6932 | 0.0097 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.47 | 0.6952 | 0.0096 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.99 | 0.6222 | 0.0129 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.85 | 0.6165 | 0.0123 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.97 | 0.6193 | 0.0125 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.85 | 0.6155 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.10 | 0.6439 | 0.0121 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.16 | 0.6390 | 0.0108 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.23 | 0.6466 | 0.0113 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.17 | 0.6436 | 0.0109 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 20.42 | 0.6798 | 0.0122 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.26 | 0.6747 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.25 | 0.6724 | 0.0118 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.18 | 0.6707 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.22 | 0.6730 | 0.0121 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 20.37 | 0.6714 | 0.0109 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.11 | 0.6646 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.11 | 0.6638 | 0.0115 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.14 | 0.6665 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.17 | 0.6691 | 0.0115 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.55 | 0.6442 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.66 | 0.6007 | 0.0146 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.92 | 0.6176 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.81 | 0.6094 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.85 | 0.6126 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.73 | 0.6039 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 18.98 | 0.6192 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 18.89 | 0.6109 | 0.0138 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 18.92 | 0.6140 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.86 | 0.6130 | 0.0147 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.62 | 0.6585 | 0.0115 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.85 | 0.6659 | 0.0105 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.73 | 0.6641 | 0.0108 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.79 | 0.6652 | 0.0107 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.33 | 0.6863 | 0.0101 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.51 | 0.6953 | 0.0096 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.40 | 0.6920 | 0.0097 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.46 | 0.6940 | 0.0097 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 31.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.71 | 0.7785 | 0.0169 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.86 | 0.3979 | 0.2239 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.01 | 0.4070 | 0.2158 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.92 | 0.4142 | 0.2202 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.96 | 0.4112 | 0.2180 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.81 | 0.3920 | 0.2060 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.95 | 0.4049 | 0.1970 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.85 | 0.4089 | 0.2016 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.88 | 0.4072 | 0.1995 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.20 | 0.5858 | 0.1030 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.72 | 0.5518 | 0.1179 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.72 | 0.5518 | 0.1179 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.57 | 0.5399 | 0.1220 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.57 | 0.5399 | 0.1220 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.85 | 0.4105 | 0.1398 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.49 | 0.3503 | 0.1611 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.49 | 0.3503 | 0.1611 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.47 | 0.3435 | 0.1641 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.47 | 0.3435 | 0.1641 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.16 | 0.2910 | 0.1692 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.08 | 0.4538 | 0.1981 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.34 | 0.4693 | 0.1867 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.18 | 0.4736 | 0.1932 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.24 | 0.4715 | 0.1903 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.09 | 0.4557 | 0.1982 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.33 | 0.4720 | 0.1862 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.18 | 0.4761 | 0.1930 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.24 | 0.4742 | 0.1899 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.39 | 0.3539 | 0.1530 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.73 | 0.3746 | 0.2416 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.88 | 0.3833 | 0.2323 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.76 | 0.3853 | 0.2384 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.80 | 0.3845 | 0.2357 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.70 | 0.3909 | 0.2329 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.87 | 0.3935 | 0.2249 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.73 | 0.3967 | 0.2308 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.78 | 0.3953 | 0.2286 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.32 | 0.7602 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.27 | 0.7612 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.36 | 0.7617 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.28 | 0.7611 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.48 | 0.7664 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.63 | 0.7683 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.66 | 0.7694 | 0.0203 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.61 | 0.7690 | 0.0199 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.69 | 0.7774 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.58 | 0.7755 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.59 | 0.7761 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.44 | 0.7737 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.49 | 0.7756 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.62 | 0.7766 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.46 | 0.7734 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.47 | 0.7739 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.40 | 0.7729 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.46 | 0.7750 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.70 | 0.7639 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.94 | 0.7543 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.22 | 0.7589 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.12 | 0.7580 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.17 | 0.7585 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.96 | 0.7546 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.25 | 0.7590 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.18 | 0.7582 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.21 | 0.7587 | 0.0228 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.12 | 0.7554 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.87 | 0.7701 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.12 | 0.7727 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.00 | 0.7720 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.04 | 0.7722 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.48 | 0.7771 | 0.0184 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.65 | 0.7793 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.55 | 0.7787 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.60 | 0.7791 | 0.0179 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.69 | 0.7250 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.70 | 0.7283 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.88 | 0.7315 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.76 | 0.7301 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.92 | 0.7401 | 0.0279 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.22 | 0.7452 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.26 | 0.7483 | 0.0265 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.20 | 0.7470 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.07 | 0.7653 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.29 | 0.7547 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.46 | 0.7631 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.95 | 0.7485 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.26 | 0.7625 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.92 | 0.7670 | 0.0217 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.12 | 0.7492 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.33 | 0.7585 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.96 | 0.7459 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.29 | 0.7588 | 0.0261 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.04 | 0.7161 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.62 | 0.6954 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.00 | 0.7053 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.98 | 0.7071 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.99 | 0.7063 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.62 | 0.6965 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.01 | 0.7060 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.01 | 0.7082 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.00 | 0.7072 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.21 | 0.6871 | 0.0468 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.45 | 0.7462 | 0.0301 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.40 | 0.7445 | 0.0328 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.71 | 0.7509 | 0.0296 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.61 | 0.7486 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.40 | 0.7597 | 0.0267 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.96 | 0.7544 | 0.0284 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.39 | 0.7612 | 0.0271 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.27 | 0.7591 | 0.0276 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 46.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.83 | 0.7305 | 0.0257 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.98 | 0.3223 | 0.3297 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.07 | 0.3357 | 0.3221 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.02 | 0.3382 | 0.3266 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.04 | 0.3375 | 0.3244 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.09 | 0.3163 | 0.2934 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.09 | 0.3297 | 0.2864 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.09 | 0.3308 | 0.2906 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.08 | 0.3303 | 0.2889 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.52 | 0.5504 | 0.1637 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 18.32 | 0.5331 | 0.1676 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 18.32 | 0.5331 | 0.1676 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 18.27 | 0.5261 | 0.1709 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 18.27 | 0.5261 | 0.1709 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.46 | 0.3073 | 0.1961 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.40 | 0.2904 | 0.2020 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.40 | 0.2904 | 0.2020 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.39 | 0.2867 | 0.2038 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.39 | 0.2867 | 0.2038 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.33 | 0.2743 | 0.2038 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.14 | 0.3824 | 0.3050 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.27 | 0.4019 | 0.2934 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.19 | 0.4027 | 0.3008 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.22 | 0.4025 | 0.2975 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.14 | 0.3836 | 0.3048 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.27 | 0.4042 | 0.2926 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.19 | 0.4045 | 0.3004 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.23 | 0.4047 | 0.2970 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.59 | 0.3567 | 0.1821 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.64 | 0.3166 | 0.3415 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.71 | 0.3293 | 0.3332 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.66 | 0.3292 | 0.3388 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.68 | 0.3296 | 0.3366 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.61 | 0.3338 | 0.3345 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.65 | 0.3374 | 0.3292 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.62 | 0.3403 | 0.3335 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.63 | 0.3390 | 0.3315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.93 | 0.7208 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.98 | 0.7221 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.02 | 0.7222 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.99 | 0.7222 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.07 | 0.7242 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.26 | 0.7264 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.25 | 0.7264 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.24 | 0.7266 | 0.0278 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.71 | 0.7287 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.58 | 0.7279 | 0.0277 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.60 | 0.7282 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.55 | 0.7271 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.60 | 0.7281 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.71 | 0.7286 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.51 | 0.7271 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.52 | 0.7274 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.56 | 0.7271 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.60 | 0.7281 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.04 | 0.7235 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.59 | 0.7161 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.74 | 0.7189 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.73 | 0.7186 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.74 | 0.7189 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.61 | 0.7164 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.76 | 0.7191 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.76 | 0.7188 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.76 | 0.7190 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.63 | 0.7188 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.33 | 0.7259 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.48 | 0.7276 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.42 | 0.7273 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.45 | 0.7275 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.69 | 0.7302 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.76 | 0.7312 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.74 | 0.7312 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.75 | 0.7313 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.93 | 0.6999 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.07 | 0.7045 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.15 | 0.7058 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.10 | 0.7054 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.23 | 0.7093 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.56 | 0.7151 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.55 | 0.7156 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.52 | 0.7155 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.57 | 0.7254 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.22 | 0.7217 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.31 | 0.7239 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.19 | 0.7198 | 0.0317 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.37 | 0.7244 | 0.0287 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.53 | 0.7256 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.10 | 0.7202 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.20 | 0.7228 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.17 | 0.7196 | 0.0311 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.35 | 0.7239 | 0.0284 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.41 | 0.7133 | 0.0323 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.87 | 0.6792 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.22 | 0.6887 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.23 | 0.6891 | 0.0407 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.23 | 0.6893 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.90 | 0.6802 | 0.0419 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.24 | 0.6893 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.27 | 0.6900 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.25 | 0.6900 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.65 | 0.7001 | 0.0354 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.54 | 0.7151 | 0.0354 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.90 | 0.7183 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.82 | 0.7188 | 0.0345 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.85 | 0.7187 | 0.0337 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.26 | 0.7242 | 0.0302 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.34 | 0.7243 | 0.0294 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.32 | 0.7256 | 0.0301 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.34 | 0.7251 | 0.0296 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 76.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.72 | 0.7102 | 0.0305 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.80 | 0.2841 | 0.3445 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.89 | 0.2925 | 0.3389 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.84 | 0.2945 | 0.3420 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.86 | 0.2944 | 0.3403 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.85 | 0.2478 | 0.3178 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.83 | 0.2550 | 0.3131 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.85 | 0.2566 | 0.3160 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.84 | 0.2560 | 0.3149 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.15 | 0.5332 | 0.2199 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.16 | 0.5302 | 0.2223 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.16 | 0.5302 | 0.2223 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.12 | 0.5267 | 0.2240 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.12 | 0.5267 | 0.2240 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.19 | 0.1824 | 0.2407 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.18 | 0.1799 | 0.2433 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.18 | 0.1799 | 0.2433 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.17 | 0.1773 | 0.2439 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.17 | 0.1773 | 0.2439 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.16 | 0.1742 | 0.2425 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.43 | 0.3256 | 0.3245 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.53 | 0.3356 | 0.3157 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.47 | 0.3375 | 0.3208 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.50 | 0.3370 | 0.3183 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.43 | 0.3258 | 0.3241 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.53 | 0.3367 | 0.3153 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.46 | 0.3382 | 0.3206 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.49 | 0.3379 | 0.3181 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.73 | 0.2353 | 0.2232 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.71 | 0.2833 | 0.3537 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.77 | 0.2895 | 0.3470 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.73 | 0.2911 | 0.3509 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.75 | 0.2909 | 0.3490 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.66 | 0.2886 | 0.3471 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.68 | 0.2890 | 0.3437 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.66 | 0.2928 | 0.3459 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.67 | 0.2908 | 0.3447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.72 | 0.7101 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.71 | 0.7102 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.73 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.72 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.73 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.73 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.73 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.73 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.72 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.73 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.72 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.70 | 0.7099 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.70 | 0.7101 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.70 | 0.7100 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.70 | 0.7101 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.69 | 0.7099 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.70 | 0.7101 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.70 | 0.7100 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.70 | 0.7101 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.72 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.72 | 0.7102 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.72 | 0.7103 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.72 | 0.7103 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.41 | 0.7050 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.45 | 0.7074 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.51 | 0.7077 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.49 | 0.7077 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.58 | 0.7076 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.57 | 0.7088 | 0.0323 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.61 | 0.7093 | 0.0323 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.60 | 0.7091 | 0.0323 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.74 | 0.7110 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.73 | 0.7107 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.72 | 0.7101 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.73 | 0.7106 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.72 | 0.7102 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.73 | 0.7109 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.72 | 0.7107 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.71 | 0.7102 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.73 | 0.7106 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.72 | 0.7103 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.69 | 0.7104 | 0.0311 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.09 | 0.7026 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.26 | 0.7053 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.26 | 0.7058 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.28 | 0.7058 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.10 | 0.7026 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.26 | 0.7053 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.29 | 0.7060 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.30 | 0.7060 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.52 | 0.7095 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.61 | 0.7092 | 0.0325 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.63 | 0.7096 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.65 | 0.7099 | 0.0321 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.65 | 0.7098 | 0.0320 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.69 | 0.7103 | 0.0314 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.67 | 0.7099 | 0.0315 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.70 | 0.7105 | 0.0313 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.69 | 0.7102 | 0.0314 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.23 | 0.7195 | 0.0449 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.32 | 0.2930 | 0.4111 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.41 | 0.3021 | 0.4010 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.36 | 0.3047 | 0.4071 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.39 | 0.3040 | 0.4037 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.28 | 0.2681 | 0.3857 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.27 | 0.2774 | 0.3754 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.28 | 0.2786 | 0.3819 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.27 | 0.2780 | 0.3794 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.36 | 0.5334 | 0.2917 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.26 | 0.5234 | 0.2980 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.26 | 0.5234 | 0.2980 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.21 | 0.5181 | 0.3007 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.21 | 0.5181 | 0.3007 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.39 | 0.2328 | 0.3091 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.35 | 0.2231 | 0.3152 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.35 | 0.2231 | 0.3152 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.33 | 0.2196 | 0.3165 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.33 | 0.2196 | 0.3165 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.30 | 0.2128 | 0.3173 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.05 | 0.3413 | 0.3833 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.17 | 0.3546 | 0.3684 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.09 | 0.3558 | 0.3775 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.13 | 0.3555 | 0.3731 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.05 | 0.3422 | 0.3829 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.17 | 0.3562 | 0.3681 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.09 | 0.3571 | 0.3768 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.13 | 0.3570 | 0.3726 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.09 | 0.2787 | 0.2869 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.10 | 0.2897 | 0.4222 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.16 | 0.2977 | 0.4111 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.12 | 0.2989 | 0.4180 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.13 | 0.2989 | 0.4151 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.05 | 0.2987 | 0.4068 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.08 | 0.3003 | 0.3993 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.06 | 0.3034 | 0.4045 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.07 | 0.3018 | 0.4018 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.56 | 0.7141 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.55 | 0.7145 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.60 | 0.7147 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.56 | 0.7146 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.66 | 0.7160 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.76 | 0.7169 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.76 | 0.7170 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.74 | 0.7170 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.23 | 0.7190 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.10 | 0.7183 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.10 | 0.7183 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.04 | 0.7177 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.07 | 0.7182 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.22 | 0.7189 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.07 | 0.7179 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.07 | 0.7180 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.05 | 0.7177 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.07 | 0.7181 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.83 | 0.7162 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.38 | 0.7117 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.53 | 0.7133 | 0.0498 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.49 | 0.7131 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.51 | 0.7132 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.39 | 0.7118 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.55 | 0.7134 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.52 | 0.7131 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.53 | 0.7133 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.50 | 0.7136 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.89 | 0.7171 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.00 | 0.7180 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.95 | 0.7178 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.98 | 0.7179 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.18 | 0.7193 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.25 | 0.7200 | 0.0451 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.21 | 0.7198 | 0.0452 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.23 | 0.7199 | 0.0452 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.78 | 0.7015 | 0.0569 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.84 | 0.7040 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.93 | 0.7051 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.88 | 0.7047 | 0.0549 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.03 | 0.7073 | 0.0553 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.22 | 0.7100 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.24 | 0.7107 | 0.0538 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.20 | 0.7104 | 0.0529 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.15 | 0.7177 | 0.0502 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.82 | 0.7151 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.86 | 0.7160 | 0.0486 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.70 | 0.7138 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.79 | 0.7158 | 0.0484 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.12 | 0.7176 | 0.0481 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.76 | 0.7144 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.82 | 0.7155 | 0.0482 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.68 | 0.7138 | 0.0510 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.78 | 0.7156 | 0.0480 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.40 | 0.7112 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.05 | 0.6899 | 0.0640 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.34 | 0.6951 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.33 | 0.6957 | 0.0625 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.34 | 0.6957 | 0.0612 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.07 | 0.6904 | 0.0639 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.35 | 0.6955 | 0.0599 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.37 | 0.6962 | 0.0621 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.37 | 0.6961 | 0.0609 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.78 | 0.7041 | 0.0554 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.35 | 0.7111 | 0.0558 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.60 | 0.7127 | 0.0534 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.56 | 0.7132 | 0.0549 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.58 | 0.7131 | 0.0541 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.89 | 0.7159 | 0.0501 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.98 | 0.7162 | 0.0491 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.93 | 0.7168 | 0.0499 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.96 | 0.7166 | 0.0493 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 239683 | 0.331 | 57.1 | 28.24 | 0.21 | 0.025 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 239683 | 0.331 | 72.5 | 28.24 | 0.21 | 0.025 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 239683 | 0.331 | 62.3 | 28.24 | 0.21 | 0.025 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 239683 | 0.331 | 51.7 | 28.24 | 0.21 | 0.025 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1245 | None | classic | 0.38 | False | 573564 | 0.987 | 148.5 | 30.90 | 0.30 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1245 | None | classic | 0.38 | False | 573564 | 0.987 | 178.6 | 30.90 | 0.30 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1245 | None | classic | 0.38 | False | 573564 | 0.987 | 193.3 | 30.90 | 0.30 | 0.019 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1245 | None | classic | 0.38 | False | 573564 | 0.987 | 158.9 | 30.90 | 0.30 | 0.019 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1165884 | 0.214 | 42.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1165884 | 0.804 | 46.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1165884 | 0.804 | 46.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1165884 | 0.510 | 40.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1165884 | 0.510 | 40.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1165884 | 0.214 | 49.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1165884 | 0.804 | 195.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1165884 | 0.804 | 195.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1165884 | 0.510 | 49.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1165884 | 0.510 | 49.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1162038 | 0.804 | 489.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 249989 | 0.333 | 67.9 | 28.58 | 0.17 | 0.023 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 249989 | 0.333 | 51.3 | 28.58 | 0.17 | 0.023 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 249989 | 0.333 | 64.9 | 28.58 | 0.17 | 0.023 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 249989 | 0.333 | 76.6 | 28.58 | 0.17 | 0.023 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 250713 | 0.344 | 72.9 | 28.64 | 0.17 | 0.025 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 250713 | 0.344 | 70.6 | 28.64 | 0.17 | 0.025 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 250713 | 0.344 | 53.5 | 28.64 | 0.17 | 0.025 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 250713 | 0.344 | 53.2 | 28.64 | 0.17 | 0.025 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1522845 | 0.804 | 107.2 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 249353 | 0.929 | 80.4 | 29.54 | 0.15 | 0.025 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 249353 | 0.929 | 74.6 | 29.54 | 0.15 | 0.025 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 249353 | 0.929 | 78.2 | 29.54 | 0.15 | 0.025 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 249353 | 0.929 | 54.6 | 29.54 | 0.15 | 0.025 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 603 | None | classic | 0.54 | False | 641785 | 1.315 | 244.7 | 27.80 | 0.23 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 603 | None | classic | 0.54 | False | 641785 | 1.315 | 245.8 | 27.80 | 0.23 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 603 | None | classic | 0.54 | False | 641785 | 1.315 | 218.5 | 27.80 | 0.23 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 603 | None | classic | 0.54 | False | 641785 | 1.315 | 234.7 | 27.80 | 0.23 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.711 | 0.016 |
| in035 | mask_ent | 0.783 | 0.016 |
| in035 | mask_grad | 0.436 | 0.016 |
| in035 | r_col | 0.811 | 0.016 |
| in035 | r_warp | 0.857 | 0.016 |

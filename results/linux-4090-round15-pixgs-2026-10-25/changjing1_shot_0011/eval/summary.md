# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 12.7% | 24.26 / 0.0152 | 20.25 / 0.0360 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 13.2% | 24.35 / 0.0155 | 21.62 / 0.0286 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 13.0% | 24.30 / 0.0155 | 21.21 / 0.0314 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 13.1% | 24.33 / 0.0156 | 21.36 / 0.0298 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 13.1% | 24.36 / 0.0154 | 21.16 / 0.0296 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.4% | 24.43 / 0.0156 | 22.15 / 0.0234 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 13.2% | 24.38 / 0.0156 | 21.81 / 0.0250 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 13.2% | 24.41 / 0.0156 | 21.86 / 0.0237 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 13.8% | 24.43 / 0.0159 | 20.74 / 0.0487 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 16.8% | 24.94 / 0.0164 | 20.28 / 0.0463 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 17.6% | 25.01 / 0.0168 | 21.32 / 0.0353 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 17.2% | 24.99 / 0.0167 | 21.02 / 0.0403 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 17.4% | 25.00 / 0.0167 | 21.13 / 0.0375 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 17.6% | 25.05 / 0.0169 | 20.72 / 0.0383 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 18.4% | 25.14 / 0.0173 | 21.94 / 0.0298 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 18.1% | 25.09 / 0.0170 | 21.61 / 0.0318 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 18.1% | 25.11 / 0.0170 | 21.79 / 0.0302 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 17.9% | 25.05 / 0.0176 | 20.70 / 0.0596 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 10.5% | 24.15 / 0.0157 | 20.20 / 0.0366 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 11.8% | 24.41 / 0.0166 | 21.04 / 0.0353 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 11.1% | 24.23 / 0.0163 | 20.95 / 0.0350 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 11.3% | 24.28 / 0.0163 | 21.01 / 0.0350 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 11.6% | 24.38 / 0.0164 | 20.76 / 0.0384 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 12.7% | 24.60 / 0.0172 | 21.25 / 0.0357 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 12.1% | 24.48 / 0.0165 | 21.41 / 0.0360 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 12.3% | 24.51 / 0.0167 | 21.27 / 0.0364 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.05 / 0.0485 | 24.83 / 0.0744 | 19.87 / 0.0131 | 29.77 / 0.0313 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.59 / 0.0643 | 23.35 / 0.1479 | 18.13 / 0.0179 | 29.60 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.31 / 0.0589 | 24.74 / 0.1140 | 19.02 / 0.0157 | 29.69 / 0.0332 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.19 / 0.0613 | 24.50 / 0.1266 | 18.78 / 0.0162 | 29.71 / 0.0333 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.23 / 0.0600 | 24.75 / 0.1185 | 18.83 / 0.0157 | 29.71 / 0.0331 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.07 / 0.0590 | 23.86 / 0.1227 | 18.67 / 0.0158 | 29.66 / 0.0333 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.64 / 0.0542 | 25.61 / 0.0944 | 19.76 / 0.0135 | 29.69 / 0.0326 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.45 / 0.0566 | 25.09 / 0.1053 | 19.26 / 0.0143 | 29.71 / 0.0330 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.50 / 0.0555 | 25.45 / 0.0977 | 19.38 / 0.0142 | 29.71 / 0.0327 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.36 / 0.0614 | 23.78 / 0.1457 | 19.04 / 0.0191 | 29.78 / 0.0320 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.06 / 0.0720 | 23.76 / 0.1479 | 18.02 / 0.0193 | 29.27 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.65 / 0.0632 | 24.78 / 0.1100 | 18.73 / 0.0165 | 29.52 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.53 / 0.0674 | 24.73 / 0.1272 | 18.43 / 0.0178 | 29.50 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.58 / 0.0653 | 24.86 / 0.1197 | 18.53 / 0.0172 | 29.53 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.24 / 0.0648 | 24.24 / 0.1294 | 18.27 / 0.0171 | 29.27 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.92 / 0.0587 | 25.73 / 0.0980 | 19.43 / 0.0139 | 29.37 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.74 / 0.0612 | 25.61 / 0.1103 | 18.96 / 0.0148 | 29.41 / 0.0353 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.83 / 0.0597 | 25.81 / 0.1019 | 19.19 / 0.0142 | 29.38 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.86 / 0.0648 | 23.73 / 0.1458 | 18.77 / 0.0203 | 29.68 / 0.0330 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.81 / 0.0636 | 23.27 / 0.1449 | 18.33 / 0.0167 | 29.70 / 0.0335 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.29 / 0.0592 | 24.20 / 0.1190 | 19.05 / 0.0144 | 29.71 / 0.0329 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.18 / 0.0612 | 24.03 / 0.1338 | 18.88 / 0.0153 | 29.74 / 0.0332 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.22 / 0.0602 | 24.19 / 0.1263 | 18.93 / 0.0149 | 29.73 / 0.0330 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.00 / 0.0620 | 24.06 / 0.1380 | 18.79 / 0.0164 | 29.74 / 0.0331 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.35 / 0.0579 | 24.32 / 0.1152 | 19.47 / 0.0141 | 29.69 / 0.0332 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.25 / 0.0601 | 24.39 / 0.1251 | 19.31 / 0.0146 | 29.73 / 0.0332 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.25 / 0.0591 | 24.29 / 0.1213 | 19.35 / 0.0144 | 29.70 / 0.0332 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.4%） | — | — | 28.05 / 0.0485 | 24.83 / 0.0744 | 29.77 |
| in035 | rife | 6.6% | 10.5% | 26.81 / 0.0636 | 23.27 / 0.1449 | 29.70 |
| in035 | cnw_cnn | 9.1% | 12.7% | 26.59 / 0.0643 | 23.35 / 0.1479 | 29.60 |
| in035 | cnw_f5 | 11.7% | 16.8% | 26.06 / 0.0720 | 23.76 / 0.1479 | 29.27 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.48 / 0.0497 | -1.55 / +0.0189 (core 6.5%) | -1.53 / +0.0179 (core 9.3%) | -1.85 / +0.0252 (core 11.6%) |
| in035 | 2 | 0-3 | 27.72 / 0.0480 | -0.87 / +0.0164 (core 6.5%) | -1.30 / +0.0179 (core 9.3%) | -1.90 / +0.0271 (core 11.6%) |
| in035 | 4 | 3-5 | 28.96 / 0.0477 | -1.32 / +0.0100 (core 4.2%) | -1.55 / +0.0115 (core 5.6%) | -2.23 / +0.0181 (core 8.2%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.05 / 0.0485 | 24.83 | 29.77 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.59 / 0.0643 | 23.35 | 29.60 | 0/3 |
| in035 | cnw_cnn | oracle | 2.8% | 27.23 / 0.0548 | 24.38 | 29.77 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.31 / 0.0589 | 24.74 | 29.69 | 0/3 |
| in035 | cnw_cnn | oracle | 2.8% | 27.70 / 0.0522 | 25.31 | 29.77 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.19 / 0.0613 | 24.50 | 29.71 | 0/3 |
| in035 | cnw_cnn | oracle | 2.8% | 27.58 / 0.0532 | 25.06 | 29.77 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.23 / 0.0600 | 24.75 | 29.71 | 0/3 |
| in035 | cnw_cnn | oracle | 2.8% | 27.61 / 0.0527 | 25.26 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.07 / 0.0590 | 23.86 | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 27.54 / 0.0514 | 24.47 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.64 / 0.0542 | 25.61 | 29.69 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 28.01 / 0.0492 | 26.00 | 29.77 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.45 / 0.0566 | 25.09 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 27.82 / 0.0500 | 25.44 | 29.77 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.50 / 0.0555 | 25.45 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 27.87 / 0.0497 | 25.82 | 29.77 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.36 / 0.0614 | 23.78 | 29.78 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.9% | 27.66 / 0.0548 | 24.28 | 29.77 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.06 / 0.0720 | 23.76 | 29.27 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 27.11 / 0.0568 | 24.65 | 29.76 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.65 / 0.0632 | 24.78 | 29.52 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 27.50 / 0.0529 | 25.34 | 29.76 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.53 / 0.0674 | 24.73 | 29.50 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 27.36 / 0.0549 | 25.28 | 29.77 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.58 / 0.0653 | 24.86 | 29.53 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 27.41 / 0.0540 | 25.41 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.24 / 0.0648 | 24.24 | 29.27 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.1% | 27.24 / 0.0534 | 24.86 | 29.76 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.92 / 0.0587 | 25.73 | 29.37 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.2% | 27.81 / 0.0500 | 26.20 | 29.77 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.74 / 0.0612 | 25.61 | 29.41 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.2% | 27.61 / 0.0511 | 26.03 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.83 / 0.0597 | 25.81 | 29.38 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.2% | 27.71 / 0.0504 | 26.28 | 29.77 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.86 / 0.0648 | 23.73 | 29.68 | 0/3 |
| in035 | cnw_f5_pix | oracle | 3.2% | 27.48 / 0.0560 | 24.24 | 29.77 | 0/3 |
| in035 | rife | 不复核 | —% | 26.81 / 0.0636 | 23.27 | 29.70 | 0/3 |
| in035 | rife | oracle | 2.2% | 27.34 / 0.0528 | 24.26 | 29.77 | 0/3 |
| in035 | rife | 不复核 | —% | 27.29 / 0.0592 | 24.20 | 29.71 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.71 / 0.0506 | 24.79 | 29.77 | 0/3 |
| in035 | rife | 不复核 | —% | 27.18 / 0.0612 | 24.03 | 29.74 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.62 / 0.0516 | 24.64 | 29.77 | 0/3 |
| in035 | rife | 不复核 | —% | 27.22 / 0.0602 | 24.19 | 29.73 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.64 / 0.0511 | 24.79 | 29.77 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.00 / 0.0620 | 24.06 | 29.74 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 27.57 / 0.0519 | 24.93 | 29.77 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.35 / 0.0579 | 24.32 | 29.69 | 0/3 |
| in035 | rife_mw | oracle | 2.4% | 27.86 / 0.0496 | 25.10 | 29.77 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.25 / 0.0601 | 24.39 | 29.73 | 0/3 |
| in035 | rife_mw | oracle | 2.4% | 27.80 / 0.0503 | 25.17 | 29.77 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.25 / 0.0591 | 24.29 | 29.70 | 0/3 |
| in035 | rife_mw | oracle | 2.4% | 27.81 / 0.0499 | 25.08 | 29.77 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.05 / 0.0485 | 24.83 / 0.0744 | — |
| in035 | FF | 0（前馈） | 1008×686（64%） | 27.06 | 26.59 / 0.0643 | 23.35 / 0.1479 | 0/3 |
| in035 | 25 | 0.59 s | 1008×686（64%） | 27.80 | 27.19 / 0.0613 | 24.50 / 0.1266 | 0/3 |
| in035 | 50 | 1.17 s | 1008×686（64%） | 28.12 | 27.23 / 0.0600 | 24.75 / 0.1185 | 0/3 |
| in035 | 100 | 2.29 s | 1008×686（64%） | 28.46 | 27.31 / 0.0589 | 24.74 / 0.1140 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.05 / 0.0485 | 24.83 / 0.0744 | 29.77 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.59 / 0.0643 | 23.35 / 0.1479 | 29.60 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.23 / 0.0548 | 24.38 / 0.1027 | 29.77 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.19 / 0.0613 | 24.50 / 0.1266 | 29.71 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.58 / 0.0532 | 25.06 / 0.0902 | 29.77 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.23 / 0.0600 | 24.75 / 0.1185 | 29.71 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.61 / 0.0527 | 25.26 / 0.0845 | 29.77 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.31 / 0.0589 | 24.74 / 0.1140 | 29.69 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.70 / 0.0522 | 25.31 / 0.0817 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.07 / 0.0590 | 23.86 / 0.1227 | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.54 / 0.0514 | 24.47 / 0.0882 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.45 / 0.0566 | 25.09 / 0.1053 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.82 / 0.0500 | 25.44 / 0.0751 | 29.77 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.50 / 0.0555 | 25.45 / 0.0977 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.87 / 0.0497 | 25.82 / 0.0705 | 29.77 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.64 / 0.0542 | 25.61 / 0.0944 | 29.69 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.01 / 0.0492 | 26.00 / 0.0695 | 29.77 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.06 / 0.0720 | 23.76 / 0.1479 | 29.27 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.11 / 0.0568 | 24.65 / 0.1003 | 29.76 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.53 / 0.0674 | 24.73 / 0.1272 | 29.50 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.36 / 0.0549 | 25.28 / 0.0861 | 29.77 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.58 / 0.0653 | 24.86 / 0.1197 | 29.53 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.41 / 0.0540 | 25.41 / 0.0827 | 29.77 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.65 / 0.0632 | 24.78 / 0.1100 | 29.52 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.50 / 0.0529 | 25.34 / 0.0786 | 29.76 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.24 / 0.0648 | 24.24 / 0.1294 | 29.27 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.24 / 0.0534 | 24.86 / 0.0892 | 29.76 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.74 / 0.0612 | 25.61 / 0.1103 | 29.41 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.61 / 0.0511 | 26.03 / 0.0769 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.83 / 0.0597 | 25.81 / 0.1019 | 29.38 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.71 / 0.0504 | 26.28 / 0.0721 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 26.92 / 0.0587 | 25.73 / 0.0980 | 29.37 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.81 / 0.0500 | 26.20 / 0.0697 | 29.77 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.81 / 0.0636 | 23.27 / 0.1449 | 29.70 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.34 / 0.0528 | 24.26 / 0.0929 | 29.77 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.18 / 0.0612 | 24.03 / 0.1338 | 29.74 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.62 / 0.0516 | 24.64 / 0.0882 | 29.77 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.22 / 0.0602 | 24.19 / 0.1263 | 29.73 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.64 / 0.0511 | 24.79 / 0.0849 | 29.77 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.29 / 0.0592 | 24.20 / 0.1190 | 29.71 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.71 / 0.0506 | 24.79 / 0.0808 | 29.77 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.00 / 0.0620 | 24.06 / 0.1380 | 29.74 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.57 / 0.0519 | 24.93 / 0.0909 | 29.77 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.25 / 0.0601 | 24.39 / 0.1251 | 29.73 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.80 / 0.0503 | 25.17 / 0.0808 | 29.77 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.25 / 0.0591 | 24.29 / 0.1213 | 29.70 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.81 / 0.0499 | 25.08 / 0.0810 | 29.77 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.35 / 0.0579 | 24.32 / 0.1152 | 29.69 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.86 / 0.0496 | 25.10 / 0.0793 | 29.77 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.83 / 0.0744 | 19.87 / 0.0131 | 29.77 / 0.0313 | 28.05 / 0.0485 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 6.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.83 | 0.7613 | 0.0744 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 21.77 | 0.7330 | 0.1819 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 23.36 | 0.7571 | 0.1396 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 23.27 | 0.7677 | 0.1546 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 23.50 | 0.7691 | 0.1446 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 22.69 | 0.7449 | 0.1484 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 24.52 | 0.7629 | 0.1155 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 23.95 | 0.7614 | 0.1295 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 24.31 | 0.7638 | 0.1204 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 23.66 | 0.7712 | 0.1524 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 22.90 | 0.7417 | 0.1663 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 24.31 | 0.7649 | 0.1248 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 24.27 | 0.7694 | 0.1435 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 24.43 | 0.7719 | 0.1334 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 23.80 | 0.7612 | 0.1417 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 25.45 | 0.7686 | 0.1086 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 25.40 | 0.7726 | 0.1202 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 25.56 | 0.7734 | 0.1105 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 23.66 | 0.7715 | 0.1508 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 19.22 | 0.7050 | 0.2173 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 20.16 | 0.7266 | 0.1685 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 20.15 | 0.7357 | 0.1943 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 20.22 | 0.7360 | 0.1793 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 19.52 | 0.7086 | 0.1867 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 20.36 | 0.6972 | 0.1612 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 20.05 | 0.7066 | 0.1768 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 20.12 | 0.6982 | 0.1712 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.38 | 0.7715 | 0.1027 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.31 | 0.7870 | 0.0817 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.06 | 0.7844 | 0.0902 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.26 | 0.7877 | 0.0845 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.47 | 0.7688 | 0.0882 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.00 | 0.7843 | 0.0695 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.44 | 0.7779 | 0.0751 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.82 | 0.7818 | 0.0705 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.28 | 0.7788 | 0.1101 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.65 | 0.7698 | 0.1003 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.34 | 0.7857 | 0.0786 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.28 | 0.7811 | 0.0861 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.41 | 0.7852 | 0.0827 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.86 | 0.7765 | 0.0892 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.20 | 0.7868 | 0.0697 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.03 | 0.7846 | 0.0769 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.28 | 0.7873 | 0.0721 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.24 | 0.7766 | 0.1098 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.26 | 0.7605 | 0.0929 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.79 | 0.7789 | 0.0808 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.64 | 0.7749 | 0.0882 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.79 | 0.7790 | 0.0849 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 24.93 | 0.7665 | 0.0909 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.10 | 0.7630 | 0.0793 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.17 | 0.7679 | 0.0808 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.08 | 0.7638 | 0.0810 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.35 | 0.7561 | 0.1479 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.74 | 0.7755 | 0.1140 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.50 | 0.7796 | 0.1266 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.75 | 0.7816 | 0.1185 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.86 | 0.7608 | 0.1227 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.61 | 0.7777 | 0.0944 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.09 | 0.7744 | 0.1053 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.45 | 0.7777 | 0.0977 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.78 | 0.7737 | 0.1457 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.76 | 0.7580 | 0.1479 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.78 | 0.7778 | 0.1100 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.73 | 0.7776 | 0.1272 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.86 | 0.7806 | 0.1197 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.24 | 0.7691 | 0.1294 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.73 | 0.7796 | 0.0980 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.61 | 0.7798 | 0.1103 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.81 | 0.7820 | 0.1019 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.73 | 0.7722 | 0.1458 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.27 | 0.7424 | 0.1449 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.20 | 0.7645 | 0.1190 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.03 | 0.7674 | 0.1338 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.19 | 0.7693 | 0.1263 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.06 | 0.7543 | 0.1380 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.32 | 0.7464 | 0.1152 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.39 | 0.7547 | 0.1251 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.29 | 0.7485 | 0.1213 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.87 | 0.6189 | 0.0131 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.85 | 0.3604 | 0.0815 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.00 | 0.3948 | 0.0781 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.94 | 0.3848 | 0.0794 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.95 | 0.3884 | 0.0787 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.25 | 0.3910 | 0.0702 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.52 | 0.4391 | 0.0652 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.36 | 0.4217 | 0.0680 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.42 | 0.4310 | 0.0667 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.22 | 0.3618 | 0.0489 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.77 | 0.3725 | 0.0686 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.99 | 0.4105 | 0.0652 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.90 | 0.3965 | 0.0668 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.94 | 0.4025 | 0.0660 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.92 | 0.4322 | 0.0652 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.12 | 0.4738 | 0.0617 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.06 | 0.4612 | 0.0629 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.08 | 0.4684 | 0.0623 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.65 | 0.3919 | 0.0440 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.19 | 0.3322 | 0.0874 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.31 | 0.3609 | 0.0840 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.27 | 0.3539 | 0.0858 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.28 | 0.3572 | 0.0851 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.25 | 0.3611 | 0.0865 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.32 | 0.3683 | 0.0834 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.29 | 0.3709 | 0.0852 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.29 | 0.3687 | 0.0846 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.18 | 0.5910 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.02 | 0.6129 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.79 | 0.6052 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.84 | 0.6077 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.72 | 0.6128 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.79 | 0.6460 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.29 | 0.6309 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.41 | 0.6376 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.04 | 0.6113 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.05 | 0.5665 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.74 | 0.5914 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.45 | 0.5792 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.55 | 0.5850 | 0.0171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.31 | 0.6026 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.45 | 0.6378 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 18.99 | 0.6237 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.21 | 0.6306 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 18.78 | 0.5914 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.37 | 0.5913 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.07 | 0.6142 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.90 | 0.6084 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.95 | 0.6122 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 18.83 | 0.6102 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.49 | 0.6284 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.35 | 0.6249 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.38 | 0.6263 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.13 | 0.5875 | 0.0179 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.02 | 0.6108 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.78 | 0.6030 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.83 | 0.6056 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.67 | 0.6098 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.76 | 0.6433 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.26 | 0.6289 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.38 | 0.6354 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.04 | 0.6082 | 0.0191 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.02 | 0.5624 | 0.0193 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.73 | 0.5889 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.43 | 0.5756 | 0.0178 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.53 | 0.5817 | 0.0172 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.27 | 0.5977 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.43 | 0.6353 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 18.96 | 0.6202 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.19 | 0.6275 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.77 | 0.5872 | 0.0203 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.33 | 0.5879 | 0.0167 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.05 | 0.6123 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.88 | 0.6062 | 0.0153 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.93 | 0.6099 | 0.0149 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 18.79 | 0.6066 | 0.0164 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.47 | 0.6258 | 0.0141 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.31 | 0.6216 | 0.0146 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.35 | 0.6237 | 0.0144 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 32.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.11 | 0.7602 | 0.0214 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.84 | 0.4681 | 0.2045 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.99 | 0.4902 | 0.1936 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.89 | 0.4910 | 0.1986 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.92 | 0.4919 | 0.1959 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.98 | 0.4536 | 0.1833 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.04 | 0.4741 | 0.1736 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.99 | 0.4745 | 0.1782 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.00 | 0.4743 | 0.1759 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.01 | 0.3588 | 0.1641 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.90 | 0.5069 | 0.1787 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.05 | 0.5296 | 0.1658 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.97 | 0.5316 | 0.1714 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.00 | 0.5318 | 0.1685 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.97 | 0.5326 | 0.1696 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.11 | 0.5517 | 0.1578 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.02 | 0.5570 | 0.1624 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.05 | 0.5557 | 0.1599 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.94 | 0.4009 | 0.1496 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.75 | 0.4358 | 0.2148 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.90 | 0.4531 | 0.2032 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.80 | 0.4536 | 0.2099 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.84 | 0.4541 | 0.2068 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.74 | 0.4376 | 0.2098 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.92 | 0.4495 | 0.1983 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.78 | 0.4514 | 0.2057 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.83 | 0.4499 | 0.2028 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.44 | 0.7463 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.22 | 0.7546 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.97 | 0.7525 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.05 | 0.7536 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.93 | 0.7521 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.75 | 0.7620 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.40 | 0.7585 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.48 | 0.7602 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.05 | 0.7496 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.28 | 0.7394 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.92 | 0.7489 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.67 | 0.7455 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.77 | 0.7473 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.48 | 0.7480 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.42 | 0.7587 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.06 | 0.7558 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.23 | 0.7576 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.75 | 0.7412 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.63 | 0.7482 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.25 | 0.7562 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.09 | 0.7541 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.12 | 0.7554 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 24.98 | 0.7522 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.52 | 0.7570 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.39 | 0.7567 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.41 | 0.7567 | 0.0234 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.02 | 0.7215 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.99 | 0.7349 | 0.0321 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.78 | 0.7345 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.85 | 0.7354 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.69 | 0.7329 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.43 | 0.7473 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.20 | 0.7457 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.20 | 0.7466 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.11 | 0.7090 | 0.0476 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.35 | 0.6918 | 0.0436 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.08 | 0.7065 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.87 | 0.7053 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.94 | 0.7066 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.59 | 0.7067 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.49 | 0.7248 | 0.0309 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.30 | 0.7256 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.40 | 0.7264 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.28 | 0.6734 | 0.0562 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.39 | 0.7264 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.82 | 0.7341 | 0.0362 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.91 | 0.7373 | 0.0359 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.91 | 0.7373 | 0.0355 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.56 | 0.7250 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.81 | 0.7308 | 0.0347 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.96 | 0.7336 | 0.0347 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.84 | 0.7316 | 0.0344 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 44.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.08 | 0.7277 | 0.0282 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.72 | 0.3992 | 0.3206 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.79 | 0.4170 | 0.3098 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.75 | 0.4175 | 0.3155 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.77 | 0.4181 | 0.3125 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.14 | 0.3972 | 0.2748 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.14 | 0.4071 | 0.2660 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.14 | 0.4078 | 0.2710 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.13 | 0.4075 | 0.2686 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.07 | 0.3427 | 0.1930 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.40 | 0.4355 | 0.2955 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.47 | 0.4532 | 0.2825 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.44 | 0.4542 | 0.2888 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.45 | 0.4544 | 0.2858 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.43 | 0.4607 | 0.2840 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.47 | 0.4704 | 0.2755 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.45 | 0.4746 | 0.2798 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.46 | 0.4728 | 0.2777 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.94 | 0.3938 | 0.1774 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.31 | 0.3851 | 0.3281 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.38 | 0.3982 | 0.3182 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.34 | 0.3985 | 0.3239 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.36 | 0.3991 | 0.3213 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.32 | 0.3908 | 0.3223 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.37 | 0.3930 | 0.3162 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.33 | 0.3983 | 0.3204 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.35 | 0.3953 | 0.3187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.80 | 0.7198 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.50 | 0.7253 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.32 | 0.7243 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.37 | 0.7247 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.24 | 0.7246 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.98 | 0.7313 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.68 | 0.7290 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.74 | 0.7300 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.55 | 0.7255 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.59 | 0.7145 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.19 | 0.7209 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.97 | 0.7189 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.05 | 0.7200 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.79 | 0.7212 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.68 | 0.7283 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.35 | 0.7265 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.51 | 0.7276 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.23 | 0.7204 | 0.0353 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.91 | 0.7203 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.50 | 0.7261 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.36 | 0.7247 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.39 | 0.7256 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.19 | 0.7237 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.66 | 0.7264 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.56 | 0.7265 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.57 | 0.7264 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.95 | 0.7060 | 0.0423 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.96 | 0.7156 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.78 | 0.7160 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.84 | 0.7163 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.60 | 0.7168 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.46 | 0.7252 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.16 | 0.7243 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.23 | 0.7250 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.14 | 0.7179 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.22 | 0.6866 | 0.0489 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.00 | 0.6974 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.82 | 0.6968 | 0.0443 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.89 | 0.6976 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.52 | 0.6987 | 0.0423 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.49 | 0.7092 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.22 | 0.7092 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.35 | 0.7097 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.35 | 0.7016 | 0.0430 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.16 | 0.7099 | 0.0418 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.89 | 0.7179 | 0.0375 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.72 | 0.7178 | 0.0394 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.77 | 0.7183 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.30 | 0.7123 | 0.0404 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.89 | 0.7145 | 0.0366 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.71 | 0.7160 | 0.0386 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.73 | 0.7149 | 0.0377 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 76.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.77 | 0.7188 | 0.0313 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.91 | 0.3176 | 0.3395 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.97 | 0.3212 | 0.3322 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.93 | 0.3234 | 0.3363 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.95 | 0.3226 | 0.3344 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.94 | 0.2696 | 0.3095 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.94 | 0.2703 | 0.3038 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.93 | 0.2730 | 0.3072 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.93 | 0.2719 | 0.3054 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.51 | 0.1712 | 0.2438 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.35 | 0.3500 | 0.3160 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.38 | 0.3535 | 0.3066 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.36 | 0.3570 | 0.3117 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.37 | 0.3556 | 0.3091 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.35 | 0.3563 | 0.3073 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.36 | 0.3544 | 0.3009 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.36 | 0.3601 | 0.3045 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.36 | 0.3573 | 0.3027 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.83 | 0.2191 | 0.2266 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.79 | 0.3117 | 0.3444 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.83 | 0.3129 | 0.3385 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.80 | 0.3153 | 0.3420 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.81 | 0.3144 | 0.3403 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.79 | 0.3129 | 0.3399 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.82 | 0.3110 | 0.3354 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.80 | 0.3152 | 0.3380 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.81 | 0.3133 | 0.3367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.77 | 0.7187 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.77 | 0.7189 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.76 | 0.7186 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.76 | 0.7187 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.77 | 0.7187 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.77 | 0.7187 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.76 | 0.7186 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7187 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.77 | 0.7187 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.77 | 0.7187 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.77 | 0.7189 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.77 | 0.7188 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.77 | 0.7189 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.77 | 0.7189 | 0.0312 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.60 | 0.7170 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.69 | 0.7181 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.71 | 0.7185 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.71 | 0.7184 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.66 | 0.7185 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.69 | 0.7189 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.71 | 0.7191 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.71 | 0.7191 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.78 | 0.7198 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.27 | 0.7147 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.52 | 0.7167 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.50 | 0.7171 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.53 | 0.7171 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.27 | 0.7157 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.37 | 0.7166 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.41 | 0.7172 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.38 | 0.7169 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.68 | 0.7192 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.70 | 0.7183 | 0.0335 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.71 | 0.7187 | 0.0329 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.74 | 0.7191 | 0.0332 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.73 | 0.7190 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.74 | 0.7186 | 0.0331 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.69 | 0.7178 | 0.0332 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.73 | 0.7185 | 0.0332 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.70 | 0.7181 | 0.0332 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.05 | 0.7219 | 0.0485 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.59 | 0.3455 | 0.4040 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.66 | 0.3547 | 0.3902 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.61 | 0.3563 | 0.3979 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.63 | 0.3560 | 0.3941 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.53 | 0.3126 | 0.3711 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.54 | 0.3189 | 0.3586 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.53 | 0.3200 | 0.3657 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.53 | 0.3195 | 0.3616 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.99 | 0.2333 | 0.3241 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.07 | 0.3779 | 0.3784 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.11 | 0.3873 | 0.3611 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.09 | 0.3897 | 0.3703 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.10 | 0.3890 | 0.3658 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.08 | 0.3918 | 0.3625 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.10 | 0.3957 | 0.3497 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.09 | 0.3999 | 0.3564 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.09 | 0.3980 | 0.3528 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.40 | 0.2785 | 0.3005 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.34 | 0.3337 | 0.4117 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.39 | 0.3393 | 0.3999 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.36 | 0.3413 | 0.4070 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.37 | 0.3408 | 0.4039 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.35 | 0.3379 | 0.4029 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.38 | 0.3370 | 0.3928 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.35 | 0.3415 | 0.3987 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.36 | 0.3391 | 0.3960 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.23 | 0.7181 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.70 | 0.7209 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.58 | 0.7203 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.61 | 0.7206 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.54 | 0.7206 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.01 | 0.7240 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.82 | 0.7228 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.87 | 0.7234 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.66 | 0.7209 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.11 | 0.7157 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.50 | 0.7188 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.36 | 0.7178 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.41 | 0.7183 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.24 | 0.7188 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.81 | 0.7224 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.61 | 0.7215 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.71 | 0.7221 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.48 | 0.7185 | 0.0560 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.34 | 0.7186 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.71 | 0.7212 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.62 | 0.7206 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.64 | 0.7210 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.57 | 0.7205 | 0.0519 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.86 | 0.7217 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.80 | 0.7219 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.81 | 0.7218 | 0.0499 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.59 | 0.7111 | 0.0643 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.31 | 0.7159 | 0.0589 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.19 | 0.7162 | 0.0613 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.23 | 0.7163 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.07 | 0.7168 | 0.0590 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.64 | 0.7213 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.45 | 0.7208 | 0.0566 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.50 | 0.7212 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.36 | 0.7177 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.06 | 0.7015 | 0.0720 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.65 | 0.7072 | 0.0632 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.53 | 0.7071 | 0.0674 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.58 | 0.7074 | 0.0653 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.24 | 0.7075 | 0.0648 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.92 | 0.7130 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.74 | 0.7131 | 0.0612 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.83 | 0.7133 | 0.0597 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.86 | 0.7101 | 0.0648 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.81 | 0.7134 | 0.0636 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.29 | 0.7171 | 0.0592 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.18 | 0.7173 | 0.0612 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.22 | 0.7175 | 0.0602 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.00 | 0.7155 | 0.0620 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.35 | 0.7161 | 0.0579 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.25 | 0.7172 | 0.0601 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.25 | 0.7165 | 0.0591 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 254113 | 0.179 | 39.3 | 29.22 | 0.13 | 0.026 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 254113 | 0.179 | 34.1 | 29.22 | 0.13 | 0.026 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 254113 | 0.179 | 38.6 | 29.22 | 0.13 | 0.026 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 254113 | 0.179 | 36.3 | 29.22 | 0.13 | 0.026 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 855 | None | classic | 0.41 | False | 451441 | 0.518 | 89.8 | 32.11 | 0.25 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 855 | None | classic | 0.41 | False | 451441 | 0.518 | 89.3 | 32.11 | 0.25 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 855 | None | classic | 0.41 | False | 451441 | 0.518 | 88.8 | 32.11 | 0.25 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 855 | None | classic | 0.41 | False | 451441 | 0.518 | 86.9 | 32.11 | 0.25 | 0.008 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1349517 | 0.808 | 155.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 264139 | 0.176 | 36.3 | 29.45 | 0.13 | 0.029 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 264139 | 0.176 | 33.5 | 29.45 | 0.13 | 0.029 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 264139 | 0.176 | 36.1 | 29.45 | 0.13 | 0.029 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 264139 | 0.176 | 34.6 | 29.45 | 0.13 | 0.029 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 877 | None | classic | 0.50 | False | 420827 | 0.518 | 92.3 | 30.69 | 0.19 | 0.012 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 877 | None | classic | 0.50 | False | 420827 | 0.518 | 102.0 | 30.69 | 0.19 | 0.012 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 877 | None | classic | 0.50 | False | 420827 | 0.518 | 92.2 | 30.69 | 0.19 | 0.012 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 877 | None | classic | 0.50 | False | 420827 | 0.518 | 90.2 | 30.69 | 0.19 | 0.012 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1701145 | 0.808 | 73.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 244200 | 0.322 | 44.0 | 29.64 | 0.20 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 244200 | 0.322 | 34.5 | 29.64 | 0.20 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 244200 | 0.322 | 29.4 | 29.64 | 0.20 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 244200 | 0.322 | 28.8 | 29.64 | 0.20 | 0.027 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 920 | None | classic | 1.27 | False | 407608 | 0.504 | 82.8 | 28.78 | 0.08 | 0.015 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 920 | None | classic | 1.27 | False | 407608 | 0.504 | 82.4 | 28.78 | 0.08 | 0.015 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 920 | None | classic | 1.27 | False | 407608 | 0.504 | 78.4 | 28.78 | 0.08 | 0.015 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 920 | None | classic | 1.27 | False | 407608 | 0.504 | 85.6 | 28.78 | 0.08 | 0.015 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.793 | 0.019 |
| in035 | mask_ent | 0.677 | 0.019 |
| in035 | mask_grad | 0.486 | 0.019 |
| in035 | r_col | 0.857 | 0.019 |
| in035 | r_warp | 0.917 | 0.019 |

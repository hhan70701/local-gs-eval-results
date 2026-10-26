# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 12.3% | 24.23 / 0.0167 | 19.41 / 0.0395 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 13.0% | 24.26 / 0.0169 | 21.40 / 0.0301 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 12.7% | 24.25 / 0.0169 | 20.84 / 0.0333 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 12.9% | 24.26 / 0.0168 | 21.21 / 0.0310 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 12.6% | 24.21 / 0.0170 | 20.57 / 0.0343 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.4% | 24.33 / 0.0171 | 21.81 / 0.0265 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 13.1% | 24.29 / 0.0174 | 21.63 / 0.0285 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 13.2% | 24.32 / 0.0173 | 21.67 / 0.0271 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 13.8% | 24.38 / 0.0189 | 21.32 / 0.0479 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 16.2% | 24.84 / 0.0183 | 19.57 / 0.0522 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 17.0% | 24.93 / 0.0190 | 21.41 / 0.0398 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 16.8% | 24.88 / 0.0188 | 20.86 / 0.0454 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 16.9% | 24.91 / 0.0188 | 21.17 / 0.0419 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 16.8% | 24.82 / 0.0185 | 20.74 / 0.0429 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 17.5% | 24.94 / 0.0190 | 21.91 / 0.0331 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 17.2% | 24.91 / 0.0187 | 21.79 / 0.0358 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 17.3% | 24.93 / 0.0189 | 21.85 / 0.0336 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 17.4% | 24.91 / 0.0192 | 21.07 / 0.0576 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 9.9% | 23.92 / 0.0140 | 19.83 / 0.0351 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 11.6% | 24.27 / 0.0153 | 21.59 / 0.0312 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 10.5% | 24.02 / 0.0148 | 21.32 / 0.0314 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 10.9% | 24.14 / 0.0151 | 21.59 / 0.0302 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 11.9% | 24.25 / 0.0151 | 20.31 / 0.0379 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 13.3% | 24.57 / 0.0155 | 21.48 / 0.0354 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 12.5% | 24.38 / 0.0158 | 21.40 / 0.0358 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 12.8% | 24.45 / 0.0154 | 21.47 / 0.0359 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.87 / 0.0511 | 24.22 / 0.0909 | 19.96 / 0.0141 | 29.48 / 0.0329 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.07 / 0.0656 | 21.17 / 0.1825 | 18.33 / 0.0179 | 29.25 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.18 / 0.0595 | 23.90 / 0.1233 | 19.16 / 0.0148 | 29.34 / 0.0352 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.95 / 0.0618 | 23.23 / 0.1473 | 18.96 / 0.0158 | 29.34 / 0.0352 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.14 / 0.0605 | 23.85 / 0.1292 | 19.08 / 0.0152 | 29.34 / 0.0352 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.74 / 0.0618 | 21.78 / 0.1464 | 19.00 / 0.0159 | 29.27 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.37 / 0.0571 | 23.80 / 0.1062 | 19.78 / 0.0133 | 29.34 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.25 / 0.0593 | 23.22 / 0.1238 | 19.49 / 0.0145 | 29.33 / 0.0354 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.30 / 0.0580 | 23.48 / 0.1150 | 19.58 / 0.0140 | 29.34 / 0.0351 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.57 / 0.0596 | 24.29 / 0.1364 | 20.16 / 0.0173 | 29.40 / 0.0341 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.56 / 0.0735 | 21.48 / 0.1795 | 18.41 / 0.0194 | 28.88 / 0.0392 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.66 / 0.0647 | 24.44 / 0.1238 | 19.45 / 0.0157 | 29.10 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.43 / 0.0690 | 24.11 / 0.1444 | 19.25 / 0.0171 | 29.06 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.59 / 0.0665 | 24.51 / 0.1304 | 19.41 / 0.0163 | 29.10 / 0.0378 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.41 / 0.0662 | 21.68 / 0.1526 | 18.85 / 0.0169 | 29.17 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.05 / 0.0600 | 23.57 / 0.1143 | 19.59 / 0.0143 | 29.19 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.98 / 0.0628 | 23.09 / 0.1292 | 19.39 / 0.0153 | 29.22 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.99 / 0.0611 | 23.26 / 0.1178 | 19.40 / 0.0148 | 29.21 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.97 / 0.0629 | 24.03 / 0.1399 | 19.76 / 0.0189 | 29.33 / 0.0349 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.56 / 0.0654 | 21.49 / 0.1735 | 19.14 / 0.0171 | 29.37 / 0.0347 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.37 / 0.0619 | 24.26 / 0.1342 | 20.14 / 0.0148 | 29.26 / 0.0352 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.24 / 0.0636 | 23.51 / 0.1472 | 19.86 / 0.0154 | 29.40 / 0.0346 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.37 / 0.0625 | 24.10 / 0.1410 | 20.03 / 0.0151 | 29.34 / 0.0348 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.71 / 0.0649 | 22.00 / 0.1630 | 19.28 / 0.0164 | 29.36 / 0.0353 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.41 / 0.0596 | 24.06 / 0.1196 | 19.94 / 0.0142 | 29.34 / 0.0351 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.30 / 0.0621 | 23.60 / 0.1429 | 19.71 / 0.0150 | 29.38 / 0.0351 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.36 / 0.0607 | 23.94 / 0.1273 | 19.79 / 0.0146 | 29.36 / 0.0350 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.5%） | — | — | 27.87 / 0.0511 | 24.22 / 0.0909 | 29.48 |
| in035 | rife | 6.9% | 9.9% | 26.56 / 0.0654 | 21.49 / 0.1735 | 29.37 |
| in035 | cnw_cnn | 8.9% | 12.3% | 26.07 / 0.0656 | 21.17 / 0.1825 | 29.25 |
| in035 | cnw_f5 | 11.6% | 16.2% | 25.56 / 0.0735 | 21.48 / 0.1795 | 28.88 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.89 / 0.0532 | -1.38 / +0.0185 (core 6.4%) | -1.63 / +0.0168 (core 8.5%) | -2.07 / +0.0274 (core 12.2%) |
| in035 | 2 | 0-3 | 27.96 / 0.0509 | -1.70 / +0.0145 (core 6.4%) | -2.25 / +0.0146 (core 8.5%) | -3.04 / +0.0256 (core 12.2%) |
| in035 | 4 | 3-5 | 28.77 / 0.0491 | -0.85 / +0.0102 (core 4.9%) | -1.52 / +0.0122 (core 6.4%) | -1.84 / +0.0144 (core 7.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.87 / 0.0511 | 24.22 | 29.48 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.07 / 0.0656 | 21.17 | 29.25 | 0/3 |
| in035 | cnw_cnn | oracle | 2.3% | 27.05 / 0.0557 | 22.84 | 29.46 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.18 / 0.0595 | 23.90 | 29.34 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 27.59 / 0.0527 | 24.47 | 29.46 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.95 / 0.0618 | 23.23 | 29.34 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 27.46 / 0.0541 | 24.08 | 29.46 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.14 / 0.0605 | 23.85 | 29.34 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 27.55 / 0.0533 | 24.36 | 29.46 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.74 / 0.0618 | 21.78 | 29.27 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.41 / 0.0534 | 22.67 | 29.47 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.37 / 0.0571 | 23.80 | 29.34 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.79 / 0.0506 | 24.15 | 29.48 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.25 / 0.0593 | 23.22 | 29.33 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.69 / 0.0518 | 23.54 | 29.48 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.30 / 0.0580 | 23.48 | 29.34 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.73 / 0.0512 | 23.80 | 29.48 | 2/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.57 / 0.0596 | 24.29 | 29.40 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.5% | 27.94 / 0.0538 | 25.05 | 29.49 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.56 / 0.0735 | 21.48 | 28.88 | 0/3 |
| in035 | cnw_f5 | oracle | 2.7% | 27.03 / 0.0577 | 23.15 | 29.46 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.66 / 0.0647 | 24.44 | 29.10 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.63 / 0.0542 | 24.95 | 29.47 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.43 / 0.0690 | 24.11 | 29.06 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.52 / 0.0559 | 24.78 | 29.47 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.59 / 0.0665 | 24.51 | 29.10 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.61 / 0.0549 | 24.97 | 29.47 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.41 / 0.0662 | 21.68 | 29.17 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.8% | 27.31 / 0.0546 | 22.72 | 29.47 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.05 / 0.0600 | 23.57 | 29.19 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.8% | 27.70 / 0.0515 | 24.08 | 29.47 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.98 / 0.0628 | 23.09 | 29.22 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.8% | 27.62 / 0.0526 | 23.53 | 29.47 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.99 / 0.0611 | 23.26 | 29.21 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.8% | 27.64 / 0.0520 | 23.71 | 29.47 | 1/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.97 / 0.0629 | 24.03 | 29.33 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.8% | 27.70 / 0.0551 | 25.00 | 29.49 | 0/3 |
| in035 | rife | 不复核 | —% | 26.56 / 0.0654 | 21.49 | 29.37 | 0/3 |
| in035 | rife | oracle | 2.0% | 27.44 / 0.0544 | 23.07 | 29.48 | 0/3 |
| in035 | rife | 不复核 | —% | 27.37 / 0.0619 | 24.26 | 29.26 | 0/3 |
| in035 | rife | oracle | 2.1% | 27.90 / 0.0522 | 24.83 | 29.48 | 1/3 |
| in035 | rife | 不复核 | —% | 27.24 / 0.0636 | 23.51 | 29.40 | 0/3 |
| in035 | rife | oracle | 2.0% | 27.79 / 0.0530 | 24.37 | 29.48 | 0/3 |
| in035 | rife | 不复核 | —% | 27.37 / 0.0625 | 24.10 | 29.34 | 0/3 |
| in035 | rife | oracle | 2.1% | 27.87 / 0.0526 | 24.66 | 29.48 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 26.71 / 0.0649 | 22.00 | 29.36 | 0/3 |
| in035 | rife_mw | oracle | 2.2% | 27.53 / 0.0538 | 23.35 | 29.48 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.41 / 0.0596 | 24.06 | 29.34 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 27.84 / 0.0513 | 24.91 | 29.48 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.30 / 0.0621 | 23.60 | 29.38 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 27.76 / 0.0524 | 24.41 | 29.48 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.36 / 0.0607 | 23.94 | 29.36 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 27.79 / 0.0518 | 24.69 | 29.48 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.87 / 0.0511 | 24.22 / 0.0909 | — |
| in035 | FF | 0（前馈） | 1008×673（63%） | 26.81 | 26.07 / 0.0656 | 21.17 / 0.1825 | 0/3 |
| in035 | 25 | 1.30 s | 1008×673（63%） | 27.62 | 26.95 / 0.0618 | 23.23 / 0.1473 | 0/3 |
| in035 | 50 | 2.60 s | 1008×673（63%） | 27.95 | 27.14 / 0.0605 | 23.85 / 0.1292 | 0/3 |
| in035 | 100 | 5.21 s | 1008×673（63%） | 28.30 | 27.18 / 0.0595 | 23.90 / 0.1233 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.87 / 0.0511 | 24.22 / 0.0909 | 29.48 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.07 / 0.0656 | 21.17 / 0.1825 | 29.25 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.05 / 0.0557 | 22.84 / 0.1218 | 29.46 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 26.95 / 0.0618 | 23.23 / 0.1473 | 29.34 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.46 / 0.0541 | 24.08 / 0.1002 | 29.46 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.14 / 0.0605 | 23.85 / 0.1292 | 29.34 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.55 / 0.0533 | 24.36 / 0.0883 | 29.46 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.18 / 0.0595 | 23.90 / 0.1233 | 29.34 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.59 / 0.0527 | 24.47 / 0.0841 | 29.46 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 26.74 / 0.0618 | 21.78 / 0.1464 | 29.27 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.41 / 0.0534 | 22.67 / 0.1006 | 29.47 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.25 / 0.0593 | 23.22 / 0.1238 | 29.33 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.69 / 0.0518 | 23.54 / 0.0858 | 29.48 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.30 / 0.0580 | 23.48 / 0.1150 | 29.34 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.73 / 0.0512 | 23.80 / 0.0825 | 29.48 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.37 / 0.0571 | 23.80 / 0.1062 | 29.34 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.79 / 0.0506 | 24.15 / 0.0777 | 29.48 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 25.56 / 0.0735 | 21.48 / 0.1795 | 28.88 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.03 / 0.0577 | 23.15 / 0.1193 | 29.46 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.43 / 0.0690 | 24.11 / 0.1444 | 29.06 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.52 / 0.0559 | 24.78 / 0.0960 | 29.47 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.59 / 0.0665 | 24.51 / 0.1304 | 29.10 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.61 / 0.0549 | 24.97 / 0.0882 | 29.47 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.66 / 0.0647 | 24.44 / 0.1238 | 29.10 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.63 / 0.0542 | 24.95 / 0.0853 | 29.47 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.41 / 0.0662 | 21.68 / 0.1526 | 29.17 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.31 / 0.0546 | 22.72 / 0.1040 | 29.47 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.98 / 0.0628 | 23.09 / 0.1292 | 29.22 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.62 / 0.0526 | 23.53 / 0.0885 | 29.47 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.99 / 0.0611 | 23.26 / 0.1178 | 29.21 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.64 / 0.0520 | 23.71 / 0.0825 | 29.47 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.05 / 0.0600 | 23.57 / 0.1143 | 29.19 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.70 / 0.0515 | 24.08 / 0.0816 | 29.47 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.56 / 0.0654 | 21.49 / 0.1735 | 29.37 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.44 / 0.0544 | 23.07 / 0.1168 | 29.48 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.24 / 0.0636 | 23.51 / 0.1472 | 29.40 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.79 / 0.0530 | 24.37 / 0.0978 | 29.48 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.37 / 0.0625 | 24.10 / 0.1410 | 29.34 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.87 / 0.0526 | 24.66 / 0.0955 | 29.48 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.37 / 0.0619 | 24.26 / 0.1342 | 29.26 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.90 / 0.0522 | 24.83 / 0.0906 | 29.48 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.71 / 0.0649 | 22.00 / 0.1630 | 29.36 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.53 / 0.0538 | 23.35 / 0.1070 | 29.48 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.30 / 0.0621 | 23.60 / 0.1429 | 29.38 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.76 / 0.0524 | 24.41 / 0.0926 | 29.48 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.36 / 0.0607 | 23.94 / 0.1273 | 29.36 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.79 / 0.0518 | 24.69 / 0.0826 | 29.48 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.41 / 0.0596 | 24.06 / 0.1196 | 29.34 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.84 / 0.0513 | 24.91 / 0.0788 | 29.48 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.22 / 0.0909 | 19.96 / 0.0141 | 29.48 / 0.0329 | 27.87 / 0.0511 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 5.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.22 | 0.7129 | 0.0909 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 19.48 | 0.6821 | 0.1939 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 23.53 | 0.7369 | 0.1343 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 22.68 | 0.7304 | 0.1592 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 23.49 | 0.7400 | 0.1419 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 21.16 | 0.6769 | 0.1565 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 23.56 | 0.7139 | 0.1130 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 22.75 | 0.7105 | 0.1328 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 23.16 | 0.7141 | 0.1224 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 23.79 | 0.7273 | 0.1475 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 20.26 | 0.6883 | 0.1924 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 23.66 | 0.7399 | 0.1320 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 23.26 | 0.7367 | 0.1562 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 23.74 | 0.7437 | 0.1395 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 21.02 | 0.6771 | 0.1605 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 23.26 | 0.7076 | 0.1189 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 22.58 | 0.7028 | 0.1347 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 22.93 | 0.7062 | 0.1254 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 23.79 | 0.7274 | 0.1475 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 18.54 | 0.6736 | 0.2174 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 21.69 | 0.7355 | 0.1564 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 20.71 | 0.7230 | 0.1805 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 21.36 | 0.7336 | 0.1649 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 19.53 | 0.6617 | 0.1893 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 22.23 | 0.7004 | 0.1392 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 21.34 | 0.6936 | 0.1639 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 21.87 | 0.7003 | 0.1506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.84 | 0.7002 | 0.1218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.47 | 0.7333 | 0.0841 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.08 | 0.7254 | 0.1002 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.36 | 0.7323 | 0.0883 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.67 | 0.6900 | 0.1006 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.15 | 0.7179 | 0.0777 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.54 | 0.7071 | 0.0858 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.80 | 0.7131 | 0.0825 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.05 | 0.7385 | 0.1017 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 23.15 | 0.7064 | 0.1193 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.95 | 0.7397 | 0.0853 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.78 | 0.7337 | 0.0960 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.97 | 0.7388 | 0.0882 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.72 | 0.6920 | 0.1040 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.08 | 0.7168 | 0.0816 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.53 | 0.7053 | 0.0885 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.71 | 0.7098 | 0.0825 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.00 | 0.7371 | 0.1021 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.07 | 0.7118 | 0.1168 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.83 | 0.7486 | 0.0906 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.37 | 0.7399 | 0.0978 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.66 | 0.7446 | 0.0955 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 23.35 | 0.7009 | 0.1070 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.91 | 0.7310 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.41 | 0.7197 | 0.0926 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.69 | 0.7268 | 0.0826 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 21.17 | 0.6870 | 0.1825 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.90 | 0.7382 | 0.1233 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.23 | 0.7291 | 0.1473 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.85 | 0.7399 | 0.1292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.78 | 0.6821 | 0.1464 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.80 | 0.7179 | 0.1062 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.22 | 0.7133 | 0.1238 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.48 | 0.7175 | 0.1150 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.29 | 0.7353 | 0.1364 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 21.48 | 0.6924 | 0.1795 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.44 | 0.7428 | 0.1238 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.11 | 0.7369 | 0.1444 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.51 | 0.7449 | 0.1304 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.68 | 0.6815 | 0.1526 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.57 | 0.7115 | 0.1143 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.09 | 0.7067 | 0.1292 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.26 | 0.7092 | 0.1178 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.03 | 0.7305 | 0.1399 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.49 | 0.6913 | 0.1735 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.26 | 0.7493 | 0.1342 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.51 | 0.7361 | 0.1472 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.10 | 0.7449 | 0.1410 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.00 | 0.6837 | 0.1630 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.06 | 0.7206 | 0.1196 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.60 | 0.7132 | 0.1429 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.94 | 0.7199 | 0.1273 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.96 | 0.6330 | 0.0141 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.90 | 0.2992 | 0.0894 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.08 | 0.3498 | 0.0852 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.03 | 0.3361 | 0.0866 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.06 | 0.3449 | 0.0860 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.41 | 0.3512 | 0.0779 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.55 | 0.3809 | 0.0735 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.45 | 0.3710 | 0.0759 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.48 | 0.3760 | 0.0750 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.52 | 0.3559 | 0.0546 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.82 | 0.3472 | 0.0799 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.04 | 0.3957 | 0.0747 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.96 | 0.3797 | 0.0769 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.00 | 0.3894 | 0.0757 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.21 | 0.3798 | 0.0701 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.39 | 0.4111 | 0.0661 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.29 | 0.3995 | 0.0680 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.34 | 0.4037 | 0.0671 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.00 | 0.3757 | 0.0509 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.93 | 0.3430 | 0.0943 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.17 | 0.3971 | 0.0889 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.07 | 0.3798 | 0.0914 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.11 | 0.3915 | 0.0901 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.02 | 0.3561 | 0.0917 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.22 | 0.3723 | 0.0878 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.12 | 0.3700 | 0.0900 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.16 | 0.3714 | 0.0892 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.39 | 0.5946 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.21 | 0.6334 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.00 | 0.6194 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.13 | 0.6281 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.05 | 0.6293 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.80 | 0.6524 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.54 | 0.6448 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.62 | 0.6482 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.16 | 0.6589 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.44 | 0.5949 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.48 | 0.6388 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.28 | 0.6249 | 0.0171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.44 | 0.6335 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.89 | 0.6235 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.61 | 0.6460 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.42 | 0.6390 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.43 | 0.6401 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.78 | 0.6379 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.17 | 0.6383 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.16 | 0.6774 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.88 | 0.6660 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.04 | 0.6728 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.32 | 0.6349 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.95 | 0.6560 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.73 | 0.6474 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.80 | 0.6513 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.33 | 0.5902 | 0.0179 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.16 | 0.6315 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.96 | 0.6172 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.08 | 0.6263 | 0.0152 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.00 | 0.6274 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.78 | 0.6515 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.49 | 0.6438 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.58 | 0.6475 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.16 | 0.6560 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.41 | 0.5913 | 0.0194 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.45 | 0.6368 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.25 | 0.6224 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.41 | 0.6312 | 0.0163 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.85 | 0.6202 | 0.0169 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.59 | 0.6438 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.39 | 0.6368 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.40 | 0.6381 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.76 | 0.6336 | 0.0189 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.14 | 0.6353 | 0.0171 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.14 | 0.6755 | 0.0148 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.86 | 0.6633 | 0.0154 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.03 | 0.6708 | 0.0151 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.28 | 0.6318 | 0.0164 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.94 | 0.6544 | 0.0142 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.71 | 0.6460 | 0.0150 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.79 | 0.6499 | 0.0146 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 32.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.08 | 0.7572 | 0.0227 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.47 | 0.4425 | 0.2085 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.63 | 0.4764 | 0.1966 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.55 | 0.4747 | 0.2012 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.58 | 0.4775 | 0.1987 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.45 | 0.4274 | 0.1900 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.60 | 0.4519 | 0.1787 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.50 | 0.4548 | 0.1831 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.53 | 0.4538 | 0.1811 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.55 | 0.3449 | 0.1677 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.72 | 0.4832 | 0.1855 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.93 | 0.5193 | 0.1697 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.82 | 0.5128 | 0.1777 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.87 | 0.5177 | 0.1735 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.60 | 0.4753 | 0.1659 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.88 | 0.5027 | 0.1529 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.73 | 0.5038 | 0.1584 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.80 | 0.5033 | 0.1554 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.62 | 0.3862 | 0.1548 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.94 | 0.4345 | 0.2177 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.23 | 0.4689 | 0.2005 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.05 | 0.4615 | 0.2104 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.12 | 0.4670 | 0.2058 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.98 | 0.4378 | 0.2119 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.30 | 0.4624 | 0.1955 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.08 | 0.4598 | 0.2053 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.17 | 0.4614 | 0.2009 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.50 | 0.7400 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.47 | 0.7531 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.22 | 0.7497 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.40 | 0.7521 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.05 | 0.7484 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.76 | 0.7566 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.57 | 0.7553 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.65 | 0.7564 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.80 | 0.7538 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.46 | 0.7367 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.53 | 0.7514 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.30 | 0.7477 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.48 | 0.7504 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.86 | 0.7455 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.58 | 0.7540 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.41 | 0.7526 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.46 | 0.7532 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.42 | 0.7451 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.12 | 0.7494 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.99 | 0.7610 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.79 | 0.7587 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.93 | 0.7604 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.20 | 0.7488 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.77 | 0.7554 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.62 | 0.7541 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.70 | 0.7551 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.56 | 0.7089 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.05 | 0.7326 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.73 | 0.7302 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.01 | 0.7334 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.52 | 0.7236 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.26 | 0.7383 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.25 | 0.7403 | 0.0309 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.25 | 0.7403 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.54 | 0.7129 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 21.91 | 0.6839 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.43 | 0.7111 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.05 | 0.7057 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.29 | 0.7097 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.94 | 0.7064 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.80 | 0.7236 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.77 | 0.7262 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.79 | 0.7259 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.71 | 0.6801 | 0.0537 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.40 | 0.7243 | 0.0392 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.43 | 0.7401 | 0.0376 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.41 | 0.7418 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.59 | 0.7428 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.41 | 0.7179 | 0.0402 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.07 | 0.7298 | 0.0375 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.22 | 0.7318 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.19 | 0.7316 | 0.0376 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 43.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.08 | 0.7173 | 0.0290 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.13 | 0.3648 | 0.3275 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.19 | 0.3876 | 0.3184 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.17 | 0.3865 | 0.3222 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.18 | 0.3886 | 0.3204 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.48 | 0.3561 | 0.2855 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.48 | 0.3670 | 0.2777 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.48 | 0.3696 | 0.2821 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.47 | 0.3683 | 0.2803 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.67 | 0.3081 | 0.1966 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.02 | 0.4077 | 0.3061 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.08 | 0.4333 | 0.2923 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.06 | 0.4298 | 0.2996 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.07 | 0.4330 | 0.2958 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.32 | 0.4142 | 0.2635 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.34 | 0.4227 | 0.2533 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.32 | 0.4270 | 0.2586 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.34 | 0.4247 | 0.2561 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.63 | 0.3655 | 0.1818 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.16 | 0.3733 | 0.3290 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.27 | 0.3995 | 0.3167 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.22 | 0.3943 | 0.3235 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.24 | 0.3985 | 0.3202 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.21 | 0.3811 | 0.3219 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.28 | 0.3889 | 0.3125 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.24 | 0.3934 | 0.3182 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.25 | 0.3913 | 0.3157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.89 | 0.7074 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.66 | 0.7161 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.53 | 0.7142 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.65 | 0.7158 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.24 | 0.7124 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.90 | 0.7180 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.75 | 0.7173 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.82 | 0.7177 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.27 | 0.7212 | 0.0314 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.78 | 0.7053 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.67 | 0.7150 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.56 | 0.7129 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.69 | 0.7146 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.11 | 0.7110 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.77 | 0.7162 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.65 | 0.7158 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.67 | 0.7158 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.83 | 0.7151 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.35 | 0.7132 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.13 | 0.7216 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.96 | 0.7198 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.08 | 0.7211 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.40 | 0.7133 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.96 | 0.7179 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.82 | 0.7170 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.88 | 0.7176 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.43 | 0.6909 | 0.0421 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.01 | 0.7064 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.75 | 0.7052 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.02 | 0.7072 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.28 | 0.6995 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.28 | 0.7081 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.11 | 0.7092 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.17 | 0.7089 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.80 | 0.7137 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.69 | 0.6716 | 0.0483 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.16 | 0.6902 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.89 | 0.6866 | 0.0443 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.10 | 0.6896 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.79 | 0.6906 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.79 | 0.6985 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.69 | 0.7009 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.70 | 0.6999 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.74 | 0.6954 | 0.0395 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.97 | 0.6992 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.30 | 0.7134 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.04 | 0.7116 | 0.0400 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.27 | 0.7135 | 0.0389 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.09 | 0.6987 | 0.0413 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.25 | 0.7065 | 0.0362 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.06 | 0.7071 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.16 | 0.7070 | 0.0374 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 77.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.48 | 0.7042 | 0.0329 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.54 | 0.2874 | 0.3503 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.58 | 0.2915 | 0.3443 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.56 | 0.2928 | 0.3471 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.57 | 0.2925 | 0.3457 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.61 | 0.2381 | 0.3225 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.57 | 0.2401 | 0.3180 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.60 | 0.2421 | 0.3209 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.58 | 0.2413 | 0.3197 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.41 | 0.1390 | 0.2528 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.08 | 0.3238 | 0.3295 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.10 | 0.3284 | 0.3193 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.09 | 0.3308 | 0.3251 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.10 | 0.3302 | 0.3222 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.02 | 0.2805 | 0.3016 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.01 | 0.2809 | 0.2949 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.01 | 0.2845 | 0.2992 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.01 | 0.2828 | 0.2972 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.76 | 0.1936 | 0.2386 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.63 | 0.2921 | 0.3487 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.67 | 0.2988 | 0.3406 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.64 | 0.2981 | 0.3450 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.66 | 0.2988 | 0.3429 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.65 | 0.2950 | 0.3434 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.67 | 0.2957 | 0.3390 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.66 | 0.2995 | 0.3412 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.66 | 0.2978 | 0.3402 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.46 | 0.7039 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.46 | 0.7040 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.46 | 0.7040 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.46 | 0.7040 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.47 | 0.7041 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.48 | 0.7042 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.48 | 0.7042 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.48 | 0.7042 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.49 | 0.7043 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.46 | 0.7040 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.47 | 0.7041 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.47 | 0.7041 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.47 | 0.7041 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.47 | 0.7041 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.47 | 0.7041 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.47 | 0.7042 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.47 | 0.7041 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.49 | 0.7044 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.48 | 0.7042 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.48 | 0.7042 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.48 | 0.7042 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.48 | 0.7042 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.48 | 0.7042 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.48 | 0.7043 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.48 | 0.7043 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.48 | 0.7043 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.25 | 0.7020 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.34 | 0.7030 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.34 | 0.7033 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.34 | 0.7032 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.27 | 0.7017 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.34 | 0.7029 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.33 | 0.7030 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.34 | 0.7030 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.40 | 0.7053 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.88 | 0.6992 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.10 | 0.7014 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.06 | 0.7014 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.10 | 0.7017 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.17 | 0.7010 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.19 | 0.7020 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.22 | 0.7026 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.21 | 0.7024 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.33 | 0.7048 | 0.0349 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.37 | 0.7032 | 0.0347 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.26 | 0.7034 | 0.0352 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.40 | 0.7040 | 0.0346 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.34 | 0.7037 | 0.0348 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.36 | 0.7031 | 0.0353 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.34 | 0.7031 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.38 | 0.7037 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.36 | 0.7035 | 0.0350 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.87 | 0.7099 | 0.0511 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.17 | 0.3108 | 0.4168 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.22 | 0.3237 | 0.4048 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.19 | 0.3233 | 0.4110 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.20 | 0.3243 | 0.4081 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.14 | 0.2759 | 0.3886 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.12 | 0.2823 | 0.3777 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.13 | 0.2841 | 0.3839 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.12 | 0.2833 | 0.3809 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.74 | 0.1997 | 0.3364 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.79 | 0.3485 | 0.3935 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.83 | 0.3621 | 0.3748 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.81 | 0.3615 | 0.3859 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.82 | 0.3626 | 0.3804 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.63 | 0.3210 | 0.3619 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.64 | 0.3262 | 0.3472 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.63 | 0.3292 | 0.3557 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.63 | 0.3276 | 0.3519 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.21 | 0.2507 | 0.3124 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.20 | 0.3159 | 0.4169 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.26 | 0.3304 | 0.4017 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.23 | 0.3280 | 0.4107 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.24 | 0.3301 | 0.4062 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.23 | 0.3216 | 0.4074 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.26 | 0.3257 | 0.3953 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.24 | 0.3291 | 0.4026 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.25 | 0.3276 | 0.3992 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.05 | 0.7049 | 0.0557 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.59 | 0.7092 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.46 | 0.7080 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.55 | 0.7088 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.41 | 0.7077 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.79 | 0.7103 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.69 | 0.7099 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.73 | 0.7102 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.94 | 0.7115 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.03 | 0.7040 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.63 | 0.7087 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.52 | 0.7076 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.61 | 0.7084 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.31 | 0.7069 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.70 | 0.7095 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.62 | 0.7092 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.64 | 0.7092 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.70 | 0.7088 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.44 | 0.7082 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.90 | 0.7119 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.79 | 0.7111 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.87 | 0.7117 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.53 | 0.7083 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.84 | 0.7106 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.76 | 0.7101 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.79 | 0.7104 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.07 | 0.6968 | 0.0656 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.18 | 0.7045 | 0.0595 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.95 | 0.7035 | 0.0618 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.14 | 0.7045 | 0.0605 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.74 | 0.7013 | 0.0618 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.37 | 0.7057 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.25 | 0.7061 | 0.0593 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.30 | 0.7061 | 0.0580 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.57 | 0.7085 | 0.0596 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.56 | 0.6872 | 0.0735 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.66 | 0.6968 | 0.0647 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.43 | 0.6948 | 0.0690 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.59 | 0.6963 | 0.0665 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.41 | 0.6968 | 0.0662 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.05 | 0.7013 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.98 | 0.7023 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.99 | 0.7019 | 0.0611 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.97 | 0.7001 | 0.0629 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.56 | 0.7015 | 0.0654 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.37 | 0.7079 | 0.0619 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.24 | 0.7072 | 0.0636 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.37 | 0.7080 | 0.0625 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.71 | 0.7018 | 0.0649 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.41 | 0.7056 | 0.0596 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.30 | 0.7059 | 0.0621 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.36 | 0.7059 | 0.0607 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 300385 | 0.327 | 79.2 | 29.13 | 0.30 | 0.035 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 300385 | 0.327 | 78.5 | 29.13 | 0.30 | 0.035 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 300385 | 0.327 | 53.7 | 29.13 | 0.30 | 0.035 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 300385 | 0.327 | 77.4 | 29.13 | 0.30 | 0.035 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 817 | None | classic | 0.30 | False | 457831 | 0.990 | 181.4 | 30.01 | 0.34 | 0.018 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 817 | None | classic | 0.30 | False | 457831 | 0.990 | 197.1 | 30.01 | 0.34 | 0.018 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 817 | None | classic | 0.30 | False | 457831 | 0.990 | 184.8 | 30.01 | 0.34 | 0.018 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 817 | None | classic | 0.30 | False | 457831 | 0.990 | 168.0 | 30.01 | 0.34 | 0.018 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1176033 | 0.806 | 465.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 297019 | 0.324 | 62.0 | 29.18 | 0.25 | 0.032 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 297019 | 0.324 | 57.8 | 29.18 | 0.25 | 0.032 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 297019 | 0.324 | 56.6 | 29.18 | 0.25 | 0.032 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 297019 | 0.324 | 60.6 | 29.18 | 0.25 | 0.032 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 819 | None | classic | 0.43 | False | 429413 | 0.989 | 187.6 | 30.93 | 0.07 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 819 | None | classic | 0.43 | False | 429413 | 0.989 | 186.1 | 30.93 | 0.07 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 819 | None | classic | 0.43 | False | 429413 | 0.989 | 194.5 | 30.93 | 0.07 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 819 | None | classic | 0.43 | False | 429413 | 0.989 | 163.5 | 30.93 | 0.07 | 0.009 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1565306 | 0.806 | 105.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 280468 | 0.916 | 81.3 | 30.05 | 0.28 | 0.024 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 280468 | 0.916 | 90.3 | 30.05 | 0.28 | 0.024 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 280468 | 0.916 | 117.8 | 30.05 | 0.28 | 0.024 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 280468 | 0.916 | 85.0 | 30.05 | 0.28 | 0.024 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 883 | None | classic | 1.17 | False | 414073 | 0.988 | 154.9 | 29.21 | 0.24 | 0.014 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 883 | None | classic | 1.17 | False | 414073 | 0.988 | 161.9 | 29.21 | 0.24 | 0.014 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 883 | None | classic | 1.17 | False | 414073 | 0.988 | 156.5 | 29.21 | 0.24 | 0.014 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 883 | None | classic | 1.17 | False | 414073 | 0.988 | 168.1 | 29.21 | 0.24 | 0.014 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.750 | 0.018 |
| in035 | mask_ent | 0.690 | 0.018 |
| in035 | mask_grad | 0.491 | 0.018 |
| in035 | r_col | 0.851 | 0.018 |
| in035 | r_warp | 0.882 | 0.018 |

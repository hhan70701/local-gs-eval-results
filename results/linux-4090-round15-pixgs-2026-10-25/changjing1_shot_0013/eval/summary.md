# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 13.0% | 24.28 / 0.0146 | 20.50 / 0.0381 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 13.4% | 24.38 / 0.0147 | 21.45 / 0.0307 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 13.0% | 24.27 / 0.0147 | 20.96 / 0.0342 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 13.1% | 24.33 / 0.0144 | 21.12 / 0.0321 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 12.7% | 24.41 / 0.0140 | 20.99 / 0.0335 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.4% | 24.52 / 0.0148 | 22.24 / 0.0279 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 13.0% | 24.45 / 0.0145 | 21.81 / 0.0297 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 13.1% | 24.47 / 0.0146 | 21.98 / 0.0285 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 13.9% | 24.67 / 0.0170 | 21.99 / 0.0471 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 19.3% | 25.02 / 0.0191 | 20.60 / 0.0544 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 20.1% | 25.08 / 0.0193 | 21.69 / 0.0469 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 19.5% | 25.05 / 0.0190 | 21.41 / 0.0500 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 19.7% | 25.05 / 0.0191 | 21.54 / 0.0482 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 19.4% | 25.02 / 0.0191 | 22.12 / 0.0464 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 20.3% | 25.14 / 0.0196 | 23.37 / 0.0371 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 19.7% | 25.07 / 0.0195 | 23.26 / 0.0403 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 19.8% | 25.08 / 0.0196 | 23.40 / 0.0380 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 19.9% | 25.20 / 0.0202 | 21.83 / 0.0647 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 10.3% | 24.21 / 0.0198 | 21.07 / 0.0474 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 12.2% | 24.60 / 0.0209 | 21.91 / 0.0440 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 11.1% | 24.41 / 0.0201 | 21.78 / 0.0450 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 11.5% | 24.47 / 0.0207 | 21.87 / 0.0443 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 12.0% | 24.43 / 0.0218 | 21.52 / 0.0535 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 13.4% | 24.68 / 0.0218 | 22.65 / 0.0458 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 12.9% | 24.55 / 0.0220 | 22.27 / 0.0500 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 13.1% | 24.59 / 0.0219 | 22.50 / 0.0480 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.02 / 0.0578 | 24.52 / 0.0754 | 19.50 / 0.0172 | 29.74 / 0.0344 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.81 / 0.0771 | 24.61 / 0.1379 | 18.68 / 0.0226 | 29.33 / 0.0381 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.37 / 0.0713 | 26.74 / 0.1080 | 19.17 / 0.0204 | 29.57 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.13 / 0.0740 | 25.89 / 0.1200 | 18.92 / 0.0216 | 29.47 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.23 / 0.0728 | 26.47 / 0.1140 | 19.00 / 0.0211 | 29.53 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.25 / 0.0738 | 23.17 / 0.1387 | 19.20 / 0.0218 | 29.49 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.94 / 0.0668 | 26.58 / 0.0968 | 20.31 / 0.0180 | 29.60 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.61 / 0.0708 | 24.64 / 0.1177 | 19.62 / 0.0202 | 29.56 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.73 / 0.0692 | 25.57 / 0.1066 | 19.92 / 0.0194 | 29.56 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.63 / 0.0714 | 25.15 / 0.1562 | 19.53 / 0.0233 | 29.68 / 0.0358 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.10 / 0.0895 | 25.69 / 0.1474 | 18.33 / 0.0251 | 28.96 / 0.0442 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.88 / 0.0803 | 27.32 / 0.1102 | 19.02 / 0.0224 | 29.35 / 0.0407 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.64 / 0.0855 | 27.06 / 0.1274 | 18.72 / 0.0240 | 29.23 / 0.0423 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.73 / 0.0829 | 27.22 / 0.1209 | 18.81 / 0.0234 | 29.29 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.21 / 0.0819 | 23.85 / 0.1470 | 19.76 / 0.0215 | 29.38 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.15 / 0.0707 | 27.36 / 0.1067 | 21.07 / 0.0168 | 29.62 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.83 / 0.0772 | 25.14 / 0.1238 | 20.41 / 0.0188 | 29.56 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.96 / 0.0743 | 26.08 / 0.1149 | 20.71 / 0.0179 | 29.58 / 0.0396 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.22 / 0.0771 | 24.92 / 0.1654 | 19.40 / 0.0247 | 29.59 / 0.0379 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.28 / 0.0775 | 23.81 / 0.1421 | 19.26 / 0.0208 | 29.63 / 0.0380 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.63 / 0.0736 | 25.07 / 0.1248 | 19.76 / 0.0179 | 29.56 / 0.0389 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.56 / 0.0752 | 24.66 / 0.1321 | 19.50 / 0.0194 | 29.63 / 0.0385 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.60 / 0.0741 | 24.89 / 0.1298 | 19.62 / 0.0186 | 29.60 / 0.0387 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.42 / 0.0767 | 22.70 / 0.1527 | 19.62 / 0.0195 | 29.42 / 0.0393 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.03 / 0.0707 | 24.71 / 0.1360 | 20.47 / 0.0164 | 29.62 / 0.0385 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.70 / 0.0751 | 23.53 / 0.1468 | 19.86 / 0.0184 | 29.44 / 0.0398 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.81 / 0.0738 | 24.15 / 0.1417 | 20.14 / 0.0175 | 29.46 / 0.0397 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.5%） | — | — | 28.02 / 0.0578 | 24.52 / 0.0754 | 29.74 |
| in035 | rife | 6.2% | 10.3% | 27.28 / 0.0775 | 23.81 / 0.1421 | 29.63 |
| in035 | cnw_cnn | 8.4% | 13.0% | 26.81 / 0.0771 | 24.61 / 0.1379 | 29.33 |
| in035 | cnw_f5 | 11.7% | 19.3% | 26.10 / 0.0895 | 25.69 / 0.1474 | 28.96 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.77 / 0.0623 | -0.47 / +0.0206 (core 4.0%) | -0.57 / +0.0203 (core 8.1%) | -1.39 / +0.0347 (core 11.6%) |
| in035 | 2 | 0-3 | 28.34 / 0.0530 | -1.20 / +0.0248 (core 4.0%) | -1.77 / +0.0231 (core 8.1%) | -2.99 / +0.0395 (core 11.6%) |
| in035 | 4 | 3-5 | 28.94 / 0.0581 | -0.54 / +0.0136 (core 6.2%) | -1.27 / +0.0144 (core 5.7%) | -1.37 / +0.0207 (core 8.2%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.02 / 0.0578 | 24.52 | 29.74 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.81 / 0.0771 | 24.61 | 29.33 | 0/3 |
| in035 | cnw_cnn | oracle | 2.6% | 27.57 / 0.0651 | 24.97 | 29.72 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.37 / 0.0713 | 26.74 | 29.57 | 0/3 |
| in035 | cnw_cnn | oracle | 2.6% | 27.83 / 0.0621 | 26.83 | 29.73 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.13 / 0.0740 | 25.89 | 29.47 | 0/3 |
| in035 | cnw_cnn | oracle | 2.6% | 27.69 / 0.0636 | 26.00 | 29.72 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.23 / 0.0728 | 26.47 | 29.53 | 0/3 |
| in035 | cnw_cnn | oracle | 2.6% | 27.74 / 0.0630 | 26.54 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.25 / 0.0738 | 23.17 | 29.49 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 27.79 / 0.0639 | 23.67 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.94 / 0.0668 | 26.58 | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 28.27 / 0.0597 | 26.89 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.61 / 0.0708 | 24.64 | 29.56 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 27.99 / 0.0619 | 24.95 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.73 / 0.0692 | 25.57 | 29.56 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 28.11 / 0.0609 | 25.88 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.63 / 0.0714 | 25.15 | 29.68 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.6% | 27.94 / 0.0638 | 26.15 | 29.74 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.10 / 0.0895 | 25.69 | 28.96 | 0/3 |
| in035 | cnw_f5 | oracle | 3.3% | 27.29 / 0.0682 | 26.11 | 29.68 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.88 / 0.0803 | 27.32 | 29.35 | 0/3 |
| in035 | cnw_f5 | oracle | 3.4% | 27.69 / 0.0644 | 27.17 | 29.71 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.64 / 0.0855 | 27.06 | 29.23 | 0/3 |
| in035 | cnw_f5 | oracle | 3.3% | 27.53 / 0.0663 | 27.03 | 29.69 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.73 / 0.0829 | 27.22 | 29.29 | 0/3 |
| in035 | cnw_f5 | oracle | 3.3% | 27.58 / 0.0654 | 27.08 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.21 / 0.0819 | 23.85 | 29.38 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.3% | 27.98 / 0.0647 | 24.34 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.15 / 0.0707 | 27.36 | 29.62 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.3% | 28.53 / 0.0595 | 27.50 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.83 / 0.0772 | 25.14 | 29.56 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.3% | 28.28 / 0.0617 | 25.43 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.96 / 0.0743 | 26.08 | 29.58 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.3% | 28.40 / 0.0607 | 26.31 | 29.73 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.22 / 0.0771 | 24.92 | 29.59 | 0/3 |
| in035 | cnw_f5_pix | oracle | 3.3% | 27.82 / 0.0652 | 26.14 | 29.73 | 0/3 |
| in035 | rife | 不复核 | —% | 27.28 / 0.0775 | 23.81 | 29.63 | 0/3 |
| in035 | rife | oracle | 1.9% | 27.85 / 0.0635 | 24.66 | 29.73 | 0/3 |
| in035 | rife | 不复核 | —% | 27.63 / 0.0736 | 25.07 | 29.56 | 0/3 |
| in035 | rife | oracle | 2.0% | 28.09 / 0.0602 | 25.51 | 29.74 | 0/3 |
| in035 | rife | 不复核 | —% | 27.56 / 0.0752 | 24.66 | 29.63 | 0/3 |
| in035 | rife | oracle | 1.9% | 27.98 / 0.0618 | 25.18 | 29.73 | 0/3 |
| in035 | rife | 不复核 | —% | 27.60 / 0.0741 | 24.89 | 29.60 | 0/3 |
| in035 | rife | oracle | 1.9% | 28.03 / 0.0609 | 25.34 | 29.74 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.42 / 0.0767 | 22.70 | 29.42 | 0/3 |
| in035 | rife_mw | oracle | 2.2% | 28.00 / 0.0614 | 23.63 | 29.73 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.03 / 0.0707 | 24.71 | 29.62 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 28.36 / 0.0587 | 25.79 | 29.74 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.70 / 0.0751 | 23.53 | 29.44 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 28.13 / 0.0605 | 24.41 | 29.74 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.81 / 0.0738 | 24.15 | 29.46 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 28.24 / 0.0599 | 25.14 | 29.74 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.02 / 0.0578 | 24.52 / 0.0754 | — |
| in035 | FF | 0（前馈） | 1008×682（66%） | 26.56 | 26.81 / 0.0771 | 24.61 / 0.1379 | 0/3 |
| in035 | 25 | 0.62 s | 1008×682（66%） | 27.32 | 27.13 / 0.0740 | 25.89 / 0.1200 | 0/3 |
| in035 | 50 | 1.22 s | 1008×682（66%） | 27.68 | 27.23 / 0.0728 | 26.47 / 0.1140 | 0/3 |
| in035 | 100 | 2.42 s | 1008×682（66%） | 28.10 | 27.37 / 0.0713 | 26.74 / 0.1080 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.02 / 0.0578 | 24.52 / 0.0754 | 29.74 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.81 / 0.0771 | 24.61 / 0.1379 | 29.33 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.57 / 0.0651 | 24.97 / 0.1033 | 29.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.13 / 0.0740 | 25.89 / 0.1200 | 29.47 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.69 / 0.0636 | 26.00 / 0.0925 | 29.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.23 / 0.0728 | 26.47 / 0.1140 | 29.53 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.74 / 0.0630 | 26.54 / 0.0893 | 29.73 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.37 / 0.0713 | 26.74 / 0.1080 | 29.57 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.83 / 0.0621 | 26.83 / 0.0858 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.25 / 0.0738 | 23.17 / 0.1387 | 29.49 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.79 / 0.0639 | 23.67 / 0.1050 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.61 / 0.0708 | 24.64 / 0.1177 | 29.56 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.99 / 0.0619 | 24.95 / 0.0891 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.73 / 0.0692 | 25.57 / 0.1066 | 29.56 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.11 / 0.0609 | 25.88 / 0.0814 | 29.72 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.94 / 0.0668 | 26.58 / 0.0968 | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.27 / 0.0597 | 26.89 / 0.0759 | 29.73 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.10 / 0.0895 | 25.69 / 0.1474 | 28.96 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.29 / 0.0682 | 26.11 / 0.1003 | 29.68 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.64 / 0.0855 | 27.06 / 0.1274 | 29.23 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.53 / 0.0663 | 27.03 / 0.0903 | 29.69 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.73 / 0.0829 | 27.22 / 0.1209 | 29.29 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.58 / 0.0654 | 27.08 / 0.0896 | 29.70 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.88 / 0.0803 | 27.32 / 0.1102 | 29.35 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.69 / 0.0644 | 27.17 / 0.0811 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.21 / 0.0819 | 23.85 / 0.1470 | 29.38 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.98 / 0.0647 | 24.34 / 0.1006 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.83 / 0.0772 | 25.14 / 0.1238 | 29.56 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.28 / 0.0617 | 25.43 / 0.0828 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.96 / 0.0743 | 26.08 / 0.1149 | 29.58 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.40 / 0.0607 | 26.31 / 0.0808 | 29.73 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.15 / 0.0707 | 27.36 / 0.1067 | 29.62 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.53 / 0.0595 | 27.50 / 0.0772 | 29.73 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.28 / 0.0775 | 23.81 / 0.1421 | 29.63 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.85 / 0.0635 | 24.66 / 0.1000 | 29.73 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.56 / 0.0752 | 24.66 / 0.1321 | 29.63 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.98 / 0.0618 | 25.18 / 0.0932 | 29.73 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.60 / 0.0741 | 24.89 / 0.1298 | 29.60 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.03 / 0.0609 | 25.34 / 0.0921 | 29.74 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.63 / 0.0736 | 25.07 / 0.1248 | 29.56 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.09 / 0.0602 | 25.51 / 0.0896 | 29.74 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.42 / 0.0767 | 22.70 / 0.1527 | 29.42 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.00 / 0.0614 | 23.63 / 0.1035 | 29.73 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.70 / 0.0751 | 23.53 / 0.1468 | 29.44 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.13 / 0.0605 | 24.41 / 0.1010 | 29.74 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.81 / 0.0738 | 24.15 / 0.1417 | 29.46 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.24 / 0.0599 | 25.14 / 0.0966 | 29.74 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.03 / 0.0707 | 24.71 / 0.1360 | 29.62 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.36 / 0.0587 | 25.79 / 0.0917 | 29.74 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.52 / 0.0754 | 19.50 / 0.0172 | 29.74 / 0.0344 | 28.02 / 0.0578 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.52 | 0.7276 | 0.0754 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 21.09 | 0.7591 | 0.1989 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 22.14 | 0.7949 | 0.1585 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 21.57 | 0.7896 | 0.1762 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 21.85 | 0.7960 | 0.1677 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 20.05 | 0.7172 | 0.1974 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 21.72 | 0.7681 | 0.1440 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 20.50 | 0.7448 | 0.1753 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 21.06 | 0.7575 | 0.1582 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 22.76 | 0.7547 | 0.2093 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 24.88 | 0.7916 | 0.1669 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 25.93 | 0.8315 | 0.1322 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 26.12 | 0.8229 | 0.1490 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 26.03 | 0.8298 | 0.1433 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 23.62 | 0.7572 | 0.1641 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 26.85 | 0.8191 | 0.1185 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 24.73 | 0.7891 | 0.1424 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 25.56 | 0.8043 | 0.1323 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 24.09 | 0.7781 | 0.1837 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 20.19 | 0.7212 | 0.2181 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 23.14 | 0.7773 | 0.1696 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 21.73 | 0.7581 | 0.1975 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 22.53 | 0.7706 | 0.1841 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 19.35 | 0.6852 | 0.2116 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 21.51 | 0.7506 | 0.1697 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 20.41 | 0.7217 | 0.1929 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 21.10 | 0.7390 | 0.1805 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.97 | 0.7788 | 0.1033 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.83 | 0.8039 | 0.0858 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.00 | 0.7952 | 0.0925 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.54 | 0.8012 | 0.0893 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.67 | 0.7522 | 0.1050 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.89 | 0.7925 | 0.0759 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.95 | 0.7673 | 0.0891 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.88 | 0.7793 | 0.0814 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.15 | 0.7895 | 0.0981 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.11 | 0.7922 | 0.1003 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.17 | 0.8176 | 0.0811 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.03 | 0.8087 | 0.0903 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.08 | 0.8141 | 0.0896 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.34 | 0.7690 | 0.1006 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.50 | 0.8122 | 0.0772 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.43 | 0.7896 | 0.0828 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.31 | 0.8009 | 0.0808 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.14 | 0.7904 | 0.1011 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.66 | 0.7364 | 0.1000 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.51 | 0.7603 | 0.0896 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.18 | 0.7471 | 0.0932 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.34 | 0.7535 | 0.0921 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 23.63 | 0.7343 | 0.1035 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.79 | 0.7747 | 0.0917 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.41 | 0.7514 | 0.1010 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.14 | 0.7644 | 0.0966 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.61 | 0.7774 | 0.1379 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.74 | 0.8099 | 0.1080 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.89 | 0.8032 | 0.1200 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.47 | 0.8091 | 0.1140 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.17 | 0.7438 | 0.1387 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.58 | 0.7913 | 0.0968 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.64 | 0.7671 | 0.1177 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.57 | 0.7797 | 0.1066 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.15 | 0.7820 | 0.1562 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.69 | 0.7951 | 0.1474 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.32 | 0.8326 | 0.1102 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.06 | 0.8226 | 0.1274 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.22 | 0.8300 | 0.1209 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.85 | 0.7631 | 0.1470 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.36 | 0.8194 | 0.1067 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.14 | 0.7932 | 0.1238 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.08 | 0.8069 | 0.1149 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.92 | 0.7811 | 0.1654 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.81 | 0.7249 | 0.1421 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.07 | 0.7631 | 0.1248 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.66 | 0.7455 | 0.1321 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.89 | 0.7545 | 0.1298 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.70 | 0.7121 | 0.1527 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.71 | 0.7584 | 0.1360 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.53 | 0.7357 | 0.1468 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.15 | 0.7481 | 0.1417 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.50 | 0.5831 | 0.0172 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.60 | 0.3597 | 0.1029 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.77 | 0.4044 | 0.0984 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.66 | 0.3869 | 0.1012 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.71 | 0.3972 | 0.0999 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.72 | 0.4005 | 0.1010 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.95 | 0.4616 | 0.0935 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.80 | 0.4307 | 0.0977 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.87 | 0.4451 | 0.0961 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.50 | 0.3847 | 0.0641 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.79 | 0.4261 | 0.0771 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.17 | 0.4978 | 0.0714 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.94 | 0.4693 | 0.0750 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.04 | 0.4852 | 0.0737 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.98 | 0.5089 | 0.0732 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.36 | 0.5808 | 0.0644 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 10.15 | 0.5470 | 0.0691 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.24 | 0.5645 | 0.0672 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.86 | 0.4674 | 0.0519 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.29 | 0.3835 | 0.1099 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.51 | 0.4410 | 0.1030 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.38 | 0.4219 | 0.1073 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.43 | 0.4343 | 0.1055 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.29 | 0.3990 | 0.1072 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.47 | 0.4585 | 0.1022 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.34 | 0.4248 | 0.1058 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.39 | 0.4408 | 0.1046 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.73 | 0.6066 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.20 | 0.6397 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.94 | 0.6268 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.03 | 0.6335 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.21 | 0.6250 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.33 | 0.6649 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.64 | 0.6417 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.94 | 0.6517 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.55 | 0.6271 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.35 | 0.5892 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.04 | 0.6423 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.74 | 0.6203 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.83 | 0.6322 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.77 | 0.6556 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.07 | 0.7151 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.43 | 0.6889 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.72 | 0.7031 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.41 | 0.6203 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.28 | 0.6058 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.76 | 0.6427 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.50 | 0.6269 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.62 | 0.6370 | 0.0184 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.63 | 0.6249 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.47 | 0.6720 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.86 | 0.6454 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.14 | 0.6588 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.68 | 0.6027 | 0.0226 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.17 | 0.6375 | 0.0204 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.92 | 0.6243 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.00 | 0.6312 | 0.0211 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.20 | 0.6232 | 0.0218 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.31 | 0.6650 | 0.0180 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.62 | 0.6410 | 0.0202 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.92 | 0.6513 | 0.0194 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.53 | 0.6237 | 0.0233 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.33 | 0.5857 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.02 | 0.6398 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.72 | 0.6174 | 0.0240 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.81 | 0.6297 | 0.0234 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.76 | 0.6536 | 0.0215 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.07 | 0.7148 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.41 | 0.6878 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.71 | 0.7024 | 0.0179 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.40 | 0.6160 | 0.0247 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.26 | 0.6046 | 0.0208 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.76 | 0.6422 | 0.0179 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.50 | 0.6266 | 0.0194 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.62 | 0.6365 | 0.0186 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.62 | 0.6237 | 0.0195 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.47 | 0.6714 | 0.0164 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.86 | 0.6449 | 0.0184 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.14 | 0.6582 | 0.0175 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.37 | 0.7729 | 0.0297 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.35 | 0.5203 | 0.2521 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.56 | 0.5387 | 0.2376 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.43 | 0.5373 | 0.2451 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.48 | 0.5391 | 0.2415 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.37 | 0.5341 | 0.2469 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.68 | 0.5640 | 0.2292 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.46 | 0.5588 | 0.2386 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.54 | 0.5620 | 0.2345 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.40 | 0.4329 | 0.2015 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.65 | 0.5763 | 0.2118 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.99 | 0.6047 | 0.1933 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.76 | 0.5990 | 0.2035 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.85 | 0.6028 | 0.1988 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.75 | 0.6165 | 0.2034 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.22 | 0.6535 | 0.1803 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.90 | 0.6468 | 0.1930 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.02 | 0.6505 | 0.1877 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.92 | 0.5097 | 0.1772 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.80 | 0.5194 | 0.2614 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.01 | 0.5449 | 0.2444 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.88 | 0.5404 | 0.2539 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.93 | 0.5434 | 0.2496 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.76 | 0.5222 | 0.2570 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.94 | 0.5461 | 0.2426 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.80 | 0.5433 | 0.2506 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.85 | 0.5452 | 0.2474 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.47 | 0.7711 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.85 | 0.7792 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.65 | 0.7763 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.72 | 0.7777 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.80 | 0.7744 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.59 | 0.7831 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.13 | 0.7784 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.34 | 0.7803 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.90 | 0.7751 | 0.0387 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.07 | 0.7653 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.64 | 0.7769 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.44 | 0.7727 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.50 | 0.7748 | 0.0380 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.14 | 0.7790 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.06 | 0.7929 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.67 | 0.7880 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.84 | 0.7904 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.68 | 0.7714 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.98 | 0.7740 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.38 | 0.7822 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.19 | 0.7792 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.28 | 0.7810 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.17 | 0.7763 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.80 | 0.7865 | 0.0314 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.42 | 0.7818 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.60 | 0.7841 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.88 | 0.7491 | 0.0500 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.53 | 0.7607 | 0.0437 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.26 | 0.7578 | 0.0468 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.34 | 0.7592 | 0.0453 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.31 | 0.7552 | 0.0470 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.11 | 0.7693 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.85 | 0.7657 | 0.0435 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.95 | 0.7671 | 0.0423 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.09 | 0.7430 | 0.0611 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.01 | 0.7280 | 0.0595 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.75 | 0.7457 | 0.0529 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.61 | 0.7416 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.68 | 0.7441 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.27 | 0.7551 | 0.0527 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.32 | 0.7799 | 0.0441 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.11 | 0.7739 | 0.0480 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.17 | 0.7768 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.28 | 0.7178 | 0.0727 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.70 | 0.7572 | 0.0513 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.11 | 0.7696 | 0.0471 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.15 | 0.7682 | 0.0486 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.19 | 0.7701 | 0.0475 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.85 | 0.7567 | 0.0508 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.39 | 0.7722 | 0.0470 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.31 | 0.7694 | 0.0488 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.42 | 0.7714 | 0.0476 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 44.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.07 | 0.7193 | 0.0353 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.60 | 0.3934 | 0.3593 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.71 | 0.4115 | 0.3469 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.66 | 0.4088 | 0.3541 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.68 | 0.4106 | 0.3511 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.63 | 0.4112 | 0.3527 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.74 | 0.4363 | 0.3365 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.66 | 0.4307 | 0.3460 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.70 | 0.4335 | 0.3420 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.51 | 0.3573 | 0.2184 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.41 | 0.4708 | 0.3143 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.54 | 0.4963 | 0.2987 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.47 | 0.4917 | 0.3079 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.50 | 0.4946 | 0.3039 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.44 | 0.5080 | 0.3053 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.71 | 0.5413 | 0.2844 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.53 | 0.5339 | 0.2972 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.60 | 0.5381 | 0.2919 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.29 | 0.4659 | 0.1904 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.22 | 0.3865 | 0.3723 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.38 | 0.4098 | 0.3578 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.29 | 0.4045 | 0.3667 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.33 | 0.4074 | 0.3629 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.16 | 0.3929 | 0.3662 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.23 | 0.4140 | 0.3540 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.19 | 0.4091 | 0.3617 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.21 | 0.4117 | 0.3588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.58 | 0.7194 | 0.0409 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.96 | 0.7251 | 0.0385 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.78 | 0.7232 | 0.0397 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.87 | 0.7242 | 0.0392 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.81 | 0.7216 | 0.0398 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.39 | 0.7271 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.07 | 0.7245 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.20 | 0.7254 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.21 | 0.7245 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.09 | 0.7141 | 0.0435 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.65 | 0.7228 | 0.0403 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.47 | 0.7198 | 0.0419 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.53 | 0.7214 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.03 | 0.7242 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.82 | 0.7338 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.51 | 0.7305 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.66 | 0.7322 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.98 | 0.7217 | 0.0417 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.90 | 0.7204 | 0.0402 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.31 | 0.7265 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.13 | 0.7241 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.22 | 0.7255 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.95 | 0.7218 | 0.0384 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.54 | 0.7288 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.16 | 0.7253 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.33 | 0.7270 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.58 | 0.7069 | 0.0503 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.32 | 0.7162 | 0.0452 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.04 | 0.7140 | 0.0476 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.17 | 0.7151 | 0.0466 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.08 | 0.7124 | 0.0470 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.94 | 0.7231 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.55 | 0.7195 | 0.0445 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.68 | 0.7209 | 0.0432 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.83 | 0.7190 | 0.0465 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.50 | 0.6882 | 0.0601 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.48 | 0.7050 | 0.0524 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.22 | 0.7006 | 0.0566 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.33 | 0.7031 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.90 | 0.7117 | 0.0533 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.23 | 0.7310 | 0.0436 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.79 | 0.7257 | 0.0490 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.97 | 0.7284 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.08 | 0.7067 | 0.0518 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.97 | 0.7110 | 0.0522 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.58 | 0.7213 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.46 | 0.7190 | 0.0500 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.52 | 0.7205 | 0.0487 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.07 | 0.7126 | 0.0514 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.03 | 0.7248 | 0.0449 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.49 | 0.7204 | 0.0495 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.67 | 0.7222 | 0.0481 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 71.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.74 | 0.7047 | 0.0344 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.69 | 0.2903 | 0.3672 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.74 | 0.2951 | 0.3588 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.71 | 0.2959 | 0.3637 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.73 | 0.2957 | 0.3613 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.69 | 0.2944 | 0.3615 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.72 | 0.3013 | 0.3529 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.70 | 0.3025 | 0.3580 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.71 | 0.3026 | 0.3558 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.12 | 0.1687 | 0.2565 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.52 | 0.3485 | 0.3287 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.57 | 0.3562 | 0.3156 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.54 | 0.3576 | 0.3231 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.55 | 0.3572 | 0.3193 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.49 | 0.3586 | 0.3226 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.60 | 0.3691 | 0.3074 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.53 | 0.3698 | 0.3168 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.55 | 0.3698 | 0.3125 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.63 | 0.2497 | 0.2304 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.44 | 0.2756 | 0.3806 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.54 | 0.2825 | 0.3713 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.48 | 0.2813 | 0.3768 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.50 | 0.2820 | 0.3743 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.40 | 0.2771 | 0.3784 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.42 | 0.2827 | 0.3721 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.41 | 0.2834 | 0.3758 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.42 | 0.2834 | 0.3743 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.72 | 0.7046 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.73 | 0.7046 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.72 | 0.7046 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.73 | 0.7046 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.71 | 0.7045 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7047 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.72 | 0.7046 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.72 | 0.7046 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.74 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.68 | 0.7042 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.71 | 0.7044 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.69 | 0.7043 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.70 | 0.7044 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.72 | 0.7046 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7047 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.73 | 0.7047 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.73 | 0.7047 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.73 | 0.7047 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.73 | 0.7046 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.74 | 0.7046 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.73 | 0.7046 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.74 | 0.7046 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.73 | 0.7046 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.74 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.74 | 0.7046 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.74 | 0.7047 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.33 | 0.7027 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.57 | 0.7037 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.47 | 0.7036 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.53 | 0.7038 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.49 | 0.7039 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.60 | 0.7047 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.56 | 0.7048 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.56 | 0.7048 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.68 | 0.7055 | 0.0358 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.96 | 0.6997 | 0.0442 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.35 | 0.7025 | 0.0407 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.23 | 0.7024 | 0.0423 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.29 | 0.7026 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.38 | 0.7041 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.62 | 0.7067 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.56 | 0.7066 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.58 | 0.7067 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.59 | 0.7054 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.63 | 0.7037 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.56 | 0.7035 | 0.0389 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.63 | 0.7042 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.60 | 0.7040 | 0.0387 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.42 | 0.7030 | 0.0393 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.62 | 0.7038 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.44 | 0.7037 | 0.0398 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.46 | 0.7036 | 0.0397 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.02 | 0.7204 | 0.0578 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.64 | 0.3566 | 0.4551 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.70 | 0.3667 | 0.4388 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.67 | 0.3661 | 0.4481 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.68 | 0.3667 | 0.4439 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.65 | 0.3662 | 0.4443 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.70 | 0.3814 | 0.4245 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.66 | 0.3791 | 0.4365 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.68 | 0.3806 | 0.4313 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.73 | 0.2706 | 0.3625 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.66 | 0.4136 | 0.4094 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.72 | 0.4293 | 0.3890 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.69 | 0.4273 | 0.4014 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.71 | 0.4287 | 0.3957 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.64 | 0.4349 | 0.3968 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.77 | 0.4546 | 0.3703 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.68 | 0.4515 | 0.3876 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.72 | 0.4533 | 0.3800 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.45 | 0.3508 | 0.3206 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.34 | 0.3427 | 0.4699 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.44 | 0.3559 | 0.4525 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.38 | 0.3534 | 0.4632 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.40 | 0.3550 | 0.4586 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.30 | 0.3481 | 0.4596 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.34 | 0.3594 | 0.4448 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.32 | 0.3579 | 0.4544 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.33 | 0.3589 | 0.4504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.57 | 0.7209 | 0.0651 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.83 | 0.7241 | 0.0621 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.69 | 0.7230 | 0.0636 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.74 | 0.7235 | 0.0630 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.79 | 0.7221 | 0.0639 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.27 | 0.7256 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.99 | 0.7237 | 0.0619 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.11 | 0.7244 | 0.0609 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.94 | 0.7243 | 0.0638 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.29 | 0.7183 | 0.0682 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.69 | 0.7230 | 0.0644 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.53 | 0.7212 | 0.0663 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.58 | 0.7221 | 0.0654 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.98 | 0.7237 | 0.0647 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.53 | 0.7290 | 0.0595 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.28 | 0.7269 | 0.0617 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.40 | 0.7280 | 0.0607 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.82 | 0.7230 | 0.0652 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.85 | 0.7208 | 0.0635 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.09 | 0.7237 | 0.0602 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.98 | 0.7226 | 0.0618 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.03 | 0.7233 | 0.0609 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.00 | 0.7225 | 0.0614 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.36 | 0.7261 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.13 | 0.7242 | 0.0605 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.24 | 0.7251 | 0.0599 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.81 | 0.7144 | 0.0771 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.37 | 0.7195 | 0.0713 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.13 | 0.7182 | 0.0740 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.23 | 0.7190 | 0.0728 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.25 | 0.7177 | 0.0738 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.94 | 0.7238 | 0.0668 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.61 | 0.7217 | 0.0708 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.73 | 0.7226 | 0.0692 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.63 | 0.7225 | 0.0714 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.10 | 0.7049 | 0.0895 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.88 | 0.7141 | 0.0803 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.64 | 0.7117 | 0.0855 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.73 | 0.7130 | 0.0829 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.21 | 0.7180 | 0.0819 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.15 | 0.7286 | 0.0707 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.83 | 0.7258 | 0.0772 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.96 | 0.7273 | 0.0743 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.22 | 0.7170 | 0.0771 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.28 | 0.7162 | 0.0775 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.63 | 0.7208 | 0.0736 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.56 | 0.7200 | 0.0752 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.60 | 0.7206 | 0.0741 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.42 | 0.7176 | 0.0767 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.03 | 0.7238 | 0.0707 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.70 | 0.7218 | 0.0751 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.81 | 0.7226 | 0.0738 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 266533 | 0.169 | 31.6 | 28.68 | 0.13 | 0.035 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 266533 | 0.169 | 37.1 | 28.68 | 0.13 | 0.035 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 266533 | 0.169 | 34.3 | 28.68 | 0.13 | 0.035 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 266533 | 0.169 | 36.1 | 28.68 | 0.13 | 0.035 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 905 | None | classic | 1.22 | False | 732752 | 0.688 | 114.4 | 28.90 | 0.13 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 905 | None | classic | 1.22 | False | 732752 | 0.688 | 113.3 | 28.90 | 0.13 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 905 | None | classic | 1.22 | False | 732752 | 0.688 | 111.7 | 28.90 | 0.13 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 905 | None | classic | 1.22 | False | 732752 | 0.688 | 113.1 | 28.90 | 0.13 | 0.017 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1515198 | 0.797 | 160.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 270784 | 0.174 | 33.2 | 28.85 | 0.22 | 0.019 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 270784 | 0.174 | 29.9 | 28.85 | 0.22 | 0.019 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 270784 | 0.174 | 34.2 | 28.85 | 0.22 | 0.019 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 270784 | 0.174 | 28.7 | 28.85 | 0.22 | 0.019 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1080 | None | classic | 1.74 | False | 412035 | 0.350 | 67.3 | 29.35 | 0.16 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1080 | None | classic | 1.74 | False | 412035 | 0.350 | 65.4 | 29.35 | 0.16 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1080 | None | classic | 1.74 | False | 412035 | 0.350 | 73.4 | 29.35 | 0.16 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1080 | None | classic | 1.74 | False | 412035 | 0.350 | 70.5 | 29.35 | 0.16 | 0.005 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2125107 | 0.797 | 78.4 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 252377 | 0.321 | 42.7 | 29.56 | 0.16 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 252377 | 0.321 | 31.6 | 29.56 | 0.16 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 252377 | 0.321 | 29.5 | 29.56 | 0.16 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 252377 | 0.321 | 30.0 | 29.56 | 0.16 | 0.027 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 935 | None | classic | 1.31 | False | 440233 | 0.514 | 82.3 | 29.46 | 0.23 | 0.021 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 935 | None | classic | 1.31 | False | 440233 | 0.514 | 84.0 | 29.46 | 0.23 | 0.021 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 935 | None | classic | 1.31 | False | 440233 | 0.514 | 80.1 | 29.46 | 0.23 | 0.021 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 935 | None | classic | 1.31 | False | 440233 | 0.514 | 82.8 | 29.46 | 0.23 | 0.021 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.741 | 0.019 |
| in035 | mask_ent | 0.634 | 0.019 |
| in035 | mask_grad | 0.460 | 0.019 |
| in035 | r_col | 0.839 | 0.019 |
| in035 | r_warp | 0.874 | 0.019 |

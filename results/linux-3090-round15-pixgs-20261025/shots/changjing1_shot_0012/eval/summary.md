# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 18.2% | 25.21 / 0.0190 | 20.65 / 0.0462 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 19.1% | 25.28 / 0.0199 | 21.90 / 0.0375 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 18.6% | 25.23 / 0.0192 | 21.56 / 0.0410 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 18.7% | 25.24 / 0.0194 | 21.68 / 0.0393 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 18.2% | 25.15 / 0.0187 | 21.98 / 0.0414 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 19.1% | 25.26 / 0.0196 | 23.81 / 0.0319 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 18.6% | 25.19 / 0.0190 | 23.42 / 0.0347 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 18.8% | 25.21 / 0.0192 | 23.55 / 0.0327 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 19.4% | 25.19 / 0.0215 | 21.32 / 0.0694 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 26.8% | 25.87 / 0.0235 | 20.59 / 0.0666 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 27.8% | 25.89 / 0.0243 | 21.74 / 0.0535 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 27.3% | 25.88 / 0.0243 | 21.56 / 0.0592 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 27.4% | 25.89 / 0.0242 | 21.61 / 0.0565 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 26.8% | 25.85 / 0.0235 | 20.77 / 0.0657 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 27.7% | 25.87 / 0.0245 | 21.93 / 0.0519 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 27.2% | 25.86 / 0.0239 | 21.74 / 0.0580 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 27.4% | 25.86 / 0.0242 | 21.78 / 0.0551 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 27.1% | 25.77 / 0.0260 | 21.41 / 0.0854 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 20.4% | 25.64 / 0.0212 | 22.18 / 0.0558 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 22.6% | 25.85 / 0.0226 | 23.50 / 0.0496 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 21.3% | 25.75 / 0.0220 | 23.35 / 0.0496 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 21.8% | 25.80 / 0.0225 | 23.54 / 0.0491 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 19.8% | 25.58 / 0.0211 | 22.92 / 0.0531 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 21.9% | 25.83 / 0.0221 | 24.13 / 0.0447 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 20.6% | 25.69 / 0.0213 | 24.18 / 0.0462 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 21.1% | 25.76 / 0.0216 | 24.26 / 0.0452 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.76 / 0.0513 | 26.59 / 0.0713 | 19.75 / 0.0167 | 29.67 / 0.0267 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.94 / 0.0759 | 25.16 / 0.1255 | 18.36 / 0.0238 | 28.73 / 0.0324 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.59 / 0.0682 | 25.49 / 0.1078 | 19.13 / 0.0201 | 28.88 / 0.0314 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.49 / 0.0718 | 25.61 / 0.1162 | 18.92 / 0.0219 | 28.91 / 0.0316 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.52 / 0.0699 | 25.45 / 0.1117 | 18.94 / 0.0211 | 28.88 / 0.0315 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.72 / 0.0712 | 25.81 / 0.1204 | 19.35 / 0.0201 | 29.10 / 0.0310 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.63 / 0.0632 | 27.81 / 0.0916 | 20.86 / 0.0162 | 29.26 / 0.0300 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.46 / 0.0667 | 27.44 / 0.1018 | 20.40 / 0.0175 | 29.28 / 0.0302 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.52 / 0.0646 | 27.66 / 0.0959 | 20.58 / 0.0168 | 29.26 / 0.0301 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.84 / 0.0728 | 25.80 / 0.1451 | 19.61 / 0.0261 | 29.55 / 0.0284 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.90 / 0.0903 | 25.69 / 0.1349 | 18.06 / 0.0256 | 27.88 / 0.0390 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.74 / 0.0766 | 27.24 / 0.1005 | 18.98 / 0.0214 | 28.38 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.61 / 0.0839 | 26.96 / 0.1167 | 18.74 / 0.0234 | 28.31 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.66 / 0.0803 | 27.08 / 0.1089 | 18.80 / 0.0225 | 28.35 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.07 / 0.0895 | 25.82 / 0.1302 | 18.26 / 0.0250 | 27.98 / 0.0385 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.88 / 0.0761 | 27.41 / 0.1015 | 19.08 / 0.0212 | 28.54 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.76 / 0.0827 | 27.18 / 0.1153 | 18.86 / 0.0227 | 28.47 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.80 / 0.0791 | 27.26 / 0.1065 | 18.91 / 0.0219 | 28.51 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.20 / 0.0801 | 24.93 / 0.1758 | 19.10 / 0.0289 | 29.46 / 0.0298 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.45 / 0.0790 | 24.07 / 0.1303 | 18.90 / 0.0211 | 29.02 / 0.0322 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.02 / 0.0704 | 25.24 / 0.1133 | 20.00 / 0.0178 | 28.99 / 0.0318 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.99 / 0.0746 | 25.07 / 0.1205 | 19.62 / 0.0192 | 29.13 / 0.0317 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.02 / 0.0725 | 25.10 / 0.1168 | 19.78 / 0.0184 | 29.09 / 0.0317 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.82 / 0.0778 | 25.09 / 0.1321 | 19.69 / 0.0204 | 29.14 / 0.0319 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.53 / 0.0675 | 26.06 / 0.1109 | 20.77 / 0.0167 | 29.17 / 0.0313 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.47 / 0.0725 | 25.87 / 0.1194 | 20.46 / 0.0182 | 29.28 / 0.0315 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.53 / 0.0701 | 25.97 / 0.1161 | 20.61 / 0.0174 | 29.25 / 0.0314 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.3%） | — | — | 27.76 / 0.0513 | 26.59 / 0.0713 | 29.67 |
| in035 | rife | 11.8% | 20.4% | 26.45 / 0.0790 | 24.07 / 0.1303 | 29.02 |
| in035 | cnw_cnn | 11.2% | 18.2% | 25.94 / 0.0759 | 25.16 / 0.1255 | 28.73 |
| in035 | cnw_f5 | 17.3% | 26.8% | 24.90 / 0.0903 | 25.69 / 0.1349 | 27.88 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.51 / 0.0569 | -1.21 / +0.0298 (core 12.6%) | -1.89 / +0.0282 (core 13.1%) | -2.87 / +0.0411 (core 19.9%) |
| in035 | 2 | 0-3 | 27.39 / 0.0519 | -1.80 / +0.0358 (core 12.6%) | -2.00 / +0.0324 (core 13.1%) | -3.40 / +0.0510 (core 19.9%) |
| in035 | 4 | 3-5 | 29.38 / 0.0452 | -0.92 / +0.0174 (core 6.3%) | -1.56 / +0.0131 (core 4.6%) | -2.29 / +0.0249 (core 8.7%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.76 / 0.0513 | 26.59 | 29.67 | — |
| in035 | cnw_cnn | 不复核 | —% | 25.94 / 0.0759 | 25.16 | 28.73 | 0/3 |
| in035 | cnw_cnn | oracle | 3.5% | 26.96 / 0.0600 | 26.13 | 29.59 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.59 / 0.0682 | 25.49 | 28.88 | 0/3 |
| in035 | cnw_cnn | oracle | 3.5% | 27.40 / 0.0558 | 26.27 | 29.62 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.49 / 0.0718 | 25.61 | 28.91 | 0/3 |
| in035 | cnw_cnn | oracle | 3.5% | 27.28 / 0.0578 | 26.35 | 29.62 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.52 / 0.0699 | 25.45 | 28.88 | 0/3 |
| in035 | cnw_cnn | oracle | 3.5% | 27.30 / 0.0569 | 26.18 | 29.62 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.72 / 0.0712 | 25.81 | 29.10 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.5% | 27.52 / 0.0565 | 26.56 | 29.63 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.63 / 0.0632 | 27.81 | 29.26 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.6% | 28.17 / 0.0523 | 28.29 | 29.65 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.46 / 0.0667 | 27.44 | 29.28 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.5% | 28.00 / 0.0539 | 28.05 | 29.64 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.52 / 0.0646 | 27.66 | 29.26 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.5% | 28.08 / 0.0529 | 28.25 | 29.64 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.84 / 0.0728 | 25.80 | 29.55 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 3.6% | 27.51 / 0.0605 | 26.77 | 29.67 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 24.90 / 0.0903 | 25.69 | 27.88 | 0/3 |
| in035 | cnw_f5 | oracle | 4.3% | 26.73 / 0.0629 | 26.86 | 29.57 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.74 / 0.0766 | 27.24 | 28.38 | 0/3 |
| in035 | cnw_f5 | oracle | 4.5% | 27.22 / 0.0576 | 28.09 | 29.62 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.61 / 0.0839 | 26.96 | 28.31 | 0/3 |
| in035 | cnw_f5 | oracle | 4.4% | 27.12 / 0.0606 | 27.78 | 29.60 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.66 / 0.0803 | 27.08 | 28.35 | 0/3 |
| in035 | cnw_f5 | oracle | 4.4% | 27.15 / 0.0594 | 27.90 | 29.61 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.07 / 0.0895 | 25.82 | 27.98 | 0/3 |
| in035 | cnw_f5_mw | oracle | 4.4% | 26.84 / 0.0625 | 26.95 | 29.57 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.88 / 0.0761 | 27.41 | 28.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 4.5% | 27.28 / 0.0574 | 28.27 | 29.62 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.76 / 0.0827 | 27.18 | 28.47 | 0/3 |
| in035 | cnw_f5_mw | oracle | 4.4% | 27.19 / 0.0601 | 28.01 | 29.61 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.80 / 0.0791 | 27.26 | 28.51 | 0/3 |
| in035 | cnw_f5_mw | oracle | 4.4% | 27.21 / 0.0587 | 28.09 | 29.62 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.20 / 0.0801 | 24.93 | 29.46 | 0/3 |
| in035 | cnw_f5_pix | oracle | 4.4% | 27.18 / 0.0636 | 26.55 | 29.67 | 0/3 |
| in035 | rife | 不复核 | —% | 26.45 / 0.0790 | 24.07 | 29.02 | 0/3 |
| in035 | rife | oracle | 3.5% | 27.30 / 0.0582 | 25.21 | 29.61 | 0/3 |
| in035 | rife | 不复核 | —% | 27.02 / 0.0704 | 25.24 | 28.99 | 0/3 |
| in035 | rife | oracle | 3.7% | 27.76 / 0.0541 | 26.65 | 29.62 | 0/3 |
| in035 | rife | 不复核 | —% | 26.99 / 0.0746 | 25.07 | 29.13 | 0/3 |
| in035 | rife | oracle | 3.6% | 27.65 / 0.0561 | 26.14 | 29.61 | 0/3 |
| in035 | rife | 不复核 | —% | 27.02 / 0.0725 | 25.10 | 29.09 | 0/3 |
| in035 | rife | oracle | 3.6% | 27.70 / 0.0549 | 26.36 | 29.62 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.82 / 0.0778 | 25.09 | 29.14 | 0/3 |
| in035 | rife_mw | oracle | 3.4% | 27.64 / 0.0576 | 26.23 | 29.62 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.53 / 0.0675 | 26.06 | 29.17 | 0/3 |
| in035 | rife_mw | oracle | 3.6% | 28.12 / 0.0528 | 27.19 | 29.63 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.47 / 0.0725 | 25.87 | 29.28 | 0/3 |
| in035 | rife_mw | oracle | 3.5% | 28.02 / 0.0550 | 26.85 | 29.63 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.53 / 0.0701 | 25.97 | 29.25 | 0/3 |
| in035 | rife_mw | oracle | 3.5% | 28.07 / 0.0539 | 26.98 | 29.63 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.76 / 0.0513 | 26.59 / 0.0713 | — |
| in035 | FF | 0（前馈） | 1008×656（61%） | 26.39 | 25.94 / 0.0759 | 25.16 / 0.1255 | 0/3 |
| in035 | 25 | 1.46 s | 1008×656（61%） | 27.59 | 26.49 / 0.0718 | 25.61 / 0.1162 | 0/3 |
| in035 | 50 | 2.91 s | 1008×656（61%） | 28.22 | 26.52 / 0.0699 | 25.45 / 0.1117 | 0/3 |
| in035 | 100 | 5.83 s | 1008×656（61%） | 28.89 | 26.59 / 0.0682 | 25.49 / 0.1078 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.76 / 0.0513 | 26.59 / 0.0713 | 29.67 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 25.94 / 0.0759 | 25.16 / 0.1255 | 28.73 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 26.96 / 0.0600 | 26.13 / 0.0886 | 29.59 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 26.49 / 0.0718 | 25.61 / 0.1162 | 28.91 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.28 / 0.0578 | 26.35 / 0.0843 | 29.62 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 26.52 / 0.0699 | 25.45 / 0.1117 | 28.88 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.30 / 0.0569 | 26.18 / 0.0820 | 29.62 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 26.59 / 0.0682 | 25.49 / 0.1078 | 28.88 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.40 / 0.0558 | 26.27 / 0.0813 | 29.62 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 26.72 / 0.0712 | 25.81 / 0.1204 | 29.10 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.52 / 0.0565 | 26.56 / 0.0844 | 29.63 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.46 / 0.0667 | 27.44 / 0.1018 | 29.28 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.00 / 0.0539 | 28.05 / 0.0726 | 29.64 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.52 / 0.0646 | 27.66 / 0.0959 | 29.26 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.08 / 0.0529 | 28.25 / 0.0695 | 29.64 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.63 / 0.0632 | 27.81 / 0.0916 | 29.26 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.17 / 0.0523 | 28.29 / 0.0680 | 29.65 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 24.90 / 0.0903 | 25.69 / 0.1349 | 27.88 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 26.73 / 0.0629 | 26.86 / 0.0865 | 29.57 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 25.61 / 0.0839 | 26.96 / 0.1167 | 28.31 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.12 / 0.0606 | 27.78 / 0.0755 | 29.60 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 25.66 / 0.0803 | 27.08 / 0.1089 | 28.35 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.15 / 0.0594 | 27.90 / 0.0715 | 29.61 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 25.74 / 0.0766 | 27.24 / 0.1005 | 28.38 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.22 / 0.0576 | 28.09 / 0.0682 | 29.62 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 25.07 / 0.0895 | 25.82 / 0.1302 | 27.98 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 26.84 / 0.0625 | 26.95 / 0.0819 | 29.57 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 25.76 / 0.0827 | 27.18 / 0.1153 | 28.47 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.19 / 0.0601 | 28.01 / 0.0727 | 29.61 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 25.80 / 0.0791 | 27.26 / 0.1065 | 28.51 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.21 / 0.0587 | 28.09 / 0.0685 | 29.62 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 25.88 / 0.0761 | 27.41 / 0.1015 | 28.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.28 / 0.0574 | 28.27 / 0.0666 | 29.62 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.45 / 0.0790 | 24.07 / 0.1303 | 29.02 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.30 / 0.0582 | 25.21 / 0.0835 | 29.61 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 26.99 / 0.0746 | 25.07 / 0.1205 | 29.13 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.65 / 0.0561 | 26.14 / 0.0769 | 29.61 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.02 / 0.0725 | 25.10 / 0.1168 | 29.09 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.70 / 0.0549 | 26.36 / 0.0722 | 29.62 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.02 / 0.0704 | 25.24 / 0.1133 | 28.99 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.76 / 0.0541 | 26.65 / 0.0697 | 29.62 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.82 / 0.0778 | 25.09 / 0.1321 | 29.14 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.64 / 0.0576 | 26.23 / 0.0833 | 29.62 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.47 / 0.0725 | 25.87 / 0.1194 | 29.28 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.02 / 0.0550 | 26.85 / 0.0738 | 29.63 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.53 / 0.0701 | 25.97 / 0.1161 | 29.25 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.07 / 0.0539 | 26.98 / 0.0717 | 29.63 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.53 / 0.0675 | 26.06 / 0.1109 | 29.17 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.12 / 0.0528 | 27.19 / 0.0688 | 29.63 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 / 0.0713 | 19.75 / 0.0167 | 29.67 / 0.0267 | 27.76 / 0.0513 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 6.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 | 0.7494 | 0.0713 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 21.25 | 0.6776 | 0.2144 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 22.67 | 0.6851 | 0.1666 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 21.82 | 0.6904 | 0.1883 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 22.08 | 0.6874 | 0.1776 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 22.52 | 0.7313 | 0.1984 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 25.31 | 0.7696 | 0.1421 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 23.79 | 0.7654 | 0.1701 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 24.28 | 0.7673 | 0.1559 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 24.25 | 0.7452 | 0.1975 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 22.16 | 0.7176 | 0.1955 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 23.44 | 0.7424 | 0.1477 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 23.02 | 0.7402 | 0.1727 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 23.15 | 0.7425 | 0.1608 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 22.26 | 0.7223 | 0.1898 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 23.61 | 0.7499 | 0.1461 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 23.22 | 0.7475 | 0.1708 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 23.33 | 0.7493 | 0.1581 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 21.14 | 0.7024 | 0.2269 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 19.21 | 0.7164 | 0.2073 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 21.80 | 0.7498 | 0.1567 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 20.13 | 0.7427 | 0.1855 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 20.91 | 0.7467 | 0.1710 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 19.36 | 0.7215 | 0.2086 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 22.20 | 0.7586 | 0.1537 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 19.98 | 0.7510 | 0.1863 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 20.94 | 0.7560 | 0.1715 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.13 | 0.7553 | 0.0886 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.27 | 0.7544 | 0.0813 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.35 | 0.7578 | 0.0843 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.18 | 0.7554 | 0.0820 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.56 | 0.7738 | 0.0844 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.29 | 0.7886 | 0.0680 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.05 | 0.7877 | 0.0726 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.25 | 0.7892 | 0.0695 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.77 | 0.7695 | 0.1007 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.86 | 0.7720 | 0.0865 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.09 | 0.7840 | 0.0682 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.78 | 0.7822 | 0.0755 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.90 | 0.7837 | 0.0715 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.95 | 0.7756 | 0.0819 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.27 | 0.7875 | 0.0666 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.01 | 0.7858 | 0.0727 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.09 | 0.7866 | 0.0685 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.55 | 0.7667 | 0.1099 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.21 | 0.7621 | 0.0835 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.65 | 0.7782 | 0.0697 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.14 | 0.7732 | 0.0769 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.36 | 0.7760 | 0.0722 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.23 | 0.7707 | 0.0833 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.19 | 0.7843 | 0.0688 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.85 | 0.7812 | 0.0738 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.98 | 0.7827 | 0.0717 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.16 | 0.7389 | 0.1255 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.49 | 0.7359 | 0.1078 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.61 | 0.7429 | 0.1162 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.45 | 0.7395 | 0.1117 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.81 | 0.7682 | 0.1204 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.81 | 0.7901 | 0.0916 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.44 | 0.7892 | 0.1018 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.66 | 0.7906 | 0.0959 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.80 | 0.7634 | 0.1451 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.69 | 0.7620 | 0.1349 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.24 | 0.7790 | 0.1005 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.96 | 0.7795 | 0.1167 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.08 | 0.7805 | 0.1089 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.82 | 0.7663 | 0.1302 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.41 | 0.7840 | 0.1015 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.18 | 0.7844 | 0.1153 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.26 | 0.7848 | 0.1065 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.93 | 0.7525 | 0.1758 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.07 | 0.7482 | 0.1303 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.24 | 0.7680 | 0.1133 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.07 | 0.7675 | 0.1205 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.10 | 0.7680 | 0.1168 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.09 | 0.7563 | 0.1321 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.06 | 0.7765 | 0.1109 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.87 | 0.7769 | 0.1194 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.97 | 0.7778 | 0.1161 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.75 | 0.6006 | 0.0167 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 9.70 | 0.3888 | 0.0654 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 10.12 | 0.4352 | 0.0590 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.85 | 0.4197 | 0.0626 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.93 | 0.4248 | 0.0611 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.98 | 0.4846 | 0.0605 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.48 | 0.5504 | 0.0532 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.20 | 0.5299 | 0.0568 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 10.30 | 0.5400 | 0.0552 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.00 | 0.4475 | 0.0452 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 12.10 | 0.4440 | 0.0517 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.72 | 0.5077 | 0.0455 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.39 | 0.4884 | 0.0486 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.52 | 0.4976 | 0.0472 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 12.18 | 0.4583 | 0.0508 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 12.79 | 0.5189 | 0.0449 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 12.48 | 0.5001 | 0.0477 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 12.59 | 0.5089 | 0.0464 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.07 | 0.4723 | 0.0399 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.10 | 0.4455 | 0.0701 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.42 | 0.4955 | 0.0640 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.25 | 0.4822 | 0.0672 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.31 | 0.4879 | 0.0657 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 9.12 | 0.4602 | 0.0705 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 9.40 | 0.5213 | 0.0644 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.26 | 0.5055 | 0.0675 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.32 | 0.5138 | 0.0662 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.40 | 0.5618 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.15 | 0.5924 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.94 | 0.5835 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.96 | 0.5856 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.39 | 0.6285 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.87 | 0.6807 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.43 | 0.6647 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.60 | 0.6727 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.64 | 0.6080 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.11 | 0.5503 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.00 | 0.6046 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.78 | 0.5859 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.83 | 0.5929 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.31 | 0.5611 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.10 | 0.6111 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 18.89 | 0.5937 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 18.94 | 0.6012 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.13 | 0.5774 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.93 | 0.6120 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.02 | 0.6533 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.64 | 0.6405 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.80 | 0.6463 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.76 | 0.6334 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.79 | 0.6783 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.50 | 0.6672 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.64 | 0.6743 | 0.0172 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.36 | 0.5587 | 0.0238 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.13 | 0.5898 | 0.0201 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.92 | 0.5807 | 0.0219 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.94 | 0.5828 | 0.0211 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.35 | 0.6262 | 0.0201 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.86 | 0.6799 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.40 | 0.6636 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.58 | 0.6716 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.61 | 0.6023 | 0.0261 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.06 | 0.5454 | 0.0256 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.98 | 0.6013 | 0.0214 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.74 | 0.5814 | 0.0234 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.80 | 0.5895 | 0.0225 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.26 | 0.5566 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.08 | 0.6086 | 0.0212 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 18.86 | 0.5905 | 0.0227 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 18.91 | 0.5984 | 0.0219 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.10 | 0.5709 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.90 | 0.6103 | 0.0211 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.00 | 0.6512 | 0.0178 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.62 | 0.6393 | 0.0192 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.78 | 0.6448 | 0.0184 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.69 | 0.6307 | 0.0204 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.77 | 0.6770 | 0.0167 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.46 | 0.6657 | 0.0182 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.61 | 0.6728 | 0.0174 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 45.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 | 0.7718 | 0.0287 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.11 | 0.5059 | 0.2287 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.44 | 0.5303 | 0.2094 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.21 | 0.5299 | 0.2198 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.29 | 0.5309 | 0.2152 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.13 | 0.5483 | 0.2236 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.44 | 0.5814 | 0.2019 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.25 | 0.5779 | 0.2124 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.32 | 0.5799 | 0.2076 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.92 | 0.4362 | 0.1896 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.92 | 0.5519 | 0.1925 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.29 | 0.5840 | 0.1706 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 10.06 | 0.5825 | 0.1822 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.15 | 0.5840 | 0.1767 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.95 | 0.5582 | 0.1914 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.29 | 0.5910 | 0.1689 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 10.08 | 0.5889 | 0.1809 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.16 | 0.5908 | 0.1752 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.55 | 0.4830 | 0.1695 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.58 | 0.5312 | 0.2289 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.88 | 0.5563 | 0.2084 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.66 | 0.5552 | 0.2204 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.74 | 0.5562 | 0.2152 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.56 | 0.5336 | 0.2294 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.81 | 0.5638 | 0.2079 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.63 | 0.5605 | 0.2202 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.70 | 0.5631 | 0.2149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.22 | 0.7561 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.88 | 0.7646 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.69 | 0.7627 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.72 | 0.7635 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.00 | 0.7714 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.07 | 0.7834 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.78 | 0.7804 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.90 | 0.7822 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.83 | 0.7614 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.91 | 0.7525 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.64 | 0.7654 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.48 | 0.7621 | 0.0393 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.51 | 0.7635 | 0.0380 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.07 | 0.7552 | 0.0415 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.72 | 0.7672 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.56 | 0.7641 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.59 | 0.7656 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.37 | 0.7522 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.76 | 0.7684 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.58 | 0.7776 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.34 | 0.7757 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.45 | 0.7768 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.33 | 0.7723 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.09 | 0.7826 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.92 | 0.7807 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.01 | 0.7821 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.68 | 0.7301 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.57 | 0.7434 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.39 | 0.7430 | 0.0489 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.45 | 0.7439 | 0.0475 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.69 | 0.7548 | 0.0499 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.89 | 0.7737 | 0.0412 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.67 | 0.7715 | 0.0445 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.74 | 0.7730 | 0.0427 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.43 | 0.7177 | 0.0727 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.64 | 0.7038 | 0.0639 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.51 | 0.7269 | 0.0529 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.43 | 0.7245 | 0.0580 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.44 | 0.7260 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.81 | 0.7079 | 0.0627 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.66 | 0.7312 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.57 | 0.7290 | 0.0570 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.59 | 0.7306 | 0.0539 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.50 | 0.6863 | 0.0838 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.41 | 0.7487 | 0.0561 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.18 | 0.7602 | 0.0512 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.19 | 0.7638 | 0.0526 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.24 | 0.7634 | 0.0515 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.94 | 0.7542 | 0.0548 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.72 | 0.7697 | 0.0483 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.80 | 0.7716 | 0.0503 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.82 | 0.7720 | 0.0492 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 53.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.98 | 0.7280 | 0.0352 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.38 | 0.4466 | 0.2845 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.56 | 0.4704 | 0.2657 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.45 | 0.4703 | 0.2767 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.49 | 0.4714 | 0.2719 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.40 | 0.4843 | 0.2756 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.56 | 0.5146 | 0.2556 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.47 | 0.5115 | 0.2667 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.51 | 0.5136 | 0.2617 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.13 | 0.4601 | 0.1714 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.21 | 0.5006 | 0.2456 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.44 | 0.5314 | 0.2228 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.32 | 0.5297 | 0.2348 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.36 | 0.5313 | 0.2292 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.23 | 0.5065 | 0.2437 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.44 | 0.5376 | 0.2217 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.33 | 0.5361 | 0.2331 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.37 | 0.5380 | 0.2276 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.25 | 0.5247 | 0.1473 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.32 | 0.4731 | 0.2825 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.50 | 0.4962 | 0.2637 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.38 | 0.4959 | 0.2741 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.42 | 0.4968 | 0.2696 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.29 | 0.4748 | 0.2818 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.42 | 0.5021 | 0.2632 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.34 | 0.5002 | 0.2730 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.37 | 0.5023 | 0.2686 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.11 | 0.7173 | 0.0433 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.72 | 0.7242 | 0.0392 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.59 | 0.7228 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.64 | 0.7235 | 0.0402 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.67 | 0.7281 | 0.0397 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.57 | 0.7377 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.37 | 0.7355 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.46 | 0.7370 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.78 | 0.7261 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.76 | 0.7142 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.44 | 0.7248 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.31 | 0.7219 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.35 | 0.7233 | 0.0428 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.92 | 0.7164 | 0.0459 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.53 | 0.7264 | 0.0409 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.40 | 0.7238 | 0.0434 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.43 | 0.7252 | 0.0421 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.30 | 0.7193 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.52 | 0.7265 | 0.0419 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.24 | 0.7344 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.05 | 0.7326 | 0.0399 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.14 | 0.7337 | 0.0387 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.86 | 0.7285 | 0.0413 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.56 | 0.7373 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.40 | 0.7355 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.48 | 0.7369 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.87 | 0.6968 | 0.0570 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.75 | 0.7075 | 0.0498 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.63 | 0.7078 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.70 | 0.7084 | 0.0515 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.70 | 0.7158 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.93 | 0.7318 | 0.0443 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.71 | 0.7294 | 0.0479 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.80 | 0.7311 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.86 | 0.7123 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.68 | 0.6746 | 0.0683 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.74 | 0.6947 | 0.0566 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.57 | 0.6919 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.64 | 0.6937 | 0.0598 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.89 | 0.6784 | 0.0674 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.91 | 0.6988 | 0.0560 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.73 | 0.6963 | 0.0615 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.81 | 0.6983 | 0.0584 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.99 | 0.6952 | 0.0619 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.41 | 0.7135 | 0.0600 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.27 | 0.7261 | 0.0518 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.18 | 0.7265 | 0.0560 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.25 | 0.7271 | 0.0540 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.77 | 0.7162 | 0.0589 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.75 | 0.7317 | 0.0493 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.65 | 0.7316 | 0.0539 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.76 | 0.7330 | 0.0516 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.67 | 0.7076 | 0.0267 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.97 | 0.3586 | 0.2647 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.12 | 0.3704 | 0.2525 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.02 | 0.3727 | 0.2594 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.05 | 0.3718 | 0.2562 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.95 | 0.3768 | 0.2600 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.06 | 0.3859 | 0.2485 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.99 | 0.3892 | 0.2549 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.01 | 0.3880 | 0.2519 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.43 | 0.3314 | 0.1757 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.17 | 0.4219 | 0.2357 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.30 | 0.4364 | 0.2198 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.22 | 0.4401 | 0.2282 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.25 | 0.4385 | 0.2241 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.18 | 0.4258 | 0.2349 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.28 | 0.4395 | 0.2193 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.22 | 0.4438 | 0.2275 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.24 | 0.4423 | 0.2234 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.14 | 0.4257 | 0.1502 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.91 | 0.3684 | 0.2669 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.04 | 0.3774 | 0.2567 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.96 | 0.3799 | 0.2625 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.99 | 0.3793 | 0.2598 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.88 | 0.3703 | 0.2664 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.96 | 0.3796 | 0.2562 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.91 | 0.3820 | 0.2619 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.93 | 0.3812 | 0.2591 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.59 | 0.7068 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.62 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.62 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.62 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.63 | 0.7071 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.65 | 0.7075 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.64 | 0.7074 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.64 | 0.7075 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.67 | 0.7078 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.57 | 0.7067 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.62 | 0.7072 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.60 | 0.7070 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.61 | 0.7072 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.57 | 0.7067 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.62 | 0.7073 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.61 | 0.7071 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.62 | 0.7072 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.67 | 0.7078 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.61 | 0.7071 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.62 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.61 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.62 | 0.7073 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.62 | 0.7072 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.63 | 0.7074 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.63 | 0.7074 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.63 | 0.7074 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.73 | 0.6992 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.88 | 0.7010 | 0.0314 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.91 | 0.7016 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.88 | 0.7014 | 0.0315 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.10 | 0.7038 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.26 | 0.7056 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.28 | 0.7059 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.26 | 0.7057 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.55 | 0.7085 | 0.0284 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.88 | 0.6936 | 0.0390 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.38 | 0.6978 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.31 | 0.6981 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.35 | 0.6980 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.98 | 0.6946 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.54 | 0.6992 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.47 | 0.6997 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.51 | 0.6997 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.46 | 0.7088 | 0.0298 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.02 | 0.7045 | 0.0322 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.99 | 0.7050 | 0.0318 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.13 | 0.7062 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.09 | 0.7058 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.14 | 0.7055 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.17 | 0.7062 | 0.0313 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.28 | 0.7071 | 0.0315 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.25 | 0.7070 | 0.0314 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.76 | 0.7224 | 0.0513 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.14 | 0.4093 | 0.3511 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.31 | 0.4269 | 0.3251 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.20 | 0.4277 | 0.3402 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.24 | 0.4278 | 0.3330 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.13 | 0.4387 | 0.3412 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.26 | 0.4589 | 0.3146 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.18 | 0.4586 | 0.3295 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.21 | 0.4592 | 0.3223 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.82 | 0.3988 | 0.2571 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.46 | 0.4661 | 0.3120 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.62 | 0.4888 | 0.2811 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.53 | 0.4897 | 0.2980 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.57 | 0.4898 | 0.2896 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.47 | 0.4712 | 0.3108 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.60 | 0.4936 | 0.2802 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.53 | 0.4948 | 0.2965 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.56 | 0.4950 | 0.2883 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.66 | 0.4751 | 0.2218 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.03 | 0.4262 | 0.3487 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.17 | 0.4423 | 0.3244 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.08 | 0.4434 | 0.3375 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.11 | 0.4435 | 0.3316 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.00 | 0.4286 | 0.3478 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.09 | 0.4476 | 0.3221 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.04 | 0.4476 | 0.3361 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.06 | 0.4484 | 0.3299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.96 | 0.7151 | 0.0600 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.40 | 0.7191 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.28 | 0.7184 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.30 | 0.7187 | 0.0569 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.52 | 0.7220 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.17 | 0.7280 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.00 | 0.7265 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.08 | 0.7274 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.51 | 0.7213 | 0.0605 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.73 | 0.7134 | 0.0629 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.22 | 0.7196 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.12 | 0.7180 | 0.0606 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.15 | 0.7188 | 0.0594 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.84 | 0.7147 | 0.0625 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.28 | 0.7206 | 0.0574 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.19 | 0.7191 | 0.0601 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.21 | 0.7200 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.18 | 0.7174 | 0.0636 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.30 | 0.7207 | 0.0582 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.76 | 0.7250 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.65 | 0.7242 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.70 | 0.7247 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.64 | 0.7225 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.12 | 0.7276 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.02 | 0.7267 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.07 | 0.7274 | 0.0539 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.94 | 0.7017 | 0.0759 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.59 | 0.7082 | 0.0682 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.49 | 0.7085 | 0.0718 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.52 | 0.7088 | 0.0699 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.72 | 0.7144 | 0.0712 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.63 | 0.7243 | 0.0632 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.46 | 0.7229 | 0.0667 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.52 | 0.7239 | 0.0646 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.84 | 0.7141 | 0.0728 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.90 | 0.6866 | 0.0903 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.74 | 0.6994 | 0.0766 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.61 | 0.6981 | 0.0839 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.66 | 0.6990 | 0.0803 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.07 | 0.6891 | 0.0895 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.88 | 0.7024 | 0.0761 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.76 | 0.7012 | 0.0827 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.80 | 0.7023 | 0.0791 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.20 | 0.7046 | 0.0801 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.45 | 0.7128 | 0.0790 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.02 | 0.7198 | 0.0704 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.99 | 0.7206 | 0.0746 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.02 | 0.7207 | 0.0725 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.82 | 0.7155 | 0.0778 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.53 | 0.7246 | 0.0675 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.47 | 0.7247 | 0.0725 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.53 | 0.7255 | 0.0701 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 264359 | 0.330 | 63.2 | 28.73 | 0.12 | 0.020 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 264359 | 0.330 | 51.8 | 28.73 | 0.12 | 0.020 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 264359 | 0.330 | 53.3 | 28.73 | 0.12 | 0.020 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 264359 | 0.330 | 52.9 | 28.73 | 0.12 | 0.020 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1206 | None | classic | 2.17 | False | 406157 | 0.669 | 115.9 | 29.54 | 0.09 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1206 | None | classic | 2.17 | False | 406157 | 0.669 | 120.0 | 29.54 | 0.09 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1206 | None | classic | 2.17 | False | 406157 | 0.669 | 137.6 | 29.54 | 0.09 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1206 | None | classic | 2.17 | False | 406157 | 0.669 | 125.4 | 29.54 | 0.09 | 0.011 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1925468 | 0.803 | 477.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 261820 | 0.337 | 53.1 | 28.58 | 0.24 | 0.015 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 261820 | 0.337 | 76.6 | 28.58 | 0.24 | 0.015 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 261820 | 0.337 | 72.4 | 28.58 | 0.24 | 0.015 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 261820 | 0.337 | 49.2 | 28.58 | 0.24 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 262069 | 0.342 | 70.6 | 28.72 | 0.25 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 262069 | 0.342 | 59.6 | 28.72 | 0.25 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 262069 | 0.342 | 56.3 | 28.72 | 0.25 | 0.015 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 262069 | 0.342 | 66.3 | 28.72 | 0.25 | 0.015 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2415696 | 0.803 | 125.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 251471 | 0.901 | 81.6 | 29.57 | 0.26 | 0.013 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 251471 | 0.901 | 73.6 | 29.57 | 0.26 | 0.013 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 251471 | 0.901 | 79.4 | 29.57 | 0.26 | 0.013 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 251471 | 0.901 | 60.6 | 29.57 | 0.26 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1290 | None | classic | 2.49 | False | 382203 | 0.665 | 118.3 | 29.61 | 0.18 | 0.022 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1290 | None | classic | 2.49 | False | 382203 | 0.665 | 118.0 | 29.61 | 0.18 | 0.022 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1290 | None | classic | 2.49 | False | 382203 | 0.665 | 120.7 | 29.61 | 0.18 | 0.022 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1290 | None | classic | 2.49 | False | 382203 | 0.665 | 121.9 | 29.61 | 0.18 | 0.022 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.783 | 0.023 |
| in035 | mask_ent | 0.691 | 0.023 |
| in035 | mask_grad | 0.508 | 0.023 |
| in035 | r_col | 0.824 | 0.023 |
| in035 | r_warp | 0.891 | 0.023 |

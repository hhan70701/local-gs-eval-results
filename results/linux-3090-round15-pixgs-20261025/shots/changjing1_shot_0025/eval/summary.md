# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 11.4% | 24.36 / 0.0104 | 20.85 / 0.0292 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.9% | 24.49 / 0.0111 | 21.47 / 0.0230 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.6% | 24.39 / 0.0107 | 21.65 / 0.0258 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.7% | 24.41 / 0.0107 | 21.63 / 0.0238 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 11.2% | 24.36 / 0.0103 | 21.70 / 0.0230 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.5% | 24.45 / 0.0104 | 23.13 / 0.0163 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.3% | 24.40 / 0.0103 | 22.88 / 0.0192 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.3% | 24.41 / 0.0102 | 23.09 / 0.0173 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 11.9% | 24.34 / 0.0113 | 20.34 / 0.0382 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 17.6% | 25.19 / 0.0127 | 20.38 / 0.0426 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 18.2% | 25.30 / 0.0129 | 20.94 / 0.0353 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 17.9% | 25.25 / 0.0128 | 21.21 / 0.0383 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 18.0% | 25.27 / 0.0128 | 21.08 / 0.0363 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 17.0% | 25.10 / 0.0125 | 22.04 / 0.0319 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 17.5% | 25.22 / 0.0127 | 22.79 / 0.0230 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 17.3% | 25.16 / 0.0126 | 23.19 / 0.0266 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 17.3% | 25.17 / 0.0125 | 22.96 / 0.0244 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 17.9% | 25.11 / 0.0135 | 20.91 / 0.0503 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 12.6% | 24.35 / 0.0116 | 21.23 / 0.0382 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 14.4% | 24.57 / 0.0126 | 21.93 / 0.0363 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 13.4% | 24.51 / 0.0121 | 22.33 / 0.0349 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 13.7% | 24.54 / 0.0120 | 22.45 / 0.0335 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 13.1% | 24.51 / 0.0120 | 22.04 / 0.0354 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 15.0% | 24.87 / 0.0126 | 22.99 / 0.0326 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 14.0% | 24.71 / 0.0124 | 23.26 / 0.0328 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 14.3% | 24.76 / 0.0127 | 23.18 / 0.0324 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.73 / 0.0449 | 27.35 / 0.0425 | 20.43 / 0.0134 | 30.01 / 0.0261 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.59 / 0.0614 | 26.72 / 0.0754 | 19.80 / 0.0173 | 29.33 / 0.0305 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.70 / 0.0559 | 26.68 / 0.0645 | 19.85 / 0.0157 | 29.44 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.86 / 0.0590 | 26.93 / 0.0717 | 20.06 / 0.0162 | 29.50 / 0.0295 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.81 / 0.0573 | 26.83 / 0.0676 | 19.98 / 0.0158 | 29.48 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.99 / 0.0561 | 26.85 / 0.0634 | 20.23 / 0.0156 | 29.55 / 0.0286 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.44 / 0.0501 | 27.75 / 0.0497 | 20.69 / 0.0133 | 29.77 / 0.0275 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.37 / 0.0532 | 27.60 / 0.0572 | 20.57 / 0.0142 | 29.74 / 0.0279 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.42 / 0.0516 | 27.79 / 0.0531 | 20.67 / 0.0138 | 29.76 / 0.0277 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.92 / 0.0550 | 26.06 / 0.0684 | 19.79 / 0.0171 | 29.90 / 0.0272 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.69 / 0.0719 | 25.89 / 0.0930 | 19.30 / 0.0190 | 28.88 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.91 / 0.0645 | 25.97 / 0.0834 | 19.30 / 0.0177 | 28.96 / 0.0324 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.11 / 0.0683 | 26.26 / 0.0882 | 19.52 / 0.0180 | 29.10 / 0.0325 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.05 / 0.0662 | 26.16 / 0.0860 | 19.43 / 0.0177 | 29.06 / 0.0324 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.63 / 0.0617 | 26.87 / 0.0716 | 20.12 / 0.0158 | 29.32 / 0.0303 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.94 / 0.0544 | 27.63 / 0.0537 | 20.28 / 0.0144 | 29.42 / 0.0290 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.14 / 0.0577 | 27.67 / 0.0641 | 20.51 / 0.0145 | 29.54 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.02 / 0.0559 | 27.72 / 0.0583 | 20.35 / 0.0144 | 29.48 / 0.0292 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.68 / 0.0595 | 25.81 / 0.0846 | 19.76 / 0.0175 | 29.84 / 0.0276 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.61 / 0.0648 | 26.01 / 0.0981 | 20.25 / 0.0165 | 29.55 / 0.0299 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.99 / 0.0596 | 26.21 / 0.0824 | 20.25 / 0.0147 | 29.53 / 0.0297 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.09 / 0.0620 | 26.41 / 0.0898 | 20.41 / 0.0152 | 29.68 / 0.0294 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.10 / 0.0603 | 26.35 / 0.0850 | 20.39 / 0.0148 | 29.65 / 0.0294 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.99 / 0.0625 | 26.70 / 0.0878 | 20.58 / 0.0155 | 29.56 / 0.0297 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.48 / 0.0559 | 26.78 / 0.0686 | 20.84 / 0.0131 | 29.74 / 0.0285 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.50 / 0.0594 | 27.16 / 0.0771 | 20.86 / 0.0144 | 29.75 / 0.0289 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.51 / 0.0577 | 26.95 / 0.0723 | 20.88 / 0.0139 | 29.75 / 0.0286 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 7.7%） | — | — | 27.73 / 0.0449 | 27.35 / 0.0425 | 30.01 |
| in035 | rife | 6.2% | 12.6% | 26.61 / 0.0648 | 26.01 / 0.0981 | 29.55 |
| in035 | cnw_cnn | 7.0% | 11.4% | 26.59 / 0.0614 | 26.72 / 0.0754 | 29.33 |
| in035 | cnw_f5 | 10.9% | 17.6% | 25.69 / 0.0719 | 25.89 / 0.0930 | 28.88 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.17 / 0.0453 | -1.24 / +0.0273 (core 7.3%) | -1.12 / +0.0189 (core 7.9%) | -2.11 / +0.0328 (core 12.6%) |
| in035 | 2 | 0-3 | 27.22 / 0.0461 | -1.34 / +0.0233 (core 7.3%) | -1.04 / +0.0222 (core 7.9%) | -2.07 / +0.0329 (core 12.6%) |
| in035 | 4 | 3-5 | 28.82 / 0.0434 | -0.79 / +0.0090 (core 2.6%) | -1.29 / +0.0082 (core 3.1%) | -1.96 / +0.0151 (core 4.9%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.73 / 0.0449 | 27.35 | 30.01 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.59 / 0.0614 | 26.72 | 29.33 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 27.35 / 0.0507 | 27.44 | 29.92 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.70 / 0.0559 | 26.68 | 29.44 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 27.40 / 0.0481 | 27.33 | 29.96 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.86 / 0.0590 | 26.93 | 29.50 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 27.50 / 0.0495 | 27.58 | 29.94 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.81 / 0.0573 | 26.83 | 29.48 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 27.47 / 0.0486 | 27.49 | 29.95 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.99 / 0.0561 | 26.85 | 29.55 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.64 / 0.0475 | 27.74 | 29.97 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.44 / 0.0501 | 27.75 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.90 / 0.0449 | 28.30 | 30.00 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.37 / 0.0532 | 27.60 | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.85 / 0.0462 | 28.19 | 29.99 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.42 / 0.0516 | 27.79 | 29.76 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.90 / 0.0455 | 28.34 | 30.00 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.92 / 0.0550 | 26.06 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.4% | 27.44 / 0.0485 | 26.90 | 30.00 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.69 / 0.0719 | 25.89 | 28.88 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 27.06 / 0.0528 | 27.18 | 29.85 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.91 / 0.0645 | 25.97 | 28.96 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 27.05 / 0.0505 | 27.07 | 29.87 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.11 / 0.0683 | 26.26 | 29.10 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 27.18 / 0.0516 | 27.31 | 29.87 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.05 / 0.0662 | 26.16 | 29.06 | 0/3 |
| in035 | cnw_f5 | oracle | 3.1% | 27.11 / 0.0509 | 27.20 | 29.87 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.63 / 0.0617 | 26.87 | 29.32 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.1% | 27.57 / 0.0485 | 27.84 | 29.95 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.94 / 0.0544 | 27.63 | 29.42 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.1% | 27.65 / 0.0462 | 28.27 | 29.96 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.14 / 0.0577 | 27.67 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.1% | 27.78 / 0.0472 | 28.34 | 29.96 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.02 / 0.0559 | 27.72 | 29.48 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.1% | 27.69 / 0.0465 | 28.36 | 29.95 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.68 / 0.0595 | 25.81 | 29.84 | 0/3 |
| in035 | cnw_f5_pix | oracle | 3.2% | 27.40 / 0.0490 | 26.98 | 29.99 | 0/3 |
| in035 | rife | 不复核 | —% | 26.61 / 0.0648 | 26.01 | 29.55 | 0/3 |
| in035 | rife | oracle | 2.2% | 27.61 / 0.0494 | 27.30 | 29.95 | 0/3 |
| in035 | rife | 不复核 | —% | 26.99 / 0.0596 | 26.21 | 29.53 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.65 / 0.0473 | 27.15 | 29.95 | 0/3 |
| in035 | rife | 不复核 | —% | 27.09 / 0.0620 | 26.41 | 29.68 | 0/3 |
| in035 | rife | oracle | 2.2% | 27.72 / 0.0484 | 27.39 | 29.97 | 0/3 |
| in035 | rife | 不复核 | —% | 27.10 / 0.0603 | 26.35 | 29.65 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.71 / 0.0476 | 27.27 | 29.96 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.99 / 0.0625 | 26.70 | 29.56 | 0/3 |
| in035 | rife_mw | oracle | 2.2% | 27.81 / 0.0478 | 27.85 | 29.94 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.48 / 0.0559 | 26.78 | 29.74 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 27.94 / 0.0456 | 27.69 | 29.97 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.50 / 0.0594 | 27.16 | 29.75 | 0/3 |
| in035 | rife_mw | oracle | 2.2% | 27.96 / 0.0471 | 28.04 | 29.97 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.51 / 0.0577 | 26.95 | 29.75 | 0/3 |
| in035 | rife_mw | oracle | 2.2% | 27.96 / 0.0465 | 27.87 | 29.97 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.73 / 0.0449 | 27.35 / 0.0425 | — |
| in035 | FF | 0（前馈） | 1004×652（60%） | 25.53 | 26.59 / 0.0614 | 26.72 / 0.0754 | 0/3 |
| in035 | 25 | 1.37 s | 1004×652（60%） | 26.29 | 26.86 / 0.0590 | 26.93 / 0.0717 | 0/3 |
| in035 | 50 | 2.74 s | 1004×652（60%） | 26.68 | 26.81 / 0.0573 | 26.83 / 0.0676 | 0/3 |
| in035 | 100 | 5.42 s | 1004×652（60%） | 27.12 | 26.70 / 0.0559 | 26.68 / 0.0645 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.73 / 0.0449 | 27.35 / 0.0425 | 30.01 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.59 / 0.0614 | 26.72 / 0.0754 | 29.33 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.35 / 0.0507 | 27.44 / 0.0585 | 29.92 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 26.86 / 0.0590 | 26.93 / 0.0717 | 29.50 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.50 / 0.0495 | 27.58 / 0.0559 | 29.94 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 26.81 / 0.0573 | 26.83 / 0.0676 | 29.48 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.47 / 0.0486 | 27.49 / 0.0539 | 29.95 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 26.70 / 0.0559 | 26.68 / 0.0645 | 29.44 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.40 / 0.0481 | 27.33 / 0.0526 | 29.96 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 26.99 / 0.0561 | 26.85 / 0.0634 | 29.55 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.64 / 0.0475 | 27.74 / 0.0514 | 29.97 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.37 / 0.0532 | 27.60 / 0.0572 | 29.74 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.85 / 0.0462 | 28.19 / 0.0484 | 29.99 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.42 / 0.0516 | 27.79 / 0.0531 | 29.76 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.90 / 0.0455 | 28.34 / 0.0460 | 30.00 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.44 / 0.0501 | 27.75 / 0.0497 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.90 / 0.0449 | 28.30 / 0.0439 | 30.00 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 25.69 / 0.0719 | 25.89 / 0.0930 | 28.88 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.06 / 0.0528 | 27.18 / 0.0633 | 29.85 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.11 / 0.0683 | 26.26 / 0.0882 | 29.10 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.18 / 0.0516 | 27.31 / 0.0607 | 29.87 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.05 / 0.0662 | 26.16 / 0.0860 | 29.06 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.11 / 0.0509 | 27.20 / 0.0596 | 29.87 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 25.91 / 0.0645 | 25.97 / 0.0834 | 28.96 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.05 / 0.0505 | 27.07 / 0.0588 | 29.87 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.63 / 0.0617 | 26.87 / 0.0716 | 29.32 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.57 / 0.0485 | 27.84 / 0.0528 | 29.95 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.14 / 0.0577 | 27.67 / 0.0641 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.78 / 0.0472 | 28.34 / 0.0490 | 29.96 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.02 / 0.0559 | 27.72 / 0.0583 | 29.48 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.69 / 0.0465 | 28.36 / 0.0459 | 29.95 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 26.94 / 0.0544 | 27.63 / 0.0537 | 29.42 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.65 / 0.0462 | 28.27 / 0.0433 | 29.96 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.61 / 0.0648 | 26.01 / 0.0981 | 29.55 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.61 / 0.0494 | 27.30 / 0.0616 | 29.95 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.09 / 0.0620 | 26.41 / 0.0898 | 29.68 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.72 / 0.0484 | 27.39 / 0.0586 | 29.97 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.10 / 0.0603 | 26.35 / 0.0850 | 29.65 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.71 / 0.0476 | 27.27 / 0.0571 | 29.96 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.99 / 0.0596 | 26.21 / 0.0824 | 29.53 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.65 / 0.0473 | 27.15 / 0.0548 | 29.95 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.99 / 0.0625 | 26.70 / 0.0878 | 29.56 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.81 / 0.0478 | 27.85 / 0.0554 | 29.94 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.50 / 0.0594 | 27.16 / 0.0771 | 29.75 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.96 / 0.0471 | 28.04 / 0.0524 | 29.97 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.51 / 0.0577 | 26.95 / 0.0723 | 29.75 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.96 / 0.0465 | 27.87 / 0.0504 | 29.97 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.48 / 0.0559 | 26.78 / 0.0686 | 29.74 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.94 / 0.0456 | 27.69 / 0.0475 | 29.97 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.35 / 0.0425 | 20.43 / 0.0134 | 30.01 / 0.0261 | 27.73 / 0.0449 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 21.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.35 | 0.8103 | 0.0425 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.28 | 0.4957 | 0.4362 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.69 | 0.4980 | 0.4053 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.45 | 0.5088 | 0.4226 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.55 | 0.5037 | 0.4139 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.44 | 0.5242 | 0.4059 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.23 | 0.5712 | 0.3662 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.73 | 0.5558 | 0.3905 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.93 | 0.5656 | 0.3787 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.79 | 0.4246 | 0.3429 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 10.21 | 0.5499 | 0.3494 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.44 | 0.5492 | 0.3200 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 10.34 | 0.5653 | 0.3332 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.40 | 0.5578 | 0.3258 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 10.71 | 0.5951 | 0.3029 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 11.35 | 0.6289 | 0.2607 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 11.15 | 0.6268 | 0.2838 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 11.28 | 0.6310 | 0.2714 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.25 | 0.5278 | 0.2818 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.00 | 0.5670 | 0.3320 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.25 | 0.5728 | 0.2944 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.18 | 0.5834 | 0.3133 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.22 | 0.5797 | 0.3020 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.33 | 0.6150 | 0.3044 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 12.80 | 0.6329 | 0.2586 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 12.62 | 0.6371 | 0.2817 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 12.72 | 0.6362 | 0.2697 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.44 | 0.8039 | 0.0585 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.33 | 0.8039 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.58 | 0.8059 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.49 | 0.8050 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.74 | 0.8084 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.30 | 0.8187 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.19 | 0.8149 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.34 | 0.8184 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.90 | 0.8140 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.18 | 0.7987 | 0.0633 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.07 | 0.7993 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.31 | 0.8013 | 0.0607 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.20 | 0.8005 | 0.0596 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.84 | 0.8106 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.27 | 0.8192 | 0.0433 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.34 | 0.8176 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.36 | 0.8193 | 0.0459 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.98 | 0.8164 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.30 | 0.8018 | 0.0616 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.15 | 0.8009 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.39 | 0.8035 | 0.0586 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.27 | 0.8023 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.85 | 0.8130 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.69 | 0.8123 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.04 | 0.8146 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.87 | 0.8133 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.72 | 0.7852 | 0.0754 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.68 | 0.7849 | 0.0645 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.93 | 0.7884 | 0.0717 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.83 | 0.7866 | 0.0676 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.85 | 0.7909 | 0.0634 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.75 | 0.8104 | 0.0497 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.60 | 0.8047 | 0.0572 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.79 | 0.8099 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.06 | 0.7976 | 0.0684 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.89 | 0.7670 | 0.0930 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.97 | 0.7679 | 0.0834 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.26 | 0.7740 | 0.0882 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.16 | 0.7713 | 0.0860 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.87 | 0.7903 | 0.0716 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.63 | 0.8084 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.67 | 0.8058 | 0.0641 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.72 | 0.8088 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.81 | 0.7936 | 0.0846 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.01 | 0.7747 | 0.0981 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.21 | 0.7758 | 0.0824 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.41 | 0.7820 | 0.0898 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.35 | 0.7800 | 0.0850 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.70 | 0.7942 | 0.0878 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.78 | 0.8000 | 0.0686 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.16 | 0.8035 | 0.0771 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.95 | 0.8017 | 0.0723 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 7.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.43 | 0.6895 | 0.0134 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.04 | 0.2974 | 0.0992 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.26 | 0.3038 | 0.0941 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.11 | 0.3064 | 0.0970 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.15 | 0.3059 | 0.0958 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.18 | 0.3514 | 0.0958 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.27 | 0.3933 | 0.0899 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.22 | 0.3817 | 0.0929 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.24 | 0.3892 | 0.0916 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.71 | 0.3584 | 0.0647 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.89 | 0.3351 | 0.0819 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.97 | 0.3313 | 0.0784 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.93 | 0.3415 | 0.0796 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.95 | 0.3385 | 0.0788 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.16 | 0.3982 | 0.0778 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.12 | 0.4166 | 0.0733 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.20 | 0.4284 | 0.0748 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.17 | 0.4230 | 0.0743 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.64 | 0.4274 | 0.0566 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.03 | 0.2578 | 0.1084 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.66 | 0.2719 | 0.1019 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.21 | 0.2701 | 0.1058 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.48 | 0.2708 | 0.1040 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.97 | 0.2993 | 0.1069 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.08 | 0.3292 | 0.1013 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.02 | 0.3206 | 0.1043 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.05 | 0.3243 | 0.1030 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.82 | 0.6630 | 0.0171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.88 | 0.6722 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.09 | 0.6748 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.01 | 0.6749 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.27 | 0.6843 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.74 | 0.7179 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.61 | 0.7065 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.71 | 0.7152 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.79 | 0.6869 | 0.0171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.33 | 0.6355 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.32 | 0.6407 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.55 | 0.6450 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.45 | 0.6440 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.12 | 0.6749 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.30 | 0.7013 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.52 | 0.7003 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.36 | 0.7007 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.77 | 0.6880 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.27 | 0.6711 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.28 | 0.6762 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.42 | 0.6794 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.41 | 0.6788 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.67 | 0.7024 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.90 | 0.7135 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.89 | 0.7096 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.91 | 0.7109 | 0.0138 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.80 | 0.6596 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.85 | 0.6699 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.06 | 0.6721 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.98 | 0.6723 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.23 | 0.6809 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.69 | 0.7157 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.57 | 0.7040 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.67 | 0.7126 | 0.0138 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.79 | 0.6849 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.30 | 0.6309 | 0.0190 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.30 | 0.6373 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.52 | 0.6410 | 0.0180 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.43 | 0.6403 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.12 | 0.6717 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.28 | 0.6989 | 0.0144 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.51 | 0.6979 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.35 | 0.6982 | 0.0144 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.76 | 0.6851 | 0.0175 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.25 | 0.6685 | 0.0165 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.25 | 0.6734 | 0.0147 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.41 | 0.6773 | 0.0152 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.39 | 0.6763 | 0.0148 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.58 | 0.6986 | 0.0155 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.84 | 0.7119 | 0.0131 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.86 | 0.7085 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.88 | 0.7100 | 0.0139 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 36.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.93 | 0.7679 | 0.0217 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.64 | 0.4530 | 0.2294 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.97 | 0.4650 | 0.2130 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.76 | 0.4691 | 0.2225 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.84 | 0.4681 | 0.2184 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.72 | 0.4788 | 0.2202 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.97 | 0.5097 | 0.2041 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.80 | 0.5085 | 0.2131 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.87 | 0.5107 | 0.2091 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.88 | 0.3363 | 0.1839 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.75 | 0.5043 | 0.1924 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.10 | 0.5210 | 0.1754 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.89 | 0.5276 | 0.1846 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.97 | 0.5267 | 0.1800 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.95 | 0.5358 | 0.1788 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.14 | 0.5622 | 0.1616 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.05 | 0.5712 | 0.1693 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.08 | 0.5687 | 0.1654 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.17 | 0.4241 | 0.1628 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.41 | 0.4467 | 0.2280 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.73 | 0.4655 | 0.2108 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.52 | 0.4674 | 0.2210 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.62 | 0.4680 | 0.2159 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.41 | 0.4690 | 0.2221 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.69 | 0.4953 | 0.2054 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.51 | 0.4955 | 0.2149 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.58 | 0.4963 | 0.2107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.25 | 0.7574 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.35 | 0.7605 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.51 | 0.7612 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.46 | 0.7612 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.73 | 0.7634 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.14 | 0.7737 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.05 | 0.7711 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.12 | 0.7733 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.04 | 0.7569 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.81 | 0.7484 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.86 | 0.7513 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.05 | 0.7529 | 0.0290 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.95 | 0.7520 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.54 | 0.7602 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.74 | 0.7681 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.90 | 0.7685 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.80 | 0.7686 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.98 | 0.7553 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.68 | 0.7605 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.76 | 0.7633 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.85 | 0.7639 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.85 | 0.7638 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.05 | 0.7689 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.27 | 0.7731 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.26 | 0.7720 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.26 | 0.7723 | 0.0240 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.27 | 0.7344 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.37 | 0.7382 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.63 | 0.7421 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.54 | 0.7411 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.77 | 0.7427 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.35 | 0.7616 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.31 | 0.7592 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.36 | 0.7619 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.18 | 0.7133 | 0.0496 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.00 | 0.7040 | 0.0447 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.27 | 0.7121 | 0.0390 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.59 | 0.7180 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.45 | 0.7162 | 0.0400 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.21 | 0.7283 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.62 | 0.7460 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.92 | 0.7500 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.76 | 0.7490 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.55 | 0.6925 | 0.0582 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.03 | 0.7282 | 0.0429 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.35 | 0.7327 | 0.0410 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.70 | 0.7403 | 0.0404 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.70 | 0.7389 | 0.0395 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.63 | 0.7417 | 0.0401 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.87 | 0.7499 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.25 | 0.7542 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.12 | 0.7527 | 0.0377 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 46.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.26 | 0.7364 | 0.0273 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.16 | 0.3956 | 0.2842 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.34 | 0.4078 | 0.2702 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.23 | 0.4102 | 0.2782 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.27 | 0.4100 | 0.2743 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.18 | 0.4196 | 0.2769 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.32 | 0.4461 | 0.2625 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.24 | 0.4432 | 0.2701 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.27 | 0.4455 | 0.2665 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.01 | 0.3556 | 0.1798 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.84 | 0.4506 | 0.2497 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.97 | 0.4685 | 0.2338 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.91 | 0.4733 | 0.2417 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.94 | 0.4731 | 0.2377 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.81 | 0.4761 | 0.2377 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.88 | 0.4968 | 0.2236 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.86 | 0.5030 | 0.2289 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.87 | 0.5015 | 0.2260 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.38 | 0.4502 | 0.1523 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.25 | 0.3982 | 0.2808 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.59 | 0.4185 | 0.2638 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.37 | 0.4176 | 0.2740 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.49 | 0.4191 | 0.2691 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.26 | 0.4182 | 0.2776 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.44 | 0.4400 | 0.2629 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.34 | 0.4410 | 0.2710 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.39 | 0.4420 | 0.2673 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.83 | 0.7297 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.92 | 0.7324 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.04 | 0.7326 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.01 | 0.7328 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.11 | 0.7331 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.52 | 0.7410 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.45 | 0.7390 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.53 | 0.7408 | 0.0275 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.86 | 0.7348 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.40 | 0.7230 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.44 | 0.7259 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.58 | 0.7265 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.50 | 0.7261 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.07 | 0.7317 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.23 | 0.7376 | 0.0277 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.44 | 0.7378 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.33 | 0.7380 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.82 | 0.7347 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.20 | 0.7327 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.35 | 0.7356 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.44 | 0.7359 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.43 | 0.7359 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.45 | 0.7374 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.74 | 0.7416 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.75 | 0.7408 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.77 | 0.7413 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.74 | 0.7125 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.01 | 0.7172 | 0.0358 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.16 | 0.7183 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.13 | 0.7183 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.11 | 0.7182 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.79 | 0.7333 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.69 | 0.7305 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.76 | 0.7327 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.17 | 0.7222 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.53 | 0.6895 | 0.0492 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.00 | 0.6980 | 0.0427 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.20 | 0.7010 | 0.0458 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.14 | 0.7005 | 0.0440 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.71 | 0.7092 | 0.0407 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.25 | 0.7237 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.52 | 0.7251 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.39 | 0.7251 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.83 | 0.7157 | 0.0407 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.69 | 0.7132 | 0.0433 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.46 | 0.7208 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.53 | 0.7236 | 0.0407 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.59 | 0.7235 | 0.0391 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.13 | 0.7220 | 0.0418 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.98 | 0.7333 | 0.0358 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.00 | 0.7337 | 0.0386 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.03 | 0.7341 | 0.0373 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 71.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.01 | 0.7477 | 0.0261 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.91 | 0.3596 | 0.2976 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.02 | 0.3609 | 0.2879 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.94 | 0.3670 | 0.2928 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.97 | 0.3641 | 0.2901 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.85 | 0.3681 | 0.2918 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.95 | 0.3789 | 0.2805 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.88 | 0.3798 | 0.2867 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.91 | 0.3796 | 0.2837 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.96 | 0.2636 | 0.2078 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.83 | 0.4046 | 0.2659 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.92 | 0.4062 | 0.2553 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.87 | 0.4162 | 0.2606 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.89 | 0.4124 | 0.2580 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.78 | 0.4157 | 0.2573 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.85 | 0.4224 | 0.2457 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.82 | 0.4283 | 0.2515 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.84 | 0.4266 | 0.2483 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.86 | 0.3484 | 0.1801 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.07 | 0.3550 | 0.2970 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.66 | 0.3674 | 0.2865 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.26 | 0.3648 | 0.2929 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.49 | 0.3663 | 0.2897 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.03 | 0.3697 | 0.2926 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.23 | 0.3809 | 0.2821 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.11 | 0.3809 | 0.2881 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.17 | 0.3820 | 0.2851 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.92 | 0.7467 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.96 | 0.7471 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.94 | 0.7471 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.95 | 0.7471 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.97 | 0.7473 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.00 | 0.7477 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.99 | 0.7477 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.00 | 0.7478 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.00 | 0.7479 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.85 | 0.7462 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.87 | 0.7466 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.87 | 0.7466 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.87 | 0.7466 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.95 | 0.7470 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.96 | 0.7475 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.96 | 0.7475 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.95 | 0.7475 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.99 | 0.7478 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.95 | 0.7469 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.95 | 0.7470 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.97 | 0.7472 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.96 | 0.7471 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.94 | 0.7470 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.97 | 0.7474 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.97 | 0.7473 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.97 | 0.7474 | 0.0262 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.33 | 0.7410 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.44 | 0.7415 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.50 | 0.7424 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.48 | 0.7421 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.55 | 0.7438 | 0.0286 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7460 | 0.0275 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.74 | 0.7459 | 0.0279 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.76 | 0.7461 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.90 | 0.7479 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.88 | 0.7364 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.96 | 0.7377 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.10 | 0.7391 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.06 | 0.7387 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.32 | 0.7411 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.42 | 0.7435 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.54 | 0.7440 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.48 | 0.7439 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.84 | 0.7481 | 0.0276 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.55 | 0.7422 | 0.0299 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.53 | 0.7417 | 0.0297 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.68 | 0.7439 | 0.0294 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.65 | 0.7433 | 0.0294 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.56 | 0.7437 | 0.0297 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.74 | 0.7457 | 0.0285 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.75 | 0.7458 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.75 | 0.7459 | 0.0286 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.73 | 0.7453 | 0.0449 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.53 | 0.3680 | 0.3758 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.68 | 0.3720 | 0.3563 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.58 | 0.3773 | 0.3682 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.62 | 0.3752 | 0.3621 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.51 | 0.3855 | 0.3640 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.63 | 0.4043 | 0.3432 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.56 | 0.4027 | 0.3556 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.59 | 0.4041 | 0.3496 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.27 | 0.2996 | 0.2934 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.63 | 0.4147 | 0.3378 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.75 | 0.4206 | 0.3143 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.69 | 0.4295 | 0.3273 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.71 | 0.4266 | 0.3209 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.63 | 0.4371 | 0.3196 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.70 | 0.4497 | 0.2969 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.68 | 0.4557 | 0.3086 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.69 | 0.4539 | 0.3022 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.26 | 0.3862 | 0.2555 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.64 | 0.3641 | 0.3755 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.19 | 0.3783 | 0.3556 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.83 | 0.3775 | 0.3674 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.03 | 0.3785 | 0.3614 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.62 | 0.3841 | 0.3674 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.80 | 0.4001 | 0.3457 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.69 | 0.4002 | 0.3582 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.75 | 0.4013 | 0.3520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.35 | 0.7402 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.40 | 0.7416 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.50 | 0.7419 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.47 | 0.7419 | 0.0486 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.64 | 0.7433 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.90 | 0.7477 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.85 | 0.7465 | 0.0462 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.90 | 0.7476 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.44 | 0.7445 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.06 | 0.7364 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.05 | 0.7376 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.18 | 0.7382 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.11 | 0.7379 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.57 | 0.7421 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.65 | 0.7453 | 0.0462 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.78 | 0.7455 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.69 | 0.7455 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.40 | 0.7442 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.61 | 0.7419 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.65 | 0.7428 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.72 | 0.7434 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.71 | 0.7432 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.81 | 0.7453 | 0.0478 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.94 | 0.7471 | 0.0456 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.96 | 0.7468 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.96 | 0.7469 | 0.0465 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.59 | 0.7290 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.70 | 0.7309 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.86 | 0.7323 | 0.0590 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.81 | 0.7319 | 0.0573 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.99 | 0.7344 | 0.0561 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.44 | 0.7431 | 0.0501 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.37 | 0.7414 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.42 | 0.7428 | 0.0516 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.92 | 0.7378 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.69 | 0.7150 | 0.0719 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.91 | 0.7189 | 0.0645 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.11 | 0.7214 | 0.0683 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.05 | 0.7208 | 0.0662 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.63 | 0.7285 | 0.0617 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.94 | 0.7365 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.14 | 0.7374 | 0.0577 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.02 | 0.7372 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.68 | 0.7343 | 0.0595 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.61 | 0.7297 | 0.0648 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.99 | 0.7320 | 0.0596 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.09 | 0.7350 | 0.0620 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.10 | 0.7344 | 0.0603 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.99 | 0.7362 | 0.0625 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.48 | 0.7420 | 0.0559 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.50 | 0.7423 | 0.0594 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.51 | 0.7424 | 0.0577 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1277 | None | classic | 2.44 | False | 230504 | 0.329 | 58.8 | 27.94 | 0.07 | 0.027 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1277 | None | classic | 2.44 | False | 230504 | 0.329 | 55.2 | 27.94 | 0.07 | 0.027 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1277 | None | classic | 2.44 | False | 230504 | 0.329 | 73.1 | 27.94 | 0.07 | 0.027 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1277 | None | classic | 2.44 | False | 230504 | 0.329 | 57.3 | 27.94 | 0.07 | 0.027 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 945 | None | classic | 0.53 | False | 540098 | 1.000 | 200.1 | 30.18 | 0.14 | 0.015 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 945 | None | classic | 0.53 | False | 540098 | 1.000 | 188.5 | 30.18 | 0.14 | 0.015 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 945 | None | classic | 0.53 | False | 540098 | 1.000 | 206.0 | 30.18 | 0.14 | 0.015 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 945 | None | classic | 0.53 | False | 540098 | 1.000 | 231.0 | 30.18 | 0.14 | 0.015 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1469364 | 0.811 | 479.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 266576 | 0.337 | 80.6 | 27.96 | 0.23 | 0.024 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 266576 | 0.337 | 69.6 | 27.96 | 0.23 | 0.024 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 266576 | 0.337 | 69.4 | 27.96 | 0.23 | 0.024 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 266576 | 0.337 | 74.8 | 27.96 | 0.23 | 0.024 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 954 | None | classic | 1.36 | False | 502919 | 0.997 | 206.3 | 28.29 | 0.12 | 0.003 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 954 | None | classic | 1.36 | False | 502919 | 0.997 | 183.4 | 28.29 | 0.12 | 0.003 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 954 | None | classic | 1.36 | False | 502919 | 0.997 | 190.3 | 28.29 | 0.12 | 0.003 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 954 | None | classic | 1.36 | False | 502919 | 0.997 | 201.4 | 28.29 | 0.12 | 0.003 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1922573 | 0.811 | 117.9 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 253452 | 0.931 | 85.1 | 28.20 | 0.08 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 253452 | 0.931 | 73.5 | 28.20 | 0.08 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 253452 | 0.931 | 98.2 | 28.20 | 0.08 | 0.027 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 253452 | 0.931 | 67.0 | 28.20 | 0.08 | 0.027 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1124 | None | classic | 1.89 | False | 455073 | 1.043 | 161.4 | 28.75 | 0.07 | 0.021 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1124 | None | classic | 1.89 | False | 455073 | 1.043 | 167.5 | 28.75 | 0.07 | 0.021 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1124 | None | classic | 1.89 | False | 455073 | 1.043 | 178.9 | 28.75 | 0.07 | 0.021 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1124 | None | classic | 1.89 | False | 455073 | 1.043 | 145.4 | 28.75 | 0.07 | 0.021 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.599 | 0.024 |
| in035 | mask_ent | 0.705 | 0.024 |
| in035 | mask_grad | 0.441 | 0.024 |
| in035 | r_col | 0.762 | 0.024 |
| in035 | r_warp | 0.831 | 0.024 |

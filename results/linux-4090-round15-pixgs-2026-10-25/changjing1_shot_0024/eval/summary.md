# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 7.5% | 23.50 / 0.0099 | 20.02 / 0.0282 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.1% | 23.60 / 0.0108 | 21.60 / 0.0224 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.7% | 23.52 / 0.0103 | 21.02 / 0.0252 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.8% | 23.52 / 0.0106 | 21.25 / 0.0241 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.5% | 23.55 / 0.0104 | 20.36 / 0.0255 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.2% | 23.75 / 0.0105 | 21.63 / 0.0196 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.7% | 23.67 / 0.0103 | 21.05 / 0.0217 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.9% | 23.70 / 0.0103 | 21.31 / 0.0202 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 8.8% | 23.90 / 0.0119 | 20.07 / 0.0411 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 12.8% | 24.63 / 0.0114 | 19.95 / 0.0383 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 13.5% | 24.65 / 0.0117 | 20.82 / 0.0326 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 13.2% | 24.70 / 0.0116 | 20.69 / 0.0365 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 13.2% | 24.68 / 0.0116 | 20.75 / 0.0346 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 12.8% | 24.67 / 0.0110 | 20.97 / 0.0314 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 13.6% | 24.72 / 0.0113 | 23.30 / 0.0232 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 13.1% | 24.73 / 0.0111 | 22.55 / 0.0270 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 13.2% | 24.71 / 0.0111 | 22.84 / 0.0247 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 13.8% | 24.78 / 0.0122 | 20.39 / 0.0481 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 7.2% | 25.01 / 0.0073 | 21.15 / 0.0247 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 8.4% | 25.29 / 0.0079 | 22.35 / 0.0228 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 7.6% | 25.12 / 0.0074 | 21.92 / 0.0233 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 7.8% | 25.22 / 0.0073 | 22.28 / 0.0220 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 7.3% | 24.57 / 0.0075 | 21.52 / 0.0230 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 8.6% | 25.05 / 0.0083 | 21.43 / 0.0237 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 7.7% | 24.72 / 0.0078 | 21.80 / 0.0234 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 7.9% | 24.81 / 0.0081 | 21.61 / 0.0230 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.68 / 0.0491 | 26.17 / 0.0477 | 19.74 / 0.0112 | 29.91 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.07 / 0.0603 | 25.06 / 0.0915 | 19.09 / 0.0149 | 29.54 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.36 / 0.0558 | 25.89 / 0.0727 | 19.47 / 0.0129 | 29.70 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.32 / 0.0582 | 25.85 / 0.0822 | 19.38 / 0.0138 | 29.73 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.34 / 0.0571 | 25.95 / 0.0763 | 19.43 / 0.0134 | 29.72 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.10 / 0.0571 | 24.69 / 0.0821 | 19.63 / 0.0143 | 29.61 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.35 / 0.0535 | 25.38 / 0.0642 | 19.85 / 0.0120 | 29.66 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.28 / 0.0554 | 25.18 / 0.0741 | 19.76 / 0.0130 | 29.65 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.33 / 0.0544 | 25.34 / 0.0681 | 19.83 / 0.0125 | 29.65 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.01 / 0.0569 | 25.25 / 0.0852 | 19.08 / 0.0153 | 29.76 / 0.0364 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.29 / 0.0714 | 24.14 / 0.1051 | 18.32 / 0.0185 | 29.09 / 0.0417 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.43 / 0.0653 | 24.82 / 0.0861 | 18.49 / 0.0161 | 29.20 / 0.0400 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.49 / 0.0696 | 24.90 / 0.0958 | 18.55 / 0.0173 | 29.29 / 0.0410 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.49 / 0.0677 | 24.88 / 0.0899 | 18.66 / 0.0168 | 29.28 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.81 / 0.0659 | 23.95 / 0.0984 | 19.55 / 0.0155 | 29.26 / 0.0394 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.52 / 0.0579 | 25.32 / 0.0723 | 20.63 / 0.0122 | 29.61 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.17 / 0.0631 | 24.59 / 0.0873 | 20.13 / 0.0145 | 29.45 / 0.0384 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.33 / 0.0605 | 24.88 / 0.0792 | 20.35 / 0.0135 | 29.56 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.92 / 0.0601 | 24.99 / 0.0950 | 19.05 / 0.0157 | 29.71 / 0.0370 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.26 / 0.0604 | 25.28 / 0.0760 | 19.73 / 0.0141 | 29.70 / 0.0369 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.50 / 0.0567 | 25.97 / 0.0627 | 20.07 / 0.0123 | 29.76 / 0.0364 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.39 / 0.0592 | 25.61 / 0.0692 | 19.86 / 0.0133 | 29.76 / 0.0368 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.45 / 0.0582 | 25.77 / 0.0654 | 19.93 / 0.0130 | 29.77 / 0.0366 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.39 / 0.0588 | 25.72 / 0.0678 | 19.93 / 0.0138 | 29.73 / 0.0360 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.54 / 0.0563 | 26.07 / 0.0614 | 20.21 / 0.0126 | 29.78 / 0.0358 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.43 / 0.0587 | 25.95 / 0.0653 | 20.05 / 0.0133 | 29.77 / 0.0362 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.48 / 0.0577 | 26.05 / 0.0629 | 20.10 / 0.0129 | 29.78 / 0.0359 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.8%） | — | — | 27.68 / 0.0491 | 26.17 / 0.0477 | 29.91 |
| in035 | rife | 2.5% | 7.2% | 27.26 / 0.0604 | 25.28 / 0.0760 | 29.70 |
| in035 | cnw_cnn | 4.4% | 7.5% | 27.07 / 0.0603 | 25.06 / 0.0915 | 29.54 |
| in035 | cnw_f5 | 7.0% | 12.8% | 26.29 / 0.0714 | 24.14 / 0.1051 | 29.09 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.53 / 0.0510 | -0.41 / +0.0149 (core 3.6%) | -0.30 / +0.0119 (core 5.1%) | -1.25 / +0.0290 (core 8.9%) |
| in035 | 2 | 0-3 | 27.11 / 0.0483 | -0.72 / +0.0163 (core 3.6%) | -0.42 / +0.0143 (core 5.1%) | -1.44 / +0.0295 (core 8.9%) |
| in035 | 4 | 3-5 | 29.40 / 0.0479 | -0.14 / +0.0027 (core 0.3%) | -1.12 / +0.0076 (core 1.8%) | -1.50 / +0.0086 (core 2.4%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.68 / 0.0491 | 26.17 | 29.91 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.07 / 0.0603 | 25.06 | 29.54 | 0/3 |
| in035 | cnw_cnn | oracle | 2.1% | 27.49 / 0.0539 | 26.45 | 29.84 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.36 / 0.0558 | 25.89 | 29.70 | 0/3 |
| in035 | cnw_cnn | oracle | 2.2% | 27.70 / 0.0516 | 27.23 | 29.89 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.32 / 0.0582 | 25.85 | 29.73 | 0/3 |
| in035 | cnw_cnn | oracle | 2.1% | 27.66 / 0.0528 | 27.07 | 29.88 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.34 / 0.0571 | 25.95 | 29.72 | 0/3 |
| in035 | cnw_cnn | oracle | 2.2% | 27.68 / 0.0523 | 27.20 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.10 / 0.0571 | 24.69 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.1% | 27.57 / 0.0521 | 26.40 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.35 / 0.0535 | 25.38 | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.1% | 27.76 / 0.0501 | 27.22 | 29.90 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.28 / 0.0554 | 25.18 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.1% | 27.71 / 0.0512 | 26.96 | 29.90 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.33 / 0.0544 | 25.34 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.1% | 27.75 / 0.0507 | 27.16 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.01 / 0.0569 | 25.25 | 29.76 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.1% | 27.24 / 0.0524 | 26.43 | 29.90 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.29 / 0.0714 | 24.14 | 29.09 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.03 / 0.0574 | 26.05 | 29.77 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.43 / 0.0653 | 24.82 | 29.20 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.12 / 0.0549 | 26.66 | 29.84 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.49 / 0.0696 | 24.90 | 29.29 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.13 / 0.0563 | 26.61 | 29.81 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.49 / 0.0677 | 24.88 | 29.28 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.15 / 0.0556 | 26.60 | 29.83 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.81 / 0.0659 | 23.95 | 29.26 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 27.45 / 0.0544 | 25.83 | 29.84 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.52 / 0.0579 | 25.32 | 29.61 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.8% | 27.90 / 0.0511 | 26.97 | 29.88 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.17 / 0.0631 | 24.59 | 29.45 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 27.66 / 0.0533 | 26.37 | 29.84 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.33 / 0.0605 | 24.88 | 29.56 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 27.77 / 0.0523 | 26.61 | 29.86 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.92 / 0.0601 | 24.99 | 29.71 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.7% | 27.21 / 0.0533 | 26.31 | 29.90 | 0/3 |
| in035 | rife | 不复核 | —% | 27.26 / 0.0604 | 25.28 | 29.70 | 0/3 |
| in035 | rife | oracle | 1.5% | 27.58 / 0.0526 | 26.08 | 29.87 | 0/3 |
| in035 | rife | 不复核 | —% | 27.50 / 0.0567 | 25.97 | 29.76 | 0/3 |
| in035 | rife | oracle | 1.5% | 27.75 / 0.0506 | 26.71 | 29.90 | 0/3 |
| in035 | rife | 不复核 | —% | 27.39 / 0.0592 | 25.61 | 29.76 | 0/3 |
| in035 | rife | oracle | 1.5% | 27.66 / 0.0516 | 26.31 | 29.89 | 0/3 |
| in035 | rife | 不复核 | —% | 27.45 / 0.0582 | 25.77 | 29.77 | 0/3 |
| in035 | rife | oracle | 1.5% | 27.70 / 0.0513 | 26.44 | 29.90 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.39 / 0.0588 | 25.72 | 29.73 | 0/3 |
| in035 | rife_mw | oracle | 1.4% | 27.75 / 0.0514 | 26.44 | 29.90 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.54 / 0.0563 | 26.07 | 29.78 | 0/3 |
| in035 | rife_mw | oracle | 1.5% | 27.80 / 0.0506 | 26.79 | 29.89 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.43 / 0.0587 | 25.95 | 29.77 | 0/3 |
| in035 | rife_mw | oracle | 1.5% | 27.78 / 0.0513 | 26.60 | 29.89 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.48 / 0.0577 | 26.05 | 29.78 | 0/3 |
| in035 | rife_mw | oracle | 1.5% | 27.79 / 0.0509 | 26.67 | 29.89 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.68 / 0.0491 | 26.17 / 0.0477 | — |
| in035 | FF | 0（前馈） | 989×560（52%） | 25.89 | 27.07 / 0.0603 | 25.06 / 0.0915 | 0/3 |
| in035 | 25 | 0.56 s | 989×560（52%） | 26.41 | 27.32 / 0.0582 | 25.85 / 0.0822 | 0/3 |
| in035 | 50 | 1.12 s | 989×560（52%） | 26.68 | 27.34 / 0.0571 | 25.95 / 0.0763 | 0/3 |
| in035 | 100 | 2.22 s | 989×560（52%） | 26.96 | 27.36 / 0.0558 | 25.89 / 0.0727 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.68 / 0.0491 | 26.17 / 0.0477 | 29.91 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.07 / 0.0603 | 25.06 / 0.0915 | 29.54 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.49 / 0.0539 | 26.45 / 0.0642 | 29.84 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.32 / 0.0582 | 25.85 / 0.0822 | 29.73 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.66 / 0.0528 | 27.07 / 0.0593 | 29.88 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.34 / 0.0571 | 25.95 / 0.0763 | 29.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.68 / 0.0523 | 27.20 / 0.0564 | 29.89 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.36 / 0.0558 | 25.89 / 0.0727 | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.70 / 0.0516 | 27.23 / 0.0554 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.10 / 0.0571 | 24.69 / 0.0821 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.57 / 0.0521 | 26.40 / 0.0599 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.28 / 0.0554 | 25.18 / 0.0741 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.71 / 0.0512 | 26.96 / 0.0549 | 29.90 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.33 / 0.0544 | 25.34 / 0.0681 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.75 / 0.0507 | 27.16 / 0.0517 | 29.90 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.35 / 0.0535 | 25.38 / 0.0642 | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.76 / 0.0501 | 27.22 / 0.0491 | 29.90 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.29 / 0.0714 | 24.14 / 0.1051 | 29.09 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.03 / 0.0574 | 26.05 / 0.0670 | 29.77 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.49 / 0.0696 | 24.90 / 0.0958 | 29.29 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.13 / 0.0563 | 26.61 / 0.0611 | 29.81 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.49 / 0.0677 | 24.88 / 0.0899 | 29.28 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.15 / 0.0556 | 26.60 / 0.0588 | 29.83 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.43 / 0.0653 | 24.82 / 0.0861 | 29.20 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.12 / 0.0549 | 26.66 / 0.0575 | 29.84 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.81 / 0.0659 | 23.95 / 0.0984 | 29.26 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.45 / 0.0544 | 25.83 / 0.0666 | 29.84 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.17 / 0.0631 | 24.59 / 0.0873 | 29.45 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.66 / 0.0533 | 26.37 / 0.0616 | 29.84 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.33 / 0.0605 | 24.88 / 0.0792 | 29.56 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.77 / 0.0523 | 26.61 / 0.0577 | 29.86 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.52 / 0.0579 | 25.32 / 0.0723 | 29.61 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.90 / 0.0511 | 26.97 / 0.0530 | 29.88 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.26 / 0.0604 | 25.28 / 0.0760 | 29.70 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.58 / 0.0526 | 26.08 / 0.0583 | 29.87 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.39 / 0.0592 | 25.61 / 0.0692 | 29.76 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.66 / 0.0516 | 26.31 / 0.0551 | 29.89 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.45 / 0.0582 | 25.77 / 0.0654 | 29.77 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.70 / 0.0513 | 26.44 / 0.0532 | 29.90 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.50 / 0.0567 | 25.97 / 0.0627 | 29.76 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.75 / 0.0506 | 26.71 / 0.0509 | 29.90 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.39 / 0.0588 | 25.72 / 0.0678 | 29.73 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.75 / 0.0514 | 26.44 / 0.0558 | 29.90 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.43 / 0.0587 | 25.95 / 0.0653 | 29.77 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.78 / 0.0513 | 26.60 / 0.0544 | 29.89 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.48 / 0.0577 | 26.05 / 0.0629 | 29.78 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.79 / 0.0509 | 26.67 / 0.0531 | 29.89 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.54 / 0.0563 | 26.07 / 0.0614 | 29.78 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.80 / 0.0506 | 26.79 / 0.0513 | 29.89 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.17 / 0.0477 | 19.74 / 0.0112 | 29.91 / 0.0339 | 27.68 / 0.0491 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 13.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.17 | 0.8157 | 0.0477 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.73 | 0.4836 | 0.3788 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.97 | 0.5239 | 0.3380 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.82 | 0.5166 | 0.3611 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.86 | 0.5225 | 0.3489 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.73 | 0.4578 | 0.3566 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.28 | 0.5093 | 0.3117 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.95 | 0.4886 | 0.3370 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.10 | 0.5006 | 0.3236 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.79 | 0.4412 | 0.3103 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 11.87 | 0.5218 | 0.3174 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.19 | 0.5337 | 0.2724 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.15 | 0.5509 | 0.2963 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.18 | 0.5456 | 0.2830 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 12.07 | 0.5071 | 0.2978 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 13.00 | 0.5844 | 0.2386 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 12.45 | 0.5532 | 0.2750 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 12.66 | 0.5696 | 0.2572 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.52 | 0.5564 | 0.2528 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.07 | 0.4396 | 0.4183 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.65 | 0.4644 | 0.3785 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.35 | 0.4606 | 0.4042 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.50 | 0.4637 | 0.3912 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.77 | 0.4391 | 0.3954 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.39 | 0.4665 | 0.3534 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.96 | 0.4609 | 0.3814 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.14 | 0.4633 | 0.3677 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.45 | 0.8130 | 0.0642 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.23 | 0.8232 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.07 | 0.8208 | 0.0593 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.20 | 0.8228 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.40 | 0.8051 | 0.0599 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.22 | 0.8260 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.96 | 0.8168 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.16 | 0.8235 | 0.0517 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.43 | 0.8135 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.05 | 0.8036 | 0.0670 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.66 | 0.8081 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.61 | 0.8105 | 0.0611 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.60 | 0.8098 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.83 | 0.7931 | 0.0666 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.97 | 0.8121 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.37 | 0.8022 | 0.0616 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.61 | 0.8064 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.31 | 0.8114 | 0.0646 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.08 | 0.8062 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.71 | 0.8155 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.31 | 0.8100 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.44 | 0.8122 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.44 | 0.8113 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.79 | 0.8122 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.60 | 0.8109 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.67 | 0.8115 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.06 | 0.7836 | 0.0915 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.89 | 0.8013 | 0.0727 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.85 | 0.7983 | 0.0822 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.95 | 0.8012 | 0.0763 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.69 | 0.7691 | 0.0821 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.38 | 0.7955 | 0.0642 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.18 | 0.7847 | 0.0741 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.34 | 0.7922 | 0.0681 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.25 | 0.7889 | 0.0852 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.14 | 0.7575 | 0.1051 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.82 | 0.7630 | 0.0861 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.90 | 0.7709 | 0.0958 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.88 | 0.7684 | 0.0899 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.95 | 0.7452 | 0.0984 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.32 | 0.7809 | 0.0723 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.59 | 0.7629 | 0.0873 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.88 | 0.7726 | 0.0792 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.99 | 0.7818 | 0.0950 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.28 | 0.7809 | 0.0760 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.97 | 0.7961 | 0.0627 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.61 | 0.7887 | 0.0692 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.77 | 0.7928 | 0.0654 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.72 | 0.7886 | 0.0678 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.07 | 0.7942 | 0.0614 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.95 | 0.7919 | 0.0653 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.05 | 0.7942 | 0.0629 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.74 | 0.6486 | 0.0112 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.92 | 0.2676 | 0.0964 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.11 | 0.3090 | 0.0923 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.01 | 0.2908 | 0.0948 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.07 | 0.2992 | 0.0937 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.82 | 0.2803 | 0.0955 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.91 | 0.3147 | 0.0911 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.86 | 0.3009 | 0.0933 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.88 | 0.3116 | 0.0922 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.22 | 0.2421 | 0.0590 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.00 | 0.2889 | 0.0752 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.07 | 0.3161 | 0.0708 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.04 | 0.3080 | 0.0734 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.05 | 0.3132 | 0.0724 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.02 | 0.3480 | 0.0701 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.19 | 0.4189 | 0.0643 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.09 | 0.3824 | 0.0685 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.14 | 0.4011 | 0.0669 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.59 | 0.3358 | 0.0465 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.30 | 0.2221 | 0.0974 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.66 | 0.2504 | 0.0914 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.42 | 0.2344 | 0.0951 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.54 | 0.2424 | 0.0936 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.21 | 0.2195 | 0.0983 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.32 | 0.2467 | 0.0941 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.24 | 0.2324 | 0.0966 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.26 | 0.2383 | 0.0955 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.10 | 0.6342 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.48 | 0.6622 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.39 | 0.6532 | 0.0138 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.44 | 0.6580 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.64 | 0.6463 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.87 | 0.6704 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.78 | 0.6594 | 0.0130 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.85 | 0.6682 | 0.0124 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.08 | 0.6244 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.33 | 0.5959 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.50 | 0.6080 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.56 | 0.6044 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.67 | 0.6065 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.58 | 0.6354 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.65 | 0.6865 | 0.0121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.16 | 0.6602 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.38 | 0.6731 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.05 | 0.6238 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.73 | 0.6381 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.07 | 0.6533 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.86 | 0.6428 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.93 | 0.6469 | 0.0128 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.94 | 0.6515 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.22 | 0.6596 | 0.0124 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.06 | 0.6533 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.11 | 0.6559 | 0.0127 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.09 | 0.6335 | 0.0149 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.47 | 0.6620 | 0.0129 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.38 | 0.6526 | 0.0138 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.43 | 0.6574 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.63 | 0.6447 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.85 | 0.6695 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.76 | 0.6583 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.83 | 0.6672 | 0.0125 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.08 | 0.6229 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.32 | 0.5934 | 0.0185 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.49 | 0.6063 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.55 | 0.6025 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.66 | 0.6045 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.55 | 0.6331 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.63 | 0.6854 | 0.0122 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.13 | 0.6585 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.35 | 0.6717 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.05 | 0.6213 | 0.0157 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.73 | 0.6376 | 0.0141 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.07 | 0.6528 | 0.0123 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.86 | 0.6420 | 0.0133 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.93 | 0.6463 | 0.0130 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.93 | 0.6497 | 0.0138 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.21 | 0.6590 | 0.0126 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.05 | 0.6524 | 0.0133 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.10 | 0.6550 | 0.0129 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 29.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.75 | 0.7592 | 0.0184 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.11 | 0.4075 | 0.2409 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.28 | 0.4327 | 0.2318 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.18 | 0.4238 | 0.2374 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.22 | 0.4267 | 0.2349 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.04 | 0.4004 | 0.2387 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.15 | 0.4258 | 0.2302 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.07 | 0.4194 | 0.2351 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.10 | 0.4244 | 0.2328 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.89 | 0.2349 | 0.1876 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.82 | 0.4565 | 0.1945 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.10 | 0.4774 | 0.1806 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.92 | 0.4752 | 0.1887 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.99 | 0.4763 | 0.1849 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.81 | 0.4864 | 0.1879 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.14 | 0.5365 | 0.1707 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.88 | 0.5166 | 0.1818 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.98 | 0.5257 | 0.1776 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.69 | 0.3409 | 0.1593 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.15 | 0.3932 | 0.2355 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.45 | 0.4184 | 0.2239 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.24 | 0.4081 | 0.2315 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.33 | 0.4131 | 0.2282 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.04 | 0.3905 | 0.2313 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.32 | 0.4083 | 0.2217 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.09 | 0.4048 | 0.2284 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.17 | 0.4060 | 0.2259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.12 | 0.7528 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.54 | 0.7607 | 0.0207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.42 | 0.7581 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.47 | 0.7592 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.49 | 0.7517 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.81 | 0.7640 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.71 | 0.7586 | 0.0207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.79 | 0.7624 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.75 | 0.7433 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.44 | 0.7399 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.60 | 0.7439 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.68 | 0.7435 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.73 | 0.7434 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.41 | 0.7488 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.36 | 0.7670 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.92 | 0.7576 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.09 | 0.7619 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.65 | 0.7412 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.54 | 0.7511 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.91 | 0.7582 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.72 | 0.7546 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.80 | 0.7562 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.82 | 0.7555 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.08 | 0.7597 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.95 | 0.7576 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.01 | 0.7589 | 0.0199 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.02 | 0.7338 | 0.0278 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.62 | 0.7449 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.37 | 0.7421 | 0.0264 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.42 | 0.7431 | 0.0255 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.22 | 0.7264 | 0.0265 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.57 | 0.7407 | 0.0236 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.52 | 0.7367 | 0.0249 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.56 | 0.7401 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.17 | 0.7017 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.89 | 0.7020 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.28 | 0.7098 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.30 | 0.7105 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.35 | 0.7097 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.75 | 0.7181 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.02 | 0.7488 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.72 | 0.7369 | 0.0299 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.74 | 0.7429 | 0.0287 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.30 | 0.6756 | 0.0524 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.62 | 0.7254 | 0.0313 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.74 | 0.7327 | 0.0303 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.82 | 0.7314 | 0.0300 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.86 | 0.7334 | 0.0291 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.90 | 0.7293 | 0.0284 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.57 | 0.7335 | 0.0292 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.99 | 0.7346 | 0.0290 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.83 | 0.7352 | 0.0291 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 43.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.41 | 0.7277 | 0.0289 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.22 | 0.3117 | 0.3736 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.26 | 0.3248 | 0.3646 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.24 | 0.3211 | 0.3698 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.25 | 0.3227 | 0.3673 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.22 | 0.3098 | 0.3689 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.25 | 0.3236 | 0.3613 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.23 | 0.3195 | 0.3658 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.24 | 0.3223 | 0.3637 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.33 | 0.1910 | 0.2524 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.57 | 0.3683 | 0.3361 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.63 | 0.3772 | 0.3245 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.59 | 0.3780 | 0.3316 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.61 | 0.3777 | 0.3284 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.59 | 0.3988 | 0.3262 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.67 | 0.4260 | 0.3116 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.62 | 0.4167 | 0.3211 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.63 | 0.4216 | 0.3170 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.62 | 0.3095 | 0.2194 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.33 | 0.3097 | 0.3703 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.46 | 0.3235 | 0.3602 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.39 | 0.3184 | 0.3671 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.42 | 0.3210 | 0.3641 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.30 | 0.3125 | 0.3679 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.35 | 0.3224 | 0.3601 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.31 | 0.3193 | 0.3663 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.33 | 0.3204 | 0.3639 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.22 | 0.7245 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.60 | 0.7289 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.51 | 0.7277 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.54 | 0.7283 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.32 | 0.7226 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.64 | 0.7294 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.55 | 0.7265 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.62 | 0.7286 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.13 | 0.7230 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.53 | 0.7163 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.73 | 0.7188 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.70 | 0.7185 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.73 | 0.7187 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.16 | 0.7203 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.94 | 0.7303 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.57 | 0.7250 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.74 | 0.7275 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.08 | 0.7225 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.31 | 0.7235 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.63 | 0.7273 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.46 | 0.7254 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.52 | 0.7263 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.58 | 0.7259 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.75 | 0.7273 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.69 | 0.7266 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.72 | 0.7270 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.53 | 0.7149 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.00 | 0.7214 | 0.0334 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.87 | 0.7198 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.90 | 0.7206 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.58 | 0.7114 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.88 | 0.7202 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.80 | 0.7168 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.86 | 0.7193 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.84 | 0.7172 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.43 | 0.6965 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.66 | 0.6997 | 0.0411 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.70 | 0.7007 | 0.0440 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.71 | 0.7003 | 0.0427 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.27 | 0.7062 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.31 | 0.7236 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.86 | 0.7162 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.04 | 0.7200 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.71 | 0.7142 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.79 | 0.7147 | 0.0376 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.23 | 0.7217 | 0.0344 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.02 | 0.7185 | 0.0365 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.12 | 0.7204 | 0.0356 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.96 | 0.7160 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.27 | 0.7206 | 0.0349 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.06 | 0.7182 | 0.0372 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.15 | 0.7194 | 0.0362 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.91 | 0.7355 | 0.0339 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.87 | 0.3150 | 0.3969 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.90 | 0.3200 | 0.3895 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.88 | 0.3215 | 0.3937 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.89 | 0.3212 | 0.3915 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.88 | 0.3117 | 0.3934 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.90 | 0.3180 | 0.3863 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.89 | 0.3184 | 0.3906 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.89 | 0.3187 | 0.3884 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.19 | 0.1577 | 0.2845 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.68 | 0.3549 | 0.3586 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.73 | 0.3561 | 0.3490 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.70 | 0.3619 | 0.3544 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.71 | 0.3595 | 0.3514 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.68 | 0.3653 | 0.3526 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.74 | 0.3783 | 0.3407 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.70 | 0.3765 | 0.3485 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.72 | 0.3782 | 0.3448 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.14 | 0.2475 | 0.2530 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.85 | 0.3097 | 0.3966 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.95 | 0.3119 | 0.3887 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.89 | 0.3140 | 0.3935 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.92 | 0.3136 | 0.3908 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.84 | 0.3128 | 0.3903 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.87 | 0.3148 | 0.3845 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.85 | 0.3172 | 0.3885 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.86 | 0.3162 | 0.3866 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.84 | 0.7347 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.89 | 0.7351 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.88 | 0.7351 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.89 | 0.7351 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.89 | 0.7352 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.90 | 0.7355 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.90 | 0.7354 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.90 | 0.7355 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.90 | 0.7355 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.77 | 0.7341 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.84 | 0.7346 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.81 | 0.7345 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.83 | 0.7346 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.84 | 0.7346 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7351 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.84 | 0.7348 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.86 | 0.7350 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.90 | 0.7355 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.87 | 0.7350 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.90 | 0.7354 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.89 | 0.7352 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.90 | 0.7353 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.90 | 0.7352 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.89 | 0.7351 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.89 | 0.7351 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.89 | 0.7351 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.54 | 0.7321 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.70 | 0.7334 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.73 | 0.7336 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.72 | 0.7337 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.61 | 0.7322 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.66 | 0.7335 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.65 | 0.7335 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.65 | 0.7336 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.76 | 0.7345 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.09 | 0.7272 | 0.0417 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.20 | 0.7275 | 0.0400 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.29 | 0.7289 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.28 | 0.7284 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.26 | 0.7292 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.61 | 0.7331 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.45 | 0.7317 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.56 | 0.7327 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.71 | 0.7345 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.70 | 0.7330 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.76 | 0.7339 | 0.0364 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.76 | 0.7339 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.77 | 0.7340 | 0.0366 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.73 | 0.7332 | 0.0360 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.78 | 0.7342 | 0.0358 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.77 | 0.7340 | 0.0362 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.78 | 0.7342 | 0.0359 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.68 | 0.7307 | 0.0491 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.19 | 0.3145 | 0.4679 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.23 | 0.3247 | 0.4538 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.21 | 0.3230 | 0.4622 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.22 | 0.3241 | 0.4583 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.18 | 0.3103 | 0.4582 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.21 | 0.3230 | 0.4461 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.20 | 0.3200 | 0.4538 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.20 | 0.3224 | 0.4503 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.37 | 0.1780 | 0.3783 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.10 | 0.3563 | 0.4252 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.16 | 0.3623 | 0.4061 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.13 | 0.3653 | 0.4188 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.14 | 0.3642 | 0.4127 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.11 | 0.3732 | 0.4104 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.17 | 0.3956 | 0.3890 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.13 | 0.3879 | 0.4042 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.15 | 0.3924 | 0.3975 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.46 | 0.2736 | 0.3300 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.16 | 0.3054 | 0.4673 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.28 | 0.3134 | 0.4546 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.21 | 0.3120 | 0.4628 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.24 | 0.3131 | 0.4587 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.14 | 0.3081 | 0.4566 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.18 | 0.3144 | 0.4448 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.15 | 0.3140 | 0.4534 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.17 | 0.3142 | 0.4496 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.49 | 0.7285 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.70 | 0.7310 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.66 | 0.7303 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.68 | 0.7307 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.57 | 0.7278 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.76 | 0.7318 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.71 | 0.7302 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.75 | 0.7314 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.24 | 0.7271 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.03 | 0.7234 | 0.0574 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.12 | 0.7248 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.13 | 0.7246 | 0.0563 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.15 | 0.7247 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.45 | 0.7258 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.90 | 0.7314 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.66 | 0.7282 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.77 | 0.7298 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.21 | 0.7271 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.58 | 0.7277 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.75 | 0.7300 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.66 | 0.7289 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.70 | 0.7295 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.75 | 0.7292 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.80 | 0.7297 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.78 | 0.7294 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.79 | 0.7296 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.07 | 0.7229 | 0.0603 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.36 | 0.7269 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.32 | 0.7263 | 0.0582 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.34 | 0.7268 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.10 | 0.7211 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.35 | 0.7269 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.28 | 0.7249 | 0.0554 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.33 | 0.7264 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.01 | 0.7236 | 0.0569 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.29 | 0.7109 | 0.0714 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.43 | 0.7128 | 0.0653 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.49 | 0.7137 | 0.0696 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.49 | 0.7134 | 0.0677 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.81 | 0.7158 | 0.0659 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.52 | 0.7268 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.17 | 0.7216 | 0.0631 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.33 | 0.7244 | 0.0605 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.92 | 0.7223 | 0.0601 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.26 | 0.7223 | 0.0604 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.50 | 0.7260 | 0.0567 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.39 | 0.7245 | 0.0592 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.45 | 0.7256 | 0.0582 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.39 | 0.7234 | 0.0588 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.54 | 0.7261 | 0.0563 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.43 | 0.7247 | 0.0587 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.48 | 0.7254 | 0.0577 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 249871 | 0.167 | 33.8 | 28.89 | 0.09 | 0.026 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 249871 | 0.167 | 40.4 | 28.89 | 0.09 | 0.026 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 249871 | 0.167 | 37.2 | 28.89 | 0.09 | 0.026 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 249871 | 0.167 | 37.1 | 28.89 | 0.09 | 0.026 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 860 | None | classic | 1.11 | False | 349921 | 0.348 | 71.1 | 28.53 | 0.13 | 0.026 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 860 | None | classic | 1.11 | False | 349921 | 0.348 | 74.8 | 28.53 | 0.13 | 0.026 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 860 | None | classic | 1.11 | False | 349921 | 0.348 | 68.8 | 28.53 | 0.13 | 0.026 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 860 | None | classic | 1.11 | False | 349921 | 0.348 | 69.5 | 28.53 | 0.13 | 0.026 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1011356 | 0.815 | 159.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 252074 | 0.173 | 37.9 | 27.92 | 0.18 | 0.026 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 252074 | 0.173 | 33.1 | 27.92 | 0.18 | 0.026 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 252074 | 0.173 | 37.4 | 27.92 | 0.18 | 0.026 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 252074 | 0.173 | 33.8 | 27.92 | 0.18 | 0.026 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1065 | None | classic | 1.70 | False | 452806 | 0.342 | 82.3 | 28.84 | 0.10 | 0.029 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1065 | None | classic | 1.70 | False | 452806 | 0.342 | 76.8 | 28.84 | 0.10 | 0.029 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1065 | None | classic | 1.70 | False | 452806 | 0.342 | 65.0 | 28.84 | 0.10 | 0.029 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1065 | None | classic | 1.70 | False | 452806 | 0.342 | 66.8 | 28.84 | 0.10 | 0.029 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1562879 | 0.815 | 75.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 243727 | 0.322 | 44.0 | 28.72 | 0.10 | 0.023 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 243727 | 0.322 | 34.6 | 28.72 | 0.10 | 0.023 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 243727 | 0.322 | 32.2 | 28.72 | 0.10 | 0.023 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 243727 | 0.322 | 33.3 | 28.72 | 0.10 | 0.023 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 708 | None | classic | 0.75 | False | 504745 | 0.504 | 104.7 | 28.51 | 0.16 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 708 | None | classic | 0.75 | False | 504745 | 0.504 | 103.5 | 28.51 | 0.16 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 708 | None | classic | 0.75 | False | 504745 | 0.504 | 91.1 | 28.51 | 0.16 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 708 | None | classic | 0.75 | False | 504745 | 0.504 | 87.0 | 28.51 | 0.16 | 0.013 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.577 | 0.025 |
| in035 | mask_ent | 0.735 | 0.025 |
| in035 | mask_grad | 0.435 | 0.025 |
| in035 | r_col | 0.675 | 0.025 |
| in035 | r_warp | 0.838 | 0.025 |

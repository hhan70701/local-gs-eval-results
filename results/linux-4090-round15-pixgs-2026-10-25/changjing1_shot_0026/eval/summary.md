# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 7.8% | 25.34 / 0.0093 | 20.50 / 0.0321 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.3% | 25.42 / 0.0095 | 21.79 / 0.0247 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.9% | 25.38 / 0.0094 | 21.37 / 0.0280 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.0% | 25.39 / 0.0093 | 21.63 / 0.0256 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.6% | 25.23 / 0.0090 | 21.86 / 0.0224 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.1% | 25.34 / 0.0091 | 23.30 / 0.0171 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.8% | 25.26 / 0.0091 | 23.40 / 0.0178 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.9% | 25.30 / 0.0089 | 23.33 / 0.0174 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 8.5% | 25.14 / 0.0110 | 19.94 / 0.0394 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 13.7% | 25.80 / 0.0101 | 19.94 / 0.0411 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.3% | 25.86 / 0.0104 | 21.44 / 0.0318 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 13.9% | 25.83 / 0.0100 | 21.07 / 0.0358 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.0% | 25.85 / 0.0101 | 21.30 / 0.0335 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 13.8% | 25.83 / 0.0103 | 21.66 / 0.0308 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.3% | 25.86 / 0.0105 | 22.85 / 0.0232 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.0% | 25.85 / 0.0104 | 22.82 / 0.0248 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.0% | 25.86 / 0.0104 | 22.95 / 0.0230 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 14.2% | 25.77 / 0.0111 | 20.14 / 0.0509 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 6.4% | 24.81 / 0.0068 | 19.97 / 0.0286 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 7.8% | 25.11 / 0.0075 | 21.02 / 0.0275 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 7.0% | 25.08 / 0.0071 | 20.94 / 0.0267 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 7.3% | 25.15 / 0.0073 | 21.09 / 0.0268 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 7.1% | 24.87 / 0.0079 | 20.76 / 0.0298 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 8.3% | 25.22 / 0.0086 | 21.07 / 0.0288 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 7.7% | 25.03 / 0.0076 | 21.40 / 0.0277 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 7.9% | 25.10 / 0.0078 | 21.35 / 0.0277 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.36 / 0.0499 | 28.83 / 0.0316 | 20.30 / 0.0110 | 30.03 / 0.0336 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.06 / 0.0654 | 28.08 / 0.0459 | 19.29 / 0.0145 | 29.62 / 0.0377 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.52 / 0.0597 | 28.26 / 0.0389 | 19.68 / 0.0124 | 29.73 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.38 / 0.0624 | 28.22 / 0.0430 | 19.50 / 0.0133 | 29.71 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.46 / 0.0611 | 28.26 / 0.0414 | 19.58 / 0.0128 | 29.72 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.65 / 0.0588 | 28.88 / 0.0387 | 20.09 / 0.0130 | 29.78 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.06 / 0.0547 | 29.28 / 0.0344 | 20.52 / 0.0112 | 29.88 / 0.0353 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.08 / 0.0563 | 29.20 / 0.0363 | 20.52 / 0.0117 | 29.90 / 0.0354 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.06 / 0.0556 | 29.25 / 0.0353 | 20.51 / 0.0116 | 29.89 / 0.0354 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.25 / 0.0590 | 28.46 / 0.0386 | 19.11 / 0.0156 | 29.73 / 0.0354 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.92 / 0.0772 | 26.09 / 0.0807 | 18.41 / 0.0192 | 29.13 / 0.0416 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.78 / 0.0670 | 26.91 / 0.0656 | 18.96 / 0.0158 | 29.49 / 0.0387 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.54 / 0.0719 | 26.77 / 0.0732 | 18.71 / 0.0171 | 29.44 / 0.0397 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.68 / 0.0693 | 26.90 / 0.0691 | 18.81 / 0.0162 | 29.47 / 0.0392 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.90 / 0.0672 | 26.64 / 0.0710 | 19.71 / 0.0156 | 29.52 / 0.0384 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.57 / 0.0594 | 27.61 / 0.0551 | 20.14 / 0.0130 | 29.77 / 0.0364 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.45 / 0.0630 | 27.34 / 0.0628 | 20.04 / 0.0141 | 29.75 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.53 / 0.0609 | 27.53 / 0.0574 | 20.10 / 0.0134 | 29.77 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.74 / 0.0634 | 27.14 / 0.0720 | 18.80 / 0.0168 | 29.55 / 0.0368 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.17 / 0.0663 | 26.44 / 0.0802 | 19.63 / 0.0153 | 29.67 / 0.0369 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.60 / 0.0606 | 26.84 / 0.0715 | 20.10 / 0.0131 | 29.67 / 0.0362 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.47 / 0.0644 | 26.65 / 0.0781 | 19.97 / 0.0141 | 29.69 / 0.0365 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.54 / 0.0628 | 26.80 / 0.0741 | 20.06 / 0.0134 | 29.68 / 0.0364 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.42 / 0.0634 | 26.61 / 0.0787 | 20.14 / 0.0135 | 29.58 / 0.0373 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.70 / 0.0592 | 27.24 / 0.0668 | 20.10 / 0.0125 | 29.68 / 0.0365 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.65 / 0.0623 | 27.10 / 0.0737 | 20.18 / 0.0128 | 29.67 / 0.0369 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.66 / 0.0610 | 27.32 / 0.0687 | 20.15 / 0.0128 | 29.67 / 0.0367 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.4%） | — | — | 28.36 / 0.0499 | 28.83 / 0.0316 | 30.03 |
| in035 | rife | 3.4% | 6.4% | 27.17 / 0.0663 | 26.44 / 0.0802 | 29.67 |
| in035 | cnw_cnn | 4.8% | 7.8% | 27.06 / 0.0654 | 28.08 / 0.0459 | 29.62 |
| in035 | cnw_f5 | 8.5% | 13.7% | 25.92 / 0.0772 | 26.09 / 0.0807 | 29.13 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.77 / 0.0529 | -1.11 / +0.0181 (core 2.5%) | -1.21 / +0.0184 (core 4.0%) | -2.41 / +0.0326 (core 8.3%) |
| in035 | 2 | 0-3 | 28.32 / 0.0476 | -1.50 / +0.0181 (core 2.5%) | -1.57 / +0.0175 (core 4.0%) | -2.99 / +0.0306 (core 8.3%) |
| in035 | 4 | 3-5 | 28.99 / 0.0491 | -0.95 / +0.0133 (core 2.8%) | -1.12 / +0.0108 (core 3.6%) | -1.91 / +0.0189 (core 6.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.36 / 0.0499 | 28.83 | 30.03 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.06 / 0.0654 | 28.08 | 29.62 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 27.80 / 0.0549 | 28.75 | 30.01 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.52 / 0.0597 | 28.26 | 29.73 | 0/3 |
| in035 | cnw_cnn | oracle | 1.4% | 28.03 / 0.0521 | 28.90 | 30.02 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.38 / 0.0624 | 28.22 | 29.71 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 27.94 / 0.0533 | 28.87 | 30.02 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.46 / 0.0611 | 28.26 | 29.72 | 0/3 |
| in035 | cnw_cnn | oracle | 1.4% | 27.99 / 0.0527 | 28.93 | 30.02 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.65 / 0.0588 | 28.88 | 29.78 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 28.16 / 0.0520 | 29.38 | 30.02 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.06 / 0.0547 | 29.28 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 28.40 / 0.0501 | 29.60 | 30.03 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.08 / 0.0563 | 29.20 | 29.90 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 28.39 / 0.0508 | 29.59 | 30.03 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.06 / 0.0556 | 29.25 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 28.39 / 0.0506 | 29.63 | 30.03 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.25 / 0.0590 | 28.46 | 29.73 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.4% | 27.78 / 0.0540 | 28.69 | 30.01 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.92 / 0.0772 | 26.09 | 29.13 | 0/3 |
| in035 | cnw_f5 | oracle | 2.1% | 27.33 / 0.0591 | 27.84 | 29.99 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.78 / 0.0670 | 26.91 | 29.49 | 0/3 |
| in035 | cnw_f5 | oracle | 2.2% | 27.70 / 0.0550 | 28.34 | 30.01 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.54 / 0.0719 | 26.77 | 29.44 | 0/3 |
| in035 | cnw_f5 | oracle | 2.2% | 27.56 / 0.0570 | 28.24 | 30.00 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.68 / 0.0693 | 26.90 | 29.47 | 0/3 |
| in035 | cnw_f5 | oracle | 2.2% | 27.62 / 0.0559 | 28.36 | 30.00 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.90 / 0.0672 | 26.64 | 29.52 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.1% | 27.91 / 0.0550 | 28.19 | 30.02 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.57 / 0.0594 | 27.61 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.2% | 28.20 / 0.0520 | 28.68 | 30.03 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.45 / 0.0630 | 27.34 | 29.75 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.1% | 28.13 / 0.0534 | 28.40 | 30.03 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.53 / 0.0609 | 27.53 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.1% | 28.17 / 0.0527 | 28.58 | 30.03 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.74 / 0.0634 | 27.14 | 29.55 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.1% | 27.55 / 0.0552 | 28.77 | 29.95 | 0/3 |
| in035 | rife | 不复核 | —% | 27.17 / 0.0663 | 26.44 | 29.67 | 0/3 |
| in035 | rife | oracle | 0.9% | 28.02 / 0.0543 | 28.90 | 30.03 | 0/3 |
| in035 | rife | 不复核 | —% | 27.60 / 0.0606 | 26.84 | 29.67 | 0/3 |
| in035 | rife | oracle | 1.0% | 28.23 / 0.0524 | 29.09 | 30.03 | 0/3 |
| in035 | rife | 不复核 | —% | 27.47 / 0.0644 | 26.65 | 29.69 | 0/3 |
| in035 | rife | oracle | 1.0% | 28.17 / 0.0534 | 28.96 | 30.02 | 0/3 |
| in035 | rife | 不复核 | —% | 27.54 / 0.0628 | 26.80 | 29.68 | 0/3 |
| in035 | rife | oracle | 1.0% | 28.21 / 0.0529 | 29.01 | 30.02 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.42 / 0.0634 | 26.61 | 29.58 | 0/3 |
| in035 | rife_mw | oracle | 1.0% | 28.21 / 0.0522 | 29.25 | 30.02 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.70 / 0.0592 | 27.24 | 29.68 | 0/3 |
| in035 | rife_mw | oracle | 1.1% | 28.25 / 0.0510 | 29.54 | 30.03 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.65 / 0.0623 | 27.10 | 29.67 | 0/3 |
| in035 | rife_mw | oracle | 1.0% | 28.27 / 0.0517 | 29.43 | 30.02 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.66 / 0.0610 | 27.32 | 29.67 | 0/3 |
| in035 | rife_mw | oracle | 1.0% | 28.26 / 0.0514 | 29.51 | 30.03 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.36 / 0.0499 | 28.83 / 0.0316 | — |
| in035 | FF | 0（前馈） | 976×641（59%） | 26.13 | 27.06 / 0.0654 | 28.08 / 0.0459 | 0/3 |
| in035 | 25 | 0.58 s | 976×641（59%） | 26.85 | 27.38 / 0.0624 | 28.22 / 0.0430 | 0/3 |
| in035 | 50 | 1.16 s | 976×641（59%） | 27.23 | 27.46 / 0.0611 | 28.26 / 0.0414 | 0/3 |
| in035 | 100 | 2.30 s | 976×641（59%） | 27.62 | 27.52 / 0.0597 | 28.26 / 0.0389 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.36 / 0.0499 | 28.83 / 0.0316 | 30.03 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.06 / 0.0654 | 28.08 / 0.0459 | 29.62 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.80 / 0.0549 | 28.75 / 0.0368 | 30.01 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.38 / 0.0624 | 28.22 / 0.0430 | 29.71 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.94 / 0.0533 | 28.87 / 0.0359 | 30.02 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.46 / 0.0611 | 28.26 / 0.0414 | 29.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.99 / 0.0527 | 28.93 / 0.0353 | 30.02 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.52 / 0.0597 | 28.26 / 0.0389 | 29.73 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.03 / 0.0521 | 28.90 / 0.0334 | 30.02 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.65 / 0.0588 | 28.88 / 0.0387 | 29.78 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.16 / 0.0520 | 29.38 / 0.0338 | 30.02 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.08 / 0.0563 | 29.20 / 0.0363 | 29.90 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.39 / 0.0508 | 29.59 / 0.0323 | 30.03 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.06 / 0.0556 | 29.25 / 0.0353 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.39 / 0.0506 | 29.63 / 0.0319 | 30.03 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.06 / 0.0547 | 29.28 / 0.0344 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.40 / 0.0501 | 29.60 / 0.0316 | 30.03 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 25.92 / 0.0772 | 26.09 / 0.0807 | 29.13 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.33 / 0.0591 | 27.84 / 0.0481 | 29.99 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.54 / 0.0719 | 26.77 / 0.0732 | 29.44 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.56 / 0.0570 | 28.24 / 0.0447 | 30.00 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.68 / 0.0693 | 26.90 / 0.0691 | 29.47 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.62 / 0.0559 | 28.36 / 0.0434 | 30.00 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.78 / 0.0670 | 26.91 / 0.0656 | 29.49 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.70 / 0.0550 | 28.34 / 0.0424 | 30.01 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.90 / 0.0672 | 26.64 / 0.0710 | 29.52 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.91 / 0.0550 | 28.19 / 0.0443 | 30.02 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.45 / 0.0630 | 27.34 / 0.0628 | 29.75 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.13 / 0.0534 | 28.40 / 0.0424 | 30.03 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.53 / 0.0609 | 27.53 / 0.0574 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.17 / 0.0527 | 28.58 / 0.0407 | 30.03 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.57 / 0.0594 | 27.61 / 0.0551 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.20 / 0.0520 | 28.68 / 0.0400 | 30.03 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.17 / 0.0663 | 26.44 / 0.0802 | 29.67 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.02 / 0.0543 | 28.90 / 0.0370 | 30.03 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.47 / 0.0644 | 26.65 / 0.0781 | 29.69 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.17 / 0.0534 | 28.96 / 0.0374 | 30.02 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.54 / 0.0628 | 26.80 / 0.0741 | 29.68 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.21 / 0.0529 | 29.01 / 0.0364 | 30.02 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.60 / 0.0606 | 26.84 / 0.0715 | 29.67 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.23 / 0.0524 | 29.09 / 0.0353 | 30.03 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.42 / 0.0634 | 26.61 / 0.0787 | 29.58 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.21 / 0.0522 | 29.25 / 0.0352 | 30.02 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.65 / 0.0623 | 27.10 / 0.0737 | 29.67 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.27 / 0.0517 | 29.43 / 0.0351 | 30.02 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.66 / 0.0610 | 27.32 / 0.0687 | 29.67 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.26 / 0.0514 | 29.51 / 0.0342 | 30.03 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.70 / 0.0592 | 27.24 / 0.0668 | 29.68 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.25 / 0.0510 | 29.54 / 0.0329 | 30.03 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.83 / 0.0316 | 20.30 / 0.0110 | 30.03 / 0.0336 | 28.36 / 0.0499 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 10.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.83 | 0.8556 | 0.0316 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.57 | 0.4323 | 0.4900 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.87 | 0.4471 | 0.4647 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.69 | 0.4450 | 0.4790 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.78 | 0.4469 | 0.4703 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.73 | 0.3336 | 0.4444 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.83 | 0.3599 | 0.4317 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.82 | 0.3530 | 0.4359 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.85 | 0.3592 | 0.4316 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 9.51 | 0.2571 | 0.4226 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 18.39 | 0.6521 | 0.2280 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 20.25 | 0.6928 | 0.1703 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 19.38 | 0.6841 | 0.2038 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 19.81 | 0.6917 | 0.1860 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 18.53 | 0.6874 | 0.2003 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.73 | 0.7365 | 0.1548 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 19.43 | 0.7246 | 0.1808 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 19.67 | 0.7345 | 0.1661 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.57 | 0.7258 | 0.1839 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.97 | 0.5747 | 0.3182 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 13.74 | 0.6199 | 0.2739 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 13.40 | 0.6055 | 0.2989 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 13.47 | 0.6143 | 0.2874 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 13.23 | 0.5901 | 0.2916 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 13.79 | 0.6314 | 0.2528 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 13.54 | 0.6226 | 0.2768 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 13.60 | 0.6304 | 0.2667 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.75 | 0.8547 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.90 | 0.8555 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.87 | 0.8551 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.93 | 0.8554 | 0.0353 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.38 | 0.8601 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.60 | 0.8619 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.59 | 0.8615 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.63 | 0.8620 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.69 | 0.8577 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.84 | 0.8454 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.34 | 0.8478 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.24 | 0.8465 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.36 | 0.8472 | 0.0434 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.19 | 0.8492 | 0.0443 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.68 | 0.8534 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.40 | 0.8506 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.58 | 0.8523 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.77 | 0.8600 | 0.0383 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.90 | 0.8541 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.09 | 0.8567 | 0.0353 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.96 | 0.8542 | 0.0374 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.01 | 0.8551 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.25 | 0.8575 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.54 | 0.8618 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.43 | 0.8596 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.51 | 0.8608 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.08 | 0.8415 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.26 | 0.8437 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.22 | 0.8432 | 0.0430 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.26 | 0.8435 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.88 | 0.8523 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.28 | 0.8580 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.20 | 0.8561 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.25 | 0.8573 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.46 | 0.8540 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.09 | 0.8057 | 0.0807 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.91 | 0.8190 | 0.0656 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.77 | 0.8146 | 0.0732 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.90 | 0.8173 | 0.0691 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.64 | 0.8223 | 0.0710 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.61 | 0.8433 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.34 | 0.8358 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.53 | 0.8412 | 0.0574 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.14 | 0.8419 | 0.0720 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.44 | 0.8131 | 0.0802 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.84 | 0.8247 | 0.0715 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.65 | 0.8174 | 0.0781 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.80 | 0.8207 | 0.0741 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.61 | 0.8149 | 0.0787 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.24 | 0.8325 | 0.0668 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.10 | 0.8261 | 0.0737 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.32 | 0.8309 | 0.0687 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.30 | 0.6607 | 0.0110 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.12 | 0.2531 | 0.0973 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.31 | 0.2879 | 0.0924 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.22 | 0.2729 | 0.0947 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.27 | 0.2817 | 0.0935 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.25 | 0.3068 | 0.0873 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.32 | 0.3449 | 0.0833 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.31 | 0.3304 | 0.0850 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.30 | 0.3389 | 0.0841 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.38 | 0.2537 | 0.0616 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.49 | 0.3017 | 0.0784 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.78 | 0.3501 | 0.0711 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.62 | 0.3249 | 0.0753 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.69 | 0.3386 | 0.0732 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.10 | 0.3941 | 0.0646 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.27 | 0.4167 | 0.0600 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.07 | 0.4053 | 0.0621 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.08 | 0.4113 | 0.0614 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.98 | 0.3590 | 0.0465 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.64 | 0.2410 | 0.1062 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.54 | 0.2890 | 0.0964 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.91 | 0.2662 | 0.1025 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.18 | 0.2776 | 0.0997 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.50 | 0.2577 | 0.1041 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.60 | 0.2758 | 0.1007 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.55 | 0.2715 | 0.1029 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.57 | 0.2741 | 0.1021 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.33 | 0.6189 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.70 | 0.6396 | 0.0124 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.53 | 0.6288 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.60 | 0.6350 | 0.0128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.13 | 0.6668 | 0.0128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.52 | 0.6795 | 0.0112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.53 | 0.6773 | 0.0117 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.52 | 0.6788 | 0.0116 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.13 | 0.6331 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.45 | 0.5851 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.98 | 0.6132 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.73 | 0.5979 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.82 | 0.6052 | 0.0159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.74 | 0.6509 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.16 | 0.6680 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.06 | 0.6620 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.12 | 0.6660 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 18.82 | 0.6235 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.67 | 0.6396 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.13 | 0.6607 | 0.0129 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.99 | 0.6488 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.08 | 0.6546 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.16 | 0.6540 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.11 | 0.6561 | 0.0124 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.19 | 0.6548 | 0.0127 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.16 | 0.6542 | 0.0127 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.29 | 0.6158 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.68 | 0.6375 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.50 | 0.6259 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.58 | 0.6325 | 0.0128 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.09 | 0.6638 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.52 | 0.6786 | 0.0112 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.52 | 0.6760 | 0.0117 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.51 | 0.6776 | 0.0116 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.11 | 0.6295 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.41 | 0.5810 | 0.0192 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.96 | 0.6105 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.71 | 0.5950 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.81 | 0.6025 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.71 | 0.6479 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.14 | 0.6658 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.04 | 0.6598 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.10 | 0.6638 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.80 | 0.6188 | 0.0168 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.63 | 0.6372 | 0.0153 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.10 | 0.6593 | 0.0131 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.97 | 0.6473 | 0.0141 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.06 | 0.6532 | 0.0134 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.14 | 0.6510 | 0.0135 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.10 | 0.6547 | 0.0125 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.18 | 0.6531 | 0.0128 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.15 | 0.6525 | 0.0128 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 31.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.27 | 0.7764 | 0.0200 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.96 | 0.4215 | 0.2482 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.21 | 0.4473 | 0.2364 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.05 | 0.4424 | 0.2430 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.11 | 0.4464 | 0.2402 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.37 | 0.3969 | 0.2337 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.32 | 0.4246 | 0.2224 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.34 | 0.4233 | 0.2269 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.31 | 0.4249 | 0.2249 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.79 | 0.2896 | 0.1942 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.73 | 0.4754 | 0.2025 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.12 | 0.5033 | 0.1857 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.89 | 0.5000 | 0.1944 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.98 | 0.5036 | 0.1903 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.39 | 0.4823 | 0.1880 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.59 | 0.5169 | 0.1722 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.47 | 0.5139 | 0.1795 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.50 | 0.5175 | 0.1761 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.02 | 0.3947 | 0.1688 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.66 | 0.4162 | 0.2476 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.11 | 0.4483 | 0.2308 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.82 | 0.4386 | 0.2411 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.95 | 0.4449 | 0.2367 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.64 | 0.4220 | 0.2440 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.89 | 0.4461 | 0.2306 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.73 | 0.4447 | 0.2382 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.79 | 0.4463 | 0.2353 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.29 | 0.7623 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.68 | 0.7689 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.53 | 0.7666 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.60 | 0.7681 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.00 | 0.7732 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.36 | 0.7790 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.35 | 0.7779 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.35 | 0.7786 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.92 | 0.7626 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.52 | 0.7493 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.14 | 0.7606 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.90 | 0.7563 | 0.0277 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.99 | 0.7586 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.53 | 0.7652 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.00 | 0.7742 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.91 | 0.7716 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.97 | 0.7735 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.55 | 0.7570 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.61 | 0.7659 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.01 | 0.7717 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.91 | 0.7692 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.99 | 0.7708 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.01 | 0.7695 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.95 | 0.7718 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.08 | 0.7718 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.03 | 0.7720 | 0.0222 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.02 | 0.7361 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.65 | 0.7464 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.51 | 0.7446 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.63 | 0.7464 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.94 | 0.7530 | 0.0294 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.47 | 0.7642 | 0.0258 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.59 | 0.7646 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.54 | 0.7649 | 0.0261 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.23 | 0.7239 | 0.0426 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.45 | 0.6981 | 0.0436 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.51 | 0.7201 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.28 | 0.7155 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.44 | 0.7189 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.76 | 0.7293 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.49 | 0.7499 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.54 | 0.7478 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.58 | 0.7510 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.05 | 0.6888 | 0.0579 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.06 | 0.7328 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.35 | 0.7418 | 0.0376 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.50 | 0.7408 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.52 | 0.7428 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.47 | 0.7315 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.39 | 0.7420 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.73 | 0.7418 | 0.0365 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.61 | 0.7425 | 0.0362 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 42.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.89 | 0.7383 | 0.0282 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.33 | 0.3573 | 0.3572 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.43 | 0.3788 | 0.3436 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.38 | 0.3753 | 0.3503 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.40 | 0.3784 | 0.3471 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.92 | 0.3486 | 0.3179 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.76 | 0.3691 | 0.3070 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.86 | 0.3668 | 0.3117 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.80 | 0.3689 | 0.3094 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.74 | 0.2829 | 0.2331 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.45 | 0.4108 | 0.3136 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.56 | 0.4314 | 0.2983 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.51 | 0.4295 | 0.3059 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.53 | 0.4321 | 0.3023 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.54 | 0.4184 | 0.2746 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.62 | 0.4449 | 0.2587 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.59 | 0.4409 | 0.2665 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.60 | 0.4446 | 0.2629 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.47 | 0.3849 | 0.1967 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.03 | 0.3471 | 0.3614 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.31 | 0.3745 | 0.3450 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.14 | 0.3653 | 0.3555 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.22 | 0.3701 | 0.3515 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.02 | 0.3622 | 0.3562 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.10 | 0.3808 | 0.3460 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.06 | 0.3791 | 0.3526 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.07 | 0.3804 | 0.3500 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.94 | 0.7285 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.34 | 0.7328 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.19 | 0.7309 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.27 | 0.7321 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.63 | 0.7359 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 | 0.7391 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.97 | 0.7385 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.95 | 0.7389 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.19 | 0.7341 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.20 | 0.7205 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.92 | 0.7279 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.64 | 0.7246 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.77 | 0.7264 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.11 | 0.7305 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.56 | 0.7363 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.45 | 0.7343 | 0.0314 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.53 | 0.7357 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.08 | 0.7334 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.26 | 0.7322 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.72 | 0.7370 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.59 | 0.7346 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.67 | 0.7358 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.65 | 0.7341 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.78 | 0.7376 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.80 | 0.7364 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.80 | 0.7369 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.83 | 0.7127 | 0.0409 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.57 | 0.7205 | 0.0358 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.33 | 0.7181 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.47 | 0.7197 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.78 | 0.7254 | 0.0358 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.39 | 0.7320 | 0.0317 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.40 | 0.7314 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.38 | 0.7319 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.66 | 0.7264 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.25 | 0.6882 | 0.0493 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.57 | 0.7034 | 0.0411 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.20 | 0.6991 | 0.0446 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.43 | 0.7021 | 0.0427 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.62 | 0.7106 | 0.0417 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.63 | 0.7258 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.44 | 0.7219 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.59 | 0.7251 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.23 | 0.7193 | 0.0403 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.01 | 0.7139 | 0.0422 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.82 | 0.7239 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.58 | 0.7199 | 0.0403 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.72 | 0.7221 | 0.0388 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.40 | 0.7155 | 0.0398 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.98 | 0.7261 | 0.0356 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.84 | 0.7223 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.88 | 0.7240 | 0.0372 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.03 | 0.7368 | 0.0336 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.43 | 0.3389 | 0.3822 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.47 | 0.3436 | 0.3712 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.44 | 0.3462 | 0.3771 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.46 | 0.3454 | 0.3740 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.95 | 0.2899 | 0.3558 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.91 | 0.2982 | 0.3472 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.92 | 0.2996 | 0.3517 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.91 | 0.2996 | 0.3489 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.92 | 0.1916 | 0.2767 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.25 | 0.3940 | 0.3422 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.32 | 0.3996 | 0.3251 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.28 | 0.4043 | 0.3343 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.30 | 0.4030 | 0.3295 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.99 | 0.3584 | 0.3127 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.11 | 0.3707 | 0.2997 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.04 | 0.3718 | 0.3058 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.07 | 0.3722 | 0.3022 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.20 | 0.2923 | 0.2385 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.23 | 0.3216 | 0.3845 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.55 | 0.3347 | 0.3733 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.35 | 0.3300 | 0.3802 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.44 | 0.3320 | 0.3771 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.17 | 0.3291 | 0.3803 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.22 | 0.3347 | 0.3726 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.18 | 0.3373 | 0.3769 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.20 | 0.3369 | 0.3747 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 30.01 | 0.7365 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.02 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.02 | 0.7366 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.02 | 0.7366 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.02 | 0.7366 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.03 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.03 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.03 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.01 | 0.7367 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.99 | 0.7361 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.01 | 0.7366 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.00 | 0.7364 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.00 | 0.7365 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.02 | 0.7364 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.03 | 0.7368 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.03 | 0.7367 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.03 | 0.7368 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.95 | 0.7366 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.03 | 0.7366 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 30.03 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 30.02 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 30.02 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 30.02 | 0.7365 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.03 | 0.7367 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.02 | 0.7366 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.03 | 0.7366 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.62 | 0.7333 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.73 | 0.7342 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.71 | 0.7342 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.72 | 0.7342 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.78 | 0.7349 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7361 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.90 | 0.7363 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.89 | 0.7362 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.73 | 0.7357 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.13 | 0.7288 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.49 | 0.7313 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.44 | 0.7313 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.47 | 0.7315 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.52 | 0.7324 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7359 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.75 | 0.7355 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.77 | 0.7360 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.55 | 0.7356 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.67 | 0.7322 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.67 | 0.7330 | 0.0362 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.69 | 0.7329 | 0.0365 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.68 | 0.7330 | 0.0364 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.58 | 0.7321 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.68 | 0.7335 | 0.0365 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.67 | 0.7333 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.67 | 0.7334 | 0.0367 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.36 | 0.7393 | 0.0499 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.82 | 0.3386 | 0.4543 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.90 | 0.3501 | 0.4352 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.86 | 0.3498 | 0.4462 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.87 | 0.3508 | 0.4409 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.24 | 0.3034 | 0.4222 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.18 | 0.3176 | 0.4075 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.21 | 0.3168 | 0.4149 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.19 | 0.3179 | 0.4111 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.17 | 0.2194 | 0.3651 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.76 | 0.3950 | 0.4096 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.85 | 0.4077 | 0.3824 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.80 | 0.4089 | 0.3985 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.82 | 0.4096 | 0.3907 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.42 | 0.3760 | 0.3763 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.52 | 0.3943 | 0.3518 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.45 | 0.3926 | 0.3642 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.48 | 0.3944 | 0.3578 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.59 | 0.3234 | 0.3087 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.58 | 0.3233 | 0.4574 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.93 | 0.3427 | 0.4384 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.70 | 0.3356 | 0.4507 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.81 | 0.3390 | 0.4455 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.52 | 0.3337 | 0.4452 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.58 | 0.3438 | 0.4304 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.54 | 0.3444 | 0.4405 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.56 | 0.3448 | 0.4365 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.80 | 0.7345 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.03 | 0.7365 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.94 | 0.7357 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.99 | 0.7362 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.16 | 0.7380 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.40 | 0.7400 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.39 | 0.7396 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.39 | 0.7398 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.78 | 0.7362 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.33 | 0.7302 | 0.0591 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.70 | 0.7337 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.56 | 0.7322 | 0.0570 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.62 | 0.7330 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.91 | 0.7355 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.20 | 0.7387 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.13 | 0.7376 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.17 | 0.7383 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.55 | 0.7349 | 0.0552 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.02 | 0.7361 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.23 | 0.7381 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.17 | 0.7372 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.21 | 0.7377 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.21 | 0.7372 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.25 | 0.7386 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.27 | 0.7381 | 0.0517 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.26 | 0.7383 | 0.0514 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.06 | 0.7260 | 0.0654 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.52 | 0.7299 | 0.0597 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.38 | 0.7290 | 0.0624 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.46 | 0.7296 | 0.0611 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.65 | 0.7325 | 0.0588 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.06 | 0.7368 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.08 | 0.7365 | 0.0563 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.06 | 0.7367 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.25 | 0.7317 | 0.0590 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.92 | 0.7122 | 0.0772 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.78 | 0.7201 | 0.0670 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.54 | 0.7182 | 0.0719 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.68 | 0.7195 | 0.0693 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.90 | 0.7242 | 0.0672 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.57 | 0.7331 | 0.0594 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.45 | 0.7310 | 0.0630 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.53 | 0.7328 | 0.0609 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.74 | 0.7270 | 0.0634 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.17 | 0.7256 | 0.0663 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.60 | 0.7301 | 0.0606 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.47 | 0.7284 | 0.0644 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.54 | 0.7294 | 0.0628 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.42 | 0.7268 | 0.0634 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.70 | 0.7319 | 0.0592 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.65 | 0.7302 | 0.0623 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.66 | 0.7310 | 0.0610 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 279550 | 0.168 | 36.0 | 28.77 | 0.33 | 0.036 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 279550 | 0.168 | 38.3 | 28.77 | 0.33 | 0.036 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 279550 | 0.168 | 34.9 | 28.77 | 0.33 | 0.036 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 279550 | 0.168 | 34.4 | 28.77 | 0.33 | 0.036 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 893 | None | classic | 0.30 | False | 418608 | 0.503 | 93.8 | 29.15 | 0.59 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 893 | None | classic | 0.30 | False | 418608 | 0.503 | 102.7 | 29.15 | 0.59 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 893 | None | classic | 0.30 | False | 418608 | 0.503 | 93.3 | 29.15 | 0.59 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 893 | None | classic | 0.30 | False | 418608 | 0.503 | 105.0 | 29.15 | 0.59 | 0.011 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1205495 | 0.813 | 165.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 287660 | 0.165 | 44.3 | 28.75 | 0.31 | 0.042 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 287660 | 0.165 | 40.5 | 28.75 | 0.31 | 0.042 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 287660 | 0.165 | 38.1 | 28.75 | 0.31 | 0.042 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 287660 | 0.165 | 43.7 | 28.75 | 0.31 | 0.042 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1053 | None | classic | 0.30 | False | 575915 | 0.527 | 101.0 | 31.72 | 1.14 | 0.078 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1053 | None | classic | 0.30 | False | 575915 | 0.527 | 103.1 | 31.72 | 1.14 | 0.078 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1053 | None | classic | 0.30 | False | 575915 | 0.527 | 113.5 | 31.72 | 1.14 | 0.078 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1053 | None | classic | 0.30 | False | 575915 | 0.527 | 110.2 | 31.72 | 1.14 | 0.078 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1887199 | 0.813 | 77.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 261134 | 0.323 | 42.2 | 29.18 | 0.12 | 0.032 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 261134 | 0.323 | 34.1 | 29.18 | 0.12 | 0.032 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 261134 | 0.323 | 36.8 | 29.18 | 0.12 | 0.032 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 261134 | 0.323 | 39.8 | 29.18 | 0.12 | 0.032 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 951 | None | classic | 1.35 | False | 483472 | 0.510 | 96.4 | 28.90 | 0.21 | 0.016 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 951 | None | classic | 1.35 | False | 483472 | 0.510 | 89.5 | 28.90 | 0.21 | 0.016 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 951 | None | classic | 1.35 | False | 483472 | 0.510 | 93.7 | 28.90 | 0.21 | 0.016 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 951 | None | classic | 1.35 | False | 483472 | 0.510 | 94.3 | 28.90 | 0.21 | 0.016 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.635 | 0.017 |
| in035 | mask_ent | 0.665 | 0.017 |
| in035 | mask_grad | 0.447 | 0.017 |
| in035 | r_col | 0.801 | 0.017 |
| in035 | r_warp | 0.851 | 0.017 |

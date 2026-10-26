# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 4.4% | 24.84 / 0.0060 | 19.37 / 0.0178 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.8% | 25.04 / 0.0066 | 20.75 / 0.0150 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.6% | 24.93 / 0.0065 | 20.36 / 0.0162 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.6% | 24.97 / 0.0066 | 20.53 / 0.0157 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.6% | 24.95 / 0.0059 | 20.25 / 0.0150 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.0% | 25.12 / 0.0062 | 21.92 / 0.0108 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.8% | 25.05 / 0.0060 | 21.39 / 0.0112 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.8% | 25.08 / 0.0061 | 21.67 / 0.0109 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 4.9% | 25.31 / 0.0068 | 18.95 / 0.0267 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 9.6% | 25.98 / 0.0084 | 19.08 / 0.0321 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.0% | 26.08 / 0.0086 | 19.62 / 0.0261 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.8% | 26.03 / 0.0085 | 19.37 / 0.0292 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.9% | 26.05 / 0.0085 | 19.41 / 0.0278 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 9.4% | 25.94 / 0.0081 | 19.36 / 0.0279 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.1% | 26.09 / 0.0083 | 21.11 / 0.0215 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.7% | 26.02 / 0.0081 | 20.51 / 0.0245 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.9% | 26.05 / 0.0082 | 20.81 / 0.0227 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 9.8% | 26.08 / 0.0090 | 19.89 / 0.0386 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 4.7% | 25.40 / 0.0111 | 21.67 / 0.0259 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 5.1% | 25.77 / 0.0110 | 22.79 / 0.0231 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 4.8% | 25.60 / 0.0122 | 22.61 / 0.0244 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 4.9% | 25.66 / 0.0113 | 22.75 / 0.0229 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 5.2% | 25.60 / 0.0133 | 22.86 / 0.0211 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 5.6% | 25.89 / 0.0137 | 23.93 / 0.0202 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 5.4% | 25.74 / 0.0135 | 23.58 / 0.0206 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 5.5% | 25.80 / 0.0134 | 23.70 / 0.0207 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.61 / 0.0491 | 26.76 / 0.0485 | 21.34 / 0.0109 | 29.71 / 0.0344 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.75 / 0.0553 | 26.20 / 0.0742 | 20.23 / 0.0128 | 29.60 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.07 / 0.0532 | 27.19 / 0.0604 | 20.66 / 0.0122 | 29.63 / 0.0353 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.96 / 0.0545 | 27.26 / 0.0656 | 20.49 / 0.0123 | 29.63 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.00 / 0.0540 | 27.33 / 0.0621 | 20.55 / 0.0123 | 29.63 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.11 / 0.0532 | 26.85 / 0.0613 | 20.99 / 0.0124 | 29.63 / 0.0352 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.43 / 0.0506 | 27.61 / 0.0495 | 21.64 / 0.0109 | 29.67 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.33 / 0.0518 | 27.35 / 0.0557 | 21.36 / 0.0115 | 29.67 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.39 / 0.0512 | 27.43 / 0.0525 | 21.52 / 0.0112 | 29.67 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.05 / 0.0544 | 26.06 / 0.0903 | 21.01 / 0.0127 | 29.70 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.67 / 0.0651 | 25.38 / 0.1081 | 19.57 / 0.0161 | 29.00 / 0.0392 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.87 / 0.0601 | 26.48 / 0.0811 | 19.82 / 0.0146 | 29.22 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.81 / 0.0630 | 26.53 / 0.0956 | 19.68 / 0.0155 | 29.15 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.81 / 0.0617 | 26.54 / 0.0879 | 19.69 / 0.0152 | 29.19 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.66 / 0.0616 | 24.89 / 0.1028 | 19.75 / 0.0148 | 29.16 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.33 / 0.0573 | 27.07 / 0.0832 | 20.59 / 0.0130 | 29.37 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.12 / 0.0595 | 26.43 / 0.0976 | 20.20 / 0.0137 | 29.34 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.21 / 0.0583 | 26.70 / 0.0916 | 20.30 / 0.0134 | 29.36 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.54 / 0.0588 | 24.69 / 0.1408 | 20.70 / 0.0144 | 29.57 / 0.0363 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.98 / 0.0552 | 26.56 / 0.0837 | 20.68 / 0.0116 | 29.63 / 0.0354 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.18 / 0.0536 | 27.39 / 0.0622 | 21.02 / 0.0112 | 29.67 / 0.0351 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.11 / 0.0549 | 27.56 / 0.0723 | 20.90 / 0.0114 | 29.66 / 0.0352 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.14 / 0.0543 | 27.56 / 0.0668 | 20.96 / 0.0112 | 29.67 / 0.0352 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.33 / 0.0537 | 26.75 / 0.0714 | 21.33 / 0.0114 | 29.64 / 0.0353 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.52 / 0.0519 | 28.65 / 0.0517 | 21.65 / 0.0106 | 29.69 / 0.0350 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.46 / 0.0529 | 27.90 / 0.0620 | 21.53 / 0.0107 | 29.67 / 0.0353 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.50 / 0.0525 | 28.36 / 0.0581 | 21.62 / 0.0107 | 29.68 / 0.0352 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.9%） | — | — | 28.61 / 0.0491 | 26.76 / 0.0485 | 29.71 |
| in035 | rife | 1.8% | 4.7% | 27.98 / 0.0552 | 26.56 / 0.0837 | 29.63 |
| in035 | cnw_cnn | 2.6% | 4.4% | 27.75 / 0.0553 | 26.20 / 0.0742 | 29.60 |
| in035 | cnw_f5 | 5.8% | 9.6% | 26.67 / 0.0651 | 25.38 / 0.1081 | 29.00 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 28.01 / 0.0473 | -0.83 / +0.0089 (core 2.4%) | -0.77 / +0.0066 (core 3.0%) | -1.51 / +0.0174 (core 6.0%) |
| in035 | 2 | 0-3 | 28.55 / 0.0487 | -1.11 / +0.0084 (core 2.4%) | -1.52 / +0.0091 (core 3.0%) | -2.43 / +0.0201 (core 6.0%) |
| in035 | 4 | 3-5 | 29.27 / 0.0513 | +0.04 / +0.0010 (core 0.6%) | -0.29 / +0.0030 (core 1.1%) | -1.87 / +0.0105 (core 3.6%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.61 / 0.0491 | 26.76 | 29.71 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.75 / 0.0553 | 26.20 | 29.60 | 0/3 |
| in035 | cnw_cnn | oracle | 0.9% | 28.06 / 0.0514 | 27.13 | 29.71 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.07 / 0.0532 | 27.19 | 29.63 | 0/3 |
| in035 | cnw_cnn | oracle | 0.9% | 28.29 / 0.0504 | 27.88 | 29.71 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.96 / 0.0545 | 27.26 | 29.63 | 0/3 |
| in035 | cnw_cnn | oracle | 0.9% | 28.20 / 0.0509 | 27.93 | 29.71 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.00 / 0.0540 | 27.33 | 29.63 | 0/3 |
| in035 | cnw_cnn | oracle | 0.9% | 28.23 / 0.0507 | 27.97 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.11 / 0.0532 | 26.85 | 29.63 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.0% | 28.38 / 0.0506 | 27.54 | 29.71 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.43 / 0.0506 | 27.61 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.0% | 28.62 / 0.0491 | 28.12 | 29.71 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.33 / 0.0518 | 27.35 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.0% | 28.53 / 0.0497 | 27.93 | 29.71 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.39 / 0.0512 | 27.43 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.0% | 28.58 / 0.0494 | 28.02 | 29.71 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 28.05 / 0.0544 | 26.06 | 29.70 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 0.9% | 28.37 / 0.0509 | 27.18 | 29.71 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.67 / 0.0651 | 25.38 | 29.00 | 0/3 |
| in035 | cnw_f5 | oracle | 1.6% | 27.71 / 0.0547 | 27.39 | 29.67 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.87 / 0.0601 | 26.48 | 29.22 | 0/3 |
| in035 | cnw_f5 | oracle | 1.7% | 27.86 / 0.0525 | 28.13 | 29.69 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.81 / 0.0630 | 26.53 | 29.15 | 0/3 |
| in035 | cnw_f5 | oracle | 1.7% | 27.79 / 0.0538 | 28.20 | 29.67 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.81 / 0.0617 | 26.54 | 29.19 | 0/3 |
| in035 | cnw_f5 | oracle | 1.7% | 27.80 / 0.0532 | 28.18 | 29.68 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.66 / 0.0616 | 24.89 | 29.16 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.7% | 27.76 / 0.0534 | 26.94 | 29.67 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.33 / 0.0573 | 27.07 | 29.37 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.7% | 28.14 / 0.0513 | 28.33 | 29.69 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.12 / 0.0595 | 26.43 | 29.34 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.7% | 27.97 / 0.0522 | 27.99 | 29.68 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.21 / 0.0583 | 26.70 | 29.36 | 0/3 |
| in035 | cnw_f5_mw | oracle | 1.7% | 28.02 / 0.0516 | 28.14 | 29.68 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.54 / 0.0588 | 24.69 | 29.57 | 0/3 |
| in035 | cnw_f5_pix | oracle | 1.6% | 28.16 / 0.0524 | 26.98 | 29.71 | 0/3 |
| in035 | rife | 不复核 | —% | 27.98 / 0.0552 | 26.56 | 29.63 | 0/3 |
| in035 | rife | oracle | 0.8% | 28.27 / 0.0497 | 27.38 | 29.71 | 1/3 |
| in035 | rife | 不复核 | —% | 28.18 / 0.0536 | 27.39 | 29.67 | 1/3 |
| in035 | rife | oracle | 0.8% | 28.41 / 0.0493 | 27.93 | 29.71 | 1/3 |
| in035 | rife | 不复核 | —% | 28.11 / 0.0549 | 27.56 | 29.66 | 0/3 |
| in035 | rife | oracle | 0.8% | 28.36 / 0.0495 | 27.98 | 29.71 | 1/3 |
| in035 | rife | 不复核 | —% | 28.14 / 0.0543 | 27.56 | 29.67 | 0/3 |
| in035 | rife | oracle | 0.8% | 28.38 / 0.0494 | 27.99 | 29.71 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 28.33 / 0.0537 | 26.75 | 29.64 | 0/3 |
| in035 | rife_mw | oracle | 0.8% | 28.51 / 0.0492 | 27.74 | 29.70 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 28.52 / 0.0519 | 28.65 | 29.69 | 1/3 |
| in035 | rife_mw | oracle | 0.9% | 28.64 / 0.0487 | 28.95 | 29.71 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.46 / 0.0529 | 27.90 | 29.67 | 0/3 |
| in035 | rife_mw | oracle | 0.9% | 28.59 / 0.0489 | 28.41 | 29.71 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.50 / 0.0525 | 28.36 | 29.68 | 0/3 |
| in035 | rife_mw | oracle | 0.9% | 28.63 / 0.0487 | 28.78 | 29.71 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.61 / 0.0491 | 26.76 / 0.0485 | — |
| in035 | FF | 0（前馈） | 1008×593（56%） | 26.12 | 27.75 / 0.0553 | 26.20 / 0.0742 | 0/3 |
| in035 | 25 | 1.26 s | 1008×593（56%） | 26.54 | 27.96 / 0.0545 | 27.26 / 0.0656 | 0/3 |
| in035 | 50 | 2.52 s | 1008×593（56%） | 26.76 | 28.00 / 0.0540 | 27.33 / 0.0621 | 0/3 |
| in035 | 100 | 5.01 s | 1008×593（56%） | 27.00 | 28.07 / 0.0532 | 27.19 / 0.0604 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.61 / 0.0491 | 26.76 / 0.0485 | 29.71 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.75 / 0.0553 | 26.20 / 0.0742 | 29.60 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.06 / 0.0514 | 27.13 / 0.0574 | 29.71 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.96 / 0.0545 | 27.26 / 0.0656 | 29.63 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.20 / 0.0509 | 27.93 / 0.0516 | 29.71 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 28.00 / 0.0540 | 27.33 / 0.0621 | 29.63 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.23 / 0.0507 | 27.97 / 0.0496 | 29.71 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 28.07 / 0.0532 | 27.19 / 0.0604 | 29.63 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.29 / 0.0504 | 27.88 / 0.0492 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 28.11 / 0.0532 | 26.85 / 0.0613 | 29.63 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.38 / 0.0506 | 27.54 / 0.0484 | 29.71 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.33 / 0.0518 | 27.35 / 0.0557 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.53 / 0.0497 | 27.93 / 0.0462 | 29.71 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.39 / 0.0512 | 27.43 / 0.0525 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.58 / 0.0494 | 28.02 / 0.0445 | 29.71 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.43 / 0.0506 | 27.61 / 0.0495 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.62 / 0.0491 | 28.12 / 0.0429 | 29.71 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.67 / 0.0651 | 25.38 / 0.1081 | 29.00 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.71 / 0.0547 | 27.39 / 0.0585 | 29.67 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.81 / 0.0630 | 26.53 / 0.0956 | 29.15 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.79 / 0.0538 | 28.20 / 0.0521 | 29.67 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.81 / 0.0617 | 26.54 / 0.0879 | 29.19 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.80 / 0.0532 | 28.18 / 0.0502 | 29.68 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.87 / 0.0601 | 26.48 / 0.0811 | 29.22 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.86 / 0.0525 | 28.13 / 0.0488 | 29.69 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.66 / 0.0616 | 24.89 / 0.1028 | 29.16 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.76 / 0.0534 | 26.94 / 0.0585 | 29.67 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.12 / 0.0595 | 26.43 / 0.0976 | 29.34 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.97 / 0.0522 | 27.99 / 0.0525 | 29.68 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.21 / 0.0583 | 26.70 / 0.0916 | 29.36 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.02 / 0.0516 | 28.14 / 0.0513 | 29.68 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.33 / 0.0573 | 27.07 / 0.0832 | 29.37 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.14 / 0.0513 | 28.33 / 0.0495 | 29.69 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.98 / 0.0552 | 26.56 / 0.0837 | 29.63 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.27 / 0.0497 | 27.38 / 0.0548 | 29.71 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.11 / 0.0549 | 27.56 / 0.0723 | 29.66 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.36 / 0.0495 | 27.98 / 0.0488 | 29.71 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.14 / 0.0543 | 27.56 / 0.0668 | 29.67 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.38 / 0.0494 | 27.99 / 0.0472 | 29.71 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.18 / 0.0536 | 27.39 / 0.0622 | 29.67 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.41 / 0.0493 | 27.93 / 0.0467 | 29.71 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 28.33 / 0.0537 | 26.75 / 0.0714 | 29.64 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.51 / 0.0492 | 27.74 / 0.0490 | 29.70 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.46 / 0.0529 | 27.90 / 0.0620 | 29.67 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.59 / 0.0489 | 28.41 / 0.0468 | 29.71 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.50 / 0.0525 | 28.36 / 0.0581 | 29.68 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.63 / 0.0487 | 28.78 / 0.0451 | 29.71 | 2/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.52 / 0.0519 | 28.65 / 0.0517 | 29.69 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.64 / 0.0487 | 28.95 / 0.0418 | 29.71 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.76 / 0.0485 | 21.34 / 0.0109 | 29.71 / 0.0344 | 28.61 / 0.0491 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 3.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.76 | 0.7949 | 0.0485 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 15.30 | 0.6417 | 0.2429 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 15.20 | 0.6632 | 0.2134 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 15.23 | 0.6646 | 0.2310 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 15.17 | 0.6666 | 0.2227 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 14.88 | 0.6514 | 0.2043 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 15.13 | 0.6985 | 0.1775 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 14.98 | 0.6840 | 0.1925 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 15.05 | 0.6923 | 0.1842 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 16.26 | 0.6242 | 0.2375 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 23.65 | 0.7273 | 0.1510 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 24.85 | 0.7534 | 0.1153 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 24.51 | 0.7509 | 0.1375 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 24.64 | 0.7529 | 0.1282 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 23.49 | 0.7283 | 0.1386 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 25.53 | 0.7825 | 0.1038 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 24.69 | 0.7583 | 0.1267 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 25.00 | 0.7696 | 0.1167 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 24.16 | 0.7488 | 0.1630 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 23.47 | 0.7234 | 0.1473 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 23.93 | 0.7474 | 0.1037 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 24.28 | 0.7515 | 0.1252 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 24.20 | 0.7536 | 0.1134 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 23.52 | 0.7423 | 0.0960 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 25.68 | 0.7887 | 0.0667 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 24.74 | 0.7773 | 0.0818 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 25.34 | 0.7854 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.13 | 0.7914 | 0.0574 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.88 | 0.8018 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.93 | 0.8010 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.97 | 0.8017 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.54 | 0.7978 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.12 | 0.8105 | 0.0429 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.93 | 0.8049 | 0.0462 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.02 | 0.8078 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.18 | 0.7985 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.39 | 0.7968 | 0.0585 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.13 | 0.8063 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.20 | 0.8060 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.18 | 0.8062 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.94 | 0.7953 | 0.0585 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.33 | 0.8137 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.99 | 0.8059 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.14 | 0.8098 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.98 | 0.7959 | 0.0620 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.38 | 0.7990 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.93 | 0.8059 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.98 | 0.8057 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.99 | 0.8062 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.74 | 0.7995 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.95 | 0.8214 | 0.0418 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.41 | 0.8107 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.78 | 0.8173 | 0.0451 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.20 | 0.7761 | 0.0742 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.19 | 0.7915 | 0.0604 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.26 | 0.7910 | 0.0656 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.33 | 0.7927 | 0.0621 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.85 | 0.7850 | 0.0613 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.61 | 0.8049 | 0.0495 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.35 | 0.7982 | 0.0557 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.43 | 0.8020 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.06 | 0.7829 | 0.0903 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.38 | 0.7539 | 0.1081 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.48 | 0.7746 | 0.0811 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.53 | 0.7755 | 0.0956 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.54 | 0.7768 | 0.0879 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.89 | 0.7556 | 0.1028 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.07 | 0.7941 | 0.0832 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.43 | 0.7797 | 0.0976 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.70 | 0.7874 | 0.0916 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.69 | 0.7555 | 0.1408 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.56 | 0.7896 | 0.0837 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.39 | 0.8006 | 0.0622 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.56 | 0.8043 | 0.0723 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.56 | 0.8045 | 0.0668 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.75 | 0.7842 | 0.0714 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.65 | 0.8218 | 0.0517 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.90 | 0.8100 | 0.0620 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.36 | 0.8174 | 0.0581 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 21.34 | 0.7157 | 0.0109 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.94 | 0.2123 | 0.1138 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.98 | 0.2393 | 0.1100 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.95 | 0.2308 | 0.1126 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.95 | 0.2354 | 0.1117 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.87 | 0.2219 | 0.1009 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.96 | 0.2685 | 0.0978 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.90 | 0.2484 | 0.0995 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.92 | 0.2587 | 0.0988 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.03 | 0.2026 | 0.0673 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.78 | 0.3028 | 0.0886 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.87 | 0.3347 | 0.0835 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.82 | 0.3185 | 0.0868 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.83 | 0.3246 | 0.0855 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.73 | 0.3398 | 0.0871 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.91 | 0.4021 | 0.0802 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.80 | 0.3724 | 0.0841 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.85 | 0.3852 | 0.0824 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.66 | 0.3366 | 0.0516 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.00 | 0.1785 | 0.1240 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.05 | 0.1929 | 0.1221 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.02 | 0.1894 | 0.1234 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.03 | 0.1907 | 0.1228 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.95 | 0.1545 | 0.1122 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.83 | 0.1895 | 0.1098 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.82 | 0.1703 | 0.1122 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.75 | 0.1798 | 0.1117 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.26 | 0.6915 | 0.0127 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.69 | 0.7084 | 0.0121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.52 | 0.7036 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.56 | 0.7058 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.00 | 0.7090 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.65 | 0.7355 | 0.0108 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.37 | 0.7222 | 0.0114 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.54 | 0.7292 | 0.0112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 21.01 | 0.7089 | 0.0127 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.58 | 0.6499 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.83 | 0.6694 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.70 | 0.6591 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.70 | 0.6623 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.78 | 0.6788 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.63 | 0.7151 | 0.0128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.22 | 0.6982 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.34 | 0.7054 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.71 | 0.6872 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.71 | 0.7075 | 0.0113 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.02 | 0.7152 | 0.0111 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.91 | 0.7132 | 0.0113 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.97 | 0.7138 | 0.0111 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.35 | 0.7110 | 0.0112 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.67 | 0.7336 | 0.0104 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.54 | 0.7223 | 0.0106 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.64 | 0.7285 | 0.0104 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.23 | 0.6898 | 0.0128 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.66 | 0.7068 | 0.0122 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.49 | 0.7019 | 0.0123 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.55 | 0.7045 | 0.0123 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.99 | 0.7077 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.64 | 0.7343 | 0.0109 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.36 | 0.7208 | 0.0115 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.52 | 0.7276 | 0.0112 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 21.01 | 0.7070 | 0.0127 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.57 | 0.6456 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.82 | 0.6660 | 0.0146 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.68 | 0.6553 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.69 | 0.6588 | 0.0152 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.75 | 0.6755 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.59 | 0.7129 | 0.0130 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.20 | 0.6958 | 0.0137 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.30 | 0.7031 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.70 | 0.6831 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.68 | 0.7052 | 0.0116 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.02 | 0.7138 | 0.0112 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.90 | 0.7119 | 0.0114 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.96 | 0.7125 | 0.0112 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.33 | 0.7090 | 0.0114 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.65 | 0.7319 | 0.0106 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.53 | 0.7205 | 0.0107 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.62 | 0.7269 | 0.0107 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 27.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.20 | 0.7924 | 0.0178 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.25 | 0.4147 | 0.2280 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.40 | 0.4297 | 0.2188 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.28 | 0.4285 | 0.2244 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.31 | 0.4288 | 0.2221 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.24 | 0.3734 | 0.2032 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.32 | 0.4043 | 0.1960 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.26 | 0.3997 | 0.1995 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.27 | 0.4033 | 0.1982 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.30 | 0.2580 | 0.1702 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.19 | 0.4772 | 0.1935 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.45 | 0.4935 | 0.1793 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.27 | 0.4926 | 0.1881 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.33 | 0.4922 | 0.1843 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.22 | 0.4932 | 0.1884 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.59 | 0.5356 | 0.1716 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.34 | 0.5218 | 0.1816 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.44 | 0.5281 | 0.1773 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.50 | 0.3874 | 0.1446 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.66 | 0.4023 | 0.2315 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.80 | 0.4140 | 0.2236 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.70 | 0.4138 | 0.2288 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.74 | 0.4147 | 0.2265 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.92 | 0.3487 | 0.2049 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.90 | 0.3741 | 0.1993 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.81 | 0.3638 | 0.2036 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.83 | 0.3677 | 0.2020 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.05 | 0.7829 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.48 | 0.7881 | 0.0199 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.33 | 0.7868 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.37 | 0.7873 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.70 | 0.7871 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.21 | 0.7947 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.01 | 0.7916 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.14 | 0.7932 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.53 | 0.7839 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.36 | 0.7696 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.58 | 0.7753 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.49 | 0.7729 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.47 | 0.7737 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.43 | 0.7746 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.18 | 0.7860 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.89 | 0.7816 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.01 | 0.7836 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.04 | 0.7723 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.51 | 0.7885 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.79 | 0.7912 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.70 | 0.7906 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.74 | 0.7909 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.08 | 0.7903 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.28 | 0.7961 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.22 | 0.7941 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.27 | 0.7954 | 0.0174 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.73 | 0.7679 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.22 | 0.7740 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.16 | 0.7741 | 0.0238 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.20 | 0.7741 | 0.0234 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.12 | 0.7695 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.79 | 0.7840 | 0.0207 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.66 | 0.7809 | 0.0210 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.75 | 0.7825 | 0.0208 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.02 | 0.7517 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.92 | 0.7234 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.06 | 0.7303 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.09 | 0.7308 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.01 | 0.7301 | 0.0314 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.93 | 0.7314 | 0.0315 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.96 | 0.7552 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.64 | 0.7486 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.77 | 0.7522 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.74 | 0.7088 | 0.0429 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.35 | 0.7735 | 0.0257 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.54 | 0.7756 | 0.0267 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.61 | 0.7778 | 0.0254 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.62 | 0.7780 | 0.0250 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.94 | 0.7748 | 0.0241 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.99 | 0.7838 | 0.0255 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.10 | 0.7835 | 0.0245 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.07 | 0.7843 | 0.0251 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 41.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.33 | 0.7409 | 0.0266 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.34 | 0.3278 | 0.3703 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.40 | 0.3368 | 0.3634 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.36 | 0.3363 | 0.3683 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.37 | 0.3365 | 0.3664 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.77 | 0.2970 | 0.3182 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.67 | 0.3172 | 0.3126 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.74 | 0.3117 | 0.3159 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.71 | 0.3150 | 0.3145 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.35 | 0.2183 | 0.2306 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.47 | 0.3898 | 0.3316 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.52 | 0.4028 | 0.3207 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.49 | 0.4003 | 0.3278 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.50 | 0.4010 | 0.3250 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.48 | 0.4049 | 0.3275 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.56 | 0.4306 | 0.3137 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.51 | 0.4227 | 0.3228 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.53 | 0.4265 | 0.3187 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.24 | 0.3406 | 0.1999 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.11 | 0.3181 | 0.3749 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.19 | 0.3254 | 0.3690 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.13 | 0.3247 | 0.3731 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.16 | 0.3252 | 0.3713 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.65 | 0.2818 | 0.3213 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.18 | 0.2977 | 0.3202 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.40 | 0.2899 | 0.3207 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.15 | 0.2932 | 0.3207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.60 | 0.7361 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.95 | 0.7389 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.85 | 0.7385 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.89 | 0.7387 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.99 | 0.7379 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.40 | 0.7420 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.23 | 0.7403 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.33 | 0.7411 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.04 | 0.7391 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.92 | 0.7276 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.10 | 0.7310 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.01 | 0.7294 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.02 | 0.7300 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.97 | 0.7301 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.54 | 0.7364 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.33 | 0.7341 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.42 | 0.7353 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.64 | 0.7333 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.01 | 0.7392 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.18 | 0.7405 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.13 | 0.7403 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.16 | 0.7404 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.33 | 0.7395 | 0.0270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.50 | 0.7429 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.45 | 0.7413 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.50 | 0.7422 | 0.0263 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.16 | 0.7299 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.59 | 0.7336 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.49 | 0.7334 | 0.0311 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.54 | 0.7336 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.60 | 0.7326 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.13 | 0.7395 | 0.0275 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.95 | 0.7376 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.04 | 0.7386 | 0.0282 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.73 | 0.7344 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.45 | 0.7032 | 0.0403 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.68 | 0.7091 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.61 | 0.7076 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.60 | 0.7082 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.38 | 0.7088 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.37 | 0.7220 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.09 | 0.7186 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.24 | 0.7206 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.79 | 0.7192 | 0.0354 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.58 | 0.7334 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.84 | 0.7357 | 0.0307 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.74 | 0.7354 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.78 | 0.7357 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.02 | 0.7337 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.31 | 0.7405 | 0.0292 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.24 | 0.7381 | 0.0302 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.30 | 0.7393 | 0.0297 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 80.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.71 | 0.7121 | 0.0344 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.39 | 0.2744 | 0.3949 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.44 | 0.2771 | 0.3904 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.40 | 0.2768 | 0.3934 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.41 | 0.2767 | 0.3920 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.63 | 0.2165 | 0.3602 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.61 | 0.2211 | 0.3564 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.62 | 0.2209 | 0.3587 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.62 | 0.2211 | 0.3578 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.17 | 0.1116 | 0.2952 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.93 | 0.3182 | 0.3590 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 2.96 | 0.3232 | 0.3510 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 2.94 | 0.3237 | 0.3558 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 2.95 | 0.3237 | 0.3535 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 2.93 | 0.3206 | 0.3558 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 2.96 | 0.3281 | 0.3460 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.94 | 0.3280 | 0.3524 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 2.95 | 0.3283 | 0.3495 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.99 | 0.1906 | 0.2602 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.21 | 0.2638 | 0.3987 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.30 | 0.2668 | 0.3958 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.24 | 0.2660 | 0.3979 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.26 | 0.2663 | 0.3971 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.50 | 0.2027 | 0.3597 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.08 | 0.2113 | 0.3597 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.43 | 0.2055 | 0.3597 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.16 | 0.2086 | 0.3599 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.71 | 0.7120 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.71 | 0.7120 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.71 | 0.7121 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.67 | 0.7117 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.69 | 0.7119 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.67 | 0.7118 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.68 | 0.7118 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.67 | 0.7118 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.69 | 0.7119 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.68 | 0.7119 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.68 | 0.7119 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.71 | 0.7122 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.70 | 0.7119 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.71 | 0.7120 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.71 | 0.7121 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.60 | 0.7114 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.63 | 0.7116 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.63 | 0.7117 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.63 | 0.7117 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.63 | 0.7115 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.67 | 0.7121 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.67 | 0.7121 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.67 | 0.7121 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.70 | 0.7124 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.00 | 0.7071 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.22 | 0.7089 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.15 | 0.7086 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.19 | 0.7088 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.16 | 0.7086 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.37 | 0.7103 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.34 | 0.7103 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.36 | 0.7104 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.57 | 0.7117 | 0.0363 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.63 | 0.7117 | 0.0354 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.67 | 0.7120 | 0.0351 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.66 | 0.7121 | 0.0352 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.67 | 0.7121 | 0.0352 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.64 | 0.7116 | 0.0353 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.69 | 0.7122 | 0.0350 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.67 | 0.7120 | 0.0353 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.68 | 0.7121 | 0.0352 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.61 | 0.7251 | 0.0491 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.78 | 0.2884 | 0.4633 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.84 | 0.2936 | 0.4540 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.79 | 0.2929 | 0.4604 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.81 | 0.2929 | 0.4579 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.89 | 0.2375 | 0.4307 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.87 | 0.2476 | 0.4231 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.88 | 0.2456 | 0.4277 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.87 | 0.2467 | 0.4256 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.20 | 0.1456 | 0.3830 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.48 | 0.3400 | 0.4213 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.52 | 0.3472 | 0.4062 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.49 | 0.3467 | 0.4156 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.50 | 0.3468 | 0.4115 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.48 | 0.3460 | 0.4145 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.52 | 0.3607 | 0.3969 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.49 | 0.3573 | 0.4082 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.50 | 0.3590 | 0.4032 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.29 | 0.2398 | 0.3352 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.55 | 0.2754 | 0.4671 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.63 | 0.2803 | 0.4602 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.57 | 0.2793 | 0.4652 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.60 | 0.2798 | 0.4632 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.71 | 0.2195 | 0.4341 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.33 | 0.2315 | 0.4307 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.62 | 0.2241 | 0.4329 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.39 | 0.2277 | 0.4322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.06 | 0.7222 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.29 | 0.7238 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.20 | 0.7234 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.23 | 0.7236 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.38 | 0.7235 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.62 | 0.7257 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.53 | 0.7247 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.58 | 0.7252 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.37 | 0.7241 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.71 | 0.7184 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.86 | 0.7201 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.79 | 0.7194 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.80 | 0.7196 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.76 | 0.7196 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.14 | 0.7228 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.97 | 0.7215 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.02 | 0.7220 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.16 | 0.7215 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.27 | 0.7236 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.41 | 0.7245 | 0.0493 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.36 | 0.7242 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.38 | 0.7243 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.51 | 0.7238 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.64 | 0.7257 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.59 | 0.7249 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.63 | 0.7253 | 0.0487 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.75 | 0.7190 | 0.0553 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.07 | 0.7210 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.96 | 0.7208 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.00 | 0.7209 | 0.0540 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.11 | 0.7207 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.43 | 0.7243 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.33 | 0.7233 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.39 | 0.7238 | 0.0512 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.05 | 0.7219 | 0.0544 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.67 | 0.7057 | 0.0651 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.87 | 0.7088 | 0.0601 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.81 | 0.7081 | 0.0630 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.81 | 0.7084 | 0.0617 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.66 | 0.7085 | 0.0616 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.33 | 0.7151 | 0.0573 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.12 | 0.7134 | 0.0595 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.21 | 0.7144 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.54 | 0.7150 | 0.0588 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.98 | 0.7205 | 0.0552 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.18 | 0.7219 | 0.0536 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.11 | 0.7218 | 0.0549 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.14 | 0.7219 | 0.0543 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.33 | 0.7209 | 0.0537 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.52 | 0.7245 | 0.0519 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.46 | 0.7232 | 0.0529 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.50 | 0.7239 | 0.0525 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 270056 | 0.323 | 59.3 | 28.86 | 0.27 | 0.028 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 270056 | 0.323 | 64.2 | 28.86 | 0.27 | 0.028 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 270056 | 0.323 | 69.4 | 28.86 | 0.27 | 0.028 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 270056 | 0.323 | 64.8 | 28.86 | 0.27 | 0.028 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 605 | None | classic | 0.30 | False | 416521 | 1.006 | 163.7 | 27.45 | 0.25 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 605 | None | classic | 0.30 | False | 416521 | 1.006 | 155.2 | 27.45 | 0.25 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 605 | None | classic | 0.30 | False | 416521 | 1.006 | 163.0 | 27.45 | 0.25 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 605 | None | classic | 0.30 | False | 416521 | 1.006 | 165.5 | 27.45 | 0.25 | 0.017 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 799406 | 0.805 | 448.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 265875 | 0.323 | 73.1 | 28.69 | 0.18 | 0.017 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 265875 | 0.323 | 58.0 | 28.69 | 0.18 | 0.017 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 265875 | 0.323 | 66.1 | 28.69 | 0.18 | 0.017 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 265875 | 0.323 | 54.2 | 28.69 | 0.18 | 0.017 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1164 | None | classic | 2.03 | False | 351623 | 0.668 | 104.1 | 29.36 | 0.20 | 0.035 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1164 | None | classic | 2.03 | False | 351623 | 0.668 | 109.5 | 29.36 | 0.20 | 0.035 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1164 | None | classic | 2.03 | False | 351623 | 0.668 | 112.0 | 29.36 | 0.20 | 0.035 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1164 | None | classic | 2.03 | False | 351623 | 0.668 | 134.7 | 29.36 | 0.20 | 0.035 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1331306 | 0.805 | 102.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 247951 | 0.925 | 87.5 | 29.31 | 0.10 | 0.026 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 247951 | 0.925 | 72.6 | 29.31 | 0.10 | 0.026 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 247951 | 0.925 | 81.9 | 29.31 | 0.10 | 0.026 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 247951 | 0.925 | 61.8 | 29.31 | 0.10 | 0.026 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 591 | None | classic | 0.32 | False | 431132 | 0.977 | 169.5 | 26.83 | 0.28 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 591 | None | classic | 0.32 | False | 431132 | 0.977 | 150.1 | 26.83 | 0.28 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 591 | None | classic | 0.32 | False | 431132 | 0.977 | 154.3 | 26.83 | 0.28 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 591 | None | classic | 0.32 | False | 431132 | 0.977 | 164.5 | 26.83 | 0.28 | 0.005 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.671 | 0.013 |
| in035 | mask_ent | 0.745 | 0.013 |
| in035 | mask_grad | 0.467 | 0.013 |
| in035 | r_col | 0.757 | 0.013 |
| in035 | r_warp | 0.861 | 0.013 |

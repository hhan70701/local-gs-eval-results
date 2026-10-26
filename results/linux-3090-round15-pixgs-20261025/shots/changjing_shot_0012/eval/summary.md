# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 20.3% | 25.32 / 0.0380 | 24.73 / 0.0786 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 20.5% | 25.28 / 0.0386 | 26.10 / 0.0588 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 20.5% | 25.31 / 0.0386 | 25.91 / 0.0668 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 20.5% | 25.30 / 0.0390 | 26.02 / 0.0624 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 20.3% | 25.35 / 0.0375 | 23.99 / 0.0763 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 20.8% | 25.30 / 0.0387 | 25.06 / 0.0591 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 20.5% | 25.32 / 0.0382 | 24.64 / 0.0651 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 20.6% | 25.31 / 0.0383 | 24.82 / 0.0613 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 20.2% | 24.86 / 0.0379 | 23.44 / 0.0770 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 21.8% | 25.95 / 0.0294 | 24.56 / 0.0716 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 22.2% | 25.86 / 0.0305 | 25.93 / 0.0516 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 22.0% | 25.92 / 0.0299 | 25.80 / 0.0605 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 22.1% | 25.91 / 0.0299 | 25.91 / 0.0552 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 21.8% | 25.94 / 0.0298 | 24.52 / 0.0709 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 22.2% | 25.84 / 0.0303 | 25.90 / 0.0514 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 22.0% | 25.90 / 0.0301 | 25.81 / 0.0593 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 22.1% | 25.89 / 0.0300 | 25.91 / 0.0545 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 22.3% | 25.41 / 0.0313 | 23.41 / 0.0785 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 16.4% | 25.47 / 0.0289 | 21.00 / 0.0768 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 17.5% | 25.51 / 0.0307 | 22.38 / 0.0664 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 16.8% | 25.46 / 0.0296 | 21.96 / 0.0701 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 17.0% | 25.48 / 0.0298 | 22.19 / 0.0673 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 16.3% | 25.44 / 0.0292 | 20.93 / 0.0757 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 17.2% | 25.43 / 0.0314 | 21.44 / 0.0685 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 16.5% | 25.46 / 0.0299 | 21.34 / 0.0695 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 16.7% | 25.42 / 0.0305 | 21.39 / 0.0678 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.97 / 0.0729 | 28.74 / 0.0870 | 18.57 / 0.0236 | 29.89 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.90 / 0.1014 | 29.51 / 0.1131 | 19.36 / 0.0308 | 29.79 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.44 / 0.0899 | 29.58 / 0.1041 | 20.34 / 0.0254 | 29.83 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.36 / 0.0947 | 29.54 / 0.1078 | 20.12 / 0.0279 | 29.84 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.40 / 0.0920 | 29.58 / 0.1046 | 20.20 / 0.0267 | 29.84 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.64 / 0.1009 | 29.28 / 0.1138 | 18.87 / 0.0318 | 29.81 / 0.0364 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.12 / 0.0889 | 29.38 / 0.1030 | 19.65 / 0.0267 | 29.77 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.96 / 0.0939 | 29.23 / 0.1076 | 19.32 / 0.0295 | 29.82 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.02 / 0.0909 | 29.28 / 0.1046 | 19.43 / 0.0283 | 29.80 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.58 / 0.0979 | 30.05 / 0.0973 | 19.76 / 0.0324 | 29.87 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.58 / 0.1091 | 28.81 / 0.1177 | 18.98 / 0.0330 | 29.69 / 0.0381 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.14 / 0.0931 | 28.73 / 0.1065 | 19.74 / 0.0266 | 29.82 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.06 / 0.1010 | 28.78 / 0.1113 | 19.63 / 0.0296 | 29.82 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.12 / 0.0962 | 28.72 / 0.1079 | 19.71 / 0.0281 | 29.82 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.58 / 0.1082 | 28.86 / 0.1161 | 18.95 / 0.0331 | 29.67 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.15 / 0.0932 | 28.69 / 0.1053 | 19.73 / 0.0272 | 29.80 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.08 / 0.1003 | 28.75 / 0.1118 | 19.64 / 0.0294 | 29.81 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.13 / 0.0964 | 28.71 / 0.1079 | 19.72 / 0.0283 | 29.81 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.34 / 0.1048 | 28.90 / 0.1128 | 19.27 / 0.0359 | 29.86 / 0.0365 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 25.86 / 0.1152 | 28.26 / 0.1237 | 18.87 / 0.0340 | 29.86 / 0.0383 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.37 / 0.1028 | 27.97 / 0.1189 | 20.04 / 0.0273 | 29.84 / 0.0379 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.23 / 0.1088 | 28.27 / 0.1214 | 19.73 / 0.0303 | 29.85 / 0.0381 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.33 / 0.1056 | 28.19 / 0.1196 | 19.91 / 0.0289 | 29.84 / 0.0381 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.94 / 0.1134 | 28.33 / 0.1260 | 18.85 / 0.0318 | 29.84 / 0.0384 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.11 / 0.1052 | 27.97 / 0.1235 | 19.13 / 0.0292 | 29.81 / 0.0382 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.06 / 0.1088 | 28.31 / 0.1247 | 19.10 / 0.0302 | 29.83 / 0.0385 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.08 / 0.1068 | 28.20 / 0.1226 | 19.07 / 0.0298 | 29.81 / 0.0384 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.5%） | — | — | 27.97 / 0.0729 | 28.74 / 0.0870 | 29.89 |
| in035 | rife | 9.0% | 16.4% | 25.86 / 0.1152 | 28.26 / 0.1237 | 29.86 |
| in035 | cnw_cnn | 15.6% | 20.3% | 27.90 / 0.1014 | 29.51 / 0.1131 | 29.79 |
| in035 | cnw_f5 | 16.7% | 21.8% | 27.58 / 0.1091 | 28.81 / 0.1177 | 29.69 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.51 / 0.0753 | -5.79 / +0.0589 (core 10.2%) | -0.29 / +0.0311 (core 19.7%) | -0.50 / +0.0406 (core 20.8%) |
| in035 | 2 | 0-3 | 26.83 / 0.0803 | -0.10 / +0.0502 (core 10.2%) | +0.46 / +0.0413 (core 19.7%) | -0.13 / +0.0526 (core 20.8%) |
| in035 | 4 | 3-5 | 29.57 / 0.0633 | -0.44 / +0.0176 (core 4.5%) | -0.39 / +0.0131 (core 5.0%) | -0.54 / +0.0153 (core 6.0%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.97 / 0.0729 | 28.74 | 29.89 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.90 / 0.1014 | 29.51 | 29.79 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 28.27 / 0.0796 | 29.65 | 29.88 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.44 / 0.0899 | 29.58 | 29.83 | 0/3 |
| in035 | cnw_cnn | oracle | 2.6% | 28.72 / 0.0752 | 29.81 | 29.88 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.36 / 0.0947 | 29.54 | 29.84 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 28.62 / 0.0771 | 29.64 | 29.88 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.40 / 0.0920 | 29.58 | 29.84 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 28.66 / 0.0761 | 29.71 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.64 / 0.1009 | 29.28 | 29.81 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 28.08 / 0.0794 | 29.43 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.12 / 0.0889 | 29.38 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.6% | 28.50 / 0.0750 | 29.64 | 29.87 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.96 / 0.0939 | 29.23 | 29.82 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.6% | 28.33 / 0.0776 | 29.36 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.02 / 0.0909 | 29.28 | 29.80 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.6% | 28.39 / 0.0762 | 29.46 | 29.87 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.58 / 0.0979 | 30.05 | 29.87 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.7% | 28.40 / 0.0822 | 30.09 | 29.89 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.58 / 0.1091 | 28.81 | 29.69 | 0/3 |
| in035 | cnw_f5 | oracle | 2.4% | 28.09 / 0.0830 | 28.97 | 29.88 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.14 / 0.0931 | 28.73 | 29.82 | 0/3 |
| in035 | cnw_f5 | oracle | 2.6% | 28.45 / 0.0765 | 28.94 | 29.88 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.06 / 0.1010 | 28.78 | 29.82 | 0/3 |
| in035 | cnw_f5 | oracle | 2.5% | 28.39 / 0.0801 | 28.89 | 29.89 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.12 / 0.0962 | 28.72 | 29.82 | 0/3 |
| in035 | cnw_f5 | oracle | 2.5% | 28.42 / 0.0781 | 28.87 | 29.89 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.58 / 0.1082 | 28.86 | 29.67 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.5% | 28.10 / 0.0829 | 29.02 | 29.88 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.15 / 0.0932 | 28.69 | 29.80 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.6% | 28.48 / 0.0768 | 28.88 | 29.89 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.08 / 0.1003 | 28.75 | 29.81 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.5% | 28.41 / 0.0796 | 28.86 | 29.89 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.13 / 0.0964 | 28.71 | 29.81 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.5% | 28.46 / 0.0782 | 28.86 | 29.89 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.34 / 0.1048 | 28.90 | 29.86 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.8% | 28.19 / 0.0852 | 29.06 | 29.90 | 0/3 |
| in035 | rife | 不复核 | —% | 25.86 / 0.1152 | 28.26 | 29.86 | 0/3 |
| in035 | rife | oracle | 2.2% | 28.07 / 0.0837 | 28.96 | 29.89 | 0/3 |
| in035 | rife | 不复核 | —% | 26.37 / 0.1028 | 27.97 | 29.84 | 0/3 |
| in035 | rife | oracle | 2.4% | 28.63 / 0.0776 | 28.93 | 29.89 | 0/3 |
| in035 | rife | 不复核 | —% | 26.23 / 0.1088 | 28.27 | 29.85 | 0/3 |
| in035 | rife | oracle | 2.3% | 28.47 / 0.0806 | 28.95 | 29.89 | 0/3 |
| in035 | rife | 不复核 | —% | 26.33 / 0.1056 | 28.19 | 29.84 | 0/3 |
| in035 | rife | oracle | 2.3% | 28.57 / 0.0792 | 28.94 | 29.89 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.94 / 0.1134 | 28.33 | 29.84 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 28.10 / 0.0812 | 28.83 | 29.89 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.11 / 0.1052 | 27.97 | 29.81 | 0/3 |
| in035 | rife_mw | oracle | 2.4% | 28.28 / 0.0782 | 28.99 | 29.89 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.06 / 0.1088 | 28.31 | 29.83 | 0/3 |
| in035 | rife_mw | oracle | 2.4% | 28.24 / 0.0798 | 28.99 | 29.89 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.08 / 0.1068 | 28.20 | 29.81 | 0/3 |
| in035 | rife_mw | oracle | 2.4% | 28.24 / 0.0791 | 28.98 | 29.89 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.97 / 0.0729 | 28.74 / 0.0870 | — |
| in035 | FF | 0（前馈） | 950×732（67%） | 28.75 | 27.90 / 0.1014 | 29.51 / 0.1131 | 0/3 |
| in035 | 25 | 1.69 s | 950×732（67%） | 29.45 | 28.36 / 0.0947 | 29.54 / 0.1078 | 0/3 |
| in035 | 50 | 3.39 s | 950×732（67%） | 29.69 | 28.40 / 0.0920 | 29.58 / 0.1046 | 0/3 |
| in035 | 100 | 6.77 s | 950×732（67%） | 29.92 | 28.44 / 0.0899 | 29.58 / 0.1041 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.97 / 0.0729 | 28.74 / 0.0870 | 29.89 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.90 / 0.1014 | 29.51 / 0.1131 | 29.79 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.27 / 0.0796 | 29.65 / 0.0947 | 29.88 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.36 / 0.0947 | 29.54 / 0.1078 | 29.84 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.62 / 0.0771 | 29.64 / 0.0928 | 29.88 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 28.40 / 0.0920 | 29.58 / 0.1046 | 29.84 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.66 / 0.0761 | 29.71 / 0.0914 | 29.88 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 28.44 / 0.0899 | 29.58 / 0.1041 | 29.83 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.72 / 0.0752 | 29.81 / 0.0907 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.64 / 0.1009 | 29.28 / 0.1138 | 29.81 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.08 / 0.0794 | 29.43 / 0.0952 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.96 / 0.0939 | 29.23 / 0.1076 | 29.82 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.33 / 0.0776 | 29.36 / 0.0934 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.02 / 0.0909 | 29.28 / 0.1046 | 29.80 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.39 / 0.0762 | 29.46 / 0.0915 | 29.87 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.12 / 0.0889 | 29.38 / 0.1030 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.50 / 0.0750 | 29.64 / 0.0901 | 29.87 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 27.58 / 0.1091 | 28.81 / 0.1177 | 29.69 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 28.09 / 0.0830 | 28.97 / 0.0962 | 29.88 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 28.06 / 0.1010 | 28.78 / 0.1113 | 29.82 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 28.39 / 0.0801 | 28.89 / 0.0942 | 29.89 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 28.12 / 0.0962 | 28.72 / 0.1079 | 29.82 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.42 / 0.0781 | 28.87 / 0.0926 | 29.89 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 28.14 / 0.0931 | 28.73 / 0.1065 | 29.82 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.45 / 0.0765 | 28.94 / 0.0912 | 29.88 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.58 / 0.1082 | 28.86 / 0.1161 | 29.67 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.10 / 0.0829 | 29.02 / 0.0957 | 29.88 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 28.08 / 0.1003 | 28.75 / 0.1118 | 29.81 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.41 / 0.0796 | 28.86 / 0.0942 | 29.89 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 28.13 / 0.0964 | 28.71 / 0.1079 | 29.81 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.46 / 0.0782 | 28.86 / 0.0930 | 29.89 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.15 / 0.0932 | 28.69 / 0.1053 | 29.80 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.48 / 0.0768 | 28.88 / 0.0916 | 29.89 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 25.86 / 0.1152 | 28.26 / 0.1237 | 29.86 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.07 / 0.0837 | 28.96 / 0.0983 | 29.89 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 26.23 / 0.1088 | 28.27 / 0.1214 | 29.85 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.47 / 0.0806 | 28.95 / 0.0968 | 29.89 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 26.33 / 0.1056 | 28.19 / 0.1196 | 29.84 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.57 / 0.0792 | 28.94 / 0.0958 | 29.89 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.37 / 0.1028 | 27.97 / 0.1189 | 29.84 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.63 / 0.0776 | 28.93 / 0.0951 | 29.89 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 25.94 / 0.1134 | 28.33 / 0.1260 | 29.84 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.10 / 0.0812 | 28.83 / 0.0969 | 29.89 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 26.06 / 0.1088 | 28.31 / 0.1247 | 29.83 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.24 / 0.0798 | 28.99 / 0.0951 | 29.89 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 26.08 / 0.1068 | 28.20 / 0.1226 | 29.81 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.24 / 0.0791 | 28.98 / 0.0942 | 29.89 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 26.11 / 0.1052 | 27.97 / 0.1235 | 29.81 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.28 / 0.0782 | 28.99 / 0.0946 | 29.89 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.74 / 0.0870 | 18.57 / 0.0236 | 29.89 / 0.0350 | 27.97 / 0.0729 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 27.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.74 | 0.8281 | 0.0870 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.15 | 0.6639 | 0.5475 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.24 | 0.6641 | 0.5283 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.18 | 0.6660 | 0.5375 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.20 | 0.6651 | 0.5316 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.14 | 0.6657 | 0.5477 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.22 | 0.6647 | 0.5283 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.16 | 0.6664 | 0.5378 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.18 | 0.6659 | 0.5323 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.83 | 0.4007 | 0.5095 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.93 | 0.6958 | 0.5036 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.11 | 0.6966 | 0.4753 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.98 | 0.6995 | 0.4907 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.03 | 0.6987 | 0.4813 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.95 | 0.6976 | 0.5021 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.13 | 0.6963 | 0.4751 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.00 | 0.6999 | 0.4908 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.05 | 0.6985 | 0.4823 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.85 | 0.4917 | 0.4837 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.92 | 0.6345 | 0.5975 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.05 | 0.6381 | 0.5778 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.95 | 0.6376 | 0.5909 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.99 | 0.6380 | 0.5841 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.88 | 0.6327 | 0.5980 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.02 | 0.6323 | 0.5771 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.92 | 0.6352 | 0.5892 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.95 | 0.6345 | 0.5818 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.65 | 0.8341 | 0.0947 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.81 | 0.8356 | 0.0907 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.64 | 0.8346 | 0.0928 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.71 | 0.8350 | 0.0914 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.43 | 0.8333 | 0.0952 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.64 | 0.8351 | 0.0901 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.36 | 0.8328 | 0.0934 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.46 | 0.8337 | 0.0915 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.09 | 0.8373 | 0.0885 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.97 | 0.8307 | 0.0962 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.94 | 0.8315 | 0.0912 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.89 | 0.8309 | 0.0942 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.87 | 0.8311 | 0.0926 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.02 | 0.8308 | 0.0957 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.88 | 0.8309 | 0.0916 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.86 | 0.8305 | 0.0942 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.86 | 0.8305 | 0.0930 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.06 | 0.8308 | 0.0957 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.96 | 0.8313 | 0.0983 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.93 | 0.8313 | 0.0951 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.95 | 0.8313 | 0.0968 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.94 | 0.8315 | 0.0958 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.83 | 0.8310 | 0.0969 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.99 | 0.8317 | 0.0946 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.99 | 0.8320 | 0.0951 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.98 | 0.8318 | 0.0942 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.51 | 0.8383 | 0.1131 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.58 | 0.8379 | 0.1041 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.54 | 0.8395 | 0.1078 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.58 | 0.8390 | 0.1046 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.28 | 0.8379 | 0.1138 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.38 | 0.8377 | 0.1030 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.23 | 0.8380 | 0.1076 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.28 | 0.8379 | 0.1046 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 30.05 | 0.8413 | 0.0973 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.81 | 0.8344 | 0.1177 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.73 | 0.8341 | 0.1065 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.78 | 0.8354 | 0.1113 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.72 | 0.8349 | 0.1079 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.86 | 0.8347 | 0.1161 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.69 | 0.8339 | 0.1053 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.75 | 0.8351 | 0.1118 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.71 | 0.8346 | 0.1079 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.90 | 0.8330 | 0.1128 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.26 | 0.8260 | 0.1237 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.97 | 0.8268 | 0.1189 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.27 | 0.8274 | 0.1214 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.19 | 0.8276 | 0.1196 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.33 | 0.8251 | 0.1260 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.97 | 0.8239 | 0.1235 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.31 | 0.8264 | 0.1247 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.20 | 0.8257 | 0.1226 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.57 | 0.5923 | 0.0236 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.26 | 0.4496 | 0.1005 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.45 | 0.4911 | 0.0933 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.37 | 0.4768 | 0.0971 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.40 | 0.4818 | 0.0954 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.19 | 0.4246 | 0.1013 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.36 | 0.4605 | 0.0941 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.29 | 0.4391 | 0.0980 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.32 | 0.4473 | 0.0964 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.46 | 0.4062 | 0.0861 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.46 | 0.5020 | 0.0827 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.81 | 0.5677 | 0.0721 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.65 | 0.5455 | 0.0774 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.73 | 0.5586 | 0.0748 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.49 | 0.5052 | 0.0823 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.80 | 0.5607 | 0.0731 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.66 | 0.5450 | 0.0772 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.72 | 0.5544 | 0.0751 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.06 | 0.4978 | 0.0693 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.49 | 0.4631 | 0.1076 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.95 | 0.5329 | 0.0966 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.72 | 0.5140 | 0.1022 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.82 | 0.5258 | 0.0999 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 8.49 | 0.4565 | 0.1059 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.66 | 0.4524 | 0.1001 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 8.55 | 0.4513 | 0.1034 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.60 | 0.4492 | 0.1021 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.37 | 0.6376 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.34 | 0.6748 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.12 | 0.6651 | 0.0278 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.19 | 0.6697 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.88 | 0.6132 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.65 | 0.6467 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.32 | 0.6291 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.43 | 0.6359 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.76 | 0.6496 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.98 | 0.6108 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.74 | 0.6542 | 0.0265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.63 | 0.6449 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.71 | 0.6514 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.96 | 0.6106 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.73 | 0.6523 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.64 | 0.6434 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.71 | 0.6493 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.27 | 0.6248 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.89 | 0.6084 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.05 | 0.6604 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.74 | 0.6477 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.92 | 0.6568 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 18.85 | 0.6044 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.15 | 0.6176 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.11 | 0.6140 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.09 | 0.6139 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.36 | 0.6366 | 0.0308 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.34 | 0.6743 | 0.0254 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.12 | 0.6649 | 0.0279 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.20 | 0.6695 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.87 | 0.6128 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.65 | 0.6464 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.32 | 0.6292 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.43 | 0.6358 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.76 | 0.6484 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.98 | 0.6092 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.74 | 0.6535 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.63 | 0.6439 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.71 | 0.6508 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.95 | 0.6084 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.73 | 0.6514 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.64 | 0.6421 | 0.0294 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.72 | 0.6483 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.27 | 0.6238 | 0.0359 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.87 | 0.6061 | 0.0340 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.04 | 0.6597 | 0.0273 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.73 | 0.6466 | 0.0303 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.91 | 0.6558 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 18.85 | 0.6031 | 0.0318 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.13 | 0.6158 | 0.0292 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.10 | 0.6126 | 0.0302 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.07 | 0.6123 | 0.0298 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 47.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.65 | 0.7947 | 0.0404 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.12 | 0.6400 | 0.2726 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.22 | 0.6501 | 0.2538 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.16 | 0.6513 | 0.2623 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.18 | 0.6511 | 0.2574 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.10 | 0.6369 | 0.2705 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.21 | 0.6436 | 0.2529 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.14 | 0.6456 | 0.2612 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.17 | 0.6449 | 0.2564 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.87 | 0.4807 | 0.2405 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.95 | 0.6736 | 0.2372 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.20 | 0.6877 | 0.2126 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 10.03 | 0.6880 | 0.2250 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.10 | 0.6889 | 0.2182 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.97 | 0.6735 | 0.2377 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.21 | 0.6860 | 0.2126 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 10.05 | 0.6877 | 0.2256 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.11 | 0.6880 | 0.2185 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.11 | 0.5543 | 0.2226 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.75 | 0.6133 | 0.2901 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.00 | 0.6296 | 0.2704 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.82 | 0.6287 | 0.2819 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.89 | 0.6299 | 0.2769 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.72 | 0.6084 | 0.2883 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.90 | 0.6115 | 0.2719 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.76 | 0.6160 | 0.2817 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.81 | 0.6148 | 0.2766 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.10 | 0.7961 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.85 | 0.8033 | 0.0437 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.70 | 0.8021 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.75 | 0.8026 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.59 | 0.7916 | 0.0477 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.27 | 0.7985 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.98 | 0.7959 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.08 | 0.7969 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.10 | 0.7966 | 0.0519 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.79 | 0.7935 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.41 | 0.8016 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.33 | 0.8004 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.37 | 0.8013 | 0.0463 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.77 | 0.7934 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.41 | 0.8013 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.34 | 0.8002 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.41 | 0.8011 | 0.0462 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.74 | 0.7924 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.66 | 0.7930 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.66 | 0.8026 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.36 | 0.8004 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.53 | 0.8019 | 0.0477 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.65 | 0.7928 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.91 | 0.7951 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.87 | 0.7954 | 0.0482 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.86 | 0.7951 | 0.0473 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.18 | 0.7955 | 0.0699 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.08 | 0.8027 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.93 | 0.8043 | 0.0627 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.02 | 0.8038 | 0.0599 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.63 | 0.7902 | 0.0690 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.44 | 0.7964 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.10 | 0.7970 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.24 | 0.7969 | 0.0595 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.57 | 0.7851 | 0.0718 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.81 | 0.7891 | 0.0761 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.63 | 0.7997 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.51 | 0.8003 | 0.0685 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.57 | 0.8007 | 0.0643 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.76 | 0.7891 | 0.0758 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.63 | 0.7990 | 0.0616 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.53 | 0.8001 | 0.0684 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.60 | 0.8002 | 0.0642 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.89 | 0.7700 | 0.0879 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.57 | 0.7752 | 0.0827 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.38 | 0.7852 | 0.0740 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.16 | 0.7864 | 0.0779 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.30 | 0.7869 | 0.0750 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.64 | 0.7743 | 0.0821 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.87 | 0.7748 | 0.0767 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.84 | 0.7800 | 0.0778 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.86 | 0.7785 | 0.0756 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 50.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.71 | 0.7521 | 0.0497 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.95 | 0.5376 | 0.4050 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.02 | 0.5456 | 0.3893 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.98 | 0.5474 | 0.3971 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.00 | 0.5468 | 0.3929 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.94 | 0.5375 | 0.4036 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.02 | 0.5425 | 0.3894 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.97 | 0.5453 | 0.3969 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.99 | 0.5443 | 0.3930 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.98 | 0.3953 | 0.3004 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.23 | 0.5771 | 0.3662 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.36 | 0.5907 | 0.3452 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.28 | 0.5914 | 0.3563 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.31 | 0.5923 | 0.3502 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.23 | 0.5786 | 0.3668 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.35 | 0.5905 | 0.3449 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.27 | 0.5922 | 0.3562 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.30 | 0.5923 | 0.3500 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.82 | 0.4669 | 0.2696 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.98 | 0.5362 | 0.4118 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.10 | 0.5510 | 0.3925 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.01 | 0.5504 | 0.4030 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.04 | 0.5513 | 0.3980 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.96 | 0.5344 | 0.4087 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.05 | 0.5373 | 0.3950 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.98 | 0.5409 | 0.4035 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.00 | 0.5393 | 0.3994 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.14 | 0.7532 | 0.0557 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.77 | 0.7593 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.63 | 0.7582 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.68 | 0.7586 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.80 | 0.7509 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.41 | 0.7572 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.14 | 0.7546 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.23 | 0.7556 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.26 | 0.7568 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.86 | 0.7506 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.38 | 0.7576 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.30 | 0.7563 | 0.0560 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.35 | 0.7572 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.87 | 0.7509 | 0.0589 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.39 | 0.7577 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.32 | 0.7564 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.38 | 0.7574 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.94 | 0.7534 | 0.0619 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.83 | 0.7516 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.63 | 0.7595 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.40 | 0.7576 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.54 | 0.7589 | 0.0552 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.83 | 0.7518 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.08 | 0.7544 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.03 | 0.7543 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.02 | 0.7542 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.57 | 0.7544 | 0.0723 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.33 | 0.7601 | 0.0623 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.21 | 0.7617 | 0.0670 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.27 | 0.7612 | 0.0645 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.15 | 0.7519 | 0.0719 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.84 | 0.7570 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.58 | 0.7577 | 0.0663 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.67 | 0.7575 | 0.0634 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.10 | 0.7498 | 0.0734 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.15 | 0.7488 | 0.0785 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.92 | 0.7582 | 0.0648 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.81 | 0.7587 | 0.0719 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.89 | 0.7592 | 0.0676 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.14 | 0.7496 | 0.0781 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.92 | 0.7582 | 0.0649 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.82 | 0.7588 | 0.0714 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.89 | 0.7591 | 0.0677 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.79 | 0.7444 | 0.0792 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.08 | 0.7482 | 0.0796 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.99 | 0.7585 | 0.0678 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.85 | 0.7584 | 0.0735 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.97 | 0.7592 | 0.0705 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.05 | 0.7469 | 0.0776 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.22 | 0.7491 | 0.0702 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.32 | 0.7521 | 0.0739 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.27 | 0.7510 | 0.0719 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 57.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.89 | 0.7134 | 0.0350 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.92 | 0.3238 | 0.3904 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.96 | 0.3273 | 0.3819 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.93 | 0.3280 | 0.3868 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.94 | 0.3278 | 0.3842 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.90 | 0.3222 | 0.3891 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.94 | 0.3224 | 0.3828 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.91 | 0.3249 | 0.3865 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.92 | 0.3237 | 0.3846 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.92 | 0.1520 | 0.3059 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.58 | 0.3697 | 0.3604 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.63 | 0.3747 | 0.3484 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.59 | 0.3759 | 0.3555 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.61 | 0.3757 | 0.3521 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.57 | 0.3694 | 0.3603 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.62 | 0.3750 | 0.3479 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.58 | 0.3763 | 0.3551 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.60 | 0.3761 | 0.3514 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.71 | 0.2258 | 0.2837 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.22 | 0.3543 | 0.3745 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.27 | 0.3595 | 0.3646 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.23 | 0.3598 | 0.3706 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.25 | 0.3597 | 0.3677 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.20 | 0.3509 | 0.3743 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.23 | 0.3517 | 0.3663 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.20 | 0.3538 | 0.3714 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.21 | 0.3528 | 0.3688 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.88 | 0.7133 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.88 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.88 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.88 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.88 | 0.7134 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.87 | 0.7134 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.88 | 0.7134 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.87 | 0.7134 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.89 | 0.7134 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.88 | 0.7133 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.88 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.89 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.89 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.88 | 0.7133 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.89 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.89 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.89 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.90 | 0.7135 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.89 | 0.7134 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.89 | 0.7134 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.89 | 0.7134 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.89 | 0.7134 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.89 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.89 | 0.7134 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.89 | 0.7134 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.89 | 0.7134 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.79 | 0.7136 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.83 | 0.7138 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.84 | 0.7140 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.84 | 0.7139 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.81 | 0.7136 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7137 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.82 | 0.7139 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.80 | 0.7138 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.87 | 0.7137 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.69 | 0.7132 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.82 | 0.7141 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.82 | 0.7143 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.82 | 0.7142 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.67 | 0.7131 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.80 | 0.7141 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.81 | 0.7143 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.81 | 0.7142 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.86 | 0.7140 | 0.0365 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.86 | 0.7138 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.84 | 0.7140 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.85 | 0.7141 | 0.0381 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.84 | 0.7141 | 0.0381 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.84 | 0.7136 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.81 | 0.7136 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.83 | 0.7138 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.81 | 0.7138 | 0.0384 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.97 | 0.7525 | 0.0729 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.67 | 0.4783 | 0.5090 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.72 | 0.4833 | 0.4853 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.69 | 0.4849 | 0.4964 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.70 | 0.4843 | 0.4905 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.65 | 0.4774 | 0.5068 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.70 | 0.4798 | 0.4851 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.67 | 0.4824 | 0.4953 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.68 | 0.4813 | 0.4899 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.40 | 0.3230 | 0.4362 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.56 | 0.5158 | 0.4736 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.64 | 0.5239 | 0.4413 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.59 | 0.5253 | 0.4576 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.61 | 0.5254 | 0.4490 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.56 | 0.5164 | 0.4740 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.63 | 0.5238 | 0.4414 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.58 | 0.5258 | 0.4576 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.60 | 0.5255 | 0.4490 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.69 | 0.3919 | 0.4031 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.77 | 0.4743 | 0.5216 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.84 | 0.4833 | 0.4941 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.79 | 0.4835 | 0.5092 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.81 | 0.4839 | 0.5018 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.75 | 0.4720 | 0.5171 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.80 | 0.4719 | 0.4969 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.76 | 0.4754 | 0.5084 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.77 | 0.4739 | 0.5025 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.27 | 0.7530 | 0.0796 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.72 | 0.7563 | 0.0752 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.62 | 0.7557 | 0.0771 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.66 | 0.7559 | 0.0761 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.08 | 0.7520 | 0.0794 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.50 | 0.7553 | 0.0750 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.33 | 0.7539 | 0.0776 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.39 | 0.7545 | 0.0762 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.40 | 0.7552 | 0.0822 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.09 | 0.7515 | 0.0830 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.45 | 0.7553 | 0.0765 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.39 | 0.7546 | 0.0801 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.42 | 0.7551 | 0.0781 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.10 | 0.7517 | 0.0829 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.48 | 0.7554 | 0.0768 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.41 | 0.7547 | 0.0796 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.46 | 0.7552 | 0.0782 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.19 | 0.7534 | 0.0852 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.07 | 0.7522 | 0.0837 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.63 | 0.7564 | 0.0776 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.47 | 0.7554 | 0.0806 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.57 | 0.7561 | 0.0792 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.10 | 0.7524 | 0.0812 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.28 | 0.7538 | 0.0782 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.24 | 0.7537 | 0.0798 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.24 | 0.7537 | 0.0791 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.90 | 0.7551 | 0.1014 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.44 | 0.7579 | 0.0899 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.36 | 0.7591 | 0.0947 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.40 | 0.7587 | 0.0920 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.64 | 0.7539 | 0.1009 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.12 | 0.7564 | 0.0889 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.96 | 0.7571 | 0.0939 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.02 | 0.7569 | 0.0909 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.58 | 0.7527 | 0.0979 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.58 | 0.7519 | 0.1091 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.14 | 0.7569 | 0.0931 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.06 | 0.7574 | 0.1010 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.12 | 0.7576 | 0.0962 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.58 | 0.7524 | 0.1082 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.15 | 0.7570 | 0.0932 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.08 | 0.7575 | 0.1003 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.13 | 0.7576 | 0.0964 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.34 | 0.7498 | 0.1048 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.86 | 0.7445 | 0.1152 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.37 | 0.7499 | 0.1028 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.23 | 0.7498 | 0.1088 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.33 | 0.7503 | 0.1056 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.94 | 0.7442 | 0.1134 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.11 | 0.7451 | 0.1052 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.06 | 0.7468 | 0.1088 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.08 | 0.7462 | 0.1068 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1192 | None | classic | 2.12 | False | 384281 | 0.332 | 72.5 | 30.96 | 0.08 | 0.005 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1192 | None | classic | 2.12 | False | 384281 | 0.332 | 74.3 | 30.96 | 0.08 | 0.005 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1192 | None | classic | 2.12 | False | 384281 | 0.332 | 67.1 | 30.96 | 0.08 | 0.005 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1192 | None | classic | 2.12 | False | 384281 | 0.332 | 75.5 | 30.96 | 0.08 | 0.005 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1056 | None | classic | 1.67 | False | 435491 | 0.645 | 136.4 | 30.28 | 0.11 | 0.005 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1056 | None | classic | 1.67 | False | 435491 | 0.645 | 118.2 | 30.28 | 0.11 | 0.005 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1056 | None | classic | 1.67 | False | 435491 | 0.645 | 122.1 | 30.28 | 0.11 | 0.005 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1056 | None | classic | 1.67 | False | 435491 | 0.645 | 122.7 | 30.28 | 0.11 | 0.005 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1535405 | 0.791 | 472.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 414501 | 0.329 | 67.6 | 31.68 | 0.10 | 0.004 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 414501 | 0.329 | 76.1 | 31.68 | 0.10 | 0.004 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 414501 | 0.329 | 44.8 | 31.68 | 0.10 | 0.004 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 414501 | 0.329 | 58.4 | 31.68 | 0.10 | 0.004 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1285 | None | classic | 2.47 | False | 408520 | 0.339 | 69.4 | 31.60 | 0.10 | 0.013 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1285 | None | classic | 2.47 | False | 408520 | 0.339 | 70.9 | 31.60 | 0.10 | 0.013 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1285 | None | classic | 2.47 | False | 408520 | 0.339 | 56.5 | 31.60 | 0.10 | 0.013 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1285 | None | classic | 2.47 | False | 408520 | 0.339 | 80.0 | 31.60 | 0.10 | 0.013 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2105787 | 0.791 | 122.0 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 411100 | 0.876 | 82.2 | 31.89 | 0.10 | 0.005 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 411100 | 0.876 | 76.8 | 31.89 | 0.10 | 0.005 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 411100 | 0.876 | 77.8 | 31.89 | 0.10 | 0.005 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 411100 | 0.876 | 54.6 | 31.89 | 0.10 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1148 | None | classic | 1.97 | False | 472986 | 0.653 | 112.4 | 31.03 | 0.06 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1148 | None | classic | 1.97 | False | 472986 | 0.653 | 108.9 | 31.03 | 0.06 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1148 | None | classic | 1.97 | False | 472986 | 0.653 | 97.1 | 31.03 | 0.06 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1148 | None | classic | 1.97 | False | 472986 | 0.653 | 94.3 | 31.03 | 0.06 | 0.009 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.795 | 0.022 |
| in035 | mask_ent | 0.752 | 0.022 |
| in035 | mask_grad | 0.533 | 0.022 |
| in035 | r_col | 0.769 | 0.022 |
| in035 | r_warp | 0.824 | 0.022 |

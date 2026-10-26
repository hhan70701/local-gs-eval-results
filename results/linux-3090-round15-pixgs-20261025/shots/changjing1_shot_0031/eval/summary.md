# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 7.7% | 26.01 / 0.0072 | 20.73 / 0.0228 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.2% | 26.00 / 0.0076 | 21.67 / 0.0190 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.0% | 26.04 / 0.0073 | 21.66 / 0.0204 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.1% | 26.02 / 0.0075 | 21.73 / 0.0198 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.2% | 25.91 / 0.0072 | 22.94 / 0.0156 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.7% | 25.93 / 0.0077 | 22.89 / 0.0159 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.4% | 25.94 / 0.0072 | 23.21 / 0.0156 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.5% | 25.93 / 0.0073 | 23.05 / 0.0157 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 8.5% | 25.64 / 0.0080 | 21.53 / 0.0321 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 13.4% | 26.20 / 0.0111 | 21.21 / 0.0374 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.4% | 26.17 / 0.0118 | 22.10 / 0.0313 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 14.0% | 26.17 / 0.0115 | 22.05 / 0.0345 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.2% | 26.18 / 0.0116 | 22.05 / 0.0325 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 14.6% | 26.16 / 0.0113 | 21.77 / 0.0326 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 15.0% | 26.16 / 0.0117 | 22.76 / 0.0285 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.8% | 26.16 / 0.0113 | 22.71 / 0.0301 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.8% | 26.16 / 0.0116 | 22.81 / 0.0293 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 14.3% | 25.97 / 0.0119 | 20.85 / 0.0462 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 9.6% | 25.43 / 0.0094 | 20.46 / 0.0324 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 11.5% | 25.67 / 0.0107 | 21.19 / 0.0311 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 10.6% | 25.55 / 0.0100 | 21.08 / 0.0315 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 10.9% | 25.57 / 0.0103 | 21.14 / 0.0311 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 10.5% | 25.33 / 0.0107 | 21.88 / 0.0289 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 12.3% | 25.62 / 0.0115 | 22.23 / 0.0295 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 11.4% | 25.45 / 0.0106 | 22.16 / 0.0297 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 11.7% | 25.53 / 0.0107 | 22.18 / 0.0296 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.23 / 0.0524 | 25.92 / 0.0545 | 20.67 / 0.0120 | 30.01 / 0.0363 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.90 / 0.0668 | 23.12 / 0.1203 | 19.79 / 0.0158 | 29.47 / 0.0402 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.19 / 0.0630 | 23.80 / 0.1002 | 20.10 / 0.0148 | 29.48 / 0.0399 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.16 / 0.0649 | 23.73 / 0.1081 | 20.00 / 0.0153 | 29.56 / 0.0401 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.19 / 0.0639 | 23.84 / 0.1030 | 20.05 / 0.0150 | 29.55 / 0.0399 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.69 / 0.0604 | 24.88 / 0.0905 | 20.61 / 0.0135 | 29.75 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.69 / 0.0588 | 24.52 / 0.0873 | 20.60 / 0.0137 | 29.67 / 0.0387 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.74 / 0.0602 | 24.81 / 0.0913 | 20.66 / 0.0136 | 29.77 / 0.0388 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.70 / 0.0594 | 24.68 / 0.0887 | 20.59 / 0.0137 | 29.73 / 0.0387 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.82 / 0.0615 | 24.59 / 0.1038 | 20.66 / 0.0141 | 29.92 / 0.0387 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.57 / 0.0758 | 23.12 / 0.1296 | 19.63 / 0.0174 | 29.44 / 0.0433 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.94 / 0.0693 | 24.06 / 0.1029 | 20.02 / 0.0155 | 29.62 / 0.0418 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.93 / 0.0731 | 23.81 / 0.1170 | 19.94 / 0.0165 | 29.61 / 0.0424 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.94 / 0.0711 | 23.94 / 0.1096 | 19.98 / 0.0162 | 29.61 / 0.0421 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.76 / 0.0710 | 23.42 / 0.1146 | 19.66 / 0.0162 | 29.39 / 0.0427 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.18 / 0.0652 | 25.02 / 0.0945 | 20.37 / 0.0149 | 29.53 / 0.0410 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.12 / 0.0688 | 24.26 / 0.1078 | 20.14 / 0.0153 | 29.56 / 0.0418 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.16 / 0.0670 | 24.60 / 0.1003 | 20.25 / 0.0153 | 29.56 / 0.0413 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.13 / 0.0676 | 24.41 / 0.1133 | 20.40 / 0.0157 | 29.56 / 0.0413 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.71 / 0.0708 | 21.85 / 0.1455 | 19.95 / 0.0155 | 28.87 / 0.0436 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.82 / 0.0690 | 22.13 / 0.1290 | 19.98 / 0.0152 | 28.89 / 0.0434 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.86 / 0.0704 | 22.11 / 0.1396 | 19.98 / 0.0150 | 28.88 / 0.0437 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.85 / 0.0695 | 22.13 / 0.1329 | 19.99 / 0.0151 | 28.89 / 0.0436 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.19 / 0.0688 | 23.48 / 0.1250 | 20.56 / 0.0136 | 28.86 / 0.0450 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.16 / 0.0679 | 23.76 / 0.1138 | 20.72 / 0.0135 | 28.80 / 0.0456 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.19 / 0.0691 | 23.71 / 0.1216 | 20.69 / 0.0133 | 28.78 / 0.0457 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.17 / 0.0687 | 23.76 / 0.1173 | 20.73 / 0.0133 | 28.77 / 0.0460 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.4%） | — | — | 28.23 / 0.0524 | 25.92 / 0.0545 | 30.01 |
| in035 | rife | 3.4% | 9.6% | 26.71 / 0.0708 | 21.85 / 0.1455 | 28.87 |
| in035 | cnw_cnn | 4.0% | 7.7% | 26.90 / 0.0668 | 23.12 / 0.1203 | 29.47 |
| in035 | cnw_f5 | 7.1% | 13.4% | 26.57 / 0.0758 | 23.12 / 0.1296 | 29.44 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.55 / 0.0476 | -1.50 / +0.0246 (core 3.4%) | -1.52 / +0.0183 (core 3.6%) | -2.00 / +0.0312 (core 7.5%) |
| in035 | 2 | 0-3 | 28.64 / 0.0524 | -2.26 / +0.0212 (core 3.4%) | -1.97 / +0.0162 (core 3.6%) | -2.11 / +0.0266 (core 7.5%) |
| in035 | 4 | 3-5 | 28.51 / 0.0572 | -0.80 / +0.0094 (core 2.5%) | -0.51 / +0.0089 (core 2.6%) | -0.87 / +0.0123 (core 3.7%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.23 / 0.0524 | 25.92 | 30.01 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.90 / 0.0668 | 23.12 | 29.47 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 27.72 / 0.0572 | 24.77 | 29.97 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.19 / 0.0630 | 23.80 | 29.48 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 27.87 / 0.0560 | 25.14 | 29.96 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.16 / 0.0649 | 23.73 | 29.56 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 27.84 / 0.0565 | 25.03 | 29.98 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.19 / 0.0639 | 23.84 | 29.55 | 0/3 |
| in035 | cnw_cnn | oracle | 1.3% | 27.86 / 0.0562 | 25.08 | 29.97 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.69 / 0.0604 | 24.88 | 29.75 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.4% | 28.14 / 0.0547 | 26.11 | 29.99 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.69 / 0.0588 | 24.52 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.4% | 28.13 / 0.0542 | 25.87 | 29.97 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.74 / 0.0602 | 24.81 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.4% | 28.16 / 0.0546 | 26.01 | 29.99 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.70 / 0.0594 | 24.68 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.4% | 28.12 / 0.0545 | 25.93 | 29.97 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.82 / 0.0615 | 24.59 | 29.92 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 1.5% | 28.15 / 0.0546 | 26.09 | 30.01 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.57 / 0.0758 | 23.12 | 29.44 | 0/3 |
| in035 | cnw_f5 | oracle | 2.0% | 27.56 / 0.0601 | 24.65 | 29.96 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.94 / 0.0693 | 24.06 | 29.62 | 0/3 |
| in035 | cnw_f5 | oracle | 2.1% | 27.77 / 0.0583 | 25.23 | 29.98 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.93 / 0.0731 | 23.81 | 29.61 | 0/3 |
| in035 | cnw_f5 | oracle | 2.1% | 27.74 / 0.0595 | 24.99 | 29.98 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.94 / 0.0711 | 23.94 | 29.61 | 0/3 |
| in035 | cnw_f5 | oracle | 2.1% | 27.76 / 0.0589 | 25.12 | 29.98 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.76 / 0.0710 | 23.42 | 29.39 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.2% | 27.64 / 0.0580 | 24.90 | 29.98 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.18 / 0.0652 | 25.02 | 29.53 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.2% | 27.98 / 0.0562 | 26.18 | 29.99 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.12 / 0.0688 | 24.26 | 29.56 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.2% | 27.87 / 0.0571 | 25.51 | 29.99 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.16 / 0.0670 | 24.60 | 29.56 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.2% | 27.92 / 0.0567 | 25.80 | 29.99 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.13 / 0.0676 | 24.41 | 29.56 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.2% | 27.97 / 0.0562 | 26.24 | 29.97 | 0/3 |
| in035 | rife | 不复核 | —% | 26.71 / 0.0708 | 21.85 | 28.87 | 0/3 |
| in035 | rife | oracle | 1.3% | 27.79 / 0.0564 | 24.14 | 29.92 | 0/3 |
| in035 | rife | 不复核 | —% | 26.82 / 0.0690 | 22.13 | 28.89 | 0/3 |
| in035 | rife | oracle | 1.6% | 27.82 / 0.0562 | 24.36 | 29.93 | 0/3 |
| in035 | rife | 不复核 | —% | 26.86 / 0.0704 | 22.11 | 28.88 | 0/3 |
| in035 | rife | oracle | 1.5% | 27.84 / 0.0561 | 24.25 | 29.93 | 0/3 |
| in035 | rife | 不复核 | —% | 26.85 / 0.0695 | 22.13 | 28.89 | 0/3 |
| in035 | rife | oracle | 1.5% | 27.84 / 0.0562 | 24.30 | 29.94 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.19 / 0.0688 | 23.48 | 28.86 | 0/3 |
| in035 | rife_mw | oracle | 1.6% | 28.10 / 0.0549 | 25.59 | 29.94 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.16 / 0.0679 | 23.76 | 28.80 | 0/3 |
| in035 | rife_mw | oracle | 1.8% | 28.16 / 0.0543 | 26.01 | 29.93 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.19 / 0.0691 | 23.71 | 28.78 | 0/3 |
| in035 | rife_mw | oracle | 1.7% | 28.15 / 0.0548 | 25.85 | 29.94 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.17 / 0.0687 | 23.76 | 28.77 | 0/3 |
| in035 | rife_mw | oracle | 1.8% | 28.17 / 0.0545 | 25.96 | 29.93 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.23 / 0.0524 | 25.92 / 0.0545 | — |
| in035 | FF | 0（前馈） | 1008×650（63%） | 26.36 | 26.90 / 0.0668 | 23.12 / 0.1203 | 0/3 |
| in035 | 25 | 1.32 s | 1008×650（63%） | 26.93 | 27.16 / 0.0649 | 23.73 / 0.1081 | 0/3 |
| in035 | 50 | 2.60 s | 1008×650（63%） | 27.17 | 27.19 / 0.0639 | 23.84 / 0.1030 | 0/3 |
| in035 | 100 | 5.16 s | 1008×650（63%） | 27.43 | 27.19 / 0.0630 | 23.80 / 0.1002 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.23 / 0.0524 | 25.92 / 0.0545 | 30.01 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.90 / 0.0668 | 23.12 / 0.1203 | 29.47 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.72 / 0.0572 | 24.77 / 0.0811 | 29.97 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.16 / 0.0649 | 23.73 / 0.1081 | 29.56 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.84 / 0.0565 | 25.03 / 0.0764 | 29.98 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.19 / 0.0639 | 23.84 / 0.1030 | 29.55 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.86 / 0.0562 | 25.08 / 0.0734 | 29.97 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.19 / 0.0630 | 23.80 / 0.1002 | 29.48 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.87 / 0.0560 | 25.14 / 0.0717 | 29.96 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.69 / 0.0604 | 24.88 / 0.0905 | 29.75 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.14 / 0.0547 | 26.11 / 0.0626 | 29.99 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.74 / 0.0602 | 24.81 / 0.0913 | 29.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.16 / 0.0546 | 26.01 / 0.0649 | 29.99 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.70 / 0.0594 | 24.68 / 0.0887 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.12 / 0.0545 | 25.93 / 0.0655 | 29.97 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.69 / 0.0588 | 24.52 / 0.0873 | 29.67 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.13 / 0.0542 | 25.87 / 0.0651 | 29.97 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.57 / 0.0758 | 23.12 / 0.1296 | 29.44 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.56 / 0.0601 | 24.65 / 0.0871 | 29.96 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.93 / 0.0731 | 23.81 / 0.1170 | 29.61 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.74 / 0.0595 | 24.99 / 0.0813 | 29.98 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.94 / 0.0711 | 23.94 / 0.1096 | 29.61 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.76 / 0.0589 | 25.12 / 0.0772 | 29.98 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.94 / 0.0693 | 24.06 / 0.1029 | 29.62 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.77 / 0.0583 | 25.23 / 0.0740 | 29.98 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.76 / 0.0710 | 23.42 / 0.1146 | 29.39 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.64 / 0.0580 | 24.90 / 0.0761 | 29.98 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.12 / 0.0688 | 24.26 / 0.1078 | 29.56 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.87 / 0.0571 | 25.51 / 0.0716 | 29.99 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.16 / 0.0670 | 24.60 / 0.1003 | 29.56 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.92 / 0.0567 | 25.80 / 0.0684 | 29.99 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.18 / 0.0652 | 25.02 / 0.0945 | 29.53 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.98 / 0.0562 | 26.18 / 0.0663 | 29.99 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.71 / 0.0708 | 21.85 / 0.1455 | 28.87 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.79 / 0.0564 | 24.14 / 0.0850 | 29.92 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 26.86 / 0.0704 | 22.11 / 0.1396 | 28.88 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.84 / 0.0561 | 24.25 / 0.0839 | 29.93 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 26.85 / 0.0695 | 22.13 / 0.1329 | 28.89 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.84 / 0.0562 | 24.30 / 0.0839 | 29.94 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.82 / 0.0690 | 22.13 / 0.1290 | 28.89 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.82 / 0.0562 | 24.36 / 0.0838 | 29.93 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.19 / 0.0688 | 23.48 / 0.1250 | 28.86 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.10 / 0.0549 | 25.59 / 0.0736 | 29.94 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.19 / 0.0691 | 23.71 / 0.1216 | 28.78 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.15 / 0.0548 | 25.85 / 0.0713 | 29.94 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.17 / 0.0687 | 23.76 / 0.1173 | 28.77 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.17 / 0.0545 | 25.96 / 0.0678 | 29.93 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.16 / 0.0679 | 23.76 / 0.1138 | 28.80 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.16 / 0.0543 | 26.01 / 0.0682 | 29.93 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.92 / 0.0545 | 20.67 / 0.0120 | 30.01 / 0.0363 | 28.23 / 0.0524 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 12.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.92 | 0.7909 | 0.0545 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 15.09 | 0.5540 | 0.2636 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 16.23 | 0.6103 | 0.2154 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 16.06 | 0.6036 | 0.2375 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 16.22 | 0.6130 | 0.2252 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 15.37 | 0.6293 | 0.2036 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 15.72 | 0.6069 | 0.1855 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 15.57 | 0.6358 | 0.1983 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 15.65 | 0.6233 | 0.1905 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.68 | 0.6607 | 0.2125 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 16.57 | 0.5824 | 0.2504 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 18.13 | 0.6559 | 0.1923 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 17.63 | 0.6373 | 0.2209 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 17.90 | 0.6509 | 0.2053 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 18.22 | 0.6165 | 0.1983 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.51 | 0.6788 | 0.1618 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 18.98 | 0.6587 | 0.1849 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 19.21 | 0.6694 | 0.1726 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 20.59 | 0.7005 | 0.1908 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 13.30 | 0.4748 | 0.3004 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 13.87 | 0.5116 | 0.2510 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 13.93 | 0.5126 | 0.2777 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 13.93 | 0.5165 | 0.2647 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.86 | 0.5865 | 0.2577 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 13.71 | 0.6295 | 0.2188 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 13.28 | 0.6241 | 0.2431 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 13.51 | 0.6301 | 0.2297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.77 | 0.7604 | 0.0811 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.14 | 0.7708 | 0.0717 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.03 | 0.7666 | 0.0764 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.08 | 0.7691 | 0.0734 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.11 | 0.7872 | 0.0626 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.87 | 0.7851 | 0.0651 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.01 | 0.7885 | 0.0649 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.93 | 0.7873 | 0.0655 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.09 | 0.8041 | 0.0652 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.65 | 0.7602 | 0.0871 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.23 | 0.7785 | 0.0740 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.99 | 0.7715 | 0.0813 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.12 | 0.7751 | 0.0772 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.90 | 0.7666 | 0.0761 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.18 | 0.7964 | 0.0663 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.51 | 0.7793 | 0.0716 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.80 | 0.7870 | 0.0684 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.24 | 0.8098 | 0.0646 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.14 | 0.7435 | 0.0850 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.36 | 0.7444 | 0.0838 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.25 | 0.7447 | 0.0839 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.30 | 0.7451 | 0.0839 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.59 | 0.7827 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.01 | 0.7981 | 0.0682 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.85 | 0.7936 | 0.0713 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.96 | 0.7970 | 0.0678 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.12 | 0.7073 | 0.1203 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.80 | 0.7307 | 0.1002 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.73 | 0.7261 | 0.1081 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.84 | 0.7306 | 0.1030 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.88 | 0.7446 | 0.0905 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.52 | 0.7357 | 0.0873 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.81 | 0.7460 | 0.0913 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.68 | 0.7418 | 0.0887 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.59 | 0.7678 | 0.1038 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.12 | 0.7119 | 0.1296 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.06 | 0.7477 | 0.1029 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.81 | 0.7379 | 0.1170 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.94 | 0.7441 | 0.1096 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.42 | 0.7040 | 0.1146 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.02 | 0.7555 | 0.0945 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.26 | 0.7306 | 0.1078 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.60 | 0.7427 | 0.1003 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.41 | 0.7681 | 0.1133 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.85 | 0.6563 | 0.1455 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.13 | 0.6552 | 0.1290 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.11 | 0.6626 | 0.1396 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.13 | 0.6618 | 0.1329 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.48 | 0.7220 | 0.1250 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.76 | 0.7447 | 0.1138 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.71 | 0.7405 | 0.1216 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.76 | 0.7441 | 0.1173 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.67 | 0.6410 | 0.0120 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.97 | 0.2571 | 0.0982 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.17 | 0.2955 | 0.0933 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.07 | 0.2833 | 0.0960 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.11 | 0.2913 | 0.0948 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.16 | 0.3495 | 0.0935 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.24 | 0.3456 | 0.0906 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.19 | 0.3551 | 0.0929 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.21 | 0.3500 | 0.0919 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.09 | 0.3694 | 0.0615 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.14 | 0.3280 | 0.0802 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.43 | 0.3731 | 0.0753 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.30 | 0.3592 | 0.0782 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.37 | 0.3677 | 0.0768 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.38 | 0.3688 | 0.0759 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.47 | 0.4176 | 0.0733 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.42 | 0.3975 | 0.0743 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.43 | 0.4059 | 0.0741 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.83 | 0.4292 | 0.0502 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.74 | 0.1944 | 0.1080 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.09 | 0.2178 | 0.1043 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.82 | 0.2097 | 0.1065 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.94 | 0.2142 | 0.1056 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.81 | 0.2843 | 0.1039 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.94 | 0.3109 | 0.1011 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.86 | 0.3026 | 0.1029 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.90 | 0.3076 | 0.1021 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.85 | 0.6034 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.13 | 0.6194 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.06 | 0.6116 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.09 | 0.6151 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.63 | 0.6430 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.62 | 0.6462 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.68 | 0.6460 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.61 | 0.6454 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.65 | 0.6608 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.66 | 0.6022 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.03 | 0.6249 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.95 | 0.6163 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.99 | 0.6205 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.68 | 0.6161 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.39 | 0.6525 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.15 | 0.6334 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.26 | 0.6415 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.40 | 0.6546 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.99 | 0.5936 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.02 | 0.5941 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.02 | 0.5930 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.03 | 0.5942 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.58 | 0.6416 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.76 | 0.6652 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.70 | 0.6555 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.75 | 0.6615 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.79 | 0.5986 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.10 | 0.6163 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.00 | 0.6077 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.05 | 0.6118 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.61 | 0.6407 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.60 | 0.6442 | 0.0137 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.66 | 0.6439 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.59 | 0.6436 | 0.0137 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.66 | 0.6592 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.63 | 0.5977 | 0.0174 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.02 | 0.6219 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.94 | 0.6135 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.98 | 0.6177 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.66 | 0.6129 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.37 | 0.6496 | 0.0149 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.14 | 0.6308 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.25 | 0.6387 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.40 | 0.6514 | 0.0157 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.95 | 0.5889 | 0.0155 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.98 | 0.5895 | 0.0152 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.98 | 0.5888 | 0.0150 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.99 | 0.5899 | 0.0151 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.56 | 0.6398 | 0.0136 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.72 | 0.6625 | 0.0135 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.69 | 0.6535 | 0.0133 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.73 | 0.6593 | 0.0133 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 30.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.43 | 0.7844 | 0.0210 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.20 | 0.4336 | 0.2409 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.42 | 0.4581 | 0.2283 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.29 | 0.4544 | 0.2353 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.34 | 0.4574 | 0.2319 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.31 | 0.4745 | 0.2301 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.49 | 0.4794 | 0.2203 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.35 | 0.4848 | 0.2269 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.40 | 0.4827 | 0.2238 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.94 | 0.3439 | 0.1857 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.63 | 0.4884 | 0.2059 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.98 | 0.5196 | 0.1897 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.79 | 0.5174 | 0.1988 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.88 | 0.5210 | 0.1942 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.82 | 0.5159 | 0.1955 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.03 | 0.5445 | 0.1825 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.89 | 0.5433 | 0.1898 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.94 | 0.5454 | 0.1866 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.08 | 0.4172 | 0.1623 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.94 | 0.4239 | 0.2349 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.16 | 0.4409 | 0.2226 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.03 | 0.4417 | 0.2301 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.08 | 0.4423 | 0.2267 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.00 | 0.4661 | 0.2272 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.21 | 0.4850 | 0.2171 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.06 | 0.4841 | 0.2237 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.12 | 0.4859 | 0.2206 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.62 | 0.7698 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.94 | 0.7747 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.86 | 0.7731 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.89 | 0.7740 | 0.0244 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.27 | 0.7812 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.40 | 0.7828 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.38 | 0.7831 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.35 | 0.7828 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.92 | 0.7811 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.31 | 0.7647 | 0.0288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.67 | 0.7730 | 0.0264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.60 | 0.7704 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.64 | 0.7717 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.45 | 0.7690 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.18 | 0.7818 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.97 | 0.7764 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.09 | 0.7789 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.48 | 0.7746 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.62 | 0.7668 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.74 | 0.7675 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.73 | 0.7685 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.74 | 0.7683 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.33 | 0.7820 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.52 | 0.7886 | 0.0228 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.48 | 0.7867 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.51 | 0.7880 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.29 | 0.7420 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.82 | 0.7530 | 0.0299 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.72 | 0.7514 | 0.0311 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.77 | 0.7529 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.27 | 0.7602 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.41 | 0.7609 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.44 | 0.7641 | 0.0274 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.42 | 0.7630 | 0.0274 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.87 | 0.7396 | 0.0417 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.55 | 0.7207 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.00 | 0.7367 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.00 | 0.7357 | 0.0393 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.99 | 0.7368 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.84 | 0.7273 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.51 | 0.7453 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.48 | 0.7432 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.54 | 0.7449 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.65 | 0.7101 | 0.0533 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.13 | 0.7288 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.34 | 0.7304 | 0.0355 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.48 | 0.7357 | 0.0359 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.47 | 0.7346 | 0.0349 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.33 | 0.7616 | 0.0340 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.28 | 0.7698 | 0.0329 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.54 | 0.7710 | 0.0333 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.43 | 0.7710 | 0.0332 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 42.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.17 | 0.7481 | 0.0277 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.11 | 0.3713 | 0.3620 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.24 | 0.3877 | 0.3508 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.17 | 0.3848 | 0.3567 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.20 | 0.3867 | 0.3539 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.15 | 0.4041 | 0.3505 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.21 | 0.4035 | 0.3445 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.16 | 0.4083 | 0.3493 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.18 | 0.4060 | 0.3473 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.49 | 0.2882 | 0.2362 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.30 | 0.4292 | 0.3284 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.47 | 0.4511 | 0.3132 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.38 | 0.4491 | 0.3211 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.43 | 0.4514 | 0.3172 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.37 | 0.4510 | 0.3169 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.45 | 0.4637 | 0.3071 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.40 | 0.4654 | 0.3127 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.42 | 0.4651 | 0.3102 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.63 | 0.3768 | 0.2103 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.91 | 0.3604 | 0.3632 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.05 | 0.3747 | 0.3512 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.97 | 0.3733 | 0.3582 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.01 | 0.3746 | 0.3552 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.93 | 0.3900 | 0.3552 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.00 | 0.3991 | 0.3487 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.95 | 0.3985 | 0.3533 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.97 | 0.3991 | 0.3513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.28 | 0.7377 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.59 | 0.7413 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.52 | 0.7399 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.54 | 0.7406 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.05 | 0.7462 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.04 | 0.7465 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.09 | 0.7469 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.01 | 0.7466 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.13 | 0.7496 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.01 | 0.7351 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.39 | 0.7409 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.33 | 0.7393 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.36 | 0.7402 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.16 | 0.7380 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.79 | 0.7455 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.57 | 0.7419 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.68 | 0.7436 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.92 | 0.7479 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.51 | 0.7379 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.62 | 0.7390 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.62 | 0.7394 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.62 | 0.7393 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.18 | 0.7480 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.43 | 0.7524 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.34 | 0.7511 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.40 | 0.7520 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.10 | 0.7199 | 0.0390 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.65 | 0.7272 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.56 | 0.7259 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.62 | 0.7269 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.33 | 0.7340 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.32 | 0.7337 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.36 | 0.7350 | 0.0337 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.30 | 0.7344 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.47 | 0.7390 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.50 | 0.7103 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.07 | 0.7210 | 0.0409 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.08 | 0.7200 | 0.0436 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.08 | 0.7209 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.91 | 0.7157 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.54 | 0.7261 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.46 | 0.7236 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.51 | 0.7249 | 0.0388 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.59 | 0.7301 | 0.0414 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.20 | 0.7162 | 0.0410 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.53 | 0.7182 | 0.0383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.57 | 0.7203 | 0.0395 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.57 | 0.7199 | 0.0388 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.35 | 0.7346 | 0.0376 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.61 | 0.7401 | 0.0364 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.52 | 0.7396 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.58 | 0.7403 | 0.0371 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 76.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.01 | 0.7311 | 0.0363 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.85 | 0.3204 | 0.3968 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.92 | 0.3271 | 0.3887 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.88 | 0.3273 | 0.3931 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.90 | 0.3278 | 0.3910 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.87 | 0.3315 | 0.3892 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.90 | 0.3270 | 0.3843 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.88 | 0.3332 | 0.3877 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.88 | 0.3305 | 0.3860 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.37 | 0.1680 | 0.2975 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.58 | 0.3626 | 0.3682 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.69 | 0.3728 | 0.3563 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.63 | 0.3731 | 0.3624 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.66 | 0.3737 | 0.3592 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.62 | 0.3748 | 0.3594 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.66 | 0.3735 | 0.3495 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.63 | 0.3806 | 0.3543 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.64 | 0.3776 | 0.3517 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.92 | 0.2424 | 0.2719 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.72 | 0.3014 | 0.4056 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.89 | 0.3094 | 0.3972 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.78 | 0.3075 | 0.4024 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.84 | 0.3090 | 0.3999 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.70 | 0.3102 | 0.4019 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.76 | 0.3101 | 0.3962 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.72 | 0.3125 | 0.4002 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.74 | 0.3115 | 0.3984 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.97 | 0.7304 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.96 | 0.7306 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.98 | 0.7307 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.97 | 0.7306 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.99 | 0.7308 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.97 | 0.7306 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.99 | 0.7308 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.97 | 0.7307 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.01 | 0.7312 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.96 | 0.7304 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.98 | 0.7308 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.98 | 0.7308 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.98 | 0.7308 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.98 | 0.7306 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.99 | 0.7308 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.99 | 0.7307 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.99 | 0.7308 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.97 | 0.7310 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.92 | 0.7300 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.93 | 0.7301 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.93 | 0.7301 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.94 | 0.7302 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.94 | 0.7303 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.93 | 0.7302 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.94 | 0.7303 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.93 | 0.7303 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.47 | 0.7259 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.48 | 0.7266 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.56 | 0.7270 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.55 | 0.7270 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.75 | 0.7283 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.67 | 0.7276 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.77 | 0.7287 | 0.0388 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.73 | 0.7283 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.92 | 0.7302 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.44 | 0.7270 | 0.0433 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.62 | 0.7287 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.61 | 0.7288 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.61 | 0.7288 | 0.0421 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.39 | 0.7264 | 0.0427 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.53 | 0.7269 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.56 | 0.7279 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.56 | 0.7276 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.56 | 0.7290 | 0.0413 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.87 | 0.7218 | 0.0436 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.89 | 0.7215 | 0.0434 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.88 | 0.7219 | 0.0437 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.89 | 0.7219 | 0.0436 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.86 | 0.7216 | 0.0450 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.80 | 0.7206 | 0.0456 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.78 | 0.7213 | 0.0457 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.77 | 0.7208 | 0.0460 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.23 | 0.7388 | 0.0524 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.44 | 0.3324 | 0.4660 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.52 | 0.3441 | 0.4500 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.48 | 0.3430 | 0.4587 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.50 | 0.3443 | 0.4545 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.48 | 0.3550 | 0.4468 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.51 | 0.3513 | 0.4373 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.48 | 0.3579 | 0.4446 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.49 | 0.3550 | 0.4409 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.51 | 0.2190 | 0.3821 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.27 | 0.3780 | 0.4357 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.39 | 0.3952 | 0.4125 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.32 | 0.3934 | 0.4261 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.36 | 0.3954 | 0.4194 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.32 | 0.3967 | 0.4158 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.37 | 0.4026 | 0.3987 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.34 | 0.4063 | 0.4087 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.35 | 0.4049 | 0.4032 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.17 | 0.2947 | 0.3427 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.25 | 0.3115 | 0.4735 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.43 | 0.3227 | 0.4596 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.32 | 0.3206 | 0.4684 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.37 | 0.3223 | 0.4642 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.25 | 0.3318 | 0.4608 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.31 | 0.3361 | 0.4519 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.27 | 0.3370 | 0.4585 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.29 | 0.3369 | 0.4554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.72 | 0.7331 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.87 | 0.7348 | 0.0560 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.84 | 0.7343 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.86 | 0.7346 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.14 | 0.7374 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.13 | 0.7376 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.16 | 0.7378 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.12 | 0.7377 | 0.0545 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.15 | 0.7394 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.56 | 0.7320 | 0.0601 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.77 | 0.7348 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.74 | 0.7340 | 0.0595 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.76 | 0.7345 | 0.0589 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.64 | 0.7335 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.98 | 0.7372 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.87 | 0.7355 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.92 | 0.7363 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.97 | 0.7382 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.79 | 0.7323 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.82 | 0.7325 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.84 | 0.7328 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.84 | 0.7329 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.10 | 0.7373 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.16 | 0.7392 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.15 | 0.7386 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.17 | 0.7391 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.90 | 0.7229 | 0.0668 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.19 | 0.7263 | 0.0630 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.16 | 0.7260 | 0.0649 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.19 | 0.7264 | 0.0639 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.69 | 0.7307 | 0.0604 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.69 | 0.7304 | 0.0588 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.74 | 0.7316 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.70 | 0.7311 | 0.0594 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.82 | 0.7342 | 0.0615 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.57 | 0.7194 | 0.0758 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.94 | 0.7250 | 0.0693 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.93 | 0.7244 | 0.0731 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.94 | 0.7249 | 0.0711 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.76 | 0.7211 | 0.0710 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.18 | 0.7265 | 0.0652 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.12 | 0.7255 | 0.0688 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.16 | 0.7261 | 0.0670 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.13 | 0.7293 | 0.0676 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.71 | 0.7180 | 0.0708 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.82 | 0.7178 | 0.0690 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.86 | 0.7191 | 0.0704 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.85 | 0.7189 | 0.0695 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.19 | 0.7261 | 0.0688 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.16 | 0.7276 | 0.0679 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.19 | 0.7277 | 0.0691 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.17 | 0.7278 | 0.0687 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 268573 | 0.324 | 64.3 | 28.76 | 0.11 | 0.027 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 268573 | 0.324 | 65.8 | 28.76 | 0.11 | 0.027 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 268573 | 0.324 | 69.6 | 28.76 | 0.11 | 0.027 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 268573 | 0.324 | 74.0 | 28.76 | 0.11 | 0.027 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 732 | None | classic | 0.80 | False | 610981 | 1.312 | 259.2 | 29.29 | 0.21 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 732 | None | classic | 0.80 | False | 610981 | 1.312 | 247.9 | 29.29 | 0.21 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 732 | None | classic | 0.80 | False | 610981 | 1.312 | 245.9 | 29.29 | 0.21 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 732 | None | classic | 0.80 | False | 610981 | 1.312 | 259.7 | 29.29 | 0.21 | 0.006 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1341063 | 0.804 | 467.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 262933 | 0.339 | 58.2 | 28.41 | 0.12 | 0.020 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 262933 | 0.339 | 57.8 | 28.41 | 0.12 | 0.020 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 262933 | 0.339 | 56.3 | 28.41 | 0.12 | 0.020 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 262933 | 0.339 | 66.0 | 28.41 | 0.12 | 0.020 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 946 | None | classic | 1.34 | False | 526143 | 0.988 | 190.1 | 29.14 | 0.11 | 0.012 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 946 | None | classic | 1.34 | False | 526143 | 0.988 | 199.7 | 29.14 | 0.11 | 0.012 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 946 | None | classic | 1.34 | False | 526143 | 0.988 | 196.5 | 29.14 | 0.11 | 0.012 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 946 | None | classic | 1.34 | False | 526143 | 0.988 | 159.5 | 29.14 | 0.11 | 0.012 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1898283 | 0.804 | 112.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 261514 | 0.939 | 91.2 | 28.62 | 0.17 | 0.031 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 261514 | 0.939 | 64.3 | 28.62 | 0.17 | 0.031 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 261514 | 0.939 | 87.0 | 28.62 | 0.17 | 0.031 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 261514 | 0.939 | 68.0 | 28.62 | 0.17 | 0.031 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 838 | None | classic | 0.58 | False | 465272 | 0.978 | 184.0 | 27.94 | 0.06 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 838 | None | classic | 0.58 | False | 465272 | 0.978 | 168.5 | 27.94 | 0.06 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 838 | None | classic | 0.58 | False | 465272 | 0.978 | 151.1 | 27.94 | 0.06 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 838 | None | classic | 0.58 | False | 465272 | 0.978 | 194.6 | 27.94 | 0.06 | 0.007 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.563 | 0.021 |
| in035 | mask_ent | 0.707 | 0.021 |
| in035 | mask_grad | 0.410 | 0.021 |
| in035 | r_col | 0.807 | 0.021 |
| in035 | r_warp | 0.810 | 0.021 |

# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 9.9% | 22.70 / 0.0151 | 21.26 / 0.0291 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 10.1% | 22.72 / 0.0150 | 22.54 / 0.0241 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.9% | 22.70 / 0.0149 | 22.27 / 0.0260 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.9% | 22.70 / 0.0149 | 22.34 / 0.0250 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.0% | 22.77 / 0.0143 | 22.06 / 0.0227 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.6% | 22.95 / 0.0152 | 22.97 / 0.0204 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.1% | 22.79 / 0.0144 | 22.33 / 0.0211 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 10.2% | 22.84 / 0.0147 | 22.69 / 0.0200 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 10.4% | 22.95 / 0.0163 | 21.14 / 0.0390 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 13.9% | 23.34 / 0.0160 | 20.38 / 0.0366 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.2% | 23.43 / 0.0165 | 21.54 / 0.0296 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 13.9% | 23.36 / 0.0162 | 21.17 / 0.0325 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.0% | 23.39 / 0.0164 | 21.27 / 0.0309 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 13.7% | 23.33 / 0.0153 | 21.64 / 0.0272 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.0% | 23.40 / 0.0158 | 22.76 / 0.0219 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 13.7% | 23.34 / 0.0153 | 22.42 / 0.0233 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 13.8% | 23.35 / 0.0155 | 22.58 / 0.0216 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 13.8% | 23.70 / 0.0167 | 21.26 / 0.0428 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 6.9% | 22.07 / 0.0131 | 22.21 / 0.0225 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 7.5% | 22.38 / 0.0130 | 23.39 / 0.0199 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 7.2% | 22.20 / 0.0132 | 23.04 / 0.0206 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 7.2% | 22.26 / 0.0132 | 23.29 / 0.0202 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 7.7% | 22.37 / 0.0128 | 23.28 / 0.0178 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 8.0% | 22.51 / 0.0135 | 23.52 / 0.0181 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 7.8% | 22.40 / 0.0134 | 23.54 / 0.0174 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 7.8% | 22.42 / 0.0135 | 23.61 / 0.0169 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.69 / 0.0550 | 23.18 / 0.1017 | 18.99 / 0.0156 | 29.70 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.58 / 0.0649 | 23.95 / 0.1513 | 20.21 / 0.0168 | 29.51 / 0.0387 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.95 / 0.0618 | 24.73 / 0.1320 | 20.63 / 0.0157 | 29.62 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.86 / 0.0635 | 24.64 / 0.1451 | 20.59 / 0.0161 | 29.59 / 0.0384 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.89 / 0.0627 | 24.65 / 0.1403 | 20.56 / 0.0159 | 29.61 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.81 / 0.0617 | 23.19 / 0.1366 | 20.37 / 0.0162 | 29.64 / 0.0384 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.18 / 0.0587 | 24.87 / 0.1127 | 21.15 / 0.0148 | 29.65 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.93 / 0.0609 | 24.20 / 0.1261 | 20.47 / 0.0162 | 29.65 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.06 / 0.0597 | 24.57 / 0.1194 | 20.84 / 0.0156 | 29.66 / 0.0377 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.67 / 0.0624 | 23.96 / 0.1693 | 19.95 / 0.0179 | 29.66 / 0.0377 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.61 / 0.0731 | 24.09 / 0.1462 | 19.77 / 0.0187 | 29.00 / 0.0429 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.09 / 0.0670 | 25.36 / 0.1209 | 20.54 / 0.0161 | 29.25 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.94 / 0.0701 | 25.03 / 0.1315 | 20.22 / 0.0173 | 29.18 / 0.0420 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.98 / 0.0686 | 25.22 / 0.1266 | 20.33 / 0.0168 | 29.22 / 0.0418 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.36 / 0.0658 | 24.62 / 0.1251 | 20.08 / 0.0169 | 29.47 / 0.0401 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.99 / 0.0591 | 26.76 / 0.0919 | 21.32 / 0.0144 | 29.58 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.71 / 0.0629 | 25.59 / 0.1143 | 20.58 / 0.0158 | 29.53 / 0.0392 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.81 / 0.0609 | 26.11 / 0.1049 | 20.84 / 0.0150 | 29.54 / 0.0388 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.30 / 0.0661 | 23.81 / 0.1737 | 19.85 / 0.0190 | 29.58 / 0.0385 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 28.06 / 0.0609 | 24.66 / 0.1474 | 20.95 / 0.0152 | 29.59 / 0.0374 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.28 / 0.0586 | 25.67 / 0.1242 | 21.30 / 0.0137 | 29.64 / 0.0371 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.20 / 0.0601 | 25.16 / 0.1413 | 21.14 / 0.0146 | 29.63 / 0.0373 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.24 / 0.0595 | 25.36 / 0.1332 | 21.20 / 0.0143 | 29.64 / 0.0373 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.29 / 0.0586 | 24.20 / 0.1299 | 21.20 / 0.0144 | 29.67 / 0.0371 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.45 / 0.0564 | 24.92 / 0.1139 | 21.56 / 0.0135 | 29.68 / 0.0367 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.35 / 0.0580 | 24.53 / 0.1257 | 21.37 / 0.0143 | 29.66 / 0.0370 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.39 / 0.0573 | 24.75 / 0.1208 | 21.45 / 0.0139 | 29.66 / 0.0369 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.7%） | — | — | 27.69 / 0.0550 | 23.18 / 0.1017 | 29.70 |
| in035 | rife | 3.6% | 6.9% | 28.06 / 0.0609 | 24.66 / 0.1474 | 29.59 |
| in035 | cnw_cnn | 6.7% | 9.9% | 27.58 / 0.0649 | 23.95 / 0.1513 | 29.51 |
| in035 | cnw_f5 | 9.0% | 13.9% | 26.61 / 0.0731 | 24.09 / 0.1462 | 29.00 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.99 / 0.0551 | +0.24 / +0.0076 (core 3.6%) | +0.07 / +0.0108 (core 7.4%) | -0.84 / +0.0203 (core 10.4%) |
| in035 | 2 | 0-3 | 27.48 / 0.0541 | +0.34 / +0.0069 (core 3.6%) | -0.40 / +0.0128 (core 7.4%) | -1.54 / +0.0246 (core 10.4%) |
| in035 | 4 | 3-5 | 28.60 / 0.0559 | +0.52 / +0.0032 (core 2.1%) | +0.00 / +0.0062 (core 3.3%) | -0.87 / +0.0095 (core 4.0%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.69 / 0.0550 | 23.18 | 29.70 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.58 / 0.0649 | 23.95 | 29.51 | 0/3 |
| in035 | cnw_cnn | oracle | 2.2% | 27.99 / 0.0577 | 24.43 | 29.70 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.95 / 0.0618 | 24.73 | 29.62 | 0/3 |
| in035 | cnw_cnn | oracle | 2.3% | 28.21 / 0.0563 | 24.98 | 29.70 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.86 / 0.0635 | 24.64 | 29.59 | 0/3 |
| in035 | cnw_cnn | oracle | 2.2% | 28.16 / 0.0568 | 24.82 | 29.70 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.89 / 0.0627 | 24.65 | 29.61 | 0/3 |
| in035 | cnw_cnn | oracle | 2.3% | 28.17 / 0.0568 | 24.82 | 29.70 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.81 / 0.0617 | 23.19 | 29.64 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.2% | 28.08 / 0.0558 | 24.09 | 29.70 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.18 / 0.0587 | 24.87 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.3% | 28.38 / 0.0549 | 25.22 | 29.70 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.93 / 0.0609 | 24.20 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.2% | 28.15 / 0.0557 | 24.73 | 29.70 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.06 / 0.0597 | 24.57 | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.2% | 28.27 / 0.0555 | 25.00 | 29.70 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.67 / 0.0624 | 23.96 | 29.66 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.3% | 27.98 / 0.0576 | 25.57 | 29.71 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.61 / 0.0731 | 24.09 | 29.00 | 0/3 |
| in035 | cnw_f5 | oracle | 2.9% | 27.77 / 0.0600 | 24.66 | 29.68 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.09 / 0.0670 | 25.36 | 29.25 | 0/3 |
| in035 | cnw_f5 | oracle | 3.0% | 28.11 / 0.0573 | 25.59 | 29.68 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.94 / 0.0701 | 25.03 | 29.18 | 0/3 |
| in035 | cnw_f5 | oracle | 2.9% | 27.98 / 0.0588 | 25.25 | 29.69 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.98 / 0.0686 | 25.22 | 29.22 | 0/3 |
| in035 | cnw_f5 | oracle | 3.0% | 28.03 / 0.0583 | 25.38 | 29.68 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.36 / 0.0658 | 24.62 | 29.47 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.9% | 27.97 / 0.0567 | 25.33 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.99 / 0.0591 | 26.76 | 29.58 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.0% | 28.44 / 0.0541 | 27.16 | 29.71 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.71 / 0.0629 | 25.59 | 29.53 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.9% | 28.19 / 0.0557 | 25.99 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.81 / 0.0609 | 26.11 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.9% | 28.29 / 0.0550 | 26.48 | 29.71 | 2/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.30 / 0.0661 | 23.81 | 29.58 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.9% | 27.90 / 0.0585 | 25.94 | 29.71 | 0/3 |
| in035 | rife | 不复核 | —% | 28.06 / 0.0609 | 24.66 | 29.59 | 0/3 |
| in035 | rife | oracle | 1.7% | 28.26 / 0.0558 | 25.32 | 29.70 | 1/3 |
| in035 | rife | 不复核 | —% | 28.28 / 0.0586 | 25.67 | 29.64 | 0/3 |
| in035 | rife | oracle | 1.8% | 28.39 / 0.0545 | 25.81 | 29.70 | 2/3 |
| in035 | rife | 不复核 | —% | 28.20 / 0.0601 | 25.16 | 29.63 | 0/3 |
| in035 | rife | oracle | 1.8% | 28.34 / 0.0555 | 25.44 | 29.70 | 2/3 |
| in035 | rife | 不复核 | —% | 28.24 / 0.0595 | 25.36 | 29.64 | 0/3 |
| in035 | rife | oracle | 1.8% | 28.36 / 0.0551 | 25.57 | 29.70 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.29 / 0.0586 | 24.20 | 29.67 | 0/3 |
| in035 | rife_mw | oracle | 1.8% | 28.40 / 0.0547 | 25.05 | 29.70 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.45 / 0.0564 | 24.92 | 29.68 | 1/3 |
| in035 | rife_mw | oracle | 1.9% | 28.52 / 0.0536 | 25.35 | 29.70 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.35 / 0.0580 | 24.53 | 29.66 | 0/3 |
| in035 | rife_mw | oracle | 1.9% | 28.46 / 0.0544 | 25.02 | 29.70 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 28.39 / 0.0573 | 24.75 | 29.66 | 0/3 |
| in035 | rife_mw | oracle | 1.9% | 28.49 / 0.0540 | 25.18 | 29.70 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.69 / 0.0550 | 23.18 / 0.1017 | — |
| in035 | FF | 0（前馈） | 1008×693（65%） | 26.96 | 27.58 / 0.0649 | 23.95 / 0.1513 | 0/3 |
| in035 | 25 | 1.41 s | 1008×693（65%） | 27.40 | 27.86 / 0.0635 | 24.64 / 0.1451 | 0/3 |
| in035 | 50 | 2.82 s | 1008×693（65%） | 27.59 | 27.89 / 0.0627 | 24.65 / 0.1403 | 0/3 |
| in035 | 100 | 5.61 s | 1008×693（65%） | 27.78 | 27.95 / 0.0618 | 24.73 / 0.1320 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.69 / 0.0550 | 23.18 / 0.1017 | 29.70 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.58 / 0.0649 | 23.95 / 0.1513 | 29.51 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.99 / 0.0577 | 24.43 / 0.1104 | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.86 / 0.0635 | 24.64 / 0.1451 | 29.59 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.16 / 0.0568 | 24.82 / 0.1095 | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.89 / 0.0627 | 24.65 / 0.1403 | 29.61 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.17 / 0.0568 | 24.82 / 0.1086 | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.95 / 0.0618 | 24.73 / 0.1320 | 29.62 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.21 / 0.0563 | 24.98 / 0.1030 | 29.70 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.81 / 0.0617 | 23.19 / 0.1366 | 29.64 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.08 / 0.0558 | 24.09 / 0.1055 | 29.70 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.93 / 0.0609 | 24.20 / 0.1261 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.15 / 0.0557 | 24.73 / 0.1033 | 29.70 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.06 / 0.0597 | 24.57 / 0.1194 | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.27 / 0.0555 | 25.00 / 0.1021 | 29.70 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.18 / 0.0587 | 24.87 / 0.1127 | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.38 / 0.0549 | 25.22 / 0.0968 | 29.70 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.61 / 0.0731 | 24.09 / 0.1462 | 29.00 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.77 / 0.0600 | 24.66 / 0.1087 | 29.68 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.94 / 0.0701 | 25.03 / 0.1315 | 29.18 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.98 / 0.0588 | 25.25 / 0.1005 | 29.69 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.98 / 0.0686 | 25.22 / 0.1266 | 29.22 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.03 / 0.0583 | 25.38 / 0.0994 | 29.68 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.09 / 0.0670 | 25.36 / 0.1209 | 29.25 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.11 / 0.0573 | 25.59 / 0.0958 | 29.68 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.36 / 0.0658 | 24.62 / 0.1251 | 29.47 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.97 / 0.0567 | 25.33 / 0.0888 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.71 / 0.0629 | 25.59 / 0.1143 | 29.53 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.19 / 0.0557 | 25.99 / 0.0847 | 29.71 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.81 / 0.0609 | 26.11 / 0.1049 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.29 / 0.0550 | 26.48 / 0.0792 | 29.71 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.99 / 0.0591 | 26.76 / 0.0919 | 29.58 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.44 / 0.0541 | 27.16 / 0.0677 | 29.71 | 3/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 28.06 / 0.0609 | 24.66 / 0.1474 | 29.59 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.26 / 0.0558 | 25.32 / 0.1017 | 29.70 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.20 / 0.0601 | 25.16 / 0.1413 | 29.63 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.34 / 0.0555 | 25.44 / 0.1009 | 29.70 | 2/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.24 / 0.0595 | 25.36 / 0.1332 | 29.64 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.36 / 0.0551 | 25.57 / 0.0964 | 29.70 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.28 / 0.0586 | 25.67 / 0.1242 | 29.64 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.39 / 0.0545 | 25.81 / 0.0929 | 29.70 | 2/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 28.29 / 0.0586 | 24.20 / 0.1299 | 29.67 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.40 / 0.0547 | 25.05 / 0.0944 | 29.70 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.35 / 0.0580 | 24.53 / 0.1257 | 29.66 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.46 / 0.0544 | 25.02 / 0.0979 | 29.70 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.39 / 0.0573 | 24.75 / 0.1208 | 29.66 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.49 / 0.0540 | 25.18 / 0.0969 | 29.70 | 2/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.45 / 0.0564 | 24.92 / 0.1139 | 29.68 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.52 / 0.0536 | 25.35 / 0.0904 | 29.70 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.18 / 0.1017 | 18.99 / 0.0156 | 29.70 / 0.0360 | 27.69 / 0.0550 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.18 | 0.6861 | 0.1017 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 23.96 | 0.7610 | 0.1676 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 24.57 | 0.7811 | 0.1373 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 24.69 | 0.7841 | 0.1559 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 24.64 | 0.7851 | 0.1469 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 22.90 | 0.7325 | 0.1472 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 24.91 | 0.7965 | 0.1134 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 24.03 | 0.7720 | 0.1352 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 24.48 | 0.7852 | 0.1255 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 23.57 | 0.7815 | 0.1857 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 23.12 | 0.7449 | 0.1781 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 23.73 | 0.7861 | 0.1478 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 23.96 | 0.7757 | 0.1614 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 24.01 | 0.7838 | 0.1546 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 23.50 | 0.7648 | 0.1520 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 25.22 | 0.8117 | 0.1160 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 24.33 | 0.7953 | 0.1434 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 24.78 | 0.8062 | 0.1327 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 23.53 | 0.7773 | 0.1902 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 22.99 | 0.7615 | 0.1873 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 24.58 | 0.8066 | 0.1432 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 23.76 | 0.7908 | 0.1726 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 24.07 | 0.8002 | 0.1578 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 22.87 | 0.7449 | 0.1475 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 23.76 | 0.7875 | 0.1176 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 23.41 | 0.7742 | 0.1319 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 23.62 | 0.7824 | 0.1264 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.43 | 0.7347 | 0.1104 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.98 | 0.7508 | 0.1030 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.82 | 0.7465 | 0.1095 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.82 | 0.7487 | 0.1086 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.09 | 0.7307 | 0.1055 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.22 | 0.7667 | 0.0968 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.73 | 0.7464 | 0.1033 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.00 | 0.7554 | 0.1021 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.57 | 0.7792 | 0.1028 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.66 | 0.7596 | 0.1087 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.59 | 0.7874 | 0.0958 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.25 | 0.7760 | 0.1005 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.38 | 0.7822 | 0.0994 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.33 | 0.7852 | 0.0888 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.16 | 0.8143 | 0.0677 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.99 | 0.7977 | 0.0847 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.48 | 0.8051 | 0.0792 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.94 | 0.8021 | 0.0941 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.32 | 0.7491 | 0.1017 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.81 | 0.7716 | 0.0929 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.44 | 0.7616 | 0.1009 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.57 | 0.7677 | 0.0964 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.05 | 0.7530 | 0.0944 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.35 | 0.7708 | 0.0904 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.02 | 0.7612 | 0.0979 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.18 | 0.7661 | 0.0969 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.95 | 0.7437 | 0.1513 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.73 | 0.7653 | 0.1320 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.64 | 0.7647 | 0.1451 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.65 | 0.7667 | 0.1403 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.19 | 0.7242 | 0.1366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.87 | 0.7827 | 0.1127 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.20 | 0.7576 | 0.1261 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.57 | 0.7701 | 0.1194 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.96 | 0.7712 | 0.1693 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.09 | 0.7704 | 0.1462 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.36 | 0.8059 | 0.1209 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.03 | 0.7951 | 0.1315 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.22 | 0.8026 | 0.1266 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.62 | 0.7920 | 0.1251 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.76 | 0.8318 | 0.0919 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.59 | 0.8163 | 0.1143 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.11 | 0.8249 | 0.1049 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.81 | 0.7882 | 0.1737 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.66 | 0.7439 | 0.1474 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.67 | 0.7833 | 0.1242 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.16 | 0.7690 | 0.1413 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.36 | 0.7772 | 0.1332 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.20 | 0.7442 | 0.1299 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.92 | 0.7721 | 0.1139 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.53 | 0.7627 | 0.1257 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.75 | 0.7690 | 0.1208 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.99 | 0.6014 | 0.0156 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.42 | 0.3535 | 0.1053 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.49 | 0.3685 | 0.1033 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.45 | 0.3680 | 0.1047 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.46 | 0.3697 | 0.1042 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.99 | 0.3550 | 0.0932 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.07 | 0.3901 | 0.0895 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.97 | 0.3698 | 0.0925 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.00 | 0.3785 | 0.0914 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.14 | 0.3264 | 0.0675 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.92 | 0.4076 | 0.0874 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.14 | 0.4475 | 0.0816 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.01 | 0.4313 | 0.0850 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.06 | 0.4389 | 0.0835 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.99 | 0.4259 | 0.0835 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.14 | 0.4909 | 0.0787 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.02 | 0.4568 | 0.0819 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.06 | 0.4720 | 0.0805 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.13 | 0.4018 | 0.0569 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.80 | 0.3472 | 0.1164 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.86 | 0.3749 | 0.1125 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.83 | 0.3650 | 0.1150 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.84 | 0.3708 | 0.1140 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.74 | 0.3467 | 0.1154 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.75 | 0.3699 | 0.1140 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.72 | 0.3597 | 0.1158 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.73 | 0.3646 | 0.1151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.26 | 0.6767 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.67 | 0.6880 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.63 | 0.6901 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.59 | 0.6897 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.41 | 0.6853 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.17 | 0.7147 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.51 | 0.6978 | 0.0160 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.88 | 0.7056 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.95 | 0.6794 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.81 | 0.6766 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.57 | 0.7101 | 0.0159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.25 | 0.6952 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.36 | 0.7025 | 0.0165 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.14 | 0.6933 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.37 | 0.7388 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.62 | 0.7143 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.89 | 0.7249 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.86 | 0.6802 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.96 | 0.6921 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.30 | 0.7120 | 0.0137 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.15 | 0.7055 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 21.21 | 0.7094 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.22 | 0.6995 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.56 | 0.7164 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.37 | 0.7082 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.46 | 0.7120 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.21 | 0.6743 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.63 | 0.6853 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.59 | 0.6877 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.56 | 0.6872 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.37 | 0.6828 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.15 | 0.7134 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.47 | 0.6953 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.84 | 0.7034 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.95 | 0.6777 | 0.0179 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.77 | 0.6739 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.54 | 0.7075 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.22 | 0.6927 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.33 | 0.7002 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.08 | 0.6906 | 0.0169 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.32 | 0.7382 | 0.0144 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.58 | 0.7128 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.84 | 0.7239 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.85 | 0.6767 | 0.0190 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.95 | 0.6905 | 0.0152 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.30 | 0.7115 | 0.0137 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.14 | 0.7044 | 0.0146 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 21.20 | 0.7084 | 0.0143 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.20 | 0.6977 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.56 | 0.7156 | 0.0135 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.37 | 0.7073 | 0.0143 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.45 | 0.7112 | 0.0139 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 27.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.14 | 0.7574 | 0.0232 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.03 | 0.4639 | 0.2180 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.12 | 0.4786 | 0.2104 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.04 | 0.4777 | 0.2150 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.07 | 0.4781 | 0.2129 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.75 | 0.4350 | 0.1930 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.82 | 0.4541 | 0.1845 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.73 | 0.4490 | 0.1900 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.74 | 0.4513 | 0.1880 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.37 | 0.3405 | 0.1612 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.88 | 0.5166 | 0.1863 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.08 | 0.5384 | 0.1732 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.95 | 0.5375 | 0.1812 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.00 | 0.5383 | 0.1777 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.90 | 0.5450 | 0.1764 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.09 | 0.5814 | 0.1627 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.95 | 0.5747 | 0.1707 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.00 | 0.5794 | 0.1673 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.76 | 0.4206 | 0.1421 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.41 | 0.4606 | 0.2217 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.54 | 0.4795 | 0.2132 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.45 | 0.4756 | 0.2186 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.48 | 0.4780 | 0.2162 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.38 | 0.4647 | 0.2152 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.46 | 0.4752 | 0.2093 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.38 | 0.4771 | 0.2134 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.40 | 0.4771 | 0.2117 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.74 | 0.7710 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.25 | 0.7757 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.16 | 0.7755 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.15 | 0.7755 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.02 | 0.7746 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.64 | 0.7840 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.11 | 0.7781 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.41 | 0.7809 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.49 | 0.7682 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.32 | 0.7664 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.07 | 0.7776 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.77 | 0.7738 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.87 | 0.7754 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.63 | 0.7732 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.59 | 0.7879 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.04 | 0.7810 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.24 | 0.7843 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.27 | 0.7645 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.50 | 0.7769 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.84 | 0.7831 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.72 | 0.7811 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.78 | 0.7823 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.73 | 0.7794 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.08 | 0.7852 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.90 | 0.7826 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.98 | 0.7840 | 0.0220 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.34 | 0.7573 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.99 | 0.7643 | 0.0297 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.87 | 0.7658 | 0.0312 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.89 | 0.7654 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.83 | 0.7633 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.33 | 0.7768 | 0.0263 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.94 | 0.7715 | 0.0279 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.18 | 0.7744 | 0.0269 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.45 | 0.7353 | 0.0417 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.00 | 0.7278 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.69 | 0.7434 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.52 | 0.7412 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.53 | 0.7422 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.85 | 0.7484 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.72 | 0.7730 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.45 | 0.7675 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.56 | 0.7713 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.73 | 0.7097 | 0.0478 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.48 | 0.7673 | 0.0325 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.88 | 0.7770 | 0.0303 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.87 | 0.7763 | 0.0313 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.94 | 0.7778 | 0.0307 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.85 | 0.7709 | 0.0288 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.99 | 0.7772 | 0.0288 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.03 | 0.7774 | 0.0281 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.04 | 0.7784 | 0.0282 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 40.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.52 | 0.7161 | 0.0320 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.70 | 0.3634 | 0.3663 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.74 | 0.3714 | 0.3601 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.71 | 0.3708 | 0.3641 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.72 | 0.3713 | 0.3625 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.13 | 0.3478 | 0.3170 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.11 | 0.3584 | 0.3111 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.11 | 0.3550 | 0.3159 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.12 | 0.3561 | 0.3139 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.28 | 0.2713 | 0.2309 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.78 | 0.4096 | 0.3378 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.84 | 0.4233 | 0.3278 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.80 | 0.4222 | 0.3336 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.82 | 0.4233 | 0.3310 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.77 | 0.4396 | 0.3273 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.83 | 0.4595 | 0.3172 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.79 | 0.4548 | 0.3237 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.80 | 0.4573 | 0.3205 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.30 | 0.3517 | 0.2069 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.32 | 0.3495 | 0.3774 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.36 | 0.3622 | 0.3704 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.33 | 0.3586 | 0.3751 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.34 | 0.3609 | 0.3731 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.31 | 0.3573 | 0.3723 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.32 | 0.3633 | 0.3680 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.30 | 0.3618 | 0.3722 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.31 | 0.3625 | 0.3705 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.28 | 0.7254 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.53 | 0.7276 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.54 | 0.7278 | 0.0323 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.50 | 0.7277 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.29 | 0.7268 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.82 | 0.7326 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.39 | 0.7290 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.62 | 0.7306 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.12 | 0.7269 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.85 | 0.7225 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.33 | 0.7287 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.19 | 0.7265 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.23 | 0.7275 | 0.0332 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.07 | 0.7270 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.85 | 0.7359 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.40 | 0.7314 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.58 | 0.7337 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.95 | 0.7255 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.74 | 0.7280 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.95 | 0.7317 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.87 | 0.7305 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.91 | 0.7313 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.80 | 0.7294 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.05 | 0.7330 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.93 | 0.7314 | 0.0302 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.00 | 0.7323 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.59 | 0.7193 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.08 | 0.7236 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.00 | 0.7240 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.01 | 0.7241 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.82 | 0.7235 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.49 | 0.7319 | 0.0334 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.98 | 0.7278 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.23 | 0.7296 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.76 | 0.7227 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.13 | 0.6992 | 0.0454 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.76 | 0.7108 | 0.0403 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.57 | 0.7078 | 0.0429 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.61 | 0.7097 | 0.0417 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.09 | 0.7185 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.10 | 0.7331 | 0.0332 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.60 | 0.7280 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.77 | 0.7308 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.11 | 0.7125 | 0.0405 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.41 | 0.7251 | 0.0359 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.77 | 0.7320 | 0.0339 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.65 | 0.7300 | 0.0353 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.71 | 0.7313 | 0.0347 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.59 | 0.7282 | 0.0334 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.91 | 0.7328 | 0.0316 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.73 | 0.7311 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.82 | 0.7321 | 0.0325 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.70 | 0.7061 | 0.0360 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.30 | 0.2731 | 0.3930 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.32 | 0.2746 | 0.3886 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.30 | 0.2754 | 0.3913 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.31 | 0.2753 | 0.3900 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.60 | 0.2223 | 0.3594 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.58 | 0.2220 | 0.3559 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.60 | 0.2236 | 0.3584 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.60 | 0.2226 | 0.3573 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.66 | 0.1177 | 0.2854 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.97 | 0.3154 | 0.3669 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.01 | 0.3182 | 0.3597 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 2.99 | 0.3199 | 0.3640 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 2.99 | 0.3193 | 0.3622 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 2.94 | 0.3234 | 0.3615 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 2.96 | 0.3250 | 0.3542 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.94 | 0.3277 | 0.3589 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 2.95 | 0.3264 | 0.3567 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.02 | 0.1817 | 0.2672 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.10 | 0.2592 | 0.4010 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.13 | 0.2620 | 0.3970 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.11 | 0.2616 | 0.3995 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.12 | 0.2620 | 0.3982 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.11 | 0.2626 | 0.3986 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.12 | 0.2624 | 0.3957 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.10 | 0.2633 | 0.3981 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.11 | 0.2628 | 0.3970 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.70 | 0.7060 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.70 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.70 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.70 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.70 | 0.7060 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.70 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.70 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.70 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.71 | 0.7063 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.68 | 0.7060 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.68 | 0.7061 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.69 | 0.7061 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.68 | 0.7061 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.70 | 0.7062 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7063 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.71 | 0.7063 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.71 | 0.7063 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.71 | 0.7064 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.70 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.70 | 0.7062 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.70 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.70 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.70 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.70 | 0.7062 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.70 | 0.7061 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.70 | 0.7062 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.51 | 0.7054 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.62 | 0.7061 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.59 | 0.7061 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.61 | 0.7062 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.64 | 0.7062 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.65 | 0.7064 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.65 | 0.7066 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.66 | 0.7065 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.66 | 0.7065 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.00 | 0.7018 | 0.0429 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.25 | 0.7036 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.18 | 0.7034 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.22 | 0.7037 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.47 | 0.7060 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.58 | 0.7066 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.53 | 0.7069 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.54 | 0.7068 | 0.0388 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.58 | 0.7062 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.59 | 0.7057 | 0.0374 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.64 | 0.7063 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.63 | 0.7062 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.64 | 0.7063 | 0.0373 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.67 | 0.7063 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.68 | 0.7064 | 0.0367 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.66 | 0.7064 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.66 | 0.7064 | 0.0369 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.69 | 0.7108 | 0.0550 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.84 | 0.3047 | 0.4611 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.87 | 0.3089 | 0.4523 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.85 | 0.3091 | 0.4580 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.85 | 0.3092 | 0.4552 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.99 | 0.2626 | 0.4290 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.98 | 0.2671 | 0.4216 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.99 | 0.2663 | 0.4272 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.99 | 0.2664 | 0.4247 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.82 | 0.1732 | 0.3849 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.63 | 0.3487 | 0.4303 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.67 | 0.3561 | 0.4148 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.64 | 0.3563 | 0.4241 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.65 | 0.3564 | 0.4198 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.60 | 0.3648 | 0.4148 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.62 | 0.3752 | 0.3999 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.60 | 0.3741 | 0.4094 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.61 | 0.3749 | 0.4046 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.37 | 0.2426 | 0.3495 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.57 | 0.2889 | 0.4732 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.60 | 0.2954 | 0.4636 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.58 | 0.2938 | 0.4699 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.59 | 0.2948 | 0.4671 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.57 | 0.2934 | 0.4646 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.58 | 0.2958 | 0.4586 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.56 | 0.2957 | 0.4636 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.57 | 0.2957 | 0.4613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.99 | 0.7152 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.21 | 0.7165 | 0.0563 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.16 | 0.7165 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.17 | 0.7165 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.08 | 0.7160 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.38 | 0.7191 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.15 | 0.7172 | 0.0557 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.27 | 0.7180 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.98 | 0.7163 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.77 | 0.7141 | 0.0600 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.11 | 0.7172 | 0.0573 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.98 | 0.7161 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.03 | 0.7166 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.97 | 0.7165 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.44 | 0.7209 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.19 | 0.7188 | 0.0557 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.29 | 0.7199 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.90 | 0.7160 | 0.0585 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.26 | 0.7164 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.39 | 0.7181 | 0.0545 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.34 | 0.7175 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.36 | 0.7179 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.40 | 0.7175 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.52 | 0.7192 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.46 | 0.7184 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.49 | 0.7188 | 0.0540 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.58 | 0.7124 | 0.0649 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.95 | 0.7149 | 0.0618 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.86 | 0.7149 | 0.0635 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.89 | 0.7151 | 0.0627 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.81 | 0.7149 | 0.0617 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.18 | 0.7191 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.93 | 0.7172 | 0.0609 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.06 | 0.7180 | 0.0597 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.67 | 0.7148 | 0.0624 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.61 | 0.7025 | 0.0731 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.09 | 0.7082 | 0.0670 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.94 | 0.7067 | 0.0701 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.98 | 0.7076 | 0.0686 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.36 | 0.7127 | 0.0658 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.99 | 0.7198 | 0.0591 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.71 | 0.7176 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.81 | 0.7189 | 0.0609 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.30 | 0.7106 | 0.0661 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.06 | 0.7151 | 0.0609 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.28 | 0.7184 | 0.0586 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.20 | 0.7174 | 0.0601 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.24 | 0.7180 | 0.0595 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.29 | 0.7174 | 0.0586 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.45 | 0.7195 | 0.0564 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.35 | 0.7187 | 0.0580 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.39 | 0.7191 | 0.0573 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 257077 | 0.329 | 63.7 | 29.17 | 0.21 | 0.042 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 257077 | 0.329 | 54.3 | 29.17 | 0.21 | 0.042 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 257077 | 0.329 | 65.2 | 29.17 | 0.21 | 0.042 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 257077 | 0.329 | 58.9 | 29.17 | 0.21 | 0.042 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 653 | None | classic | 0.31 | False | 368286 | 0.984 | 170.1 | 29.95 | 0.30 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 653 | None | classic | 0.31 | False | 368286 | 0.984 | 198.4 | 29.95 | 0.30 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 653 | None | classic | 0.31 | False | 368286 | 0.984 | 173.0 | 29.95 | 0.30 | 0.011 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 653 | None | classic | 0.31 | False | 368286 | 0.984 | 186.3 | 29.95 | 0.30 | 0.011 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1098582 | 0.789 | 463.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 265091 | 0.329 | 57.4 | 29.03 | 0.24 | 0.036 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 265091 | 0.329 | 78.6 | 29.03 | 0.24 | 0.036 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 265091 | 0.329 | 73.4 | 29.03 | 0.24 | 0.036 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 265091 | 0.329 | 70.7 | 29.03 | 0.24 | 0.036 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 850 | None | classic | 0.50 | False | 479831 | 0.990 | 206.0 | 32.11 | 0.13 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 850 | None | classic | 0.50 | False | 479831 | 0.990 | 211.8 | 32.11 | 0.13 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 850 | None | classic | 0.50 | False | 479831 | 0.990 | 233.9 | 32.11 | 0.13 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 850 | None | classic | 0.50 | False | 479831 | 0.990 | 206.2 | 32.11 | 0.13 | 0.008 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1505588 | 0.789 | 105.2 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 245655 | 0.920 | 81.7 | 29.72 | 0.10 | 0.040 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 245655 | 0.920 | 74.9 | 29.72 | 0.10 | 0.040 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 245655 | 0.920 | 85.4 | 29.72 | 0.10 | 0.040 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 245655 | 0.920 | 68.7 | 29.72 | 0.10 | 0.040 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 659 | None | classic | 0.55 | False | 373911 | 0.984 | 159.6 | 27.81 | 0.29 | 0.006 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 659 | None | classic | 0.55 | False | 373911 | 0.984 | 177.6 | 27.81 | 0.29 | 0.006 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 659 | None | classic | 0.55 | False | 373911 | 0.984 | 187.7 | 27.81 | 0.29 | 0.006 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 659 | None | classic | 0.55 | False | 373911 | 0.984 | 185.5 | 27.81 | 0.29 | 0.006 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.736 | 0.021 |
| in035 | mask_ent | 0.708 | 0.021 |
| in035 | mask_grad | 0.472 | 0.021 |
| in035 | r_col | 0.770 | 0.021 |
| in035 | r_warp | 0.874 | 0.021 |

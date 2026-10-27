# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 11.0% | 24.93 / 0.0105 | 19.27 / 0.0362 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.3% | 24.88 / 0.0108 | 19.77 / 0.0300 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.1% | 24.87 / 0.0108 | 19.71 / 0.0324 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.1% | 24.86 / 0.0108 | 19.65 / 0.0308 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.7% | 24.85 / 0.0103 | 21.20 / 0.0220 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.9% | 24.81 / 0.0107 | 21.23 / 0.0187 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.7% | 24.80 / 0.0105 | 21.41 / 0.0185 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 10.7% | 24.81 / 0.0105 | 21.31 / 0.0184 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 9.9% | 24.24 / 0.0105 | 21.27 / 0.0298 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 9.3% | 24.30 / 0.0104 | 21.01 / 0.0363 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.7% | 21.01 / 0.0065 | 16.97 / 0.0213 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 9.3% | 24.34 / 0.0104 | 21.01 / 0.0388 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 3.0% | 20.95 / 0.0065 | 17.33 / 0.0217 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 9.9% | 24.28 / 0.0105 | 21.46 / 0.0201 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 9.1% | 24.30 / 0.0104 | 20.90 / 0.0358 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 3.1% | 21.66 / 0.0069 | 17.40 / 0.0237 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 9.2% | 24.35 / 0.0105 | 20.57 / 0.0375 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 3.6% | 21.56 / 0.0074 | 17.37 / 0.0288 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 11.3% | 24.85 / 0.0110 | 19.44 / 0.0469 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 16.3% | 25.22 / 0.0131 | 19.19 / 0.0448 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 16.8% | 25.24 / 0.0137 | 19.82 / 0.0376 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 16.6% | 25.23 / 0.0133 | 19.77 / 0.0412 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 16.6% | 25.24 / 0.0134 | 19.73 / 0.0389 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 15.6% | 25.11 / 0.0130 | 21.35 / 0.0313 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 16.0% | 25.14 / 0.0130 | 20.85 / 0.0257 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 15.7% | 25.13 / 0.0128 | 21.25 / 0.0263 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 15.8% | 25.12 / 0.0129 | 20.89 / 0.0257 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 15.9% | 25.14 / 0.0138 | 20.02 / 0.0526 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 9.5% | 24.34 / 0.0115 | 19.14 / 0.0390 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 10.8% | 24.72 / 0.0118 | 19.86 / 0.0381 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 9.8% | 24.42 / 0.0114 | 19.80 / 0.0366 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 10.1% | 24.50 / 0.0115 | 19.82 / 0.0365 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 9.8% | 24.45 / 0.0109 | 22.08 / 0.0273 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 10.7% | 24.74 / 0.0109 | 21.23 / 0.0292 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 10.0% | 24.52 / 0.0111 | 21.76 / 0.0270 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 10.2% | 24.60 / 0.0109 | 21.45 / 0.0280 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.10 / 0.0441 | 24.95 / 0.0606 | 20.19 / 0.0111 | 30.11 / 0.0281 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.50 / 0.0602 | 23.29 / 0.1231 | 18.59 / 0.0168 | 29.60 / 0.0319 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.72 / 0.0572 | 23.44 / 0.1148 | 18.71 / 0.0163 | 29.53 / 0.0309 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.76 / 0.0586 | 23.71 / 0.1182 | 18.69 / 0.0165 | 29.70 / 0.0312 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.71 / 0.0578 | 23.55 / 0.1143 | 18.64 / 0.0165 | 29.62 / 0.0310 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.38 / 0.0509 | 24.40 / 0.0938 | 19.61 / 0.0127 | 30.00 / 0.0296 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.38 / 0.0485 | 23.79 / 0.0786 | 19.36 / 0.0122 | 30.03 / 0.0291 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.45 / 0.0491 | 24.07 / 0.0852 | 19.48 / 0.0120 | 30.07 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.42 / 0.0485 | 23.94 / 0.0795 | 19.39 / 0.0121 | 30.06 / 0.0291 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.42 / 0.0539 | 22.88 / 0.1358 | 19.03 / 0.0181 | 30.15 / 0.0281 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.55 / 0.0543 | 25.03 / 0.1052 | 20.14 / 0.0159 | 30.04 / 0.0284 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.61 / 0.0501 | 25.25 / 0.0870 | 20.08 / 0.0146 | 30.01 / 0.0283 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.40 / 0.0560 | 24.83 / 0.1128 | 19.91 / 0.0168 | 30.04 / 0.0284 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.49 / 0.0518 | 25.04 / 0.0960 | 19.93 / 0.0154 | 30.02 / 0.0282 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.49 / 0.0498 | 23.17 / 0.1049 | 19.22 / 0.0147 | 30.13 / 0.0283 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.48 / 0.0531 | 24.88 / 0.1103 | 20.09 / 0.0155 | 29.98 / 0.0286 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.55 / 0.0493 | 25.18 / 0.0868 | 20.09 / 0.0143 | 29.96 / 0.0283 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.23 / 0.0543 | 24.34 / 0.1141 | 19.67 / 0.0162 | 29.98 / 0.0286 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.31 / 0.0510 | 24.51 / 0.0975 | 19.70 / 0.0153 | 29.97 / 0.0283 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.32 / 0.0538 | 24.51 / 0.1075 | 19.56 / 0.0165 | 29.98 / 0.0288 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.54 / 0.0690 | 22.38 / 0.1388 | 17.95 / 0.0191 | 29.08 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.93 / 0.0632 | 22.98 / 0.1241 | 18.45 / 0.0174 | 29.20 / 0.0333 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.92 / 0.0662 | 22.97 / 0.1296 | 18.28 / 0.0181 | 29.23 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.91 / 0.0644 | 22.97 / 0.1256 | 18.30 / 0.0177 | 29.22 / 0.0335 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.90 / 0.0580 | 23.73 / 0.1084 | 19.39 / 0.0146 | 29.79 / 0.0311 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.47 / 0.0537 | 22.73 / 0.0993 | 18.91 / 0.0137 | 29.39 / 0.0317 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.78 / 0.0549 | 23.15 / 0.1012 | 19.18 / 0.0136 | 29.69 / 0.0313 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.54 / 0.0537 | 22.87 / 0.0971 | 18.95 / 0.0136 | 29.50 / 0.0315 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.76 / 0.0570 | 24.35 / 0.1146 | 19.11 / 0.0181 | 29.86 / 0.0298 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.88 / 0.0603 | 23.87 / 0.1274 | 18.83 / 0.0151 | 29.91 / 0.0300 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.20 / 0.0566 | 24.21 / 0.1098 | 19.25 / 0.0140 | 29.89 / 0.0300 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.11 / 0.0584 | 24.29 / 0.1165 | 19.11 / 0.0143 | 29.93 / 0.0298 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.14 / 0.0576 | 24.25 / 0.1110 | 19.17 / 0.0140 | 29.92 / 0.0299 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.75 / 0.0531 | 24.67 / 0.0971 | 20.04 / 0.0121 | 30.10 / 0.0289 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.59 / 0.0505 | 24.25 / 0.0838 | 19.80 / 0.0124 | 29.91 / 0.0292 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.70 / 0.0516 | 24.47 / 0.0853 | 19.85 / 0.0123 | 30.05 / 0.0290 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.60 / 0.0508 | 24.33 / 0.0827 | 19.77 / 0.0125 | 29.96 / 0.0291 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.0%） | — | — | 28.10 / 0.0441 | 24.95 / 0.0606 | 30.11 |
| in035 | rife | 5.2% | 9.5% | 26.88 / 0.0603 | 23.87 / 0.1274 | 29.91 |
| in035 | cnw_cnn | 6.4% | 11.0% | 26.50 / 0.0602 | 23.29 / 0.1231 | 29.60 |
| in035 | cnw_f5 | 9.5% | 16.3% | 25.54 / 0.0690 | 22.38 / 0.1388 | 29.08 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.13 / 0.0444 | -1.00 / +0.0205 (core 6.3%) | -1.24 / +0.0180 (core 6.7%) | -2.26 / +0.0293 (core 10.6%) |
| in035 | 2 | 0-3 | 27.91 / 0.0425 | -1.78 / +0.0226 (core 6.3%) | -1.85 / +0.0189 (core 6.7%) | -2.98 / +0.0316 (core 10.6%) |
| in035 | 4 | 3-5 | 29.26 / 0.0453 | -0.88 / +0.0057 (core 1.8%) | -1.72 / +0.0113 (core 3.7%) | -2.44 / +0.0139 (core 5.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.10 / 0.0441 | 24.95 | 30.11 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.50 / 0.0602 | 23.29 | 29.60 | 0/3 |
| in035 | cnw_cnn | oracle | 2.1% | 27.29 / 0.0501 | 24.13 | 30.10 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.72 / 0.0572 | 23.44 | 29.53 | 0/3 |
| in035 | cnw_cnn | oracle | 2.1% | 27.42 / 0.0491 | 24.41 | 30.09 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.76 / 0.0586 | 23.71 | 29.70 | 0/3 |
| in035 | cnw_cnn | oracle | 2.1% | 27.39 / 0.0497 | 24.48 | 30.10 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.71 / 0.0578 | 23.55 | 29.62 | 0/3 |
| in035 | cnw_cnn | oracle | 2.1% | 27.37 / 0.0494 | 24.42 | 30.09 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.38 / 0.0509 | 24.40 | 30.00 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 27.73 / 0.0459 | 24.68 | 30.11 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.38 / 0.0485 | 23.79 | 30.03 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 27.69 / 0.0451 | 24.21 | 30.11 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.45 / 0.0491 | 24.07 | 30.07 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 27.72 / 0.0450 | 24.36 | 30.11 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.42 / 0.0485 | 23.94 | 30.06 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 27.70 / 0.0450 | 24.28 | 30.11 | 0/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 27.42 / 0.0539 | 22.88 | 30.15 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 2.1% | 27.55 / 0.0513 | 23.24 | 30.12 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 27.55 / 0.0543 | 25.03 | 30.04 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 1.9% | 27.94 / 0.0492 | 25.53 | 30.12 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 27.61 / 0.0501 | 25.25 | 30.01 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 1.1% | 27.93 / 0.0477 | 25.50 | 30.11 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.40 / 0.0560 | 24.83 | 30.04 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 1.9% | 27.81 / 0.0503 | 25.37 | 30.12 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.49 / 0.0518 | 25.04 | 30.02 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 1.2% | 27.83 / 0.0487 | 25.36 | 30.11 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.49 / 0.0498 | 23.17 | 30.13 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 2.1% | 27.64 / 0.0475 | 23.51 | 30.12 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.48 / 0.0531 | 24.88 | 29.98 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.9% | 27.93 / 0.0484 | 25.50 | 30.12 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.55 / 0.0493 | 25.18 | 29.96 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.2% | 27.94 / 0.0472 | 25.59 | 30.11 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.23 / 0.0543 | 24.34 | 29.98 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 1.9% | 27.70 / 0.0492 | 24.93 | 30.12 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.31 / 0.0510 | 24.51 | 29.97 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 1.3% | 27.72 / 0.0482 | 24.97 | 30.11 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.32 / 0.0538 | 24.51 | 29.98 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.1% | 27.73 / 0.0488 | 24.83 | 30.12 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.54 / 0.0690 | 22.38 | 29.08 | 0/3 |
| in035 | cnw_f5 | oracle | 2.9% | 26.82 / 0.0534 | 23.47 | 30.05 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.93 / 0.0632 | 22.98 | 29.20 | 0/3 |
| in035 | cnw_f5 | oracle | 2.9% | 27.18 / 0.0507 | 24.20 | 30.08 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.92 / 0.0662 | 22.97 | 29.23 | 0/3 |
| in035 | cnw_f5 | oracle | 2.9% | 27.07 / 0.0522 | 23.95 | 30.07 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.91 / 0.0644 | 22.97 | 29.22 | 0/3 |
| in035 | cnw_f5 | oracle | 2.9% | 27.09 / 0.0514 | 24.03 | 30.07 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.90 / 0.0580 | 23.73 | 29.79 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.9% | 27.56 / 0.0483 | 24.25 | 30.10 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.47 / 0.0537 | 22.73 | 29.39 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.9% | 27.40 / 0.0465 | 23.63 | 30.08 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.78 / 0.0549 | 23.15 | 29.69 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.8% | 27.51 / 0.0469 | 23.77 | 30.09 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.54 / 0.0537 | 22.87 | 29.50 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.9% | 27.41 / 0.0465 | 23.63 | 30.08 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.76 / 0.0570 | 24.35 | 29.86 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.9% | 27.41 / 0.0501 | 24.74 | 30.11 | 0/3 |
| in035 | rife | 不复核 | —% | 26.88 / 0.0603 | 23.87 | 29.91 | 0/3 |
| in035 | rife | oracle | 1.9% | 27.42 / 0.0491 | 24.19 | 30.10 | 0/3 |
| in035 | rife | 不复核 | —% | 27.20 / 0.0566 | 24.21 | 29.89 | 0/3 |
| in035 | rife | oracle | 2.0% | 27.66 / 0.0477 | 24.64 | 30.10 | 0/3 |
| in035 | rife | 不复核 | —% | 27.11 / 0.0584 | 24.29 | 29.93 | 0/3 |
| in035 | rife | oracle | 1.9% | 27.60 / 0.0482 | 24.57 | 30.10 | 0/3 |
| in035 | rife | 不复核 | —% | 27.14 / 0.0576 | 24.25 | 29.92 | 0/3 |
| in035 | rife | oracle | 1.9% | 27.63 / 0.0479 | 24.59 | 30.10 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.75 / 0.0531 | 24.67 | 30.10 | 0/3 |
| in035 | rife_mw | oracle | 1.9% | 27.94 / 0.0458 | 24.84 | 30.11 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.59 / 0.0505 | 24.25 | 29.91 | 0/3 |
| in035 | rife_mw | oracle | 1.9% | 27.88 / 0.0451 | 24.54 | 30.10 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.70 / 0.0516 | 24.47 | 30.05 | 0/3 |
| in035 | rife_mw | oracle | 1.9% | 27.90 / 0.0455 | 24.60 | 30.11 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.60 / 0.0508 | 24.33 | 29.96 | 0/3 |
| in035 | rife_mw | oracle | 1.9% | 27.86 / 0.0453 | 24.54 | 30.10 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.10 / 0.0441 | 24.95 / 0.0606 | — |
| in035 | FF | 0（前馈） | 1008×635（59%） | 25.93 | 26.50 / 0.0602 | 23.29 / 0.1231 | 0/3 |
| in035 | 25 | 0.54 s | 1008×635（59%） | 26.64 | 26.76 / 0.0586 | 23.71 / 0.1182 | 0/3 |
| in035 | 50 | 1.06 s | 1008×635（59%） | 27.02 | 26.71 / 0.0578 | 23.55 / 0.1143 | 0/3 |
| in035 | 100 | 2.09 s | 1008×635（59%） | 27.46 | 26.72 / 0.0572 | 23.44 / 0.1148 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.10 / 0.0441 | 24.95 / 0.0606 | 30.11 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.50 / 0.0602 | 23.29 / 0.1231 | 29.60 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.29 / 0.0501 | 24.13 / 0.0937 | 30.10 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 26.76 / 0.0586 | 23.71 / 0.1182 | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.39 / 0.0497 | 24.48 / 0.0868 | 30.10 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 26.71 / 0.0578 | 23.55 / 0.1143 | 29.62 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.37 / 0.0494 | 24.42 / 0.0840 | 30.09 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 26.72 / 0.0572 | 23.44 / 0.1148 | 29.53 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.42 / 0.0491 | 24.41 / 0.0838 | 30.09 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.38 / 0.0509 | 24.40 / 0.0938 | 30.00 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.73 / 0.0459 | 24.68 / 0.0729 | 30.11 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.45 / 0.0491 | 24.07 / 0.0852 | 30.07 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.72 / 0.0450 | 24.36 / 0.0670 | 30.11 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.42 / 0.0485 | 23.94 / 0.0795 | 30.06 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.70 / 0.0450 | 24.28 / 0.0638 | 30.11 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.38 / 0.0485 | 23.79 / 0.0786 | 30.03 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.69 / 0.0451 | 24.21 / 0.0641 | 30.11 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 25.54 / 0.0690 | 22.38 / 0.1388 | 29.08 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 26.82 / 0.0534 | 23.47 / 0.0945 | 30.05 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 25.92 / 0.0662 | 22.97 / 0.1296 | 29.23 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.07 / 0.0522 | 23.95 / 0.0877 | 30.07 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 25.91 / 0.0644 | 22.97 / 0.1256 | 29.22 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.09 / 0.0514 | 24.03 / 0.0849 | 30.07 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 25.93 / 0.0632 | 22.98 / 0.1241 | 29.20 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.18 / 0.0507 | 24.20 / 0.0842 | 30.08 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.90 / 0.0580 | 23.73 / 0.1084 | 29.79 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.56 / 0.0483 | 24.25 / 0.0758 | 30.10 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.78 / 0.0549 | 23.15 / 0.1012 | 29.69 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.51 / 0.0469 | 23.77 / 0.0727 | 30.09 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.54 / 0.0537 | 22.87 / 0.0971 | 29.50 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.41 / 0.0465 | 23.63 / 0.0695 | 30.08 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 26.47 / 0.0537 | 22.73 / 0.0993 | 29.39 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.40 / 0.0465 | 23.63 / 0.0704 | 30.08 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.88 / 0.0603 | 23.87 / 0.1274 | 29.91 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.42 / 0.0491 | 24.19 / 0.0877 | 30.10 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.11 / 0.0584 | 24.29 / 0.1165 | 29.93 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.60 / 0.0482 | 24.57 / 0.0806 | 30.10 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.14 / 0.0576 | 24.25 / 0.1110 | 29.92 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.63 / 0.0479 | 24.59 / 0.0777 | 30.10 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.20 / 0.0566 | 24.21 / 0.1098 | 29.89 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.66 / 0.0477 | 24.64 / 0.0780 | 30.10 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.75 / 0.0531 | 24.67 / 0.0971 | 30.10 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.94 / 0.0458 | 24.84 / 0.0702 | 30.11 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.70 / 0.0516 | 24.47 / 0.0853 | 30.05 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.90 / 0.0455 | 24.60 / 0.0663 | 30.11 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.60 / 0.0508 | 24.33 / 0.0827 | 29.96 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.86 / 0.0453 | 24.54 / 0.0652 | 30.10 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.59 / 0.0505 | 24.25 / 0.0838 | 29.91 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.88 / 0.0451 | 24.54 / 0.0655 | 30.10 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.95 / 0.0606 | 20.19 / 0.0111 | 30.11 / 0.0281 | 28.10 / 0.0441 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 8.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.95 | 0.6827 | 0.0606 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 22.20 | 0.6371 | 0.2076 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 22.10 | 0.6232 | 0.1784 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 22.68 | 0.6519 | 0.1923 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 22.35 | 0.6389 | 0.1823 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 24.08 | 0.6999 | 0.1397 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 22.99 | 0.6638 | 0.1102 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 23.52 | 0.6933 | 0.1229 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 23.29 | 0.6797 | 0.1117 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 22.99 | 0.6676 | 0.1416 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 25.01 | 0.6933 | 0.1326 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 25.01 | 0.6933 | 0.1326 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 24.80 | 0.6904 | 0.1375 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 24.80 | 0.6904 | 0.1375 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 23.17 | 0.6763 | 0.1195 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 24.64 | 0.6947 | 0.1437 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 24.64 | 0.6947 | 0.1437 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 24.02 | 0.6838 | 0.1522 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 24.02 | 0.6838 | 0.1522 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 24.44 | 0.6843 | 0.1387 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 21.48 | 0.6254 | 0.2204 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 22.04 | 0.6201 | 0.1902 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 22.24 | 0.6420 | 0.2022 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 22.10 | 0.6330 | 0.1974 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 23.15 | 0.6774 | 0.1576 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 21.88 | 0.6320 | 0.1360 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 22.52 | 0.6733 | 0.1383 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 22.10 | 0.6522 | 0.1334 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 24.02 | 0.6826 | 0.1508 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 16.93 | 0.5977 | 0.2784 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 17.60 | 0.5945 | 0.2403 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 17.48 | 0.6137 | 0.2570 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 17.52 | 0.6057 | 0.2473 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 17.47 | 0.6330 | 0.2228 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 16.86 | 0.5967 | 0.2027 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 17.22 | 0.6308 | 0.2062 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 16.95 | 0.6129 | 0.2023 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.13 | 0.6691 | 0.0937 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.41 | 0.6792 | 0.0838 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.48 | 0.6790 | 0.0868 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.42 | 0.6793 | 0.0840 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.68 | 0.6885 | 0.0729 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.21 | 0.6798 | 0.0641 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.36 | 0.6853 | 0.0670 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.28 | 0.6829 | 0.0638 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.24 | 0.6634 | 0.1209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.53 | 0.6948 | 0.0844 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.50 | 0.6902 | 0.0777 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.37 | 0.6934 | 0.0911 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.36 | 0.6903 | 0.0841 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.51 | 0.6668 | 0.0917 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.50 | 0.6955 | 0.0878 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.59 | 0.6927 | 0.0775 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.93 | 0.6880 | 0.0920 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.97 | 0.6845 | 0.0856 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.83 | 0.6874 | 0.0880 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 23.47 | 0.6611 | 0.0945 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.20 | 0.6714 | 0.0842 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.95 | 0.6702 | 0.0877 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.03 | 0.6703 | 0.0849 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.25 | 0.6789 | 0.0758 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.63 | 0.6642 | 0.0704 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.77 | 0.6742 | 0.0727 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.63 | 0.6694 | 0.0695 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.74 | 0.6839 | 0.0899 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.19 | 0.6727 | 0.0877 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.64 | 0.6818 | 0.0780 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.57 | 0.6800 | 0.0806 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.59 | 0.6809 | 0.0777 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 24.84 | 0.6848 | 0.0702 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.54 | 0.6765 | 0.0655 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.60 | 0.6825 | 0.0663 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.54 | 0.6795 | 0.0652 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.29 | 0.6561 | 0.1231 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.44 | 0.6567 | 0.1148 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.71 | 0.6668 | 0.1182 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.55 | 0.6622 | 0.1143 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.40 | 0.6919 | 0.0938 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.79 | 0.6726 | 0.0786 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.07 | 0.6866 | 0.0852 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.94 | 0.6806 | 0.0795 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.88 | 0.6598 | 0.1358 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.03 | 0.6892 | 0.1052 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.25 | 0.6880 | 0.0870 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.83 | 0.6870 | 0.1128 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.04 | 0.6871 | 0.0960 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.17 | 0.6676 | 0.1049 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.88 | 0.6921 | 0.1103 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.18 | 0.6895 | 0.0868 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.34 | 0.6845 | 0.1141 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.51 | 0.6808 | 0.0975 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.51 | 0.6857 | 0.1075 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.38 | 0.6404 | 0.1388 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.98 | 0.6392 | 0.1241 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.97 | 0.6505 | 0.1296 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.97 | 0.6456 | 0.1256 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.73 | 0.6788 | 0.1084 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.73 | 0.6458 | 0.0993 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.15 | 0.6712 | 0.1012 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.87 | 0.6583 | 0.0971 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.35 | 0.6801 | 0.1146 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.87 | 0.6746 | 0.1274 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.21 | 0.6742 | 0.1098 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.29 | 0.6840 | 0.1165 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.25 | 0.6800 | 0.1110 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.67 | 0.6917 | 0.0971 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.25 | 0.6747 | 0.0838 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.47 | 0.6913 | 0.0853 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.33 | 0.6831 | 0.0827 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.19 | 0.6599 | 0.0111 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.71 | 0.2707 | 0.0791 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.81 | 0.2968 | 0.0768 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.75 | 0.2904 | 0.0781 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.76 | 0.2937 | 0.0778 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.48 | 0.3522 | 0.0660 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.51 | 0.3522 | 0.0641 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.49 | 0.3601 | 0.0643 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.49 | 0.3555 | 0.0642 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.78 | 0.3704 | 0.0386 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 14.97 | 0.4064 | 0.0383 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 14.97 | 0.4064 | 0.0383 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.85 | 0.3916 | 0.0392 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.85 | 0.3916 | 0.0392 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.40 | 0.3205 | 0.0448 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.52 | 0.3524 | 0.0473 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.52 | 0.3524 | 0.0473 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.39 | 0.3297 | 0.0481 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.39 | 0.3297 | 0.0481 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.32 | 0.3124 | 0.0487 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.83 | 0.3460 | 0.0647 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.99 | 0.3868 | 0.0609 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.93 | 0.3741 | 0.0626 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.94 | 0.3791 | 0.0618 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.00 | 0.4450 | 0.0593 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.03 | 0.4539 | 0.0560 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.01 | 0.4628 | 0.0568 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.00 | 0.4555 | 0.0567 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.91 | 0.4040 | 0.0407 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.23 | 0.2652 | 0.0915 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.37 | 0.2943 | 0.0881 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.29 | 0.2853 | 0.0898 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.32 | 0.2895 | 0.0890 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.23 | 0.3323 | 0.0889 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.25 | 0.3118 | 0.0879 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.19 | 0.3235 | 0.0888 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.20 | 0.3151 | 0.0885 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.61 | 0.6026 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.72 | 0.6180 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.71 | 0.6148 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.66 | 0.6156 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.62 | 0.6668 | 0.0126 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.38 | 0.6586 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.48 | 0.6686 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.40 | 0.6639 | 0.0120 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.03 | 0.6286 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.16 | 0.6709 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.10 | 0.6635 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.92 | 0.6621 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.95 | 0.6591 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.21 | 0.6305 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.10 | 0.6698 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.11 | 0.6640 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.68 | 0.6516 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.71 | 0.6481 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.56 | 0.6434 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 17.97 | 0.5725 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.47 | 0.6009 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.30 | 0.5911 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.31 | 0.5939 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.40 | 0.6423 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 18.93 | 0.6388 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.19 | 0.6488 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 18.96 | 0.6418 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.12 | 0.6196 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.84 | 0.6263 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.25 | 0.6373 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.12 | 0.6354 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.18 | 0.6360 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.05 | 0.6776 | 0.0121 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.81 | 0.6657 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.86 | 0.6736 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.77 | 0.6689 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.59 | 0.5993 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.71 | 0.6160 | 0.0163 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.69 | 0.6127 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.64 | 0.6136 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.61 | 0.6652 | 0.0127 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.36 | 0.6575 | 0.0122 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.48 | 0.6677 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.39 | 0.6630 | 0.0121 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.03 | 0.6279 | 0.0181 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.14 | 0.6693 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.08 | 0.6624 | 0.0146 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.91 | 0.6613 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.93 | 0.6589 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.22 | 0.6294 | 0.0147 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.09 | 0.6678 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.09 | 0.6623 | 0.0143 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.67 | 0.6503 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.70 | 0.6473 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.56 | 0.6404 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 17.95 | 0.5689 | 0.0191 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.45 | 0.5984 | 0.0174 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.28 | 0.5885 | 0.0181 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.30 | 0.5913 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.39 | 0.6396 | 0.0146 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 18.91 | 0.6364 | 0.0137 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.18 | 0.6467 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 18.95 | 0.6397 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.11 | 0.6158 | 0.0181 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.83 | 0.6250 | 0.0151 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.25 | 0.6363 | 0.0140 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.11 | 0.6344 | 0.0143 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.17 | 0.6352 | 0.0140 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.04 | 0.6762 | 0.0121 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.80 | 0.6648 | 0.0124 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.85 | 0.6730 | 0.0123 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.77 | 0.6682 | 0.0125 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 36.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.64 | 0.7705 | 0.0198 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.95 | 0.4462 | 0.2237 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.08 | 0.4543 | 0.2132 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.99 | 0.4625 | 0.2184 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.01 | 0.4583 | 0.2162 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.91 | 0.4709 | 0.1922 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.02 | 0.4675 | 0.1862 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.95 | 0.4821 | 0.1884 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.96 | 0.4748 | 0.1875 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.08 | 0.5871 | 0.1089 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.65 | 0.5651 | 0.1277 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.65 | 0.5651 | 0.1277 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.55 | 0.5519 | 0.1318 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.55 | 0.5519 | 0.1318 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.32 | 0.4495 | 0.1429 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.99 | 0.4024 | 0.1690 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.99 | 0.4024 | 0.1690 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.94 | 0.3915 | 0.1710 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.94 | 0.3915 | 0.1710 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.64 | 0.3431 | 0.1790 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.17 | 0.4806 | 0.2071 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.37 | 0.4981 | 0.1922 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.24 | 0.5025 | 0.2006 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.29 | 0.5007 | 0.1968 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.21 | 0.5448 | 0.1899 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.45 | 0.5495 | 0.1773 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.28 | 0.5607 | 0.1830 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.33 | 0.5535 | 0.1804 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.78 | 0.3939 | 0.1651 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.75 | 0.4217 | 0.2461 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.96 | 0.4295 | 0.2335 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.80 | 0.4342 | 0.2417 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.86 | 0.4321 | 0.2383 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.74 | 0.4605 | 0.2358 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.96 | 0.4535 | 0.2237 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.77 | 0.4624 | 0.2320 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.84 | 0.4571 | 0.2289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.00 | 0.7508 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.13 | 0.7555 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.12 | 0.7554 | 0.0260 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.08 | 0.7554 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.00 | 0.7683 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.86 | 0.7673 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.96 | 0.7698 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.89 | 0.7687 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.50 | 0.7612 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.37 | 0.7685 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.37 | 0.7680 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.18 | 0.7658 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.24 | 0.7663 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.65 | 0.7628 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.31 | 0.7678 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.34 | 0.7671 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.94 | 0.7639 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.99 | 0.7638 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.69 | 0.7586 | 0.0268 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.30 | 0.7411 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.77 | 0.7499 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.66 | 0.7482 | 0.0286 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.67 | 0.7490 | 0.0277 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.67 | 0.7592 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.36 | 0.7597 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.58 | 0.7625 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.38 | 0.7606 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.30 | 0.7500 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.24 | 0.7581 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.61 | 0.7611 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.52 | 0.7611 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.56 | 0.7613 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.30 | 0.7701 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.13 | 0.7680 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.20 | 0.7703 | 0.0220 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.11 | 0.7690 | 0.0220 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.27 | 0.7190 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.64 | 0.7263 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.62 | 0.7287 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.59 | 0.7279 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.71 | 0.7555 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.76 | 0.7539 | 0.0255 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.90 | 0.7612 | 0.0256 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.82 | 0.7582 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.00 | 0.7520 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.14 | 0.7493 | 0.0388 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.41 | 0.7582 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.00 | 0.7440 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.37 | 0.7562 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.09 | 0.7566 | 0.0269 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.06 | 0.7459 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.38 | 0.7546 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.70 | 0.7400 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.05 | 0.7497 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.05 | 0.7149 | 0.0494 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.28 | 0.6930 | 0.0439 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.71 | 0.7042 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.76 | 0.7072 | 0.0403 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.72 | 0.7062 | 0.0388 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.16 | 0.7355 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.72 | 0.7346 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.06 | 0.7428 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.79 | 0.7376 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.60 | 0.6934 | 0.0527 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.92 | 0.7386 | 0.0391 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.99 | 0.7362 | 0.0408 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.23 | 0.7429 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.13 | 0.7399 | 0.0390 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.41 | 0.7593 | 0.0337 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.78 | 0.7498 | 0.0343 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.27 | 0.7595 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.02 | 0.7551 | 0.0337 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 48.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.39 | 0.7371 | 0.0266 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.00 | 0.3841 | 0.2983 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.08 | 0.3932 | 0.2899 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.03 | 0.3981 | 0.2946 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.04 | 0.3956 | 0.2928 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.02 | 0.4002 | 0.2533 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.03 | 0.3978 | 0.2482 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.02 | 0.4075 | 0.2507 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.02 | 0.4026 | 0.2496 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.00 | 0.5399 | 0.1524 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.83 | 0.5317 | 0.1583 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.83 | 0.5317 | 0.1583 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.72 | 0.5219 | 0.1623 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.72 | 0.5219 | 0.1623 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.48 | 0.3650 | 0.1772 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.46 | 0.3564 | 0.1843 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.46 | 0.3564 | 0.1843 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.41 | 0.3474 | 0.1869 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.41 | 0.3474 | 0.1869 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.41 | 0.3415 | 0.1851 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.94 | 0.4230 | 0.2772 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.03 | 0.4393 | 0.2644 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.98 | 0.4417 | 0.2715 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.00 | 0.4411 | 0.2681 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.95 | 0.4787 | 0.2605 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.02 | 0.4798 | 0.2510 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.97 | 0.4899 | 0.2545 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.98 | 0.4838 | 0.2529 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.62 | 0.4017 | 0.1691 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.52 | 0.3677 | 0.3158 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.59 | 0.3756 | 0.3049 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.55 | 0.3782 | 0.3115 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.56 | 0.3767 | 0.3089 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.51 | 0.4016 | 0.3067 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.55 | 0.3955 | 0.2980 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.51 | 0.4033 | 0.3035 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.52 | 0.3986 | 0.3009 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.32 | 0.7260 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.47 | 0.7294 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.46 | 0.7294 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.43 | 0.7294 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.90 | 0.7352 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.83 | 0.7347 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.86 | 0.7361 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.84 | 0.7356 | 0.0272 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.47 | 0.7305 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.28 | 0.7366 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.28 | 0.7360 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.14 | 0.7348 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.18 | 0.7348 | 0.0311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.61 | 0.7316 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.24 | 0.7366 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.27 | 0.7360 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.94 | 0.7339 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.97 | 0.7334 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.81 | 0.7323 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.64 | 0.7187 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.14 | 0.7251 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.00 | 0.7237 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.04 | 0.7243 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.67 | 0.7299 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.48 | 0.7301 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.61 | 0.7319 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.49 | 0.7308 | 0.0289 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.38 | 0.7262 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.48 | 0.7302 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.79 | 0.7322 | 0.0298 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.73 | 0.7323 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.75 | 0.7323 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.21 | 0.7376 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.12 | 0.7365 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.14 | 0.7378 | 0.0278 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.09 | 0.7370 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.28 | 0.7091 | 0.0408 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.57 | 0.7134 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.64 | 0.7158 | 0.0393 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.57 | 0.7150 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.42 | 0.7307 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.40 | 0.7287 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.48 | 0.7330 | 0.0304 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.43 | 0.7313 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.25 | 0.7284 | 0.0363 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.77 | 0.7309 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.92 | 0.7325 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.52 | 0.7274 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.71 | 0.7305 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.37 | 0.7299 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.68 | 0.7309 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.83 | 0.7319 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.27 | 0.7268 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.42 | 0.7285 | 0.0334 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.31 | 0.7251 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.07 | 0.6862 | 0.0479 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.57 | 0.6946 | 0.0429 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.56 | 0.6961 | 0.0453 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.56 | 0.6957 | 0.0440 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.81 | 0.7174 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.39 | 0.7140 | 0.0353 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.69 | 0.7206 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.44 | 0.7167 | 0.0352 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.49 | 0.7102 | 0.0388 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.74 | 0.7228 | 0.0415 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.20 | 0.7248 | 0.0378 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.06 | 0.7261 | 0.0398 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.10 | 0.7256 | 0.0389 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.94 | 0.7366 | 0.0346 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.82 | 0.7336 | 0.0322 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.89 | 0.7377 | 0.0333 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.81 | 0.7357 | 0.0326 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 73.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.11 | 0.7260 | 0.0281 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.36 | 0.3303 | 0.3085 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.41 | 0.3333 | 0.3011 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.38 | 0.3372 | 0.3054 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.38 | 0.3352 | 0.3036 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.19 | 0.2960 | 0.2781 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.18 | 0.2921 | 0.2727 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.16 | 0.2994 | 0.2760 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.17 | 0.2954 | 0.2743 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.40 | 0.5237 | 0.1923 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.18 | 0.5176 | 0.1954 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.18 | 0.5176 | 0.1954 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.16 | 0.5152 | 0.1963 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.16 | 0.5152 | 0.1963 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.97 | 0.2277 | 0.2116 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.95 | 0.2246 | 0.2147 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.95 | 0.2246 | 0.2147 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.95 | 0.2231 | 0.2150 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.95 | 0.2231 | 0.2150 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.93 | 0.2184 | 0.2140 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.83 | 0.3607 | 0.2895 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.88 | 0.3668 | 0.2806 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.85 | 0.3703 | 0.2857 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.86 | 0.3692 | 0.2832 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.79 | 0.3814 | 0.2804 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.84 | 0.3761 | 0.2726 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.80 | 0.3857 | 0.2774 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.82 | 0.3803 | 0.2751 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.50 | 0.2679 | 0.1967 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.07 | 0.3144 | 0.3223 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.12 | 0.3172 | 0.3158 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.09 | 0.3197 | 0.3196 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.10 | 0.3181 | 0.3181 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.04 | 0.3245 | 0.3165 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.07 | 0.3208 | 0.3115 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.05 | 0.3262 | 0.3145 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.05 | 0.3228 | 0.3132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 30.10 | 0.7258 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.09 | 0.7259 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.10 | 0.7259 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.09 | 0.7259 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.11 | 0.7260 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.11 | 0.7261 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.11 | 0.7261 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.11 | 0.7261 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 30.12 | 0.7262 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 30.12 | 0.7262 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 30.11 | 0.7260 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 30.12 | 0.7261 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 30.11 | 0.7260 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 30.12 | 0.7261 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.12 | 0.7261 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 30.11 | 0.7261 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 30.12 | 0.7261 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 30.11 | 0.7261 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.12 | 0.7262 | 0.0280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 30.05 | 0.7256 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.08 | 0.7257 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.07 | 0.7258 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.07 | 0.7258 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.10 | 0.7259 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.08 | 0.7258 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.09 | 0.7258 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.08 | 0.7258 | 0.0283 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 30.11 | 0.7261 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.10 | 0.7259 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 30.10 | 0.7259 | 0.0282 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 30.10 | 0.7259 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 30.10 | 0.7259 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 30.11 | 0.7260 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.10 | 0.7260 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.11 | 0.7260 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.10 | 0.7260 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.60 | 0.7214 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.53 | 0.7216 | 0.0309 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.70 | 0.7228 | 0.0312 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.62 | 0.7224 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.00 | 0.7261 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.03 | 0.7258 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.07 | 0.7267 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.06 | 0.7263 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 30.15 | 0.7271 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 30.04 | 0.7266 | 0.0284 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 30.01 | 0.7257 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 30.04 | 0.7263 | 0.0284 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 30.02 | 0.7257 | 0.0282 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 30.13 | 0.7271 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.98 | 0.7265 | 0.0286 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.96 | 0.7256 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.98 | 0.7264 | 0.0286 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.97 | 0.7257 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.98 | 0.7266 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.08 | 0.7181 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.20 | 0.7192 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.23 | 0.7202 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.22 | 0.7199 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.79 | 0.7245 | 0.0311 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.39 | 0.7222 | 0.0317 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.69 | 0.7245 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.50 | 0.7233 | 0.0315 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.86 | 0.7259 | 0.0298 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.91 | 0.7252 | 0.0300 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.89 | 0.7247 | 0.0300 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.93 | 0.7255 | 0.0298 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.92 | 0.7252 | 0.0299 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 30.10 | 0.7266 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.91 | 0.7254 | 0.0292 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.05 | 0.7265 | 0.0290 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.96 | 0.7259 | 0.0291 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.10 | 0.7292 | 0.0441 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.09 | 0.3505 | 0.3770 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.15 | 0.3558 | 0.3635 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.11 | 0.3605 | 0.3717 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.12 | 0.3581 | 0.3681 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.84 | 0.3365 | 0.3369 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.85 | 0.3328 | 0.3276 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.83 | 0.3416 | 0.3328 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.83 | 0.3369 | 0.3301 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.69 | 0.5266 | 0.2610 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.47 | 0.5189 | 0.2667 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.47 | 0.5189 | 0.2667 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.42 | 0.5127 | 0.2710 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.42 | 0.5127 | 0.2710 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.38 | 0.2890 | 0.2751 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.34 | 0.2829 | 0.2830 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.34 | 0.2829 | 0.2830 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.32 | 0.2773 | 0.2854 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.32 | 0.2773 | 0.2854 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.31 | 0.2727 | 0.2839 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.72 | 0.3848 | 0.3535 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.78 | 0.3957 | 0.3356 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.74 | 0.3986 | 0.3458 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.76 | 0.3976 | 0.3413 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.69 | 0.4210 | 0.3324 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.75 | 0.4179 | 0.3149 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.70 | 0.4282 | 0.3230 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.72 | 0.4220 | 0.3183 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.12 | 0.3257 | 0.2587 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.72 | 0.3353 | 0.3905 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.77 | 0.3404 | 0.3754 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.74 | 0.3433 | 0.3843 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.75 | 0.3416 | 0.3807 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.69 | 0.3547 | 0.3765 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.73 | 0.3488 | 0.3636 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.70 | 0.3559 | 0.3709 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.71 | 0.3516 | 0.3672 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.29 | 0.7230 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.42 | 0.7250 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.39 | 0.7249 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.37 | 0.7249 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.73 | 0.7281 | 0.0459 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.69 | 0.7277 | 0.0451 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.72 | 0.7286 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.70 | 0.7283 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.55 | 0.7262 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.94 | 0.7287 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.93 | 0.7282 | 0.0477 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.81 | 0.7276 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.83 | 0.7274 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.64 | 0.7267 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.93 | 0.7287 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.94 | 0.7283 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.70 | 0.7271 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.72 | 0.7268 | 0.0482 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.73 | 0.7269 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.82 | 0.7187 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.18 | 0.7223 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.07 | 0.7215 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.09 | 0.7219 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.56 | 0.7248 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.40 | 0.7247 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.51 | 0.7259 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.41 | 0.7252 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.41 | 0.7234 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.42 | 0.7254 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.66 | 0.7264 | 0.0477 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.60 | 0.7265 | 0.0482 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.63 | 0.7265 | 0.0479 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.94 | 0.7293 | 0.0458 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.88 | 0.7285 | 0.0451 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.90 | 0.7294 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.86 | 0.7289 | 0.0453 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.50 | 0.7127 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.72 | 0.7152 | 0.0572 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.76 | 0.7167 | 0.0586 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.71 | 0.7162 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.38 | 0.7258 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.38 | 0.7245 | 0.0485 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.45 | 0.7273 | 0.0491 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.42 | 0.7262 | 0.0485 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.42 | 0.7257 | 0.0539 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.55 | 0.7261 | 0.0543 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.61 | 0.7262 | 0.0501 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.40 | 0.7240 | 0.0560 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.49 | 0.7249 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.49 | 0.7264 | 0.0498 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.48 | 0.7261 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.55 | 0.7259 | 0.0493 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.23 | 0.7237 | 0.0543 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.31 | 0.7240 | 0.0510 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.32 | 0.7238 | 0.0538 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.54 | 0.6991 | 0.0690 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.93 | 0.7040 | 0.0632 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.92 | 0.7051 | 0.0662 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.91 | 0.7048 | 0.0644 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.90 | 0.7174 | 0.0580 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.47 | 0.7144 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.78 | 0.7191 | 0.0549 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.54 | 0.7164 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.76 | 0.7154 | 0.0570 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.88 | 0.7211 | 0.0603 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.20 | 0.7219 | 0.0566 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.11 | 0.7230 | 0.0584 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.14 | 0.7226 | 0.0576 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.75 | 0.7288 | 0.0531 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.59 | 0.7264 | 0.0505 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.70 | 0.7292 | 0.0516 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.60 | 0.7277 | 0.0508 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 227243 | 0.174 | 32.4 | 28.30 | 0.25 | 0.020 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 227243 | 0.174 | 32.0 | 28.30 | 0.25 | 0.020 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 227243 | 0.174 | 34.9 | 28.30 | 0.25 | 0.020 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 227243 | 0.174 | 29.2 | 28.30 | 0.25 | 0.020 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 700 | None | classic | 0.39 | False | 370341 | 0.512 | 85.8 | 31.05 | 0.29 | 0.012 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 700 | None | classic | 0.39 | False | 370341 | 0.512 | 88.6 | 31.05 | 0.29 | 0.012 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 700 | None | classic | 0.39 | False | 370341 | 0.512 | 89.6 | 31.05 | 0.29 | 0.012 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 700 | None | classic | 0.39 | False | 370341 | 0.512 | 88.7 | 31.05 | 0.29 | 0.012 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1356513 | 0.180 | 27.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1356355 | 0.805 | 52.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1356355 | 0.805 | 52.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1356513 | 0.842 | 27.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1356513 | 0.842 | 27.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1356513 | 0.180 | 34.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1356355 | 0.805 | 76.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1356355 | 0.805 | 76.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1356513 | 0.842 | 35.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1356513 | 0.842 | 35.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1350568 | 0.805 | 161.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 237750 | 0.177 | 39.2 | 28.38 | 0.30 | 0.025 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 237750 | 0.177 | 31.3 | 28.38 | 0.30 | 0.025 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 237750 | 0.177 | 33.1 | 28.38 | 0.30 | 0.025 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 237750 | 0.177 | 35.9 | 28.38 | 0.30 | 0.025 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 785 | None | classic | 0.49 | False | 389646 | 0.512 | 91.8 | 29.58 | 0.10 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 785 | None | classic | 0.49 | False | 389646 | 0.512 | 97.1 | 29.58 | 0.10 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 785 | None | classic | 0.49 | False | 389646 | 0.512 | 93.2 | 29.58 | 0.10 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 785 | None | classic | 0.49 | False | 389646 | 0.512 | 87.9 | 29.58 | 0.10 | 0.009 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1621893 | 0.805 | 71.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 232750 | 0.320 | 38.9 | 28.90 | 0.19 | 0.025 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 232750 | 0.320 | 42.7 | 28.90 | 0.19 | 0.025 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 232750 | 0.320 | 33.2 | 28.90 | 0.19 | 0.025 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 232750 | 0.320 | 37.1 | 28.90 | 0.19 | 0.025 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 692 | None | classic | 0.55 | False | 385491 | 0.508 | 99.6 | 28.38 | 0.34 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 692 | None | classic | 0.55 | False | 385491 | 0.508 | 92.0 | 28.38 | 0.34 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 692 | None | classic | 0.55 | False | 385491 | 0.508 | 95.0 | 28.38 | 0.34 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 692 | None | classic | 0.55 | False | 385491 | 0.508 | 99.0 | 28.38 | 0.34 | 0.005 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.701 | 0.019 |
| in035 | mask_ent | 0.716 | 0.019 |
| in035 | mask_grad | 0.477 | 0.019 |
| in035 | r_col | 0.791 | 0.019 |
| in035 | r_warp | 0.878 | 0.019 |

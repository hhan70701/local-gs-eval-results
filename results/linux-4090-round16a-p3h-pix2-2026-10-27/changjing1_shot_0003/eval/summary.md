# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 29.9% | 28.32 / 0.0311 | 27.95 / 0.0783 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 30.1% | 28.33 / 0.0305 | 29.17 / 0.0660 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 29.9% | 28.37 / 0.0310 | 29.15 / 0.0702 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 29.9% | 28.37 / 0.0308 | 29.09 / 0.0683 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 29.4% | 28.31 / 0.0308 | 28.03 / 0.0779 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 29.5% | 28.30 / 0.0311 | 29.04 / 0.0632 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 29.3% | 28.35 / 0.0310 | 29.13 / 0.0676 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 29.4% | 28.33 / 0.0311 | 29.09 / 0.0647 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 28.6% | 27.94 / 0.0287 | 30.00 / 0.0362 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 26.8% | 27.96 / 0.0301 | 28.62 / 0.0417 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.7% | 22.87 / 0.0174 | 20.49 / 0.0375 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 26.8% | 28.00 / 0.0292 | 28.00 / 0.0465 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.9% | 22.92 / 0.0119 | 19.85 / 0.0285 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 28.7% | 27.95 / 0.0285 | 29.43 / 0.0388 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 26.7% | 28.27 / 0.0295 | 29.44 / 0.0420 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.7% | 23.67 / 0.0125 | 22.46 / 0.0207 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 26.7% | 28.36 / 0.0293 | 29.01 / 0.0465 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.9% | 23.86 / 0.0132 | 21.72 / 0.0254 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 29.2% | 27.96 / 0.0303 | 26.74 / 0.0619 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 29.8% | 28.02 / 0.0279 | 26.55 / 0.0731 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 30.1% | 28.12 / 0.0275 | 28.03 / 0.0623 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 29.9% | 28.12 / 0.0281 | 27.89 / 0.0641 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 29.9% | 28.13 / 0.0280 | 27.89 / 0.0635 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 29.5% | 28.12 / 0.0279 | 26.90 / 0.0709 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 29.8% | 28.22 / 0.0284 | 28.43 / 0.0583 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 29.6% | 28.20 / 0.0274 | 28.25 / 0.0632 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 29.6% | 28.20 / 0.0271 | 28.33 / 0.0600 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 29.6% | 27.88 / 0.0274 | 25.65 / 0.0655 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 7.3% | 29.33 / 0.0107 | 27.03 / 0.0310 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 8.3% | 29.82 / 0.0114 | 25.57 / 0.0360 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 7.6% | 29.68 / 0.0102 | 27.01 / 0.0299 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 7.9% | 29.78 / 0.0105 | 26.71 / 0.0301 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 7.4% | 29.61 / 0.0102 | 26.71 / 0.0276 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 8.2% | 29.85 / 0.0104 | 25.85 / 0.0326 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 7.6% | 29.85 / 0.0100 | 26.96 / 0.0263 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 7.8% | 29.92 / 0.0099 | 26.51 / 0.0268 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 30.70 / 0.0739 | 31.12 / 0.0877 | 20.51 / 0.0185 | 32.23 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 31.09 / 0.1125 | 31.95 / 0.1413 | 22.57 / 0.0180 | 32.03 / 0.0448 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.48 / 0.1028 | 32.14 / 0.1304 | 23.11 / 0.0158 | 32.08 / 0.0435 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.47 / 0.1057 | 32.27 / 0.1324 | 23.36 / 0.0162 | 32.04 / 0.0441 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.43 / 0.1046 | 32.19 / 0.1311 | 23.12 / 0.0164 | 32.06 / 0.0438 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.06 / 0.1119 | 31.80 / 0.1396 | 22.90 / 0.0172 | 31.99 / 0.0449 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.35 / 0.1016 | 32.13 / 0.1280 | 23.19 / 0.0155 | 32.03 / 0.0434 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.40 / 0.1031 | 32.18 / 0.1295 | 23.43 / 0.0160 | 32.06 / 0.0434 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.40 / 0.1016 | 32.19 / 0.1278 | 23.32 / 0.0161 | 32.07 / 0.0430 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 31.78 / 0.0750 | 32.54 / 0.0931 | 23.45 / 0.0139 | 32.41 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 31.86 / 0.0823 | 32.59 / 0.0945 | 23.99 / 0.0179 | 32.21 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 31.26 / 0.0758 | 31.81 / 0.0895 | 22.49 / 0.0184 | 32.16 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 31.51 / 0.0853 | 32.17 / 0.1007 | 23.62 / 0.0184 | 31.99 / 0.0420 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 31.00 / 0.0795 | 31.50 / 0.0950 | 22.27 / 0.0194 | 31.95 / 0.0408 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 31.60 / 0.0769 | 32.42 / 0.0963 | 22.93 / 0.0134 | 32.28 / 0.0385 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.85 / 0.0821 | 32.59 / 0.0984 | 23.71 / 0.0166 | 32.29 / 0.0389 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.28 / 0.0749 | 31.87 / 0.0891 | 22.34 / 0.0177 | 32.21 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 31.62 / 0.0849 | 32.34 / 0.1025 | 23.44 / 0.0178 | 32.24 / 0.0416 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 31.10 / 0.0786 | 31.69 / 0.0946 | 22.24 / 0.0188 | 32.14 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 31.02 / 0.0863 | 31.32 / 0.1070 | 22.69 / 0.0184 | 31.88 / 0.0402 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 30.99 / 0.1119 | 31.82 / 0.1383 | 22.27 / 0.0177 | 31.74 / 0.0448 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.38 / 0.1022 | 32.04 / 0.1272 | 22.74 / 0.0160 | 32.03 / 0.0427 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.37 / 0.1054 | 32.15 / 0.1293 | 23.08 / 0.0161 | 31.89 / 0.0437 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.32 / 0.1040 | 32.07 / 0.1278 | 22.80 / 0.0164 | 31.96 / 0.0431 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.06 / 0.1113 | 31.73 / 0.1364 | 22.82 / 0.0167 | 31.75 / 0.0451 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.29 / 0.1010 | 32.03 / 0.1251 | 22.93 / 0.0157 | 31.88 / 0.0435 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.38 / 0.1031 | 32.08 / 0.1269 | 23.24 / 0.0159 | 31.90 / 0.0438 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.35 / 0.1013 | 32.08 / 0.1250 | 23.08 / 0.0161 | 31.91 / 0.0432 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.98 / 0.0856 | 31.21 / 0.1082 | 22.51 / 0.0180 | 31.87 / 0.0396 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 30.50 / 0.0881 | 30.97 / 0.1026 | 20.66 / 0.0197 | 32.11 / 0.0415 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 30.44 / 0.0871 | 30.99 / 0.1021 | 20.49 / 0.0194 | 32.09 / 0.0418 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 30.44 / 0.0876 | 30.93 / 0.1021 | 20.80 / 0.0189 | 32.06 / 0.0419 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 30.40 / 0.0874 | 30.94 / 0.1016 | 20.71 / 0.0191 | 32.07 / 0.0419 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 30.48 / 0.0885 | 31.04 / 0.1007 | 20.83 / 0.0192 | 32.11 / 0.0413 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.48 / 0.0876 | 31.09 / 0.0994 | 20.77 / 0.0187 | 32.15 / 0.0410 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.50 / 0.0878 | 31.08 / 0.0988 | 20.89 / 0.0188 | 32.14 / 0.0410 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.47 / 0.0871 | 31.08 / 0.0988 | 20.78 / 0.0187 | 32.15 / 0.0410 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 3.4%） | — | — | 30.70 / 0.0739 | 31.12 / 0.0877 | 32.23 |
| in035 | rife | 3.1% | 7.3% | 30.50 / 0.0881 | 30.97 / 0.1026 | 32.11 |
| in035 | cnw_cnn | 21.2% | 29.9% | 31.09 / 0.1125 | 31.95 / 0.1413 | 32.03 |
| in035 | cnw_f5 | 21.4% | 29.8% | 30.99 / 0.1119 | 31.82 / 0.1383 | 31.74 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 29.08 / 0.0830 | +0.12 / +0.0106 (core 2.3%) | +1.37 / +0.0455 (core 27.9%) | +1.51 / +0.0466 (core 29.6%) |
| in035 | 2 | 0-3 | 31.63 / 0.0694 | -0.52 / +0.0201 (core 2.3%) | -0.43 / +0.0531 (core 27.9%) | -0.69 / +0.0589 (core 29.6%) |
| in035 | 4 | 3-5 | 31.39 / 0.0694 | -0.21 / +0.0118 (core 2.6%) | +0.22 / +0.0170 (core 6.3%) | +0.04 / +0.0084 (core 3.2%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 30.70 / 0.0739 | 31.12 | 32.23 | — |
| in035 | cnw_cnn | 不复核 | —% | 31.09 / 0.1125 | 31.95 | 32.03 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 31.42 / 0.0765 | 32.09 | 32.23 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 31.48 / 0.1028 | 32.14 | 32.08 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 31.64 / 0.0734 | 32.21 | 32.23 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 31.47 / 0.1057 | 32.27 | 32.04 | 0/3 |
| in035 | cnw_cnn | oracle | 2.4% | 31.67 / 0.0746 | 32.29 | 32.23 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 31.43 / 0.1046 | 32.19 | 32.06 | 0/3 |
| in035 | cnw_cnn | oracle | 2.3% | 31.63 / 0.0744 | 32.24 | 32.23 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 31.06 / 0.1119 | 31.80 | 31.99 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 31.52 / 0.0761 | 32.10 | 32.23 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 31.35 / 0.1016 | 32.13 | 32.03 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 31.66 / 0.0736 | 32.28 | 32.24 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 31.40 / 0.1031 | 32.18 | 32.06 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.3% | 31.70 / 0.0744 | 32.29 | 32.23 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 31.40 / 0.1016 | 32.19 | 32.07 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.3% | 31.68 / 0.0740 | 32.29 | 32.23 | 1/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 31.78 / 0.0750 | 32.54 | 32.41 | 1/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 2.4% | 31.59 / 0.0713 | 32.31 | 32.25 | 1/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 31.86 / 0.0823 | 32.59 | 32.21 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 2.3% | 31.80 / 0.0755 | 32.37 | 32.25 | 1/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 31.26 / 0.0758 | 31.81 | 32.16 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 1.2% | 31.46 / 0.0743 | 32.00 | 32.23 | 1/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 31.51 / 0.0853 | 32.17 | 31.99 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 2.3% | 31.67 / 0.0758 | 32.23 | 32.25 | 1/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 31.00 / 0.0795 | 31.50 | 31.95 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 1.2% | 31.36 / 0.0752 | 31.89 | 32.23 | 1/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 31.60 / 0.0769 | 32.42 | 32.28 | 1/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 2.4% | 31.47 / 0.0704 | 32.24 | 32.24 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 31.85 / 0.0821 | 32.59 | 32.29 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.2% | 31.75 / 0.0736 | 32.32 | 32.24 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 31.28 / 0.0749 | 31.87 | 32.21 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.1% | 31.43 / 0.0733 | 31.99 | 32.23 | 1/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 31.62 / 0.0849 | 32.34 | 32.24 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 2.2% | 31.63 / 0.0744 | 32.17 | 32.25 | 1/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 31.10 / 0.0786 | 31.69 | 32.14 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 1.2% | 31.35 / 0.0743 | 31.89 | 32.23 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 31.02 / 0.0863 | 31.32 | 31.88 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.5% | 31.34 / 0.0750 | 31.74 | 32.24 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 30.99 / 0.1119 | 31.82 | 31.74 | 0/3 |
| in035 | cnw_f5 | oracle | 2.1% | 31.36 / 0.0755 | 31.95 | 32.22 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 31.38 / 0.1022 | 32.04 | 32.03 | 0/3 |
| in035 | cnw_f5 | oracle | 2.1% | 31.55 / 0.0733 | 32.08 | 32.24 | 2/3 |
| in035 | cnw_f5 | 不复核 | —% | 31.37 / 0.1054 | 32.15 | 31.89 | 0/3 |
| in035 | cnw_f5 | oracle | 2.1% | 31.61 / 0.0739 | 32.15 | 32.23 | 2/3 |
| in035 | cnw_f5 | 不复核 | —% | 31.32 / 0.1040 | 32.07 | 31.96 | 0/3 |
| in035 | cnw_f5 | oracle | 2.1% | 31.56 / 0.0739 | 32.10 | 32.23 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 31.06 / 0.1113 | 31.73 | 31.75 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.1% | 31.50 / 0.0751 | 32.01 | 32.22 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 31.29 / 0.1010 | 32.03 | 31.88 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.1% | 31.59 / 0.0732 | 32.15 | 32.23 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 31.38 / 0.1031 | 32.08 | 31.90 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.1% | 31.65 / 0.0740 | 32.17 | 32.23 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 31.35 / 0.1013 | 32.08 | 31.91 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.1% | 31.62 / 0.0737 | 32.16 | 32.23 | 2/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 30.98 / 0.0856 | 31.21 | 31.87 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.2% | 31.29 / 0.0746 | 31.73 | 32.24 | 2/3 |
| in035 | rife | 不复核 | —% | 30.50 / 0.0881 | 30.97 | 32.11 | 0/3 |
| in035 | rife | oracle | 0.4% | 30.77 / 0.0753 | 31.27 | 32.23 | 1/3 |
| in035 | rife | 不复核 | —% | 30.44 / 0.0871 | 30.99 | 32.09 | 0/3 |
| in035 | rife | oracle | 0.4% | 30.71 / 0.0747 | 31.29 | 32.23 | 0/3 |
| in035 | rife | 不复核 | —% | 30.44 / 0.0876 | 30.93 | 32.06 | 0/3 |
| in035 | rife | oracle | 0.3% | 30.81 / 0.0744 | 31.28 | 32.23 | 1/3 |
| in035 | rife | 不复核 | —% | 30.40 / 0.0874 | 30.94 | 32.07 | 0/3 |
| in035 | rife | oracle | 0.3% | 30.78 / 0.0745 | 31.28 | 32.23 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 30.48 / 0.0885 | 31.04 | 32.11 | 0/3 |
| in035 | rife_mw | oracle | 0.4% | 30.80 / 0.0748 | 31.28 | 32.23 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 30.48 / 0.0876 | 31.09 | 32.15 | 0/3 |
| in035 | rife_mw | oracle | 0.3% | 30.78 / 0.0744 | 31.30 | 32.23 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 30.50 / 0.0878 | 31.08 | 32.14 | 0/3 |
| in035 | rife_mw | oracle | 0.3% | 30.81 / 0.0746 | 31.30 | 32.23 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 30.47 / 0.0871 | 31.08 | 32.15 | 0/3 |
| in035 | rife_mw | oracle | 0.3% | 30.78 / 0.0745 | 31.30 | 32.23 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 30.70 / 0.0739 | 31.12 / 0.0877 | — |
| in035 | FF | 0（前馈） | 958×706（63%） | 31.96 | 31.09 / 0.1125 | 31.95 / 0.1413 | 0/3 |
| in035 | 25 | 0.51 s | 958×706（63%） | 33.65 | 31.47 / 0.1057 | 32.27 / 0.1324 | 0/3 |
| in035 | 50 | 1.00 s | 958×706（63%） | 34.38 | 31.43 / 0.1046 | 32.19 / 0.1311 | 0/3 |
| in035 | 100 | 1.97 s | 958×706（63%） | 35.07 | 31.48 / 0.1028 | 32.14 / 0.1304 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 30.70 / 0.0739 | 31.12 / 0.0877 | 32.23 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 31.09 / 0.1125 | 31.95 / 0.1413 | 32.03 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 31.42 / 0.0765 | 32.09 / 0.0920 | 32.23 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 31.47 / 0.1057 | 32.27 / 0.1324 | 32.04 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 31.67 / 0.0746 | 32.29 / 0.0899 | 32.23 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 31.43 / 0.1046 | 32.19 / 0.1311 | 32.06 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 31.63 / 0.0744 | 32.24 / 0.0900 | 32.23 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 31.48 / 0.1028 | 32.14 / 0.1304 | 32.08 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 31.64 / 0.0734 | 32.21 / 0.0905 | 32.23 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 31.06 / 0.1119 | 31.80 / 0.1396 | 31.99 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 31.52 / 0.0761 | 32.10 / 0.0916 | 32.23 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 31.40 / 0.1031 | 32.18 / 0.1295 | 32.06 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 31.70 / 0.0744 | 32.29 / 0.0900 | 32.23 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 31.40 / 0.1016 | 32.19 / 0.1278 | 32.07 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 31.68 / 0.0740 | 32.29 / 0.0897 | 32.23 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 31.35 / 0.1016 | 32.13 / 0.1280 | 32.03 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 31.66 / 0.0736 | 32.28 / 0.0893 | 32.24 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 30.99 / 0.1119 | 31.82 / 0.1383 | 31.74 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 31.36 / 0.0755 | 31.95 / 0.0911 | 32.22 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 31.37 / 0.1054 | 32.15 / 0.1293 | 31.89 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 31.61 / 0.0739 | 32.15 / 0.0894 | 32.23 | 2/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 31.32 / 0.1040 | 32.07 / 0.1278 | 31.96 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 31.56 / 0.0739 | 32.10 / 0.0897 | 32.23 | 2/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 31.38 / 0.1022 | 32.04 / 0.1272 | 32.03 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 31.55 / 0.0733 | 32.08 / 0.0902 | 32.24 | 2/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 31.06 / 0.1113 | 31.73 / 0.1364 | 31.75 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 31.50 / 0.0751 | 32.01 / 0.0903 | 32.22 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 31.38 / 0.1031 | 32.08 / 0.1269 | 31.90 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 31.65 / 0.0740 | 32.17 / 0.0895 | 32.23 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 31.35 / 0.1013 | 32.08 / 0.1250 | 31.91 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 31.62 / 0.0737 | 32.16 / 0.0893 | 32.23 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 31.29 / 0.1010 | 32.03 / 0.1251 | 31.88 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 31.59 / 0.0732 | 32.15 / 0.0890 | 32.23 | 2/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 30.50 / 0.0881 | 30.97 / 0.1026 | 32.11 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 30.77 / 0.0753 | 31.27 / 0.0878 | 32.23 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 30.44 / 0.0876 | 30.93 / 0.1021 | 32.06 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 30.81 / 0.0744 | 31.28 / 0.0878 | 32.23 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 30.40 / 0.0874 | 30.94 / 0.1016 | 32.07 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 30.78 / 0.0745 | 31.28 / 0.0875 | 32.23 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 30.44 / 0.0871 | 30.99 / 0.1021 | 32.09 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 30.71 / 0.0747 | 31.29 / 0.0874 | 32.23 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 30.48 / 0.0885 | 31.04 / 0.1007 | 32.11 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 30.80 / 0.0748 | 31.28 / 0.0880 | 32.23 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 30.50 / 0.0878 | 31.08 / 0.0988 | 32.14 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 30.81 / 0.0746 | 31.30 / 0.0877 | 32.23 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 30.47 / 0.0871 | 31.08 / 0.0988 | 32.15 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 30.78 / 0.0745 | 31.30 / 0.0879 | 32.23 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 30.48 / 0.0876 | 31.09 / 0.0994 | 32.15 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 30.78 / 0.0744 | 31.30 / 0.0875 | 32.23 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.12 / 0.0877 | 20.51 / 0.0185 | 32.23 / 0.0371 | 30.70 / 0.0739 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 80.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.12 | 0.8343 | 0.0877 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.37 | 0.6841 | 0.5682 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.50 | 0.6756 | 0.5555 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.43 | 0.6839 | 0.5553 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.47 | 0.6801 | 0.5546 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.42 | 0.6826 | 0.5678 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.64 | 0.6742 | 0.5580 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.51 | 0.6829 | 0.5544 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.58 | 0.6794 | 0.5545 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 22.78 | 0.8263 | 0.2767 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 22.91 | 0.8375 | 0.2974 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 22.91 | 0.8375 | 0.2974 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 23.38 | 0.8341 | 0.3053 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 23.38 | 0.8341 | 0.3053 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.00 | 0.4403 | 0.4849 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.98 | 0.4345 | 0.5045 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.98 | 0.4345 | 0.5045 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.05 | 0.4327 | 0.5068 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.05 | 0.4327 | 0.5068 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.90 | 0.4221 | 0.5101 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.34 | 0.6768 | 0.5859 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.49 | 0.6693 | 0.5720 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.40 | 0.6765 | 0.5729 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.45 | 0.6733 | 0.5715 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.40 | 0.6748 | 0.5858 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.64 | 0.6679 | 0.5733 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.49 | 0.6754 | 0.5724 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.57 | 0.6723 | 0.5711 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 10.79 | 0.3926 | 0.5363 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.38 | 0.5997 | 0.7045 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.43 | 0.5961 | 0.6977 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.39 | 0.5992 | 0.7007 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.41 | 0.5977 | 0.6989 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.40 | 0.5992 | 0.7030 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.44 | 0.5936 | 0.6964 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.41 | 0.5993 | 0.6983 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.42 | 0.5969 | 0.6968 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 32.09 | 0.8396 | 0.0920 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 32.21 | 0.8398 | 0.0905 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 32.29 | 0.8405 | 0.0899 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 32.24 | 0.8401 | 0.0900 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 32.10 | 0.8395 | 0.0916 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.28 | 0.8401 | 0.0893 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 32.29 | 0.8403 | 0.0900 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 32.29 | 0.8402 | 0.0897 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 32.31 | 0.8399 | 0.0881 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 32.37 | 0.8403 | 0.0892 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 32.00 | 0.8381 | 0.0880 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 32.23 | 0.8399 | 0.0901 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 31.89 | 0.8379 | 0.0889 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 32.24 | 0.8400 | 0.0871 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 32.32 | 0.8398 | 0.0888 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.99 | 0.8381 | 0.0877 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 32.17 | 0.8392 | 0.0893 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 31.89 | 0.8377 | 0.0885 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 31.74 | 0.8384 | 0.0929 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 31.95 | 0.8388 | 0.0911 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 32.08 | 0.8389 | 0.0902 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 32.15 | 0.8397 | 0.0894 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 32.10 | 0.8392 | 0.0897 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 32.01 | 0.8390 | 0.0903 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 32.15 | 0.8394 | 0.0890 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 32.17 | 0.8396 | 0.0895 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 32.16 | 0.8395 | 0.0893 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 31.73 | 0.8382 | 0.0919 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.27 | 0.8356 | 0.0878 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.29 | 0.8356 | 0.0874 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.28 | 0.8356 | 0.0878 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.28 | 0.8355 | 0.0875 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 31.28 | 0.8356 | 0.0880 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.30 | 0.8356 | 0.0875 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.30 | 0.8356 | 0.0877 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.30 | 0.8356 | 0.0879 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 31.95 | 0.8508 | 0.1413 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 32.14 | 0.8468 | 0.1304 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 32.27 | 0.8512 | 0.1324 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 32.19 | 0.8491 | 0.1311 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.80 | 0.8496 | 0.1396 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.13 | 0.8457 | 0.1280 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 32.18 | 0.8502 | 0.1295 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 32.19 | 0.8483 | 0.1278 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 32.54 | 0.8410 | 0.0931 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 32.59 | 0.8489 | 0.0945 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 31.81 | 0.8374 | 0.0895 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 32.17 | 0.8459 | 0.1007 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 31.50 | 0.8363 | 0.0950 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 32.42 | 0.8457 | 0.0963 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 32.59 | 0.8495 | 0.0984 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.87 | 0.8375 | 0.0891 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 32.34 | 0.8476 | 0.1025 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 31.69 | 0.8362 | 0.0946 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 31.32 | 0.8467 | 0.1070 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 31.82 | 0.8495 | 0.1383 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 32.04 | 0.8459 | 0.1272 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 32.15 | 0.8500 | 0.1293 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 32.07 | 0.8480 | 0.1278 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.73 | 0.8489 | 0.1364 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 32.03 | 0.8452 | 0.1251 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 32.08 | 0.8493 | 0.1269 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 32.08 | 0.8474 | 0.1250 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 31.21 | 0.8455 | 0.1082 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.97 | 0.8355 | 0.1026 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 30.99 | 0.8353 | 0.1021 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 30.93 | 0.8354 | 0.1021 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 30.94 | 0.8353 | 0.1016 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 31.04 | 0.8354 | 0.1007 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.09 | 0.8348 | 0.0994 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.08 | 0.8355 | 0.0988 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.08 | 0.8352 | 0.0988 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 3.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.51 | 0.6267 | 0.0185 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 13.00 | 0.6405 | 0.0468 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 13.18 | 0.6573 | 0.0436 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 13.11 | 0.6623 | 0.0444 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 13.11 | 0.6533 | 0.0445 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 13.08 | 0.6427 | 0.0466 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.77 | 0.6636 | 0.0418 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 13.35 | 0.6608 | 0.0437 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 13.48 | 0.6602 | 0.0429 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 21.19 | 0.7337 | 0.0189 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 21.80 | 0.7109 | 0.0243 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 21.80 | 0.7109 | 0.0243 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 21.89 | 0.6979 | 0.0230 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 21.89 | 0.6979 | 0.0230 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 16.64 | 0.6635 | 0.0320 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 17.05 | 0.6454 | 0.0405 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 17.05 | 0.6454 | 0.0405 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 16.94 | 0.6291 | 0.0423 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 16.94 | 0.6291 | 0.0423 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 16.22 | 0.6229 | 0.0400 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 13.76 | 0.6233 | 0.0509 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 13.91 | 0.6358 | 0.0479 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 13.94 | 0.6429 | 0.0487 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 13.87 | 0.6336 | 0.0488 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 13.65 | 0.6227 | 0.0516 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 13.90 | 0.6360 | 0.0479 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 13.89 | 0.6411 | 0.0489 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 13.91 | 0.6368 | 0.0483 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.54 | 0.5602 | 0.0508 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.19 | 0.3917 | 0.1095 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.38 | 0.3847 | 0.1055 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.20 | 0.3833 | 0.1088 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.26 | 0.3769 | 0.1078 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.25 | 0.3923 | 0.1097 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.44 | 0.4148 | 0.1056 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.29 | 0.4043 | 0.1084 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.33 | 0.4047 | 0.1075 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.60 | 0.7218 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.10 | 0.7259 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.38 | 0.7392 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.13 | 0.7279 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.92 | 0.7323 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.21 | 0.7357 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.44 | 0.7432 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.33 | 0.7385 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.44 | 0.7539 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 23.99 | 0.7352 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 22.50 | 0.6829 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 23.63 | 0.7255 | 0.0184 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 22.27 | 0.6752 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.91 | 0.7376 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.71 | 0.7249 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.35 | 0.6834 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 23.44 | 0.7171 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.25 | 0.6805 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 22.68 | 0.7129 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 22.28 | 0.7059 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.71 | 0.7072 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.08 | 0.7224 | 0.0162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.79 | 0.7103 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.82 | 0.7237 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.93 | 0.7205 | 0.0159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.23 | 0.7291 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.07 | 0.7230 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 22.50 | 0.7022 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.66 | 0.6365 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.51 | 0.6371 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.81 | 0.6451 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.73 | 0.6405 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.85 | 0.6482 | 0.0190 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.78 | 0.6497 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.88 | 0.6505 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.79 | 0.6495 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.57 | 0.7189 | 0.0180 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.11 | 0.7242 | 0.0158 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.36 | 0.7376 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.12 | 0.7258 | 0.0164 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.90 | 0.7295 | 0.0172 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.19 | 0.7343 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.43 | 0.7416 | 0.0160 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.32 | 0.7363 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.45 | 0.7533 | 0.0139 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 23.99 | 0.7317 | 0.0179 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 22.49 | 0.6799 | 0.0184 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 23.62 | 0.7210 | 0.0184 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 22.27 | 0.6716 | 0.0194 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.93 | 0.7371 | 0.0134 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.71 | 0.7230 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.34 | 0.6820 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 23.44 | 0.7141 | 0.0178 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.24 | 0.6785 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.69 | 0.7087 | 0.0184 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.27 | 0.7026 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.74 | 0.7059 | 0.0160 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.08 | 0.7203 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.80 | 0.7071 | 0.0164 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.82 | 0.7214 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.93 | 0.7192 | 0.0157 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.24 | 0.7274 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.08 | 0.7203 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.51 | 0.6978 | 0.0180 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.66 | 0.6356 | 0.0197 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.49 | 0.6362 | 0.0194 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.80 | 0.6438 | 0.0189 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.71 | 0.6394 | 0.0191 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.83 | 0.6462 | 0.0192 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.77 | 0.6482 | 0.0187 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.89 | 0.6493 | 0.0188 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.78 | 0.6483 | 0.0187 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 60.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.14 | 0.8235 | 0.0440 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.60 | 0.6682 | 0.3299 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.96 | 0.6701 | 0.3148 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.70 | 0.6754 | 0.3195 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.79 | 0.6719 | 0.3176 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.66 | 0.6680 | 0.3296 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.10 | 0.6708 | 0.3103 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.80 | 0.6765 | 0.3170 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.91 | 0.6733 | 0.3132 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 21.80 | 0.7800 | 0.1478 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 21.60 | 0.7820 | 0.1744 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 21.60 | 0.7820 | 0.1744 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 22.16 | 0.7808 | 0.1672 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 22.16 | 0.7808 | 0.1672 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.92 | 0.5416 | 0.2489 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.58 | 0.5064 | 0.2875 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.58 | 0.5064 | 0.2875 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.63 | 0.5032 | 0.2877 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.63 | 0.5032 | 0.2877 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.62 | 0.4831 | 0.2898 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.31 | 0.6849 | 0.3028 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.70 | 0.6911 | 0.2824 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.43 | 0.6945 | 0.2899 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.53 | 0.6923 | 0.2870 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.36 | 0.6824 | 0.3033 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.81 | 0.6902 | 0.2803 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.53 | 0.6944 | 0.2876 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.64 | 0.6923 | 0.2831 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.59 | 0.5121 | 0.2764 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.34 | 0.5806 | 0.4133 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.65 | 0.5836 | 0.4029 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.41 | 0.5865 | 0.4086 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.49 | 0.5851 | 0.4064 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.31 | 0.5740 | 0.4150 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.57 | 0.5693 | 0.4060 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.37 | 0.5795 | 0.4092 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.43 | 0.5751 | 0.4078 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.95 | 0.8319 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.51 | 0.8349 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.48 | 0.8354 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.47 | 0.8349 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.14 | 0.8333 | 0.0479 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.55 | 0.8355 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.55 | 0.8359 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.55 | 0.8356 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 30.13 | 0.8333 | 0.0452 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 30.42 | 0.8318 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 30.04 | 0.8287 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 30.19 | 0.8303 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.84 | 0.8273 | 0.0474 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.98 | 0.8333 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.44 | 0.8321 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 30.06 | 0.8289 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 30.26 | 0.8308 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.93 | 0.8280 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.98 | 0.8299 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.84 | 0.8307 | 0.0493 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.37 | 0.8333 | 0.0474 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.37 | 0.8341 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.33 | 0.8334 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.09 | 0.8324 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.48 | 0.8346 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.49 | 0.8348 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.47 | 0.8345 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.91 | 0.8292 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.25 | 0.8244 | 0.0456 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.14 | 0.8251 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.33 | 0.8254 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.28 | 0.8252 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.28 | 0.8250 | 0.0459 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.17 | 0.8245 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.29 | 0.8252 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.21 | 0.8248 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.53 | 0.8337 | 0.0788 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.57 | 0.8346 | 0.0721 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.40 | 0.8385 | 0.0730 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.45 | 0.8364 | 0.0727 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.61 | 0.8318 | 0.0782 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.51 | 0.8336 | 0.0699 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.34 | 0.8367 | 0.0714 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.41 | 0.8352 | 0.0696 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 30.05 | 0.8259 | 0.0513 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.32 | 0.8318 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.79 | 0.8216 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.95 | 0.8275 | 0.0589 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.52 | 0.8200 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.75 | 0.8313 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.57 | 0.8325 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.02 | 0.8211 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.36 | 0.8296 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.87 | 0.8193 | 0.0514 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.08 | 0.8178 | 0.0703 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.06 | 0.8286 | 0.0837 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.20 | 0.8307 | 0.0752 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.05 | 0.8346 | 0.0766 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.08 | 0.8321 | 0.0764 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.35 | 0.8281 | 0.0822 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.41 | 0.8305 | 0.0724 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.24 | 0.8344 | 0.0741 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.31 | 0.8327 | 0.0722 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.45 | 0.8115 | 0.0806 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.14 | 0.8061 | 0.0616 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.64 | 0.8024 | 0.0636 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.15 | 0.8093 | 0.0610 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.02 | 0.8072 | 0.0609 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.21 | 0.8085 | 0.0601 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.94 | 0.8026 | 0.0646 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.29 | 0.8099 | 0.0603 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.12 | 0.8077 | 0.0605 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.45 | 0.8181 | 0.0515 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.69 | 0.6829 | 0.3827 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.90 | 0.6813 | 0.3660 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.77 | 0.6863 | 0.3749 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.83 | 0.6836 | 0.3709 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.73 | 0.6808 | 0.3824 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.10 | 0.6786 | 0.3633 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.87 | 0.6845 | 0.3718 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.96 | 0.6816 | 0.3673 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 22.43 | 0.7895 | 0.1657 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 22.44 | 0.7930 | 0.1860 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 22.44 | 0.7930 | 0.1860 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 23.06 | 0.7889 | 0.1830 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 23.06 | 0.7889 | 0.1830 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.93 | 0.5555 | 0.3044 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.00 | 0.5509 | 0.3247 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.00 | 0.5509 | 0.3247 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.12 | 0.5460 | 0.3275 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.12 | 0.5460 | 0.3275 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.91 | 0.5393 | 0.3258 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.22 | 0.6859 | 0.3764 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.48 | 0.6859 | 0.3593 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.33 | 0.6898 | 0.3682 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.39 | 0.6876 | 0.3643 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.24 | 0.6833 | 0.3771 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.56 | 0.6819 | 0.3579 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.40 | 0.6879 | 0.3666 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.48 | 0.6849 | 0.3621 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.96 | 0.5212 | 0.3312 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.85 | 0.5747 | 0.4915 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.97 | 0.5749 | 0.4813 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.88 | 0.5740 | 0.4887 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.91 | 0.5736 | 0.4859 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.87 | 0.5705 | 0.4946 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.98 | 0.5658 | 0.4855 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.89 | 0.5713 | 0.4910 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.92 | 0.5686 | 0.4887 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 30.47 | 0.8267 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.78 | 0.8279 | 0.0502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.83 | 0.8287 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.77 | 0.8278 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.61 | 0.8278 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.80 | 0.8286 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.86 | 0.8291 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.84 | 0.8288 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 30.73 | 0.8300 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 31.02 | 0.8285 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 30.50 | 0.8250 | 0.0517 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 30.82 | 0.8274 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 30.35 | 0.8239 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 30.55 | 0.8297 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.94 | 0.8288 | 0.0508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 30.46 | 0.8254 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 30.76 | 0.8275 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 30.34 | 0.8245 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.30 | 0.8268 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 30.35 | 0.8261 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.64 | 0.8270 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.72 | 0.8281 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.64 | 0.8271 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.57 | 0.8275 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.70 | 0.8281 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.78 | 0.8286 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.74 | 0.8282 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 30.24 | 0.8263 | 0.0519 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.54 | 0.8189 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.46 | 0.8189 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.61 | 0.8194 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.56 | 0.8190 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.60 | 0.8195 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.56 | 0.8193 | 0.0519 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.61 | 0.8196 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.56 | 0.8195 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.91 | 0.8360 | 0.0773 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.43 | 0.8334 | 0.0693 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.42 | 0.8379 | 0.0725 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.36 | 0.8352 | 0.0713 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.88 | 0.8357 | 0.0767 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.25 | 0.8321 | 0.0687 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.30 | 0.8370 | 0.0703 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.30 | 0.8346 | 0.0690 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 30.90 | 0.8297 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 30.97 | 0.8361 | 0.0575 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 30.23 | 0.8231 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 30.54 | 0.8322 | 0.0599 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.93 | 0.8209 | 0.0564 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 30.63 | 0.8353 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.94 | 0.8375 | 0.0568 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 30.24 | 0.8236 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 30.62 | 0.8347 | 0.0594 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 30.01 | 0.8216 | 0.0554 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.76 | 0.8338 | 0.0603 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.77 | 0.8337 | 0.0766 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.27 | 0.8320 | 0.0692 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.26 | 0.8361 | 0.0723 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.18 | 0.8334 | 0.0711 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.87 | 0.8342 | 0.0759 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.16 | 0.8311 | 0.0684 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.27 | 0.8362 | 0.0704 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.23 | 0.8335 | 0.0690 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.71 | 0.8328 | 0.0600 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.24 | 0.8185 | 0.0622 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.15 | 0.8177 | 0.0611 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.17 | 0.8182 | 0.0614 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.11 | 0.8176 | 0.0612 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.18 | 0.8176 | 0.0634 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.17 | 0.8151 | 0.0624 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.20 | 0.8173 | 0.0629 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.14 | 0.8163 | 0.0623 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 50.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 32.23 | 0.8147 | 0.0371 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.44 | 0.5984 | 0.3439 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.60 | 0.6000 | 0.3367 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.50 | 0.6040 | 0.3405 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.54 | 0.6031 | 0.3388 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.51 | 0.5967 | 0.3441 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.84 | 0.5990 | 0.3373 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.64 | 0.6028 | 0.3400 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.72 | 0.6019 | 0.3383 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 21.53 | 0.7768 | 0.1535 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 21.11 | 0.7670 | 0.1677 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 21.11 | 0.7670 | 0.1677 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 21.27 | 0.7628 | 0.1706 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 21.27 | 0.7628 | 0.1706 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.20 | 0.3756 | 0.2877 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.28 | 0.3734 | 0.2943 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.28 | 0.3734 | 0.2943 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.38 | 0.3718 | 0.2964 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.38 | 0.3718 | 0.2964 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.07 | 0.3546 | 0.2949 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.64 | 0.5990 | 0.3449 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.82 | 0.6042 | 0.3367 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.71 | 0.6068 | 0.3406 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.75 | 0.6064 | 0.3387 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.71 | 0.5965 | 0.3458 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.96 | 0.6006 | 0.3382 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.83 | 0.6050 | 0.3412 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.89 | 0.6039 | 0.3391 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 10.76 | 0.3285 | 0.3109 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.08 | 0.5270 | 0.4090 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.18 | 0.5285 | 0.4018 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.11 | 0.5287 | 0.4077 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.14 | 0.5289 | 0.4050 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.06 | 0.5256 | 0.4102 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.15 | 0.5260 | 0.4018 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.08 | 0.5282 | 0.4080 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.11 | 0.5274 | 0.4053 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 32.23 | 0.8147 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 32.23 | 0.8147 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 32.23 | 0.8147 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 32.23 | 0.8147 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 32.23 | 0.8146 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.24 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 32.25 | 0.8149 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 32.25 | 0.8149 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 32.25 | 0.8148 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 32.24 | 0.8149 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 32.24 | 0.8149 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 32.25 | 0.8149 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 32.24 | 0.8148 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 32.22 | 0.8146 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 32.24 | 0.8147 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 32.23 | 0.8147 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 32.23 | 0.8147 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 32.22 | 0.8146 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 32.23 | 0.8146 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 32.23 | 0.8146 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 32.23 | 0.8146 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 32.24 | 0.8149 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 32.23 | 0.8147 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 32.23 | 0.8146 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 32.23 | 0.8147 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 32.23 | 0.8146 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 32.23 | 0.8147 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 32.03 | 0.8154 | 0.0448 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 32.08 | 0.8152 | 0.0435 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 32.04 | 0.8158 | 0.0441 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 32.06 | 0.8156 | 0.0438 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.99 | 0.8151 | 0.0449 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.03 | 0.8141 | 0.0434 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 32.06 | 0.8157 | 0.0434 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 32.07 | 0.8153 | 0.0430 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 32.41 | 0.8168 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 32.21 | 0.8146 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 32.16 | 0.8143 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 31.99 | 0.8132 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 31.95 | 0.8132 | 0.0408 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 32.28 | 0.8169 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 32.29 | 0.8161 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 32.21 | 0.8144 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 32.24 | 0.8154 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 32.14 | 0.8135 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 31.88 | 0.8151 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 31.74 | 0.8124 | 0.0448 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 32.03 | 0.8139 | 0.0427 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.89 | 0.8143 | 0.0437 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.96 | 0.8141 | 0.0431 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.75 | 0.8122 | 0.0451 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.88 | 0.8126 | 0.0435 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.90 | 0.8141 | 0.0438 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.91 | 0.8136 | 0.0432 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 31.87 | 0.8138 | 0.0396 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 32.11 | 0.8150 | 0.0415 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 32.09 | 0.8148 | 0.0418 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 32.06 | 0.8145 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 32.07 | 0.8146 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 32.11 | 0.8145 | 0.0413 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 32.15 | 0.8147 | 0.0410 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 32.14 | 0.8147 | 0.0410 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 32.15 | 0.8147 | 0.0410 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.70 | 0.8223 | 0.0739 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.59 | 0.6722 | 0.4519 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.76 | 0.6680 | 0.4347 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.66 | 0.6742 | 0.4405 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.70 | 0.6712 | 0.4379 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.67 | 0.6713 | 0.4522 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.97 | 0.6669 | 0.4347 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.78 | 0.6738 | 0.4386 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.86 | 0.6708 | 0.4357 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 23.01 | 0.8097 | 0.2130 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 22.74 | 0.8125 | 0.2389 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 22.74 | 0.8125 | 0.2389 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 22.98 | 0.8081 | 0.2429 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 22.98 | 0.8081 | 0.2429 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.88 | 0.4832 | 0.3580 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.83 | 0.4769 | 0.3798 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.83 | 0.4769 | 0.3798 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.90 | 0.4740 | 0.3843 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.90 | 0.4740 | 0.3843 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.76 | 0.4653 | 0.3778 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.78 | 0.6723 | 0.4499 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.95 | 0.6700 | 0.4323 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.85 | 0.6752 | 0.4385 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.90 | 0.6727 | 0.4357 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.85 | 0.6712 | 0.4508 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.10 | 0.6679 | 0.4323 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.96 | 0.6747 | 0.4374 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.03 | 0.6718 | 0.4341 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.56 | 0.4423 | 0.3884 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.34 | 0.5755 | 0.5583 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.43 | 0.5741 | 0.5471 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.36 | 0.5753 | 0.5542 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.39 | 0.5746 | 0.5509 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.33 | 0.5730 | 0.5593 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.41 | 0.5682 | 0.5487 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.35 | 0.5737 | 0.5546 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.37 | 0.5712 | 0.5518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 31.42 | 0.8268 | 0.0765 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.64 | 0.8274 | 0.0734 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.67 | 0.8279 | 0.0746 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.63 | 0.8274 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.52 | 0.8273 | 0.0761 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.66 | 0.8279 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.70 | 0.8281 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.68 | 0.8280 | 0.0740 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 31.59 | 0.8287 | 0.0713 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 31.80 | 0.8279 | 0.0755 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 31.46 | 0.8259 | 0.0743 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 31.67 | 0.8273 | 0.0758 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 31.36 | 0.8254 | 0.0752 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 31.47 | 0.8285 | 0.0704 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.75 | 0.8280 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.43 | 0.8261 | 0.0733 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 31.63 | 0.8273 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 31.35 | 0.8257 | 0.0743 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 31.34 | 0.8270 | 0.0750 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 31.36 | 0.8265 | 0.0755 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.55 | 0.8270 | 0.0733 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.61 | 0.8276 | 0.0739 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.56 | 0.8270 | 0.0739 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.50 | 0.8273 | 0.0751 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.59 | 0.8276 | 0.0732 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.65 | 0.8278 | 0.0740 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.62 | 0.8276 | 0.0737 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 31.29 | 0.8267 | 0.0746 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.77 | 0.8227 | 0.0753 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 30.71 | 0.8227 | 0.0747 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 30.81 | 0.8229 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 30.78 | 0.8227 | 0.0745 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 30.80 | 0.8230 | 0.0748 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.78 | 0.8229 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.81 | 0.8231 | 0.0746 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.78 | 0.8230 | 0.0745 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 31.09 | 0.8354 | 0.1125 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.48 | 0.8330 | 0.1028 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.47 | 0.8364 | 0.1057 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.43 | 0.8345 | 0.1046 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.06 | 0.8351 | 0.1119 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.35 | 0.8321 | 0.1016 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.40 | 0.8359 | 0.1031 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.40 | 0.8341 | 0.1016 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 31.78 | 0.8299 | 0.0750 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 31.86 | 0.8343 | 0.0823 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 31.26 | 0.8248 | 0.0758 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 31.51 | 0.8313 | 0.0853 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 31.00 | 0.8234 | 0.0795 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 31.60 | 0.8336 | 0.0769 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.85 | 0.8357 | 0.0821 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.28 | 0.8251 | 0.0749 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 31.62 | 0.8339 | 0.0849 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 31.10 | 0.8238 | 0.0786 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 31.02 | 0.8340 | 0.0863 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 30.99 | 0.8339 | 0.1119 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.38 | 0.8322 | 0.1022 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.37 | 0.8352 | 0.1054 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.32 | 0.8334 | 0.1040 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.06 | 0.8341 | 0.1113 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.29 | 0.8315 | 0.1010 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.38 | 0.8354 | 0.1031 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.35 | 0.8335 | 0.1013 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.98 | 0.8334 | 0.0856 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.50 | 0.8223 | 0.0881 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 30.44 | 0.8219 | 0.0871 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 30.44 | 0.8222 | 0.0876 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 30.40 | 0.8218 | 0.0874 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 30.48 | 0.8218 | 0.0885 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.48 | 0.8204 | 0.0876 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.50 | 0.8217 | 0.0878 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.47 | 0.8211 | 0.0871 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1133 | None | classic | 1.92 | False | 193616 | 0.171 | 39.5 | 33.15 | 0.62 | 0.013 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1133 | None | classic | 1.92 | False | 193616 | 0.171 | 37.6 | 33.15 | 0.62 | 0.013 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1133 | None | classic | 1.92 | False | 193616 | 0.171 | 37.0 | 33.15 | 0.62 | 0.013 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1133 | None | classic | 1.92 | False | 193616 | 0.171 | 34.5 | 33.15 | 0.62 | 0.013 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1101 | None | classic | 1.81 | False | 189767 | 0.177 | 35.4 | 32.31 | 0.28 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1101 | None | classic | 1.81 | False | 189767 | 0.177 | 33.5 | 32.31 | 0.28 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1101 | None | classic | 1.81 | False | 189767 | 0.177 | 34.3 | 32.31 | 0.28 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1101 | None | classic | 1.81 | False | 189767 | 0.177 | 34.9 | 32.31 | 0.28 | 0.006 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1596720 | 0.144 | 30.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1596720 | 0.794 | 56.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1596720 | 0.794 | 56.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1596720 | 0.677 | 30.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1596720 | 0.677 | 30.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1596720 | 0.144 | 38.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1596720 | 0.794 | 81.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1596720 | 0.794 | 81.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1596720 | 0.677 | 38.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1596720 | 0.677 | 38.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1585446 | 0.794 | 165.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1133 | None | classic | 1.92 | False | 193616 | 0.177 | 38.0 | 33.15 | 0.62 | 0.013 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1133 | None | classic | 1.92 | False | 193616 | 0.177 | 42.4 | 33.15 | 0.62 | 0.013 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1133 | None | classic | 1.92 | False | 193616 | 0.177 | 47.0 | 33.15 | 0.62 | 0.013 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1133 | None | classic | 1.92 | False | 193616 | 0.177 | 34.0 | 33.15 | 0.62 | 0.013 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1101 | None | classic | 1.81 | False | 189767 | 0.173 | 31.5 | 32.31 | 0.28 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1101 | None | classic | 1.81 | False | 189767 | 0.173 | 33.4 | 32.31 | 0.28 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1101 | None | classic | 1.81 | False | 189767 | 0.173 | 35.5 | 32.31 | 0.28 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1101 | None | classic | 1.81 | False | 189767 | 0.173 | 37.3 | 32.31 | 0.28 | 0.006 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1697378 | 0.794 | 77.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1015 | None | classic | 1.54 | False | 181293 | 0.322 | 44.5 | 31.82 | 0.55 | 0.015 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1015 | None | classic | 1.54 | False | 181293 | 0.322 | 33.6 | 31.82 | 0.55 | 0.015 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1015 | None | classic | 1.54 | False | 181293 | 0.322 | 30.4 | 31.82 | 0.55 | 0.015 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1015 | None | classic | 1.54 | False | 181293 | 0.322 | 29.0 | 31.82 | 0.55 | 0.015 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 890 | None | classic | 1.18 | False | 305414 | 0.348 | 58.3 | 31.59 | 0.39 | 0.018 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 890 | None | classic | 1.18 | False | 305414 | 0.348 | 56.2 | 31.59 | 0.39 | 0.018 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 890 | None | classic | 1.18 | False | 305414 | 0.348 | 57.3 | 31.59 | 0.39 | 0.018 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 890 | None | classic | 1.18 | False | 305414 | 0.348 | 56.2 | 31.59 | 0.39 | 0.018 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.734 | 0.014 |
| in035 | mask_ent | 0.808 | 0.014 |
| in035 | mask_grad | 0.408 | 0.014 |
| in035 | r_col | 0.684 | 0.014 |
| in035 | r_warp | 0.860 | 0.014 |

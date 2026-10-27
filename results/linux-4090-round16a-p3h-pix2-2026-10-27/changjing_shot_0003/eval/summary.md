# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 8.8% | 23.28 / 0.0368 | 23.37 / 0.0572 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.1% | 23.40 / 0.0369 | 24.28 / 0.0476 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.9% | 23.33 / 0.0364 | 24.48 / 0.0510 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.0% | 23.33 / 0.0365 | 24.41 / 0.0481 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.8% | 23.24 / 0.0356 | 23.80 / 0.0540 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.1% | 23.31 / 0.0370 | 24.94 / 0.0424 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.0% | 23.30 / 0.0362 | 24.83 / 0.0477 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.1% | 23.32 / 0.0365 | 24.91 / 0.0447 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 8.1% | 22.55 / 0.0392 | 20.91 / 0.0977 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 7.2% | 22.55 / 0.0373 | 24.28 / 0.0664 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.2% | 18.39 / 0.0309 | 20.81 / 0.0464 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 7.2% | 22.58 / 0.0366 | 23.64 / 0.0668 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.3% | 18.55 / 0.0310 | 20.16 / 0.0461 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 8.2% | 22.56 / 0.0396 | 21.28 / 0.0698 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 7.1% | 22.53 / 0.0364 | 23.97 / 0.0635 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.5% | 18.91 / 0.0307 | 20.90 / 0.0495 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 7.2% | 22.56 / 0.0363 | 23.49 / 0.0649 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.6% | 18.91 / 0.0327 | 20.20 / 0.0536 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 9.2% | 23.25 / 0.0385 | 22.84 / 0.0818 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 12.8% | 24.16 / 0.0261 | 22.72 / 0.0586 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 13.2% | 24.23 / 0.0270 | 24.80 / 0.0418 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 13.2% | 24.22 / 0.0270 | 24.40 / 0.0497 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 13.2% | 24.23 / 0.0270 | 24.67 / 0.0453 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 13.1% | 24.22 / 0.0263 | 23.71 / 0.0554 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 13.6% | 24.32 / 0.0275 | 25.61 / 0.0412 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 13.5% | 24.29 / 0.0271 | 25.26 / 0.0478 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 13.5% | 24.31 / 0.0269 | 25.47 / 0.0435 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 12.9% | 24.12 / 0.0274 | 23.43 / 0.0628 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 9.4% | 23.98 / 0.0292 | 22.81 / 0.0673 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 10.7% | 24.40 / 0.0293 | 24.63 / 0.0555 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 10.1% | 24.23 / 0.0293 | 24.40 / 0.0587 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 10.4% | 24.32 / 0.0297 | 24.74 / 0.0569 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 9.4% | 23.98 / 0.0292 | 22.81 / 0.0673 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 10.7% | 24.40 / 0.0293 | 24.63 / 0.0554 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 10.1% | 24.23 / 0.0293 | 24.40 / 0.0587 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 10.4% | 24.32 / 0.0297 | 24.75 / 0.0569 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.80 / 0.0823 | 33.66 / 0.0298 | 18.96 / 0.0235 | 29.29 / 0.0447 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.72 / 0.0945 | 32.38 / 0.0614 | 19.76 / 0.0216 | 29.27 / 0.0462 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.82 / 0.0911 | 31.90 / 0.0598 | 19.95 / 0.0202 | 29.28 / 0.0458 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.92 / 0.0923 | 32.95 / 0.0511 | 20.08 / 0.0203 | 29.29 / 0.0458 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.87 / 0.0914 | 32.69 / 0.0522 | 20.00 / 0.0199 | 29.28 / 0.0457 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.90 / 0.0930 | 32.69 / 0.0550 | 20.15 / 0.0201 | 29.28 / 0.0464 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.05 / 0.0883 | 33.19 / 0.0457 | 20.49 / 0.0187 | 29.29 / 0.0457 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.05 / 0.0905 | 33.12 / 0.0474 | 20.41 / 0.0190 | 29.30 / 0.0459 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.05 / 0.0894 | 32.82 / 0.0493 | 20.47 / 0.0187 | 29.29 / 0.0457 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.38 / 0.1046 | 32.46 / 0.1027 | 18.37 / 0.0361 | 29.30 / 0.0447 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.28 / 0.0946 | 33.74 / 0.0537 | 21.08 / 0.0267 | 29.24 / 0.0467 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.27 / 0.0882 | 33.50 / 0.0361 | 20.92 / 0.0257 | 29.23 / 0.0467 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.15 / 0.0943 | 33.54 / 0.0575 | 21.00 / 0.0246 | 29.24 / 0.0466 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.17 / 0.0881 | 33.53 / 0.0354 | 20.91 / 0.0240 | 29.23 / 0.0465 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.49 / 0.0939 | 32.75 / 0.0632 | 18.51 / 0.0297 | 29.30 / 0.0448 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.17 / 0.0944 | 33.28 / 0.0593 | 20.82 / 0.0258 | 29.24 / 0.0467 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.18 / 0.0893 | 33.52 / 0.0364 | 20.71 / 0.0253 | 29.23 / 0.0466 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.07 / 0.0951 | 32.91 / 0.0657 | 20.85 / 0.0246 | 29.25 / 0.0465 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.09 / 0.0902 | 33.52 / 0.0377 | 20.77 / 0.0241 | 29.24 / 0.0464 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.75 / 0.0985 | 29.91 / 0.0975 | 19.92 / 0.0276 | 29.15 / 0.0479 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.13 / 0.1072 | 32.25 / 0.0597 | 19.02 / 0.0259 | 29.19 / 0.0514 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.80 / 0.0975 | 33.26 / 0.0481 | 20.16 / 0.0216 | 29.23 / 0.0487 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.74 / 0.1017 | 33.27 / 0.0490 | 19.82 / 0.0232 | 29.26 / 0.0499 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.79 / 0.0996 | 33.29 / 0.0462 | 20.00 / 0.0225 | 29.25 / 0.0492 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.52 / 0.1051 | 32.54 / 0.0564 | 19.72 / 0.0235 | 29.23 / 0.0509 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.01 / 0.0962 | 33.32 / 0.0481 | 20.63 / 0.0204 | 29.29 / 0.0483 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.97 / 0.1001 | 33.65 / 0.0459 | 20.39 / 0.0210 | 29.30 / 0.0495 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.00 / 0.0979 | 33.62 / 0.0454 | 20.53 / 0.0206 | 29.30 / 0.0488 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.75 / 0.1012 | 30.00 / 0.1000 | 19.99 / 0.0279 | 29.18 / 0.0487 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.36 / 0.0989 | 31.14 / 0.0654 | 19.45 / 0.0199 | 29.21 / 0.0480 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.82 / 0.0940 | 32.98 / 0.0491 | 20.34 / 0.0178 | 29.27 / 0.0467 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.74 / 0.0959 | 32.73 / 0.0546 | 20.03 / 0.0186 | 29.26 / 0.0474 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.79 / 0.0949 | 32.83 / 0.0517 | 20.21 / 0.0181 | 29.27 / 0.0469 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.36 / 0.0989 | 31.14 / 0.0654 | 19.45 / 0.0199 | 29.21 / 0.0480 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.82 / 0.0940 | 32.97 / 0.0492 | 20.34 / 0.0178 | 29.27 / 0.0467 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.74 / 0.0959 | 32.73 / 0.0546 | 20.03 / 0.0186 | 29.26 / 0.0474 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.79 / 0.0949 | 32.83 / 0.0517 | 20.21 / 0.0181 | 29.27 / 0.0469 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.7%） | — | — | 27.80 / 0.0823 | 33.66 / 0.0298 | 29.29 |
| in035 | rife | 5.4% | 9.4% | 27.36 / 0.0989 | 31.14 / 0.0654 | 29.21 |
| in035 | cnw_cnn | 5.7% | 8.8% | 27.72 / 0.0945 | 32.38 / 0.0614 | 29.27 |
| in035 | cnw_f5 | 8.7% | 12.8% | 27.13 / 0.1072 | 32.25 / 0.0597 | 29.19 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.87 / 0.0834 | -0.40 / +0.0193 (core 5.3%) | +0.07 / +0.0118 (core 5.5%) | -0.59 / +0.0254 (core 8.1%) |
| in035 | 2 | 0-3 | 28.08 / 0.0845 | -0.91 / +0.0210 (core 5.3%) | -0.43 / +0.0164 (core 5.5%) | -1.03 / +0.0289 (core 8.1%) |
| in035 | 4 | 3-5 | 28.46 / 0.0791 | -0.00 / +0.0095 (core 3.3%) | +0.10 / +0.0083 (core 3.6%) | -0.41 / +0.0204 (core 6.2%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.80 / 0.0823 | 33.66 | 29.29 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.72 / 0.0945 | 32.38 | 29.27 | 0/3 |
| in035 | cnw_cnn | oracle | 1.9% | 27.99 / 0.0826 | 33.59 | 29.29 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.82 / 0.0911 | 31.90 | 29.28 | 0/3 |
| in035 | cnw_cnn | oracle | 1.9% | 28.07 / 0.0814 | 33.65 | 29.29 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.92 / 0.0923 | 32.95 | 29.29 | 0/3 |
| in035 | cnw_cnn | oracle | 1.9% | 28.11 / 0.0815 | 33.67 | 29.29 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.87 / 0.0914 | 32.69 | 29.28 | 0/3 |
| in035 | cnw_cnn | oracle | 1.9% | 28.09 / 0.0812 | 33.66 | 29.29 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.90 / 0.0930 | 32.69 | 29.28 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.9% | 28.13 / 0.0815 | 33.66 | 29.29 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.05 / 0.0883 | 33.19 | 29.29 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 28.24 / 0.0800 | 33.61 | 29.29 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.05 / 0.0905 | 33.12 | 29.30 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.9% | 28.22 / 0.0806 | 33.71 | 29.29 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.05 / 0.0894 | 32.82 | 29.29 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.9% | 28.24 / 0.0804 | 33.65 | 29.29 | 3/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 27.38 / 0.1046 | 32.46 | 29.30 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 2.0% | 27.54 / 0.0953 | 33.60 | 29.29 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 28.28 / 0.0946 | 33.74 | 29.24 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 1.8% | 28.41 / 0.0856 | 33.59 | 29.29 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 28.27 / 0.0882 | 33.50 | 29.23 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 1.3% | 28.37 / 0.0845 | 33.66 | 29.29 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 28.15 / 0.0943 | 33.54 | 29.24 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 1.8% | 28.38 / 0.0843 | 33.50 | 29.29 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 28.17 / 0.0881 | 33.53 | 29.23 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 1.3% | 28.36 / 0.0834 | 33.66 | 29.29 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.49 / 0.0939 | 32.75 | 29.30 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 2.0% | 27.60 / 0.0882 | 33.60 | 29.29 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.17 / 0.0944 | 33.28 | 29.24 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.8% | 28.34 / 0.0847 | 33.60 | 29.29 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.18 / 0.0893 | 33.52 | 29.23 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.3% | 28.31 / 0.0840 | 33.66 | 29.29 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 28.07 / 0.0951 | 32.91 | 29.25 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 1.8% | 28.34 / 0.0841 | 33.32 | 29.29 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 28.09 / 0.0902 | 33.52 | 29.24 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 1.3% | 28.32 / 0.0836 | 33.66 | 29.29 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.75 / 0.0985 | 29.91 | 29.15 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.0% | 28.08 / 0.0865 | 33.41 | 29.29 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.13 / 0.1072 | 32.25 | 29.19 | 0/3 |
| in035 | cnw_f5 | oracle | 2.2% | 27.64 / 0.0865 | 32.93 | 29.28 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.80 / 0.0975 | 33.26 | 29.23 | 0/3 |
| in035 | cnw_f5 | oracle | 2.3% | 28.08 / 0.0826 | 33.92 | 29.29 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.74 / 0.1017 | 33.27 | 29.26 | 0/3 |
| in035 | cnw_f5 | oracle | 2.3% | 27.96 / 0.0842 | 33.54 | 29.29 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.79 / 0.0996 | 33.29 | 29.25 | 0/3 |
| in035 | cnw_f5 | oracle | 2.3% | 28.03 / 0.0836 | 33.67 | 29.29 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.52 / 0.1051 | 32.54 | 29.23 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.3% | 27.90 / 0.0851 | 33.17 | 29.28 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.01 / 0.0962 | 33.32 | 29.29 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.3% | 28.23 / 0.0817 | 33.87 | 29.29 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.97 / 0.1001 | 33.65 | 29.30 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.3% | 28.15 / 0.0830 | 33.62 | 29.29 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.00 / 0.0979 | 33.62 | 29.30 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.3% | 28.20 / 0.0823 | 33.69 | 29.29 | 2/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.75 / 0.1012 | 30.00 | 29.18 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.3% | 28.10 / 0.0865 | 33.55 | 29.29 | 0/3 |
| in035 | rife | 不复核 | —% | 27.36 / 0.0989 | 31.14 | 29.21 | 0/3 |
| in035 | rife | oracle | 1.8% | 27.86 / 0.0809 | 32.10 | 29.29 | 2/3 |
| in035 | rife | 不复核 | —% | 27.82 / 0.0940 | 32.98 | 29.27 | 0/3 |
| in035 | rife | oracle | 1.9% | 28.18 / 0.0788 | 33.36 | 29.29 | 3/3 |
| in035 | rife | 不复核 | —% | 27.74 / 0.0959 | 32.73 | 29.26 | 0/3 |
| in035 | rife | oracle | 1.8% | 28.10 / 0.0795 | 33.07 | 29.29 | 3/3 |
| in035 | rife | 不复核 | —% | 27.79 / 0.0949 | 32.83 | 29.27 | 0/3 |
| in035 | rife | oracle | 1.9% | 28.15 / 0.0790 | 33.22 | 29.29 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 27.36 / 0.0989 | 31.14 | 29.21 | 0/3 |
| in035 | rife_mw | oracle | 1.8% | 27.86 / 0.0809 | 32.10 | 29.29 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 27.82 / 0.0940 | 32.97 | 29.27 | 0/3 |
| in035 | rife_mw | oracle | 1.9% | 28.18 / 0.0788 | 33.36 | 29.29 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 27.74 / 0.0959 | 32.73 | 29.26 | 0/3 |
| in035 | rife_mw | oracle | 1.8% | 28.10 / 0.0795 | 33.07 | 29.29 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 27.79 / 0.0949 | 32.83 | 29.27 | 0/3 |
| in035 | rife_mw | oracle | 1.9% | 28.15 / 0.0790 | 33.22 | 29.29 | 3/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.80 / 0.0823 | 33.66 / 0.0298 | — |
| in035 | FF | 0（前馈） | 857×774（65%） | 28.05 | 27.72 / 0.0945 | 32.38 / 0.0614 | 0/3 |
| in035 | 25 | 0.54 s | 857×774（65%） | 28.89 | 27.92 / 0.0923 | 32.95 / 0.0511 | 0/3 |
| in035 | 50 | 1.06 s | 857×774（65%） | 29.22 | 27.87 / 0.0914 | 32.69 / 0.0522 | 0/3 |
| in035 | 100 | 2.07 s | 857×774（65%） | 29.52 | 27.82 / 0.0911 | 31.90 / 0.0598 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.80 / 0.0823 | 33.66 / 0.0298 | 29.29 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.72 / 0.0945 | 32.38 / 0.0614 | 29.27 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.99 / 0.0826 | 33.59 / 0.0312 | 29.29 | 2/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.92 / 0.0923 | 32.95 / 0.0511 | 29.29 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.11 / 0.0815 | 33.67 / 0.0313 | 29.29 | 2/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.87 / 0.0914 | 32.69 / 0.0522 | 29.28 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.09 / 0.0812 | 33.66 / 0.0309 | 29.29 | 2/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.82 / 0.0911 | 31.90 / 0.0598 | 29.28 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.07 / 0.0814 | 33.65 / 0.0309 | 29.29 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.90 / 0.0930 | 32.69 / 0.0550 | 29.28 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.13 / 0.0815 | 33.66 / 0.0309 | 29.29 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.05 / 0.0905 | 33.12 / 0.0474 | 29.30 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.22 / 0.0806 | 33.71 / 0.0307 | 29.29 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.05 / 0.0894 | 32.82 / 0.0493 | 29.29 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.24 / 0.0804 | 33.65 / 0.0303 | 29.29 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.05 / 0.0883 | 33.19 / 0.0457 | 29.29 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.24 / 0.0800 | 33.61 / 0.0294 | 29.29 | 3/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 27.13 / 0.1072 | 32.25 / 0.0597 | 29.19 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.64 / 0.0865 | 32.93 / 0.0345 | 29.28 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.74 / 0.1017 | 33.27 / 0.0490 | 29.26 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.96 / 0.0842 | 33.54 / 0.0331 | 29.29 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.79 / 0.0996 | 33.29 / 0.0462 | 29.25 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.03 / 0.0836 | 33.67 / 0.0328 | 29.29 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.80 / 0.0975 | 33.26 / 0.0481 | 29.23 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.08 / 0.0826 | 33.92 / 0.0336 | 29.29 | 1/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.52 / 0.1051 | 32.54 / 0.0564 | 29.23 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.90 / 0.0851 | 33.17 / 0.0327 | 29.28 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.97 / 0.1001 | 33.65 / 0.0459 | 29.30 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.15 / 0.0830 | 33.62 / 0.0318 | 29.29 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 28.00 / 0.0979 | 33.62 / 0.0454 | 29.30 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.20 / 0.0823 | 33.69 / 0.0316 | 29.29 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.01 / 0.0962 | 33.32 / 0.0481 | 29.29 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.23 / 0.0817 | 33.87 / 0.0317 | 29.29 | 2/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.36 / 0.0989 | 31.14 / 0.0654 | 29.21 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.86 / 0.0809 | 32.10 / 0.0348 | 29.29 | 2/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.74 / 0.0959 | 32.73 / 0.0546 | 29.26 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.10 / 0.0795 | 33.07 / 0.0331 | 29.29 | 3/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.79 / 0.0949 | 32.83 / 0.0517 | 29.27 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.15 / 0.0790 | 33.22 / 0.0330 | 29.29 | 3/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.82 / 0.0940 | 32.98 / 0.0491 | 29.27 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.18 / 0.0788 | 33.36 / 0.0329 | 29.29 | 3/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.36 / 0.0989 | 31.14 / 0.0654 | 29.21 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.86 / 0.0809 | 32.10 / 0.0348 | 29.29 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.74 / 0.0959 | 32.73 / 0.0546 | 29.26 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.10 / 0.0795 | 33.07 / 0.0331 | 29.29 | 3/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.79 / 0.0949 | 32.83 / 0.0517 | 29.27 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.15 / 0.0790 | 33.22 / 0.0330 | 29.29 | 3/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.82 / 0.0940 | 32.97 / 0.0492 | 29.27 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.18 / 0.0788 | 33.36 / 0.0329 | 29.29 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 33.66 / 0.0298 | 18.96 / 0.0235 | 29.29 / 0.0447 | 27.80 / 0.0823 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 2.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 33.66 | 0.9063 | 0.0298 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 14.77 | 0.7293 | 0.3399 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 14.83 | 0.7257 | 0.3154 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 14.72 | 0.7413 | 0.3250 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 14.63 | 0.7315 | 0.3208 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 14.83 | 0.7356 | 0.3352 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 15.24 | 0.7354 | 0.3041 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 15.03 | 0.7494 | 0.3154 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 15.07 | 0.7424 | 0.3090 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 27.72 | 0.8340 | 0.1905 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 29.90 | 0.8721 | 0.1320 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 29.90 | 0.8721 | 0.1320 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 29.38 | 0.8701 | 0.1375 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 29.38 | 0.8701 | 0.1375 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.62 | 0.6533 | 0.3199 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.72 | 0.6574 | 0.3241 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.72 | 0.6574 | 0.3241 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 15.63 | 0.6486 | 0.3464 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 15.63 | 0.6486 | 0.3464 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.95 | 0.5913 | 0.3563 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 17.52 | 0.7486 | 0.3109 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 18.85 | 0.7734 | 0.2751 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 18.72 | 0.7757 | 0.2896 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 18.74 | 0.7771 | 0.2819 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 18.09 | 0.7501 | 0.3050 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.60 | 0.7781 | 0.2653 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 19.12 | 0.7759 | 0.2794 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 19.33 | 0.7792 | 0.2704 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.45 | 0.6320 | 0.3187 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.04 | 0.6788 | 0.4097 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.68 | 0.7056 | 0.3695 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.43 | 0.7044 | 0.3862 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.56 | 0.7073 | 0.3762 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.04 | 0.6788 | 0.4097 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 12.68 | 0.7056 | 0.3696 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 12.43 | 0.7044 | 0.3863 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 12.56 | 0.7073 | 0.3762 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 33.59 | 0.9056 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 33.65 | 0.9057 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 33.67 | 0.9061 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 33.66 | 0.9061 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 33.66 | 0.9062 | 0.0309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 33.61 | 0.9055 | 0.0294 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 33.71 | 0.9065 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 33.65 | 0.9061 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 33.60 | 0.9044 | 0.0293 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 33.59 | 0.9049 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 33.66 | 0.9059 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 33.50 | 0.9050 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 33.66 | 0.9058 | 0.0300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 33.60 | 0.9056 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 33.60 | 0.9051 | 0.0287 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 33.66 | 0.9058 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 33.32 | 0.9041 | 0.0308 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 33.66 | 0.9058 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 33.41 | 0.9040 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 32.93 | 0.9024 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 33.92 | 0.9066 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 33.54 | 0.9053 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 33.67 | 0.9058 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 33.17 | 0.9034 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 33.87 | 0.9065 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 33.62 | 0.9054 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 33.69 | 0.9059 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 33.55 | 0.9023 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 32.10 | 0.8986 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 33.36 | 0.9051 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 33.07 | 0.9037 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 33.22 | 0.9043 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 32.10 | 0.8986 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 33.36 | 0.9051 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 33.07 | 0.9037 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 33.22 | 0.9043 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 32.38 | 0.8933 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.90 | 0.8941 | 0.0598 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 32.95 | 0.9029 | 0.0511 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 32.69 | 0.9008 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 32.69 | 0.8972 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 33.19 | 0.9019 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 33.12 | 0.9059 | 0.0474 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 32.82 | 0.9038 | 0.0493 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 32.46 | 0.8691 | 0.1027 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 33.74 | 0.9021 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 33.50 | 0.9024 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 33.54 | 0.9008 | 0.0575 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 33.53 | 0.9024 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 32.75 | 0.8899 | 0.0632 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 33.28 | 0.8946 | 0.0593 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 33.52 | 0.9018 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 32.91 | 0.8925 | 0.0657 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 33.52 | 0.9017 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.91 | 0.8600 | 0.0975 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 32.25 | 0.8914 | 0.0597 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 33.26 | 0.9070 | 0.0481 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 33.27 | 0.9058 | 0.0490 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 33.29 | 0.9079 | 0.0462 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 32.54 | 0.8936 | 0.0564 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 33.32 | 0.9083 | 0.0481 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 33.65 | 0.9074 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 33.62 | 0.9093 | 0.0454 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.00 | 0.8578 | 0.1000 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.14 | 0.8889 | 0.0654 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 32.98 | 0.9065 | 0.0491 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 32.73 | 0.9044 | 0.0546 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 32.83 | 0.9064 | 0.0517 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 31.14 | 0.8889 | 0.0654 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 32.97 | 0.9065 | 0.0492 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 32.73 | 0.9044 | 0.0546 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 32.83 | 0.9064 | 0.0517 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.96 | 0.5870 | 0.0235 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.12 | 0.4337 | 0.1197 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.16 | 0.4426 | 0.1153 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.12 | 0.4492 | 0.1176 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.13 | 0.4457 | 0.1164 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.16 | 0.4438 | 0.1184 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.28 | 0.4586 | 0.1130 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.18 | 0.4551 | 0.1161 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.23 | 0.4548 | 0.1145 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.88 | 0.3908 | 0.0678 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.85 | 0.5007 | 0.0608 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.85 | 0.5007 | 0.0608 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.89 | 0.5016 | 0.0571 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.89 | 0.5016 | 0.0571 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.95 | 0.3510 | 0.0695 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.64 | 0.4415 | 0.0680 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.64 | 0.4415 | 0.0680 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.66 | 0.4410 | 0.0668 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.66 | 0.4410 | 0.0668 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.36 | 0.3974 | 0.0689 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.26 | 0.4412 | 0.1044 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.55 | 0.4812 | 0.0970 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.47 | 0.4740 | 0.1001 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.52 | 0.4790 | 0.0987 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.43 | 0.4676 | 0.1005 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.89 | 0.5119 | 0.0917 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.64 | 0.5001 | 0.0959 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.74 | 0.5069 | 0.0939 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.98 | 0.4539 | 0.0614 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.53 | 0.4045 | 0.1141 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.95 | 0.4532 | 0.1060 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.76 | 0.4408 | 0.1094 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.85 | 0.4494 | 0.1075 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.53 | 0.4045 | 0.1141 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.95 | 0.4532 | 0.1060 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.76 | 0.4408 | 0.1094 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.85 | 0.4494 | 0.1075 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.80 | 0.6566 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.99 | 0.6629 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.12 | 0.6715 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.05 | 0.6687 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.16 | 0.6661 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.52 | 0.6781 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.44 | 0.6775 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.50 | 0.6780 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 18.37 | 0.5672 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.07 | 0.6822 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.92 | 0.6743 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 21.00 | 0.6784 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.91 | 0.6722 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 18.51 | 0.5767 | 0.0296 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.82 | 0.6701 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.71 | 0.6637 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.85 | 0.6707 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.77 | 0.6646 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.93 | 0.6369 | 0.0276 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.04 | 0.6372 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.17 | 0.6685 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.83 | 0.6605 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.01 | 0.6650 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.75 | 0.6575 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.65 | 0.6872 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.41 | 0.6809 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.55 | 0.6850 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.98 | 0.6404 | 0.0279 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.46 | 0.6385 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.37 | 0.6661 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.07 | 0.6587 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.25 | 0.6643 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.46 | 0.6385 | 0.0197 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.37 | 0.6660 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.07 | 0.6587 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.25 | 0.6643 | 0.0178 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.76 | 0.6564 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.95 | 0.6621 | 0.0202 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.08 | 0.6711 | 0.0203 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.00 | 0.6679 | 0.0199 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.15 | 0.6666 | 0.0201 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.49 | 0.6777 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.41 | 0.6780 | 0.0190 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.47 | 0.6781 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 18.37 | 0.5668 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.08 | 0.6818 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.92 | 0.6738 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 21.00 | 0.6781 | 0.0246 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.91 | 0.6716 | 0.0240 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 18.51 | 0.5764 | 0.0297 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.82 | 0.6696 | 0.0258 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.71 | 0.6632 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.85 | 0.6703 | 0.0246 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.77 | 0.6642 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.92 | 0.6353 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.02 | 0.6357 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.16 | 0.6681 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.82 | 0.6598 | 0.0232 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.00 | 0.6645 | 0.0225 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.72 | 0.6559 | 0.0235 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.63 | 0.6866 | 0.0204 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.39 | 0.6806 | 0.0210 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.53 | 0.6846 | 0.0206 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.99 | 0.6387 | 0.0279 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.45 | 0.6373 | 0.0199 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.34 | 0.6651 | 0.0178 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.03 | 0.6572 | 0.0186 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.21 | 0.6630 | 0.0181 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.45 | 0.6373 | 0.0199 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.34 | 0.6651 | 0.0178 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.03 | 0.6572 | 0.0186 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.21 | 0.6630 | 0.0181 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 39.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.37 | 0.6930 | 0.0409 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.82 | 0.4490 | 0.3106 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.87 | 0.4505 | 0.2996 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.83 | 0.4609 | 0.3050 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.84 | 0.4568 | 0.3022 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.83 | 0.4541 | 0.3086 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.91 | 0.4588 | 0.2957 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.85 | 0.4665 | 0.3026 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.87 | 0.4636 | 0.2992 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 19.37 | 0.5673 | 0.1802 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 19.80 | 0.5989 | 0.1734 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 19.80 | 0.5989 | 0.1734 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 19.75 | 0.5959 | 0.1746 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 19.75 | 0.5959 | 0.1746 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.61 | 0.3561 | 0.2012 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.55 | 0.3617 | 0.2105 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.55 | 0.3617 | 0.2105 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 15.52 | 0.3583 | 0.2114 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 15.52 | 0.3583 | 0.2114 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.41 | 0.3357 | 0.2142 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.07 | 0.4947 | 0.2883 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.18 | 0.5113 | 0.2707 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.13 | 0.5154 | 0.2796 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.15 | 0.5145 | 0.2752 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.17 | 0.5037 | 0.2841 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.70 | 0.5241 | 0.2642 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.30 | 0.5244 | 0.2751 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.46 | 0.5252 | 0.2700 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.69 | 0.4131 | 0.2001 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.07 | 0.4819 | 0.3036 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.26 | 0.5040 | 0.2859 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.15 | 0.5052 | 0.2953 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.19 | 0.5064 | 0.2905 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.07 | 0.4819 | 0.3036 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.26 | 0.5040 | 0.2859 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.15 | 0.5052 | 0.2953 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.19 | 0.5064 | 0.2905 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.76 | 0.6995 | 0.0415 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.90 | 0.7018 | 0.0402 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.03 | 0.7035 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.95 | 0.7029 | 0.0401 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.04 | 0.7013 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.30 | 0.7047 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.26 | 0.7050 | 0.0395 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.29 | 0.7050 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.83 | 0.6854 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.67 | 0.7049 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.57 | 0.7036 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.61 | 0.7041 | 0.0435 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.55 | 0.7031 | 0.0425 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.94 | 0.6887 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.50 | 0.7032 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.44 | 0.7023 | 0.0432 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.50 | 0.7028 | 0.0433 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.45 | 0.7019 | 0.0426 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.87 | 0.6959 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.17 | 0.6955 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.08 | 0.7036 | 0.0417 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.84 | 0.7021 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.98 | 0.7031 | 0.0431 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.68 | 0.6992 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.39 | 0.7067 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.24 | 0.7054 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.32 | 0.7064 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.87 | 0.6955 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.59 | 0.6987 | 0.0435 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.25 | 0.7049 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.08 | 0.7036 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.20 | 0.7048 | 0.0413 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.59 | 0.6987 | 0.0435 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.25 | 0.7049 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.08 | 0.7036 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.20 | 0.7048 | 0.0412 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.22 | 0.6941 | 0.0513 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.41 | 0.6994 | 0.0480 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.64 | 0.7039 | 0.0489 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.52 | 0.7025 | 0.0480 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.55 | 0.6975 | 0.0499 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.87 | 0.7042 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.87 | 0.7065 | 0.0473 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.86 | 0.7061 | 0.0463 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.43 | 0.6695 | 0.0661 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.35 | 0.6999 | 0.0543 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.38 | 0.7016 | 0.0480 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.02 | 0.6969 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.11 | 0.7000 | 0.0478 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.66 | 0.6806 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.10 | 0.6969 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.15 | 0.6988 | 0.0485 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.87 | 0.6946 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.95 | 0.6970 | 0.0497 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.97 | 0.6799 | 0.0609 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.25 | 0.6872 | 0.0619 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.54 | 0.7022 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.40 | 0.7019 | 0.0570 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.51 | 0.7029 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.93 | 0.6936 | 0.0594 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.92 | 0.7086 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.82 | 0.7082 | 0.0543 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.88 | 0.7094 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.43 | 0.6716 | 0.0683 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.52 | 0.6834 | 0.0615 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.20 | 0.6945 | 0.0568 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.22 | 0.6950 | 0.0586 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.31 | 0.6963 | 0.0574 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.52 | 0.6834 | 0.0615 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.20 | 0.6945 | 0.0568 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.22 | 0.6950 | 0.0586 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.31 | 0.6963 | 0.0574 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 43.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.63 | 0.6523 | 0.0479 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.82 | 0.3689 | 0.4568 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.87 | 0.3718 | 0.4489 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.83 | 0.3806 | 0.4532 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.84 | 0.3768 | 0.4512 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.82 | 0.3743 | 0.4556 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.87 | 0.3792 | 0.4462 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.83 | 0.3860 | 0.4515 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.84 | 0.3833 | 0.4488 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 21.18 | 0.5249 | 0.2005 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 21.65 | 0.5483 | 0.1921 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 21.65 | 0.5483 | 0.1921 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 21.62 | 0.5482 | 0.1917 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 21.62 | 0.5482 | 0.1917 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 17.65 | 0.3446 | 0.2631 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 17.85 | 0.3553 | 0.2649 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 17.85 | 0.3553 | 0.2649 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 17.83 | 0.3530 | 0.2661 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 17.83 | 0.3530 | 0.2661 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.72 | 0.3380 | 0.2666 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.77 | 0.4080 | 0.4235 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.90 | 0.4294 | 0.4087 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.83 | 0.4316 | 0.4156 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.85 | 0.4316 | 0.4121 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.88 | 0.4203 | 0.4196 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.37 | 0.4421 | 0.4027 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.98 | 0.4423 | 0.4114 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.14 | 0.4433 | 0.4072 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.72 | 0.4052 | 0.2412 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.10 | 0.3743 | 0.4452 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.20 | 0.3945 | 0.4312 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.15 | 0.3960 | 0.4370 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.17 | 0.3966 | 0.4337 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.10 | 0.3743 | 0.4452 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.20 | 0.3945 | 0.4312 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.15 | 0.3960 | 0.4370 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.17 | 0.3966 | 0.4337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.97 | 0.6580 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.13 | 0.6598 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.20 | 0.6609 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.16 | 0.6605 | 0.0462 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.23 | 0.6596 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.46 | 0.6623 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.41 | 0.6623 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.44 | 0.6624 | 0.0452 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.15 | 0.6466 | 0.0607 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.74 | 0.6623 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.67 | 0.6612 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.70 | 0.6617 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.66 | 0.6607 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.26 | 0.6492 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.61 | 0.6609 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.57 | 0.6601 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.62 | 0.6607 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.58 | 0.6598 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.12 | 0.6557 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.40 | 0.6540 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.22 | 0.6606 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.99 | 0.6595 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.14 | 0.6604 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.85 | 0.6571 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.45 | 0.6629 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.33 | 0.6621 | 0.0479 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.42 | 0.6629 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.14 | 0.6561 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.74 | 0.6557 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.32 | 0.6604 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.18 | 0.6598 | 0.0452 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.27 | 0.6604 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.74 | 0.6557 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.32 | 0.6604 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.18 | 0.6598 | 0.0452 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.27 | 0.6604 | 0.0446 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.51 | 0.6533 | 0.0570 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.70 | 0.6577 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.86 | 0.6611 | 0.0554 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.78 | 0.6600 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.83 | 0.6563 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.09 | 0.6621 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.08 | 0.6637 | 0.0536 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.08 | 0.6634 | 0.0528 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.89 | 0.6365 | 0.0697 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.56 | 0.6599 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.57 | 0.6604 | 0.0524 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.31 | 0.6579 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.38 | 0.6595 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.07 | 0.6439 | 0.0588 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.36 | 0.6576 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.39 | 0.6582 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.17 | 0.6561 | 0.0585 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.22 | 0.6570 | 0.0540 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.64 | 0.6468 | 0.0609 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.58 | 0.6475 | 0.0666 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.75 | 0.6601 | 0.0582 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.60 | 0.6604 | 0.0618 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.72 | 0.6610 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.21 | 0.6531 | 0.0646 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.04 | 0.6651 | 0.0570 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.99 | 0.6654 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.04 | 0.6663 | 0.0584 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.58 | 0.6475 | 0.0634 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.99 | 0.6477 | 0.0601 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.75 | 0.6563 | 0.0553 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.60 | 0.6566 | 0.0569 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.68 | 0.6572 | 0.0559 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.99 | 0.6477 | 0.0601 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.75 | 0.6563 | 0.0553 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.60 | 0.6566 | 0.0569 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.68 | 0.6572 | 0.0559 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 63.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.29 | 0.6481 | 0.0447 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.29 | 0.2678 | 0.4422 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.32 | 0.2686 | 0.4356 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.29 | 0.2726 | 0.4392 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.30 | 0.2709 | 0.4373 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.28 | 0.2681 | 0.4425 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.30 | 0.2700 | 0.4350 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.28 | 0.2730 | 0.4396 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.29 | 0.2718 | 0.4372 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.57 | 0.4678 | 0.2412 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.55 | 0.4659 | 0.2463 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.55 | 0.4659 | 0.2463 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.55 | 0.4677 | 0.2462 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.55 | 0.4677 | 0.2462 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.66 | 0.1935 | 0.2840 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.70 | 0.1937 | 0.2841 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.70 | 0.1937 | 0.2841 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.69 | 0.1933 | 0.2842 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.69 | 0.1933 | 0.2842 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.66 | 0.1867 | 0.2836 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.89 | 0.3049 | 0.4157 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 2.94 | 0.3114 | 0.4023 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 2.91 | 0.3146 | 0.4093 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 2.92 | 0.3135 | 0.4063 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 2.92 | 0.3079 | 0.4120 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.16 | 0.3174 | 0.3962 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.98 | 0.3177 | 0.4053 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.05 | 0.3180 | 0.4008 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.21 | 0.2431 | 0.2653 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.28 | 0.2641 | 0.4387 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.32 | 0.2693 | 0.4295 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.30 | 0.2709 | 0.4342 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.31 | 0.2706 | 0.4318 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.28 | 0.2641 | 0.4387 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.32 | 0.2693 | 0.4295 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.30 | 0.2709 | 0.4342 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.31 | 0.2706 | 0.4318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.28 | 0.6481 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.28 | 0.6481 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.29 | 0.6482 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.27 | 0.6479 | 0.0462 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.28 | 0.6490 | 0.0458 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.29 | 0.6490 | 0.0458 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.28 | 0.6490 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.28 | 0.6481 | 0.0464 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.29 | 0.6492 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.30 | 0.6492 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.29 | 0.6493 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.30 | 0.6489 | 0.0447 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.24 | 0.6481 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.23 | 0.6474 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.24 | 0.6481 | 0.0466 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.23 | 0.6474 | 0.0465 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.30 | 0.6488 | 0.0448 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.24 | 0.6480 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.23 | 0.6475 | 0.0466 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.25 | 0.6480 | 0.0465 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.24 | 0.6475 | 0.0464 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.15 | 0.6471 | 0.0479 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.19 | 0.6477 | 0.0514 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.23 | 0.6488 | 0.0487 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.26 | 0.6496 | 0.0499 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.25 | 0.6493 | 0.0492 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.23 | 0.6484 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.29 | 0.6505 | 0.0483 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.30 | 0.6505 | 0.0495 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.30 | 0.6507 | 0.0488 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.18 | 0.6481 | 0.0487 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.21 | 0.6469 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.27 | 0.6480 | 0.0467 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.26 | 0.6479 | 0.0474 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.27 | 0.6480 | 0.0469 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.21 | 0.6469 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.27 | 0.6480 | 0.0467 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.26 | 0.6479 | 0.0474 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.27 | 0.6480 | 0.0469 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.80 | 0.6599 | 0.0823 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.03 | 0.3296 | 0.5560 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.06 | 0.3302 | 0.5408 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.04 | 0.3365 | 0.5490 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.05 | 0.3337 | 0.5451 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.03 | 0.3319 | 0.5541 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.05 | 0.3343 | 0.5367 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.03 | 0.3390 | 0.5463 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.04 | 0.3371 | 0.5415 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.51 | 0.5123 | 0.3895 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 18.59 | 0.5212 | 0.3826 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 18.59 | 0.5212 | 0.3826 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 18.59 | 0.5221 | 0.3826 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 18.59 | 0.5221 | 0.3826 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.35 | 0.2617 | 0.4088 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.42 | 0.2661 | 0.4117 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.42 | 0.2661 | 0.4117 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 15.41 | 0.2653 | 0.4124 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 15.41 | 0.2653 | 0.4124 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.35 | 0.2544 | 0.4135 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.75 | 0.3669 | 0.5402 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.82 | 0.3762 | 0.5169 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.78 | 0.3803 | 0.5294 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.79 | 0.3791 | 0.5236 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.81 | 0.3722 | 0.5347 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.11 | 0.3850 | 0.5104 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.88 | 0.3855 | 0.5234 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.98 | 0.3859 | 0.5168 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.04 | 0.3162 | 0.3933 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.15 | 0.3293 | 0.5602 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.21 | 0.3397 | 0.5389 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.18 | 0.3415 | 0.5488 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.19 | 0.3415 | 0.5432 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.15 | 0.3293 | 0.5602 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.21 | 0.3397 | 0.5389 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.18 | 0.3415 | 0.5488 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.19 | 0.3415 | 0.5432 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.99 | 0.6624 | 0.0826 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.07 | 0.6632 | 0.0814 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.11 | 0.6638 | 0.0815 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.09 | 0.6636 | 0.0812 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.13 | 0.6631 | 0.0815 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.24 | 0.6644 | 0.0800 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.22 | 0.6644 | 0.0806 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.24 | 0.6645 | 0.0804 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.54 | 0.6577 | 0.0953 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.41 | 0.6644 | 0.0856 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.37 | 0.6639 | 0.0845 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.38 | 0.6642 | 0.0843 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.36 | 0.6637 | 0.0834 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.60 | 0.6588 | 0.0882 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.34 | 0.6638 | 0.0847 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.31 | 0.6634 | 0.0840 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.34 | 0.6637 | 0.0841 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.32 | 0.6633 | 0.0836 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.08 | 0.6616 | 0.0865 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.64 | 0.6606 | 0.0865 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.08 | 0.6633 | 0.0826 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.96 | 0.6629 | 0.0842 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.03 | 0.6632 | 0.0836 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.90 | 0.6620 | 0.0851 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.23 | 0.6645 | 0.0817 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.15 | 0.6641 | 0.0830 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.20 | 0.6644 | 0.0823 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.10 | 0.6618 | 0.0865 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.86 | 0.6614 | 0.0809 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.18 | 0.6635 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.10 | 0.6633 | 0.0795 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.15 | 0.6635 | 0.0790 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.86 | 0.6614 | 0.0809 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.18 | 0.6635 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.10 | 0.6633 | 0.0795 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.15 | 0.6635 | 0.0790 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.72 | 0.6605 | 0.0945 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.82 | 0.6628 | 0.0911 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.92 | 0.6644 | 0.0923 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.87 | 0.6639 | 0.0914 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.90 | 0.6618 | 0.0930 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.05 | 0.6650 | 0.0883 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.05 | 0.6657 | 0.0905 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.05 | 0.6656 | 0.0894 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.38 | 0.6537 | 0.1046 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.28 | 0.6633 | 0.0946 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.27 | 0.6631 | 0.0882 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.15 | 0.6625 | 0.0943 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.17 | 0.6626 | 0.0881 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.49 | 0.6569 | 0.0939 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.17 | 0.6623 | 0.0944 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.18 | 0.6621 | 0.0893 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.07 | 0.6616 | 0.0951 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.09 | 0.6616 | 0.0902 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.75 | 0.6573 | 0.0985 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.13 | 0.6579 | 0.1072 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.80 | 0.6633 | 0.0975 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.74 | 0.6641 | 0.1017 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.79 | 0.6641 | 0.0996 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.52 | 0.6607 | 0.1051 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.01 | 0.6667 | 0.0962 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.97 | 0.6668 | 0.1001 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.00 | 0.6673 | 0.0979 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.75 | 0.6583 | 0.1012 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.36 | 0.6570 | 0.0989 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.82 | 0.6613 | 0.0940 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.74 | 0.6614 | 0.0959 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.79 | 0.6617 | 0.0949 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.36 | 0.6570 | 0.0989 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.82 | 0.6613 | 0.0940 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.74 | 0.6614 | 0.0959 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.79 | 0.6617 | 0.0949 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 978 | None | classic | 1.43 | False | 177026 | 0.177 | 43.8 | 30.44 | 0.14 | 0.009 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 978 | None | classic | 1.43 | False | 177026 | 0.177 | 33.3 | 30.44 | 0.14 | 0.009 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 978 | None | classic | 1.43 | False | 177026 | 0.177 | 31.5 | 30.44 | 0.14 | 0.009 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 978 | None | classic | 1.43 | False | 177026 | 0.177 | 35.7 | 30.44 | 0.14 | 0.009 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 946 | None | classic | 1.34 | False | 173772 | 0.171 | 29.7 | 29.90 | 0.15 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 946 | None | classic | 1.34 | False | 173772 | 0.171 | 33.8 | 29.90 | 0.15 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 946 | None | classic | 1.34 | False | 173772 | 0.171 | 29.7 | 29.90 | 0.15 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 946 | None | classic | 1.34 | False | 173772 | 0.171 | 33.8 | 29.90 | 0.15 | 0.006 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1207695 | 0.161 | 25.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1207695 | 0.796 | 51.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1207695 | 0.796 | 51.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1207695 | 0.550 | 25.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1207695 | 0.550 | 25.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1207695 | 0.161 | 34.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1207695 | 0.796 | 74.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1207695 | 0.796 | 74.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1207695 | 0.550 | 32.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1207695 | 0.550 | 32.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1207695 | 0.796 | 159.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 284469 | 0.170 | 31.7 | 30.86 | 0.21 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 284469 | 0.170 | 31.4 | 30.86 | 0.21 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 284469 | 0.170 | 35.9 | 30.86 | 0.21 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 284469 | 0.170 | 32.9 | 30.86 | 0.21 | 0.011 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1221 | None | classic | 2.23 | False | 429249 | 0.348 | 58.4 | 30.55 | 0.06 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1221 | None | classic | 2.23 | False | 429249 | 0.348 | 56.5 | 30.55 | 0.06 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1221 | None | classic | 2.23 | False | 429249 | 0.348 | 54.9 | 30.55 | 0.06 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1221 | None | classic | 2.23 | False | 429249 | 0.348 | 59.7 | 30.55 | 0.06 | 0.007 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1662028 | 0.796 | 71.2 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 42.2 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 33.2 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 29.7 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.321 | 32.4 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.170 | 36.6 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.170 | 33.1 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.170 | 33.6 | 31.17 | 0.22 | 0.020 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 311491 | 0.170 | 33.3 | 31.17 | 0.22 | 0.020 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.772 | 0.018 |
| in035 | mask_ent | 0.753 | 0.018 |
| in035 | mask_grad | 0.485 | 0.018 |
| in035 | r_col | 0.698 | 0.018 |
| in035 | r_warp | 0.870 | 0.018 |

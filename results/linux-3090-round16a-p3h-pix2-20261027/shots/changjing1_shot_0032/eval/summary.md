# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 31.6% | 21.99 / 0.0361 | 21.45 / 0.0726 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 32.4% | 22.05 / 0.0363 | 22.58 / 0.0557 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 32.1% | 22.02 / 0.0360 | 22.58 / 0.0630 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 32.2% | 22.03 / 0.0362 | 22.72 / 0.0585 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 32.1% | 22.02 / 0.0364 | 21.61 / 0.0725 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 33.0% | 22.09 / 0.0368 | 22.98 / 0.0537 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 32.6% | 22.07 / 0.0366 | 22.88 / 0.0610 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 32.8% | 22.07 / 0.0363 | 23.00 / 0.0565 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 33.0% | 22.00 / 0.0389 | 20.84 / 0.1075 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 30.0% | 21.81 / 0.0370 | 23.81 / 0.0665 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 9.7% | 18.16 / 0.0260 | 20.95 / 0.0426 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 30.1% | 21.82 / 0.0373 | 22.75 / 0.0709 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 10.3% | 18.38 / 0.0264 | 19.65 / 0.0472 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 33.0% | 22.00 / 0.0389 | 20.84 / 0.0834 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 29.8% | 21.81 / 0.0367 | 22.95 / 0.0628 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.4% | 18.54 / 0.0244 | 19.98 / 0.0425 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 29.8% | 21.83 / 0.0371 | 21.94 / 0.0666 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 10.7% | 18.69 / 0.0252 | 18.72 / 0.0465 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 33.7% | 22.13 / 0.0385 | 22.30 / 0.0799 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 33.8% | 22.44 / 0.0376 | 20.93 / 0.0826 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 34.8% | 22.49 / 0.0379 | 22.41 / 0.0641 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 34.3% | 22.46 / 0.0378 | 22.09 / 0.0719 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 34.6% | 22.47 / 0.0378 | 22.29 / 0.0673 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 34.4% | 22.48 / 0.0383 | 21.60 / 0.0778 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 35.3% | 22.56 / 0.0386 | 23.00 / 0.0574 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 34.9% | 22.52 / 0.0386 | 22.88 / 0.0653 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 35.0% | 22.53 / 0.0388 | 23.06 / 0.0604 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 35.5% | 22.58 / 0.0401 | 22.09 / 0.0896 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 25.8% | 22.13 / 0.0350 | 20.55 / 0.0776 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 27.9% | 22.29 / 0.0370 | 21.76 / 0.0651 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 26.8% | 22.20 / 0.0360 | 21.56 / 0.0710 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 27.2% | 22.23 / 0.0359 | 21.77 / 0.0672 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 26.5% | 22.20 / 0.0356 | 21.14 / 0.0761 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 28.5% | 22.35 / 0.0361 | 22.11 / 0.0627 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 27.4% | 22.28 / 0.0353 | 21.96 / 0.0693 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 27.8% | 22.30 / 0.0355 | 22.12 / 0.0653 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 25.19 / 0.0637 | 22.65 / 0.0960 | 18.16 / 0.0327 | 29.29 / 0.0247 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.57 / 0.1000 | 22.99 / 0.1586 | 18.84 / 0.0451 | 28.72 / 0.0303 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.40 / 0.0854 | 24.18 / 0.1240 | 19.41 / 0.0369 | 28.78 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.40 / 0.0921 | 24.01 / 0.1418 | 19.48 / 0.0402 | 28.87 / 0.0297 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.49 / 0.0884 | 24.28 / 0.1315 | 19.54 / 0.0384 | 28.86 / 0.0294 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.70 / 0.0986 | 23.28 / 0.1495 | 19.01 / 0.0435 | 28.66 / 0.0303 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.74 / 0.0813 | 24.43 / 0.1114 | 19.98 / 0.0339 | 28.85 / 0.0287 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.61 / 0.0895 | 24.29 / 0.1314 | 19.84 / 0.0388 | 28.89 / 0.0295 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.70 / 0.0850 | 24.49 / 0.1193 | 19.95 / 0.0364 | 28.88 / 0.0291 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.73 / 0.1128 | 22.73 / 0.2157 | 18.63 / 0.0632 | 29.24 / 0.0250 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.42 / 0.0870 | 26.07 / 0.1127 | 21.23 / 0.0399 | 29.16 / 0.0254 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.46 / 0.0780 | 25.86 / 0.0956 | 20.94 / 0.0396 | 29.22 / 0.0250 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.78 / 0.0920 | 25.70 / 0.1149 | 20.67 / 0.0417 | 29.14 / 0.0259 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.87 / 0.0819 | 25.71 / 0.0913 | 20.47 / 0.0407 | 29.21 / 0.0252 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.65 / 0.0940 | 22.52 / 0.1710 | 18.51 / 0.0477 | 29.21 / 0.0255 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.85 / 0.0840 | 25.11 / 0.1102 | 20.55 / 0.0389 | 29.12 / 0.0260 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.91 / 0.0777 | 25.07 / 0.0990 | 20.44 / 0.0387 | 29.23 / 0.0251 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.17 / 0.0876 | 24.93 / 0.1152 | 20.09 / 0.0413 | 29.10 / 0.0260 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.26 / 0.0816 | 25.01 / 0.1035 | 20.02 / 0.0409 | 29.22 / 0.0251 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.02 / 0.0856 | 24.38 / 0.1346 | 20.28 / 0.0383 | 29.10 / 0.0262 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.94 / 0.1082 | 22.65 / 0.1714 | 18.25 / 0.0465 | 28.63 / 0.0316 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.00 / 0.0904 | 24.13 / 0.1305 | 19.19 / 0.0380 | 28.88 / 0.0294 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.79 / 0.0989 | 23.74 / 0.1508 | 18.95 / 0.0417 | 28.89 / 0.0302 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.93 / 0.0944 | 24.04 / 0.1395 | 19.11 / 0.0399 | 28.88 / 0.0298 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.44 / 0.1028 | 23.10 / 0.1611 | 18.91 / 0.0433 | 28.76 / 0.0310 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.50 / 0.0842 | 24.25 / 0.1204 | 19.89 / 0.0330 | 28.99 / 0.0288 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.33 / 0.0926 | 24.07 / 0.1402 | 19.66 / 0.0379 | 28.99 / 0.0298 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.44 / 0.0883 | 24.29 / 0.1276 | 19.79 / 0.0354 | 29.00 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.62 / 0.0892 | 24.25 / 0.1405 | 19.89 / 0.0397 | 28.97 / 0.0273 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 24.13 / 0.1022 | 22.40 / 0.1664 | 18.24 / 0.0433 | 28.87 / 0.0295 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.90 / 0.0892 | 23.63 / 0.1284 | 18.78 / 0.0368 | 28.94 / 0.0285 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.76 / 0.0962 | 23.28 / 0.1495 | 18.68 / 0.0400 | 28.91 / 0.0292 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.87 / 0.0925 | 23.53 / 0.1376 | 18.74 / 0.0382 | 28.93 / 0.0289 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.52 / 0.0985 | 22.59 / 0.1648 | 18.59 / 0.0412 | 28.98 / 0.0290 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.11 / 0.0872 | 23.26 / 0.1324 | 19.18 / 0.0348 | 28.90 / 0.0286 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.01 / 0.0924 | 23.18 / 0.1490 | 19.07 / 0.0374 | 28.91 / 0.0290 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.08 / 0.0896 | 23.24 / 0.1386 | 19.14 / 0.0359 | 28.90 / 0.0289 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 13.8%） | — | — | 25.19 / 0.0637 | 22.65 / 0.0960 | 29.29 |
| in035 | rife | 17.7% | 25.8% | 24.13 / 0.1022 | 22.40 / 0.1664 | 28.87 |
| in035 | cnw_cnn | 26.1% | 31.6% | 24.57 / 0.1000 | 22.99 / 0.1586 | 28.72 |
| in035 | cnw_f5 | 26.5% | 33.8% | 23.94 / 0.1082 | 22.65 / 0.1714 | 28.63 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 23.96 / 0.0724 | -0.49 / +0.0433 (core 15.6%) | +0.56 / +0.0356 (core 26.7%) | -0.24 / +0.0474 (core 26.6%) |
| in035 | 2 | 0-3 | 25.41 / 0.0635 | -1.65 / +0.0427 (core 15.6%) | -1.29 / +0.0447 (core 26.7%) | -2.10 / +0.0545 (core 26.6%) |
| in035 | 4 | 3-5 | 26.21 / 0.0552 | -1.04 / +0.0294 (core 13.7%) | -1.14 / +0.0288 (core 18.3%) | -1.43 / +0.0316 (core 20.0%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 25.19 / 0.0637 | 22.65 | 29.29 | — |
| in035 | cnw_cnn | 不复核 | —% | 24.57 / 0.1000 | 22.99 | 28.72 | 0/3 |
| in035 | cnw_cnn | oracle | 9.9% | 25.37 / 0.0795 | 24.03 | 29.19 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 25.40 / 0.0854 | 24.18 | 28.78 | 0/3 |
| in035 | cnw_cnn | oracle | 10.0% | 25.86 / 0.0700 | 24.85 | 29.18 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 25.40 / 0.0921 | 24.01 | 28.87 | 0/3 |
| in035 | cnw_cnn | oracle | 10.0% | 25.89 / 0.0746 | 24.75 | 29.21 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 25.49 / 0.0884 | 24.28 | 28.86 | 0/3 |
| in035 | cnw_cnn | oracle | 10.0% | 25.94 / 0.0721 | 24.94 | 29.21 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 24.70 / 0.0986 | 23.28 | 28.66 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 9.9% | 25.49 / 0.0777 | 24.28 | 29.19 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.74 / 0.0813 | 24.43 | 28.85 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 10.0% | 26.23 / 0.0669 | 25.22 | 29.23 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.61 / 0.0895 | 24.29 | 28.89 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 10.0% | 26.12 / 0.0725 | 25.08 | 29.23 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.70 / 0.0850 | 24.49 | 28.88 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 10.0% | 26.20 / 0.0696 | 25.26 | 29.23 | 0/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 24.73 / 0.1128 | 22.73 | 29.24 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 10.1% | 25.25 / 0.0962 | 23.80 | 29.29 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 26.42 / 0.0870 | 26.07 | 29.16 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 9.7% | 26.97 / 0.0718 | 26.72 | 29.28 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 26.46 / 0.0780 | 25.86 | 29.22 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 6.4% | 26.81 / 0.0710 | 26.07 | 29.29 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 25.78 / 0.0920 | 25.70 | 29.14 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 9.7% | 26.61 / 0.0744 | 26.55 | 29.27 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 25.87 / 0.0819 | 25.71 | 29.21 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 6.4% | 26.51 / 0.0731 | 26.00 | 29.28 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 24.65 / 0.0940 | 22.52 | 29.21 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 10.1% | 25.18 / 0.0804 | 23.59 | 29.27 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 25.85 / 0.0840 | 25.11 | 29.12 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 9.7% | 26.56 / 0.0703 | 25.69 | 29.26 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 25.91 / 0.0777 | 25.07 | 29.23 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 6.3% | 26.50 / 0.0694 | 25.40 | 29.29 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 25.17 / 0.0876 | 24.93 | 29.10 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 9.6% | 26.23 / 0.0728 | 25.67 | 29.26 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 25.26 / 0.0816 | 25.01 | 29.22 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 6.2% | 26.21 / 0.0716 | 25.43 | 29.28 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.02 / 0.0856 | 24.38 | 29.10 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 10.1% | 26.42 / 0.0699 | 25.22 | 29.26 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 23.94 / 0.1082 | 22.65 | 28.63 | 0/3 |
| in035 | cnw_f5 | oracle | 9.3% | 24.94 / 0.0809 | 23.86 | 29.17 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.00 / 0.0904 | 24.13 | 28.88 | 0/3 |
| in035 | cnw_f5 | oracle | 9.5% | 25.70 / 0.0704 | 25.08 | 29.23 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 24.79 / 0.0989 | 23.74 | 28.89 | 0/3 |
| in035 | cnw_f5 | oracle | 9.4% | 25.53 / 0.0755 | 24.73 | 29.22 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 24.93 / 0.0944 | 24.04 | 28.88 | 0/3 |
| in035 | cnw_f5 | oracle | 9.4% | 25.64 / 0.0728 | 24.98 | 29.23 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 24.44 / 0.1028 | 23.10 | 28.76 | 0/3 |
| in035 | cnw_f5_mw | oracle | 9.3% | 25.39 / 0.0774 | 24.35 | 29.21 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.50 / 0.0842 | 24.25 | 28.99 | 0/3 |
| in035 | cnw_f5_mw | oracle | 9.4% | 26.17 / 0.0662 | 25.34 | 29.26 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.33 / 0.0926 | 24.07 | 28.99 | 0/3 |
| in035 | cnw_f5_mw | oracle | 9.4% | 26.00 / 0.0719 | 25.18 | 29.25 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.44 / 0.0883 | 24.29 | 29.00 | 0/3 |
| in035 | cnw_f5_mw | oracle | 9.4% | 26.10 / 0.0691 | 25.37 | 29.26 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 25.62 / 0.0892 | 24.25 | 28.97 | 0/3 |
| in035 | cnw_f5_pix | oracle | 9.4% | 26.17 / 0.0710 | 25.17 | 29.26 | 0/3 |
| in035 | rife | 不复核 | —% | 24.13 / 0.1022 | 22.40 | 28.87 | 0/3 |
| in035 | rife | oracle | 6.9% | 25.05 / 0.0768 | 23.67 | 29.25 | 0/3 |
| in035 | rife | 不复核 | —% | 24.90 / 0.0892 | 23.63 | 28.94 | 0/3 |
| in035 | rife | oracle | 7.3% | 25.49 / 0.0694 | 24.65 | 29.23 | 0/3 |
| in035 | rife | 不复核 | —% | 24.76 / 0.0962 | 23.28 | 28.91 | 0/3 |
| in035 | rife | oracle | 7.1% | 25.41 / 0.0738 | 24.33 | 29.25 | 0/3 |
| in035 | rife | 不复核 | —% | 24.87 / 0.0925 | 23.53 | 28.93 | 0/3 |
| in035 | rife | oracle | 7.2% | 25.47 / 0.0714 | 24.52 | 29.24 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 24.52 / 0.0985 | 22.59 | 28.98 | 0/3 |
| in035 | rife_mw | oracle | 7.0% | 25.31 / 0.0744 | 23.97 | 29.25 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.11 / 0.0872 | 23.26 | 28.90 | 0/3 |
| in035 | rife_mw | oracle | 7.4% | 25.73 / 0.0674 | 24.53 | 29.22 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 25.01 / 0.0924 | 23.18 | 28.91 | 0/3 |
| in035 | rife_mw | oracle | 7.2% | 25.67 / 0.0709 | 24.54 | 29.25 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.08 / 0.0896 | 23.24 | 28.90 | 0/3 |
| in035 | rife_mw | oracle | 7.3% | 25.72 / 0.0692 | 24.56 | 29.24 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 25.19 / 0.0637 | 22.65 / 0.0960 | — |
| in035 | FF | 0（前馈） | 1004×721（67%） | 27.09 | 24.57 / 0.1000 | 22.99 / 0.1586 | 0/3 |
| in035 | 25 | 1.60 s | 1004×721（67%） | 28.40 | 25.40 / 0.0921 | 24.01 / 0.1418 | 0/3 |
| in035 | 50 | 3.21 s | 1004×721（67%） | 28.92 | 25.49 / 0.0884 | 24.28 / 0.1315 | 0/3 |
| in035 | 100 | 6.39 s | 1004×721（67%） | 29.48 | 25.40 / 0.0854 | 24.18 / 0.1240 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 25.19 / 0.0637 | 22.65 / 0.0960 | 29.29 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 24.57 / 0.1000 | 22.99 / 0.1586 | 28.72 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 25.37 / 0.0795 | 24.03 / 0.1295 | 29.19 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 25.40 / 0.0921 | 24.01 / 0.1418 | 28.87 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 25.89 / 0.0746 | 24.75 / 0.1173 | 29.21 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 25.49 / 0.0884 | 24.28 / 0.1315 | 28.86 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 25.94 / 0.0721 | 24.94 / 0.1087 | 29.21 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 25.40 / 0.0854 | 24.18 / 0.1240 | 28.78 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 25.86 / 0.0700 | 24.85 / 0.1033 | 29.18 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 24.70 / 0.0986 | 23.28 / 0.1495 | 28.66 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 25.49 / 0.0777 | 24.28 / 0.1244 | 29.19 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 25.61 / 0.0895 | 24.29 / 0.1314 | 28.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 26.12 / 0.0725 | 25.08 / 0.1109 | 29.23 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 25.70 / 0.0850 | 24.49 / 0.1193 | 28.88 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 26.20 / 0.0696 | 25.26 / 0.1016 | 29.23 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 25.74 / 0.0813 | 24.43 / 0.1114 | 28.85 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 26.23 / 0.0669 | 25.22 / 0.0951 | 29.23 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 23.94 / 0.1082 | 22.65 / 0.1714 | 28.63 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 24.94 / 0.0809 | 23.86 / 0.1318 | 29.17 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 24.79 / 0.0989 | 23.74 / 0.1508 | 28.89 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 25.53 / 0.0755 | 24.73 / 0.1186 | 29.22 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 24.93 / 0.0944 | 24.04 / 0.1395 | 28.88 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 25.64 / 0.0728 | 24.98 / 0.1098 | 29.23 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 25.00 / 0.0904 | 24.13 / 0.1305 | 28.88 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 25.70 / 0.0704 | 25.08 / 0.1029 | 29.23 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 24.44 / 0.1028 | 23.10 / 0.1611 | 28.76 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 25.39 / 0.0774 | 24.35 / 0.1261 | 29.21 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 25.33 / 0.0926 | 24.07 / 0.1402 | 28.99 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 26.00 / 0.0719 | 25.18 / 0.1118 | 29.25 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 25.44 / 0.0883 | 24.29 / 0.1276 | 29.00 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 26.10 / 0.0691 | 25.37 / 0.1018 | 29.26 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 25.50 / 0.0842 | 24.25 / 0.1204 | 28.99 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 26.17 / 0.0662 | 25.34 / 0.0957 | 29.26 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 24.13 / 0.1022 | 22.40 / 0.1664 | 28.87 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 25.05 / 0.0768 | 23.67 / 0.1270 | 29.25 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 24.76 / 0.0962 | 23.28 / 0.1495 | 28.91 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 25.41 / 0.0738 | 24.33 / 0.1166 | 29.25 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 24.87 / 0.0925 | 23.53 / 0.1376 | 28.93 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 25.47 / 0.0714 | 24.52 / 0.1090 | 29.24 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 24.90 / 0.0892 | 23.63 / 0.1284 | 28.94 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 25.49 / 0.0694 | 24.65 / 0.1015 | 29.23 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 24.52 / 0.0985 | 22.59 / 0.1648 | 28.98 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 25.31 / 0.0744 | 23.97 / 0.1241 | 29.25 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 25.01 / 0.0924 | 23.18 / 0.1490 | 28.91 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 25.67 / 0.0709 | 24.54 / 0.1155 | 29.25 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 25.08 / 0.0896 | 23.24 / 0.1386 | 28.90 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 25.72 / 0.0692 | 24.56 / 0.1080 | 29.24 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 25.11 / 0.0872 | 23.26 / 0.1324 | 28.90 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 25.73 / 0.0674 | 24.53 / 0.1033 | 29.22 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.65 / 0.0960 | 18.16 / 0.0327 | 29.29 / 0.0247 | 25.19 / 0.0637 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 18.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.65 | 0.6881 | 0.0960 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 17.29 | 0.6358 | 0.2348 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 18.85 | 0.6805 | 0.1811 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 18.20 | 0.6767 | 0.2096 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 18.57 | 0.6832 | 0.1938 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 17.97 | 0.6572 | 0.2187 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 19.22 | 0.6997 | 0.1661 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 18.66 | 0.6977 | 0.1924 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 18.96 | 0.7042 | 0.1760 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 22.61 | 0.6508 | 0.2277 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 25.80 | 0.7773 | 0.1256 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 25.80 | 0.7773 | 0.1256 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 25.44 | 0.7666 | 0.1271 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 25.44 | 0.7666 | 0.1271 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 21.52 | 0.6595 | 0.2023 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 22.29 | 0.7301 | 0.1596 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 22.29 | 0.7301 | 0.1596 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 22.40 | 0.7198 | 0.1622 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 22.40 | 0.7198 | 0.1622 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 22.00 | 0.7049 | 0.1727 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 18.75 | 0.6445 | 0.2241 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 20.41 | 0.7057 | 0.1684 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 19.75 | 0.6914 | 0.1966 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 20.13 | 0.7022 | 0.1801 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 19.92 | 0.6726 | 0.2071 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 21.20 | 0.7127 | 0.1550 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 20.82 | 0.7117 | 0.1801 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 21.08 | 0.7165 | 0.1636 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 22.57 | 0.7124 | 0.1678 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 18.99 | 0.6472 | 0.2218 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 20.02 | 0.6892 | 0.1677 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 19.86 | 0.6831 | 0.1967 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 19.93 | 0.6886 | 0.1811 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 19.41 | 0.6568 | 0.2193 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 19.93 | 0.6854 | 0.1710 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 19.96 | 0.6880 | 0.1937 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 19.90 | 0.6886 | 0.1799 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.03 | 0.7224 | 0.1295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.85 | 0.7463 | 0.1033 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.75 | 0.7418 | 0.1173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.94 | 0.7463 | 0.1087 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.28 | 0.7323 | 0.1244 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.22 | 0.7576 | 0.0951 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.08 | 0.7536 | 0.1109 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.26 | 0.7588 | 0.1016 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.80 | 0.7115 | 0.1659 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.72 | 0.7954 | 0.0804 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.07 | 0.7783 | 0.0837 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.55 | 0.7909 | 0.0819 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.00 | 0.7757 | 0.0823 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.59 | 0.7201 | 0.1266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.69 | 0.7769 | 0.0830 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.40 | 0.7656 | 0.0844 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.67 | 0.7720 | 0.0833 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.43 | 0.7628 | 0.0835 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.22 | 0.7663 | 0.0960 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 23.86 | 0.7182 | 0.1318 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.08 | 0.7516 | 0.1029 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.73 | 0.7416 | 0.1186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.98 | 0.7478 | 0.1098 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.35 | 0.7351 | 0.1261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.34 | 0.7611 | 0.0957 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.18 | 0.7560 | 0.1118 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.37 | 0.7609 | 0.1018 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.17 | 0.7649 | 0.0984 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.67 | 0.7135 | 0.1270 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.65 | 0.7401 | 0.1015 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.33 | 0.7304 | 0.1166 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.52 | 0.7356 | 0.1090 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 23.97 | 0.7241 | 0.1241 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.53 | 0.7424 | 0.1033 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.54 | 0.7401 | 0.1155 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.56 | 0.7420 | 0.1080 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.99 | 0.6930 | 0.1586 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.18 | 0.7281 | 0.1240 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.01 | 0.7238 | 0.1418 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.28 | 0.7297 | 0.1315 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.28 | 0.7052 | 0.1495 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.43 | 0.7384 | 0.1114 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.29 | 0.7358 | 0.1314 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.49 | 0.7413 | 0.1193 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.73 | 0.6627 | 0.2157 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.07 | 0.7803 | 0.1127 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.86 | 0.7745 | 0.0956 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.70 | 0.7721 | 0.1149 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.71 | 0.7716 | 0.0913 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.52 | 0.6826 | 0.1710 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.11 | 0.7627 | 0.1102 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.07 | 0.7589 | 0.0990 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.93 | 0.7529 | 0.1152 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.01 | 0.7537 | 0.1035 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.38 | 0.7405 | 0.1346 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.65 | 0.6868 | 0.1714 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.13 | 0.7332 | 0.1305 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.74 | 0.7223 | 0.1508 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.04 | 0.7305 | 0.1395 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.10 | 0.7075 | 0.1611 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.25 | 0.7398 | 0.1204 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.07 | 0.7366 | 0.1402 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.29 | 0.7414 | 0.1276 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.25 | 0.7366 | 0.1405 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.40 | 0.6756 | 0.1664 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.63 | 0.7152 | 0.1284 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.28 | 0.7053 | 0.1495 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.53 | 0.7117 | 0.1376 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.59 | 0.6863 | 0.1648 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.26 | 0.7096 | 0.1324 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.18 | 0.7098 | 0.1490 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.24 | 0.7107 | 0.1386 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 13.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.16 | 0.4943 | 0.0327 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 10.85 | 0.4380 | 0.1057 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.08 | 0.4732 | 0.0948 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.00 | 0.4712 | 0.1000 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.04 | 0.4781 | 0.0974 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.90 | 0.4660 | 0.1045 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.17 | 0.5203 | 0.0917 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.05 | 0.5082 | 0.0983 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.09 | 0.5188 | 0.0954 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.47 | 0.4731 | 0.0913 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.99 | 0.6098 | 0.0671 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.99 | 0.6098 | 0.0671 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.71 | 0.5856 | 0.0696 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.71 | 0.5856 | 0.0696 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.25 | 0.4521 | 0.0797 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 16.09 | 0.5461 | 0.0745 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 16.09 | 0.5461 | 0.0745 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 15.92 | 0.5248 | 0.0767 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 15.92 | 0.5248 | 0.0767 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 16.01 | 0.5309 | 0.0728 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 11.06 | 0.4235 | 0.1054 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 11.36 | 0.4763 | 0.0932 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 11.26 | 0.4620 | 0.0991 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 11.32 | 0.4727 | 0.0961 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 11.25 | 0.4820 | 0.1017 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 11.43 | 0.5367 | 0.0886 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 11.37 | 0.5223 | 0.0955 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 11.39 | 0.5330 | 0.0921 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.14 | 0.5340 | 0.0719 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.47 | 0.3884 | 0.1297 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.70 | 0.4173 | 0.1180 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.65 | 0.4120 | 0.1239 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.68 | 0.4165 | 0.1209 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 9.50 | 0.4173 | 0.1264 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 9.82 | 0.4486 | 0.1146 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.62 | 0.4412 | 0.1208 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.69 | 0.4467 | 0.1180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.86 | 0.5548 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.42 | 0.5849 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.49 | 0.5849 | 0.0401 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.55 | 0.5907 | 0.0383 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.05 | 0.5804 | 0.0432 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.00 | 0.6254 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.87 | 0.6165 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.98 | 0.6255 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 18.63 | 0.5553 | 0.0633 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.23 | 0.6950 | 0.0398 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.94 | 0.6713 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.67 | 0.6716 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.47 | 0.6512 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 18.51 | 0.5502 | 0.0477 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.55 | 0.6544 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.43 | 0.6400 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.10 | 0.6343 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.03 | 0.6233 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.29 | 0.6417 | 0.0381 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.27 | 0.5325 | 0.0462 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.19 | 0.5771 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.96 | 0.5647 | 0.0415 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.11 | 0.5736 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.94 | 0.5812 | 0.0430 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.91 | 0.6263 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.68 | 0.6130 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.81 | 0.6222 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.90 | 0.6215 | 0.0394 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.26 | 0.5316 | 0.0429 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.80 | 0.5607 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.70 | 0.5523 | 0.0398 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.76 | 0.5579 | 0.0380 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 18.63 | 0.5565 | 0.0408 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.19 | 0.5832 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.09 | 0.5764 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.15 | 0.5809 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.84 | 0.5531 | 0.0451 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.41 | 0.5842 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.48 | 0.5838 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.54 | 0.5897 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.01 | 0.5784 | 0.0435 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.98 | 0.6248 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.84 | 0.6152 | 0.0388 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.95 | 0.6245 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 18.63 | 0.5543 | 0.0632 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.23 | 0.6950 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.94 | 0.6714 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.67 | 0.6707 | 0.0417 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.47 | 0.6505 | 0.0407 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 18.51 | 0.5489 | 0.0477 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.55 | 0.6538 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.44 | 0.6399 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.09 | 0.6329 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.02 | 0.6225 | 0.0409 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.28 | 0.6393 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.25 | 0.5308 | 0.0465 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.19 | 0.5761 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.95 | 0.5635 | 0.0417 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.11 | 0.5726 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.91 | 0.5788 | 0.0433 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.89 | 0.6248 | 0.0330 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.66 | 0.6113 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.79 | 0.6207 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.89 | 0.6188 | 0.0397 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.24 | 0.5299 | 0.0433 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.78 | 0.5594 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.68 | 0.5507 | 0.0400 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.74 | 0.5567 | 0.0382 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 18.59 | 0.5542 | 0.0412 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.18 | 0.5815 | 0.0348 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.07 | 0.5741 | 0.0374 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.14 | 0.5790 | 0.0359 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 51.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.24 | 0.7128 | 0.0458 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 11.30 | 0.5939 | 0.2013 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.85 | 0.6285 | 0.1742 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.58 | 0.6273 | 0.1871 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.69 | 0.6313 | 0.1802 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 11.40 | 0.6092 | 0.1976 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.88 | 0.6466 | 0.1683 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.63 | 0.6447 | 0.1822 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.73 | 0.6483 | 0.1753 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 20.52 | 0.6248 | 0.1424 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 21.53 | 0.6951 | 0.1185 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 21.53 | 0.6951 | 0.1185 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 21.15 | 0.6771 | 0.1244 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 21.15 | 0.6771 | 0.1244 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 17.93 | 0.5953 | 0.1537 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 17.82 | 0.6193 | 0.1557 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 17.82 | 0.6193 | 0.1557 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 17.64 | 0.6035 | 0.1606 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 17.64 | 0.6035 | 0.1606 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.43 | 0.5749 | 0.1730 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 11.77 | 0.5885 | 0.1886 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.43 | 0.6280 | 0.1606 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.06 | 0.6217 | 0.1744 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.23 | 0.6265 | 0.1670 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 11.89 | 0.6227 | 0.1819 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 12.36 | 0.6592 | 0.1495 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 12.07 | 0.6574 | 0.1658 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 12.16 | 0.6607 | 0.1581 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.35 | 0.5875 | 0.1638 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.62 | 0.5548 | 0.2335 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.98 | 0.5803 | 0.2084 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.78 | 0.5799 | 0.2219 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.85 | 0.5820 | 0.2155 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 9.68 | 0.5726 | 0.2290 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 10.18 | 0.5947 | 0.2026 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.83 | 0.5937 | 0.2172 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.95 | 0.5948 | 0.2101 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 23.48 | 0.7215 | 0.0617 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.18 | 0.7364 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.14 | 0.7353 | 0.0569 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.23 | 0.7376 | 0.0546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.68 | 0.7303 | 0.0595 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.63 | 0.7477 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.46 | 0.7445 | 0.0545 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.56 | 0.7474 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.05 | 0.7132 | 0.0793 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.44 | 0.7660 | 0.0545 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.23 | 0.7582 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.94 | 0.7563 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.81 | 0.7503 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.02 | 0.7172 | 0.0635 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.96 | 0.7560 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.81 | 0.7493 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.52 | 0.7471 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.43 | 0.7424 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.55 | 0.7470 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 22.94 | 0.7109 | 0.0632 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.90 | 0.7311 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.65 | 0.7260 | 0.0581 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.80 | 0.7295 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.51 | 0.7282 | 0.0599 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.49 | 0.7468 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.27 | 0.7424 | 0.0545 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.40 | 0.7457 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.22 | 0.7390 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.04 | 0.7143 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 23.63 | 0.7269 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 23.52 | 0.7238 | 0.0563 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 23.59 | 0.7260 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 23.38 | 0.7229 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.97 | 0.7332 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.85 | 0.7310 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.92 | 0.7323 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.56 | 0.7049 | 0.0784 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.62 | 0.7277 | 0.0649 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.58 | 0.7277 | 0.0705 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.70 | 0.7307 | 0.0673 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.76 | 0.7137 | 0.0768 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.92 | 0.7390 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.80 | 0.7375 | 0.0681 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.90 | 0.7405 | 0.0643 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.13 | 0.6689 | 0.1076 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.75 | 0.7490 | 0.0735 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.78 | 0.7498 | 0.0616 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 23.87 | 0.7320 | 0.0774 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 23.97 | 0.7371 | 0.0647 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.14 | 0.6872 | 0.0858 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.07 | 0.7396 | 0.0698 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.07 | 0.7366 | 0.0624 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 23.19 | 0.7236 | 0.0732 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 23.25 | 0.7256 | 0.0655 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.04 | 0.7094 | 0.0886 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 21.75 | 0.6801 | 0.0861 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.96 | 0.7092 | 0.0706 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.72 | 0.7056 | 0.0772 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.87 | 0.7093 | 0.0732 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.32 | 0.7037 | 0.0814 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.43 | 0.7295 | 0.0647 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.33 | 0.7296 | 0.0716 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.46 | 0.7324 | 0.0671 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.50 | 0.6906 | 0.0974 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.92 | 0.6870 | 0.0832 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.73 | 0.7065 | 0.0718 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.68 | 0.7056 | 0.0772 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.77 | 0.7077 | 0.0740 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.36 | 0.6993 | 0.0804 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.07 | 0.7134 | 0.0686 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 22.98 | 0.7142 | 0.0743 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.05 | 0.7147 | 0.0710 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 47.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.11 | 0.6956 | 0.0435 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.51 | 0.5321 | 0.2580 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.71 | 0.5686 | 0.2355 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.64 | 0.5647 | 0.2471 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.67 | 0.5692 | 0.2414 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.55 | 0.5464 | 0.2535 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.75 | 0.5859 | 0.2310 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.66 | 0.5805 | 0.2414 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.69 | 0.5855 | 0.2364 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 20.55 | 0.6090 | 0.1360 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 21.46 | 0.6602 | 0.1167 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 21.46 | 0.6602 | 0.1167 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 21.03 | 0.6403 | 0.1218 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 21.03 | 0.6403 | 0.1218 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 18.44 | 0.5393 | 0.1545 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 18.79 | 0.5674 | 0.1544 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 18.79 | 0.5674 | 0.1544 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 18.48 | 0.5486 | 0.1582 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 18.48 | 0.5486 | 0.1582 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 18.87 | 0.5582 | 0.1503 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.09 | 0.5377 | 0.2407 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.31 | 0.5769 | 0.2173 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.21 | 0.5718 | 0.2292 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.25 | 0.5761 | 0.2235 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.15 | 0.5707 | 0.2326 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.29 | 0.6068 | 0.2092 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.24 | 0.6037 | 0.2202 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.26 | 0.6075 | 0.2148 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.98 | 0.5818 | 0.1379 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.58 | 0.5040 | 0.2734 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.76 | 0.5318 | 0.2522 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.69 | 0.5305 | 0.2639 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.71 | 0.5331 | 0.2586 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.57 | 0.5238 | 0.2680 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.79 | 0.5429 | 0.2500 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.64 | 0.5434 | 0.2598 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.69 | 0.5435 | 0.2554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.24 | 0.7018 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.04 | 0.7146 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.99 | 0.7130 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.08 | 0.7149 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.29 | 0.7064 | 0.0510 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.35 | 0.7210 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.11 | 0.7174 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.22 | 0.7199 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.43 | 0.6796 | 0.0760 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.09 | 0.7312 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.94 | 0.7259 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.47 | 0.7212 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.39 | 0.7172 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.51 | 0.6876 | 0.0595 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.75 | 0.7266 | 0.0494 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.65 | 0.7218 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.17 | 0.7172 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.11 | 0.7138 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.53 | 0.7229 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 23.81 | 0.6943 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.87 | 0.7106 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.63 | 0.7072 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.79 | 0.7098 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.25 | 0.7070 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.42 | 0.7227 | 0.0426 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.15 | 0.7187 | 0.0471 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.30 | 0.7215 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.48 | 0.7222 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.13 | 0.6993 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 24.96 | 0.7122 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.78 | 0.7088 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.90 | 0.7113 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 24.59 | 0.7078 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.40 | 0.7176 | 0.0425 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.26 | 0.7158 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.37 | 0.7170 | 0.0443 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.18 | 0.6862 | 0.0689 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.45 | 0.7060 | 0.0567 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.35 | 0.7052 | 0.0618 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.50 | 0.7077 | 0.0592 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.30 | 0.6920 | 0.0669 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.73 | 0.7145 | 0.0531 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.45 | 0.7113 | 0.0594 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.60 | 0.7143 | 0.0560 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.74 | 0.6537 | 0.0918 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.27 | 0.7162 | 0.0658 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.39 | 0.7177 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.25 | 0.6986 | 0.0705 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.41 | 0.7040 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.78 | 0.6695 | 0.0718 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.66 | 0.7129 | 0.0616 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.69 | 0.7102 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 23.59 | 0.6964 | 0.0656 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 23.66 | 0.6977 | 0.0613 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.94 | 0.7090 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.43 | 0.6639 | 0.0777 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.82 | 0.6904 | 0.0633 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.54 | 0.6871 | 0.0694 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.72 | 0.6903 | 0.0660 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.94 | 0.6848 | 0.0723 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.40 | 0.7102 | 0.0570 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.15 | 0.7072 | 0.0634 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.31 | 0.7102 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.63 | 0.7023 | 0.0657 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.78 | 0.6746 | 0.0745 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.04 | 0.6963 | 0.0620 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 23.78 | 0.6931 | 0.0682 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.99 | 0.6961 | 0.0647 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.37 | 0.6879 | 0.0701 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.42 | 0.7016 | 0.0595 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.21 | 0.7016 | 0.0645 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.34 | 0.7021 | 0.0619 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 56.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.29 | 0.6955 | 0.0247 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.75 | 0.3658 | 0.2393 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.82 | 0.3764 | 0.2289 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.77 | 0.3778 | 0.2344 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.79 | 0.3780 | 0.2317 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.72 | 0.3641 | 0.2372 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.79 | 0.3768 | 0.2275 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.75 | 0.3778 | 0.2330 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.76 | 0.3783 | 0.2304 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.65 | 0.5830 | 0.1319 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.44 | 0.5701 | 0.1383 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.44 | 0.5701 | 0.1383 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.46 | 0.5685 | 0.1385 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.46 | 0.5685 | 0.1385 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.97 | 0.2929 | 0.1595 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.96 | 0.2869 | 0.1632 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.96 | 0.2869 | 0.1632 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.95 | 0.2859 | 0.1634 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.95 | 0.2859 | 0.1634 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.93 | 0.2790 | 0.1626 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.98 | 0.3765 | 0.2256 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.06 | 0.3884 | 0.2150 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.01 | 0.3901 | 0.2207 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.03 | 0.3903 | 0.2177 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.97 | 0.3846 | 0.2233 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.02 | 0.3945 | 0.2137 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.99 | 0.3974 | 0.2187 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.00 | 0.3969 | 0.2161 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.96 | 0.3004 | 0.1546 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.48 | 0.3287 | 0.2626 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.69 | 0.3401 | 0.2541 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.59 | 0.3388 | 0.2594 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.64 | 0.3399 | 0.2571 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.35 | 0.3332 | 0.2589 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.48 | 0.3353 | 0.2512 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.38 | 0.3376 | 0.2569 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.42 | 0.3365 | 0.2546 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.19 | 0.6940 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.18 | 0.6940 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.21 | 0.6944 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.21 | 0.6943 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.19 | 0.6939 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.23 | 0.6944 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.23 | 0.6944 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.23 | 0.6945 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.29 | 0.6956 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.28 | 0.6955 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.29 | 0.6955 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.27 | 0.6953 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.28 | 0.6953 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.27 | 0.6953 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.26 | 0.6950 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.29 | 0.6955 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.26 | 0.6948 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.28 | 0.6953 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.26 | 0.6950 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.17 | 0.6939 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.23 | 0.6946 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.22 | 0.6946 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.23 | 0.6947 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.21 | 0.6945 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.26 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.25 | 0.6948 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.26 | 0.6949 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.26 | 0.6952 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.25 | 0.6951 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.23 | 0.6949 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.25 | 0.6951 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.24 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.25 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.22 | 0.6947 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.25 | 0.6950 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.24 | 0.6949 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.72 | 0.6888 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.78 | 0.6901 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.87 | 0.6909 | 0.0297 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.86 | 0.6908 | 0.0294 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.66 | 0.6884 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.85 | 0.6912 | 0.0287 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.89 | 0.6914 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.88 | 0.6914 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.24 | 0.6957 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.16 | 0.6951 | 0.0254 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.22 | 0.6951 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.14 | 0.6946 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.21 | 0.6949 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.21 | 0.6951 | 0.0255 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.12 | 0.6941 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.23 | 0.6953 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.10 | 0.6937 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.22 | 0.6951 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.10 | 0.6940 | 0.0262 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.63 | 0.6884 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.88 | 0.6913 | 0.0294 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.89 | 0.6917 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.88 | 0.6918 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.76 | 0.6912 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.99 | 0.6943 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.99 | 0.6944 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.00 | 0.6946 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.97 | 0.6946 | 0.0273 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.87 | 0.6911 | 0.0295 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.94 | 0.6924 | 0.0285 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.91 | 0.6921 | 0.0292 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.93 | 0.6924 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.98 | 0.6925 | 0.0290 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.90 | 0.6923 | 0.0286 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.91 | 0.6925 | 0.0290 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.90 | 0.6925 | 0.0289 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.19 | 0.6979 | 0.0637 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.81 | 0.4615 | 0.3498 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.92 | 0.4842 | 0.3196 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.86 | 0.4838 | 0.3356 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.88 | 0.4861 | 0.3275 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.81 | 0.4693 | 0.3440 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.90 | 0.4959 | 0.3139 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.85 | 0.4942 | 0.3293 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.87 | 0.4970 | 0.3216 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.77 | 0.6026 | 0.2666 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.87 | 0.6209 | 0.2471 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.87 | 0.6209 | 0.2471 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.79 | 0.6115 | 0.2523 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.79 | 0.6115 | 0.2523 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.38 | 0.4365 | 0.2705 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.43 | 0.4453 | 0.2693 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.43 | 0.4453 | 0.2693 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 15.36 | 0.4366 | 0.2728 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 15.36 | 0.4366 | 0.2728 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.42 | 0.4373 | 0.2680 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.07 | 0.4631 | 0.3379 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.19 | 0.4908 | 0.3074 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.13 | 0.4873 | 0.3231 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.16 | 0.4905 | 0.3152 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.09 | 0.4867 | 0.3269 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.15 | 0.5105 | 0.2963 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.12 | 0.5103 | 0.3122 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.13 | 0.5123 | 0.3042 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.57 | 0.4518 | 0.2586 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.36 | 0.4238 | 0.3836 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.58 | 0.4422 | 0.3568 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.48 | 0.4411 | 0.3720 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.53 | 0.4427 | 0.3650 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.26 | 0.4369 | 0.3754 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.42 | 0.4476 | 0.3512 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.31 | 0.4491 | 0.3643 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.35 | 0.4490 | 0.3579 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.37 | 0.7010 | 0.0795 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.86 | 0.7083 | 0.0700 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.89 | 0.7082 | 0.0746 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.94 | 0.7093 | 0.0721 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.49 | 0.7052 | 0.0777 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.23 | 0.7153 | 0.0669 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.12 | 0.7136 | 0.0725 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.20 | 0.7153 | 0.0696 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.25 | 0.7037 | 0.0962 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.97 | 0.7274 | 0.0718 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.81 | 0.7231 | 0.0710 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.61 | 0.7227 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.51 | 0.7194 | 0.0731 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.18 | 0.7040 | 0.0804 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.56 | 0.7208 | 0.0703 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.50 | 0.7181 | 0.0694 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.23 | 0.7164 | 0.0728 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.21 | 0.7146 | 0.0716 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.42 | 0.7187 | 0.0699 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.94 | 0.6959 | 0.0809 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.70 | 0.7066 | 0.0704 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.53 | 0.7039 | 0.0755 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.64 | 0.7059 | 0.0728 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.39 | 0.7049 | 0.0774 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.17 | 0.7154 | 0.0662 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.00 | 0.7129 | 0.0719 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.10 | 0.7147 | 0.0691 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.17 | 0.7148 | 0.0710 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.05 | 0.6983 | 0.0768 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.49 | 0.7045 | 0.0694 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.41 | 0.7031 | 0.0738 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.47 | 0.7042 | 0.0714 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.31 | 0.7029 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.73 | 0.7083 | 0.0674 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.67 | 0.7074 | 0.0709 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.72 | 0.7082 | 0.0692 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.57 | 0.6902 | 0.1000 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.40 | 0.7018 | 0.0854 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.40 | 0.7022 | 0.0921 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.49 | 0.7036 | 0.0884 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.70 | 0.6948 | 0.0986 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.74 | 0.7100 | 0.0813 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.61 | 0.7087 | 0.0895 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.70 | 0.7106 | 0.0850 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.73 | 0.6913 | 0.1128 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.42 | 0.7196 | 0.0870 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.46 | 0.7188 | 0.0780 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.78 | 0.7113 | 0.0920 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.87 | 0.7127 | 0.0819 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.65 | 0.6950 | 0.0940 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.85 | 0.7133 | 0.0840 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.91 | 0.7121 | 0.0777 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.17 | 0.7054 | 0.0876 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.26 | 0.7065 | 0.0816 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.02 | 0.7110 | 0.0856 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.94 | 0.6789 | 0.1082 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.00 | 0.6959 | 0.0904 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.79 | 0.6932 | 0.0989 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.93 | 0.6956 | 0.0944 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.44 | 0.6929 | 0.1028 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.50 | 0.7090 | 0.0842 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.33 | 0.7073 | 0.0926 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.44 | 0.7092 | 0.0883 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.62 | 0.7053 | 0.0892 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.13 | 0.6843 | 0.1022 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.90 | 0.6953 | 0.0892 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.76 | 0.6940 | 0.0962 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.87 | 0.6954 | 0.0925 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.52 | 0.6918 | 0.0985 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.11 | 0.6992 | 0.0872 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.01 | 0.6995 | 0.0924 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.08 | 0.6998 | 0.0896 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1277 | None | classic | 2.44 | False | 267139 | 0.326 | 71.1 | 29.27 | 0.29 | 0.020 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1277 | None | classic | 2.44 | False | 267139 | 0.326 | 75.7 | 29.27 | 0.29 | 0.020 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1277 | None | classic | 2.44 | False | 267139 | 0.326 | 63.2 | 29.27 | 0.29 | 0.020 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1277 | None | classic | 2.44 | False | 267139 | 0.326 | 69.0 | 29.27 | 0.29 | 0.020 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1153 | None | classic | 1.99 | False | 453097 | 0.663 | 148.2 | 28.60 | 0.07 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1153 | None | classic | 1.99 | False | 453097 | 0.663 | 126.1 | 28.60 | 0.07 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1153 | None | classic | 1.99 | False | 453097 | 0.663 | 98.2 | 28.60 | 0.07 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1153 | None | classic | 1.99 | False | 453097 | 0.663 | 146.8 | 28.60 | 0.07 | 0.006 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2477664 | 0.168 | 69.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2476363 | 0.800 | 72.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2476363 | 0.800 | 72.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2476363 | 0.589 | 69.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2476363 | 0.589 | 69.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2477664 | 0.168 | 78.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2476363 | 0.800 | 217.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2476363 | 0.800 | 217.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2476363 | 0.589 | 78.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2476363 | 0.589 | 78.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2459901 | 0.800 | 499.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 306671 | 0.319 | 69.5 | 28.91 | 0.47 | 0.025 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 306671 | 0.319 | 50.6 | 28.91 | 0.47 | 0.025 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 306671 | 0.319 | 73.3 | 28.91 | 0.47 | 0.025 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 306671 | 0.319 | 63.6 | 28.91 | 0.47 | 0.025 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1153 | None | classic | 1.99 | False | 424523 | 0.671 | 111.4 | 28.63 | 0.09 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1153 | None | classic | 1.99 | False | 424523 | 0.671 | 105.0 | 28.63 | 0.09 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1153 | None | classic | 1.99 | False | 424523 | 0.671 | 111.7 | 28.63 | 0.09 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1153 | None | classic | 1.99 | False | 424523 | 0.671 | 144.7 | 28.63 | 0.09 | 0.008 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2664726 | 0.800 | 140.3 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 268695 | 0.880 | 81.9 | 29.35 | 0.31 | 0.014 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 268695 | 0.880 | 75.9 | 29.35 | 0.31 | 0.014 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 268695 | 0.880 | 90.0 | 29.35 | 0.31 | 0.014 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 268695 | 0.880 | 56.3 | 29.35 | 0.31 | 0.014 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1207 | None | classic | 2.18 | False | 389552 | 0.650 | 113.2 | 28.98 | 0.20 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1207 | None | classic | 2.18 | False | 389552 | 0.650 | 109.3 | 28.98 | 0.20 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1207 | None | classic | 2.18 | False | 389552 | 0.650 | 131.7 | 28.98 | 0.20 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1207 | None | classic | 2.18 | False | 389552 | 0.650 | 110.9 | 28.98 | 0.20 | 0.009 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.650 | 0.061 |
| in035 | mask_ent | 0.652 | 0.061 |
| in035 | mask_grad | 0.451 | 0.061 |
| in035 | r_col | 0.810 | 0.061 |
| in035 | r_warp | 0.807 | 0.061 |

# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 12.1% | 18.38 / 0.0294 | 16.82 / 0.0541 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 12.5% | 18.51 / 0.0296 | 17.66 / 0.0477 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 12.3% | 18.43 / 0.0294 | 17.40 / 0.0500 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 12.3% | 18.44 / 0.0294 | 17.51 / 0.0491 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 12.1% | 18.39 / 0.0287 | 17.10 / 0.0480 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 12.4% | 18.45 / 0.0292 | 17.62 / 0.0433 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 12.2% | 18.39 / 0.0292 | 17.47 / 0.0441 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 12.2% | 18.41 / 0.0290 | 17.51 / 0.0434 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 11.5% | 18.55 / 0.0296 | 17.67 / 0.0556 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 10.0% | 18.12 / 0.0281 | 17.52 / 0.0465 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 4.0% | 16.37 / 0.0189 | 15.24 / 0.0338 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 10.0% | 18.15 / 0.0279 | 17.30 / 0.0488 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 4.0% | 16.79 / 0.0183 | 15.38 / 0.0354 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.5% | 18.55 / 0.0295 | 17.83 / 0.0416 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 9.9% | 18.06 / 0.0285 | 17.41 / 0.0424 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 4.0% | 17.15 / 0.0195 | 15.73 / 0.0308 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 9.9% | 18.09 / 0.0281 | 17.27 / 0.0456 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 4.0% | 17.42 / 0.0189 | 15.72 / 0.0329 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 13.3% | 18.52 / 0.0341 | 17.21 / 0.0597 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 18.4% | 18.44 / 0.0350 | 16.89 / 0.0713 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 19.2% | 18.58 / 0.0358 | 17.38 / 0.0619 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 18.8% | 18.49 / 0.0355 | 17.26 / 0.0662 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 18.9% | 18.52 / 0.0355 | 17.31 / 0.0636 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 18.5% | 18.44 / 0.0349 | 17.16 / 0.0659 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.3% | 18.59 / 0.0358 | 18.16 / 0.0557 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 18.9% | 18.51 / 0.0350 | 17.85 / 0.0597 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 18.9% | 18.53 / 0.0354 | 18.03 / 0.0567 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 19.4% | 18.70 / 0.0375 | 16.98 / 0.0776 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 10.6% | 18.32 / 0.0243 | 16.57 / 0.0488 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 11.6% | 18.63 / 0.0251 | 17.54 / 0.0455 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 11.1% | 18.27 / 0.0246 | 17.16 / 0.0445 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 11.3% | 18.33 / 0.0245 | 17.38 / 0.0423 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 11.6% | 18.38 / 0.0254 | 16.94 / 0.0448 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 12.9% | 18.69 / 0.0263 | 17.66 / 0.0419 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 12.1% | 18.32 / 0.0256 | 17.33 / 0.0414 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 12.4% | 18.46 / 0.0259 | 17.49 / 0.0406 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 22.74 / 0.0688 | 15.90 / 0.2158 | 14.97 / 0.0348 | 29.91 / 0.0341 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.42 / 0.0843 | 15.58 / 0.2686 | 14.70 / 0.0422 | 29.70 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.59 / 0.0771 | 16.03 / 0.2340 | 15.05 / 0.0383 | 29.70 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.57 / 0.0809 | 15.88 / 0.2538 | 14.93 / 0.0403 | 29.74 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.59 / 0.0793 | 15.98 / 0.2435 | 15.00 / 0.0396 | 29.71 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.55 / 0.0797 | 15.67 / 0.2516 | 14.89 / 0.0400 | 29.73 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.63 / 0.0742 | 16.05 / 0.2274 | 15.17 / 0.0371 | 29.68 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.64 / 0.0771 | 15.96 / 0.2389 | 15.11 / 0.0386 | 29.70 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.64 / 0.0758 | 16.04 / 0.2321 | 15.16 / 0.0380 | 29.68 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.66 / 0.0798 | 15.69 / 0.2653 | 14.88 / 0.0427 | 29.92 / 0.0341 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 22.60 / 0.0774 | 16.10 / 0.2323 | 15.03 / 0.0395 | 29.82 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 22.58 / 0.0752 | 16.07 / 0.2306 | 14.96 / 0.0394 | 29.82 / 0.0346 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 22.56 / 0.0787 | 16.05 / 0.2312 | 14.91 / 0.0399 | 29.89 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 22.55 / 0.0766 | 16.03 / 0.2251 | 14.86 / 0.0397 | 29.89 / 0.0343 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.64 / 0.0733 | 15.64 / 0.2331 | 14.83 / 0.0372 | 29.91 / 0.0343 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.57 / 0.0760 | 16.00 / 0.2252 | 15.02 / 0.0384 | 29.79 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.57 / 0.0740 | 15.96 / 0.2234 | 14.95 / 0.0382 | 29.81 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 22.55 / 0.0771 | 15.95 / 0.2312 | 14.93 / 0.0391 | 29.87 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.54 / 0.0751 | 15.90 / 0.2263 | 14.85 / 0.0390 | 29.88 / 0.0345 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.56 / 0.0769 | 15.78 / 0.2452 | 14.96 / 0.0380 | 29.77 / 0.0367 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.23 / 0.0958 | 15.67 / 0.2907 | 14.73 / 0.0467 | 29.44 / 0.0411 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.39 / 0.0860 | 15.96 / 0.2488 | 14.94 / 0.0423 | 29.54 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.38 / 0.0918 | 15.92 / 0.2704 | 14.88 / 0.0446 | 29.57 / 0.0401 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.37 / 0.0892 | 15.95 / 0.2588 | 14.90 / 0.0439 | 29.55 / 0.0398 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.43 / 0.0908 | 15.66 / 0.2802 | 14.83 / 0.0451 | 29.65 / 0.0390 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.73 / 0.0804 | 16.13 / 0.2402 | 15.23 / 0.0386 | 29.67 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.65 / 0.0863 | 15.95 / 0.2660 | 15.08 / 0.0422 | 29.72 / 0.0383 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.71 / 0.0834 | 16.09 / 0.2509 | 15.18 / 0.0405 | 29.70 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.31 / 0.0835 | 15.75 / 0.2511 | 14.85 / 0.0411 | 29.35 / 0.0391 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 22.41 / 0.0860 | 15.50 / 0.2728 | 14.78 / 0.0414 | 29.70 / 0.0375 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.57 / 0.0809 | 16.02 / 0.2391 | 15.16 / 0.0379 | 29.67 / 0.0385 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.58 / 0.0832 | 15.82 / 0.2596 | 15.03 / 0.0394 | 29.70 / 0.0377 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.60 / 0.0815 | 15.95 / 0.2486 | 15.11 / 0.0387 | 29.72 / 0.0377 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.52 / 0.0813 | 15.43 / 0.2626 | 14.79 / 0.0399 | 29.82 / 0.0370 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 22.59 / 0.0777 | 15.67 / 0.2437 | 14.95 / 0.0372 | 29.83 / 0.0376 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 22.62 / 0.0794 | 15.66 / 0.2563 | 14.93 / 0.0390 | 29.85 / 0.0372 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 22.62 / 0.0783 | 15.71 / 0.2476 | 14.96 / 0.0380 | 29.84 / 0.0374 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 12.2%） | — | — | 22.74 / 0.0688 | 15.90 / 0.2158 | 29.91 |
| in035 | rife | 5.3% | 10.6% | 22.41 / 0.0860 | 15.50 / 0.2728 | 29.70 |
| in035 | cnw_cnn | 7.9% | 12.1% | 22.42 / 0.0843 | 15.58 / 0.2686 | 29.70 |
| in035 | cnw_f5 | 12.2% | 18.4% | 22.23 / 0.0958 | 15.67 / 0.2907 | 29.44 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 20.93 / 0.0680 | +0.10 / +0.0183 (core 6.1%) | +0.10 / +0.0174 (core 8.4%) | +0.10 / +0.0294 (core 13.8%) |
| in035 | 2 | 0-3 | 19.48 / 0.0817 | -0.15 / +0.0183 (core 6.1%) | -0.13 / +0.0171 (core 8.4%) | -0.17 / +0.0311 (core 13.8%) |
| in035 | 4 | 3-5 | 27.82 / 0.0567 | -0.94 / +0.0150 (core 2.7%) | -0.94 / +0.0119 (core 4.5%) | -1.46 / +0.0205 (core 6.9%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 22.74 / 0.0688 | 15.90 | 29.91 | — |
| in035 | cnw_cnn | 不复核 | —% | 22.42 / 0.0843 | 15.58 | 29.70 | 0/3 |
| in035 | cnw_cnn | oracle | 5.0% | 22.57 / 0.0775 | 15.67 | 29.87 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 22.59 / 0.0771 | 16.03 | 29.70 | 0/3 |
| in035 | cnw_cnn | oracle | 5.0% | 22.72 / 0.0725 | 16.09 | 29.88 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 22.57 / 0.0809 | 15.88 | 29.74 | 0/3 |
| in035 | cnw_cnn | oracle | 5.0% | 22.69 / 0.0751 | 15.94 | 29.88 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 22.59 / 0.0793 | 15.98 | 29.71 | 0/3 |
| in035 | cnw_cnn | oracle | 5.0% | 22.71 / 0.0740 | 16.03 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 22.55 / 0.0797 | 15.67 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 4.8% | 22.70 / 0.0749 | 15.82 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 22.63 / 0.0742 | 16.05 | 29.68 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 4.8% | 22.80 / 0.0711 | 16.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 22.64 / 0.0771 | 15.96 | 29.70 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 4.8% | 22.81 / 0.0732 | 16.05 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 22.64 / 0.0758 | 16.04 | 29.68 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 4.8% | 22.81 / 0.0721 | 16.11 | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 22.66 / 0.0798 | 15.69 | 29.92 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 4.6% | 22.70 / 0.0771 | 15.77 | 29.91 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 22.60 / 0.0774 | 16.10 | 29.82 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 4.2% | 22.72 / 0.0729 | 16.18 | 29.90 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 22.58 / 0.0752 | 16.07 | 29.82 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 2.3% | 22.68 / 0.0727 | 16.11 | 29.90 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 22.56 / 0.0787 | 16.05 | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 4.2% | 22.66 / 0.0738 | 16.13 | 29.90 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 22.55 / 0.0766 | 16.03 | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 2.2% | 22.64 / 0.0734 | 16.07 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 22.64 / 0.0733 | 15.64 | 29.91 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 4.6% | 22.69 / 0.0715 | 15.72 | 29.91 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 22.57 / 0.0760 | 16.00 | 29.79 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 4.2% | 22.71 / 0.0717 | 16.12 | 29.89 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 22.57 / 0.0740 | 15.96 | 29.81 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 2.2% | 22.68 / 0.0714 | 16.05 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 22.55 / 0.0771 | 15.95 | 29.87 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 4.2% | 22.66 / 0.0728 | 16.07 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 22.54 / 0.0751 | 15.90 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 2.0% | 22.63 / 0.0725 | 15.99 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 22.56 / 0.0769 | 15.78 | 29.77 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 5.0% | 22.70 / 0.0711 | 15.99 | 29.89 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 22.23 / 0.0958 | 15.67 | 29.44 | 0/3 |
| in035 | cnw_f5 | oracle | 6.7% | 22.56 / 0.0826 | 15.81 | 29.85 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 22.39 / 0.0860 | 15.96 | 29.54 | 0/3 |
| in035 | cnw_f5 | oracle | 6.7% | 22.65 / 0.0767 | 16.05 | 29.86 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 22.38 / 0.0918 | 15.92 | 29.57 | 0/3 |
| in035 | cnw_f5 | oracle | 6.7% | 22.63 / 0.0802 | 16.00 | 29.85 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 22.37 / 0.0892 | 15.95 | 29.55 | 0/3 |
| in035 | cnw_f5 | oracle | 6.7% | 22.63 / 0.0788 | 16.03 | 29.85 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 22.43 / 0.0908 | 15.66 | 29.65 | 0/3 |
| in035 | cnw_f5_mw | oracle | 6.6% | 22.69 / 0.0802 | 15.84 | 29.87 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 22.73 / 0.0804 | 16.13 | 29.67 | 0/3 |
| in035 | cnw_f5_mw | oracle | 6.6% | 22.88 / 0.0734 | 16.22 | 29.88 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 22.65 / 0.0863 | 15.95 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | oracle | 6.6% | 22.83 / 0.0775 | 16.06 | 29.89 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 22.71 / 0.0834 | 16.09 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | oracle | 6.6% | 22.87 / 0.0755 | 16.18 | 29.88 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 22.31 / 0.0835 | 15.75 | 29.35 | 0/3 |
| in035 | cnw_f5_pix | oracle | 6.6% | 22.60 / 0.0738 | 15.98 | 29.85 | 0/3 |
| in035 | rife | 不复核 | —% | 22.41 / 0.0860 | 15.50 | 29.70 | 0/3 |
| in035 | rife | oracle | 4.3% | 22.61 / 0.0758 | 15.67 | 29.89 | 0/3 |
| in035 | rife | 不复核 | —% | 22.57 / 0.0809 | 16.02 | 29.67 | 0/3 |
| in035 | rife | oracle | 4.4% | 22.76 / 0.0719 | 16.13 | 29.91 | 0/3 |
| in035 | rife | 不复核 | —% | 22.58 / 0.0832 | 15.82 | 29.70 | 0/3 |
| in035 | rife | oracle | 4.5% | 22.74 / 0.0741 | 15.94 | 29.90 | 0/3 |
| in035 | rife | 不复核 | —% | 22.60 / 0.0815 | 15.95 | 29.72 | 0/3 |
| in035 | rife | oracle | 4.5% | 22.76 / 0.0730 | 16.05 | 29.90 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 22.52 / 0.0813 | 15.43 | 29.82 | 0/3 |
| in035 | rife_mw | oracle | 4.5% | 22.65 / 0.0742 | 15.67 | 29.89 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 22.59 / 0.0777 | 15.67 | 29.83 | 0/3 |
| in035 | rife_mw | oracle | 4.7% | 22.68 / 0.0713 | 15.84 | 29.89 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 22.62 / 0.0794 | 15.66 | 29.85 | 0/3 |
| in035 | rife_mw | oracle | 4.6% | 22.71 / 0.0731 | 15.84 | 29.90 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 22.62 / 0.0783 | 15.71 | 29.84 | 0/3 |
| in035 | rife_mw | oracle | 4.6% | 22.71 / 0.0721 | 15.88 | 29.90 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 22.74 / 0.0688 | 15.90 / 0.2158 | — |
| in035 | FF | 0（前馈） | 1008×563（53%） | 25.86 | 22.42 / 0.0843 | 15.58 / 0.2686 | 0/3 |
| in035 | 25 | 1.39 s | 1008×563（53%） | 26.54 | 22.57 / 0.0809 | 15.88 / 0.2538 | 0/3 |
| in035 | 50 | 2.81 s | 1008×563（53%） | 26.89 | 22.59 / 0.0793 | 15.98 / 0.2435 | 0/3 |
| in035 | 100 | 5.53 s | 1008×563（53%） | 27.22 | 22.59 / 0.0771 | 16.03 / 0.2340 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 22.74 / 0.0688 | 15.90 / 0.2158 | 29.91 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 22.42 / 0.0843 | 15.58 / 0.2686 | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 22.57 / 0.0775 | 15.67 / 0.2575 | 29.87 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 22.57 / 0.0809 | 15.88 / 0.2538 | 29.74 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 22.69 / 0.0751 | 15.94 / 0.2454 | 29.88 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 22.59 / 0.0793 | 15.98 / 0.2435 | 29.71 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 22.71 / 0.0740 | 16.03 / 0.2354 | 29.88 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 22.59 / 0.0771 | 16.03 / 0.2340 | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 22.72 / 0.0725 | 16.09 / 0.2267 | 29.88 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 22.55 / 0.0797 | 15.67 / 0.2516 | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 22.70 / 0.0749 | 15.82 / 0.2409 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 22.64 / 0.0771 | 15.96 / 0.2389 | 29.70 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 22.81 / 0.0732 | 16.05 / 0.2309 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 22.64 / 0.0758 | 16.04 / 0.2321 | 29.68 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 22.81 / 0.0721 | 16.11 / 0.2251 | 29.89 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 22.63 / 0.0742 | 16.05 / 0.2274 | 29.68 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 22.80 / 0.0711 | 16.12 / 0.2217 | 29.88 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 22.23 / 0.0958 | 15.67 / 0.2907 | 29.44 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 22.56 / 0.0826 | 15.81 / 0.2757 | 29.85 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 22.38 / 0.0918 | 15.92 / 0.2704 | 29.57 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 22.63 / 0.0802 | 16.00 / 0.2600 | 29.85 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 22.37 / 0.0892 | 15.95 / 0.2588 | 29.55 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 22.63 / 0.0788 | 16.03 / 0.2502 | 29.85 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 22.39 / 0.0860 | 15.96 / 0.2488 | 29.54 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 22.65 / 0.0767 | 16.05 / 0.2410 | 29.86 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 22.43 / 0.0908 | 15.66 / 0.2802 | 29.65 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 22.69 / 0.0802 | 15.84 / 0.2646 | 29.87 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 22.65 / 0.0863 | 15.95 / 0.2660 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 22.83 / 0.0775 | 16.06 / 0.2538 | 29.89 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 22.71 / 0.0834 | 16.09 / 0.2509 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 22.87 / 0.0755 | 16.18 / 0.2410 | 29.88 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 22.73 / 0.0804 | 16.13 / 0.2402 | 29.67 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 22.88 / 0.0734 | 16.22 / 0.2310 | 29.88 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 22.41 / 0.0860 | 15.50 / 0.2728 | 29.70 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 22.61 / 0.0758 | 15.67 / 0.2560 | 29.89 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 22.58 / 0.0832 | 15.82 / 0.2596 | 29.70 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 22.74 / 0.0741 | 15.94 / 0.2458 | 29.90 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 22.60 / 0.0815 | 15.95 / 0.2486 | 29.72 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 22.76 / 0.0730 | 16.05 / 0.2367 | 29.90 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 22.57 / 0.0809 | 16.02 / 0.2391 | 29.67 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 22.76 / 0.0719 | 16.13 / 0.2284 | 29.91 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 22.52 / 0.0813 | 15.43 / 0.2626 | 29.82 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 22.65 / 0.0742 | 15.67 / 0.2450 | 29.89 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 22.62 / 0.0794 | 15.66 / 0.2563 | 29.85 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 22.71 / 0.0731 | 15.84 / 0.2410 | 29.90 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 22.62 / 0.0783 | 15.71 / 0.2476 | 29.84 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 22.71 / 0.0721 | 15.88 / 0.2343 | 29.90 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 22.59 / 0.0777 | 15.67 / 0.2437 | 29.83 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 22.68 / 0.0713 | 15.84 / 0.2306 | 29.89 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 15.90 / 0.2158 | 14.97 / 0.0348 | 29.91 / 0.0341 | 22.74 / 0.0688 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 12.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 15.90 | 0.5948 | 0.2158 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 12.91 | 0.5212 | 0.3855 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 13.00 | 0.5895 | 0.3116 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 12.96 | 0.5655 | 0.3584 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 12.97 | 0.5796 | 0.3376 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 12.76 | 0.4946 | 0.3590 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 12.98 | 0.5720 | 0.3029 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 12.75 | 0.5420 | 0.3374 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 12.80 | 0.5577 | 0.3207 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.51 | 0.6032 | 0.2873 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.88 | 0.6437 | 0.2573 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.88 | 0.6437 | 0.2573 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.84 | 0.6369 | 0.2560 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.84 | 0.6369 | 0.2560 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.30 | 0.5833 | 0.2805 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.24 | 0.5815 | 0.3083 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.24 | 0.5815 | 0.3083 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.27 | 0.5738 | 0.3144 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.27 | 0.5738 | 0.3144 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.06 | 0.5507 | 0.3143 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 13.45 | 0.5302 | 0.3688 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 13.49 | 0.5903 | 0.3023 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 13.51 | 0.5742 | 0.3386 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 13.48 | 0.5837 | 0.3214 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 13.41 | 0.5025 | 0.3569 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 13.50 | 0.5828 | 0.2927 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 13.45 | 0.5472 | 0.3315 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 13.46 | 0.5665 | 0.3131 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.33 | 0.5676 | 0.3007 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.30 | 0.5070 | 0.4065 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.47 | 0.5697 | 0.3346 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.36 | 0.5480 | 0.3777 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.42 | 0.5604 | 0.3554 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.21 | 0.4693 | 0.3775 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 12.42 | 0.5184 | 0.3292 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 12.20 | 0.5041 | 0.3582 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 12.30 | 0.5130 | 0.3428 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 15.67 | 0.5927 | 0.2575 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 16.09 | 0.6208 | 0.2267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 15.94 | 0.6121 | 0.2454 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 16.03 | 0.6178 | 0.2354 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 15.82 | 0.5776 | 0.2409 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 16.12 | 0.6180 | 0.2217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 16.05 | 0.6034 | 0.2309 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 16.11 | 0.6126 | 0.2251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 15.77 | 0.5916 | 0.2526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 16.18 | 0.6194 | 0.2244 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 16.11 | 0.6129 | 0.2249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 16.13 | 0.6190 | 0.2218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 16.07 | 0.6126 | 0.2197 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 15.72 | 0.6028 | 0.2255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 16.12 | 0.6177 | 0.2195 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 16.05 | 0.6119 | 0.2198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 16.07 | 0.6140 | 0.2227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 15.99 | 0.6078 | 0.2207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 15.99 | 0.6126 | 0.2265 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 15.81 | 0.5935 | 0.2757 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 16.05 | 0.6266 | 0.2410 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 16.00 | 0.6168 | 0.2600 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 16.03 | 0.6226 | 0.2502 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 15.84 | 0.5751 | 0.2646 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 16.22 | 0.6319 | 0.2310 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 16.06 | 0.6038 | 0.2538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 16.18 | 0.6206 | 0.2410 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 15.98 | 0.6200 | 0.2280 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 15.67 | 0.5916 | 0.2560 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 16.13 | 0.6263 | 0.2284 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 15.94 | 0.6127 | 0.2458 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 16.05 | 0.6208 | 0.2367 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 15.67 | 0.5726 | 0.2450 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 15.84 | 0.6032 | 0.2306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 15.84 | 0.5923 | 0.2410 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 15.88 | 0.6000 | 0.2343 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 15.58 | 0.5773 | 0.2686 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 16.03 | 0.6123 | 0.2340 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 15.88 | 0.6026 | 0.2538 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 15.98 | 0.6094 | 0.2435 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 15.67 | 0.5632 | 0.2516 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 16.05 | 0.6136 | 0.2274 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 15.96 | 0.5962 | 0.2389 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 16.04 | 0.6067 | 0.2321 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 15.69 | 0.5783 | 0.2653 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 16.10 | 0.6148 | 0.2323 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 16.07 | 0.6105 | 0.2306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 16.05 | 0.6121 | 0.2312 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 16.03 | 0.6103 | 0.2251 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 15.64 | 0.5929 | 0.2331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 16.00 | 0.6128 | 0.2252 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 15.96 | 0.6085 | 0.2234 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 15.95 | 0.6068 | 0.2312 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 15.90 | 0.6043 | 0.2263 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 15.78 | 0.5972 | 0.2452 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 15.67 | 0.5749 | 0.2907 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 15.96 | 0.6176 | 0.2488 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 15.92 | 0.6059 | 0.2704 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 15.95 | 0.6136 | 0.2588 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 15.66 | 0.5563 | 0.2802 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 16.13 | 0.6230 | 0.2402 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 15.95 | 0.5926 | 0.2660 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 16.09 | 0.6108 | 0.2509 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 15.75 | 0.6022 | 0.2511 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 15.50 | 0.5746 | 0.2728 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 16.02 | 0.6189 | 0.2391 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 15.82 | 0.6020 | 0.2596 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 15.95 | 0.6121 | 0.2486 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 15.43 | 0.5519 | 0.2626 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 15.67 | 0.5898 | 0.2437 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 15.66 | 0.5785 | 0.2563 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 15.71 | 0.5870 | 0.2476 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 12.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 14.97 | 0.5468 | 0.0348 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.66 | 0.3804 | 0.1289 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.05 | 0.4429 | 0.1197 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.82 | 0.4182 | 0.1256 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.94 | 0.4329 | 0.1232 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.55 | 0.3690 | 0.1257 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.52 | 0.4282 | 0.1192 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.53 | 0.4051 | 0.1232 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.52 | 0.4183 | 0.1217 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.46 | 0.4719 | 0.0804 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 13.43 | 0.4805 | 0.0775 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 13.43 | 0.4805 | 0.0775 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 13.36 | 0.4724 | 0.0785 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 13.36 | 0.4724 | 0.0785 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.10 | 0.4393 | 0.0831 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.01 | 0.4279 | 0.0876 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.01 | 0.4279 | 0.0876 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.99 | 0.4194 | 0.0895 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.99 | 0.4194 | 0.0895 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.93 | 0.4099 | 0.0876 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.73 | 0.4039 | 0.1092 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.94 | 0.4571 | 0.1001 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.84 | 0.4398 | 0.1053 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.89 | 0.4488 | 0.1034 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.70 | 0.3897 | 0.1067 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.71 | 0.4681 | 0.0972 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.69 | 0.4316 | 0.1030 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.70 | 0.4514 | 0.1007 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.31 | 0.4449 | 0.0758 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.93 | 0.3345 | 0.1395 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.21 | 0.3917 | 0.1295 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.02 | 0.3695 | 0.1353 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.09 | 0.3820 | 0.1328 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.83 | 0.3101 | 0.1373 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.96 | 0.3551 | 0.1300 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.85 | 0.3391 | 0.1348 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.91 | 0.3489 | 0.1328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 14.70 | 0.5410 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 15.05 | 0.5724 | 0.0383 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 14.93 | 0.5626 | 0.0401 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 15.00 | 0.5687 | 0.0394 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 14.90 | 0.5371 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 15.17 | 0.5803 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 15.11 | 0.5645 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 15.16 | 0.5743 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 14.88 | 0.5503 | 0.0428 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 15.05 | 0.5692 | 0.0394 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 14.97 | 0.5602 | 0.0393 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 14.92 | 0.5638 | 0.0399 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 14.87 | 0.5562 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 14.83 | 0.5572 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 15.03 | 0.5660 | 0.0383 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 14.96 | 0.5576 | 0.0381 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 14.94 | 0.5594 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 14.86 | 0.5512 | 0.0389 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 14.96 | 0.5643 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 14.73 | 0.5344 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 14.94 | 0.5689 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 14.88 | 0.5581 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 14.91 | 0.5640 | 0.0437 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 14.83 | 0.5254 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 15.24 | 0.5900 | 0.0383 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 15.08 | 0.5588 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 15.18 | 0.5771 | 0.0403 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 14.86 | 0.5573 | 0.0409 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 14.78 | 0.5436 | 0.0412 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 15.16 | 0.5773 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 15.03 | 0.5651 | 0.0393 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 15.11 | 0.5722 | 0.0385 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 14.80 | 0.5255 | 0.0397 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 14.96 | 0.5614 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 14.94 | 0.5470 | 0.0389 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 14.97 | 0.5563 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 14.70 | 0.5397 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 15.05 | 0.5716 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 14.93 | 0.5615 | 0.0403 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 15.00 | 0.5677 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 14.89 | 0.5361 | 0.0400 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 15.17 | 0.5799 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 15.11 | 0.5639 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 15.16 | 0.5736 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 14.88 | 0.5495 | 0.0427 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 15.03 | 0.5687 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 14.96 | 0.5599 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 14.91 | 0.5633 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 14.86 | 0.5556 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 14.83 | 0.5564 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 15.02 | 0.5655 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 14.95 | 0.5572 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 14.93 | 0.5588 | 0.0391 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 14.85 | 0.5507 | 0.0390 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 14.96 | 0.5623 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 14.73 | 0.5329 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 14.94 | 0.5678 | 0.0423 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 14.88 | 0.5569 | 0.0446 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 14.90 | 0.5628 | 0.0439 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 14.83 | 0.5236 | 0.0451 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 15.23 | 0.5888 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 15.08 | 0.5576 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 15.18 | 0.5758 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 14.85 | 0.5547 | 0.0411 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 14.78 | 0.5422 | 0.0414 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 15.16 | 0.5768 | 0.0379 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 15.03 | 0.5643 | 0.0394 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 15.11 | 0.5717 | 0.0387 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 14.79 | 0.5237 | 0.0399 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 14.95 | 0.5606 | 0.0372 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 14.93 | 0.5461 | 0.0390 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 14.96 | 0.5555 | 0.0380 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 33.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.58 | 0.7122 | 0.0379 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.65 | 0.4349 | 0.2449 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.88 | 0.4690 | 0.2302 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.73 | 0.4593 | 0.2390 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.79 | 0.4646 | 0.2351 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.58 | 0.4390 | 0.2405 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.76 | 0.4744 | 0.2268 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.63 | 0.4677 | 0.2352 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.67 | 0.4719 | 0.2318 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.89 | 0.5702 | 0.1334 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.58 | 0.5663 | 0.1368 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.58 | 0.5663 | 0.1368 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.56 | 0.5554 | 0.1402 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.56 | 0.5554 | 0.1402 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.54 | 0.4403 | 0.1637 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.01 | 0.3862 | 0.1847 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.01 | 0.3862 | 0.1847 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.03 | 0.3780 | 0.1867 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.03 | 0.3780 | 0.1867 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.86 | 0.3421 | 0.1918 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.14 | 0.4771 | 0.2083 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.38 | 0.5115 | 0.1916 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.25 | 0.5051 | 0.2013 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.30 | 0.5081 | 0.1968 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.19 | 0.4927 | 0.2015 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.46 | 0.5453 | 0.1815 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.28 | 0.5278 | 0.1930 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.35 | 0.5368 | 0.1875 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.89 | 0.4097 | 0.1695 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.67 | 0.4256 | 0.2452 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.97 | 0.4611 | 0.2290 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.78 | 0.4526 | 0.2392 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.86 | 0.4577 | 0.2346 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.70 | 0.4195 | 0.2396 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.95 | 0.4549 | 0.2254 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.77 | 0.4461 | 0.2337 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.84 | 0.4518 | 0.2297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.24 | 0.7040 | 0.0463 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.56 | 0.7182 | 0.0426 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.48 | 0.7148 | 0.0443 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.53 | 0.7171 | 0.0435 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.42 | 0.7025 | 0.0441 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.70 | 0.7226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.65 | 0.7159 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.70 | 0.7200 | 0.0413 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.37 | 0.7029 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.55 | 0.7142 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.50 | 0.7105 | 0.0418 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.40 | 0.7111 | 0.0428 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.37 | 0.7087 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.36 | 0.7101 | 0.0413 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.55 | 0.7141 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.49 | 0.7109 | 0.0403 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.43 | 0.7104 | 0.0419 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.37 | 0.7079 | 0.0414 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.37 | 0.7049 | 0.0425 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.12 | 0.6952 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.37 | 0.7120 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.31 | 0.7071 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.33 | 0.7095 | 0.0479 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.28 | 0.6946 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.76 | 0.7268 | 0.0426 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.59 | 0.7126 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.69 | 0.7207 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.20 | 0.6965 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.26 | 0.7061 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.66 | 0.7215 | 0.0414 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.54 | 0.7174 | 0.0432 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.62 | 0.7203 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.35 | 0.7018 | 0.0429 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.49 | 0.7168 | 0.0402 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.49 | 0.7115 | 0.0418 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.51 | 0.7150 | 0.0407 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.80 | 0.6827 | 0.0534 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.22 | 0.7023 | 0.0484 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.14 | 0.6988 | 0.0505 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.19 | 0.7012 | 0.0494 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.01 | 0.6843 | 0.0500 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.27 | 0.7089 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.24 | 0.7041 | 0.0475 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.27 | 0.7076 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.16 | 0.6828 | 0.0560 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.29 | 0.6997 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.30 | 0.7001 | 0.0474 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.13 | 0.6940 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.14 | 0.6966 | 0.0491 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.19 | 0.6966 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.27 | 0.7009 | 0.0473 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.27 | 0.7007 | 0.0449 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.15 | 0.6949 | 0.0499 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.14 | 0.6970 | 0.0472 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 18.70 | 0.6699 | 0.0594 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.51 | 0.6572 | 0.0630 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.75 | 0.6800 | 0.0563 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.72 | 0.6770 | 0.0595 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.73 | 0.6789 | 0.0580 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.69 | 0.6651 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.31 | 0.7051 | 0.0520 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.12 | 0.6923 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.19 | 0.7004 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.18 | 0.6339 | 0.0723 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.64 | 0.6818 | 0.0555 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.04 | 0.7007 | 0.0528 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.03 | 0.6993 | 0.0531 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.12 | 0.7025 | 0.0520 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 18.82 | 0.6769 | 0.0532 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.02 | 0.6968 | 0.0507 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.04 | 0.6942 | 0.0512 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.07 | 0.6976 | 0.0504 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 43.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.56 | 0.7214 | 0.0444 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.11 | 0.3689 | 0.3770 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.18 | 0.3893 | 0.3669 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.14 | 0.3837 | 0.3733 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.16 | 0.3866 | 0.3708 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.12 | 0.3795 | 0.3731 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.15 | 0.4006 | 0.3628 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.13 | 0.3959 | 0.3696 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.14 | 0.3989 | 0.3670 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.99 | 0.5645 | 0.1923 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.76 | 0.5581 | 0.2012 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.76 | 0.5581 | 0.2012 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.78 | 0.5548 | 0.2027 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.78 | 0.5548 | 0.2027 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.77 | 0.3087 | 0.2417 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.62 | 0.2881 | 0.2492 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.62 | 0.2881 | 0.2492 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.64 | 0.2848 | 0.2527 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.64 | 0.2848 | 0.2527 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.63 | 0.2778 | 0.2489 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.44 | 0.4280 | 0.3434 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.52 | 0.4490 | 0.3297 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.48 | 0.4464 | 0.3378 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.49 | 0.4477 | 0.3343 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.46 | 0.4487 | 0.3373 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.54 | 0.4802 | 0.3219 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.49 | 0.4703 | 0.3316 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.51 | 0.4758 | 0.3274 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.20 | 0.3871 | 0.2220 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.20 | 0.3622 | 0.3846 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.40 | 0.3867 | 0.3726 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.26 | 0.3793 | 0.3801 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.31 | 0.3829 | 0.3770 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.22 | 0.3708 | 0.3775 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.28 | 0.3914 | 0.3670 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.24 | 0.3862 | 0.3735 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.26 | 0.3892 | 0.3706 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.36 | 0.7166 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.58 | 0.7247 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.57 | 0.7229 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.59 | 0.7241 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.50 | 0.7159 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.69 | 0.7275 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.71 | 0.7239 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.72 | 0.7263 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.36 | 0.7165 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 22.56 | 0.7228 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 22.49 | 0.7205 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 22.48 | 0.7213 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 22.44 | 0.7196 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.35 | 0.7205 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.56 | 0.7227 | 0.0469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.50 | 0.7208 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 22.50 | 0.7208 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.43 | 0.7193 | 0.0477 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 22.54 | 0.7216 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 22.19 | 0.7100 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.35 | 0.7192 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.34 | 0.7170 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.33 | 0.7181 | 0.0511 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.27 | 0.7095 | 0.0519 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.67 | 0.7281 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.56 | 0.7199 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.64 | 0.7248 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 22.34 | 0.7157 | 0.0490 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 22.37 | 0.7185 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.66 | 0.7275 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 22.61 | 0.7252 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.65 | 0.7268 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 22.41 | 0.7157 | 0.0477 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 22.48 | 0.7248 | 0.0451 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 22.52 | 0.7215 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 22.51 | 0.7236 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.07 | 0.7048 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.34 | 0.7164 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.33 | 0.7137 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.35 | 0.7151 | 0.0526 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.20 | 0.7077 | 0.0528 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.35 | 0.7227 | 0.0488 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.37 | 0.7189 | 0.0507 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.36 | 0.7214 | 0.0497 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.26 | 0.7123 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 22.35 | 0.7166 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 22.33 | 0.7155 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 22.31 | 0.7154 | 0.0536 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 22.31 | 0.7156 | 0.0515 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.24 | 0.7171 | 0.0487 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.30 | 0.7162 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.28 | 0.7154 | 0.0490 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 22.28 | 0.7149 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.27 | 0.7153 | 0.0503 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.28 | 0.7125 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 21.64 | 0.6866 | 0.0639 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.87 | 0.7012 | 0.0573 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.89 | 0.6988 | 0.0609 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.85 | 0.7000 | 0.0592 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.83 | 0.6945 | 0.0599 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.37 | 0.7191 | 0.0518 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.23 | 0.7105 | 0.0562 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.32 | 0.7157 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.83 | 0.6953 | 0.0572 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.99 | 0.7070 | 0.0580 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.29 | 0.7195 | 0.0538 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.27 | 0.7165 | 0.0554 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.31 | 0.7186 | 0.0544 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.16 | 0.7067 | 0.0538 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 22.34 | 0.7193 | 0.0503 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 22.34 | 0.7160 | 0.0517 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 22.35 | 0.7183 | 0.0507 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 73.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.91 | 0.7219 | 0.0341 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.58 | 0.3059 | 0.3747 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.64 | 0.3095 | 0.3688 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.60 | 0.3096 | 0.3721 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.62 | 0.3095 | 0.3705 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.56 | 0.3076 | 0.3727 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.58 | 0.3104 | 0.3672 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.56 | 0.3115 | 0.3705 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.57 | 0.3111 | 0.3691 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.09 | 0.5295 | 0.2408 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.32 | 0.5356 | 0.2540 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.32 | 0.5356 | 0.2540 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.35 | 0.5368 | 0.2537 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.35 | 0.5368 | 0.2537 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.44 | 0.1516 | 0.2722 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.43 | 0.1460 | 0.2747 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.43 | 0.1460 | 0.2747 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.44 | 0.1465 | 0.2747 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.44 | 0.1465 | 0.2747 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.42 | 0.1411 | 0.2767 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.37 | 0.3563 | 0.3413 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.42 | 0.3610 | 0.3310 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.39 | 0.3629 | 0.3375 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.40 | 0.3624 | 0.3346 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.37 | 0.3672 | 0.3357 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.41 | 0.3713 | 0.3260 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.38 | 0.3726 | 0.3320 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.40 | 0.3718 | 0.3292 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.46 | 0.2385 | 0.2466 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.53 | 0.2922 | 0.3810 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.70 | 0.2986 | 0.3749 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.57 | 0.2959 | 0.3788 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.62 | 0.2968 | 0.3771 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.53 | 0.2969 | 0.3762 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.57 | 0.3009 | 0.3702 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.54 | 0.3013 | 0.3739 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.56 | 0.3012 | 0.3722 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.87 | 0.7215 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.88 | 0.7217 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.88 | 0.7216 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.88 | 0.7217 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.89 | 0.7217 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7217 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.89 | 0.7217 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.89 | 0.7217 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.91 | 0.7220 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.90 | 0.7217 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.90 | 0.7217 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.90 | 0.7218 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.90 | 0.7218 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.91 | 0.7219 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.89 | 0.7217 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.90 | 0.7217 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.90 | 0.7218 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.90 | 0.7218 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.89 | 0.7217 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.85 | 0.7213 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.86 | 0.7215 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.85 | 0.7215 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.85 | 0.7215 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.87 | 0.7215 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7217 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.89 | 0.7217 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.88 | 0.7217 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.85 | 0.7213 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.89 | 0.7215 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.91 | 0.7218 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.90 | 0.7216 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.90 | 0.7217 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.89 | 0.7216 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.89 | 0.7217 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.90 | 0.7217 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.90 | 0.7217 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.70 | 0.7204 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.70 | 0.7205 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.74 | 0.7209 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.71 | 0.7206 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.73 | 0.7209 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.68 | 0.7213 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.70 | 0.7214 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.68 | 0.7214 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.92 | 0.7224 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.82 | 0.7214 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.82 | 0.7212 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.89 | 0.7218 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.89 | 0.7216 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.91 | 0.7223 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.79 | 0.7212 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.81 | 0.7211 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.87 | 0.7216 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.88 | 0.7215 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.77 | 0.7211 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.44 | 0.7187 | 0.0411 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.54 | 0.7195 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.57 | 0.7202 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.55 | 0.7199 | 0.0398 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.65 | 0.7203 | 0.0390 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.67 | 0.7208 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.72 | 0.7214 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.70 | 0.7212 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.35 | 0.7190 | 0.0391 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.70 | 0.7198 | 0.0375 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.67 | 0.7197 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.70 | 0.7201 | 0.0377 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.72 | 0.7202 | 0.0377 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.82 | 0.7207 | 0.0370 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.83 | 0.7210 | 0.0376 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.85 | 0.7214 | 0.0372 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.84 | 0.7213 | 0.0374 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.74 | 0.7087 | 0.0688 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.39 | 0.3291 | 0.4657 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.46 | 0.3435 | 0.4483 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.41 | 0.3393 | 0.4597 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.43 | 0.3416 | 0.4547 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.36 | 0.3332 | 0.4565 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.38 | 0.3457 | 0.4414 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.37 | 0.3434 | 0.4515 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.37 | 0.3448 | 0.4474 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.95 | 0.5290 | 0.3556 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.01 | 0.5281 | 0.3632 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.01 | 0.5281 | 0.3632 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.03 | 0.5273 | 0.3654 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.03 | 0.5273 | 0.3654 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.53 | 0.2269 | 0.3732 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.47 | 0.2130 | 0.3802 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.47 | 0.2130 | 0.3802 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.48 | 0.2121 | 0.3835 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.48 | 0.2121 | 0.3835 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.44 | 0.2053 | 0.3809 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.25 | 0.3784 | 0.4268 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.31 | 0.3930 | 0.4040 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.28 | 0.3913 | 0.4187 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.29 | 0.3923 | 0.4118 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.26 | 0.3912 | 0.4161 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.31 | 0.4096 | 0.3937 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.28 | 0.4045 | 0.4075 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.29 | 0.4070 | 0.4013 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.44 | 0.2950 | 0.3343 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.32 | 0.3121 | 0.4776 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.49 | 0.3277 | 0.4621 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.37 | 0.3224 | 0.4718 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.42 | 0.3248 | 0.4677 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.32 | 0.3158 | 0.4642 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.36 | 0.3281 | 0.4507 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.33 | 0.3253 | 0.4593 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.35 | 0.3269 | 0.4554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.57 | 0.7060 | 0.0775 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.72 | 0.7105 | 0.0725 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.69 | 0.7093 | 0.0751 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.71 | 0.7101 | 0.0740 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.70 | 0.7059 | 0.0749 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.80 | 0.7120 | 0.0711 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.81 | 0.7099 | 0.0732 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.81 | 0.7111 | 0.0721 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.70 | 0.7078 | 0.0771 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 22.72 | 0.7096 | 0.0729 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 22.68 | 0.7084 | 0.0727 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 22.66 | 0.7090 | 0.0738 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 22.64 | 0.7080 | 0.0734 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.69 | 0.7094 | 0.0715 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.71 | 0.7095 | 0.0717 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.68 | 0.7085 | 0.0714 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 22.66 | 0.7086 | 0.0728 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.63 | 0.7078 | 0.0725 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 22.70 | 0.7094 | 0.0711 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 22.56 | 0.7030 | 0.0826 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.65 | 0.7085 | 0.0767 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.63 | 0.7069 | 0.0802 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.63 | 0.7077 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.69 | 0.7030 | 0.0802 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.88 | 0.7130 | 0.0734 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.83 | 0.7085 | 0.0775 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.87 | 0.7111 | 0.0755 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 22.60 | 0.7065 | 0.0738 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 22.61 | 0.7067 | 0.0758 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.76 | 0.7117 | 0.0719 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 22.74 | 0.7100 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.76 | 0.7110 | 0.0730 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 22.65 | 0.7051 | 0.0742 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 22.68 | 0.7098 | 0.0713 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 22.71 | 0.7080 | 0.0731 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 22.71 | 0.7091 | 0.0721 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.42 | 0.7001 | 0.0843 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.59 | 0.7063 | 0.0771 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.57 | 0.7048 | 0.0809 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.59 | 0.7056 | 0.0793 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.55 | 0.7019 | 0.0797 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.63 | 0.7099 | 0.0742 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.64 | 0.7076 | 0.0771 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.64 | 0.7090 | 0.0758 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.66 | 0.7061 | 0.0798 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 22.60 | 0.7066 | 0.0774 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 22.58 | 0.7057 | 0.0752 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 22.56 | 0.7062 | 0.0787 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 22.55 | 0.7059 | 0.0766 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.64 | 0.7081 | 0.0733 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.57 | 0.7064 | 0.0760 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.57 | 0.7057 | 0.0740 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 22.55 | 0.7058 | 0.0771 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.54 | 0.7057 | 0.0751 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.56 | 0.7053 | 0.0769 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.23 | 0.6911 | 0.0958 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.39 | 0.6995 | 0.0860 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.38 | 0.6978 | 0.0918 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.37 | 0.6986 | 0.0892 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.43 | 0.6955 | 0.0908 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.73 | 0.7086 | 0.0804 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.65 | 0.7040 | 0.0863 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.71 | 0.7067 | 0.0834 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.31 | 0.6962 | 0.0835 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.41 | 0.7009 | 0.0860 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.57 | 0.7073 | 0.0809 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.58 | 0.7057 | 0.0832 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.60 | 0.7070 | 0.0815 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.52 | 0.7008 | 0.0813 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 22.59 | 0.7070 | 0.0777 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 22.62 | 0.7054 | 0.0794 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 22.62 | 0.7066 | 0.0783 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 321156 | 0.322 | 69.4 | 28.93 | 0.33 | 0.034 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 321156 | 0.322 | 72.6 | 28.93 | 0.33 | 0.034 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 321156 | 0.322 | 52.9 | 28.93 | 0.33 | 0.034 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 321156 | 0.322 | 65.2 | 28.93 | 0.33 | 0.034 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 877 | None | classic | 1.15 | False | 389297 | 0.660 | 129.0 | 27.94 | 0.12 | 0.030 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 877 | None | classic | 1.15 | False | 389297 | 0.660 | 113.2 | 27.94 | 0.12 | 0.030 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 877 | None | classic | 1.15 | False | 389297 | 0.660 | 123.2 | 27.94 | 0.12 | 0.030 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 877 | None | classic | 1.15 | False | 389297 | 0.660 | 117.5 | 27.94 | 0.12 | 0.030 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1298324 | 0.177 | 44.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1298238 | 0.818 | 47.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1298238 | 0.818 | 47.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1298238 | 0.494 | 43.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1298238 | 0.494 | 43.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1298324 | 0.177 | 52.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1298238 | 0.818 | 195.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1298238 | 0.818 | 195.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1298238 | 0.494 | 53.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1298238 | 0.494 | 53.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1296372 | 0.818 | 473.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 306645 | 0.345 | 56.8 | 28.77 | 0.22 | 0.034 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 306645 | 0.345 | 69.2 | 28.77 | 0.22 | 0.034 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 306645 | 0.345 | 76.1 | 28.77 | 0.22 | 0.034 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 306645 | 0.345 | 67.2 | 28.77 | 0.22 | 0.034 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1122 | None | classic | 1.88 | False | 459785 | 0.673 | 126.4 | 28.36 | 0.26 | 0.040 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1122 | None | classic | 1.88 | False | 459785 | 0.673 | 126.5 | 28.36 | 0.26 | 0.040 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1122 | None | classic | 1.88 | False | 459785 | 0.673 | 123.9 | 28.36 | 0.26 | 0.040 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1122 | None | classic | 1.88 | False | 459785 | 0.673 | 140.5 | 28.36 | 0.26 | 0.040 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1848283 | 0.818 | 117.3 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 293674 | 0.900 | 82.7 | 29.03 | 0.05 | 0.030 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 293674 | 0.900 | 81.4 | 29.03 | 0.05 | 0.030 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 293674 | 0.900 | 97.8 | 29.03 | 0.05 | 0.030 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 293674 | 0.900 | 62.7 | 29.03 | 0.05 | 0.030 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 865 | None | classic | 1.12 | False | 535878 | 0.986 | 144.2 | 28.02 | 0.13 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 865 | None | classic | 1.12 | False | 535878 | 0.986 | 158.8 | 28.02 | 0.13 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 865 | None | classic | 1.12 | False | 535878 | 0.986 | 144.5 | 28.02 | 0.13 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 865 | None | classic | 1.12 | False | 535878 | 0.986 | 154.5 | 28.02 | 0.13 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.553 | 0.073 |
| in035 | mask_ent | 0.728 | 0.073 |
| in035 | mask_grad | 0.405 | 0.073 |
| in035 | r_col | 0.876 | 0.073 |
| in035 | r_warp | 0.854 | 0.073 |

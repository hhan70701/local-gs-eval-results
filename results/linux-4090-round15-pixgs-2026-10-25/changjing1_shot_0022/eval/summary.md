# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 17.9% | 14.85 / 0.0458 | 16.00 / 0.0610 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 18.5% | 15.00 / 0.0466 | 19.02 / 0.0465 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 18.1% | 14.89 / 0.0463 | 17.46 / 0.0526 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 18.2% | 14.92 / 0.0465 | 18.34 / 0.0481 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 18.4% | 14.92 / 0.0460 | 14.34 / 0.0634 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 18.8% | 15.05 / 0.0464 | 18.94 / 0.0442 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 18.6% | 14.97 / 0.0460 | 16.50 / 0.0518 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 18.7% | 15.00 / 0.0462 | 17.94 / 0.0468 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 18.8% | 15.07 / 0.0478 | 16.24 / 0.0608 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 22.9% | 15.77 / 0.0476 | 15.61 / 0.0785 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 23.5% | 15.97 / 0.0478 | 18.88 / 0.0607 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 23.0% | 15.80 / 0.0474 | 17.00 / 0.0682 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 23.2% | 15.84 / 0.0476 | 17.97 / 0.0639 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 23.2% | 15.82 / 0.0479 | 15.21 / 0.0749 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 23.9% | 16.04 / 0.0480 | 19.69 / 0.0516 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 23.5% | 15.89 / 0.0478 | 17.19 / 0.0613 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 23.6% | 15.95 / 0.0478 | 18.58 / 0.0560 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 23.1% | 15.84 / 0.0490 | 16.51 / 0.0746 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 15.6% | 14.19 / 0.0596 | 15.66 / 0.0761 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 16.7% | 14.49 / 0.0607 | 18.60 / 0.0595 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 16.2% | 14.33 / 0.0595 | 17.58 / 0.0671 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 16.4% | 14.38 / 0.0594 | 18.29 / 0.0631 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 15.9% | 14.25 / 0.0583 | 15.80 / 0.0709 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 17.1% | 14.54 / 0.0605 | 18.37 / 0.0580 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 16.1% | 14.29 / 0.0585 | 17.41 / 0.0619 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 16.3% | 14.35 / 0.0589 | 18.04 / 0.0584 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 21.54 / 0.0828 | 13.65 / 0.2917 | 13.44 / 0.0450 | 29.95 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.63 / 0.0946 | 15.32 / 0.3016 | 15.11 / 0.0470 | 29.58 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.63 / 0.0811 | 18.40 / 0.2062 | 17.73 / 0.0357 | 29.65 / 0.0396 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.73 / 0.0875 | 16.90 / 0.2516 | 16.47 / 0.0409 | 29.66 / 0.0401 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.35 / 0.0834 | 17.93 / 0.2234 | 17.33 / 0.0378 | 29.65 / 0.0398 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.19 / 0.0953 | 13.27 / 0.3357 | 13.31 / 0.0493 | 29.71 / 0.0394 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.59 / 0.0780 | 18.01 / 0.2102 | 17.55 / 0.0345 | 29.68 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.90 / 0.0859 | 15.42 / 0.2693 | 15.34 / 0.0414 | 29.70 / 0.0385 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.95 / 0.0817 | 16.96 / 0.2352 | 16.70 / 0.0376 | 29.66 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.89 / 0.0808 | 15.63 / 0.2124 | 15.52 / 0.0355 | 29.78 / 0.0387 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 21.55 / 0.1075 | 14.03 / 0.3409 | 13.96 / 0.0527 | 29.39 / 0.0459 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.91 / 0.0897 | 17.52 / 0.2254 | 17.01 / 0.0397 | 29.48 / 0.0434 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.69 / 0.0987 | 15.59 / 0.2819 | 15.34 / 0.0465 | 29.49 / 0.0446 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.40 / 0.0939 | 16.71 / 0.2474 | 16.30 / 0.0428 | 29.49 / 0.0440 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.14 / 0.1036 | 13.28 / 0.3509 | 13.35 / 0.0522 | 29.70 / 0.0432 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.50 / 0.0820 | 17.89 / 0.2088 | 17.49 / 0.0351 | 29.77 / 0.0412 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.74 / 0.0921 | 15.26 / 0.2761 | 15.21 / 0.0435 | 29.80 / 0.0418 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.77 / 0.0864 | 16.75 / 0.2341 | 16.52 / 0.0389 | 29.80 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.53 / 0.0880 | 15.61 / 0.2178 | 15.42 / 0.0385 | 29.35 / 0.0432 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 22.83 / 0.0935 | 15.38 / 0.3113 | 15.29 / 0.0448 | 29.83 / 0.0394 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.85 / 0.0801 | 18.40 / 0.2016 | 17.86 / 0.0328 | 29.85 / 0.0388 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.21 / 0.0865 | 17.29 / 0.2575 | 17.00 / 0.0387 | 29.86 / 0.0389 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.67 / 0.0832 | 18.06 / 0.2295 | 17.62 / 0.0356 | 29.85 / 0.0389 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.93 / 0.0888 | 15.35 / 0.2894 | 15.32 / 0.0419 | 29.87 / 0.0386 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.76 / 0.0759 | 17.97 / 0.2036 | 17.57 / 0.0319 | 29.87 / 0.0384 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.15 / 0.0819 | 16.99 / 0.2485 | 16.78 / 0.0371 | 29.88 / 0.0384 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.57 / 0.0787 | 17.66 / 0.2240 | 17.33 / 0.0343 | 29.88 / 0.0384 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 13.5%） | — | — | 21.54 / 0.0828 | 13.65 / 0.2917 | 29.95 |
| in035 | rife | 12.1% | 15.6% | 22.83 / 0.0935 | 15.38 / 0.3113 | 29.83 |
| in035 | cnw_cnn | 13.0% | 17.9% | 22.63 / 0.0946 | 15.32 / 0.3016 | 29.58 |
| in035 | cnw_f5 | 15.9% | 22.9% | 21.55 / 0.1075 | 14.03 / 0.3409 | 29.39 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 22.44 / 0.0772 | -0.77 / +0.0140 (core 13.2%) | -0.62 / +0.0141 (core 14.0%) | -1.72 / +0.0319 (core 17.7%) |
| in035 | 2 | 0-3 | 19.37 / 0.0894 | +3.22 / +0.0148 (core 13.2%) | +3.62 / +0.0122 (core 14.0%) | +2.30 / +0.0294 (core 17.7%) |
| in035 | 4 | 3-5 | 22.81 / 0.0817 | +1.44 / +0.0032 (core 9.2%) | +0.28 / +0.0092 (core 9.0%) | -0.53 / +0.0128 (core 10.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 21.54 / 0.0828 | 13.65 | 29.95 | — |
| in035 | cnw_cnn | 不复核 | —% | 22.63 / 0.0946 | 15.32 | 29.58 | 0/3 |
| in035 | cnw_cnn | oracle | 9.8% | 22.87 / 0.0860 | 15.43 | 29.90 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 24.63 / 0.0811 | 18.40 | 29.65 | 3/3 |
| in035 | cnw_cnn | oracle | 9.8% | 24.89 / 0.0746 | 18.49 | 29.92 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 23.73 / 0.0875 | 16.90 | 29.66 | 0/3 |
| in035 | cnw_cnn | oracle | 9.8% | 23.96 / 0.0801 | 16.99 | 29.91 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 24.35 / 0.0834 | 17.93 | 29.65 | 1/3 |
| in035 | cnw_cnn | oracle | 9.8% | 24.61 / 0.0767 | 18.02 | 29.92 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 21.19 / 0.0953 | 13.27 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 9.9% | 21.35 / 0.0881 | 13.37 | 29.94 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 24.59 / 0.0780 | 18.01 | 29.68 | 3/3 |
| in035 | cnw_cnn_mw | oracle | 9.9% | 24.80 / 0.0732 | 18.10 | 29.94 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 22.90 / 0.0859 | 15.42 | 29.70 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 9.9% | 23.09 / 0.0802 | 15.52 | 29.94 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 23.95 / 0.0817 | 16.96 | 29.66 | 3/3 |
| in035 | cnw_cnn_mw | oracle | 9.9% | 24.16 / 0.0764 | 17.06 | 29.94 | 3/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 22.89 / 0.0808 | 15.63 | 29.78 | 2/3 |
| in035 | cnw_cnn_pix | oracle | 9.8% | 23.13 / 0.0739 | 15.86 | 29.93 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 21.55 / 0.1075 | 14.03 | 29.39 | 0/3 |
| in035 | cnw_f5 | oracle | 10.5% | 21.88 / 0.0921 | 14.17 | 29.91 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 23.91 / 0.0897 | 17.52 | 29.48 | 1/3 |
| in035 | cnw_f5 | oracle | 10.4% | 24.31 / 0.0788 | 17.66 | 29.91 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 22.69 / 0.0987 | 15.59 | 29.49 | 0/3 |
| in035 | cnw_f5 | oracle | 10.5% | 23.03 / 0.0857 | 15.72 | 29.91 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 23.40 / 0.0939 | 16.71 | 29.49 | 0/3 |
| in035 | cnw_f5 | oracle | 10.5% | 23.79 / 0.0818 | 16.85 | 29.91 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 21.14 / 0.1036 | 13.28 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | oracle | 10.5% | 21.36 / 0.0914 | 13.42 | 29.94 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 24.50 / 0.0820 | 17.89 | 29.77 | 2/3 |
| in035 | cnw_f5_mw | oracle | 10.5% | 24.73 / 0.0738 | 18.03 | 29.95 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 22.74 / 0.0921 | 15.26 | 29.80 | 0/3 |
| in035 | cnw_f5_mw | oracle | 10.5% | 22.95 / 0.0822 | 15.41 | 29.94 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 23.77 / 0.0864 | 16.75 | 29.80 | 1/3 |
| in035 | cnw_f5_mw | oracle | 10.5% | 23.99 / 0.0776 | 16.89 | 29.94 | 3/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 22.53 / 0.0880 | 15.61 | 29.35 | 0/3 |
| in035 | cnw_f5_pix | oracle | 10.3% | 22.99 / 0.0767 | 15.84 | 29.91 | 3/3 |
| in035 | rife | 不复核 | —% | 22.83 / 0.0935 | 15.38 | 29.83 | 0/3 |
| in035 | rife | oracle | 9.7% | 23.01 / 0.0841 | 15.49 | 29.94 | 0/3 |
| in035 | rife | 不复核 | —% | 24.85 / 0.0801 | 18.40 | 29.85 | 2/3 |
| in035 | rife | oracle | 9.8% | 25.01 / 0.0721 | 18.50 | 29.95 | 3/3 |
| in035 | rife | 不复核 | —% | 24.21 / 0.0865 | 17.29 | 29.86 | 1/3 |
| in035 | rife | oracle | 9.8% | 24.37 / 0.0781 | 17.38 | 29.95 | 3/3 |
| in035 | rife | 不复核 | —% | 24.67 / 0.0832 | 18.06 | 29.85 | 1/3 |
| in035 | rife | oracle | 9.8% | 24.84 / 0.0750 | 18.15 | 29.95 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 22.93 / 0.0888 | 15.35 | 29.87 | 0/3 |
| in035 | rife_mw | oracle | 9.7% | 23.07 / 0.0810 | 15.46 | 29.95 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 24.76 / 0.0759 | 17.97 | 29.87 | 3/3 |
| in035 | rife_mw | oracle | 9.9% | 24.85 / 0.0705 | 18.06 | 29.95 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 24.15 / 0.0819 | 16.99 | 29.88 | 2/3 |
| in035 | rife_mw | oracle | 9.7% | 24.25 / 0.0758 | 17.09 | 29.95 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 24.57 / 0.0787 | 17.66 | 29.88 | 3/3 |
| in035 | rife_mw | oracle | 9.8% | 24.66 / 0.0731 | 17.75 | 29.95 | 3/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 21.54 / 0.0828 | 13.65 / 0.2917 | — |
| in035 | FF | 0（前馈） | 1008×664（62%） | 23.60 | 22.63 / 0.0946 | 15.32 / 0.3016 | 0/3 |
| in035 | 25 | 0.68 s | 1008×664（62%） | 24.29 | 23.73 / 0.0875 | 16.90 / 0.2516 | 0/3 |
| in035 | 50 | 1.35 s | 1008×664（62%） | 24.78 | 24.35 / 0.0834 | 17.93 / 0.2234 | 1/3 |
| in035 | 100 | 2.67 s | 1008×664（62%） | 25.17 | 24.63 / 0.0811 | 18.40 / 0.2062 | 3/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 21.54 / 0.0828 | 13.65 / 0.2917 | 29.95 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 22.63 / 0.0946 | 15.32 / 0.3016 | 29.58 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 22.87 / 0.0860 | 15.43 / 0.2922 | 29.90 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 23.73 / 0.0875 | 16.90 / 0.2516 | 29.66 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 23.96 / 0.0801 | 16.99 / 0.2463 | 29.91 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 24.35 / 0.0834 | 17.93 / 0.2234 | 29.65 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 24.61 / 0.0767 | 18.02 / 0.2181 | 29.92 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 24.63 / 0.0811 | 18.40 / 0.2062 | 29.65 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 24.89 / 0.0746 | 18.49 / 0.2011 | 29.92 | 3/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 21.19 / 0.0953 | 13.27 / 0.3357 | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 21.35 / 0.0881 | 13.37 / 0.3257 | 29.94 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 22.90 / 0.0859 | 15.42 / 0.2693 | 29.70 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 23.09 / 0.0802 | 15.52 / 0.2618 | 29.94 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 23.95 / 0.0817 | 16.96 / 0.2352 | 29.66 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 24.16 / 0.0764 | 17.06 / 0.2285 | 29.94 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 24.59 / 0.0780 | 18.01 / 0.2102 | 29.68 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 24.80 / 0.0732 | 18.10 / 0.2048 | 29.94 | 3/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 21.55 / 0.1075 | 14.03 / 0.3409 | 29.39 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 21.88 / 0.0921 | 14.17 / 0.3258 | 29.91 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 22.69 / 0.0987 | 15.59 / 0.2819 | 29.49 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 23.03 / 0.0857 | 15.72 / 0.2691 | 29.91 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 23.40 / 0.0939 | 16.71 / 0.2474 | 29.49 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 23.79 / 0.0818 | 16.85 / 0.2354 | 29.91 | 2/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 23.91 / 0.0897 | 17.52 / 0.2254 | 29.48 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 24.31 / 0.0788 | 17.66 / 0.2149 | 29.91 | 3/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 21.14 / 0.1036 | 13.28 / 0.3509 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 21.36 / 0.0914 | 13.42 / 0.3385 | 29.94 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 22.74 / 0.0921 | 15.26 / 0.2761 | 29.80 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 22.95 / 0.0822 | 15.41 / 0.2652 | 29.94 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 23.77 / 0.0864 | 16.75 / 0.2341 | 29.80 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 23.99 / 0.0776 | 16.89 / 0.2255 | 29.94 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 24.50 / 0.0820 | 17.89 / 0.2088 | 29.77 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 24.73 / 0.0738 | 18.03 / 0.2003 | 29.95 | 3/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 22.83 / 0.0935 | 15.38 / 0.3113 | 29.83 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 23.01 / 0.0841 | 15.49 / 0.2949 | 29.94 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 24.21 / 0.0865 | 17.29 / 0.2575 | 29.86 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 24.37 / 0.0781 | 17.38 / 0.2455 | 29.95 | 3/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 24.67 / 0.0832 | 18.06 / 0.2295 | 29.85 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 24.84 / 0.0750 | 18.15 / 0.2179 | 29.95 | 3/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 24.85 / 0.0801 | 18.40 / 0.2016 | 29.85 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 25.01 / 0.0721 | 18.50 / 0.1921 | 29.95 | 3/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 22.93 / 0.0888 | 15.35 / 0.2894 | 29.87 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 23.07 / 0.0810 | 15.46 / 0.2725 | 29.95 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 24.15 / 0.0819 | 16.99 / 0.2485 | 29.88 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 24.25 / 0.0758 | 17.09 / 0.2345 | 29.95 | 3/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 24.57 / 0.0787 | 17.66 / 0.2240 | 29.88 | 3/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 24.66 / 0.0731 | 17.75 / 0.2113 | 29.95 | 3/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 24.76 / 0.0759 | 17.97 / 0.2036 | 29.87 | 3/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 24.85 / 0.0705 | 18.06 / 0.1931 | 29.95 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 13.65 / 0.2917 | 13.44 / 0.0450 | 29.95 / 0.0356 | 21.54 / 0.0828 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 12.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 13.65 | 0.4133 | 0.2917 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 14.83 | 0.4806 | 0.3500 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 18.19 | 0.6092 | 0.2374 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 16.59 | 0.5709 | 0.2906 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 17.71 | 0.6003 | 0.2575 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 12.83 | 0.4608 | 0.3846 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 17.60 | 0.5858 | 0.2345 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 14.98 | 0.5267 | 0.3073 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 16.52 | 0.5565 | 0.2671 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.15 | 0.6003 | 0.2544 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 13.72 | 0.4755 | 0.3553 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 17.10 | 0.5841 | 0.2336 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 15.31 | 0.5545 | 0.2889 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 16.39 | 0.5755 | 0.2535 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 12.96 | 0.4737 | 0.3667 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 17.54 | 0.6047 | 0.2115 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.94 | 0.5415 | 0.2838 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 16.39 | 0.5744 | 0.2395 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.28 | 0.6080 | 0.2364 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.80 | 0.4868 | 0.3406 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 18.15 | 0.5841 | 0.2160 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 16.79 | 0.5566 | 0.2799 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 17.70 | 0.5729 | 0.2474 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 14.67 | 0.4177 | 0.3185 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 17.55 | 0.5280 | 0.2210 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 16.22 | 0.4903 | 0.2729 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 16.95 | 0.5114 | 0.2452 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 15.43 | 0.5101 | 0.2922 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.49 | 0.6171 | 0.2011 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 16.99 | 0.5829 | 0.2463 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.02 | 0.6083 | 0.2181 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 13.37 | 0.4878 | 0.3257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 18.10 | 0.5964 | 0.2048 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 15.52 | 0.5420 | 0.2618 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 17.06 | 0.5687 | 0.2285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 15.86 | 0.6354 | 0.1879 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 14.17 | 0.4928 | 0.3258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 17.66 | 0.5915 | 0.2149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 15.72 | 0.5618 | 0.2691 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 16.85 | 0.5828 | 0.2354 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 13.42 | 0.4867 | 0.3385 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 18.03 | 0.6085 | 0.2003 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 15.41 | 0.5457 | 0.2652 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 16.89 | 0.5775 | 0.2255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 15.84 | 0.6338 | 0.1927 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 15.49 | 0.5100 | 0.2949 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.50 | 0.5939 | 0.1921 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 17.38 | 0.5686 | 0.2455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.15 | 0.5823 | 0.2179 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 15.46 | 0.4529 | 0.2725 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 18.06 | 0.5487 | 0.1931 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 17.09 | 0.5167 | 0.2345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 17.75 | 0.5360 | 0.2113 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 15.32 | 0.5037 | 0.3016 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.40 | 0.6134 | 0.2062 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 16.90 | 0.5806 | 0.2516 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 17.93 | 0.6054 | 0.2234 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 13.27 | 0.4835 | 0.3357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 18.01 | 0.5966 | 0.2102 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 15.42 | 0.5418 | 0.2693 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 16.96 | 0.5689 | 0.2352 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 15.63 | 0.6225 | 0.2124 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 14.03 | 0.4851 | 0.3409 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 17.52 | 0.5853 | 0.2254 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 15.59 | 0.5573 | 0.2819 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 16.71 | 0.5775 | 0.2474 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 13.28 | 0.4795 | 0.3509 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 17.89 | 0.6058 | 0.2088 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 15.26 | 0.5427 | 0.2761 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 16.75 | 0.5751 | 0.2341 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 15.61 | 0.6201 | 0.2178 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 15.38 | 0.5001 | 0.3113 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.40 | 0.5883 | 0.2016 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 17.29 | 0.5633 | 0.2575 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.06 | 0.5774 | 0.2295 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 15.35 | 0.4400 | 0.2894 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 17.97 | 0.5400 | 0.2036 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 16.99 | 0.5083 | 0.2485 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 17.66 | 0.5274 | 0.2240 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 13.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 13.44 | 0.3787 | 0.0450 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 9.17 | 0.3447 | 0.1313 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.88 | 0.4485 | 0.1167 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.57 | 0.4152 | 0.1240 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.78 | 0.4397 | 0.1198 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.58 | 0.3365 | 0.1337 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.68 | 0.4284 | 0.1163 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.20 | 0.3857 | 0.1254 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.51 | 0.4061 | 0.1207 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.05 | 0.4554 | 0.0826 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.87 | 0.3606 | 0.1131 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.91 | 0.4559 | 0.0974 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 10.41 | 0.4270 | 0.1059 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.72 | 0.4468 | 0.1014 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.62 | 0.3761 | 0.1108 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.94 | 0.4840 | 0.0922 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 10.32 | 0.4327 | 0.1018 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.70 | 0.4582 | 0.0968 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.63 | 0.4884 | 0.0716 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.56 | 0.3371 | 0.1418 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.19 | 0.4138 | 0.1271 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.92 | 0.3932 | 0.1348 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.08 | 0.4041 | 0.1309 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 8.51 | 0.2814 | 0.1394 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.92 | 0.3652 | 0.1281 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 8.77 | 0.3372 | 0.1343 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.86 | 0.3535 | 0.1311 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 15.12 | 0.4724 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 17.74 | 0.5715 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 16.47 | 0.5386 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 17.34 | 0.5621 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 13.31 | 0.4607 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 17.55 | 0.5580 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 15.34 | 0.5111 | 0.0413 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 16.70 | 0.5336 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 15.53 | 0.5896 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 13.96 | 0.4537 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 17.01 | 0.5436 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 15.34 | 0.5158 | 0.0463 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 16.31 | 0.5349 | 0.0427 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 13.36 | 0.4600 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 17.49 | 0.5705 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 15.22 | 0.5170 | 0.0434 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 16.52 | 0.5433 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 15.43 | 0.5796 | 0.0383 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 15.29 | 0.4841 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 17.87 | 0.5564 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 17.00 | 0.5379 | 0.0387 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 17.62 | 0.5476 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 15.32 | 0.4348 | 0.0418 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 17.57 | 0.5145 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 16.79 | 0.4897 | 0.0370 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 17.33 | 0.5044 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 15.11 | 0.4715 | 0.0470 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 17.73 | 0.5709 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 16.47 | 0.5382 | 0.0409 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 17.33 | 0.5615 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 13.31 | 0.4603 | 0.0493 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 17.55 | 0.5579 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 15.34 | 0.5110 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 16.70 | 0.5334 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 15.52 | 0.5871 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 13.96 | 0.4531 | 0.0527 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 17.01 | 0.5430 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 15.34 | 0.5152 | 0.0465 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 16.30 | 0.5343 | 0.0428 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 13.35 | 0.4597 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 17.49 | 0.5702 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 15.21 | 0.5169 | 0.0435 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 16.52 | 0.5432 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 15.42 | 0.5773 | 0.0385 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 15.29 | 0.4840 | 0.0448 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 17.86 | 0.5562 | 0.0328 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 17.00 | 0.5380 | 0.0387 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 17.62 | 0.5474 | 0.0356 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 15.32 | 0.4343 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 17.57 | 0.5143 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 16.78 | 0.4894 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 17.33 | 0.5042 | 0.0343 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 36.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.50 | 0.6367 | 0.0515 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.18 | 0.4198 | 0.2587 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.62 | 0.4732 | 0.2366 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.37 | 0.4590 | 0.2485 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.49 | 0.4691 | 0.2421 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.01 | 0.4318 | 0.2588 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.55 | 0.4901 | 0.2325 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.26 | 0.4706 | 0.2465 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.39 | 0.4809 | 0.2397 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.26 | 0.3631 | 0.1966 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.18 | 0.4522 | 0.2278 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.68 | 0.4995 | 0.2032 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.39 | 0.4892 | 0.2172 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.53 | 0.4959 | 0.2101 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.14 | 0.4760 | 0.2224 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.82 | 0.5395 | 0.1926 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.44 | 0.5149 | 0.2082 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.62 | 0.5265 | 0.2003 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.14 | 0.4067 | 0.1771 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.52 | 0.4172 | 0.2622 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.90 | 0.4603 | 0.2420 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.68 | 0.4509 | 0.2537 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.77 | 0.4561 | 0.2483 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.46 | 0.3911 | 0.2588 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.76 | 0.4400 | 0.2403 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.57 | 0.4278 | 0.2511 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.64 | 0.4348 | 0.2464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.98 | 0.6661 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.44 | 0.7082 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.27 | 0.6947 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.06 | 0.7041 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 17.29 | 0.6629 | 0.0570 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.31 | 0.7078 | 0.0430 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.26 | 0.6879 | 0.0496 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.53 | 0.6977 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.16 | 0.7014 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 17.86 | 0.6545 | 0.0616 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.71 | 0.6936 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.18 | 0.6820 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.06 | 0.6896 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 17.28 | 0.6571 | 0.0607 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.19 | 0.7083 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.07 | 0.6846 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.30 | 0.6963 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.01 | 0.6924 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.17 | 0.6712 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.55 | 0.7040 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.78 | 0.6956 | 0.0478 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 21.34 | 0.7001 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.21 | 0.6541 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.32 | 0.6892 | 0.0410 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.60 | 0.6784 | 0.0459 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.11 | 0.6848 | 0.0432 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.61 | 0.6522 | 0.0621 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.00 | 0.6954 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.87 | 0.6844 | 0.0554 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.59 | 0.6929 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 17.02 | 0.6532 | 0.0633 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.93 | 0.7017 | 0.0482 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 18.97 | 0.6838 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.19 | 0.6934 | 0.0508 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 18.47 | 0.6723 | 0.0619 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 17.44 | 0.6289 | 0.0721 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.09 | 0.6687 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.70 | 0.6606 | 0.0652 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.48 | 0.6661 | 0.0611 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 16.94 | 0.6384 | 0.0700 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.72 | 0.6966 | 0.0508 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 18.71 | 0.6726 | 0.0597 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.86 | 0.6844 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.09 | 0.6404 | 0.0743 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.88 | 0.6548 | 0.0625 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.07 | 0.6875 | 0.0527 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.45 | 0.6824 | 0.0563 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.95 | 0.6860 | 0.0536 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 18.94 | 0.6360 | 0.0595 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.89 | 0.6749 | 0.0507 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.33 | 0.6664 | 0.0542 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.80 | 0.6729 | 0.0519 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 45.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.45 | 0.6607 | 0.0580 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.77 | 0.3724 | 0.3830 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.91 | 0.4079 | 0.3645 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.84 | 0.3987 | 0.3745 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.88 | 0.4051 | 0.3694 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.71 | 0.3840 | 0.3840 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.88 | 0.4217 | 0.3598 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.79 | 0.4087 | 0.3734 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.84 | 0.4155 | 0.3665 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.09 | 0.3222 | 0.2485 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.81 | 0.4160 | 0.3495 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.97 | 0.4494 | 0.3278 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.88 | 0.4420 | 0.3405 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.92 | 0.4469 | 0.3345 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.79 | 0.4402 | 0.3442 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.01 | 0.4820 | 0.3159 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.89 | 0.4670 | 0.3320 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.96 | 0.4748 | 0.3239 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.40 | 0.4019 | 0.2243 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.25 | 0.3545 | 0.3972 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.44 | 0.3845 | 0.3782 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.32 | 0.3775 | 0.3889 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.37 | 0.3814 | 0.3840 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.23 | 0.3433 | 0.3909 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.30 | 0.3772 | 0.3741 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.26 | 0.3685 | 0.3828 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.28 | 0.3735 | 0.3785 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 21.27 | 0.6791 | 0.0592 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.38 | 0.7045 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.50 | 0.6969 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.16 | 0.7024 | 0.0507 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.47 | 0.6769 | 0.0624 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.16 | 0.7045 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.33 | 0.6924 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.47 | 0.6985 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 21.48 | 0.7083 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 20.28 | 0.6720 | 0.0645 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.75 | 0.6967 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.52 | 0.6894 | 0.0593 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.28 | 0.6943 | 0.0560 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.45 | 0.6740 | 0.0650 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.16 | 0.7060 | 0.0484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.17 | 0.6912 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.33 | 0.6985 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 21.37 | 0.7040 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 21.22 | 0.6816 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 23.42 | 0.7030 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 22.69 | 0.6976 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 23.22 | 0.7006 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.38 | 0.6727 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.26 | 0.6963 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 22.63 | 0.6890 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.06 | 0.6933 | 0.0477 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.98 | 0.6688 | 0.0658 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.06 | 0.6958 | 0.0538 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.19 | 0.6889 | 0.0595 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.82 | 0.6941 | 0.0560 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.28 | 0.6707 | 0.0679 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.90 | 0.7008 | 0.0520 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.09 | 0.6888 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.20 | 0.6949 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 21.18 | 0.6998 | 0.0561 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.92 | 0.6543 | 0.0754 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.29 | 0.6807 | 0.0606 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.13 | 0.6745 | 0.0685 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.83 | 0.6787 | 0.0647 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.21 | 0.6650 | 0.0733 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.93 | 0.7015 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.94 | 0.6862 | 0.0637 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.09 | 0.6938 | 0.0580 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.84 | 0.6854 | 0.0619 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.01 | 0.6743 | 0.0658 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.23 | 0.6977 | 0.0531 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.52 | 0.6927 | 0.0591 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.04 | 0.6957 | 0.0560 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.22 | 0.6657 | 0.0616 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.16 | 0.6930 | 0.0493 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 22.51 | 0.6857 | 0.0551 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 22.96 | 0.6903 | 0.0519 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 71.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.95 | 0.7213 | 0.0356 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.74 | 0.3153 | 0.3818 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.80 | 0.3192 | 0.3730 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.77 | 0.3198 | 0.3781 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.78 | 0.3197 | 0.3756 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.71 | 0.3186 | 0.3782 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.74 | 0.3212 | 0.3710 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.72 | 0.3225 | 0.3753 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.73 | 0.3223 | 0.3732 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.58 | 0.1569 | 0.2802 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.49 | 0.3646 | 0.3470 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.55 | 0.3704 | 0.3355 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.51 | 0.3718 | 0.3421 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.53 | 0.3715 | 0.3388 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.49 | 0.3765 | 0.3393 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.56 | 0.3807 | 0.3288 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.51 | 0.3820 | 0.3348 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.53 | 0.3818 | 0.3318 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.64 | 0.2493 | 0.2493 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.35 | 0.2860 | 0.3969 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.46 | 0.2901 | 0.3909 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.38 | 0.2892 | 0.3944 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.41 | 0.2896 | 0.3928 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.34 | 0.2878 | 0.3935 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.36 | 0.2904 | 0.3893 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.34 | 0.2915 | 0.3912 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.35 | 0.2910 | 0.3901 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.90 | 0.7209 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.92 | 0.7210 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.91 | 0.7210 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.92 | 0.7210 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.94 | 0.7211 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.94 | 0.7213 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.94 | 0.7213 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.94 | 0.7213 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.93 | 0.7212 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.91 | 0.7208 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.91 | 0.7210 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.91 | 0.7210 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.91 | 0.7210 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.94 | 0.7211 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.95 | 0.7213 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.94 | 0.7213 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.94 | 0.7213 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.91 | 0.7209 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.94 | 0.7211 | 0.0361 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.95 | 0.7213 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.95 | 0.7212 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.95 | 0.7213 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.95 | 0.7213 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.95 | 0.7213 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.95 | 0.7213 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.95 | 0.7213 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.58 | 0.7194 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.65 | 0.7198 | 0.0396 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.66 | 0.7202 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.65 | 0.7201 | 0.0398 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.71 | 0.7204 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.68 | 0.7211 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.70 | 0.7213 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.66 | 0.7213 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.78 | 0.7207 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.39 | 0.7179 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.48 | 0.7184 | 0.0434 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.49 | 0.7193 | 0.0446 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.49 | 0.7189 | 0.0440 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.70 | 0.7206 | 0.0432 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7214 | 0.0412 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.80 | 0.7221 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.80 | 0.7219 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.35 | 0.7183 | 0.0432 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.83 | 0.7202 | 0.0394 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.85 | 0.7205 | 0.0388 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.86 | 0.7207 | 0.0389 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.85 | 0.7206 | 0.0389 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.87 | 0.7207 | 0.0386 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.87 | 0.7208 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.88 | 0.7213 | 0.0384 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.88 | 0.7211 | 0.0384 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 21.54 | 0.6863 | 0.0828 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.63 | 0.3321 | 0.4783 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.73 | 0.3530 | 0.4535 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.68 | 0.3481 | 0.4671 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.71 | 0.3518 | 0.4597 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.58 | 0.3382 | 0.4754 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.67 | 0.3587 | 0.4458 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.62 | 0.3523 | 0.4611 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.65 | 0.3558 | 0.4533 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.73 | 0.2251 | 0.3878 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.41 | 0.3767 | 0.4405 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.52 | 0.3972 | 0.4111 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.45 | 0.3938 | 0.4278 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.48 | 0.3964 | 0.4192 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.40 | 0.3942 | 0.4300 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.53 | 0.4173 | 0.3950 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.45 | 0.4094 | 0.4133 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.49 | 0.4135 | 0.4037 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.75 | 0.3046 | 0.3434 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.18 | 0.3064 | 0.4953 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.32 | 0.3238 | 0.4737 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.22 | 0.3197 | 0.4853 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.27 | 0.3219 | 0.4799 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.16 | 0.3015 | 0.4840 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.20 | 0.3199 | 0.4654 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.18 | 0.3159 | 0.4749 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.19 | 0.3184 | 0.4700 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.87 | 0.6959 | 0.0860 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.89 | 0.7103 | 0.0746 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.96 | 0.7058 | 0.0801 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.61 | 0.7090 | 0.0767 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.35 | 0.6950 | 0.0881 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.80 | 0.7106 | 0.0732 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.09 | 0.7036 | 0.0802 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.16 | 0.7070 | 0.0764 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 23.13 | 0.7126 | 0.0739 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 21.88 | 0.6915 | 0.0921 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.31 | 0.7050 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.03 | 0.7010 | 0.0857 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.79 | 0.7037 | 0.0818 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.36 | 0.6933 | 0.0914 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.73 | 0.7111 | 0.0738 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.95 | 0.7027 | 0.0822 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.99 | 0.7068 | 0.0776 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 22.99 | 0.7093 | 0.0767 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.01 | 0.6977 | 0.0841 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.01 | 0.7093 | 0.0721 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.37 | 0.7064 | 0.0781 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 24.84 | 0.7080 | 0.0750 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 23.07 | 0.6921 | 0.0810 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.85 | 0.7049 | 0.0705 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.25 | 0.7010 | 0.0758 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.66 | 0.7033 | 0.0731 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.63 | 0.6909 | 0.0946 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.63 | 0.7061 | 0.0811 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.73 | 0.7022 | 0.0875 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.35 | 0.7051 | 0.0834 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.19 | 0.6921 | 0.0953 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.59 | 0.7091 | 0.0780 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.90 | 0.7022 | 0.0859 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.95 | 0.7056 | 0.0817 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.89 | 0.7085 | 0.0808 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 21.55 | 0.6816 | 0.1075 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.91 | 0.6962 | 0.0897 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.69 | 0.6929 | 0.0987 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.40 | 0.6952 | 0.0939 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.14 | 0.6882 | 0.1036 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.50 | 0.7081 | 0.0820 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.74 | 0.6999 | 0.0921 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.77 | 0.7041 | 0.0864 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.53 | 0.6989 | 0.0880 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.83 | 0.6937 | 0.0935 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.85 | 0.7063 | 0.0801 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.21 | 0.7036 | 0.0865 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.67 | 0.7052 | 0.0832 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.93 | 0.6886 | 0.0888 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.76 | 0.7031 | 0.0759 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.15 | 0.6993 | 0.0819 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.57 | 0.7017 | 0.0787 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 282451 | 0.165 | 36.0 | 25.87 | 0.28 | 0.044 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 282451 | 0.165 | 45.1 | 25.87 | 0.28 | 0.044 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 282451 | 0.165 | 37.3 | 25.87 | 0.28 | 0.044 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 282451 | 0.165 | 36.0 | 25.87 | 0.28 | 0.044 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1064 | None | classic | 1.69 | False | 401387 | 0.330 | 72.0 | 24.87 | 0.11 | 0.025 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1064 | None | classic | 1.69 | False | 401387 | 0.330 | 70.3 | 24.87 | 0.11 | 0.025 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1064 | None | classic | 1.69 | False | 401387 | 0.330 | 72.3 | 24.87 | 0.11 | 0.025 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1064 | None | classic | 1.69 | False | 401387 | 0.330 | 71.6 | 24.87 | 0.11 | 0.025 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1534883 | 0.799 | 167.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 264895 | 0.164 | 33.2 | 25.67 | 0.29 | 0.036 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 264895 | 0.164 | 37.2 | 25.67 | 0.29 | 0.036 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 264895 | 0.164 | 34.2 | 25.67 | 0.29 | 0.036 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 264895 | 0.164 | 33.7 | 25.67 | 0.29 | 0.036 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1117 | None | classic | 1.86 | False | 437966 | 0.344 | 76.5 | 25.00 | 0.23 | 0.021 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1117 | None | classic | 1.86 | False | 437966 | 0.344 | 76.1 | 25.00 | 0.23 | 0.021 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1117 | None | classic | 1.86 | False | 437966 | 0.344 | 78.1 | 25.00 | 0.23 | 0.021 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1117 | None | classic | 1.86 | False | 437966 | 0.344 | 74.9 | 25.00 | 0.23 | 0.021 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1963824 | 0.799 | 82.9 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 276372 | 0.329 | 41.4 | 26.62 | 0.22 | 0.036 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 276372 | 0.329 | 44.1 | 26.62 | 0.22 | 0.036 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 276372 | 0.329 | 35.3 | 26.62 | 0.22 | 0.036 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 276372 | 0.329 | 39.0 | 26.62 | 0.22 | 0.036 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 867 | None | classic | 1.12 | False | 495068 | 0.508 | 79.7 | 24.16 | 0.09 | 0.026 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 867 | None | classic | 1.12 | False | 495068 | 0.508 | 84.0 | 24.16 | 0.09 | 0.026 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 867 | None | classic | 1.12 | False | 495068 | 0.508 | 83.0 | 24.16 | 0.09 | 0.026 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 867 | None | classic | 1.12 | False | 495068 | 0.508 | 82.8 | 24.16 | 0.09 | 0.026 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.748 | 0.092 |
| in035 | mask_ent | 0.680 | 0.092 |
| in035 | mask_grad | 0.278 | 0.092 |
| in035 | r_col | 0.920 | 0.092 |
| in035 | r_warp | 0.962 | 0.092 |

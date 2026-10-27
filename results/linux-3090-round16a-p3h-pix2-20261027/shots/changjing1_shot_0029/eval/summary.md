# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 16.6% | 21.83 / 0.0228 | 19.47 / 0.0593 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 17.7% | 22.05 / 0.0240 | 20.36 / 0.0502 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 17.4% | 21.99 / 0.0234 | 20.35 / 0.0543 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 17.5% | 22.05 / 0.0235 | 20.37 / 0.0512 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 17.3% | 21.93 / 0.0227 | 20.47 / 0.0507 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 18.2% | 22.06 / 0.0238 | 21.75 / 0.0376 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 17.9% | 22.05 / 0.0232 | 21.50 / 0.0426 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 18.0% | 22.07 / 0.0235 | 21.84 / 0.0392 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.8% | 21.52 / 0.0243 | 20.27 / 0.0557 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.0% | 21.42 / 0.0236 | 21.53 / 0.0407 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 5.6% | 18.51 / 0.0185 | 18.45 / 0.0291 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.8% | 21.46 / 0.0237 | 21.12 / 0.0415 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 5.5% | 18.66 / 0.0163 | 18.10 / 0.0286 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.8% | 21.51 / 0.0240 | 20.29 / 0.0461 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.6% | 21.46 / 0.0244 | 21.29 / 0.0409 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 5.8% | 18.81 / 0.0180 | 18.53 / 0.0283 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.4% | 21.51 / 0.0241 | 20.96 / 0.0419 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 6.0% | 19.15 / 0.0172 | 18.48 / 0.0298 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 17.7% | 22.01 / 0.0250 | 20.62 / 0.0576 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 21.2% | 22.74 / 0.0223 | 19.65 / 0.0605 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 22.4% | 22.90 / 0.0227 | 20.73 / 0.0498 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 21.9% | 22.85 / 0.0223 | 20.37 / 0.0553 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 22.1% | 22.87 / 0.0225 | 20.43 / 0.0520 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 21.3% | 22.69 / 0.0213 | 20.46 / 0.0510 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 21.7% | 22.77 / 0.0219 | 21.74 / 0.0402 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 21.6% | 22.77 / 0.0217 | 21.48 / 0.0458 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 21.6% | 22.78 / 0.0218 | 21.66 / 0.0427 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 22.0% | 22.79 / 0.0229 | 20.59 / 0.0647 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 15.9% | 22.10 / 0.0208 | 19.58 / 0.0561 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 17.8% | 22.43 / 0.0223 | 20.37 / 0.0527 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 17.0% | 22.29 / 0.0213 | 20.14 / 0.0549 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 17.3% | 22.34 / 0.0219 | 20.29 / 0.0536 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 17.4% | 22.37 / 0.0208 | 19.87 / 0.0559 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 19.4% | 22.75 / 0.0226 | 20.37 / 0.0524 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 18.3% | 22.54 / 0.0220 | 20.27 / 0.0533 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 18.7% | 22.63 / 0.0222 | 20.24 / 0.0518 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 26.36 / 0.0567 | 22.65 / 0.0806 | 18.85 / 0.0187 | 29.73 / 0.0343 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.27 / 0.0788 | 20.89 / 0.1716 | 18.52 / 0.0272 | 28.80 / 0.0402 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.76 / 0.0723 | 21.65 / 0.1442 | 19.03 / 0.0244 | 28.91 / 0.0393 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.88 / 0.0749 | 21.79 / 0.1547 | 19.16 / 0.0251 | 29.02 / 0.0393 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.85 / 0.0731 | 21.75 / 0.1465 | 19.10 / 0.0245 | 28.99 / 0.0391 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.95 / 0.0721 | 21.94 / 0.1439 | 19.10 / 0.0242 | 29.09 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.72 / 0.0626 | 23.38 / 0.1019 | 20.05 / 0.0187 | 29.55 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.44 / 0.0678 | 22.79 / 0.1233 | 19.63 / 0.0214 | 29.46 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.62 / 0.0653 | 23.14 / 0.1116 | 19.90 / 0.0201 | 29.53 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.85 / 0.0720 | 21.37 / 0.1558 | 18.46 / 0.0292 | 29.75 / 0.0344 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.41 / 0.0670 | 23.27 / 0.1161 | 19.62 / 0.0236 | 29.43 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.38 / 0.0636 | 23.25 / 0.0993 | 19.51 / 0.0224 | 29.42 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.24 / 0.0669 | 22.92 / 0.1181 | 19.37 / 0.0234 | 29.50 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.26 / 0.0637 | 22.97 / 0.1050 | 19.29 / 0.0226 | 29.49 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.80 / 0.0678 | 21.31 / 0.1302 | 18.42 / 0.0258 | 29.69 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.27 / 0.0670 | 22.78 / 0.1174 | 19.31 / 0.0231 | 29.46 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.35 / 0.0638 | 22.95 / 0.1033 | 19.37 / 0.0223 | 29.51 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.14 / 0.0668 | 22.55 / 0.1224 | 19.14 / 0.0233 | 29.51 / 0.0358 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.24 / 0.0641 | 22.77 / 0.1100 | 19.24 / 0.0226 | 29.56 / 0.0354 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.97 / 0.0680 | 21.63 / 0.1353 | 18.80 / 0.0233 | 29.57 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.85 / 0.0874 | 20.83 / 0.1761 | 18.50 / 0.0282 | 28.53 / 0.0441 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.41 / 0.0770 | 21.59 / 0.1443 | 19.22 / 0.0241 | 28.62 / 0.0421 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.34 / 0.0826 | 21.50 / 0.1608 | 19.02 / 0.0260 | 28.68 / 0.0430 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.34 / 0.0799 | 21.53 / 0.1525 | 19.06 / 0.0252 | 28.66 / 0.0425 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.49 / 0.0788 | 21.29 / 0.1556 | 18.98 / 0.0243 | 28.71 / 0.0413 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.26 / 0.0701 | 22.55 / 0.1259 | 19.89 / 0.0202 | 29.11 / 0.0392 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.08 / 0.0758 | 22.19 / 0.1470 | 19.60 / 0.0222 | 28.99 / 0.0405 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.18 / 0.0731 | 22.35 / 0.1381 | 19.78 / 0.0214 | 29.06 / 0.0399 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.80 / 0.0721 | 21.68 / 0.1417 | 18.86 / 0.0241 | 29.35 / 0.0374 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 25.16 / 0.0807 | 20.88 / 0.1708 | 19.16 / 0.0252 | 27.82 / 0.0424 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.48 / 0.0761 | 21.46 / 0.1482 | 19.48 / 0.0234 | 27.83 / 0.0423 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.36 / 0.0800 | 21.31 / 0.1615 | 19.35 / 0.0243 | 27.82 / 0.0426 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.42 / 0.0777 | 21.42 / 0.1524 | 19.40 / 0.0238 | 27.84 / 0.0423 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.21 / 0.0782 | 21.32 / 0.1480 | 19.15 / 0.0240 | 27.60 / 0.0419 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.34 / 0.0717 | 22.04 / 0.1132 | 19.54 / 0.0215 | 27.40 / 0.0416 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.31 / 0.0761 | 21.77 / 0.1337 | 19.32 / 0.0230 | 27.52 / 0.0419 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.31 / 0.0740 | 21.88 / 0.1210 | 19.43 / 0.0221 | 27.44 / 0.0417 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.8%） | — | — | 26.36 / 0.0567 | 22.65 / 0.0806 | 29.73 |
| in035 | rife | 6.9% | 15.9% | 25.16 / 0.0807 | 20.88 / 0.1708 | 27.82 |
| in035 | cnw_cnn | 11.1% | 16.6% | 25.27 / 0.0788 | 20.89 / 0.1716 | 28.80 |
| in035 | cnw_f5 | 12.5% | 21.2% | 24.85 / 0.0874 | 20.83 / 0.1761 | 28.53 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 25.93 / 0.0565 | -1.51 / +0.0225 (core 6.5%) | -0.88 / +0.0186 (core 10.7%) | -1.48 / +0.0303 (core 13.2%) |
| in035 | 2 | 0-3 | 25.43 / 0.0610 | -1.00 / +0.0301 (core 6.5%) | -0.62 / +0.0259 (core 10.7%) | -1.18 / +0.0393 (core 13.2%) |
| in035 | 4 | 3-5 | 27.73 / 0.0526 | -1.10 / +0.0194 (core 4.5%) | -1.77 / +0.0217 (core 8.0%) | -1.88 / +0.0224 (core 7.9%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 26.36 / 0.0567 | 22.65 | 29.73 | — |
| in035 | cnw_cnn | 不复核 | —% | 25.27 / 0.0788 | 20.89 | 28.80 | 0/3 |
| in035 | cnw_cnn | oracle | 5.3% | 25.97 / 0.0678 | 22.06 | 29.55 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 25.76 / 0.0723 | 21.65 | 28.91 | 0/3 |
| in035 | cnw_cnn | oracle | 5.3% | 26.34 / 0.0638 | 22.60 | 29.55 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 25.88 / 0.0749 | 21.79 | 29.02 | 0/3 |
| in035 | cnw_cnn | oracle | 5.3% | 26.40 / 0.0652 | 22.74 | 29.59 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 25.85 / 0.0731 | 21.75 | 28.99 | 0/3 |
| in035 | cnw_cnn | oracle | 5.3% | 26.38 / 0.0641 | 22.69 | 29.58 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.95 / 0.0721 | 21.94 | 29.09 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.3% | 26.40 / 0.0638 | 22.81 | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.72 / 0.0626 | 23.38 | 29.55 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.4% | 26.99 / 0.0580 | 24.01 | 29.70 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.44 / 0.0678 | 22.79 | 29.46 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.4% | 26.76 / 0.0611 | 23.47 | 29.68 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.62 / 0.0653 | 23.14 | 29.53 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.4% | 26.92 / 0.0597 | 23.81 | 29.70 | 1/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 25.85 / 0.0720 | 21.37 | 29.75 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 5.3% | 26.05 / 0.0685 | 21.84 | 29.74 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 26.41 / 0.0670 | 23.27 | 29.43 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 5.1% | 26.70 / 0.0616 | 23.63 | 29.69 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 26.38 / 0.0636 | 23.25 | 29.42 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 3.0% | 26.64 / 0.0606 | 23.49 | 29.69 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 26.24 / 0.0669 | 22.92 | 29.50 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 5.0% | 26.55 / 0.0615 | 23.35 | 29.70 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 26.26 / 0.0637 | 22.97 | 29.49 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 2.9% | 26.51 / 0.0606 | 23.28 | 29.70 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 25.80 / 0.0678 | 21.31 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 5.3% | 26.03 / 0.0643 | 21.82 | 29.72 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 26.27 / 0.0670 | 22.78 | 29.46 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 5.0% | 26.56 / 0.0613 | 23.23 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.35 / 0.0638 | 22.95 | 29.51 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 2.9% | 26.59 / 0.0604 | 23.25 | 29.70 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 26.14 / 0.0668 | 22.55 | 29.51 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 4.9% | 26.45 / 0.0616 | 23.06 | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 26.24 / 0.0641 | 22.77 | 29.56 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 2.9% | 26.50 / 0.0607 | 23.16 | 29.71 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 25.97 / 0.0680 | 21.63 | 29.57 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 5.4% | 26.26 / 0.0614 | 22.25 | 29.70 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 24.85 / 0.0874 | 20.83 | 28.53 | 0/3 |
| in035 | cnw_f5 | oracle | 5.2% | 25.93 / 0.0683 | 22.12 | 29.62 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.41 / 0.0770 | 21.59 | 28.62 | 0/3 |
| in035 | cnw_f5 | oracle | 5.3% | 26.41 / 0.0632 | 22.71 | 29.60 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.34 / 0.0826 | 21.50 | 28.68 | 0/3 |
| in035 | cnw_f5 | oracle | 5.3% | 26.29 / 0.0654 | 22.61 | 29.62 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.34 / 0.0799 | 21.53 | 28.66 | 0/3 |
| in035 | cnw_f5 | oracle | 5.3% | 26.30 / 0.0644 | 22.61 | 29.61 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.49 / 0.0788 | 21.29 | 28.71 | 0/3 |
| in035 | cnw_f5_mw | oracle | 5.2% | 26.27 / 0.0641 | 22.39 | 29.66 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.26 / 0.0701 | 22.55 | 29.11 | 0/3 |
| in035 | cnw_f5_mw | oracle | 5.2% | 26.85 / 0.0601 | 23.33 | 29.70 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.08 / 0.0758 | 22.19 | 28.99 | 0/3 |
| in035 | cnw_f5_mw | oracle | 5.2% | 26.69 / 0.0626 | 23.05 | 29.69 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.18 / 0.0731 | 22.35 | 29.06 | 0/3 |
| in035 | cnw_f5_mw | oracle | 5.2% | 26.78 / 0.0614 | 23.19 | 29.70 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 25.80 / 0.0721 | 21.68 | 29.35 | 0/3 |
| in035 | cnw_f5_pix | oracle | 5.3% | 26.27 / 0.0623 | 22.35 | 29.70 | 0/3 |
| in035 | rife | 不复核 | —% | 25.16 / 0.0807 | 20.88 | 27.82 | 0/3 |
| in035 | rife | oracle | 4.4% | 26.35 / 0.0657 | 22.65 | 29.48 | 0/3 |
| in035 | rife | 不复核 | —% | 25.48 / 0.0761 | 21.46 | 27.83 | 0/3 |
| in035 | rife | oracle | 4.7% | 26.55 / 0.0632 | 23.01 | 29.48 | 0/3 |
| in035 | rife | 不复核 | —% | 25.36 / 0.0800 | 21.31 | 27.82 | 0/3 |
| in035 | rife | oracle | 4.6% | 26.46 / 0.0648 | 22.96 | 29.48 | 0/3 |
| in035 | rife | 不复核 | —% | 25.42 / 0.0777 | 21.42 | 27.84 | 0/3 |
| in035 | rife | oracle | 4.7% | 26.51 / 0.0637 | 23.02 | 29.48 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.21 / 0.0782 | 21.32 | 27.60 | 0/3 |
| in035 | rife_mw | oracle | 4.5% | 26.40 / 0.0633 | 22.82 | 29.52 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.34 / 0.0717 | 22.04 | 27.40 | 0/3 |
| in035 | rife_mw | oracle | 4.7% | 26.63 / 0.0597 | 23.41 | 29.53 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.31 / 0.0761 | 21.77 | 27.52 | 0/3 |
| in035 | rife_mw | oracle | 4.6% | 26.52 / 0.0620 | 23.14 | 29.53 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.31 / 0.0740 | 21.88 | 27.44 | 0/3 |
| in035 | rife_mw | oracle | 4.6% | 26.57 / 0.0610 | 23.26 | 29.53 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 26.36 / 0.0567 | 22.65 / 0.0806 | — |
| in035 | FF | 0（前馈） | 1007×661（60%） | 26.00 | 25.27 / 0.0788 | 20.89 / 0.1716 | 0/3 |
| in035 | 25 | 1.18 s | 1007×661（60%） | 26.83 | 25.88 / 0.0749 | 21.79 / 0.1547 | 0/3 |
| in035 | 50 | 2.35 s | 1007×661（60%） | 27.17 | 25.85 / 0.0731 | 21.75 / 0.1465 | 0/3 |
| in035 | 100 | 4.70 s | 1007×661（60%） | 27.55 | 25.76 / 0.0723 | 21.65 / 0.1442 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 26.36 / 0.0567 | 22.65 / 0.0806 | 29.73 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 25.27 / 0.0788 | 20.89 / 0.1716 | 28.80 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 25.97 / 0.0678 | 22.06 / 0.1345 | 29.55 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 25.88 / 0.0749 | 21.79 / 0.1547 | 29.02 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 26.40 / 0.0652 | 22.74 / 0.1228 | 29.59 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 25.85 / 0.0731 | 21.75 / 0.1465 | 28.99 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 26.38 / 0.0641 | 22.69 / 0.1174 | 29.58 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 25.76 / 0.0723 | 21.65 / 0.1442 | 28.91 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 26.34 / 0.0638 | 22.60 / 0.1167 | 29.55 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 25.95 / 0.0721 | 21.94 / 0.1439 | 29.09 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 26.40 / 0.0638 | 22.81 / 0.1159 | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 26.44 / 0.0678 | 22.79 / 0.1233 | 29.46 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 26.76 / 0.0611 | 23.47 / 0.1018 | 29.68 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 26.62 / 0.0653 | 23.14 / 0.1116 | 29.53 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 26.92 / 0.0597 | 23.81 / 0.0939 | 29.70 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 26.72 / 0.0626 | 23.38 / 0.1019 | 29.55 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 26.99 / 0.0580 | 24.01 / 0.0870 | 29.70 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 24.85 / 0.0874 | 20.83 / 0.1761 | 28.53 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 25.93 / 0.0683 | 22.12 / 0.1291 | 29.62 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 25.34 / 0.0826 | 21.50 / 0.1608 | 28.68 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 26.29 / 0.0654 | 22.61 / 0.1189 | 29.62 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 25.34 / 0.0799 | 21.53 / 0.1525 | 28.66 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 26.30 / 0.0644 | 22.61 / 0.1141 | 29.61 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 25.41 / 0.0770 | 21.59 / 0.1443 | 28.62 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 26.41 / 0.0632 | 22.71 / 0.1088 | 29.60 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 25.49 / 0.0788 | 21.29 / 0.1556 | 28.71 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 26.27 / 0.0641 | 22.39 / 0.1179 | 29.66 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.08 / 0.0758 | 22.19 / 0.1470 | 28.99 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 26.69 / 0.0626 | 23.05 / 0.1133 | 29.69 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.18 / 0.0731 | 22.35 / 0.1381 | 29.06 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 26.78 / 0.0614 | 23.19 / 0.1075 | 29.70 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 26.26 / 0.0701 | 22.55 / 0.1259 | 29.11 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 26.85 / 0.0601 | 23.33 / 0.0996 | 29.70 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 25.16 / 0.0807 | 20.88 / 0.1708 | 27.82 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 26.35 / 0.0657 | 22.65 / 0.1230 | 29.48 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 25.36 / 0.0800 | 21.31 / 0.1615 | 27.82 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 26.46 / 0.0648 | 22.96 / 0.1182 | 29.48 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 25.42 / 0.0777 | 21.42 / 0.1524 | 27.84 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 26.51 / 0.0637 | 23.02 / 0.1142 | 29.48 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 25.48 / 0.0761 | 21.46 / 0.1482 | 27.83 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 26.55 / 0.0632 | 23.01 / 0.1137 | 29.48 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 25.21 / 0.0782 | 21.32 / 0.1480 | 27.60 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 26.40 / 0.0633 | 22.82 / 0.1133 | 29.52 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 25.31 / 0.0761 | 21.77 / 0.1337 | 27.52 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 26.52 / 0.0620 | 23.14 / 0.1027 | 29.53 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 25.31 / 0.0740 | 21.88 / 0.1210 | 27.44 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 26.57 / 0.0610 | 23.26 / 0.0942 | 29.53 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 25.34 / 0.0717 | 22.04 / 0.1132 | 27.40 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 26.63 / 0.0597 | 23.41 / 0.0896 | 29.53 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.65 / 0.0806 | 18.85 / 0.0187 | 29.73 / 0.0343 | 26.36 / 0.0567 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 15.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.65 | 0.7055 | 0.0806 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 18.60 | 0.5924 | 0.2237 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 19.47 | 0.6085 | 0.1804 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 19.61 | 0.6251 | 0.1999 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 19.48 | 0.6193 | 0.1872 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 19.18 | 0.6312 | 0.1811 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 20.77 | 0.7085 | 0.1224 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 19.99 | 0.6843 | 0.1530 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 20.32 | 0.6989 | 0.1361 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 21.37 | 0.6794 | 0.1606 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 23.30 | 0.7303 | 0.1212 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 23.30 | 0.7303 | 0.1212 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 22.93 | 0.7177 | 0.1246 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 22.93 | 0.7177 | 0.1246 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 20.62 | 0.6678 | 0.1511 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 21.57 | 0.6950 | 0.1488 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 21.57 | 0.6950 | 0.1488 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 21.22 | 0.6786 | 0.1553 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 21.22 | 0.6786 | 0.1553 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 20.63 | 0.6705 | 0.1647 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 17.63 | 0.5723 | 0.2305 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 18.37 | 0.5834 | 0.1835 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 18.40 | 0.6023 | 0.2078 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 18.36 | 0.5963 | 0.1951 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 18.03 | 0.6041 | 0.2082 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.39 | 0.6650 | 0.1595 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 18.89 | 0.6552 | 0.1882 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 19.05 | 0.6638 | 0.1737 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.90 | 0.6584 | 0.1719 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 16.55 | 0.5779 | 0.2427 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 17.63 | 0.6016 | 0.1952 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 17.43 | 0.6103 | 0.2214 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 17.58 | 0.6094 | 0.2067 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 15.98 | 0.5978 | 0.2062 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 17.42 | 0.6564 | 0.1490 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 16.72 | 0.6405 | 0.1796 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 17.13 | 0.6523 | 0.1614 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.06 | 0.6873 | 0.1345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.60 | 0.6951 | 0.1167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.74 | 0.7018 | 0.1228 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.69 | 0.6998 | 0.1174 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.81 | 0.7044 | 0.1159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.01 | 0.7408 | 0.0870 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.47 | 0.7258 | 0.1018 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.81 | 0.7343 | 0.0939 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 21.84 | 0.6957 | 0.1363 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 23.63 | 0.7361 | 0.0943 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 23.49 | 0.7283 | 0.0884 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 23.35 | 0.7282 | 0.0971 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 23.28 | 0.7215 | 0.0931 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 21.82 | 0.6957 | 0.1136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.23 | 0.7229 | 0.0965 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 23.25 | 0.7186 | 0.0907 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 23.06 | 0.7173 | 0.1001 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 23.16 | 0.7185 | 0.0949 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 22.25 | 0.7153 | 0.1026 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 22.12 | 0.6897 | 0.1291 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 22.71 | 0.6947 | 0.1088 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.61 | 0.7014 | 0.1189 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.61 | 0.6988 | 0.1141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.39 | 0.6989 | 0.1179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 23.33 | 0.7251 | 0.0996 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.05 | 0.7202 | 0.1133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.19 | 0.7240 | 0.1075 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 22.35 | 0.7202 | 0.1034 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 22.65 | 0.6940 | 0.1230 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 23.01 | 0.7017 | 0.1137 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 22.96 | 0.7043 | 0.1182 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 23.02 | 0.7046 | 0.1142 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 22.82 | 0.6999 | 0.1133 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.41 | 0.7248 | 0.0896 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.14 | 0.7145 | 0.1027 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.26 | 0.7217 | 0.0942 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.89 | 0.6400 | 0.1716 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.65 | 0.6486 | 0.1442 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.79 | 0.6628 | 0.1547 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.75 | 0.6579 | 0.1465 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.94 | 0.6680 | 0.1439 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.38 | 0.7272 | 0.1019 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.79 | 0.7053 | 0.1233 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.14 | 0.7182 | 0.1116 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 21.37 | 0.6787 | 0.1558 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 23.27 | 0.7249 | 0.1161 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 23.25 | 0.7222 | 0.0993 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 22.92 | 0.7134 | 0.1181 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 22.97 | 0.7141 | 0.1050 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 21.31 | 0.6793 | 0.1302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.78 | 0.7078 | 0.1174 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.95 | 0.7096 | 0.1033 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 22.55 | 0.6990 | 0.1224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.77 | 0.7084 | 0.1100 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 21.63 | 0.6897 | 0.1353 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 20.83 | 0.6320 | 0.1761 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.59 | 0.6381 | 0.1443 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.50 | 0.6512 | 0.1608 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.53 | 0.6472 | 0.1525 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.29 | 0.6535 | 0.1556 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.55 | 0.7001 | 0.1259 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.19 | 0.6913 | 0.1470 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.35 | 0.6981 | 0.1381 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.68 | 0.6928 | 0.1417 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.88 | 0.6423 | 0.1708 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.46 | 0.6542 | 0.1482 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.31 | 0.6600 | 0.1615 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 21.42 | 0.6602 | 0.1524 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.32 | 0.6559 | 0.1480 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 22.04 | 0.6975 | 0.1132 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.77 | 0.6826 | 0.1337 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.88 | 0.6931 | 0.1210 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.85 | 0.5620 | 0.0187 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 9.27 | 0.3858 | 0.1008 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.56 | 0.3985 | 0.0962 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.48 | 0.4068 | 0.0979 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.52 | 0.4042 | 0.0973 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.48 | 0.4110 | 0.0881 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.73 | 0.4865 | 0.0800 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.68 | 0.4576 | 0.0838 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 10.71 | 0.4735 | 0.0817 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.60 | 0.4322 | 0.0607 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.16 | 0.4806 | 0.0552 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.16 | 0.4806 | 0.0552 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.04 | 0.4686 | 0.0552 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.04 | 0.4686 | 0.0552 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.15 | 0.3979 | 0.0642 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.42 | 0.4238 | 0.0628 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.42 | 0.4238 | 0.0628 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.33 | 0.4113 | 0.0635 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.33 | 0.4113 | 0.0635 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.23 | 0.4131 | 0.0634 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.48 | 0.3721 | 0.0919 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.75 | 0.3929 | 0.0846 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.69 | 0.3953 | 0.0880 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.73 | 0.3949 | 0.0865 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.59 | 0.4039 | 0.0866 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.70 | 0.4605 | 0.0811 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.69 | 0.4459 | 0.0837 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.68 | 0.4546 | 0.0828 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.52 | 0.4081 | 0.0594 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.06 | 0.3454 | 0.1086 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.30 | 0.3622 | 0.1030 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.22 | 0.3680 | 0.1057 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.27 | 0.3660 | 0.1046 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.89 | 0.3516 | 0.1065 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.13 | 0.3930 | 0.0999 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 8.01 | 0.3797 | 0.1034 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.07 | 0.3898 | 0.1015 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.54 | 0.5726 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.06 | 0.5859 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.18 | 0.5921 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.13 | 0.5900 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.12 | 0.6006 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.06 | 0.6536 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.65 | 0.6315 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.92 | 0.6441 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 18.46 | 0.5613 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.62 | 0.6162 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.50 | 0.6036 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.37 | 0.6055 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.29 | 0.5939 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 18.42 | 0.5597 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.32 | 0.5963 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.37 | 0.5923 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.15 | 0.5895 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.25 | 0.5927 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 18.80 | 0.5911 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.50 | 0.5730 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.23 | 0.5905 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.03 | 0.5921 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.07 | 0.5909 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.99 | 0.6023 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.90 | 0.6427 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.62 | 0.6339 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.79 | 0.6402 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 18.86 | 0.5950 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.21 | 0.5874 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 19.49 | 0.6002 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.37 | 0.6012 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.42 | 0.6021 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.19 | 0.5940 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.55 | 0.6225 | 0.0212 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.35 | 0.6107 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.45 | 0.6192 | 0.0217 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.52 | 0.5707 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.03 | 0.5836 | 0.0244 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.16 | 0.5902 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.10 | 0.5876 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.10 | 0.5980 | 0.0242 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.05 | 0.6523 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.63 | 0.6296 | 0.0214 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.90 | 0.6424 | 0.0201 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 18.46 | 0.5605 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.62 | 0.6155 | 0.0236 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 19.51 | 0.6039 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.37 | 0.6044 | 0.0234 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 19.29 | 0.5933 | 0.0226 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 18.42 | 0.5586 | 0.0258 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.31 | 0.5952 | 0.0231 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.37 | 0.5920 | 0.0223 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.14 | 0.5881 | 0.0233 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.24 | 0.5921 | 0.0226 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 18.80 | 0.5891 | 0.0233 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.50 | 0.5707 | 0.0282 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.22 | 0.5885 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.02 | 0.5901 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.06 | 0.5890 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.98 | 0.6003 | 0.0243 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.89 | 0.6417 | 0.0202 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.60 | 0.6324 | 0.0222 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.78 | 0.6390 | 0.0214 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.86 | 0.5928 | 0.0241 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.16 | 0.5849 | 0.0252 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 19.48 | 0.5982 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.35 | 0.5993 | 0.0243 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.40 | 0.6001 | 0.0238 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.15 | 0.5908 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.54 | 0.6210 | 0.0215 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.32 | 0.6084 | 0.0230 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.43 | 0.6173 | 0.0221 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.35 | 0.7094 | 0.0264 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.34 | 0.4725 | 0.2062 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.63 | 0.4957 | 0.1922 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.48 | 0.5013 | 0.1985 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.55 | 0.5005 | 0.1951 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 8.73 | 0.4463 | 0.1875 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.80 | 0.4915 | 0.1735 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 8.71 | 0.4820 | 0.1798 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 8.70 | 0.4902 | 0.1767 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.88 | 0.5531 | 0.1073 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.95 | 0.5697 | 0.1080 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.95 | 0.5697 | 0.1080 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.78 | 0.5551 | 0.1088 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.78 | 0.5551 | 0.1088 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.81 | 0.4400 | 0.1382 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.61 | 0.4229 | 0.1518 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.61 | 0.4229 | 0.1518 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.52 | 0.4081 | 0.1528 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.52 | 0.4081 | 0.1528 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.25 | 0.3708 | 0.1630 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.85 | 0.4976 | 0.1757 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.27 | 0.5249 | 0.1569 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.04 | 0.5254 | 0.1668 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.14 | 0.5255 | 0.1620 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.97 | 0.5358 | 0.1661 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.11 | 0.5731 | 0.1507 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.04 | 0.5733 | 0.1579 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.06 | 0.5761 | 0.1542 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.63 | 0.4349 | 0.1448 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.65 | 0.4674 | 0.2052 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.06 | 0.4958 | 0.1879 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.83 | 0.4942 | 0.1969 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.92 | 0.4965 | 0.1925 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.57 | 0.4668 | 0.1973 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.89 | 0.4981 | 0.1807 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.68 | 0.4917 | 0.1897 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.77 | 0.4962 | 0.1851 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.90 | 0.7082 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 23.59 | 0.7171 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 23.56 | 0.7189 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 23.57 | 0.7182 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.48 | 0.7202 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.30 | 0.7403 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 23.95 | 0.7327 | 0.0297 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.16 | 0.7371 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.65 | 0.7003 | 0.0387 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 23.73 | 0.7228 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 23.67 | 0.7191 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 23.45 | 0.7169 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 23.43 | 0.7139 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.70 | 0.7042 | 0.0342 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.58 | 0.7195 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 23.57 | 0.7150 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 23.38 | 0.7150 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 23.40 | 0.7135 | 0.0307 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 23.00 | 0.7119 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 22.64 | 0.7011 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 23.39 | 0.7124 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 23.19 | 0.7124 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 23.21 | 0.7121 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.16 | 0.7155 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.06 | 0.7338 | 0.0295 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 23.80 | 0.7304 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 23.94 | 0.7328 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 22.95 | 0.7092 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 23.48 | 0.7144 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 23.93 | 0.7242 | 0.0304 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 23.73 | 0.7224 | 0.0324 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 23.83 | 0.7237 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 23.58 | 0.7163 | 0.0318 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.91 | 0.7281 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.79 | 0.7241 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.82 | 0.7265 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 21.58 | 0.6799 | 0.0451 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.33 | 0.6902 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.31 | 0.6967 | 0.0423 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.32 | 0.6945 | 0.0407 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 22.37 | 0.6936 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.06 | 0.7216 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.89 | 0.7154 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 23.08 | 0.7204 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.18 | 0.6764 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 23.34 | 0.7090 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 23.38 | 0.7110 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 22.93 | 0.6971 | 0.0390 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 23.02 | 0.7019 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.23 | 0.6863 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.17 | 0.7046 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 23.27 | 0.7048 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 22.85 | 0.6946 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.95 | 0.6992 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 21.81 | 0.6701 | 0.0514 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 20.92 | 0.6544 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.68 | 0.6686 | 0.0443 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.41 | 0.6720 | 0.0486 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.44 | 0.6701 | 0.0466 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.68 | 0.6811 | 0.0472 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.56 | 0.7083 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.37 | 0.7091 | 0.0431 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.47 | 0.7114 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.12 | 0.6403 | 0.0640 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.01 | 0.6804 | 0.0480 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.48 | 0.6890 | 0.0453 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.33 | 0.6921 | 0.0468 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.42 | 0.6919 | 0.0455 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 22.23 | 0.6767 | 0.0473 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 22.47 | 0.6941 | 0.0416 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 22.44 | 0.6909 | 0.0453 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 22.33 | 0.6934 | 0.0433 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 41.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.07 | 0.6945 | 0.0324 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.49 | 0.3829 | 0.3324 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.55 | 0.3983 | 0.3226 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.53 | 0.4016 | 0.3273 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.54 | 0.4011 | 0.3250 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.42 | 0.3609 | 0.2909 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.35 | 0.3867 | 0.2812 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.34 | 0.3806 | 0.2863 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.30 | 0.3850 | 0.2836 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.61 | 0.5245 | 0.1659 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.68 | 0.5323 | 0.1651 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.68 | 0.5323 | 0.1651 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.57 | 0.5236 | 0.1661 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.57 | 0.5236 | 0.1661 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.35 | 0.2984 | 0.2145 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.37 | 0.3007 | 0.2174 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.37 | 0.3007 | 0.2174 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.33 | 0.2938 | 0.2186 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.33 | 0.2938 | 0.2186 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.33 | 0.2903 | 0.2190 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.39 | 0.4170 | 0.3025 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.47 | 0.4379 | 0.2881 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.43 | 0.4377 | 0.2958 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.45 | 0.4386 | 0.2921 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.42 | 0.4463 | 0.2923 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.47 | 0.4728 | 0.2824 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.45 | 0.4698 | 0.2878 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.46 | 0.4727 | 0.2854 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.54 | 0.3695 | 0.1949 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.55 | 0.3835 | 0.3282 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.67 | 0.4041 | 0.3167 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.60 | 0.4020 | 0.3240 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.63 | 0.4036 | 0.3208 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.56 | 0.3905 | 0.3207 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.62 | 0.4085 | 0.3107 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.59 | 0.4075 | 0.3166 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.60 | 0.4095 | 0.3135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.83 | 0.6968 | 0.0397 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.56 | 0.7026 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.52 | 0.7039 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.52 | 0.7034 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.50 | 0.7054 | 0.0363 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.25 | 0.7181 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.95 | 0.7131 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.16 | 0.7161 | 0.0330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.37 | 0.6875 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.64 | 0.7048 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.59 | 0.7022 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.41 | 0.7009 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.39 | 0.6986 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.42 | 0.6903 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.51 | 0.7030 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.46 | 0.6996 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.36 | 0.7002 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.34 | 0.6987 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 24.99 | 0.7007 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.54 | 0.6921 | 0.0418 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.51 | 0.6999 | 0.0366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.19 | 0.6999 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.31 | 0.6999 | 0.0378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.99 | 0.7002 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.94 | 0.7127 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.63 | 0.7098 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.79 | 0.7117 | 0.0356 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 24.97 | 0.7002 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.32 | 0.7001 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.81 | 0.7067 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.62 | 0.7060 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.72 | 0.7069 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.41 | 0.7019 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.75 | 0.7099 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.59 | 0.7069 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.66 | 0.7090 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.01 | 0.6823 | 0.0468 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.93 | 0.6903 | 0.0415 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.92 | 0.6936 | 0.0436 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.93 | 0.6924 | 0.0423 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.00 | 0.6940 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.84 | 0.7134 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.52 | 0.7067 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.72 | 0.7108 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.00 | 0.6802 | 0.0473 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.26 | 0.6985 | 0.0408 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.30 | 0.6975 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.98 | 0.6926 | 0.0412 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.07 | 0.6933 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.02 | 0.6840 | 0.0426 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.12 | 0.6966 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.16 | 0.6943 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.90 | 0.6922 | 0.0409 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.96 | 0.6926 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.59 | 0.6916 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 23.29 | 0.6649 | 0.0541 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.40 | 0.6779 | 0.0446 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.12 | 0.6783 | 0.0498 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.22 | 0.6783 | 0.0474 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.20 | 0.6832 | 0.0466 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.31 | 0.7046 | 0.0403 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.03 | 0.7009 | 0.0441 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.18 | 0.7038 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.36 | 0.6844 | 0.0454 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.46 | 0.6853 | 0.0467 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.24 | 0.6962 | 0.0421 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.96 | 0.6955 | 0.0453 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.11 | 0.6966 | 0.0435 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.76 | 0.6870 | 0.0447 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.83 | 0.6993 | 0.0400 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.84 | 0.6960 | 0.0428 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.80 | 0.6985 | 0.0416 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 74.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.73 | 0.7262 | 0.0343 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.10 | 0.3330 | 0.3528 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.13 | 0.3355 | 0.3460 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.12 | 0.3399 | 0.3492 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.12 | 0.3388 | 0.3475 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.06 | 0.2855 | 0.3217 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.95 | 0.2988 | 0.3159 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.97 | 0.2983 | 0.3188 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.94 | 0.2998 | 0.3176 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.63 | 0.5429 | 0.2236 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.54 | 0.5351 | 0.2288 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.54 | 0.5351 | 0.2288 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.53 | 0.5333 | 0.2287 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.53 | 0.5333 | 0.2287 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.78 | 0.2047 | 0.2539 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.81 | 0.2031 | 0.2557 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.81 | 0.2031 | 0.2557 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.80 | 0.2017 | 0.2564 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.80 | 0.2017 | 0.2564 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.78 | 0.1988 | 0.2564 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.62 | 0.3567 | 0.3309 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.68 | 0.3638 | 0.3200 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.65 | 0.3666 | 0.3256 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.66 | 0.3663 | 0.3228 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.61 | 0.3667 | 0.3261 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.64 | 0.3770 | 0.3173 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.62 | 0.3773 | 0.3227 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.63 | 0.3781 | 0.3202 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.18 | 0.2490 | 0.2390 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.99 | 0.3133 | 0.3564 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.10 | 0.3202 | 0.3494 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.02 | 0.3204 | 0.3531 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.05 | 0.3207 | 0.3511 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.99 | 0.3173 | 0.3504 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.03 | 0.3241 | 0.3437 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.01 | 0.3256 | 0.3476 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.02 | 0.3255 | 0.3454 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.55 | 0.7236 | 0.0352 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.55 | 0.7237 | 0.0353 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.59 | 0.7241 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.58 | 0.7240 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.60 | 0.7242 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.70 | 0.7256 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.68 | 0.7252 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.70 | 0.7255 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.74 | 0.7264 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.69 | 0.7260 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.69 | 0.7258 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.70 | 0.7260 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.70 | 0.7258 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.72 | 0.7260 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.69 | 0.7256 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.70 | 0.7259 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.69 | 0.7256 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.71 | 0.7259 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.70 | 0.7257 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.62 | 0.7245 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.60 | 0.7245 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.62 | 0.7247 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.61 | 0.7246 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.66 | 0.7249 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.70 | 0.7256 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.69 | 0.7255 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.70 | 0.7256 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.70 | 0.7260 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.48 | 0.7237 | 0.0353 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.48 | 0.7237 | 0.0354 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.48 | 0.7237 | 0.0354 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.48 | 0.7237 | 0.0354 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.52 | 0.7241 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.53 | 0.7246 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.53 | 0.7244 | 0.0351 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.53 | 0.7246 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.80 | 0.7162 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.91 | 0.7160 | 0.0393 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.02 | 0.7177 | 0.0393 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.99 | 0.7173 | 0.0391 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.09 | 0.7191 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.55 | 0.7242 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.46 | 0.7228 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.53 | 0.7238 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.75 | 0.7271 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.43 | 0.7247 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.42 | 0.7239 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.50 | 0.7247 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.49 | 0.7240 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.69 | 0.7263 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.46 | 0.7243 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.51 | 0.7244 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.51 | 0.7243 | 0.0358 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.56 | 0.7245 | 0.0354 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.57 | 0.7251 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.53 | 0.7123 | 0.0441 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.62 | 0.7130 | 0.0421 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.68 | 0.7143 | 0.0430 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.66 | 0.7140 | 0.0425 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.71 | 0.7155 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.11 | 0.7203 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.99 | 0.7193 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.06 | 0.7201 | 0.0399 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.35 | 0.7237 | 0.0374 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.82 | 0.7118 | 0.0424 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.83 | 0.7119 | 0.0423 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.82 | 0.7122 | 0.0426 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.84 | 0.7124 | 0.0423 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.60 | 0.7120 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.40 | 0.7142 | 0.0416 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.52 | 0.7135 | 0.0419 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.44 | 0.7140 | 0.0417 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.36 | 0.7141 | 0.0567 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.88 | 0.3567 | 0.4258 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.93 | 0.3635 | 0.4111 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.91 | 0.3685 | 0.4190 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.92 | 0.3672 | 0.4146 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.70 | 0.3223 | 0.3928 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.61 | 0.3464 | 0.3760 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.62 | 0.3412 | 0.3854 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.59 | 0.3453 | 0.3806 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.93 | 0.5371 | 0.3215 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.90 | 0.5343 | 0.3209 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.90 | 0.5343 | 0.3209 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.86 | 0.5295 | 0.3214 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.86 | 0.5295 | 0.3214 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.22 | 0.2641 | 0.3409 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.27 | 0.2622 | 0.3434 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.27 | 0.2622 | 0.3434 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.24 | 0.2578 | 0.3439 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.24 | 0.2578 | 0.3439 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.22 | 0.2547 | 0.3458 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.47 | 0.3775 | 0.4010 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.54 | 0.3892 | 0.3780 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.51 | 0.3914 | 0.3917 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.53 | 0.3913 | 0.3853 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.47 | 0.3967 | 0.3879 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.50 | 0.4153 | 0.3691 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.49 | 0.4138 | 0.3808 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.49 | 0.4157 | 0.3754 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.64 | 0.3040 | 0.3158 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.75 | 0.3378 | 0.4340 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.87 | 0.3491 | 0.4183 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.79 | 0.3493 | 0.4279 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.82 | 0.3497 | 0.4233 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.74 | 0.3428 | 0.4185 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.79 | 0.3564 | 0.4034 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.76 | 0.3554 | 0.4125 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.77 | 0.3569 | 0.4077 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.97 | 0.7108 | 0.0678 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.34 | 0.7130 | 0.0638 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.40 | 0.7143 | 0.0652 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.38 | 0.7139 | 0.0641 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.40 | 0.7153 | 0.0638 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.99 | 0.7234 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.76 | 0.7203 | 0.0611 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.92 | 0.7222 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.05 | 0.7123 | 0.0685 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.70 | 0.7186 | 0.0616 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.64 | 0.7169 | 0.0606 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.55 | 0.7169 | 0.0615 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.51 | 0.7153 | 0.0606 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.03 | 0.7124 | 0.0643 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.56 | 0.7166 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.59 | 0.7158 | 0.0604 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.45 | 0.7153 | 0.0616 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.50 | 0.7155 | 0.0607 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.26 | 0.7156 | 0.0614 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.93 | 0.7103 | 0.0683 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.41 | 0.7131 | 0.0632 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.29 | 0.7136 | 0.0654 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.30 | 0.7133 | 0.0644 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.27 | 0.7147 | 0.0641 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.85 | 0.7210 | 0.0601 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.69 | 0.7198 | 0.0626 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.78 | 0.7207 | 0.0614 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.27 | 0.7159 | 0.0623 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.35 | 0.7128 | 0.0657 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.55 | 0.7150 | 0.0632 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.46 | 0.7149 | 0.0648 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.51 | 0.7152 | 0.0637 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.40 | 0.7140 | 0.0633 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.63 | 0.7187 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.52 | 0.7168 | 0.0620 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.57 | 0.7181 | 0.0610 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.27 | 0.6995 | 0.0788 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.76 | 0.7020 | 0.0723 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.88 | 0.7052 | 0.0749 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.85 | 0.7042 | 0.0731 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.95 | 0.7068 | 0.0721 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.72 | 0.7205 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.44 | 0.7159 | 0.0678 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.62 | 0.7188 | 0.0653 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.85 | 0.7098 | 0.0720 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.41 | 0.7148 | 0.0670 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.38 | 0.7135 | 0.0636 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.24 | 0.7123 | 0.0669 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.26 | 0.7118 | 0.0637 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.80 | 0.7101 | 0.0678 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.27 | 0.7126 | 0.0670 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.35 | 0.7124 | 0.0638 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.14 | 0.7107 | 0.0668 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.24 | 0.7119 | 0.0641 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.97 | 0.7108 | 0.0680 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.85 | 0.6905 | 0.0874 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.41 | 0.6948 | 0.0770 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.34 | 0.6966 | 0.0826 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.34 | 0.6960 | 0.0799 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.49 | 0.7011 | 0.0788 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.26 | 0.7133 | 0.0701 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.08 | 0.7112 | 0.0758 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.18 | 0.7130 | 0.0731 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.80 | 0.7073 | 0.0721 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.16 | 0.6979 | 0.0807 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.48 | 0.7010 | 0.0761 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.36 | 0.7015 | 0.0800 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.42 | 0.7018 | 0.0777 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.21 | 0.6984 | 0.0782 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.34 | 0.7066 | 0.0717 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.31 | 0.7039 | 0.0761 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.31 | 0.7058 | 0.0740 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 228358 | 0.333 | 65.5 | 28.51 | 0.20 | 0.022 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 228358 | 0.333 | 59.3 | 28.51 | 0.20 | 0.022 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 228358 | 0.333 | 75.2 | 28.51 | 0.20 | 0.022 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 228358 | 0.333 | 66.3 | 28.51 | 0.20 | 0.022 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 838 | None | classic | 0.43 | False | 508642 | 0.976 | 202.5 | 31.28 | 0.25 | 0.001 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 838 | None | classic | 0.43 | False | 508642 | 0.976 | 187.3 | 31.28 | 0.25 | 0.001 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 838 | None | classic | 0.43 | False | 508642 | 0.976 | 205.5 | 31.28 | 0.25 | 0.001 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 838 | None | classic | 0.43 | False | 508642 | 0.976 | 180.2 | 31.28 | 0.25 | 0.001 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1414493 | 0.178 | 45.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1414493 | 0.793 | 50.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1414493 | 0.793 | 50.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1414493 | 0.491 | 46.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1414493 | 0.491 | 46.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1414493 | 0.178 | 53.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1414493 | 0.793 | 194.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1414493 | 0.793 | 194.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1414493 | 0.491 | 53.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1414493 | 0.491 | 53.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1412384 | 0.793 | 489.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 236982 | 0.332 | 66.7 | 28.31 | 0.13 | 0.014 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 236982 | 0.332 | 51.9 | 28.31 | 0.13 | 0.014 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 236982 | 0.332 | 54.6 | 28.31 | 0.13 | 0.014 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 236982 | 0.332 | 69.6 | 28.31 | 0.13 | 0.014 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1159 | None | classic | 2.01 | False | 420147 | 0.658 | 142.2 | 28.77 | 0.13 | 0.026 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1159 | None | classic | 2.01 | False | 420147 | 0.658 | 118.2 | 28.77 | 0.13 | 0.026 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1159 | None | classic | 2.01 | False | 420147 | 0.658 | 118.2 | 28.77 | 0.13 | 0.026 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1159 | None | classic | 2.01 | False | 420147 | 0.658 | 111.6 | 28.77 | 0.13 | 0.026 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1798100 | 0.793 | 129.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 223091 | 0.914 | 85.0 | 28.80 | 0.23 | 0.024 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 223091 | 0.914 | 78.2 | 28.80 | 0.23 | 0.024 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 223091 | 0.914 | 106.1 | 28.80 | 0.23 | 0.024 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 223091 | 0.914 | 66.9 | 28.80 | 0.23 | 0.024 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 875 | None | classic | 1.14 | False | 510115 | 0.984 | 157.4 | 28.10 | 0.25 | 0.027 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 875 | None | classic | 1.14 | False | 510115 | 0.984 | 164.4 | 28.10 | 0.25 | 0.027 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 875 | None | classic | 1.14 | False | 510115 | 0.984 | 145.2 | 28.10 | 0.25 | 0.027 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 875 | None | classic | 1.14 | False | 510115 | 0.984 | 158.5 | 28.10 | 0.25 | 0.027 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.696 | 0.041 |
| in035 | mask_ent | 0.703 | 0.041 |
| in035 | mask_grad | 0.427 | 0.041 |
| in035 | r_col | 0.837 | 0.041 |
| in035 | r_warp | 0.873 | 0.041 |

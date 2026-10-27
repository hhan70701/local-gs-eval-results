# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 2.9% | 26.06 / 0.0043 | 20.32 / 0.0127 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.2% | 26.06 / 0.0046 | 21.21 / 0.0107 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.0% | 26.13 / 0.0044 | 21.02 / 0.0111 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.1% | 26.08 / 0.0044 | 20.87 / 0.0110 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.8% | 26.04 / 0.0040 | 18.70 / 0.0112 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.0% | 26.22 / 0.0044 | 21.50 / 0.0101 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.8% | 26.10 / 0.0041 | 19.57 / 0.0100 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.9% | 26.17 / 0.0041 | 20.09 / 0.0096 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 2.9% | 25.97 / 0.0044 | 26.23 / 0.0059 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 2.6% | 25.94 / 0.0042 | 24.39 / 0.0125 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 0.3% | 22.14 / 0.0019 | 19.63 / 0.0047 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 2.5% | 25.70 / 0.0043 | 24.00 / 0.0124 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 0.3% | 21.46 / 0.0020 | 19.63 / 0.0047 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 2.8% | 25.99 / 0.0041 | 25.91 / 0.0048 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 2.5% | 25.98 / 0.0040 | 23.86 / 0.0099 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 0.4% | 22.29 / 0.0017 | 19.82 / 0.0044 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 2.5% | 25.67 / 0.0044 | 23.33 / 0.0104 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 0.4% | 22.31 / 0.0016 | 19.70 / 0.0051 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 3.2% | 26.11 / 0.0045 | 22.47 / 0.0139 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 4.8% | 25.71 / 0.0048 | 21.64 / 0.0147 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.0% | 25.78 / 0.0049 | 22.43 / 0.0107 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.8% | 25.78 / 0.0047 | 22.30 / 0.0124 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.9% | 25.77 / 0.0047 | 22.23 / 0.0115 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 4.3% | 25.65 / 0.0043 | 20.27 / 0.0122 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.5% | 25.85 / 0.0044 | 22.51 / 0.0092 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.3% | 25.73 / 0.0041 | 21.81 / 0.0102 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.4% | 25.77 / 0.0042 | 21.92 / 0.0098 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 5.1% | 25.85 / 0.0057 | 22.38 / 0.0186 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 2.0% | 26.87 / 0.0198 | 25.19 / 0.0280 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 2.2% | 27.09 / 0.0230 | 26.60 / 0.0264 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 2.0% | 26.94 / 0.0221 | 25.83 / 0.0290 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 2.1% | 27.03 / 0.0229 | 26.32 / 0.0281 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 1.7% | 26.32 / 0.0202 | 25.99 / 0.0229 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 1.9% | 26.52 / 0.0222 | 26.45 / 0.0178 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 1.8% | 26.38 / 0.0223 | 26.88 / 0.0188 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 1.8% | 26.42 / 0.0225 | 26.95 / 0.0171 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.76 / 0.0522 | 38.18 / 0.0213 | 21.79 / 0.0091 | 29.88 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.28 / 0.0568 | 38.18 / 0.0213 | 21.59 / 0.0102 | 29.70 / 0.0420 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.29 / 0.0552 | 38.18 / 0.0213 | 21.49 / 0.0101 | 29.80 / 0.0413 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.28 / 0.0562 | 38.18 / 0.0213 | 21.40 / 0.0103 | 29.79 / 0.0415 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.26 / 0.0558 | 38.18 / 0.0213 | 21.38 / 0.0104 | 29.80 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.58 / 0.0548 | 38.18 / 0.0213 | 20.87 / 0.0106 | 29.31 / 0.0420 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.38 / 0.0541 | 38.18 / 0.0213 | 21.69 / 0.0095 | 29.81 / 0.0409 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.91 / 0.0547 | 38.18 / 0.0213 | 21.22 / 0.0103 | 29.61 / 0.0416 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.11 / 0.0543 | 38.18 / 0.0213 | 21.43 / 0.0100 | 29.73 / 0.0412 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.83 / 0.0529 | 38.18 / 0.0213 | 22.04 / 0.0094 | 29.89 / 0.0405 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.73 / 0.0550 | 38.18 / 0.0213 | 21.75 / 0.0103 | 29.88 / 0.0405 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.73 / 0.0534 | 38.18 / 0.0213 | 21.65 / 0.0095 | 29.88 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.71 / 0.0555 | 38.18 / 0.0213 | 21.77 / 0.0104 | 29.88 / 0.0405 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.73 / 0.0534 | 38.18 / 0.0213 | 21.74 / 0.0097 | 29.88 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.78 / 0.0526 | 38.18 / 0.0213 | 22.00 / 0.0090 | 29.87 / 0.0406 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.69 / 0.0538 | 38.18 / 0.0213 | 21.71 / 0.0097 | 29.85 / 0.0405 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.73 / 0.0530 | 38.18 / 0.0213 | 21.68 / 0.0094 | 29.87 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.67 / 0.0546 | 38.18 / 0.0213 | 21.70 / 0.0100 | 29.86 / 0.0406 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.72 / 0.0537 | 38.18 / 0.0213 | 21.73 / 0.0097 | 29.87 / 0.0404 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.65 / 0.0547 | 38.18 / 0.0213 | 21.68 / 0.0105 | 29.85 / 0.0406 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.27 / 0.0582 | 38.18 / 0.0213 | 21.37 / 0.0101 | 29.66 / 0.0424 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.35 / 0.0554 | 38.18 / 0.0213 | 21.60 / 0.0096 | 29.65 / 0.0416 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.38 / 0.0571 | 38.18 / 0.0213 | 21.69 / 0.0097 | 29.70 / 0.0420 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.36 / 0.0562 | 38.18 / 0.0213 | 21.63 / 0.0097 | 29.68 / 0.0418 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.69 / 0.0559 | 38.18 / 0.0213 | 20.98 / 0.0104 | 29.53 / 0.0424 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.36 / 0.0549 | 38.18 / 0.0213 | 21.64 / 0.0097 | 29.74 / 0.0411 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.05 / 0.0556 | 38.18 / 0.0213 | 21.48 / 0.0101 | 29.70 / 0.0418 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.17 / 0.0555 | 38.18 / 0.0213 | 21.57 / 0.0100 | 29.74 / 0.0414 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.51 / 0.0569 | 38.18 / 0.0213 | 21.62 / 0.0116 | 29.81 / 0.0408 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 28.71 / 0.0529 | 38.11 / 0.0236 | 21.94 / 0.0083 | 29.87 / 0.0409 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.78 / 0.0521 | 38.15 / 0.0228 | 22.11 / 0.0081 | 29.88 / 0.0408 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.74 / 0.0527 | 38.09 / 0.0240 | 22.03 / 0.0082 | 29.87 / 0.0410 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.77 / 0.0524 | 38.10 / 0.0239 | 22.08 / 0.0082 | 29.88 / 0.0409 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.74 / 0.0524 | 37.80 / 0.0251 | 21.93 / 0.0082 | 29.87 / 0.0409 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.78 / 0.0518 | 38.15 / 0.0221 | 22.04 / 0.0082 | 29.88 / 0.0406 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.76 / 0.0523 | 37.97 / 0.0238 | 21.92 / 0.0082 | 29.88 / 0.0408 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.76 / 0.0521 | 38.10 / 0.0227 | 21.95 / 0.0082 | 29.88 / 0.0407 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.1%） | — | — | 28.76 / 0.0522 | 38.18 / 0.0213 | 29.88 |
| in035 | rife | 1.0% | 2.0% | 28.71 / 0.0529 | 38.11 / 0.0236 | 29.87 |
| in035 | cnw_cnn | 1.3% | 2.9% | 28.28 / 0.0568 | 38.18 / 0.0213 | 29.70 |
| in035 | cnw_f5 | 2.4% | 4.8% | 28.27 / 0.0582 | 38.18 / 0.0213 | 29.66 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.62 / 0.0539 | -0.07 / +0.0008 (core 0.9%) | -0.38 / +0.0059 (core 1.6%) | -0.52 / +0.0084 (core 3.1%) |
| in035 | 2 | 0-3 | 28.98 / 0.0508 | -0.04 / +0.0004 (core 0.9%) | -0.66 / +0.0056 (core 1.6%) | -0.79 / +0.0084 (core 3.1%) |
| in035 | 4 | 3-5 | 29.67 / 0.0518 | -0.04 / +0.0009 (core 0.6%) | -0.38 / +0.0024 (core 0.5%) | -0.16 / +0.0013 (core 0.6%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.76 / 0.0522 | — | 29.88 | — |
| in035 | cnw_cnn | 不复核 | —% | 28.28 / 0.0568 | — | 29.70 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.64 / 0.0533 | — | 29.86 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.29 / 0.0552 | — | 29.80 | 0/3 |
| in035 | cnw_cnn | oracle | 0.6% | 28.57 / 0.0530 | — | 29.86 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.28 / 0.0562 | — | 29.79 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.56 / 0.0532 | — | 29.86 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.26 / 0.0558 | — | 29.80 | 0/3 |
| in035 | cnw_cnn | oracle | 0.5% | 28.55 / 0.0533 | — | 29.86 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.58 / 0.0548 | — | 29.31 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.29 / 0.0532 | — | 29.86 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.38 / 0.0541 | — | 29.81 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.64 / 0.0527 | — | 29.88 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.91 / 0.0547 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.43 / 0.0531 | — | 29.87 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.11 / 0.0543 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.52 / 0.0529 | — | 29.87 | 1/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 28.83 / 0.0529 | — | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 0.5% | 28.82 / 0.0526 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 28.73 / 0.0550 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 0.5% | 28.78 / 0.0535 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 28.73 / 0.0534 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 0.1% | 28.75 / 0.0526 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 28.71 / 0.0555 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 0.5% | 28.76 / 0.0539 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 28.73 / 0.0534 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 0.2% | 28.76 / 0.0528 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 28.78 / 0.0526 | — | 29.87 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 0.5% | 28.81 / 0.0522 | — | 29.88 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.69 / 0.0538 | — | 29.85 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 0.4% | 28.77 / 0.0527 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.73 / 0.0530 | — | 29.87 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.2% | 28.76 / 0.0525 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 28.67 / 0.0546 | — | 29.86 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 0.5% | 28.74 / 0.0532 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 28.72 / 0.0537 | — | 29.87 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 0.2% | 28.75 / 0.0530 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 28.65 / 0.0547 | — | 29.85 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 0.5% | 28.75 / 0.0536 | — | 29.88 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.27 / 0.0582 | — | 29.66 | 0/3 |
| in035 | cnw_f5 | oracle | 0.9% | 28.61 / 0.0536 | — | 29.86 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.35 / 0.0554 | — | 29.65 | 0/3 |
| in035 | cnw_f5 | oracle | 0.9% | 28.65 / 0.0527 | — | 29.86 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.38 / 0.0571 | — | 29.70 | 0/3 |
| in035 | cnw_f5 | oracle | 0.9% | 28.68 / 0.0531 | — | 29.86 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.36 / 0.0562 | — | 29.68 | 0/3 |
| in035 | cnw_f5 | oracle | 0.9% | 28.65 / 0.0530 | — | 29.86 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.69 / 0.0559 | — | 29.53 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.8% | 28.46 / 0.0531 | — | 29.87 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.36 / 0.0549 | — | 29.74 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.8% | 28.66 / 0.0527 | — | 29.87 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.05 / 0.0556 | — | 29.70 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.8% | 28.59 / 0.0529 | — | 29.87 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.17 / 0.0555 | — | 29.74 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.8% | 28.63 / 0.0527 | — | 29.87 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 28.51 / 0.0569 | — | 29.81 | 0/3 |
| in035 | cnw_f5_pix | oracle | 0.9% | 28.71 / 0.0545 | — | 29.88 | 0/3 |
| in035 | rife | 不复核 | —% | 28.71 / 0.0529 | — | 29.87 | 0/3 |
| in035 | rife | oracle | 0.3% | 28.77 / 0.0516 | — | 29.88 | 1/3 |
| in035 | rife | 不复核 | —% | 28.78 / 0.0521 | — | 29.88 | 2/3 |
| in035 | rife | oracle | 0.3% | 28.81 / 0.0513 | — | 29.88 | 3/3 |
| in035 | rife | 不复核 | —% | 28.74 / 0.0527 | — | 29.87 | 0/3 |
| in035 | rife | oracle | 0.3% | 28.79 / 0.0515 | — | 29.88 | 3/3 |
| in035 | rife | 不复核 | —% | 28.77 / 0.0524 | — | 29.88 | 1/3 |
| in035 | rife | oracle | 0.3% | 28.80 / 0.0514 | — | 29.88 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 28.74 / 0.0524 | — | 29.87 | 0/3 |
| in035 | rife_mw | oracle | 0.3% | 28.78 / 0.0514 | — | 29.88 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 28.78 / 0.0518 | — | 29.88 | 2/3 |
| in035 | rife_mw | oracle | 0.3% | 28.80 / 0.0512 | — | 29.88 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 28.76 / 0.0523 | — | 29.88 | 2/3 |
| in035 | rife_mw | oracle | 0.3% | 28.78 / 0.0513 | — | 29.88 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 28.76 / 0.0521 | — | 29.88 | 2/3 |
| in035 | rife_mw | oracle | 0.3% | 28.79 / 0.0512 | — | 29.88 | 3/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.76 / 0.0522 | — / — | — |
| in035 | FF | 0（前馈） | 909×664（58%） | 26.95 | 28.28 / 0.0568 | — / — | 0/3 |
| in035 | 25 | 0.55 s | 909×664（58%） | 27.37 | 28.28 / 0.0562 | — / — | 0/3 |
| in035 | 50 | 1.08 s | 909×664（58%） | 27.57 | 28.26 / 0.0558 | — / — | 0/3 |
| in035 | 100 | 2.12 s | 909×664（58%） | 27.78 | 28.29 / 0.0552 | — / — | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.76 / 0.0522 | — / — | 29.88 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 28.28 / 0.0568 | — / — | 29.70 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.64 / 0.0533 | — / — | 29.86 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.28 / 0.0562 | — / — | 29.79 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.56 / 0.0532 | — / — | 29.86 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 28.26 / 0.0558 | — / — | 29.80 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.55 / 0.0533 | — / — | 29.86 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 28.29 / 0.0552 | — / — | 29.80 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.57 / 0.0530 | — / — | 29.86 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.58 / 0.0548 | — / — | 29.31 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.29 / 0.0532 | — / — | 29.86 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.91 / 0.0547 | — / — | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.43 / 0.0531 | — / — | 29.87 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.11 / 0.0543 | — / — | 29.73 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.52 / 0.0529 | — / — | 29.87 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.38 / 0.0541 | — / — | 29.81 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.64 / 0.0527 | — / — | 29.88 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 28.27 / 0.0582 | — / — | 29.66 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 28.61 / 0.0536 | — / — | 29.86 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 28.38 / 0.0571 | — / — | 29.70 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 28.68 / 0.0531 | — / — | 29.86 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 28.36 / 0.0562 | — / — | 29.68 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.65 / 0.0530 | — / — | 29.86 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 28.35 / 0.0554 | — / — | 29.65 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.65 / 0.0527 | — / — | 29.86 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.69 / 0.0559 | — / — | 29.53 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.46 / 0.0531 | — / — | 29.87 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 28.05 / 0.0556 | — / — | 29.70 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.59 / 0.0529 | — / — | 29.87 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 28.17 / 0.0555 | — / — | 29.74 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.63 / 0.0527 | — / — | 29.87 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.36 / 0.0549 | — / — | 29.74 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.66 / 0.0527 | — / — | 29.87 | 0/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 28.71 / 0.0529 | — / — | 29.87 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.77 / 0.0516 | — / — | 29.88 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.74 / 0.0527 | — / — | 29.87 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.79 / 0.0515 | — / — | 29.88 | 3/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.77 / 0.0524 | — / — | 29.88 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.80 / 0.0514 | — / — | 29.88 | 3/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.78 / 0.0521 | — / — | 29.88 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.81 / 0.0513 | — / — | 29.88 | 3/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 28.74 / 0.0524 | — / — | 29.87 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.78 / 0.0514 | — / — | 29.88 | 3/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.76 / 0.0523 | — / — | 29.88 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.78 / 0.0513 | — / — | 29.88 | 3/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.76 / 0.0521 | — / — | 29.88 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.79 / 0.0512 | — / — | 29.88 | 3/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.78 / 0.0518 | — / — | 29.88 | 2/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.80 / 0.0512 | — / — | 29.88 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 38.18 / 0.0213 | 21.79 / 0.0091 | 29.88 / 0.0404 | 28.76 / 0.0522 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 3.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 38.18 | 0.9278 | 0.0213 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.21 | 0.5603 | 0.7115 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.21 | 0.5603 | 0.7115 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.21 | 0.5603 | 0.7115 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.21 | 0.5603 | 0.7115 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.21 | 0.5603 | 0.7115 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.21 | 0.5603 | 0.7115 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.21 | 0.5603 | 0.7115 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.21 | 0.5603 | 0.7115 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 12.21 | 0.5870 | 0.5530 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 12.20 | 0.5866 | 0.5534 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 12.20 | 0.5866 | 0.5534 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 12.19 | 0.5859 | 0.5535 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 12.19 | 0.5859 | 0.5535 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 7.90 | 0.0006 | 0.6253 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 7.90 | 0.0006 | 0.6253 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 7.90 | 0.0006 | 0.6253 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 7.90 | 0.0006 | 0.6253 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 7.90 | 0.0006 | 0.6253 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 7.90 | 0.0006 | 0.6253 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.21 | 0.5568 | 0.7101 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.21 | 0.5560 | 0.7098 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.21 | 0.5565 | 0.7101 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.21 | 0.5564 | 0.7100 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.21 | 0.5582 | 0.7112 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.21 | 0.5564 | 0.7099 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.21 | 0.5574 | 0.7109 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.21 | 0.5569 | 0.7104 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 7.90 | 0.0006 | 0.6253 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.08 | 0.6273 | 0.5668 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.13 | 0.6319 | 0.5490 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.09 | 0.6303 | 0.5624 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.11 | 0.6312 | 0.5560 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.04 | 0.6221 | 0.5684 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.08 | 0.6278 | 0.5554 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.06 | 0.6242 | 0.5665 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.06 | 0.6259 | 0.5599 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 38.18 | 0.9278 | 0.0213 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 38.11 | 0.9276 | 0.0236 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 38.15 | 0.9276 | 0.0228 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 38.09 | 0.9275 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 38.10 | 0.9275 | 0.0239 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 37.80 | 0.9267 | 0.0251 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 38.15 | 0.9277 | 0.0221 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 37.97 | 0.9271 | 0.0238 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 38.10 | 0.9275 | 0.0227 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 21.79 | 0.7389 | 0.0091 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.20 | 0.2471 | 0.1011 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.32 | 0.2797 | 0.0975 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.24 | 0.2690 | 0.0996 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.27 | 0.2720 | 0.0987 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.04 | 0.1997 | 0.1007 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.20 | 0.2855 | 0.0974 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.09 | 0.2307 | 0.0998 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.13 | 0.2518 | 0.0991 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.07 | 0.3515 | 0.0474 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 13.06 | 0.3389 | 0.0494 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 13.06 | 0.3389 | 0.0494 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 12.94 | 0.3225 | 0.0505 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 12.94 | 0.3225 | 0.0505 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 10.96 | 0.2978 | 0.0576 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.97 | 0.2839 | 0.0591 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.97 | 0.2839 | 0.0591 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 10.94 | 0.2701 | 0.0599 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 10.94 | 0.2701 | 0.0599 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.92 | 0.2680 | 0.0600 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.04 | 0.3965 | 0.0861 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.23 | 0.4314 | 0.0810 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.11 | 0.4282 | 0.0840 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.17 | 0.4323 | 0.0825 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.84 | 0.3448 | 0.0869 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.00 | 0.4257 | 0.0831 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.91 | 0.3955 | 0.0855 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.95 | 0.4145 | 0.0847 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.71 | 0.4328 | 0.0523 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.41 | 0.1369 | 0.1145 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.41 | 0.1512 | 0.1140 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.41 | 0.1450 | 0.1144 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.41 | 0.1484 | 0.1142 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.38 | 0.1427 | 0.1149 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.39 | 0.1477 | 0.1146 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.38 | 0.1436 | 0.1148 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.38 | 0.1442 | 0.1148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 21.60 | 0.7368 | 0.0101 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.49 | 0.7354 | 0.0101 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.42 | 0.7364 | 0.0102 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.40 | 0.7349 | 0.0103 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.87 | 0.7146 | 0.0106 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.70 | 0.7411 | 0.0095 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.22 | 0.7256 | 0.0103 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.44 | 0.7319 | 0.0100 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.03 | 0.7473 | 0.0094 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.75 | 0.7407 | 0.0102 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 21.66 | 0.7357 | 0.0095 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 21.77 | 0.7381 | 0.0104 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 21.74 | 0.7367 | 0.0097 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.00 | 0.7463 | 0.0091 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.71 | 0.7375 | 0.0096 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 21.69 | 0.7362 | 0.0094 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 21.70 | 0.7369 | 0.0100 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 21.73 | 0.7366 | 0.0097 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 21.68 | 0.7370 | 0.0105 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 21.38 | 0.7313 | 0.0100 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.59 | 0.7502 | 0.0095 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.68 | 0.7452 | 0.0096 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.63 | 0.7493 | 0.0096 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.02 | 0.7232 | 0.0103 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.68 | 0.7522 | 0.0096 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.53 | 0.7438 | 0.0100 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.64 | 0.7494 | 0.0098 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 21.63 | 0.7343 | 0.0114 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 21.94 | 0.7463 | 0.0083 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.11 | 0.7559 | 0.0081 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 22.03 | 0.7514 | 0.0082 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.08 | 0.7539 | 0.0082 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.93 | 0.7535 | 0.0082 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 22.05 | 0.7607 | 0.0081 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.93 | 0.7567 | 0.0082 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.96 | 0.7581 | 0.0081 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 21.59 | 0.7349 | 0.0102 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.49 | 0.7351 | 0.0101 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.40 | 0.7353 | 0.0103 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.38 | 0.7342 | 0.0104 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.87 | 0.7139 | 0.0106 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.69 | 0.7402 | 0.0095 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.22 | 0.7250 | 0.0103 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.43 | 0.7311 | 0.0100 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.04 | 0.7473 | 0.0094 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.75 | 0.7404 | 0.0103 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 21.65 | 0.7358 | 0.0095 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 21.77 | 0.7375 | 0.0104 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 21.74 | 0.7365 | 0.0097 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.00 | 0.7461 | 0.0090 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.71 | 0.7372 | 0.0097 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 21.68 | 0.7364 | 0.0094 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 21.70 | 0.7360 | 0.0100 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 21.73 | 0.7358 | 0.0097 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 21.68 | 0.7362 | 0.0105 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 21.37 | 0.7301 | 0.0101 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.60 | 0.7498 | 0.0096 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.69 | 0.7448 | 0.0097 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.63 | 0.7488 | 0.0097 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.98 | 0.7209 | 0.0104 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.64 | 0.7508 | 0.0097 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.48 | 0.7418 | 0.0101 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.57 | 0.7471 | 0.0100 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.62 | 0.7329 | 0.0116 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.94 | 0.7456 | 0.0083 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.11 | 0.7556 | 0.0081 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.03 | 0.7508 | 0.0082 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.08 | 0.7534 | 0.0082 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.93 | 0.7531 | 0.0082 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 22.04 | 0.7608 | 0.0082 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.92 | 0.7565 | 0.0082 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.95 | 0.7580 | 0.0082 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 19.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.36 | 0.7701 | 0.0139 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.49 | 0.3542 | 0.2095 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.60 | 0.3666 | 0.2045 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.52 | 0.3678 | 0.2073 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.56 | 0.3674 | 0.2059 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.42 | 0.3367 | 0.2079 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.56 | 0.3749 | 0.2032 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.46 | 0.3594 | 0.2058 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.50 | 0.3648 | 0.2046 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.06 | 0.4621 | 0.1079 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.00 | 0.4409 | 0.1163 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.00 | 0.4409 | 0.1163 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 14.87 | 0.4222 | 0.1192 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 14.87 | 0.4222 | 0.1192 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.19 | 0.2696 | 0.1381 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.15 | 0.2420 | 0.1456 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.15 | 0.2420 | 0.1456 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.12 | 0.2291 | 0.1470 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.12 | 0.2291 | 0.1470 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.01 | 0.2042 | 0.1507 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.53 | 0.4213 | 0.1862 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.75 | 0.4453 | 0.1776 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.59 | 0.4442 | 0.1828 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.66 | 0.4457 | 0.1802 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.28 | 0.3844 | 0.1862 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.56 | 0.4212 | 0.1795 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.34 | 0.4083 | 0.1838 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.42 | 0.4139 | 0.1820 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.33 | 0.2774 | 0.1358 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.18 | 0.3003 | 0.2222 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.22 | 0.3068 | 0.2190 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.19 | 0.3060 | 0.2214 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.20 | 0.3072 | 0.2204 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.14 | 0.3037 | 0.2222 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.19 | 0.3027 | 0.2194 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.15 | 0.3065 | 0.2214 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.16 | 0.3049 | 0.2207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.05 | 0.7669 | 0.0151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.89 | 0.7656 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.90 | 0.7666 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.82 | 0.7658 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.10 | 0.7546 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.04 | 0.7665 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.43 | 0.7594 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.69 | 0.7620 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.55 | 0.7739 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.35 | 0.7713 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.28 | 0.7698 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.31 | 0.7692 | 0.0159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.31 | 0.7693 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.53 | 0.7736 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.32 | 0.7701 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.31 | 0.7698 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.22 | 0.7687 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.27 | 0.7688 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.07 | 0.7655 | 0.0163 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.02 | 0.7674 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.16 | 0.7733 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.27 | 0.7721 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.17 | 0.7730 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.50 | 0.7613 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.12 | 0.7711 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.96 | 0.7681 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.01 | 0.7694 | 0.0144 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.94 | 0.7625 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.37 | 0.7714 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.56 | 0.7748 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.46 | 0.7733 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.51 | 0.7742 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.44 | 0.7743 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.53 | 0.7762 | 0.0133 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.46 | 0.7758 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.49 | 0.7761 | 0.0133 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.75 | 0.7455 | 0.0183 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.72 | 0.7484 | 0.0179 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.73 | 0.7504 | 0.0178 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.57 | 0.7492 | 0.0180 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.73 | 0.7324 | 0.0178 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.03 | 0.7535 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.12 | 0.7435 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.36 | 0.7471 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.50 | 0.7717 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.07 | 0.7643 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.15 | 0.7671 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.97 | 0.7592 | 0.0194 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.16 | 0.7654 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.42 | 0.7717 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.96 | 0.7612 | 0.0176 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.13 | 0.7659 | 0.0156 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.83 | 0.7580 | 0.0184 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.04 | 0.7640 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.81 | 0.7428 | 0.0219 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.96 | 0.7465 | 0.0197 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.17 | 0.7613 | 0.0179 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.18 | 0.7593 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.10 | 0.7613 | 0.0184 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.89 | 0.7325 | 0.0183 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.05 | 0.7566 | 0.0170 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.63 | 0.7489 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.69 | 0.7528 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.02 | 0.7205 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.06 | 0.7651 | 0.0149 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.32 | 0.7697 | 0.0142 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.18 | 0.7685 | 0.0147 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.27 | 0.7698 | 0.0144 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.26 | 0.7712 | 0.0140 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.34 | 0.7733 | 0.0139 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.36 | 0.7747 | 0.0138 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.38 | 0.7750 | 0.0137 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 35.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.22 | 0.7272 | 0.0245 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.20 | 0.2991 | 0.3833 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.26 | 0.3091 | 0.3769 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.22 | 0.3080 | 0.3805 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.24 | 0.3083 | 0.3789 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.13 | 0.2857 | 0.3809 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.19 | 0.3093 | 0.3760 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.15 | 0.2961 | 0.3793 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.16 | 0.3005 | 0.3780 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.79 | 0.4682 | 0.1744 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.80 | 0.4610 | 0.1797 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.80 | 0.4610 | 0.1797 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.73 | 0.4540 | 0.1808 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.73 | 0.4540 | 0.1808 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.00 | 0.1936 | 0.2217 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.01 | 0.1878 | 0.2247 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.01 | 0.1878 | 0.2247 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.00 | 0.1824 | 0.2268 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.00 | 0.1824 | 0.2268 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.97 | 0.1797 | 0.2255 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.89 | 0.3547 | 0.3555 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.98 | 0.3690 | 0.3479 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.91 | 0.3674 | 0.3529 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.94 | 0.3687 | 0.3505 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.79 | 0.3322 | 0.3544 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.85 | 0.3552 | 0.3486 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.80 | 0.3451 | 0.3527 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.82 | 0.3494 | 0.3511 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.88 | 0.2416 | 0.2054 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.47 | 0.2645 | 0.3900 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.48 | 0.2700 | 0.3882 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.47 | 0.2683 | 0.3898 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.47 | 0.2695 | 0.3891 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.44 | 0.2652 | 0.3907 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.45 | 0.2663 | 0.3886 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.44 | 0.2667 | 0.3902 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.44 | 0.2661 | 0.3895 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.02 | 0.7255 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.89 | 0.7250 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.88 | 0.7254 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.85 | 0.7251 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.31 | 0.7195 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.00 | 0.7256 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.57 | 0.7218 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.75 | 0.7232 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.37 | 0.7293 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.25 | 0.7283 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.20 | 0.7273 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.22 | 0.7273 | 0.0263 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.21 | 0.7273 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.34 | 0.7289 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.23 | 0.7277 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.22 | 0.7274 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.17 | 0.7272 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.20 | 0.7271 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.17 | 0.7275 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.95 | 0.7259 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.06 | 0.7291 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.12 | 0.7284 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.06 | 0.7289 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.64 | 0.7228 | 0.0254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.05 | 0.7277 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.93 | 0.7261 | 0.0253 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.00 | 0.7270 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.11 | 0.7267 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.25 | 0.7281 | 0.0240 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.36 | 0.7298 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.30 | 0.7291 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.34 | 0.7295 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.28 | 0.7293 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.34 | 0.7303 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.29 | 0.7301 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.30 | 0.7302 | 0.0236 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.27 | 0.7176 | 0.0286 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.32 | 0.7189 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.28 | 0.7194 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.23 | 0.7191 | 0.0278 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.31 | 0.7104 | 0.0278 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.43 | 0.7200 | 0.0264 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.70 | 0.7144 | 0.0274 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.98 | 0.7163 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.37 | 0.7293 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.14 | 0.7268 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.13 | 0.7265 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.09 | 0.7250 | 0.0278 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.16 | 0.7264 | 0.0256 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.28 | 0.7286 | 0.0249 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.07 | 0.7259 | 0.0261 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.15 | 0.7265 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.02 | 0.7249 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.12 | 0.7260 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.98 | 0.7248 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.32 | 0.7174 | 0.0297 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.55 | 0.7240 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.55 | 0.7227 | 0.0289 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.53 | 0.7238 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.41 | 0.7099 | 0.0286 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.51 | 0.7221 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.97 | 0.7172 | 0.0279 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.15 | 0.7195 | 0.0278 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.72 | 0.7206 | 0.0294 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.11 | 0.7251 | 0.0253 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.28 | 0.7282 | 0.0245 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.19 | 0.7271 | 0.0252 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.25 | 0.7280 | 0.0249 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.18 | 0.7279 | 0.0249 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.28 | 0.7297 | 0.0243 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.23 | 0.7297 | 0.0247 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.24 | 0.7297 | 0.0245 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.88 | 0.7252 | 0.0404 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.33 | 0.2610 | 0.4666 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.35 | 0.2644 | 0.4617 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.33 | 0.2643 | 0.4644 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.34 | 0.2645 | 0.4631 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.30 | 0.2582 | 0.4651 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.31 | 0.2613 | 0.4607 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.30 | 0.2607 | 0.4637 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.30 | 0.2609 | 0.4626 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.80 | 0.4339 | 0.3329 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 13.84 | 0.4329 | 0.3338 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 13.84 | 0.4329 | 0.3338 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 13.79 | 0.4326 | 0.3338 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 13.79 | 0.4326 | 0.3338 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.58 | 0.0795 | 0.3525 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.59 | 0.0795 | 0.3522 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.59 | 0.0795 | 0.3522 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.58 | 0.0790 | 0.3526 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.58 | 0.0790 | 0.3526 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.58 | 0.0771 | 0.3523 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.66 | 0.2911 | 0.4440 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 2.69 | 0.2946 | 0.4372 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 2.67 | 0.2956 | 0.4412 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 2.68 | 0.2954 | 0.4391 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 2.62 | 0.2848 | 0.4438 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 2.63 | 0.2877 | 0.4371 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.62 | 0.2880 | 0.4417 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 2.63 | 0.2878 | 0.4397 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.02 | 0.1200 | 0.3343 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.08 | 0.2472 | 0.4714 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.09 | 0.2482 | 0.4700 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.08 | 0.2482 | 0.4712 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.09 | 0.2482 | 0.4708 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.07 | 0.2477 | 0.4718 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.08 | 0.2478 | 0.4699 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.07 | 0.2482 | 0.4714 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.08 | 0.2479 | 0.4707 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.86 | 0.7250 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.86 | 0.7251 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.86 | 0.7250 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.86 | 0.7251 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.86 | 0.7250 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.87 | 0.7251 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.87 | 0.7251 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.86 | 0.7249 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.86 | 0.7250 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.86 | 0.7250 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.86 | 0.7250 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.87 | 0.7250 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.87 | 0.7251 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.87 | 0.7251 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.87 | 0.7251 | 0.0405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.70 | 0.7241 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.80 | 0.7247 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.79 | 0.7247 | 0.0415 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.80 | 0.7248 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.31 | 0.7229 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.81 | 0.7247 | 0.0409 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.61 | 0.7239 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.73 | 0.7243 | 0.0412 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.89 | 0.7255 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.88 | 0.7254 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.88 | 0.7253 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.88 | 0.7252 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.87 | 0.7254 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.85 | 0.7253 | 0.0405 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.87 | 0.7252 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.86 | 0.7252 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.87 | 0.7252 | 0.0404 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.85 | 0.7253 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.66 | 0.7237 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.65 | 0.7241 | 0.0416 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.70 | 0.7243 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.68 | 0.7242 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.53 | 0.7233 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.74 | 0.7244 | 0.0411 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.70 | 0.7243 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.74 | 0.7244 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.81 | 0.7250 | 0.0408 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.87 | 0.7251 | 0.0409 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.88 | 0.7254 | 0.0408 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.87 | 0.7253 | 0.0410 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.88 | 0.7254 | 0.0409 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.87 | 0.7253 | 0.0409 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7253 | 0.0406 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.88 | 0.7254 | 0.0408 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.88 | 0.7254 | 0.0407 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.76 | 0.7276 | 0.0522 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.59 | 0.2625 | 0.5226 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.62 | 0.2679 | 0.5134 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.60 | 0.2674 | 0.5192 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.61 | 0.2676 | 0.5167 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.55 | 0.2549 | 0.5140 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.57 | 0.2660 | 0.5098 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.55 | 0.2604 | 0.5129 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.56 | 0.2623 | 0.5119 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.95 | 0.4284 | 0.4195 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 13.98 | 0.4251 | 0.4237 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 13.98 | 0.4251 | 0.4237 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 13.92 | 0.4223 | 0.4254 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 13.92 | 0.4223 | 0.4254 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.70 | 0.1113 | 0.4319 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.70 | 0.1091 | 0.4342 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.70 | 0.1091 | 0.4342 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.70 | 0.1069 | 0.4365 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.70 | 0.1069 | 0.4365 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.69 | 0.1050 | 0.4354 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.99 | 0.3027 | 0.4927 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.04 | 0.3100 | 0.4790 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.00 | 0.3097 | 0.4879 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.02 | 0.3102 | 0.4834 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 2.94 | 0.2884 | 0.4845 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 2.96 | 0.2996 | 0.4774 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.94 | 0.2954 | 0.4828 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 2.95 | 0.2972 | 0.4810 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.22 | 0.1536 | 0.4049 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.18 | 0.2376 | 0.5289 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.18 | 0.2398 | 0.5260 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.18 | 0.2394 | 0.5286 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.18 | 0.2397 | 0.5276 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.16 | 0.2382 | 0.5287 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.17 | 0.2387 | 0.5259 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.16 | 0.2389 | 0.5280 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.17 | 0.2386 | 0.5271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.64 | 0.7268 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.57 | 0.7265 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.56 | 0.7267 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.55 | 0.7266 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.29 | 0.7245 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.64 | 0.7269 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.43 | 0.7254 | 0.0531 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.52 | 0.7260 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.82 | 0.7285 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.78 | 0.7281 | 0.0535 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.75 | 0.7277 | 0.0526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.76 | 0.7277 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.76 | 0.7277 | 0.0528 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.81 | 0.7283 | 0.0522 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.77 | 0.7279 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.76 | 0.7277 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.74 | 0.7276 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.75 | 0.7276 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.75 | 0.7278 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.61 | 0.7269 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.65 | 0.7281 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.68 | 0.7279 | 0.0531 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.65 | 0.7281 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.46 | 0.7257 | 0.0531 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.66 | 0.7276 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.59 | 0.7270 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.63 | 0.7273 | 0.0527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.71 | 0.7275 | 0.0545 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.77 | 0.7280 | 0.0516 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.81 | 0.7286 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.79 | 0.7283 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.80 | 0.7285 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.78 | 0.7284 | 0.0514 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.80 | 0.7288 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.78 | 0.7287 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.79 | 0.7287 | 0.0512 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.28 | 0.7235 | 0.0568 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.29 | 0.7242 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.28 | 0.7244 | 0.0562 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.26 | 0.7243 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.58 | 0.7199 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.38 | 0.7246 | 0.0541 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.91 | 0.7220 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.11 | 0.7230 | 0.0543 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.83 | 0.7285 | 0.0529 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.73 | 0.7276 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.73 | 0.7274 | 0.0534 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.71 | 0.7269 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.73 | 0.7273 | 0.0534 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.78 | 0.7282 | 0.0526 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.69 | 0.7271 | 0.0538 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.73 | 0.7274 | 0.0530 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.67 | 0.7268 | 0.0546 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.72 | 0.7272 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.65 | 0.7268 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.27 | 0.7232 | 0.0582 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.35 | 0.7257 | 0.0554 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.38 | 0.7254 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.36 | 0.7258 | 0.0562 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.69 | 0.7198 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.36 | 0.7250 | 0.0549 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.05 | 0.7230 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.17 | 0.7240 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.51 | 0.7251 | 0.0569 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.71 | 0.7269 | 0.0529 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.78 | 0.7280 | 0.0521 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.74 | 0.7276 | 0.0527 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.77 | 0.7279 | 0.0524 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.74 | 0.7279 | 0.0524 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.78 | 0.7285 | 0.0518 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.76 | 0.7285 | 0.0523 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.76 | 0.7285 | 0.0521 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1154 | None | classic | 1.99 | False | 274273 | 0.172 | 40.5 | 29.72 | 0.13 | 0.016 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1154 | None | classic | 1.99 | False | 274273 | 0.172 | 42.1 | 29.72 | 0.13 | 0.016 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1154 | None | classic | 1.99 | False | 274273 | 0.172 | 41.3 | 29.72 | 0.13 | 0.016 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1154 | None | classic | 1.99 | False | 274273 | 0.172 | 41.5 | 29.72 | 0.13 | 0.016 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 617 | None | classic | 0.57 | False | 513353 | 0.526 | 104.4 | 31.22 | 0.32 | 0.009 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 617 | None | classic | 0.57 | False | 513353 | 0.526 | 97.0 | 31.22 | 0.32 | 0.009 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 617 | None | classic | 0.57 | False | 513353 | 0.526 | 94.1 | 31.22 | 0.32 | 0.009 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 617 | None | classic | 0.57 | False | 513353 | 0.526 | 92.5 | 31.22 | 0.32 | 0.009 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 462093 | 0.273 | 17.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 461073 | 11.179 | 42.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 461073 | 11.179 | 42.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 461073 | 6.352 | 17.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 461073 | 6.352 | 17.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 462093 | 0.273 | 23.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 461073 | 11.179 | 66.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 461073 | 11.179 | 66.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 461073 | 6.352 | 23.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 461073 | 6.352 | 23.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 460163 | 11.179 | 145.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1083 | None | classic | 1.75 | False | 233847 | 0.169 | 44.3 | 30.12 | 0.17 | 0.017 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1083 | None | classic | 1.75 | False | 233847 | 0.169 | 36.5 | 30.12 | 0.17 | 0.017 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1083 | None | classic | 1.75 | False | 233847 | 0.169 | 40.4 | 30.12 | 0.17 | 0.017 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1083 | None | classic | 1.75 | False | 233847 | 0.169 | 36.2 | 30.12 | 0.17 | 0.017 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 614 | None | classic | 0.56 | False | 488182 | 0.528 | 102.9 | 31.68 | 0.38 | 0.017 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 614 | None | classic | 0.56 | False | 488182 | 0.528 | 101.4 | 31.68 | 0.38 | 0.017 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 614 | None | classic | 0.56 | False | 488182 | 0.528 | 107.2 | 31.68 | 0.38 | 0.017 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 614 | None | classic | 0.56 | False | 488182 | 0.528 | 115.6 | 31.68 | 0.38 | 0.017 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 661188 | 11.179 | 57.4 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 912 | None | classic | 1.24 | False | 165416 | 0.321 | 41.8 | 28.59 | 0.25 | 0.006 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 912 | None | classic | 1.24 | False | 165416 | 0.321 | 39.1 | 28.59 | 0.25 | 0.006 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 912 | None | classic | 1.24 | False | 165416 | 0.321 | 38.6 | 28.59 | 0.25 | 0.006 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 912 | None | classic | 1.24 | False | 165416 | 0.321 | 34.1 | 28.59 | 0.25 | 0.006 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 640 | None | classic | 0.61 | False | 334285 | 0.346 | 60.6 | 31.13 | 0.24 | 0.011 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 640 | None | classic | 0.61 | False | 334285 | 0.346 | 62.7 | 31.13 | 0.24 | 0.011 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 640 | None | classic | 0.61 | False | 334285 | 0.346 | 59.5 | 31.13 | 0.24 | 0.011 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 640 | None | classic | 0.61 | False | 334285 | 0.346 | 61.4 | 31.13 | 0.24 | 0.011 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.720 | 0.014 |
| in035 | mask_ent | 0.773 | 0.014 |
| in035 | mask_grad | 0.449 | 0.014 |
| in035 | r_col | 0.786 | 0.014 |
| in035 | r_warp | 0.826 | 0.014 |

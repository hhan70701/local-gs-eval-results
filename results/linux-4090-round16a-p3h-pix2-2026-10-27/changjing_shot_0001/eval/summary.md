# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 1.7% | 23.72 / 0.0455 | 23.15 / 0.0646 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 1.8% | 23.83 / 0.0461 | 24.39 / 0.0548 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 1.7% | 23.72 / 0.0448 | 24.37 / 0.0583 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 1.7% | 23.75 / 0.0454 | 24.54 / 0.0557 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 1.5% | 23.68 / 0.0384 | 20.51 / 0.0532 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 1.6% | 23.82 / 0.0349 | 19.38 / 0.0455 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 1.5% | 23.73 / 0.0342 | 19.68 / 0.0481 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 1.5% | 23.79 / 0.0345 | 19.34 / 0.0479 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 1.9% | 24.18 / 0.0456 | 26.82 / 0.0527 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 1.4% | 23.65 / 0.0455 | 24.92 / 0.0780 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 0.2% | 20.01 / 0.0294 | 22.69 / 0.0367 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 1.5% | 23.78 / 0.0469 | 24.34 / 0.0881 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 0.3% | 20.63 / 0.0408 | 22.12 / 0.0824 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 1.9% | 24.17 / 0.0487 | 24.19 / 0.0541 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 1.4% | 23.54 / 0.0465 | 22.90 / 0.0794 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 0.5% | 21.24 / 0.0409 | 20.87 / 0.0613 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 1.4% | 23.65 / 0.0465 | 22.92 / 0.0853 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 0.5% | 21.32 / 0.0442 | 21.60 / 0.0811 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 1.7% | 23.97 / 0.0322 | 21.89 / 0.0778 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 3.2% | 24.84 / 0.0044 | 21.81 / 0.0105 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.2% | 24.85 / 0.0048 | 21.97 / 0.0082 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.2% | 24.85 / 0.0047 | 21.83 / 0.0093 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.2% | 24.85 / 0.0049 | 21.55 / 0.0093 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 3.0% | 24.72 / 0.0046 | 21.61 / 0.0081 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.1% | 24.91 / 0.0047 | 21.70 / 0.0098 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.9% | 24.73 / 0.0047 | 21.83 / 0.0073 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.0% | 24.79 / 0.0048 | 21.85 / 0.0084 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 3.2% | 24.98 / 0.0054 | 21.81 / 0.0173 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 3.0% | 26.30 / 0.0232 | 21.96 / 0.0356 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 3.6% | 26.29 / 0.0258 | 22.57 / 0.0360 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 3.2% | 26.26 / 0.0255 | 22.68 / 0.0346 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 3.3% | 26.25 / 0.0243 | 22.76 / 0.0346 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 3.0% | 25.34 / 0.0233 | 21.94 / 0.0310 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 3.4% | 25.71 / 0.0249 | 20.67 / 0.0387 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 2.9% | 25.33 / 0.0229 | 21.23 / 0.0304 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 3.0% | 25.33 / 0.0232 | 21.19 / 0.0319 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 29.05 / 0.0551 | 38.12 / 0.0216 | 21.87 / 0.0079 | 29.88 / 0.0455 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.01 / 0.0579 | 38.12 / 0.0216 | 22.03 / 0.0088 | 29.86 / 0.0462 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.04 / 0.0558 | 38.12 / 0.0216 | 22.29 / 0.0078 | 29.84 / 0.0459 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.07 / 0.0567 | 38.12 / 0.0216 | 22.25 / 0.0082 | 29.87 / 0.0460 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.07 / 0.0561 | 38.12 / 0.0216 | 22.30 / 0.0079 | 29.86 / 0.0459 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.78 / 0.0578 | 38.12 / 0.0216 | 21.50 / 0.0095 | 29.85 / 0.0460 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.30 / 0.0578 | 38.12 / 0.0216 | 20.47 / 0.0107 | 29.74 / 0.0469 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.51 / 0.0580 | 38.12 / 0.0216 | 20.95 / 0.0105 | 29.80 / 0.0465 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.35 / 0.0578 | 38.12 / 0.0216 | 20.60 / 0.0108 | 29.77 / 0.0467 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.20 / 0.0551 | 38.12 / 0.0216 | 22.47 / 0.0077 | 29.89 / 0.0455 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.15 / 0.0561 | 38.12 / 0.0216 | 22.23 / 0.0086 | 29.89 / 0.0455 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.11 / 0.0554 | 38.12 / 0.0216 | 22.03 / 0.0083 | 29.88 / 0.0455 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.14 / 0.0567 | 38.12 / 0.0216 | 22.19 / 0.0092 | 29.89 / 0.0456 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.09 / 0.0558 | 38.12 / 0.0216 | 21.97 / 0.0088 | 29.88 / 0.0455 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.09 / 0.0556 | 38.12 / 0.0216 | 22.20 / 0.0082 | 29.88 / 0.0457 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.07 / 0.0567 | 38.12 / 0.0216 | 22.04 / 0.0089 | 29.88 / 0.0458 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.08 / 0.0559 | 38.12 / 0.0216 | 21.98 / 0.0086 | 29.88 / 0.0455 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.08 / 0.0574 | 38.12 / 0.0216 | 22.06 / 0.0093 | 29.88 / 0.0458 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.10 / 0.0557 | 38.12 / 0.0216 | 22.02 / 0.0087 | 29.88 / 0.0456 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.04 / 0.0578 | 38.12 / 0.0216 | 22.08 / 0.0096 | 29.88 / 0.0458 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.70 / 0.0598 | 38.12 / 0.0216 | 21.61 / 0.0095 | 29.71 / 0.0470 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.64 / 0.0579 | 38.12 / 0.0216 | 21.56 / 0.0088 | 29.70 / 0.0470 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.67 / 0.0589 | 38.12 / 0.0216 | 21.50 / 0.0094 | 29.76 / 0.0468 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.61 / 0.0583 | 38.12 / 0.0216 | 21.43 / 0.0092 | 29.73 / 0.0468 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.73 / 0.0578 | 38.12 / 0.0216 | 21.96 / 0.0083 | 29.72 / 0.0464 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.71 / 0.0564 | 38.12 / 0.0216 | 21.65 / 0.0087 | 29.77 / 0.0464 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.76 / 0.0576 | 38.12 / 0.0216 | 21.80 / 0.0084 | 29.77 / 0.0464 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.75 / 0.0571 | 38.12 / 0.0216 | 21.72 / 0.0086 | 29.78 / 0.0464 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.91 / 0.0594 | 38.12 / 0.0216 | 21.99 / 0.0103 | 29.87 / 0.0460 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 28.61 / 0.0622 | 38.12 / 0.0230 | 21.24 / 0.0093 | 29.83 / 0.0467 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.83 / 0.0588 | 38.03 / 0.0248 | 21.89 / 0.0079 | 29.84 / 0.0465 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.67 / 0.0610 | 38.08 / 0.0243 | 21.39 / 0.0089 | 29.84 / 0.0466 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.73 / 0.0599 | 38.02 / 0.0254 | 21.61 / 0.0085 | 29.84 / 0.0465 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.43 / 0.0619 | 37.75 / 0.0319 | 20.98 / 0.0099 | 29.79 / 0.0479 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.08 / 0.0629 | 37.82 / 0.0307 | 20.29 / 0.0111 | 29.78 / 0.0479 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.05 / 0.0621 | 37.83 / 0.0289 | 20.12 / 0.0108 | 29.75 / 0.0482 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.95 / 0.0627 | 37.78 / 0.0305 | 19.98 / 0.0113 | 29.75 / 0.0484 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.0%） | — | — | 29.05 / 0.0551 | 38.12 / 0.0216 | 29.88 |
| in035 | rife | 1.3% | 3.0% | 28.61 / 0.0622 | 38.12 / 0.0230 | 29.83 |
| in035 | cnw_cnn | 0.9% | 1.7% | 29.01 / 0.0579 | 38.12 / 0.0216 | 29.86 |
| in035 | cnw_f5 | 1.7% | 3.2% | 28.70 / 0.0598 | 38.12 / 0.0216 | 29.71 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 28.12 / 0.0561 | -0.42 / +0.0087 (core 1.5%) | +0.04 / +0.0042 (core 1.1%) | -0.33 / +0.0068 (core 2.2%) |
| in035 | 2 | 0-3 | 29.12 / 0.0551 | -0.86 / +0.0116 (core 1.5%) | -0.15 / +0.0038 (core 1.1%) | -0.54 / +0.0066 (core 2.2%) |
| in035 | 4 | 3-5 | 29.91 / 0.0540 | -0.05 / +0.0011 (core 0.5%) | -0.02 / +0.0004 (core 0.2%) | -0.18 / +0.0007 (core 0.3%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 29.05 / 0.0551 | 38.12 | 29.88 | — |
| in035 | cnw_cnn | 不复核 | —% | 29.01 / 0.0579 | 38.12 | 29.86 | 0/3 |
| in035 | cnw_cnn | oracle | 0.6% | 29.08 / 0.0562 | 38.12 | 29.87 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 29.04 / 0.0558 | 38.12 | 29.84 | 0/3 |
| in035 | cnw_cnn | oracle | 0.6% | 29.11 / 0.0551 | 38.12 | 29.87 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 29.07 / 0.0567 | 38.12 | 29.87 | 0/3 |
| in035 | cnw_cnn | oracle | 0.6% | 29.11 / 0.0556 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 29.07 / 0.0561 | 38.12 | 29.86 | 0/3 |
| in035 | cnw_cnn | oracle | 0.6% | 29.12 / 0.0553 | 38.12 | 29.87 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.78 / 0.0578 | 38.12 | 29.85 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.93 / 0.0564 | 38.12 | 29.87 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.30 / 0.0578 | 38.12 | 29.74 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.54 / 0.0565 | 38.12 | 29.84 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.51 / 0.0580 | 38.12 | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.72 / 0.0568 | 38.12 | 29.85 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.35 / 0.0578 | 38.12 | 29.77 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 0.5% | 28.59 / 0.0567 | 38.12 | 29.84 | 1/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 29.20 / 0.0551 | 38.12 | 29.89 | 1/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 0.5% | 29.19 / 0.0549 | 38.12 | 29.88 | 2/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 29.15 / 0.0561 | 38.12 | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 0.5% | 29.16 / 0.0557 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 29.11 / 0.0554 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 0.2% | 29.11 / 0.0554 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 29.14 / 0.0567 | 38.12 | 29.89 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 0.5% | 29.15 / 0.0562 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 29.09 / 0.0558 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 0.2% | 29.09 / 0.0558 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 29.09 / 0.0556 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 0.5% | 29.13 / 0.0552 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 29.07 / 0.0567 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 0.5% | 29.11 / 0.0558 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 29.08 / 0.0559 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.3% | 29.10 / 0.0556 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 29.08 / 0.0574 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 0.5% | 29.12 / 0.0561 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 29.10 / 0.0557 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 0.3% | 29.10 / 0.0556 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 29.04 / 0.0578 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 0.5% | 29.10 / 0.0564 | 38.12 | 29.88 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.70 / 0.0598 | 38.12 | 29.71 | 0/3 |
| in035 | cnw_f5 | oracle | 0.8% | 28.97 / 0.0568 | 38.12 | 29.86 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.64 / 0.0579 | 38.12 | 29.70 | 0/3 |
| in035 | cnw_f5 | oracle | 0.8% | 28.92 / 0.0555 | 38.12 | 29.86 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.67 / 0.0589 | 38.12 | 29.76 | 0/3 |
| in035 | cnw_f5 | oracle | 0.8% | 28.91 / 0.0567 | 38.12 | 29.86 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.61 / 0.0583 | 38.12 | 29.73 | 0/3 |
| in035 | cnw_f5 | oracle | 0.8% | 28.89 / 0.0561 | 38.12 | 29.85 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.73 / 0.0578 | 38.12 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.8% | 29.04 / 0.0558 | 38.12 | 29.87 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.71 / 0.0564 | 38.12 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.8% | 28.93 / 0.0555 | 38.12 | 29.87 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.76 / 0.0576 | 38.12 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.8% | 29.01 / 0.0559 | 38.12 | 29.87 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.75 / 0.0571 | 38.12 | 29.78 | 0/3 |
| in035 | cnw_f5_mw | oracle | 0.8% | 28.97 / 0.0558 | 38.12 | 29.87 | 1/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 28.91 / 0.0594 | 38.12 | 29.87 | 0/3 |
| in035 | cnw_f5_pix | oracle | 0.8% | 29.07 / 0.0573 | 38.12 | 29.88 | 0/3 |
| in035 | rife | 不复核 | —% | 28.61 / 0.0622 | 38.12 | 29.83 | 0/3 |
| in035 | rife | oracle | 0.5% | 28.82 / 0.0572 | 38.12 | 29.87 | 0/3 |
| in035 | rife | 不复核 | —% | 28.83 / 0.0588 | 38.03 | 29.84 | 0/3 |
| in035 | rife | oracle | 0.7% | 28.98 / 0.0554 | 38.12 | 29.87 | 1/3 |
| in035 | rife | 不复核 | —% | 28.67 / 0.0610 | 38.08 | 29.84 | 0/3 |
| in035 | rife | oracle | 0.6% | 28.85 / 0.0565 | 38.12 | 29.87 | 1/3 |
| in035 | rife | 不复核 | —% | 28.73 / 0.0599 | 38.02 | 29.84 | 0/3 |
| in035 | rife | oracle | 0.6% | 28.90 / 0.0560 | 38.12 | 29.87 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 28.43 / 0.0619 | 37.75 | 29.79 | 1/3 |
| in035 | rife_mw | oracle | 0.7% | 28.70 / 0.0572 | 38.12 | 29.87 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 28.08 / 0.0629 | 37.82 | 29.78 | 1/3 |
| in035 | rife_mw | oracle | 0.7% | 28.39 / 0.0581 | 38.12 | 29.86 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 28.05 / 0.0621 | 37.83 | 29.75 | 1/3 |
| in035 | rife_mw | oracle | 0.7% | 28.35 / 0.0576 | 38.12 | 29.84 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 27.95 / 0.0627 | 37.78 | 29.75 | 1/3 |
| in035 | rife_mw | oracle | 0.7% | 28.26 / 0.0582 | 38.12 | 29.84 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 29.05 / 0.0551 | 38.12 / 0.0216 | — |
| in035 | FF | 0（前馈） | 903×647（63%） | 27.24 | 29.01 / 0.0579 | 38.12 / 0.0216 | 0/3 |
| in035 | 25 | 0.43 s | 903×647（63%） | 27.59 | 29.07 / 0.0567 | 38.12 / 0.0216 | 0/3 |
| in035 | 50 | 0.84 s | 903×647（63%） | 27.73 | 29.07 / 0.0561 | 38.12 / 0.0216 | 0/3 |
| in035 | 100 | 1.64 s | 903×647（63%） | 27.85 | 29.04 / 0.0558 | 38.12 / 0.0216 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 29.05 / 0.0551 | 38.12 / 0.0216 | 29.88 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 29.01 / 0.0579 | 38.12 / 0.0216 | 29.86 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 29.08 / 0.0562 | 38.12 / 0.0216 | 29.87 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 29.07 / 0.0567 | 38.12 / 0.0216 | 29.87 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 29.11 / 0.0556 | 38.12 / 0.0216 | 29.88 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 29.07 / 0.0561 | 38.12 / 0.0216 | 29.86 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 29.12 / 0.0553 | 38.12 / 0.0216 | 29.87 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 29.04 / 0.0558 | 38.12 / 0.0216 | 29.84 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 29.11 / 0.0551 | 38.12 / 0.0216 | 29.87 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 28.78 / 0.0578 | 38.12 / 0.0216 | 29.85 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.93 / 0.0564 | 38.12 / 0.0216 | 29.87 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.51 / 0.0580 | 38.12 / 0.0216 | 29.80 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.72 / 0.0568 | 38.12 / 0.0216 | 29.85 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.35 / 0.0578 | 38.12 / 0.0216 | 29.77 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.59 / 0.0567 | 38.12 / 0.0216 | 29.84 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.30 / 0.0578 | 38.12 / 0.0216 | 29.74 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.54 / 0.0565 | 38.12 / 0.0216 | 29.84 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 28.70 / 0.0598 | 38.12 / 0.0216 | 29.71 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 28.97 / 0.0568 | 38.12 / 0.0216 | 29.86 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 28.67 / 0.0589 | 38.12 / 0.0216 | 29.76 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 28.91 / 0.0567 | 38.12 / 0.0216 | 29.86 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 28.61 / 0.0583 | 38.12 / 0.0216 | 29.73 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.89 / 0.0561 | 38.12 / 0.0216 | 29.85 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 28.64 / 0.0579 | 38.12 / 0.0216 | 29.70 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.92 / 0.0555 | 38.12 / 0.0216 | 29.86 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 28.73 / 0.0578 | 38.12 / 0.0216 | 29.72 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 29.04 / 0.0558 | 38.12 / 0.0216 | 29.87 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 28.76 / 0.0576 | 38.12 / 0.0216 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 29.01 / 0.0559 | 38.12 / 0.0216 | 29.87 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 28.75 / 0.0571 | 38.12 / 0.0216 | 29.78 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.97 / 0.0558 | 38.12 / 0.0216 | 29.87 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.71 / 0.0564 | 38.12 / 0.0216 | 29.77 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.93 / 0.0555 | 38.12 / 0.0216 | 29.87 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 28.61 / 0.0622 | 38.12 / 0.0230 | 29.83 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.82 / 0.0572 | 38.12 / 0.0216 | 29.87 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.67 / 0.0610 | 38.08 / 0.0243 | 29.84 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.85 / 0.0565 | 38.12 / 0.0216 | 29.87 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.73 / 0.0599 | 38.02 / 0.0254 | 29.84 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.90 / 0.0560 | 38.12 / 0.0216 | 29.87 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.83 / 0.0588 | 38.03 / 0.0248 | 29.84 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.98 / 0.0554 | 38.12 / 0.0216 | 29.87 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 28.43 / 0.0619 | 37.75 / 0.0319 | 29.79 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.70 / 0.0572 | 38.12 / 0.0216 | 29.87 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.05 / 0.0621 | 37.83 / 0.0289 | 29.75 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.35 / 0.0576 | 38.12 / 0.0216 | 29.84 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.95 / 0.0627 | 37.78 / 0.0305 | 29.75 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.26 / 0.0582 | 38.12 / 0.0216 | 29.84 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.08 / 0.0629 | 37.82 / 0.0307 | 29.78 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.39 / 0.0581 | 38.12 / 0.0216 | 29.86 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 38.12 / 0.0216 | 21.87 / 0.0079 | 29.88 / 0.0455 | 29.05 / 0.0551 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 3.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 38.12 | 0.9320 | 0.0216 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 12.11 | 0.5444 | 0.5575 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 12.10 | 0.5437 | 0.5568 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 12.10 | 0.5437 | 0.5568 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 12.12 | 0.5452 | 0.5573 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 12.12 | 0.5452 | 0.5573 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 7.75 | 0.0006 | 0.6242 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 7.75 | 0.0006 | 0.6242 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 7.75 | 0.0006 | 0.6242 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 7.75 | 0.0006 | 0.6242 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 7.75 | 0.0006 | 0.6242 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 7.75 | 0.0006 | 0.6242 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.32 | 0.5547 | 0.7123 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 7.75 | 0.0006 | 0.6242 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.68 | 0.6191 | 0.5435 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.76 | 0.6231 | 0.5271 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.71 | 0.6242 | 0.5407 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.74 | 0.6242 | 0.5352 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.65 | 0.6292 | 0.5380 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.72 | 0.6245 | 0.5328 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.66 | 0.6294 | 0.5402 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.68 | 0.6273 | 0.5364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 38.12 | 0.9320 | 0.0216 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 38.12 | 0.9323 | 0.0230 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 38.03 | 0.9312 | 0.0248 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 38.08 | 0.9319 | 0.0243 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 38.02 | 0.9312 | 0.0254 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 37.75 | 0.9303 | 0.0319 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 37.82 | 0.9296 | 0.0307 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 37.83 | 0.9304 | 0.0289 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 37.78 | 0.9297 | 0.0305 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 21.87 | 0.7537 | 0.0079 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.86 | 0.2814 | 0.1117 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.92 | 0.3091 | 0.1095 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.88 | 0.3033 | 0.1108 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.90 | 0.3077 | 0.1102 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.84 | 0.2570 | 0.1126 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.79 | 0.2260 | 0.1135 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.81 | 0.2399 | 0.1139 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.79 | 0.2293 | 0.1140 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 12.27 | 0.3125 | 0.0540 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 12.21 | 0.3057 | 0.0563 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 12.21 | 0.3057 | 0.0563 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 12.19 | 0.2947 | 0.0576 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 12.19 | 0.2947 | 0.0576 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 10.37 | 0.2444 | 0.0669 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.39 | 0.2389 | 0.0686 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.39 | 0.2389 | 0.0686 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 10.38 | 0.2306 | 0.0694 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 10.38 | 0.2306 | 0.0694 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.36 | 0.2264 | 0.0698 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.47 | 0.3103 | 0.1022 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.50 | 0.3298 | 0.1003 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.48 | 0.3229 | 0.1015 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.48 | 0.3240 | 0.1010 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.51 | 0.3387 | 0.1012 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.51 | 0.3422 | 0.1000 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.50 | 0.3402 | 0.1010 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.50 | 0.3403 | 0.1006 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.02 | 0.2943 | 0.0643 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.31 | 0.2986 | 0.1066 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.36 | 0.3402 | 0.1033 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.34 | 0.3311 | 0.1052 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.35 | 0.3355 | 0.1042 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.26 | 0.2579 | 0.1084 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.17 | 0.2087 | 0.1081 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.17 | 0.2126 | 0.1090 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.15 | 0.2066 | 0.1089 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.02 | 0.7577 | 0.0088 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.28 | 0.7774 | 0.0078 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.22 | 0.7712 | 0.0082 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.30 | 0.7763 | 0.0079 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.49 | 0.7424 | 0.0095 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.48 | 0.7249 | 0.0106 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.94 | 0.7326 | 0.0105 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.60 | 0.7270 | 0.0107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.46 | 0.7709 | 0.0077 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 22.22 | 0.7637 | 0.0086 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 22.02 | 0.7567 | 0.0084 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 22.18 | 0.7608 | 0.0092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 21.97 | 0.7534 | 0.0088 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.19 | 0.7627 | 0.0082 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.04 | 0.7547 | 0.0089 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 21.97 | 0.7522 | 0.0086 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 22.06 | 0.7551 | 0.0093 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.02 | 0.7535 | 0.0087 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 22.07 | 0.7566 | 0.0096 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 21.62 | 0.7499 | 0.0095 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.57 | 0.7616 | 0.0087 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.51 | 0.7562 | 0.0093 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.45 | 0.7580 | 0.0091 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.96 | 0.7622 | 0.0083 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.65 | 0.7580 | 0.0087 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.81 | 0.7596 | 0.0084 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.72 | 0.7584 | 0.0085 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 21.99 | 0.7549 | 0.0102 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 21.25 | 0.7568 | 0.0093 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.89 | 0.7836 | 0.0079 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.40 | 0.7705 | 0.0089 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 21.62 | 0.7757 | 0.0084 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.00 | 0.7446 | 0.0098 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.34 | 0.7156 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.16 | 0.7154 | 0.0106 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.01 | 0.7087 | 0.0112 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.03 | 0.7573 | 0.0088 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.29 | 0.7772 | 0.0078 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.25 | 0.7717 | 0.0082 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.30 | 0.7759 | 0.0079 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.50 | 0.7426 | 0.0095 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.47 | 0.7246 | 0.0107 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.95 | 0.7326 | 0.0105 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.60 | 0.7268 | 0.0108 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 22.47 | 0.7704 | 0.0077 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 22.23 | 0.7637 | 0.0086 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 22.03 | 0.7568 | 0.0083 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 22.19 | 0.7605 | 0.0092 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 21.97 | 0.7532 | 0.0088 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 22.20 | 0.7621 | 0.0082 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.04 | 0.7545 | 0.0089 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 21.98 | 0.7523 | 0.0086 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 22.06 | 0.7545 | 0.0093 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 22.02 | 0.7532 | 0.0087 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.08 | 0.7558 | 0.0096 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 21.61 | 0.7485 | 0.0095 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.56 | 0.7604 | 0.0088 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.50 | 0.7548 | 0.0094 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.43 | 0.7566 | 0.0092 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.96 | 0.7612 | 0.0083 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.65 | 0.7572 | 0.0087 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.80 | 0.7589 | 0.0084 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.72 | 0.7577 | 0.0086 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 21.99 | 0.7532 | 0.0103 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.24 | 0.7546 | 0.0093 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.89 | 0.7824 | 0.0079 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.39 | 0.7691 | 0.0089 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 21.61 | 0.7743 | 0.0085 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.98 | 0.7426 | 0.0099 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.29 | 0.7125 | 0.0111 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.12 | 0.7131 | 0.0108 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.98 | 0.7061 | 0.0113 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 19.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.06 | 0.8101 | 0.0131 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.90 | 0.3687 | 0.2248 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.96 | 0.3762 | 0.2187 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.91 | 0.3782 | 0.2226 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.93 | 0.3781 | 0.2208 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.88 | 0.3554 | 0.2274 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.92 | 0.3477 | 0.2244 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.88 | 0.3537 | 0.2276 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.89 | 0.3500 | 0.2267 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.64 | 0.4104 | 0.1204 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 13.58 | 0.3975 | 0.1275 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 13.58 | 0.3975 | 0.1275 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 13.56 | 0.3893 | 0.1300 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 13.56 | 0.3893 | 0.1300 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.17 | 0.1919 | 0.1575 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.06 | 0.1670 | 0.1676 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.06 | 0.1670 | 0.1676 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.05 | 0.1612 | 0.1689 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.05 | 0.1612 | 0.1689 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.98 | 0.1390 | 0.1710 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.57 | 0.4054 | 0.2073 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.63 | 0.4099 | 0.2011 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.58 | 0.4143 | 0.2050 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.60 | 0.4123 | 0.2032 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.53 | 0.3981 | 0.2067 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.66 | 0.4100 | 0.2010 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.55 | 0.4071 | 0.2052 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.59 | 0.4084 | 0.2036 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.90 | 0.2099 | 0.1595 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.42 | 0.3902 | 0.2039 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.59 | 0.4006 | 0.1961 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.46 | 0.4037 | 0.2018 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.50 | 0.4030 | 0.1997 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.33 | 0.3750 | 0.2036 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.49 | 0.3443 | 0.1991 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.33 | 0.3607 | 0.2032 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.37 | 0.3530 | 0.2021 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.17 | 0.8119 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.30 | 0.8151 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.30 | 0.8145 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.32 | 0.8151 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.88 | 0.8083 | 0.0148 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.06 | 0.8031 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.44 | 0.8051 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.16 | 0.8035 | 0.0158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.49 | 0.8153 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.35 | 0.8139 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.23 | 0.8126 | 0.0138 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.28 | 0.8125 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.18 | 0.8114 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.29 | 0.8134 | 0.0134 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.20 | 0.8121 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.17 | 0.8119 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.20 | 0.8117 | 0.0143 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.19 | 0.8116 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.02 | 0.8085 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.84 | 0.8100 | 0.0150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.84 | 0.8125 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.80 | 0.8116 | 0.0146 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.74 | 0.8118 | 0.0142 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.06 | 0.8120 | 0.0140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.90 | 0.8104 | 0.0138 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.03 | 0.8118 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.95 | 0.8110 | 0.0138 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.80 | 0.8060 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.20 | 0.8061 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.73 | 0.8117 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.32 | 0.8093 | 0.0157 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.45 | 0.8096 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.08 | 0.8042 | 0.0164 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.41 | 0.7913 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.44 | 0.7981 | 0.0171 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.24 | 0.7950 | 0.0176 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.93 | 0.8078 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.06 | 0.8121 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.16 | 0.8127 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.16 | 0.8131 | 0.0144 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.37 | 0.7995 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.53 | 0.7946 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.88 | 0.7970 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.61 | 0.7954 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.48 | 0.8132 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.23 | 0.8109 | 0.0161 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.20 | 0.8119 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.10 | 0.8081 | 0.0164 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.09 | 0.8097 | 0.0147 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.12 | 0.8098 | 0.0141 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.95 | 0.8068 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.04 | 0.8094 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.93 | 0.8057 | 0.0170 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.07 | 0.8093 | 0.0151 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.78 | 0.7902 | 0.0229 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.17 | 0.7996 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.12 | 0.8042 | 0.0159 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.11 | 0.8042 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.99 | 0.8043 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.11 | 0.7988 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.60 | 0.7945 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.16 | 0.8012 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.93 | 0.7988 | 0.0165 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.93 | 0.7753 | 0.0267 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.21 | 0.7853 | 0.0234 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.16 | 0.7804 | 0.0273 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.43 | 0.7911 | 0.0227 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.34 | 0.7881 | 0.0238 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.18 | 0.7871 | 0.0216 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.79 | 0.7542 | 0.0307 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.69 | 0.7831 | 0.0225 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.44 | 0.7775 | 0.0241 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 32.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.65 | 0.7464 | 0.0226 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.62 | 0.2884 | 0.4067 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.64 | 0.2944 | 0.4026 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.62 | 0.2945 | 0.4050 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.63 | 0.2945 | 0.4037 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.61 | 0.2814 | 0.4090 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.60 | 0.2764 | 0.4076 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.60 | 0.2794 | 0.4094 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.60 | 0.2771 | 0.4088 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 15.06 | 0.4085 | 0.2014 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.05 | 0.4052 | 0.2041 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.05 | 0.4052 | 0.2041 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.05 | 0.4030 | 0.2060 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.05 | 0.4030 | 0.2060 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 12.32 | 0.1261 | 0.2497 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.33 | 0.1240 | 0.2523 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.33 | 0.1240 | 0.2523 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 12.32 | 0.1219 | 0.2536 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 12.32 | 0.1219 | 0.2536 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.30 | 0.1188 | 0.2540 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.17 | 0.3267 | 0.3903 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.19 | 0.3295 | 0.3857 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.18 | 0.3323 | 0.3888 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.18 | 0.3309 | 0.3873 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.19 | 0.3284 | 0.3891 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.19 | 0.3336 | 0.3848 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.19 | 0.3339 | 0.3877 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.19 | 0.3338 | 0.3863 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.92 | 0.1839 | 0.2393 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.34 | 0.3359 | 0.3861 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.38 | 0.3481 | 0.3789 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.36 | 0.3467 | 0.3840 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.36 | 0.3477 | 0.3816 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.33 | 0.3281 | 0.3874 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.33 | 0.3149 | 0.3840 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.32 | 0.3183 | 0.3872 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.32 | 0.3152 | 0.3862 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.72 | 0.7473 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.80 | 0.7491 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.81 | 0.7489 | 0.0228 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.82 | 0.7492 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.47 | 0.7448 | 0.0241 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.79 | 0.7413 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.11 | 0.7428 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.88 | 0.7417 | 0.0249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.97 | 0.7497 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.88 | 0.7490 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.78 | 0.7479 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.84 | 0.7485 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.75 | 0.7475 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.81 | 0.7484 | 0.0226 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.76 | 0.7479 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.73 | 0.7475 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.77 | 0.7478 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.75 | 0.7475 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.74 | 0.7476 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.50 | 0.7460 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.47 | 0.7470 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.48 | 0.7468 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.42 | 0.7467 | 0.0234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.67 | 0.7476 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.50 | 0.7466 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.64 | 0.7476 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.56 | 0.7471 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.64 | 0.7470 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.11 | 0.7468 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.54 | 0.7503 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.20 | 0.7487 | 0.0238 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.34 | 0.7494 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.91 | 0.7435 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.41 | 0.7378 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.34 | 0.7393 | 0.0252 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.19 | 0.7380 | 0.0256 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.55 | 0.7455 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.67 | 0.7481 | 0.0231 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.73 | 0.7482 | 0.0237 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.72 | 0.7484 | 0.0233 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.12 | 0.7413 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.38 | 0.7375 | 0.0261 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.71 | 0.7391 | 0.0264 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.48 | 0.7380 | 0.0263 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.98 | 0.7497 | 0.0226 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.87 | 0.7488 | 0.0236 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.78 | 0.7479 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.82 | 0.7481 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.74 | 0.7473 | 0.0234 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.72 | 0.7474 | 0.0231 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.67 | 0.7469 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.69 | 0.7470 | 0.0233 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.69 | 0.7468 | 0.0246 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.73 | 0.7473 | 0.0232 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.58 | 0.7460 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.90 | 0.7400 | 0.0265 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.89 | 0.7424 | 0.0249 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.96 | 0.7426 | 0.0260 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.87 | 0.7425 | 0.0256 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.06 | 0.7419 | 0.0249 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.03 | 0.7427 | 0.0240 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.10 | 0.7435 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.08 | 0.7432 | 0.0243 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.25 | 0.7432 | 0.0266 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.63 | 0.7398 | 0.0295 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.15 | 0.7438 | 0.0262 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.78 | 0.7430 | 0.0284 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.93 | 0.7435 | 0.0273 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.34 | 0.7359 | 0.0292 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.80 | 0.7288 | 0.0301 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.76 | 0.7317 | 0.0297 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.60 | 0.7299 | 0.0300 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 86.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.88 | 0.7265 | 0.0455 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.12 | 0.2521 | 0.5231 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.13 | 0.2526 | 0.5203 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.12 | 0.2537 | 0.5223 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.12 | 0.2532 | 0.5214 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.10 | 0.2499 | 0.5230 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.10 | 0.2480 | 0.5231 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.10 | 0.2499 | 0.5235 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.10 | 0.2488 | 0.5236 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.21 | 0.3423 | 0.3798 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 13.20 | 0.3424 | 0.3799 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 13.20 | 0.3424 | 0.3799 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 13.21 | 0.3424 | 0.3804 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 13.21 | 0.3424 | 0.3804 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.45 | 0.0546 | 0.4026 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.46 | 0.0542 | 0.4033 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.46 | 0.0542 | 0.4033 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.46 | 0.0545 | 0.4034 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.46 | 0.0545 | 0.4034 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.45 | 0.0524 | 0.4030 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.35 | 0.2696 | 0.5107 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 2.37 | 0.2692 | 0.5066 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 2.36 | 0.2716 | 0.5092 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 2.36 | 0.2707 | 0.5080 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 2.36 | 0.2681 | 0.5085 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 2.36 | 0.2686 | 0.5056 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.36 | 0.2706 | 0.5075 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 2.36 | 0.2698 | 0.5067 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.62 | 0.0807 | 0.3915 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.34 | 0.2660 | 0.5002 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.36 | 0.2679 | 0.4957 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.34 | 0.2692 | 0.4985 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.35 | 0.2688 | 0.4971 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.33 | 0.2683 | 0.4995 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.34 | 0.2651 | 0.4977 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.33 | 0.2677 | 0.4995 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.33 | 0.2664 | 0.4987 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.87 | 0.7265 | 0.0456 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.87 | 0.7265 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.87 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.87 | 0.7264 | 0.0456 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.84 | 0.7262 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.85 | 0.7263 | 0.0459 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.84 | 0.7262 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.88 | 0.7265 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.88 | 0.7265 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.86 | 0.7264 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.86 | 0.7264 | 0.0458 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.86 | 0.7264 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.85 | 0.7264 | 0.0458 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.87 | 0.7265 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.87 | 0.7264 | 0.0458 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.87 | 0.7265 | 0.0456 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.87 | 0.7265 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.88 | 0.7266 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.87 | 0.7265 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.87 | 0.7265 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.87 | 0.7265 | 0.0456 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.87 | 0.7265 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.87 | 0.7264 | 0.0456 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.86 | 0.7263 | 0.0458 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.84 | 0.7263 | 0.0459 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.84 | 0.7263 | 0.0460 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.86 | 0.7267 | 0.0462 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.84 | 0.7266 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.87 | 0.7268 | 0.0460 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.86 | 0.7267 | 0.0459 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.85 | 0.7263 | 0.0460 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.74 | 0.7259 | 0.0469 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.80 | 0.7262 | 0.0465 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.77 | 0.7260 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.89 | 0.7268 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.89 | 0.7267 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.88 | 0.7265 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.89 | 0.7267 | 0.0456 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.88 | 0.7265 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.88 | 0.7267 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.88 | 0.7267 | 0.0458 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.88 | 0.7265 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.88 | 0.7267 | 0.0458 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.88 | 0.7265 | 0.0456 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.88 | 0.7267 | 0.0458 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.71 | 0.7258 | 0.0470 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.70 | 0.7259 | 0.0470 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.76 | 0.7262 | 0.0468 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.73 | 0.7261 | 0.0468 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.72 | 0.7259 | 0.0464 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7261 | 0.0464 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.77 | 0.7263 | 0.0464 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.78 | 0.7262 | 0.0464 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.87 | 0.7267 | 0.0460 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.83 | 0.7261 | 0.0467 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.84 | 0.7261 | 0.0465 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.84 | 0.7262 | 0.0466 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.84 | 0.7261 | 0.0465 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.79 | 0.7259 | 0.0479 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.78 | 0.7256 | 0.0479 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.75 | 0.7257 | 0.0482 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.75 | 0.7256 | 0.0484 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.05 | 0.7347 | 0.0551 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.30 | 0.2571 | 0.5732 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.31 | 0.2594 | 0.5660 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.30 | 0.2603 | 0.5707 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.31 | 0.2599 | 0.5685 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.29 | 0.2526 | 0.5725 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.28 | 0.2485 | 0.5688 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.28 | 0.2515 | 0.5720 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.28 | 0.2496 | 0.5709 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 13.22 | 0.3435 | 0.4669 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 13.21 | 0.3420 | 0.4707 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 13.21 | 0.3420 | 0.4707 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 13.22 | 0.3415 | 0.4728 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 13.22 | 0.3415 | 0.4728 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 11.44 | 0.0759 | 0.4849 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.45 | 0.0746 | 0.4876 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.45 | 0.0746 | 0.4876 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 11.45 | 0.0743 | 0.4892 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 11.45 | 0.0743 | 0.4892 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.44 | 0.0718 | 0.4896 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 2.58 | 0.2788 | 0.5550 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 2.59 | 0.2785 | 0.5461 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 2.58 | 0.2811 | 0.5521 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 2.58 | 0.2798 | 0.5492 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 2.58 | 0.2776 | 0.5505 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 2.59 | 0.2797 | 0.5437 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 2.58 | 0.2810 | 0.5491 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 2.58 | 0.2806 | 0.5466 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.69 | 0.1070 | 0.4698 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.54 | 0.2734 | 0.5478 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.56 | 0.2785 | 0.5370 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.54 | 0.2792 | 0.5441 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.55 | 0.2791 | 0.5403 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.53 | 0.2710 | 0.5455 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.53 | 0.2638 | 0.5397 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.52 | 0.2668 | 0.5443 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.52 | 0.2648 | 0.5425 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.08 | 0.7350 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.11 | 0.7357 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.11 | 0.7356 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.12 | 0.7357 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.93 | 0.7338 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.54 | 0.7322 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.72 | 0.7328 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.59 | 0.7324 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.19 | 0.7360 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.16 | 0.7358 | 0.0557 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.11 | 0.7353 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.15 | 0.7356 | 0.0562 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.09 | 0.7351 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.13 | 0.7355 | 0.0552 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.11 | 0.7354 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.10 | 0.7352 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.12 | 0.7353 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.10 | 0.7352 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.10 | 0.7352 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.97 | 0.7344 | 0.0568 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.92 | 0.7346 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.91 | 0.7345 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.89 | 0.7344 | 0.0561 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.04 | 0.7349 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.93 | 0.7344 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.01 | 0.7349 | 0.0559 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.97 | 0.7347 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.07 | 0.7351 | 0.0573 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.82 | 0.7347 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.98 | 0.7359 | 0.0554 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.85 | 0.7354 | 0.0565 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.90 | 0.7356 | 0.0560 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.70 | 0.7334 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.39 | 0.7311 | 0.0581 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.35 | 0.7316 | 0.0576 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.26 | 0.7311 | 0.0582 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.01 | 0.7345 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.04 | 0.7353 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.07 | 0.7355 | 0.0567 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.07 | 0.7355 | 0.0561 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.78 | 0.7325 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.30 | 0.7305 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.51 | 0.7314 | 0.0580 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.35 | 0.7308 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.20 | 0.7361 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.15 | 0.7358 | 0.0561 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.11 | 0.7353 | 0.0554 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.14 | 0.7356 | 0.0567 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.09 | 0.7351 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.09 | 0.7352 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.07 | 0.7351 | 0.0567 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.08 | 0.7350 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.08 | 0.7351 | 0.0574 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.10 | 0.7351 | 0.0557 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.04 | 0.7347 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.70 | 0.7324 | 0.0598 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.64 | 0.7329 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.67 | 0.7331 | 0.0589 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.61 | 0.7329 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.73 | 0.7327 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.71 | 0.7329 | 0.0564 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.76 | 0.7334 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.75 | 0.7332 | 0.0571 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.91 | 0.7338 | 0.0594 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.61 | 0.7324 | 0.0622 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.83 | 0.7337 | 0.0588 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.67 | 0.7334 | 0.0610 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.73 | 0.7336 | 0.0599 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.43 | 0.7307 | 0.0619 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.08 | 0.7278 | 0.0629 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.05 | 0.7288 | 0.0621 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.95 | 0.7281 | 0.0627 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 938 | None | classic | 1.32 | False | 177730 | 0.173 | 37.0 | 28.89 | 0.22 | 0.016 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 938 | None | classic | 1.32 | False | 177730 | 0.173 | 33.3 | 28.89 | 0.22 | 0.016 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 938 | None | classic | 1.32 | False | 177730 | 0.173 | 35.0 | 28.89 | 0.22 | 0.016 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 938 | None | classic | 1.32 | False | 177730 | 0.173 | 31.6 | 28.89 | 0.22 | 0.016 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 597 | None | classic | 0.53 | False | 472521 | 0.531 | 77.9 | 31.03 | 0.36 | 0.009 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 597 | None | classic | 0.53 | False | 472521 | 0.531 | 78.5 | 31.03 | 0.36 | 0.009 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 597 | None | classic | 0.53 | False | 472521 | 0.531 | 77.0 | 31.03 | 0.36 | 0.009 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 597 | None | classic | 0.53 | False | 472521 | 0.531 | 76.8 | 31.03 | 0.36 | 0.009 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 275165 | 0.169 | 15.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 275165 | 0.979 | 40.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 275165 | 0.979 | 40.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 275165 | 0.610 | 15.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 275165 | 0.610 | 15.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 275165 | 0.169 | 21.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 275165 | 0.979 | 63.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 275165 | 0.979 | 63.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 275165 | 0.610 | 21.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 275165 | 0.610 | 21.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 275165 | 0.979 | 142.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 955 | None | classic | 1.36 | False | 183254 | 0.177 | 40.9 | 28.43 | 0.15 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 955 | None | classic | 1.36 | False | 183254 | 0.177 | 37.3 | 28.43 | 0.15 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 955 | None | classic | 1.36 | False | 183254 | 0.177 | 34.8 | 28.43 | 0.15 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 955 | None | classic | 1.36 | False | 183254 | 0.177 | 35.3 | 28.43 | 0.15 | 0.011 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 600 | None | classic | 0.54 | False | 408371 | 0.533 | 79.7 | 31.39 | 0.28 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 600 | None | classic | 0.54 | False | 408371 | 0.533 | 77.3 | 31.39 | 0.28 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 600 | None | classic | 0.54 | False | 408371 | 0.533 | 76.8 | 31.39 | 0.28 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 600 | None | classic | 0.54 | False | 408371 | 0.533 | 79.5 | 31.39 | 0.28 | 0.005 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 431623 | 0.979 | 54.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 995 | None | classic | 1.48 | False | 192868 | 0.323 | 43.0 | 29.12 | 0.23 | 0.013 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 995 | None | classic | 1.48 | False | 192868 | 0.323 | 32.1 | 29.12 | 0.23 | 0.013 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 995 | None | classic | 1.48 | False | 192868 | 0.323 | 29.4 | 29.12 | 0.23 | 0.013 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 995 | None | classic | 1.48 | False | 192868 | 0.323 | 34.7 | 29.12 | 0.23 | 0.013 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 622 | None | classic | 0.58 | False | 402506 | 0.514 | 88.4 | 31.19 | 0.35 | 0.011 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 622 | None | classic | 0.58 | False | 402506 | 0.514 | 84.9 | 31.19 | 0.35 | 0.011 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 622 | None | classic | 0.58 | False | 402506 | 0.514 | 81.4 | 31.19 | 0.35 | 0.011 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 622 | None | classic | 0.58 | False | 402506 | 0.514 | 80.1 | 31.19 | 0.35 | 0.011 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.746 | 0.010 |
| in035 | mask_ent | 0.753 | 0.010 |
| in035 | mask_grad | 0.463 | 0.010 |
| in035 | r_col | 0.681 | 0.010 |
| in035 | r_warp | 0.872 | 0.010 |

# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 9.7% | 23.58 / 0.0193 | 22.24 / 0.0365 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.9% | 23.78 / 0.0194 | 24.02 / 0.0289 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.8% | 23.63 / 0.0195 | 23.37 / 0.0317 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.9% | 23.72 / 0.0195 | 23.76 / 0.0299 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.0% | 23.74 / 0.0200 | 23.61 / 0.0303 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.1% | 23.85 / 0.0201 | 23.87 / 0.0238 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.1% | 23.83 / 0.0202 | 23.98 / 0.0258 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 10.1% | 23.85 / 0.0201 | 24.00 / 0.0245 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 9.2% | 23.17 / 0.0208 | 21.36 / 0.0580 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 8.4% | 23.09 / 0.0192 | 24.12 / 0.0410 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 2.2% | 18.91 / 0.0177 | 20.44 / 0.0276 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 8.4% | 23.06 / 0.0199 | 23.26 / 0.0470 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 2.4% | 19.12 / 0.0191 | 19.84 / 0.0319 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 9.2% | 23.18 / 0.0213 | 21.77 / 0.0411 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 8.4% | 23.10 / 0.0193 | 23.58 / 0.0399 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.4% | 19.15 / 0.0180 | 20.28 / 0.0293 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 8.5% | 23.07 / 0.0203 | 22.75 / 0.0458 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 2.8% | 19.58 / 0.0135 | 19.61 / 0.0291 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 10.7% | 23.81 / 0.0209 | 22.65 / 0.0503 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 13.2% | 24.31 / 0.0220 | 21.86 / 0.0464 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 13.4% | 24.49 / 0.0222 | 23.04 / 0.0350 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 13.3% | 24.36 / 0.0220 | 22.78 / 0.0397 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 13.3% | 24.43 / 0.0221 | 22.97 / 0.0368 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 13.1% | 24.31 / 0.0218 | 22.45 / 0.0460 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 13.4% | 24.45 / 0.0220 | 23.89 / 0.0346 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 13.2% | 24.34 / 0.0220 | 23.24 / 0.0396 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 13.3% | 24.42 / 0.0219 | 23.52 / 0.0372 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 14.4% | 24.52 / 0.0228 | 23.01 / 0.0537 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 12.8% | 24.33 / 0.0319 | 23.45 / 0.0660 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 13.1% | 24.57 / 0.0316 | 24.32 / 0.0568 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 13.3% | 24.45 / 0.0323 | 24.15 / 0.0634 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 13.2% | 24.53 / 0.0325 | 24.25 / 0.0604 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 13.4% | 24.53 / 0.0316 | 24.22 / 0.0674 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 13.4% | 24.63 / 0.0318 | 24.32 / 0.0590 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 13.3% | 24.62 / 0.0312 | 24.73 / 0.0616 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 13.3% | 24.66 / 0.0310 | 24.82 / 0.0577 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.80 / 0.0722 | 30.17 / 0.0406 | 19.68 / 0.0231 | 29.42 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.37 / 0.0854 | 30.32 / 0.0608 | 20.03 / 0.0250 | 29.37 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.78 / 0.0796 | 30.28 / 0.0610 | 20.53 / 0.0226 | 29.41 / 0.0345 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.69 / 0.0821 | 30.69 / 0.0542 | 20.41 / 0.0231 | 29.41 / 0.0346 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.77 / 0.0807 | 30.73 / 0.0548 | 20.55 / 0.0225 | 29.42 / 0.0345 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.66 / 0.0803 | 30.60 / 0.0537 | 20.28 / 0.0204 | 29.37 / 0.0351 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.73 / 0.0760 | 31.41 / 0.0514 | 20.50 / 0.0199 | 29.35 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.76 / 0.0776 | 31.21 / 0.0461 | 20.38 / 0.0198 | 29.37 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.76 / 0.0766 | 31.30 / 0.0478 | 20.46 / 0.0195 | 29.36 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.35 / 0.0946 | 30.32 / 0.0997 | 19.34 / 0.0369 | 29.43 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.14 / 0.0836 | 31.38 / 0.0756 | 21.34 / 0.0267 | 29.39 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.07 / 0.0778 | 31.25 / 0.0630 | 21.06 / 0.0251 | 29.38 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.93 / 0.0872 | 31.20 / 0.0787 | 20.99 / 0.0290 | 29.38 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.95 / 0.0793 | 31.29 / 0.0709 | 20.83 / 0.0271 | 29.37 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.44 / 0.0839 | 30.90 / 0.0704 | 19.50 / 0.0303 | 29.42 / 0.0341 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.02 / 0.0826 | 31.17 / 0.0754 | 21.03 / 0.0259 | 29.39 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.02 / 0.0776 | 31.10 / 0.0674 | 20.87 / 0.0247 | 29.38 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.79 / 0.0868 | 30.77 / 0.0792 | 20.71 / 0.0291 | 29.38 / 0.0348 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.84 / 0.0810 | 30.68 / 0.0759 | 20.68 / 0.0271 | 29.37 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.81 / 0.0849 | 30.95 / 0.0662 | 20.65 / 0.0272 | 29.39 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.86 / 0.0960 | 30.35 / 0.0631 | 19.72 / 0.0257 | 29.18 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.30 / 0.0868 | 30.02 / 0.0598 | 20.36 / 0.0224 | 29.28 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.25 / 0.0905 | 30.31 / 0.0561 | 20.24 / 0.0232 | 29.28 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.29 / 0.0884 | 30.18 / 0.0555 | 20.36 / 0.0223 | 29.29 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.07 / 0.0948 | 30.53 / 0.0637 | 20.09 / 0.0243 | 29.23 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.60 / 0.0863 | 30.15 / 0.0605 | 20.75 / 0.0206 | 29.29 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.43 / 0.0899 | 30.72 / 0.0548 | 20.48 / 0.0221 | 29.29 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.49 / 0.0879 | 30.65 / 0.0553 | 20.61 / 0.0213 | 29.28 / 0.0357 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.68 / 0.0902 | 30.74 / 0.0697 | 20.80 / 0.0277 | 29.28 / 0.0369 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.38 / 0.0927 | 30.39 / 0.0750 | 20.50 / 0.0223 | 29.34 / 0.0369 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.50 / 0.0873 | 30.51 / 0.0626 | 20.89 / 0.0205 | 29.30 / 0.0368 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.54 / 0.0903 | 30.67 / 0.0626 | 20.78 / 0.0210 | 29.33 / 0.0371 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.50 / 0.0892 | 30.58 / 0.0620 | 20.78 / 0.0207 | 29.29 / 0.0371 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.52 / 0.0950 | 30.27 / 0.0781 | 21.15 / 0.0199 | 29.05 / 0.0403 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.56 / 0.0897 | 30.47 / 0.0671 | 21.53 / 0.0185 | 29.01 / 0.0398 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.63 / 0.0915 | 30.56 / 0.0664 | 21.38 / 0.0186 | 29.04 / 0.0403 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.62 / 0.0905 | 30.51 / 0.0661 | 21.51 / 0.0186 | 29.01 / 0.0399 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.2%） | — | — | 27.80 / 0.0722 | 30.17 / 0.0406 | 29.42 |
| in035 | rife | 7.6% | 12.8% | 27.38 / 0.0927 | 30.39 / 0.0750 | 29.34 |
| in035 | cnw_cnn | 7.5% | 9.7% | 27.37 / 0.0854 | 30.32 / 0.0608 | 29.37 |
| in035 | cnw_f5 | 10.6% | 13.2% | 26.86 / 0.0960 | 30.35 / 0.0631 | 29.18 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.85 / 0.0723 | -0.69 / +0.0246 (core 6.5%) | -0.19 / +0.0150 (core 7.4%) | -0.70 / +0.0242 (core 9.4%) |
| in035 | 2 | 0-3 | 27.88 / 0.0733 | -0.72 / +0.0210 (core 6.5%) | -0.71 / +0.0135 (core 7.4%) | -1.00 / +0.0221 (core 9.4%) |
| in035 | 4 | 3-5 | 28.67 / 0.0709 | +0.16 / +0.0161 (core 5.9%) | -0.39 / +0.0113 (core 4.8%) | -1.13 / +0.0253 (core 8.4%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.80 / 0.0722 | — | 29.42 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.37 / 0.0854 | — | 29.37 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 27.73 / 0.0760 | — | 29.42 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.78 / 0.0796 | — | 29.41 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 27.95 / 0.0731 | — | 29.42 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.69 / 0.0821 | — | 29.41 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 27.89 / 0.0744 | — | 29.42 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.77 / 0.0807 | — | 29.42 | 0/3 |
| in035 | cnw_cnn | oracle | 2.5% | 27.95 / 0.0736 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.66 / 0.0803 | — | 29.37 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.88 / 0.0722 | — | 29.41 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.73 / 0.0760 | — | 29.35 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 27.95 / 0.0704 | — | 29.40 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.76 / 0.0776 | — | 29.37 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.94 / 0.0710 | — | 29.41 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.76 / 0.0766 | — | 29.36 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.4% | 27.96 / 0.0705 | — | 29.41 | 3/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 27.35 / 0.0946 | — | 29.43 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 2.5% | 27.56 / 0.0860 | — | 29.42 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 28.14 / 0.0836 | — | 29.39 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 2.4% | 28.30 / 0.0767 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 28.07 / 0.0778 | — | 29.38 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 1.3% | 28.21 / 0.0744 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.93 / 0.0872 | — | 29.38 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 2.4% | 28.17 / 0.0783 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 27.95 / 0.0793 | — | 29.37 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 1.4% | 28.13 / 0.0758 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 27.44 / 0.0839 | — | 29.42 | 0/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 2.5% | 27.62 / 0.0786 | — | 29.42 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.02 / 0.0826 | — | 29.39 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.4% | 28.20 / 0.0756 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.02 / 0.0776 | — | 29.38 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.4% | 28.16 / 0.0741 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.79 / 0.0868 | — | 29.38 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 2.4% | 28.06 / 0.0781 | — | 29.42 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 27.84 / 0.0810 | — | 29.37 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 1.5% | 28.06 / 0.0762 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.81 / 0.0849 | — | 29.39 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 2.6% | 28.07 / 0.0764 | — | 29.42 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.86 / 0.0960 | — | 29.18 | 0/3 |
| in035 | cnw_f5 | oracle | 2.7% | 27.55 / 0.0773 | — | 29.40 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.30 / 0.0868 | — | 29.28 | 0/3 |
| in035 | cnw_f5 | oracle | 2.7% | 27.79 / 0.0736 | — | 29.41 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.25 / 0.0905 | — | 29.28 | 0/3 |
| in035 | cnw_f5 | oracle | 2.8% | 27.74 / 0.0750 | — | 29.41 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.29 / 0.0884 | — | 29.29 | 0/3 |
| in035 | cnw_f5 | oracle | 2.7% | 27.78 / 0.0741 | — | 29.41 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.07 / 0.0948 | — | 29.23 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 27.74 / 0.0766 | — | 29.41 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.60 / 0.0863 | — | 29.29 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 28.02 / 0.0727 | — | 29.41 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.43 / 0.0899 | — | 29.29 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 27.90 / 0.0746 | — | 29.41 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.49 / 0.0879 | — | 29.28 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.7% | 27.96 / 0.0736 | — | 29.41 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.68 / 0.0902 | — | 29.28 | 0/3 |
| in035 | cnw_f5_pix | oracle | 2.8% | 28.09 / 0.0774 | — | 29.42 | 0/3 |
| in035 | rife | 不复核 | —% | 27.38 / 0.0927 | — | 29.34 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.84 / 0.0733 | — | 29.41 | 1/3 |
| in035 | rife | 不复核 | —% | 27.50 / 0.0873 | — | 29.30 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.96 / 0.0709 | — | 29.42 | 2/3 |
| in035 | rife | 不复核 | —% | 27.54 / 0.0903 | — | 29.33 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.96 / 0.0723 | — | 29.41 | 1/3 |
| in035 | rife | 不复核 | —% | 27.50 / 0.0892 | — | 29.29 | 0/3 |
| in035 | rife | oracle | 2.3% | 27.94 / 0.0716 | — | 29.41 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 27.52 / 0.0950 | — | 29.05 | 0/3 |
| in035 | rife_mw | oracle | 2.2% | 28.15 / 0.0718 | — | 29.41 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 27.56 / 0.0897 | — | 29.01 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 28.25 / 0.0699 | — | 29.42 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 27.63 / 0.0915 | — | 29.04 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 28.22 / 0.0707 | — | 29.42 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 27.62 / 0.0905 | — | 29.01 | 0/3 |
| in035 | rife_mw | oracle | 2.3% | 28.24 / 0.0703 | — | 29.42 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.80 / 0.0722 | — / — | — |
| in035 | FF | 0（前馈） | 930×771（67%） | 28.49 | 27.37 / 0.0854 | — / — | 0/3 |
| in035 | 25 | 1.30 s | 930×771（67%） | 29.19 | 27.69 / 0.0821 | — / — | 0/3 |
| in035 | 50 | 2.58 s | 930×771（67%） | 29.46 | 27.77 / 0.0807 | — / — | 0/3 |
| in035 | 100 | 5.14 s | 930×771（67%） | 29.72 | 27.78 / 0.0796 | — / — | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.80 / 0.0722 | — / — | 29.42 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.37 / 0.0854 | — / — | 29.37 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.73 / 0.0760 | — / — | 29.42 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 27.69 / 0.0821 | — / — | 29.41 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.89 / 0.0744 | — / — | 29.42 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.77 / 0.0807 | — / — | 29.42 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.95 / 0.0736 | — / — | 29.42 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.78 / 0.0796 | — / — | 29.41 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.95 / 0.0731 | — / — | 29.42 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.66 / 0.0803 | — / — | 29.37 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.88 / 0.0722 | — / — | 29.41 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.76 / 0.0776 | — / — | 29.37 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.94 / 0.0710 | — / — | 29.41 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.76 / 0.0766 | — / — | 29.36 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.96 / 0.0705 | — / — | 29.41 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.73 / 0.0760 | — / — | 29.35 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.95 / 0.0704 | — / — | 29.40 | 3/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.86 / 0.0960 | — / — | 29.18 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.55 / 0.0773 | — / — | 29.40 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.25 / 0.0905 | — / — | 29.28 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.74 / 0.0750 | — / — | 29.41 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.29 / 0.0884 | — / — | 29.29 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.78 / 0.0741 | — / — | 29.41 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.30 / 0.0868 | — / — | 29.28 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.79 / 0.0736 | — / — | 29.41 | 1/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.07 / 0.0948 | — / — | 29.23 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.74 / 0.0766 | — / — | 29.41 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.43 / 0.0899 | — / — | 29.29 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.90 / 0.0746 | — / — | 29.41 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.49 / 0.0879 | — / — | 29.28 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.96 / 0.0736 | — / — | 29.41 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.60 / 0.0863 | — / — | 29.29 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.02 / 0.0727 | — / — | 29.41 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.38 / 0.0927 | — / — | 29.34 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.84 / 0.0733 | — / — | 29.41 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 27.54 / 0.0903 | — / — | 29.33 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.96 / 0.0723 | — / — | 29.41 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.50 / 0.0892 | — / — | 29.29 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.94 / 0.0716 | — / — | 29.41 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.50 / 0.0873 | — / — | 29.30 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.96 / 0.0709 | — / — | 29.42 | 2/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.52 / 0.0950 | — / — | 29.05 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.15 / 0.0718 | — / — | 29.41 | 2/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 27.63 / 0.0915 | — / — | 29.04 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.22 / 0.0707 | — / — | 29.42 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 27.62 / 0.0905 | — / — | 29.01 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.24 / 0.0703 | — / — | 29.42 | 2/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 27.56 / 0.0897 | — / — | 29.01 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.25 / 0.0699 | — / — | 29.42 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.17 / 0.0406 | 19.68 / 0.0231 | 29.42 / 0.0339 | 27.80 / 0.0722 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 2.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.17 | 0.8212 | 0.0406 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 13.95 | 0.6678 | 0.3574 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 13.60 | 0.6591 | 0.3476 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 14.23 | 0.6809 | 0.3395 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 14.10 | 0.6760 | 0.3379 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 13.44 | 0.6834 | 0.3472 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.37 | 0.6848 | 0.3310 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 13.61 | 0.6986 | 0.3312 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 13.49 | 0.6905 | 0.3326 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 25.81 | 0.8269 | 0.1858 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 26.86 | 0.8396 | 0.1704 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 26.86 | 0.8396 | 0.1704 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 26.56 | 0.8331 | 0.1808 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 26.56 | 0.8331 | 0.1808 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.99 | 0.5863 | 0.3253 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 16.11 | 0.5792 | 0.3336 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 16.11 | 0.5792 | 0.3336 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 16.00 | 0.5752 | 0.3321 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 16.00 | 0.5752 | 0.3321 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.62 | 0.5409 | 0.3254 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 15.38 | 0.6788 | 0.3178 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.76 | 0.6689 | 0.3040 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 15.46 | 0.6879 | 0.2997 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 15.29 | 0.6833 | 0.2965 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 15.18 | 0.6892 | 0.3180 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.47 | 0.6627 | 0.3086 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 15.43 | 0.6953 | 0.3037 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 15.18 | 0.6846 | 0.3020 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.92 | 0.5789 | 0.3002 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.39 | 0.6790 | 0.3497 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.53 | 0.6708 | 0.3350 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.66 | 0.6961 | 0.3341 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.65 | 0.6824 | 0.3350 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.15 | 0.6511 | 0.3568 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 12.70 | 0.6571 | 0.3373 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 12.66 | 0.6744 | 0.3380 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 12.78 | 0.6673 | 0.3374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 30.58 | 0.8454 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.44 | 0.8438 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.76 | 0.8493 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.83 | 0.8498 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.82 | 0.8508 | 0.0456 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.49 | 0.8600 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.24 | 0.8586 | 0.0427 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.33 | 0.8586 | 0.0434 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 30.87 | 0.8410 | 0.0825 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 31.47 | 0.8538 | 0.0690 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 31.27 | 0.8506 | 0.0615 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 31.48 | 0.8535 | 0.0700 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 31.30 | 0.8504 | 0.0697 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 31.21 | 0.8506 | 0.0557 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.31 | 0.8525 | 0.0682 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.14 | 0.8491 | 0.0656 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 31.33 | 0.8530 | 0.0675 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 31.16 | 0.8489 | 0.0677 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 31.06 | 0.8518 | 0.0609 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 30.47 | 0.8353 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.17 | 0.8291 | 0.0547 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.34 | 0.8334 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.25 | 0.8326 | 0.0519 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.75 | 0.8421 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.22 | 0.8309 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.76 | 0.8427 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.69 | 0.8402 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 31.08 | 0.8514 | 0.0614 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.91 | 0.8411 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.06 | 0.8497 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.12 | 0.8503 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.06 | 0.8496 | 0.0403 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 30.88 | 0.8388 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.15 | 0.8493 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.16 | 0.8495 | 0.0390 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.14 | 0.8497 | 0.0389 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 30.32 | 0.8367 | 0.0608 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.28 | 0.8365 | 0.0610 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.69 | 0.8470 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.73 | 0.8462 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.60 | 0.8446 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.41 | 0.8576 | 0.0514 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.21 | 0.8597 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.30 | 0.8583 | 0.0478 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 30.32 | 0.8274 | 0.0997 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 31.38 | 0.8493 | 0.0756 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 31.25 | 0.8506 | 0.0630 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 31.20 | 0.8433 | 0.0787 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 31.29 | 0.8499 | 0.0709 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 30.90 | 0.8411 | 0.0704 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.17 | 0.8476 | 0.0754 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.10 | 0.8478 | 0.0674 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 30.77 | 0.8419 | 0.0792 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 30.68 | 0.8396 | 0.0759 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 30.95 | 0.8506 | 0.0662 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 30.35 | 0.8299 | 0.0631 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.02 | 0.8242 | 0.0598 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.31 | 0.8339 | 0.0561 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.18 | 0.8308 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.53 | 0.8388 | 0.0637 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.15 | 0.8283 | 0.0605 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.72 | 0.8444 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.65 | 0.8404 | 0.0553 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.74 | 0.8497 | 0.0697 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.39 | 0.8237 | 0.0750 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 30.51 | 0.8358 | 0.0626 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 30.67 | 0.8413 | 0.0626 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 30.58 | 0.8389 | 0.0620 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 30.27 | 0.8179 | 0.0781 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.47 | 0.8293 | 0.0671 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.56 | 0.8347 | 0.0664 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.51 | 0.8325 | 0.0661 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.68 | 0.6246 | 0.0231 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.83 | 0.4041 | 0.1287 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.91 | 0.4358 | 0.1238 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.88 | 0.4351 | 0.1252 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.90 | 0.4423 | 0.1243 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.83 | 0.4224 | 0.1246 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.85 | 0.4219 | 0.1232 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.83 | 0.4231 | 0.1233 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.83 | 0.4212 | 0.1232 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 14.90 | 0.4175 | 0.0809 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 15.56 | 0.5025 | 0.0706 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 15.56 | 0.5025 | 0.0706 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 15.45 | 0.4804 | 0.0740 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 15.45 | 0.4804 | 0.0740 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.42 | 0.3750 | 0.0863 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.77 | 0.4400 | 0.0820 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.77 | 0.4400 | 0.0820 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 13.68 | 0.4178 | 0.0860 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 13.68 | 0.4178 | 0.0860 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.66 | 0.4080 | 0.0837 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.70 | 0.3917 | 0.1094 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.81 | 0.4250 | 0.1038 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.78 | 0.4214 | 0.1050 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.80 | 0.4284 | 0.1039 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.76 | 0.4238 | 0.1070 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.86 | 0.4458 | 0.1021 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.82 | 0.4474 | 0.1035 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.84 | 0.4486 | 0.1024 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.22 | 0.4419 | 0.0735 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.90 | 0.3628 | 0.1279 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.93 | 0.3732 | 0.1251 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.93 | 0.3813 | 0.1257 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.93 | 0.3768 | 0.1255 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.90 | 0.3832 | 0.1267 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.95 | 0.3998 | 0.1231 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.91 | 0.3988 | 0.1249 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.92 | 0.3993 | 0.1240 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.02 | 0.6555 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.52 | 0.6809 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.40 | 0.6775 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.54 | 0.6840 | 0.0224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.26 | 0.6736 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.49 | 0.6817 | 0.0199 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.36 | 0.6780 | 0.0199 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.45 | 0.6799 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.34 | 0.6168 | 0.0369 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.31 | 0.7009 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 21.03 | 0.6847 | 0.0251 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.97 | 0.6837 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.82 | 0.6721 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.50 | 0.6235 | 0.0303 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.00 | 0.6849 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.85 | 0.6751 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.68 | 0.6689 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.66 | 0.6659 | 0.0271 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.63 | 0.6650 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.72 | 0.6352 | 0.0256 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.36 | 0.6676 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.23 | 0.6581 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.35 | 0.6656 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.08 | 0.6574 | 0.0243 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.77 | 0.6865 | 0.0206 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.46 | 0.6771 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.61 | 0.6822 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.77 | 0.6725 | 0.0277 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.52 | 0.6789 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.91 | 0.6962 | 0.0203 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.81 | 0.6934 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.80 | 0.6944 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 21.17 | 0.7067 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.54 | 0.7243 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.40 | 0.7208 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.52 | 0.7242 | 0.0185 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.03 | 0.6548 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 20.53 | 0.6807 | 0.0226 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 20.41 | 0.6773 | 0.0231 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 20.55 | 0.6839 | 0.0225 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 20.28 | 0.6739 | 0.0204 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.50 | 0.6817 | 0.0199 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.38 | 0.6782 | 0.0198 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.46 | 0.6799 | 0.0195 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.34 | 0.6160 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.34 | 0.7012 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 21.06 | 0.6850 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.99 | 0.6834 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.83 | 0.6720 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.50 | 0.6225 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.03 | 0.6849 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.87 | 0.6755 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.71 | 0.6688 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.68 | 0.6661 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.65 | 0.6635 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.72 | 0.6338 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.36 | 0.6662 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.24 | 0.6569 | 0.0232 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.36 | 0.6644 | 0.0223 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 20.09 | 0.6564 | 0.0243 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.75 | 0.6853 | 0.0206 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.48 | 0.6767 | 0.0221 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.61 | 0.6815 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.80 | 0.6713 | 0.0277 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.50 | 0.6773 | 0.0223 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.89 | 0.6942 | 0.0205 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.78 | 0.6918 | 0.0210 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.78 | 0.6927 | 0.0207 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 21.15 | 0.7055 | 0.0199 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 21.53 | 0.7230 | 0.0185 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 21.38 | 0.7201 | 0.0186 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 21.51 | 0.7233 | 0.0186 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 45.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.83 | 0.7006 | 0.0432 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.97 | 0.4478 | 0.3167 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.04 | 0.4608 | 0.3048 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.99 | 0.4652 | 0.3104 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.00 | 0.4651 | 0.3071 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.97 | 0.4573 | 0.3084 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.01 | 0.4557 | 0.2991 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.98 | 0.4657 | 0.3033 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.99 | 0.4615 | 0.3009 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 19.32 | 0.5843 | 0.1909 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 19.52 | 0.6086 | 0.1818 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 19.52 | 0.6086 | 0.1818 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 19.45 | 0.5994 | 0.1877 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 19.45 | 0.5994 | 0.1877 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 15.31 | 0.3642 | 0.2210 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.46 | 0.3736 | 0.2257 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.46 | 0.3736 | 0.2257 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 15.40 | 0.3660 | 0.2291 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 15.40 | 0.3660 | 0.2291 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.19 | 0.3402 | 0.2334 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.98 | 0.5044 | 0.2873 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.11 | 0.5199 | 0.2675 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.04 | 0.5256 | 0.2772 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.07 | 0.5248 | 0.2721 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.98 | 0.5108 | 0.2845 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.11 | 0.5258 | 0.2666 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.05 | 0.5319 | 0.2754 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.07 | 0.5304 | 0.2708 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.62 | 0.4394 | 0.2084 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.90 | 0.4716 | 0.3139 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.96 | 0.4767 | 0.2999 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.92 | 0.4864 | 0.3077 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.93 | 0.4822 | 0.3037 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.95 | 0.4748 | 0.3111 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.06 | 0.4740 | 0.2971 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.97 | 0.4875 | 0.3051 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.00 | 0.4826 | 0.3013 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.79 | 0.7018 | 0.0472 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.18 | 0.7077 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.08 | 0.7071 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.17 | 0.7081 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.04 | 0.7063 | 0.0431 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.24 | 0.7083 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.19 | 0.7083 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.25 | 0.7085 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.38 | 0.6951 | 0.0586 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.73 | 0.7107 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.58 | 0.7081 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.49 | 0.7074 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.42 | 0.7059 | 0.0476 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.53 | 0.6979 | 0.0509 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.55 | 0.7082 | 0.0474 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.48 | 0.7067 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.29 | 0.7050 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.29 | 0.7046 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.22 | 0.7026 | 0.0487 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.53 | 0.6978 | 0.0488 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.99 | 0.7040 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.86 | 0.7028 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.94 | 0.7039 | 0.0455 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.79 | 0.7014 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.32 | 0.7079 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.08 | 0.7064 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.20 | 0.7074 | 0.0451 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.21 | 0.7022 | 0.0500 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.09 | 0.7067 | 0.0454 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.38 | 0.7109 | 0.0430 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.34 | 0.7107 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.33 | 0.7109 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.61 | 0.7119 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.82 | 0.7153 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.77 | 0.7153 | 0.0427 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.82 | 0.7156 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.14 | 0.6952 | 0.0564 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.89 | 0.7074 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.69 | 0.7071 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.83 | 0.7086 | 0.0516 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.68 | 0.7043 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.86 | 0.7066 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.88 | 0.7095 | 0.0485 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.90 | 0.7086 | 0.0473 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.88 | 0.6808 | 0.0708 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.37 | 0.7057 | 0.0586 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.33 | 0.7065 | 0.0497 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.96 | 0.6985 | 0.0638 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.10 | 0.7036 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.11 | 0.6898 | 0.0580 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.10 | 0.7021 | 0.0584 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.21 | 0.7045 | 0.0505 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.67 | 0.6958 | 0.0630 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.86 | 0.7004 | 0.0538 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.83 | 0.6852 | 0.0662 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.34 | 0.6843 | 0.0655 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.89 | 0.6965 | 0.0568 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.94 | 0.6978 | 0.0607 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.96 | 0.6986 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.61 | 0.6886 | 0.0649 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.41 | 0.7028 | 0.0557 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.10 | 0.7020 | 0.0604 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.22 | 0.7031 | 0.0577 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.44 | 0.6759 | 0.0741 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.30 | 0.6988 | 0.0641 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.71 | 0.7062 | 0.0588 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.66 | 0.7083 | 0.0619 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.67 | 0.7077 | 0.0604 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.73 | 0.7031 | 0.0644 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.72 | 0.7055 | 0.0608 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.97 | 0.7115 | 0.0615 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.00 | 0.7104 | 0.0604 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 41.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 | 0.6791 | 0.0408 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.65 | 0.4181 | 0.3889 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.71 | 0.4327 | 0.3781 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.67 | 0.4360 | 0.3830 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.68 | 0.4362 | 0.3805 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.69 | 0.4292 | 0.3812 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.72 | 0.4266 | 0.3746 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.70 | 0.4368 | 0.3774 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.70 | 0.4326 | 0.3759 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 20.46 | 0.5618 | 0.1647 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 20.63 | 0.5841 | 0.1575 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 20.63 | 0.5841 | 0.1575 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 20.56 | 0.5742 | 0.1611 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 20.56 | 0.5742 | 0.1611 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 16.45 | 0.3656 | 0.2282 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 16.65 | 0.3809 | 0.2279 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 16.65 | 0.3809 | 0.2279 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 16.58 | 0.3723 | 0.2312 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 16.58 | 0.3723 | 0.2312 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 16.50 | 0.3642 | 0.2296 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.97 | 0.4565 | 0.3506 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.03 | 0.4763 | 0.3365 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.01 | 0.4801 | 0.3425 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.02 | 0.4803 | 0.3390 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.97 | 0.4659 | 0.3489 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.04 | 0.4839 | 0.3356 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.01 | 0.4883 | 0.3414 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.02 | 0.4874 | 0.3383 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.56 | 0.4493 | 0.1971 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.99 | 0.4252 | 0.3790 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.04 | 0.4306 | 0.3696 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.01 | 0.4404 | 0.3735 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.02 | 0.4362 | 0.3716 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.95 | 0.4271 | 0.3808 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.03 | 0.4315 | 0.3714 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.97 | 0.4403 | 0.3762 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.99 | 0.4369 | 0.3737 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.52 | 0.6804 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.93 | 0.6862 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.81 | 0.6856 | 0.0422 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.91 | 0.6867 | 0.0414 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.81 | 0.6847 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.92 | 0.6862 | 0.0385 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.93 | 0.6867 | 0.0392 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.95 | 0.6867 | 0.0387 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.12 | 0.6735 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.48 | 0.6900 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.34 | 0.6870 | 0.0428 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.25 | 0.6863 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.18 | 0.6848 | 0.0442 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.23 | 0.6755 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.29 | 0.6872 | 0.0437 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.24 | 0.6857 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.03 | 0.6836 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.04 | 0.6833 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.02 | 0.6829 | 0.0442 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.22 | 0.6752 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.71 | 0.6816 | 0.0413 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.56 | 0.6802 | 0.0428 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.64 | 0.6814 | 0.0419 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.51 | 0.6796 | 0.0444 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.08 | 0.6866 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.81 | 0.6848 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.93 | 0.6858 | 0.0415 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.05 | 0.6830 | 0.0451 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.70 | 0.6825 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.97 | 0.6861 | 0.0392 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.94 | 0.6862 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.93 | 0.6863 | 0.0399 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.30 | 0.6897 | 0.0402 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.49 | 0.6926 | 0.0384 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.44 | 0.6929 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.48 | 0.6929 | 0.0388 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.93 | 0.6746 | 0.0528 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.64 | 0.6857 | 0.0471 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.44 | 0.6857 | 0.0496 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.58 | 0.6870 | 0.0482 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.43 | 0.6829 | 0.0480 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.54 | 0.6842 | 0.0439 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.61 | 0.6878 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.60 | 0.6867 | 0.0444 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.75 | 0.6638 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.20 | 0.6876 | 0.0516 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.11 | 0.6855 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.82 | 0.6806 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.89 | 0.6826 | 0.0476 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.91 | 0.6695 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.96 | 0.6847 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.01 | 0.6840 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.54 | 0.6783 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.66 | 0.6798 | 0.0491 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.54 | 0.6782 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.11 | 0.6617 | 0.0609 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.89 | 0.6742 | 0.0528 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.71 | 0.6746 | 0.0562 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.79 | 0.6756 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.39 | 0.6673 | 0.0600 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.35 | 0.6816 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.97 | 0.6808 | 0.0557 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.11 | 0.6817 | 0.0540 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.36 | 0.6754 | 0.0557 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.01 | 0.6758 | 0.0577 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.33 | 0.6806 | 0.0530 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.34 | 0.6845 | 0.0556 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.32 | 0.6828 | 0.0545 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.36 | 0.6800 | 0.0602 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.48 | 0.6833 | 0.0555 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.58 | 0.6881 | 0.0572 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.57 | 0.6865 | 0.0564 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 58.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.42 | 0.6770 | 0.0339 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.82 | 0.3005 | 0.3682 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.88 | 0.3049 | 0.3600 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.85 | 0.3076 | 0.3645 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.86 | 0.3067 | 0.3621 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 2.82 | 0.2982 | 0.3643 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.87 | 0.2987 | 0.3586 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 2.84 | 0.3040 | 0.3616 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 2.85 | 0.3018 | 0.3596 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 16.27 | 0.4817 | 0.1917 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 16.21 | 0.4779 | 0.1963 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 16.21 | 0.4779 | 0.1963 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 16.22 | 0.4772 | 0.1956 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 16.22 | 0.4772 | 0.1956 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 13.98 | 0.2036 | 0.2333 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.01 | 0.2035 | 0.2347 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.01 | 0.2035 | 0.2347 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.01 | 0.2029 | 0.2341 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.01 | 0.2029 | 0.2341 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.96 | 0.1963 | 0.2345 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.17 | 0.3229 | 0.3361 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.20 | 0.3294 | 0.3245 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.19 | 0.3325 | 0.3303 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.19 | 0.3317 | 0.3270 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.17 | 0.3235 | 0.3352 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.21 | 0.3303 | 0.3242 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.20 | 0.3332 | 0.3296 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.20 | 0.3324 | 0.3265 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.47 | 0.2413 | 0.2147 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.66 | 0.2913 | 0.3563 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.70 | 0.2944 | 0.3496 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.68 | 0.2981 | 0.3531 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.69 | 0.2967 | 0.3514 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.64 | 0.2882 | 0.3619 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.70 | 0.2915 | 0.3535 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.66 | 0.2948 | 0.3591 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.67 | 0.2936 | 0.3561 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.42 | 0.6769 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.42 | 0.6771 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.42 | 0.6771 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.42 | 0.6771 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.40 | 0.6769 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.41 | 0.6769 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.42 | 0.6772 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.42 | 0.6772 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.42 | 0.6770 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.42 | 0.6771 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.42 | 0.6770 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.42 | 0.6771 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.42 | 0.6771 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.42 | 0.6770 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.42 | 0.6771 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.42 | 0.6771 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.42 | 0.6772 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.40 | 0.6767 | 0.0341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.41 | 0.6769 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.41 | 0.6769 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.42 | 0.6772 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.42 | 0.6770 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.41 | 0.6770 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.42 | 0.6770 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.42 | 0.6770 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.42 | 0.6770 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.37 | 0.6768 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.41 | 0.6775 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.41 | 0.6776 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.42 | 0.6776 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.37 | 0.6769 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.35 | 0.6765 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.37 | 0.6770 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.36 | 0.6768 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.43 | 0.6775 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 29.39 | 0.6773 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 29.38 | 0.6768 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 29.38 | 0.6772 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.37 | 0.6768 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.42 | 0.6773 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.39 | 0.6772 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.38 | 0.6768 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 29.38 | 0.6771 | 0.0348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.37 | 0.6768 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.39 | 0.6773 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.18 | 0.6754 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.28 | 0.6761 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.28 | 0.6767 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.29 | 0.6767 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.23 | 0.6759 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.29 | 0.6766 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.29 | 0.6771 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.28 | 0.6769 | 0.0357 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.28 | 0.6769 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.34 | 0.6769 | 0.0369 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.30 | 0.6768 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.33 | 0.6775 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.29 | 0.6770 | 0.0371 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.05 | 0.6746 | 0.0403 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.01 | 0.6752 | 0.0398 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.04 | 0.6756 | 0.0403 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.01 | 0.6755 | 0.0399 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.80 | 0.6802 | 0.0722 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.47 | 0.3482 | 0.5032 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.52 | 0.3557 | 0.4856 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.49 | 0.3594 | 0.4944 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.50 | 0.3587 | 0.4894 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.47 | 0.3514 | 0.4926 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.51 | 0.3502 | 0.4803 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.49 | 0.3576 | 0.4850 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.50 | 0.3545 | 0.4818 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 17.45 | 0.5262 | 0.3571 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 17.45 | 0.5343 | 0.3505 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 17.45 | 0.5343 | 0.3505 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 17.44 | 0.5301 | 0.3543 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 17.44 | 0.5301 | 0.3543 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 14.67 | 0.2660 | 0.3887 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.78 | 0.2735 | 0.3882 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.78 | 0.2735 | 0.3882 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 14.76 | 0.2696 | 0.3916 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 14.76 | 0.2696 | 0.3916 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 14.68 | 0.2623 | 0.3888 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 4.21 | 0.3839 | 0.4777 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 4.24 | 0.3926 | 0.4524 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 4.23 | 0.3975 | 0.4645 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 4.23 | 0.3964 | 0.4576 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 4.21 | 0.3879 | 0.4747 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 4.25 | 0.3959 | 0.4522 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 4.23 | 0.4013 | 0.4628 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 4.24 | 0.3996 | 0.4569 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.33 | 0.3295 | 0.3596 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.56 | 0.3510 | 0.5051 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.59 | 0.3531 | 0.4875 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.58 | 0.3598 | 0.4960 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.58 | 0.3568 | 0.4917 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 3.57 | 0.3508 | 0.5029 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 3.63 | 0.3528 | 0.4856 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 3.59 | 0.3596 | 0.4942 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 3.60 | 0.3570 | 0.4893 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.73 | 0.6807 | 0.0760 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.95 | 0.6832 | 0.0731 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.89 | 0.6830 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.95 | 0.6835 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.88 | 0.6827 | 0.0722 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 | 0.6833 | 0.0704 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.94 | 0.6835 | 0.0710 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.96 | 0.6835 | 0.0705 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.56 | 0.6784 | 0.0860 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.30 | 0.6853 | 0.0767 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.21 | 0.6838 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.17 | 0.6838 | 0.0783 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.13 | 0.6829 | 0.0758 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.62 | 0.6792 | 0.0786 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.20 | 0.6841 | 0.0756 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.16 | 0.6833 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.06 | 0.6826 | 0.0781 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.06 | 0.6823 | 0.0762 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.07 | 0.6825 | 0.0764 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.55 | 0.6783 | 0.0773 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.79 | 0.6808 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.74 | 0.6804 | 0.0750 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.78 | 0.6809 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.74 | 0.6805 | 0.0766 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.02 | 0.6832 | 0.0727 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.90 | 0.6827 | 0.0746 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.96 | 0.6830 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.09 | 0.6827 | 0.0774 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.84 | 0.6816 | 0.0733 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.96 | 0.6833 | 0.0709 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.96 | 0.6832 | 0.0723 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.94 | 0.6833 | 0.0716 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.15 | 0.6846 | 0.0718 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.25 | 0.6860 | 0.0699 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.22 | 0.6860 | 0.0707 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.24 | 0.6861 | 0.0703 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.37 | 0.6781 | 0.0854 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.78 | 0.6831 | 0.0796 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.69 | 0.6832 | 0.0821 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.77 | 0.6838 | 0.0807 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.66 | 0.6819 | 0.0803 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.73 | 0.6824 | 0.0760 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.76 | 0.6841 | 0.0776 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.76 | 0.6835 | 0.0766 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.35 | 0.6747 | 0.0946 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.14 | 0.6844 | 0.0836 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.07 | 0.6831 | 0.0778 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.93 | 0.6815 | 0.0872 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.95 | 0.6818 | 0.0793 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.44 | 0.6769 | 0.0839 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.02 | 0.6832 | 0.0826 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.02 | 0.6825 | 0.0776 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.79 | 0.6805 | 0.0868 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.84 | 0.6806 | 0.0810 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.81 | 0.6810 | 0.0849 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.86 | 0.6728 | 0.0960 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.30 | 0.6775 | 0.0868 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.25 | 0.6785 | 0.0905 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.29 | 0.6787 | 0.0884 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.07 | 0.6757 | 0.0948 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.60 | 0.6810 | 0.0863 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.43 | 0.6815 | 0.0899 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.49 | 0.6816 | 0.0879 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.68 | 0.6802 | 0.0902 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.38 | 0.6783 | 0.0927 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.50 | 0.6803 | 0.0873 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.54 | 0.6821 | 0.0903 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.50 | 0.6813 | 0.0892 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.52 | 0.6793 | 0.0950 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.56 | 0.6809 | 0.0897 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.63 | 0.6831 | 0.0915 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.62 | 0.6824 | 0.0905 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1131 | None | classic | 1.91 | False | 260354 | 0.326 | 62.2 | 30.61 | 0.07 | 0.017 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1131 | None | classic | 1.91 | False | 260354 | 0.326 | 73.9 | 30.61 | 0.07 | 0.017 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1131 | None | classic | 1.91 | False | 260354 | 0.326 | 50.9 | 30.61 | 0.07 | 0.017 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1131 | None | classic | 1.91 | False | 260354 | 0.326 | 52.6 | 30.61 | 0.07 | 0.017 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 777 | None | classic | 0.90 | False | 247355 | 0.665 | 112.5 | 29.29 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 777 | None | classic | 0.90 | False | 247355 | 0.665 | 107.0 | 29.29 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 777 | None | classic | 0.90 | False | 247355 | 0.665 | 115.4 | 29.29 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 777 | None | classic | 0.90 | False | 247355 | 0.665 | 122.3 | 29.29 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1105682 | 0.165 | 40.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1105406 | 0.794 | 44.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1105406 | 0.794 | 44.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1105406 | 0.574 | 39.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 1105406 | 0.574 | 39.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1105682 | 0.165 | 47.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1105406 | 0.794 | 188.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1105406 | 0.794 | 188.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1105406 | 0.574 | 47.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1105406 | 0.574 | 47.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1104688 | 0.794 | 447.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1223 | None | classic | 2.24 | False | 322023 | 0.328 | 61.6 | 30.98 | 0.12 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1223 | None | classic | 2.24 | False | 322023 | 0.328 | 64.7 | 30.98 | 0.12 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1223 | None | classic | 2.24 | False | 322023 | 0.328 | 49.9 | 30.98 | 0.12 | 0.011 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1223 | None | classic | 2.24 | False | 322023 | 0.328 | 51.1 | 30.98 | 0.12 | 0.011 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1191 | None | classic | 2.12 | False | 286046 | 0.327 | 55.4 | 30.67 | 0.06 | 0.031 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1191 | None | classic | 2.12 | False | 286046 | 0.327 | 54.2 | 30.67 | 0.06 | 0.031 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1191 | None | classic | 2.12 | False | 286046 | 0.327 | 56.9 | 30.67 | 0.06 | 0.031 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1191 | None | classic | 2.12 | False | 286046 | 0.327 | 74.3 | 30.67 | 0.06 | 0.031 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1534248 | 0.794 | 101.0 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1017 | None | classic | 1.55 | False | 188652 | 0.891 | 80.9 | 30.27 | 0.15 | 0.002 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1017 | None | classic | 1.55 | False | 188652 | 0.891 | 69.8 | 30.27 | 0.15 | 0.002 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1017 | None | classic | 1.55 | False | 188652 | 0.891 | 77.7 | 30.27 | 0.15 | 0.002 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1017 | None | classic | 1.55 | False | 188652 | 0.891 | 59.6 | 30.27 | 0.15 | 0.002 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 854 | None | classic | 1.09 | False | 336885 | 0.655 | 106.9 | 28.85 | 0.13 | 0.004 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 854 | None | classic | 1.09 | False | 336885 | 0.655 | 114.3 | 28.85 | 0.13 | 0.004 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 854 | None | classic | 1.09 | False | 336885 | 0.655 | 98.2 | 28.85 | 0.13 | 0.004 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 854 | None | classic | 1.09 | False | 336885 | 0.655 | 99.0 | 28.85 | 0.13 | 0.004 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.764 | 0.021 |
| in035 | mask_ent | 0.756 | 0.021 |
| in035 | mask_grad | 0.480 | 0.021 |
| in035 | r_col | 0.676 | 0.021 |
| in035 | r_warp | 0.880 | 0.021 |

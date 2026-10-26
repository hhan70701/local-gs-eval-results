# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 22.1% | 24.78 / 0.0361 | 25.16 / 0.0701 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 22.3% | 24.76 / 0.0358 | 27.33 / 0.0492 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 22.2% | 24.77 / 0.0360 | 26.80 / 0.0577 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 22.3% | 24.77 / 0.0357 | 27.05 / 0.0523 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 21.8% | 24.76 / 0.0358 | 24.76 / 0.0645 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 21.9% | 24.74 / 0.0353 | 26.18 / 0.0477 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 21.9% | 24.75 / 0.0348 | 25.91 / 0.0538 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 21.9% | 24.75 / 0.0353 | 26.10 / 0.0500 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 22.2% | 24.55 / 0.0349 | 21.92 / 0.0775 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 22.5% | 25.12 / 0.0282 | 24.44 / 0.0609 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 22.8% | 25.09 / 0.0293 | 26.75 / 0.0432 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 22.6% | 25.10 / 0.0283 | 26.18 / 0.0499 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 22.7% | 25.10 / 0.0288 | 26.43 / 0.0456 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 22.5% | 25.14 / 0.0287 | 24.23 / 0.0601 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 22.9% | 25.14 / 0.0292 | 26.15 / 0.0431 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 22.6% | 25.16 / 0.0288 | 25.62 / 0.0504 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 22.7% | 25.16 / 0.0291 | 25.91 / 0.0458 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 23.6% | 24.94 / 0.0286 | 21.77 / 0.0791 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 18.8% | 24.83 / 0.0275 | 20.50 / 0.0764 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 19.6% | 24.79 / 0.0283 | 22.13 / 0.0645 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 19.1% | 24.81 / 0.0279 | 21.49 / 0.0688 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 19.2% | 24.77 / 0.0281 | 21.81 / 0.0645 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 20.2% | 24.79 / 0.0291 | 21.85 / 0.0727 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 20.9% | 24.94 / 0.0302 | 22.58 / 0.0674 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 20.7% | 24.88 / 0.0299 | 22.38 / 0.0681 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 20.8% | 24.90 / 0.0301 | 22.46 / 0.0664 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.99 / 0.0657 | 28.76 / 0.0917 | 18.40 / 0.0218 | 30.12 / 0.0305 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.32 / 0.0897 | 29.96 / 0.1174 | 19.85 / 0.0227 | 30.09 / 0.0320 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.11 / 0.0776 | 30.66 / 0.1044 | 21.50 / 0.0183 | 30.10 / 0.0316 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.95 / 0.0833 | 30.44 / 0.1101 | 21.08 / 0.0207 | 30.10 / 0.0317 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.02 / 0.0800 | 30.61 / 0.1061 | 21.29 / 0.0195 | 30.10 / 0.0316 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.13 / 0.0861 | 29.79 / 0.1120 | 19.58 / 0.0227 | 30.09 / 0.0316 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.68 / 0.0757 | 30.22 / 0.1018 | 20.82 / 0.0195 | 30.08 / 0.0314 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.62 / 0.0797 | 30.04 / 0.1064 | 20.47 / 0.0210 | 30.08 / 0.0316 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.67 / 0.0773 | 30.18 / 0.1034 | 20.67 / 0.0202 | 30.08 / 0.0315 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.45 / 0.0896 | 29.46 / 0.1137 | 18.57 / 0.0285 | 29.93 / 0.0319 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.79 / 0.0931 | 28.36 / 0.1187 | 19.14 / 0.0252 | 29.97 / 0.0325 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.72 / 0.0802 | 29.34 / 0.1082 | 20.82 / 0.0195 | 29.99 / 0.0321 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.54 / 0.0856 | 29.01 / 0.1130 | 20.45 / 0.0221 | 30.02 / 0.0320 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.62 / 0.0823 | 29.24 / 0.1103 | 20.60 / 0.0208 | 30.01 / 0.0319 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.71 / 0.0939 | 28.14 / 0.1213 | 18.96 / 0.0262 | 30.00 / 0.0325 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.49 / 0.0807 | 29.01 / 0.1095 | 20.51 / 0.0204 | 30.04 / 0.0319 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.32 / 0.0865 | 28.71 / 0.1148 | 20.05 / 0.0230 | 30.04 / 0.0320 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.41 / 0.0829 | 28.91 / 0.1119 | 20.27 / 0.0218 | 30.04 / 0.0320 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.17 / 0.0978 | 27.31 / 0.1378 | 18.25 / 0.0327 | 29.96 / 0.0324 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 25.70 / 0.1074 | 28.74 / 0.1245 | 18.56 / 0.0293 | 29.99 / 0.0337 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.46 / 0.0943 | 28.82 / 0.1185 | 20.58 / 0.0217 | 29.82 / 0.0341 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.20 / 0.1013 | 28.78 / 0.1220 | 19.96 / 0.0248 | 29.86 / 0.0343 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.36 / 0.0971 | 28.79 / 0.1205 | 20.28 / 0.0231 | 29.81 / 0.0342 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.37 / 0.1015 | 28.55 / 0.1315 | 19.86 / 0.0262 | 30.06 / 0.0328 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.73 / 0.0931 | 28.41 / 0.1257 | 20.02 / 0.0241 | 30.05 / 0.0324 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.60 / 0.0976 | 28.54 / 0.1290 | 20.07 / 0.0252 | 30.08 / 0.0327 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.65 / 0.0951 | 28.50 / 0.1272 | 19.99 / 0.0247 | 30.06 / 0.0326 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.8%） | — | — | 27.99 / 0.0657 | 28.76 / 0.0917 | 30.12 |
| in035 | rife | 11.5% | 18.8% | 25.70 / 0.1074 | 28.74 / 0.1245 | 29.99 |
| in035 | cnw_cnn | 17.7% | 22.1% | 28.32 / 0.0897 | 29.96 / 0.1174 | 30.09 |
| in035 | cnw_f5 | 17.7% | 22.5% | 27.79 / 0.0931 | 28.36 / 0.1187 | 29.97 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.46 / 0.0702 | -6.24 / +0.0589 (core 11.1%) | +0.22 / +0.0243 (core 21.3%) | -0.37 / +0.0290 (core 21.7%) |
| in035 | 2 | 0-3 | 27.34 / 0.0684 | -0.22 / +0.0484 (core 11.1%) | +0.99 / +0.0339 (core 21.3%) | +0.24 / +0.0392 (core 21.7%) |
| in035 | 4 | 3-5 | 29.18 / 0.0583 | -0.40 / +0.0178 (core 7.4%) | -0.23 / +0.0139 (core 6.7%) | -0.47 / +0.0142 (core 6.8%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.99 / 0.0657 | 28.76 | 30.12 | — |
| in035 | cnw_cnn | 不复核 | —% | 28.32 / 0.0897 | 29.96 | 30.09 | 0/3 |
| in035 | cnw_cnn | oracle | 3.1% | 28.63 / 0.0690 | 30.30 | 30.12 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 29.11 / 0.0776 | 30.66 | 30.10 | 0/3 |
| in035 | cnw_cnn | oracle | 3.1% | 29.29 / 0.0641 | 30.78 | 30.12 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.95 / 0.0833 | 30.44 | 30.10 | 0/3 |
| in035 | cnw_cnn | oracle | 3.1% | 29.14 / 0.0668 | 30.53 | 30.12 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 29.02 / 0.0800 | 30.61 | 30.10 | 0/3 |
| in035 | cnw_cnn | oracle | 3.1% | 29.21 / 0.0654 | 30.71 | 30.12 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.13 / 0.0861 | 29.79 | 30.09 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.1% | 28.51 / 0.0674 | 30.05 | 30.12 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.68 / 0.0757 | 30.22 | 30.08 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.1% | 29.02 / 0.0638 | 30.40 | 30.12 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.62 / 0.0797 | 30.04 | 30.08 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.1% | 28.90 / 0.0655 | 30.20 | 30.12 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.67 / 0.0773 | 30.18 | 30.08 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.1% | 28.98 / 0.0647 | 30.34 | 30.12 | 2/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.45 / 0.0896 | 29.46 | 29.93 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 3.2% | 27.69 / 0.0737 | 30.27 | 30.12 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.79 / 0.0931 | 28.36 | 29.97 | 0/3 |
| in035 | cnw_f5 | oracle | 3.0% | 28.26 / 0.0709 | 29.00 | 30.12 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.72 / 0.0802 | 29.34 | 29.99 | 0/3 |
| in035 | cnw_f5 | oracle | 3.0% | 28.98 / 0.0654 | 29.55 | 30.11 | 2/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.54 / 0.0856 | 29.01 | 30.02 | 0/3 |
| in035 | cnw_f5 | oracle | 3.0% | 28.84 / 0.0685 | 29.30 | 30.12 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.62 / 0.0823 | 29.24 | 30.01 | 0/3 |
| in035 | cnw_f5 | oracle | 3.0% | 28.90 / 0.0668 | 29.45 | 30.11 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.71 / 0.0939 | 28.14 | 30.00 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.9% | 28.14 / 0.0713 | 28.83 | 30.12 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.49 / 0.0807 | 29.01 | 30.04 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.0% | 28.82 / 0.0658 | 29.29 | 30.12 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.32 / 0.0865 | 28.71 | 30.04 | 0/3 |
| in035 | cnw_f5_mw | oracle | 2.9% | 28.64 / 0.0688 | 29.07 | 30.12 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.41 / 0.0829 | 28.91 | 30.04 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.0% | 28.73 / 0.0674 | 29.19 | 30.12 | 0/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.17 / 0.0978 | 27.31 | 29.96 | 0/3 |
| in035 | cnw_f5_pix | oracle | 3.2% | 27.50 / 0.0773 | 28.84 | 30.13 | 0/3 |
| in035 | rife | 不复核 | —% | 25.70 / 0.1074 | 28.74 | 29.99 | 0/3 |
| in035 | rife | oracle | 2.8% | 28.00 / 0.0747 | 29.13 | 30.12 | 0/3 |
| in035 | rife | 不复核 | —% | 26.46 / 0.0943 | 28.82 | 29.82 | 0/3 |
| in035 | rife | oracle | 2.9% | 28.91 / 0.0674 | 29.24 | 30.12 | 1/3 |
| in035 | rife | 不复核 | —% | 26.20 / 0.1013 | 28.78 | 29.86 | 0/3 |
| in035 | rife | oracle | 2.8% | 28.66 / 0.0711 | 29.13 | 30.12 | 0/3 |
| in035 | rife | 不复核 | —% | 26.36 / 0.0971 | 28.79 | 29.81 | 0/3 |
| in035 | rife | oracle | 2.9% | 28.80 / 0.0691 | 29.20 | 30.12 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.37 / 0.1015 | 28.55 | 30.06 | 0/3 |
| in035 | rife_mw | oracle | 3.0% | 28.55 / 0.0712 | 29.17 | 30.12 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.73 / 0.0931 | 28.41 | 30.05 | 0/3 |
| in035 | rife_mw | oracle | 2.9% | 28.66 / 0.0688 | 28.99 | 30.11 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.60 / 0.0976 | 28.54 | 30.08 | 0/3 |
| in035 | rife_mw | oracle | 3.0% | 28.68 / 0.0702 | 29.09 | 30.12 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.65 / 0.0951 | 28.50 | 30.06 | 0/3 |
| in035 | rife_mw | oracle | 2.9% | 28.66 / 0.0696 | 29.07 | 30.11 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.99 / 0.0657 | 28.76 / 0.0917 | — |
| in035 | FF | 0（前馈） | 954×670（62%） | 29.83 | 28.32 / 0.0897 | 29.96 / 0.1174 | 0/3 |
| in035 | 25 | 0.70 s | 954×670（62%） | 30.57 | 28.95 / 0.0833 | 30.44 / 0.1101 | 0/3 |
| in035 | 50 | 1.38 s | 954×670（62%） | 30.86 | 29.02 / 0.0800 | 30.61 / 0.1061 | 0/3 |
| in035 | 100 | 2.74 s | 954×670（62%） | 31.12 | 29.11 / 0.0776 | 30.66 / 0.1044 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.99 / 0.0657 | 28.76 / 0.0917 | 30.12 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 28.32 / 0.0897 | 29.96 / 0.1174 | 30.09 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.63 / 0.0690 | 30.30 / 0.0911 | 30.12 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.95 / 0.0833 | 30.44 / 0.1101 | 30.10 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 29.14 / 0.0668 | 30.53 / 0.0880 | 30.12 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 29.02 / 0.0800 | 30.61 / 0.1061 | 30.10 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 29.21 / 0.0654 | 30.71 / 0.0863 | 30.12 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 29.11 / 0.0776 | 30.66 / 0.1044 | 30.10 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 29.29 / 0.0641 | 30.78 / 0.0849 | 30.12 | 2/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 28.13 / 0.0861 | 29.79 / 0.1120 | 30.09 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.51 / 0.0674 | 30.05 / 0.0898 | 30.12 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.62 / 0.0797 | 30.04 / 0.1064 | 30.08 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.90 / 0.0655 | 30.20 / 0.0878 | 30.12 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.67 / 0.0773 | 30.18 / 0.1034 | 30.08 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.98 / 0.0647 | 30.34 / 0.0868 | 30.12 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.68 / 0.0757 | 30.22 / 0.1018 | 30.08 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 29.02 / 0.0638 | 30.40 / 0.0864 | 30.12 | 3/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 27.79 / 0.0931 | 28.36 / 0.1187 | 29.97 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 28.26 / 0.0709 | 29.00 / 0.0956 | 30.12 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 28.54 / 0.0856 | 29.01 / 0.1130 | 30.02 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 28.84 / 0.0685 | 29.30 / 0.0939 | 30.12 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 28.62 / 0.0823 | 29.24 / 0.1103 | 30.01 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.90 / 0.0668 | 29.45 / 0.0921 | 30.11 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 28.72 / 0.0802 | 29.34 / 0.1082 | 29.99 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.98 / 0.0654 | 29.55 / 0.0908 | 30.11 | 2/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.71 / 0.0939 | 28.14 / 0.1213 | 30.00 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.14 / 0.0713 | 28.83 / 0.0958 | 30.12 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 28.32 / 0.0865 | 28.71 / 0.1148 | 30.04 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.64 / 0.0688 | 29.07 / 0.0938 | 30.12 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 28.41 / 0.0829 | 28.91 / 0.1119 | 30.04 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.73 / 0.0674 | 29.19 / 0.0925 | 30.12 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.49 / 0.0807 | 29.01 / 0.1095 | 30.04 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.82 / 0.0658 | 29.29 / 0.0914 | 30.12 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 25.70 / 0.1074 | 28.74 / 0.1245 | 29.99 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.00 / 0.0747 | 29.13 / 0.0963 | 30.12 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 26.20 / 0.1013 | 28.78 / 0.1220 | 29.86 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 28.66 / 0.0711 | 29.13 / 0.0961 | 30.12 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 26.36 / 0.0971 | 28.79 / 0.1205 | 29.81 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.80 / 0.0691 | 29.20 / 0.0954 | 30.12 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.46 / 0.0943 | 28.82 / 0.1185 | 29.82 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.91 / 0.0674 | 29.24 / 0.0945 | 30.12 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.37 / 0.1015 | 28.55 / 0.1315 | 30.06 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 28.55 / 0.0712 | 29.17 / 0.0991 | 30.12 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 26.60 / 0.0976 | 28.54 / 0.1290 | 30.08 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 28.68 / 0.0702 | 29.09 / 0.0979 | 30.12 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 26.65 / 0.0951 | 28.50 / 0.1272 | 30.06 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 28.66 / 0.0696 | 29.07 / 0.0973 | 30.11 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 26.73 / 0.0931 | 28.41 / 0.1257 | 30.05 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 28.66 / 0.0688 | 28.99 / 0.0968 | 30.11 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.76 / 0.0917 | 18.40 / 0.0218 | 30.12 / 0.0305 | 27.99 / 0.0657 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 24.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.76 | 0.8280 | 0.0917 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.96 | 0.7146 | 0.4907 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.09 | 0.7200 | 0.4584 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.99 | 0.7207 | 0.4752 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.03 | 0.7212 | 0.4653 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.13 | 0.6264 | 0.4840 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.22 | 0.6376 | 0.4568 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.13 | 0.6317 | 0.4692 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.13 | 0.6348 | 0.4632 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.60 | 0.5229 | 0.4608 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.74 | 0.7016 | 0.5015 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 9.91 | 0.7075 | 0.4718 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 9.78 | 0.7078 | 0.4878 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 9.84 | 0.7083 | 0.4785 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.70 | 0.6955 | 0.5013 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 9.88 | 0.6993 | 0.4718 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 9.74 | 0.7007 | 0.4884 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 9.79 | 0.7004 | 0.4783 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.42 | 0.5083 | 0.4922 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.29 | 0.6716 | 0.5692 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.43 | 0.6794 | 0.5442 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.33 | 0.6773 | 0.5592 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.37 | 0.6784 | 0.5515 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.88 | 0.6003 | 0.5742 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.96 | 0.5976 | 0.5523 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.90 | 0.6025 | 0.5665 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.92 | 0.6006 | 0.5588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 30.30 | 0.8392 | 0.0911 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.78 | 0.8422 | 0.0849 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.53 | 0.8408 | 0.0880 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.71 | 0.8418 | 0.0863 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.05 | 0.8369 | 0.0898 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.40 | 0.8386 | 0.0864 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.20 | 0.8375 | 0.0878 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.34 | 0.8382 | 0.0868 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.27 | 0.8378 | 0.0954 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.00 | 0.8295 | 0.0956 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.55 | 0.8333 | 0.0908 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.30 | 0.8316 | 0.0939 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.45 | 0.8325 | 0.0921 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.83 | 0.8278 | 0.0958 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.29 | 0.8306 | 0.0914 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.07 | 0.8294 | 0.0938 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.19 | 0.8301 | 0.0925 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.84 | 0.8272 | 0.1069 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.13 | 0.8308 | 0.0963 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.24 | 0.8318 | 0.0945 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.13 | 0.8313 | 0.0961 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.20 | 0.8317 | 0.0954 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.17 | 0.8309 | 0.0991 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.99 | 0.8309 | 0.0968 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.09 | 0.8315 | 0.0979 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.07 | 0.8315 | 0.0973 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.96 | 0.8425 | 0.1174 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.66 | 0.8465 | 0.1044 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.44 | 0.8466 | 0.1101 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.61 | 0.8473 | 0.1061 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.79 | 0.8406 | 0.1120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.22 | 0.8418 | 0.1018 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.04 | 0.8424 | 0.1064 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.18 | 0.8426 | 0.1034 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.46 | 0.8361 | 0.1137 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.36 | 0.8309 | 0.1187 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.34 | 0.8361 | 0.1082 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.01 | 0.8355 | 0.1130 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.24 | 0.8364 | 0.1103 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.14 | 0.8273 | 0.1213 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.01 | 0.8317 | 0.1095 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.71 | 0.8316 | 0.1148 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.91 | 0.8321 | 0.1119 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.31 | 0.8222 | 0.1378 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.74 | 0.8283 | 0.1245 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.82 | 0.8313 | 0.1185 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.78 | 0.8304 | 0.1220 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.79 | 0.8310 | 0.1205 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.55 | 0.8283 | 0.1315 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.41 | 0.8274 | 0.1257 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.54 | 0.8297 | 0.1290 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.50 | 0.8290 | 0.1272 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.40 | 0.5665 | 0.0218 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.92 | 0.4791 | 0.0900 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.11 | 0.5358 | 0.0845 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.04 | 0.5186 | 0.0874 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.07 | 0.5261 | 0.0860 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.49 | 0.4527 | 0.0876 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.57 | 0.4983 | 0.0819 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.61 | 0.4785 | 0.0853 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.64 | 0.4865 | 0.0841 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 11.98 | 0.3992 | 0.0760 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 10.33 | 0.5127 | 0.0756 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.62 | 0.5827 | 0.0674 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 10.53 | 0.5671 | 0.0714 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.57 | 0.5740 | 0.0693 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 10.30 | 0.5054 | 0.0766 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.61 | 0.5720 | 0.0680 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 10.48 | 0.5523 | 0.0723 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.54 | 0.5619 | 0.0704 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.83 | 0.4606 | 0.0690 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.43 | 0.4763 | 0.0979 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.67 | 0.5545 | 0.0897 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.60 | 0.5410 | 0.0939 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.64 | 0.5503 | 0.0919 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 10.04 | 0.5086 | 0.0923 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 9.95 | 0.4720 | 0.0897 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.98 | 0.4955 | 0.0909 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.95 | 0.4791 | 0.0906 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.86 | 0.6519 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.50 | 0.7101 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.08 | 0.6937 | 0.0207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.29 | 0.7012 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.59 | 0.6448 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.83 | 0.6841 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.48 | 0.6717 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.68 | 0.6790 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 18.57 | 0.6159 | 0.0284 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 19.16 | 0.6108 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.83 | 0.6792 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.45 | 0.6626 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.61 | 0.6710 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.97 | 0.6029 | 0.0261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.51 | 0.6634 | 0.0205 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.05 | 0.6449 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.27 | 0.6537 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 18.26 | 0.5907 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.57 | 0.5912 | 0.0291 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.59 | 0.6643 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.96 | 0.6465 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.29 | 0.6576 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.86 | 0.6415 | 0.0262 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.02 | 0.6365 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.07 | 0.6460 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.00 | 0.6404 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.85 | 0.6517 | 0.0227 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.50 | 0.7097 | 0.0183 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.08 | 0.6936 | 0.0207 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.29 | 0.7009 | 0.0195 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.58 | 0.6447 | 0.0227 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.82 | 0.6839 | 0.0195 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.47 | 0.6715 | 0.0210 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.67 | 0.6788 | 0.0202 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 18.57 | 0.6145 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 19.14 | 0.6090 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 20.82 | 0.6784 | 0.0195 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 20.45 | 0.6619 | 0.0221 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 20.60 | 0.6703 | 0.0208 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.96 | 0.6019 | 0.0262 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.51 | 0.6627 | 0.0204 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 20.05 | 0.6442 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.27 | 0.6530 | 0.0218 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.25 | 0.5891 | 0.0327 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.56 | 0.5895 | 0.0293 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.58 | 0.6628 | 0.0217 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.96 | 0.6452 | 0.0248 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.28 | 0.6562 | 0.0231 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.86 | 0.6404 | 0.0262 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.02 | 0.6349 | 0.0241 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.07 | 0.6448 | 0.0252 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.99 | 0.6390 | 0.0247 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 50.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.55 | 0.7800 | 0.0369 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 8.58 | 0.6442 | 0.2463 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 8.71 | 0.6547 | 0.2283 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 8.63 | 0.6562 | 0.2368 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 8.66 | 0.6557 | 0.2320 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.11 | 0.5808 | 0.2331 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.22 | 0.5886 | 0.2163 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.11 | 0.5923 | 0.2229 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 10.15 | 0.5917 | 0.2186 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.91 | 0.4971 | 0.2140 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 9.96 | 0.6614 | 0.2260 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 10.17 | 0.6773 | 0.2042 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 10.05 | 0.6782 | 0.2146 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 10.10 | 0.6784 | 0.2087 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 9.93 | 0.6583 | 0.2258 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 10.13 | 0.6733 | 0.2035 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 10.00 | 0.6725 | 0.2145 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 10.05 | 0.6736 | 0.2081 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.97 | 0.5378 | 0.2109 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.38 | 0.6288 | 0.2548 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.51 | 0.6432 | 0.2368 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.42 | 0.6438 | 0.2473 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.45 | 0.6441 | 0.2423 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 10.25 | 0.6095 | 0.2408 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 10.35 | 0.6064 | 0.2260 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 10.29 | 0.6158 | 0.2344 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 10.30 | 0.6116 | 0.2300 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.44 | 0.7870 | 0.0415 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.60 | 0.7968 | 0.0367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.34 | 0.7946 | 0.0394 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.47 | 0.7955 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.24 | 0.7854 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.12 | 0.7918 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.92 | 0.7902 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.04 | 0.7912 | 0.0372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.18 | 0.7788 | 0.0473 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.89 | 0.7813 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.17 | 0.7932 | 0.0380 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.89 | 0.7908 | 0.0411 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.01 | 0.7919 | 0.0395 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.73 | 0.7794 | 0.0438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.90 | 0.7900 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.58 | 0.7870 | 0.0415 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.73 | 0.7884 | 0.0399 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.91 | 0.7742 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.36 | 0.7778 | 0.0465 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.00 | 0.7912 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.48 | 0.7878 | 0.0433 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.75 | 0.7898 | 0.0415 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.37 | 0.7863 | 0.0436 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.56 | 0.7854 | 0.0414 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.59 | 0.7875 | 0.0427 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.55 | 0.7864 | 0.0421 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.77 | 0.7915 | 0.0621 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.15 | 0.8011 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.85 | 0.8014 | 0.0559 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.00 | 0.8013 | 0.0527 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.45 | 0.7867 | 0.0588 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.38 | 0.7918 | 0.0484 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.28 | 0.7942 | 0.0526 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.37 | 0.7935 | 0.0500 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.37 | 0.7654 | 0.0686 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.07 | 0.7816 | 0.0654 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.59 | 0.7949 | 0.0527 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.22 | 0.7949 | 0.0582 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.38 | 0.7951 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.96 | 0.7793 | 0.0662 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.26 | 0.7909 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.91 | 0.7897 | 0.0590 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.08 | 0.7906 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.84 | 0.7522 | 0.0828 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.34 | 0.7640 | 0.0801 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.63 | 0.7756 | 0.0724 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.17 | 0.7765 | 0.0747 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.45 | 0.7772 | 0.0717 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.37 | 0.7717 | 0.0773 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.82 | 0.7689 | 0.0712 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.71 | 0.7764 | 0.0739 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.75 | 0.7735 | 0.0716 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.69 | 0.7516 | 0.0452 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.92 | 0.5430 | 0.3498 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.98 | 0.5538 | 0.3340 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.94 | 0.5540 | 0.3427 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.96 | 0.5542 | 0.3380 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.95 | 0.4781 | 0.3191 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.99 | 0.4861 | 0.3049 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.96 | 0.4863 | 0.3121 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.94 | 0.4868 | 0.3081 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 13.43 | 0.3925 | 0.2641 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.98 | 0.5688 | 0.3314 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.08 | 0.5833 | 0.3129 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.02 | 0.5835 | 0.3231 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.05 | 0.5839 | 0.3175 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.97 | 0.5647 | 0.3300 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.07 | 0.5779 | 0.3120 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.00 | 0.5776 | 0.3225 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.03 | 0.5783 | 0.3170 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 14.26 | 0.4461 | 0.2524 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.22 | 0.5460 | 0.3565 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.28 | 0.5603 | 0.3391 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.24 | 0.5601 | 0.3486 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.26 | 0.5604 | 0.3434 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 8.29 | 0.5086 | 0.3213 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.32 | 0.5075 | 0.3097 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 8.29 | 0.5157 | 0.3153 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.29 | 0.5119 | 0.3126 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.55 | 0.7591 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.54 | 0.7682 | 0.0434 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.31 | 0.7656 | 0.0461 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.42 | 0.7668 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.37 | 0.7577 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.14 | 0.7641 | 0.0431 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.95 | 0.7624 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.07 | 0.7636 | 0.0440 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.33 | 0.7517 | 0.0531 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.03 | 0.7525 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.11 | 0.7633 | 0.0445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.89 | 0.7608 | 0.0477 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.99 | 0.7621 | 0.0460 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.88 | 0.7507 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.87 | 0.7600 | 0.0450 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.60 | 0.7573 | 0.0480 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.73 | 0.7587 | 0.0466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.09 | 0.7470 | 0.0567 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.67 | 0.7510 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.00 | 0.7618 | 0.0467 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.61 | 0.7593 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.82 | 0.7609 | 0.0483 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.47 | 0.7569 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.63 | 0.7574 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.66 | 0.7587 | 0.0495 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.62 | 0.7580 | 0.0489 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.08 | 0.7631 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.24 | 0.7720 | 0.0523 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.00 | 0.7717 | 0.0581 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.11 | 0.7720 | 0.0549 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.82 | 0.7608 | 0.0596 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.61 | 0.7655 | 0.0510 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.52 | 0.7671 | 0.0549 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.58 | 0.7670 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.85 | 0.7444 | 0.0674 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.38 | 0.7534 | 0.0663 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.72 | 0.7657 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.44 | 0.7649 | 0.0607 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.57 | 0.7656 | 0.0573 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.29 | 0.7507 | 0.0668 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.39 | 0.7607 | 0.0553 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.14 | 0.7598 | 0.0612 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.27 | 0.7606 | 0.0578 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.61 | 0.7372 | 0.0753 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.02 | 0.7502 | 0.0734 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.39 | 0.7618 | 0.0609 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.98 | 0.7606 | 0.0673 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.20 | 0.7617 | 0.0635 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.87 | 0.7549 | 0.0688 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.16 | 0.7557 | 0.0603 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.26 | 0.7603 | 0.0646 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.17 | 0.7583 | 0.0622 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 55.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.12 | 0.7280 | 0.0305 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 2.83 | 0.3309 | 0.3314 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 2.85 | 0.3327 | 0.3260 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 2.83 | 0.3336 | 0.3293 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 2.84 | 0.3332 | 0.3276 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 4.97 | 0.2494 | 0.3182 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.97 | 0.2513 | 0.3138 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 4.98 | 0.2517 | 0.3162 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 4.96 | 0.2516 | 0.3154 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.03 | 0.1490 | 0.2652 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.35 | 0.3638 | 0.3124 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.40 | 0.3652 | 0.3057 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.36 | 0.3673 | 0.3102 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.38 | 0.3664 | 0.3083 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.36 | 0.3649 | 0.3114 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.40 | 0.3675 | 0.3044 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.37 | 0.3699 | 0.3086 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.38 | 0.3690 | 0.3064 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 12.53 | 0.2047 | 0.2505 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.35 | 0.3658 | 0.3105 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.39 | 0.3690 | 0.3041 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 3.36 | 0.3696 | 0.3078 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.37 | 0.3689 | 0.3062 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.45 | 0.2876 | 0.2926 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.45 | 0.2913 | 0.2877 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.44 | 0.2941 | 0.2905 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.45 | 0.2930 | 0.2889 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 30.12 | 0.7280 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.12 | 0.7280 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.12 | 0.7280 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.12 | 0.7280 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.12 | 0.7280 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 30.12 | 0.7279 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.11 | 0.7278 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.12 | 0.7279 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.11 | 0.7279 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.12 | 0.7279 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.12 | 0.7279 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.12 | 0.7280 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.12 | 0.7279 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 30.13 | 0.7281 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 30.12 | 0.7279 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.11 | 0.7279 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.12 | 0.7279 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.11 | 0.7279 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 30.09 | 0.7281 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.10 | 0.7282 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.10 | 0.7283 | 0.0317 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.10 | 0.7283 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.09 | 0.7281 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.08 | 0.7280 | 0.0314 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.08 | 0.7281 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.08 | 0.7281 | 0.0315 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.93 | 0.7270 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.97 | 0.7274 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.99 | 0.7276 | 0.0321 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.02 | 0.7279 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.01 | 0.7278 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.00 | 0.7273 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.04 | 0.7278 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.04 | 0.7279 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.04 | 0.7279 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.96 | 0.7276 | 0.0324 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.99 | 0.7277 | 0.0337 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.82 | 0.7270 | 0.0341 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.86 | 0.7273 | 0.0343 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.81 | 0.7271 | 0.0342 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 30.06 | 0.7268 | 0.0328 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.05 | 0.7274 | 0.0324 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.08 | 0.7277 | 0.0327 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.06 | 0.7276 | 0.0326 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.99 | 0.7586 | 0.0657 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 4.87 | 0.4994 | 0.4433 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 4.91 | 0.5057 | 0.4212 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 4.88 | 0.5066 | 0.4318 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 4.89 | 0.5065 | 0.4257 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.98 | 0.4265 | 0.4259 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.99 | 0.4300 | 0.4061 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.99 | 0.4317 | 0.4148 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.98 | 0.4314 | 0.4097 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.92 | 0.3464 | 0.3803 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.50 | 0.5197 | 0.4244 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.57 | 0.5276 | 0.3989 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.52 | 0.5288 | 0.4118 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.54 | 0.5286 | 0.4050 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.51 | 0.5181 | 0.4227 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.56 | 0.5259 | 0.3971 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.52 | 0.5270 | 0.4102 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.54 | 0.5270 | 0.4030 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 13.46 | 0.3849 | 0.3654 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.01 | 0.4914 | 0.4532 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.05 | 0.4999 | 0.4307 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.02 | 0.5002 | 0.4433 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.03 | 0.5004 | 0.4368 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.10 | 0.4298 | 0.4292 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.11 | 0.4294 | 0.4130 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.09 | 0.4347 | 0.4214 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.10 | 0.4323 | 0.4170 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.63 | 0.7628 | 0.0690 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.29 | 0.7679 | 0.0641 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.14 | 0.7664 | 0.0668 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.21 | 0.7671 | 0.0654 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.51 | 0.7620 | 0.0674 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.02 | 0.7656 | 0.0638 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.90 | 0.7647 | 0.0655 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.98 | 0.7654 | 0.0647 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.69 | 0.7586 | 0.0737 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.26 | 0.7590 | 0.0709 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.98 | 0.7649 | 0.0654 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.84 | 0.7635 | 0.0685 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.90 | 0.7643 | 0.0668 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.14 | 0.7580 | 0.0713 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.82 | 0.7631 | 0.0658 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.64 | 0.7616 | 0.0688 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.73 | 0.7624 | 0.0674 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.50 | 0.7559 | 0.0773 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.00 | 0.7582 | 0.0747 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.91 | 0.7642 | 0.0674 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.66 | 0.7628 | 0.0711 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.80 | 0.7637 | 0.0691 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.55 | 0.7613 | 0.0712 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.66 | 0.7618 | 0.0688 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.68 | 0.7624 | 0.0702 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.66 | 0.7621 | 0.0696 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.32 | 0.7667 | 0.0897 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.11 | 0.7715 | 0.0776 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.95 | 0.7715 | 0.0833 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.02 | 0.7717 | 0.0800 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.13 | 0.7653 | 0.0861 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.68 | 0.7677 | 0.0757 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.62 | 0.7688 | 0.0797 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.67 | 0.7687 | 0.0773 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.45 | 0.7548 | 0.0896 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.79 | 0.7611 | 0.0931 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.72 | 0.7676 | 0.0802 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.54 | 0.7674 | 0.0856 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.62 | 0.7677 | 0.0823 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.71 | 0.7595 | 0.0939 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.49 | 0.7649 | 0.0807 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.32 | 0.7647 | 0.0865 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.41 | 0.7650 | 0.0829 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.17 | 0.7507 | 0.0978 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.70 | 0.7508 | 0.1074 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.46 | 0.7569 | 0.0943 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.20 | 0.7564 | 0.1013 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.36 | 0.7570 | 0.0971 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.37 | 0.7534 | 0.1015 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.73 | 0.7547 | 0.0931 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.60 | 0.7567 | 0.0976 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.65 | 0.7559 | 0.0951 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1250 | None | classic | 2.34 | False | 406138 | 0.172 | 34.7 | 32.30 | 0.09 | 0.008 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1250 | None | classic | 2.34 | False | 406138 | 0.172 | 32.7 | 32.30 | 0.09 | 0.008 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1250 | None | classic | 2.34 | False | 406138 | 0.172 | 32.8 | 32.30 | 0.09 | 0.008 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1250 | None | classic | 2.34 | False | 406138 | 0.172 | 32.7 | 32.30 | 0.09 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1056 | None | classic | 0.39 | False | 764336 | 0.691 | 125.1 | 31.00 | 0.15 | 0.010 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1056 | None | classic | 0.39 | False | 764336 | 0.691 | 120.2 | 31.00 | 0.15 | 0.010 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1056 | None | classic | 0.39 | False | 764336 | 0.691 | 128.3 | 31.00 | 0.15 | 0.010 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1056 | None | classic | 0.39 | False | 764336 | 0.691 | 125.1 | 31.00 | 0.15 | 0.010 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1431287 | 0.807 | 161.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 400431 | 0.176 | 30.7 | 31.76 | 0.13 | 0.008 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 400431 | 0.176 | 34.3 | 31.76 | 0.13 | 0.008 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 400431 | 0.176 | 34.3 | 31.76 | 0.13 | 0.008 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 400431 | 0.176 | 29.6 | 31.76 | 0.13 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1262 | None | classic | 2.38 | False | 661164 | 0.507 | 87.4 | 31.80 | 0.13 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1262 | None | classic | 2.38 | False | 661164 | 0.507 | 90.3 | 31.80 | 0.13 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1262 | None | classic | 2.38 | False | 661164 | 0.507 | 85.8 | 31.80 | 0.13 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1262 | None | classic | 2.38 | False | 661164 | 0.507 | 90.2 | 31.80 | 0.13 | 0.005 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1769545 | 0.807 | 75.9 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 402589 | 0.322 | 46.5 | 32.15 | 0.11 | 0.005 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 402589 | 0.322 | 28.3 | 32.15 | 0.11 | 0.005 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 402589 | 0.322 | 27.6 | 32.15 | 0.11 | 0.005 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 402589 | 0.322 | 28.6 | 32.15 | 0.11 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 994 | None | classic | 0.38 | False | 469949 | 0.512 | 76.9 | 31.53 | 0.19 | 0.003 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 994 | None | classic | 0.38 | False | 469949 | 0.512 | 77.3 | 31.53 | 0.19 | 0.003 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 994 | None | classic | 0.38 | False | 469949 | 0.512 | 78.1 | 31.53 | 0.19 | 0.003 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 994 | None | classic | 0.38 | False | 469949 | 0.512 | 78.6 | 31.53 | 0.19 | 0.003 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.819 | 0.024 |
| in035 | mask_ent | 0.684 | 0.024 |
| in035 | mask_grad | 0.467 | 0.024 |
| in035 | r_col | 0.787 | 0.024 |
| in035 | r_warp | 0.864 | 0.024 |

# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 36.1% | 24.29 / 0.0580 | 24.33 / 0.1009 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 36.6% | 24.21 / 0.0580 | 25.55 / 0.0784 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 36.3% | 24.23 / 0.0585 | 25.15 / 0.0882 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 36.4% | 24.21 / 0.0586 | 25.41 / 0.0836 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 36.1% | 24.30 / 0.0582 | 24.27 / 0.0998 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 36.6% | 24.19 / 0.0589 | 25.36 / 0.0796 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 36.3% | 24.24 / 0.0589 | 25.31 / 0.0875 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 36.4% | 24.21 / 0.0596 | 25.41 / 0.0831 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 38.9% | 24.19 / 0.0674 | 22.99 / 0.1455 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 38.3% | 24.44 / 0.0711 | 24.61 / 0.1181 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 38.7% | 24.38 / 0.0721 | 25.42 / 0.0938 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 38.6% | 24.40 / 0.0721 | 25.22 / 0.1018 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 38.6% | 24.40 / 0.0723 | 25.36 / 0.0970 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 38.3% | 24.45 / 0.0708 | 24.43 / 0.1176 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 38.9% | 24.36 / 0.0706 | 25.47 / 0.0923 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 38.7% | 24.40 / 0.0715 | 25.30 / 0.1007 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 38.7% | 24.38 / 0.0711 | 25.45 / 0.0961 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 40.7% | 24.33 / 0.0789 | 23.13 / 0.1693 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 28.6% | 22.98 / 0.0989 | 22.30 / 0.1880 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 29.6% | 23.05 / 0.1016 | 23.61 / 0.1604 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 29.1% | 23.02 / 0.1001 | 23.20 / 0.1732 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 29.4% | 23.04 / 0.1007 | 23.44 / 0.1638 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 29.3% | 23.03 / 0.1017 | 22.72 / 0.1894 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 30.6% | 23.14 / 0.1041 | 23.56 / 0.1671 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 29.8% | 23.07 / 0.1025 | 23.30 / 0.1733 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 30.1% | 23.10 / 0.1039 | 23.48 / 0.1677 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 26.21 / 0.0825 | 23.66 / 0.1001 | 17.48 / 0.0377 | 29.57 / 0.0332 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.41 / 0.1164 | 23.83 / 0.1117 | 18.67 / 0.0384 | 29.53 / 0.0382 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.13 / 0.0989 | 25.27 / 0.0971 | 19.58 / 0.0318 | 29.55 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.89 / 0.1054 | 24.77 / 0.1039 | 19.20 / 0.0346 | 29.55 / 0.0374 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.04 / 0.1021 | 25.03 / 0.0999 | 19.43 / 0.0333 | 29.55 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.39 / 0.1161 | 23.46 / 0.1146 | 18.90 / 0.0387 | 29.54 / 0.0383 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.07 / 0.0999 | 24.94 / 0.1024 | 19.70 / 0.0327 | 29.57 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.01 / 0.1048 | 24.72 / 0.1070 | 19.57 / 0.0347 | 29.58 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.05 / 0.1022 | 24.84 / 0.1040 | 19.69 / 0.0338 | 29.57 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.77 / 0.1294 | 22.36 / 0.1581 | 18.72 / 0.0555 | 29.48 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.53 / 0.1174 | 24.35 / 0.1085 | 18.92 / 0.0360 | 29.46 / 0.0393 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.05 / 0.0984 | 25.42 / 0.0927 | 19.47 / 0.0301 | 29.55 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.91 / 0.1055 | 25.09 / 0.1003 | 19.25 / 0.0327 | 29.55 / 0.0378 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.98 / 0.1016 | 25.27 / 0.0962 | 19.36 / 0.0318 | 29.55 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.44 / 0.1173 | 23.70 / 0.1100 | 19.13 / 0.0372 | 29.47 / 0.0395 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.11 / 0.0993 | 25.11 / 0.0947 | 19.88 / 0.0306 | 29.54 / 0.0370 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.00 / 0.1054 | 24.79 / 0.1009 | 19.68 / 0.0334 | 29.54 / 0.0379 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.09 / 0.1016 | 25.02 / 0.0978 | 19.85 / 0.0320 | 29.54 / 0.0373 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.76 / 0.1305 | 22.32 / 0.1606 | 18.76 / 0.0559 | 29.47 / 0.0358 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 25.88 / 0.1210 | 23.86 / 0.1138 | 19.23 / 0.0368 | 29.39 / 0.0397 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.71 / 0.1070 | 25.74 / 0.0946 | 20.18 / 0.0304 | 29.40 / 0.0398 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.45 / 0.1126 | 25.16 / 0.1035 | 19.89 / 0.0331 | 29.43 / 0.0391 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.60 / 0.1087 | 25.47 / 0.0983 | 20.08 / 0.0316 | 29.43 / 0.0390 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.13 / 0.1209 | 23.91 / 0.1130 | 19.32 / 0.0359 | 29.39 / 0.0405 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.67 / 0.1108 | 25.98 / 0.0951 | 19.83 / 0.0312 | 29.34 / 0.0429 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.50 / 0.1136 | 25.20 / 0.1025 | 19.60 / 0.0337 | 29.42 / 0.0402 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.60 / 0.1112 | 25.59 / 0.0978 | 19.72 / 0.0327 | 29.39 / 0.0412 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 8.3%） | — | — | 26.21 / 0.0825 | 23.66 / 0.1001 | 29.57 |
| in035 | rife | 20.7% | 28.6% | 25.88 / 0.1210 | 23.86 / 0.1138 | 29.39 |
| in035 | cnw_cnn | 32.0% | 36.1% | 26.41 / 0.1164 | 23.83 / 0.1117 | 29.53 |
| in035 | cnw_f5 | 34.3% | 38.3% | 26.53 / 0.1174 | 24.35 / 0.1085 | 29.46 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 24.97 / 0.0857 | +0.81 / +0.0294 (core 19.5%) | +1.05 / +0.0299 (core 35.3%) | +1.36 / +0.0281 (core 37.6%) |
| in035 | 2 | 0-3 | 26.01 / 0.0836 | -0.97 / +0.0538 (core 19.5%) | +0.58 / +0.0378 (core 35.3%) | +0.69 / +0.0381 (core 37.6%) |
| in035 | 4 | 3-5 | 27.65 / 0.0783 | -0.82 / +0.0320 (core 14.2%) | -1.03 / +0.0338 (core 21.3%) | -1.09 / +0.0385 (core 22.9%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 26.21 / 0.0825 | 23.66 | 29.57 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.41 / 0.1164 | 23.83 | 29.53 | 0/3 |
| in035 | cnw_cnn | oracle | 5.6% | 26.75 / 0.0843 | 24.37 | 29.56 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.13 / 0.0989 | 25.27 | 29.55 | 0/3 |
| in035 | cnw_cnn | oracle | 5.8% | 27.33 / 0.0788 | 25.76 | 29.55 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.89 / 0.1054 | 24.77 | 29.55 | 0/3 |
| in035 | cnw_cnn | oracle | 5.7% | 27.10 / 0.0819 | 25.26 | 29.56 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.04 / 0.1021 | 25.03 | 29.55 | 0/3 |
| in035 | cnw_cnn | oracle | 5.7% | 27.25 / 0.0805 | 25.56 | 29.55 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.39 / 0.1161 | 23.46 | 29.54 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.6% | 26.88 / 0.0842 | 24.40 | 29.56 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.07 / 0.0999 | 24.94 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.7% | 27.36 / 0.0789 | 25.49 | 29.56 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.01 / 0.1048 | 24.72 | 29.58 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.7% | 27.29 / 0.0813 | 25.33 | 29.56 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.05 / 0.1022 | 24.84 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.7% | 27.35 / 0.0806 | 25.46 | 29.56 | 2/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 25.77 / 0.1294 | 22.36 | 29.48 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 5.9% | 26.68 / 0.0998 | 23.77 | 29.56 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.53 / 0.1174 | 24.35 | 29.46 | 0/3 |
| in035 | cnw_f5 | oracle | 5.8% | 26.90 / 0.0834 | 24.85 | 29.56 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.05 / 0.0984 | 25.42 | 29.55 | 0/3 |
| in035 | cnw_f5 | oracle | 5.9% | 27.26 / 0.0778 | 25.77 | 29.56 | 2/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.91 / 0.1055 | 25.09 | 29.55 | 0/3 |
| in035 | cnw_f5 | oracle | 5.9% | 27.12 / 0.0810 | 25.45 | 29.56 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.98 / 0.1016 | 25.27 | 29.55 | 0/3 |
| in035 | cnw_f5 | oracle | 5.9% | 27.20 / 0.0797 | 25.64 | 29.56 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.44 / 0.1173 | 23.70 | 29.47 | 0/3 |
| in035 | cnw_f5_mw | oracle | 5.8% | 26.98 / 0.0832 | 24.50 | 29.56 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.11 / 0.0993 | 25.11 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 5.9% | 27.45 / 0.0776 | 25.52 | 29.56 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.00 / 0.1054 | 24.79 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 5.9% | 27.33 / 0.0809 | 25.28 | 29.56 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.09 / 0.1016 | 25.02 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 5.9% | 27.42 / 0.0792 | 25.46 | 29.56 | 2/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 25.76 / 0.1305 | 22.32 | 29.47 | 0/3 |
| in035 | cnw_f5_pix | oracle | 6.1% | 26.70 / 0.1006 | 23.78 | 29.56 | 0/3 |
| in035 | rife | 不复核 | —% | 25.88 / 0.1210 | 23.86 | 29.39 | 0/3 |
| in035 | rife | oracle | 6.0% | 27.07 / 0.0839 | 24.71 | 29.56 | 1/3 |
| in035 | rife | 不复核 | —% | 26.71 / 0.1070 | 25.74 | 29.40 | 0/3 |
| in035 | rife | oracle | 6.1% | 27.64 / 0.0779 | 26.29 | 29.57 | 3/3 |
| in035 | rife | 不复核 | —% | 26.45 / 0.1126 | 25.16 | 29.43 | 0/3 |
| in035 | rife | oracle | 6.1% | 27.49 / 0.0811 | 25.80 | 29.57 | 2/3 |
| in035 | rife | 不复核 | —% | 26.60 / 0.1087 | 25.47 | 29.43 | 0/3 |
| in035 | rife | oracle | 6.1% | 27.59 / 0.0794 | 26.11 | 29.57 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 26.13 / 0.1209 | 23.91 | 29.39 | 0/3 |
| in035 | rife_mw | oracle | 6.1% | 27.12 / 0.0833 | 24.80 | 29.56 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 26.67 / 0.1108 | 25.98 | 29.34 | 0/3 |
| in035 | rife_mw | oracle | 6.2% | 27.49 / 0.0787 | 26.36 | 29.57 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 26.50 / 0.1136 | 25.20 | 29.42 | 0/3 |
| in035 | rife_mw | oracle | 6.1% | 27.35 / 0.0813 | 25.79 | 29.56 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 26.60 / 0.1112 | 25.59 | 29.39 | 0/3 |
| in035 | rife_mw | oracle | 6.1% | 27.42 / 0.0800 | 26.05 | 29.57 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 26.21 / 0.0825 | 23.66 / 0.1001 | — |
| in035 | FF | 0（前馈） | 994×664（63%） | 29.47 | 26.41 / 0.1164 | 23.83 / 0.1117 | 0/3 |
| in035 | 25 | 1.54 s | 994×664（63%） | 30.67 | 26.89 / 0.1054 | 24.77 / 0.1039 | 0/3 |
| in035 | 50 | 3.08 s | 994×664（63%） | 31.07 | 27.04 / 0.1021 | 25.03 / 0.0999 | 0/3 |
| in035 | 100 | 6.12 s | 994×664（63%） | 31.41 | 27.13 / 0.0989 | 25.27 / 0.0971 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 26.21 / 0.0825 | 23.66 / 0.1001 | 29.57 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.41 / 0.1164 | 23.83 / 0.1117 | 29.53 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 26.75 / 0.0843 | 24.37 / 0.0930 | 29.56 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 26.89 / 0.1054 | 24.77 / 0.1039 | 29.55 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.10 / 0.0819 | 25.26 / 0.0878 | 29.56 | 2/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.04 / 0.1021 | 25.03 / 0.0999 | 29.55 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.25 / 0.0805 | 25.56 / 0.0854 | 29.55 | 2/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.13 / 0.0989 | 25.27 / 0.0971 | 29.55 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.33 / 0.0788 | 25.76 / 0.0832 | 29.55 | 2/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 26.39 / 0.1161 | 23.46 / 0.1146 | 29.54 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 26.88 / 0.0842 | 24.40 / 0.0957 | 29.56 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.01 / 0.1048 | 24.72 / 0.1070 | 29.58 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.29 / 0.0813 | 25.33 / 0.0902 | 29.56 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.05 / 0.1022 | 24.84 / 0.1040 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.35 / 0.0806 | 25.46 / 0.0887 | 29.56 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.07 / 0.0999 | 24.94 / 0.1024 | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.36 / 0.0789 | 25.49 / 0.0864 | 29.56 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.53 / 0.1174 | 24.35 / 0.1085 | 29.46 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 26.90 / 0.0834 | 24.85 / 0.0902 | 29.56 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.91 / 0.1055 | 25.09 / 0.1003 | 29.55 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.12 / 0.0810 | 25.45 / 0.0850 | 29.56 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.98 / 0.1016 | 25.27 / 0.0962 | 29.55 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.20 / 0.0797 | 25.64 / 0.0828 | 29.56 | 2/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.05 / 0.0984 | 25.42 / 0.0927 | 29.55 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.26 / 0.0778 | 25.77 / 0.0806 | 29.56 | 2/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.44 / 0.1173 | 23.70 / 0.1100 | 29.47 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 26.98 / 0.0832 | 24.50 / 0.0904 | 29.56 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.00 / 0.1054 | 24.79 / 0.1009 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.33 / 0.0809 | 25.28 / 0.0863 | 29.56 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.09 / 0.1016 | 25.02 / 0.0978 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.42 / 0.0792 | 25.46 / 0.0835 | 29.56 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.11 / 0.0993 | 25.11 / 0.0947 | 29.54 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.45 / 0.0776 | 25.52 / 0.0811 | 29.56 | 2/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 25.88 / 0.1210 | 23.86 / 0.1138 | 29.39 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.07 / 0.0839 | 24.71 / 0.0961 | 29.56 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 26.45 / 0.1126 | 25.16 / 0.1035 | 29.43 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.49 / 0.0811 | 25.80 / 0.0883 | 29.57 | 2/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 26.60 / 0.1087 | 25.47 / 0.0983 | 29.43 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.59 / 0.0794 | 26.11 / 0.0854 | 29.57 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.71 / 0.1070 | 25.74 / 0.0946 | 29.40 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.64 / 0.0779 | 26.29 / 0.0832 | 29.57 | 3/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.13 / 0.1209 | 23.91 / 0.1130 | 29.39 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.12 / 0.0833 | 24.80 / 0.0943 | 29.56 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 26.50 / 0.1136 | 25.20 / 0.1025 | 29.42 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.35 / 0.0813 | 25.79 / 0.0883 | 29.56 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 26.60 / 0.1112 | 25.59 / 0.0978 | 29.39 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.42 / 0.0800 | 26.05 / 0.0860 | 29.57 | 2/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 26.67 / 0.1108 | 25.98 / 0.0951 | 29.34 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.49 / 0.0787 | 26.36 / 0.0839 | 29.57 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.66 / 0.1001 | 17.48 / 0.0377 | 29.57 / 0.0332 | 26.21 / 0.0825 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 17.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.66 | 0.7485 | 0.1001 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 19.67 | 0.7482 | 0.1728 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 21.71 | 0.7789 | 0.1418 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 20.78 | 0.7733 | 0.1595 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 21.18 | 0.7765 | 0.1498 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 19.02 | 0.7400 | 0.1780 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 21.20 | 0.7621 | 0.1506 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 20.24 | 0.7620 | 0.1632 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 20.68 | 0.7635 | 0.1569 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 18.80 | 0.6754 | 0.2012 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 20.43 | 0.7729 | 0.1522 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 21.79 | 0.7973 | 0.1264 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 21.36 | 0.7955 | 0.1382 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 21.55 | 0.7980 | 0.1317 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 19.81 | 0.7599 | 0.1570 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 21.32 | 0.7796 | 0.1325 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 20.81 | 0.7824 | 0.1419 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 21.07 | 0.7833 | 0.1364 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.26 | 0.6831 | 0.1976 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 17.62 | 0.7252 | 0.1926 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 19.32 | 0.7593 | 0.1659 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 18.68 | 0.7571 | 0.1774 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 18.98 | 0.7597 | 0.1701 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 18.14 | 0.7287 | 0.1919 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 19.80 | 0.7581 | 0.1673 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 19.05 | 0.7557 | 0.1773 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 19.36 | 0.7585 | 0.1711 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.37 | 0.7743 | 0.0930 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.76 | 0.7956 | 0.0832 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.26 | 0.7910 | 0.0878 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.56 | 0.7934 | 0.0854 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.40 | 0.7725 | 0.0957 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.49 | 0.7853 | 0.0864 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.33 | 0.7854 | 0.0902 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.46 | 0.7858 | 0.0887 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 23.77 | 0.7523 | 0.1260 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 24.85 | 0.7856 | 0.0902 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.77 | 0.8019 | 0.0806 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.45 | 0.7990 | 0.0850 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.64 | 0.8009 | 0.0828 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.50 | 0.7747 | 0.0904 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.52 | 0.7879 | 0.0811 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.28 | 0.7878 | 0.0863 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.46 | 0.7886 | 0.0835 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 23.78 | 0.7526 | 0.1284 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.71 | 0.7661 | 0.0961 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.29 | 0.7895 | 0.0832 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.80 | 0.7862 | 0.0883 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.11 | 0.7883 | 0.0854 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 24.80 | 0.7684 | 0.0943 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.36 | 0.7888 | 0.0839 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.79 | 0.7847 | 0.0883 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.05 | 0.7867 | 0.0860 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 23.83 | 0.7806 | 0.1117 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.27 | 0.8055 | 0.0971 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.77 | 0.8010 | 0.1039 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.03 | 0.8035 | 0.0999 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 23.46 | 0.7746 | 0.1146 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.94 | 0.7912 | 0.1024 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.72 | 0.7920 | 0.1070 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.84 | 0.7926 | 0.1040 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 22.36 | 0.7180 | 0.1581 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.35 | 0.7929 | 0.1085 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.42 | 0.8128 | 0.0927 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.09 | 0.8108 | 0.1003 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.27 | 0.8127 | 0.0962 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 23.70 | 0.7781 | 0.1100 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.11 | 0.7951 | 0.0947 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.79 | 0.7966 | 0.1009 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.02 | 0.7976 | 0.0978 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 22.32 | 0.7182 | 0.1606 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.86 | 0.7670 | 0.1138 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.74 | 0.7974 | 0.0946 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.16 | 0.7931 | 0.1035 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.47 | 0.7963 | 0.0983 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.91 | 0.7694 | 0.1130 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.98 | 0.7961 | 0.0951 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.20 | 0.7914 | 0.1025 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.59 | 0.7950 | 0.0978 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 8.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.48 | 0.5080 | 0.0377 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 11.36 | 0.4989 | 0.0952 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.81 | 0.5459 | 0.0839 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.62 | 0.5282 | 0.0894 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.72 | 0.5373 | 0.0871 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 11.28 | 0.5101 | 0.0955 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.80 | 0.5383 | 0.0847 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.61 | 0.5361 | 0.0896 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.72 | 0.5388 | 0.0875 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.90 | 0.4873 | 0.0860 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 12.01 | 0.5443 | 0.0835 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.43 | 0.5749 | 0.0749 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.32 | 0.5676 | 0.0787 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.39 | 0.5726 | 0.0773 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 12.04 | 0.5452 | 0.0853 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 12.62 | 0.5740 | 0.0752 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 12.44 | 0.5721 | 0.0795 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 12.56 | 0.5757 | 0.0775 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.68 | 0.5069 | 0.0794 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.00 | 0.4896 | 0.1046 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 10.31 | 0.5290 | 0.0951 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 10.21 | 0.5221 | 0.0993 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 10.27 | 0.5254 | 0.0974 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 10.06 | 0.4995 | 0.1026 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 10.29 | 0.5153 | 0.0956 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 10.20 | 0.5138 | 0.0991 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 10.25 | 0.5143 | 0.0977 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.68 | 0.5799 | 0.0383 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.59 | 0.6184 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.21 | 0.6025 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.44 | 0.6111 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.93 | 0.5897 | 0.0385 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.71 | 0.6123 | 0.0325 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.58 | 0.6109 | 0.0346 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.70 | 0.6134 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 18.73 | 0.5643 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.93 | 0.6019 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.49 | 0.6268 | 0.0299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.26 | 0.6189 | 0.0327 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.39 | 0.6241 | 0.0317 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.15 | 0.6027 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.90 | 0.6242 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.71 | 0.6233 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.87 | 0.6265 | 0.0319 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 18.78 | 0.5667 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.24 | 0.5919 | 0.0365 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.19 | 0.6274 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 19.90 | 0.6202 | 0.0329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.08 | 0.6241 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.33 | 0.5990 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.83 | 0.6144 | 0.0312 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.61 | 0.6102 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.73 | 0.6128 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.67 | 0.5787 | 0.0384 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.58 | 0.6175 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.20 | 0.6017 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.43 | 0.6101 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.90 | 0.5883 | 0.0387 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.70 | 0.6115 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.57 | 0.6101 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.69 | 0.6129 | 0.0338 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 18.72 | 0.5607 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.92 | 0.6008 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.47 | 0.6256 | 0.0301 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.25 | 0.6181 | 0.0327 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.36 | 0.6230 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.13 | 0.6015 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.88 | 0.6237 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.68 | 0.6225 | 0.0334 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.85 | 0.6258 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.76 | 0.5631 | 0.0559 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.23 | 0.5912 | 0.0368 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.18 | 0.6266 | 0.0304 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 19.89 | 0.6196 | 0.0331 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.08 | 0.6235 | 0.0316 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.32 | 0.5977 | 0.0359 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.83 | 0.6136 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.60 | 0.6095 | 0.0337 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.72 | 0.6122 | 0.0327 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 53.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.54 | 0.7580 | 0.0600 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 10.49 | 0.6736 | 0.2481 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 10.71 | 0.6887 | 0.2245 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 10.59 | 0.6886 | 0.2367 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 10.64 | 0.6894 | 0.2310 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.43 | 0.6714 | 0.2476 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.70 | 0.6837 | 0.2246 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 10.54 | 0.6865 | 0.2361 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 10.60 | 0.6860 | 0.2304 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 16.99 | 0.5855 | 0.2208 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 11.20 | 0.6977 | 0.2283 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 11.39 | 0.7103 | 0.2055 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 11.30 | 0.7124 | 0.2163 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 11.34 | 0.7124 | 0.2110 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 11.20 | 0.6929 | 0.2289 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 11.42 | 0.7051 | 0.2060 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 11.32 | 0.7092 | 0.2166 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 11.37 | 0.7086 | 0.2109 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.81 | 0.6056 | 0.2094 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.48 | 0.6394 | 0.2766 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.63 | 0.6543 | 0.2596 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.56 | 0.6565 | 0.2687 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.60 | 0.6566 | 0.2640 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 9.53 | 0.6420 | 0.2783 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 9.67 | 0.6515 | 0.2608 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.59 | 0.6554 | 0.2703 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.63 | 0.6549 | 0.2650 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.14 | 0.7641 | 0.0634 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.94 | 0.7741 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.63 | 0.7707 | 0.0618 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.82 | 0.7728 | 0.0603 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.32 | 0.7651 | 0.0628 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.97 | 0.7718 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.88 | 0.7713 | 0.0605 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.97 | 0.7719 | 0.0599 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.01 | 0.7551 | 0.0804 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.36 | 0.7689 | 0.0628 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.85 | 0.7764 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.65 | 0.7745 | 0.0609 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.76 | 0.7758 | 0.0594 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.48 | 0.7677 | 0.0622 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.13 | 0.7749 | 0.0570 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.97 | 0.7744 | 0.0604 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.09 | 0.7751 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.02 | 0.7549 | 0.0820 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.54 | 0.7652 | 0.0621 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.33 | 0.7749 | 0.0564 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.11 | 0.7734 | 0.0598 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.25 | 0.7745 | 0.0581 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.61 | 0.7669 | 0.0618 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.13 | 0.7732 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.94 | 0.7720 | 0.0602 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.04 | 0.7728 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.64 | 0.7674 | 0.0894 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.57 | 0.7790 | 0.0747 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.26 | 0.7780 | 0.0811 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.45 | 0.7793 | 0.0779 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.61 | 0.7667 | 0.0886 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.45 | 0.7739 | 0.0762 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.40 | 0.7768 | 0.0807 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.46 | 0.7763 | 0.0780 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.40 | 0.7191 | 0.1192 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.73 | 0.7704 | 0.0903 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.37 | 0.7798 | 0.0748 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.18 | 0.7809 | 0.0816 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.29 | 0.7812 | 0.0782 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.62 | 0.7669 | 0.0901 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.48 | 0.7762 | 0.0751 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.33 | 0.7789 | 0.0808 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.45 | 0.7788 | 0.0775 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.37 | 0.7164 | 0.1210 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.90 | 0.7554 | 0.0953 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.95 | 0.7677 | 0.0826 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.60 | 0.7685 | 0.0891 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.80 | 0.7690 | 0.0853 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.20 | 0.7582 | 0.0952 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.91 | 0.7660 | 0.0847 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.68 | 0.7683 | 0.0891 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.82 | 0.7684 | 0.0861 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 55.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.61 | 0.7076 | 0.0647 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.76 | 0.5484 | 0.3262 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.83 | 0.5638 | 0.3056 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.79 | 0.5627 | 0.3171 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.81 | 0.5638 | 0.3116 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.76 | 0.5479 | 0.3262 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.84 | 0.5603 | 0.3051 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.80 | 0.5622 | 0.3158 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.82 | 0.5620 | 0.3105 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.03 | 0.4757 | 0.2392 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.03 | 0.5683 | 0.3097 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 7.10 | 0.5803 | 0.2895 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 7.07 | 0.5824 | 0.2995 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 7.08 | 0.5823 | 0.2942 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.03 | 0.5635 | 0.3111 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 7.10 | 0.5749 | 0.2909 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 7.07 | 0.5784 | 0.3007 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 7.08 | 0.5779 | 0.2957 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.99 | 0.4981 | 0.2287 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.05 | 0.5263 | 0.3498 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.11 | 0.5410 | 0.3312 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.08 | 0.5426 | 0.3410 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.10 | 0.5427 | 0.3359 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.07 | 0.5305 | 0.3484 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.11 | 0.5402 | 0.3307 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.10 | 0.5430 | 0.3398 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.10 | 0.5425 | 0.3348 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.31 | 0.7150 | 0.0659 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.07 | 0.7246 | 0.0604 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.77 | 0.7212 | 0.0637 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.96 | 0.7232 | 0.0622 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.48 | 0.7161 | 0.0659 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.11 | 0.7225 | 0.0605 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.02 | 0.7220 | 0.0630 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.10 | 0.7225 | 0.0623 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.21 | 0.7094 | 0.0815 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.52 | 0.7188 | 0.0649 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.00 | 0.7262 | 0.0592 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.80 | 0.7241 | 0.0625 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.91 | 0.7254 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.63 | 0.7178 | 0.0647 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.24 | 0.7244 | 0.0590 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.09 | 0.7238 | 0.0624 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.21 | 0.7246 | 0.0607 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.23 | 0.7094 | 0.0823 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.72 | 0.7164 | 0.0655 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.50 | 0.7254 | 0.0594 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.28 | 0.7240 | 0.0628 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.43 | 0.7250 | 0.0610 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.79 | 0.7177 | 0.0648 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.28 | 0.7235 | 0.0602 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.10 | 0.7223 | 0.0629 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.20 | 0.7231 | 0.0615 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.86 | 0.7177 | 0.0829 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.76 | 0.7293 | 0.0702 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.45 | 0.7276 | 0.0766 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.64 | 0.7291 | 0.0734 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.83 | 0.7176 | 0.0829 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.68 | 0.7252 | 0.0710 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.60 | 0.7270 | 0.0761 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.66 | 0.7267 | 0.0737 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.05 | 0.6847 | 0.1058 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.05 | 0.7209 | 0.0822 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.67 | 0.7305 | 0.0693 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.50 | 0.7307 | 0.0754 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.59 | 0.7312 | 0.0721 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.95 | 0.7180 | 0.0826 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.77 | 0.7269 | 0.0696 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.64 | 0.7286 | 0.0758 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.75 | 0.7287 | 0.0725 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.05 | 0.6841 | 0.1071 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.93 | 0.7165 | 0.0878 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.07 | 0.7281 | 0.0736 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.80 | 0.7289 | 0.0803 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.97 | 0.7292 | 0.0765 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.08 | 0.7186 | 0.0879 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.95 | 0.7267 | 0.0756 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.69 | 0.7282 | 0.0811 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.84 | 0.7283 | 0.0776 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 52.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.57 | 0.6892 | 0.0332 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 3.02 | 0.3341 | 0.3006 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 3.05 | 0.3370 | 0.2936 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 3.03 | 0.3387 | 0.2976 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 3.04 | 0.3381 | 0.2955 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 3.02 | 0.3342 | 0.3002 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.04 | 0.3373 | 0.2932 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 3.03 | 0.3392 | 0.2971 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 3.03 | 0.3387 | 0.2952 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.01 | 0.2332 | 0.2139 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 3.17 | 0.3475 | 0.2915 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 3.20 | 0.3500 | 0.2824 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 3.18 | 0.3531 | 0.2876 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 3.19 | 0.3519 | 0.2849 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 3.17 | 0.3449 | 0.2930 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 3.19 | 0.3477 | 0.2840 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 3.18 | 0.3506 | 0.2887 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 3.19 | 0.3497 | 0.2860 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.56 | 0.2569 | 0.2027 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.72 | 0.3097 | 0.3225 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.74 | 0.3124 | 0.3169 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 2.73 | 0.3144 | 0.3199 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.73 | 0.3139 | 0.3181 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 2.73 | 0.3113 | 0.3212 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 2.75 | 0.3121 | 0.3161 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 2.74 | 0.3157 | 0.3186 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 2.74 | 0.3144 | 0.3171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.56 | 0.6890 | 0.0333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.55 | 0.6890 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.56 | 0.6890 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.55 | 0.6890 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.56 | 0.6890 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.56 | 0.6891 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.56 | 0.6891 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.56 | 0.6891 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.56 | 0.6891 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.56 | 0.6891 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.56 | 0.6891 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.56 | 0.6891 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.56 | 0.6891 | 0.0337 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.56 | 0.6890 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.56 | 0.6891 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.56 | 0.6891 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.56 | 0.6891 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.56 | 0.6891 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.56 | 0.6891 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.57 | 0.6891 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.57 | 0.6891 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.57 | 0.6891 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.56 | 0.6891 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.57 | 0.6892 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.56 | 0.6891 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.57 | 0.6891 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.53 | 0.6913 | 0.0382 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.55 | 0.6913 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.55 | 0.6918 | 0.0374 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.55 | 0.6916 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.54 | 0.6913 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.57 | 0.6912 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.58 | 0.6918 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.57 | 0.6916 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.48 | 0.6906 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.46 | 0.6907 | 0.0393 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.55 | 0.6912 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.55 | 0.6917 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.55 | 0.6915 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.47 | 0.6905 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.54 | 0.6910 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.54 | 0.6915 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.54 | 0.6913 | 0.0373 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.47 | 0.6906 | 0.0358 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.39 | 0.6896 | 0.0397 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.40 | 0.6900 | 0.0398 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 29.43 | 0.6903 | 0.0391 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.43 | 0.6903 | 0.0390 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.39 | 0.6898 | 0.0405 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.34 | 0.6896 | 0.0429 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.42 | 0.6905 | 0.0402 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.39 | 0.6903 | 0.0412 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.21 | 0.7197 | 0.0825 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.26 | 0.5029 | 0.4089 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.31 | 0.5127 | 0.3794 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.28 | 0.5128 | 0.3930 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.29 | 0.5132 | 0.3864 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.25 | 0.5024 | 0.4078 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.30 | 0.5106 | 0.3790 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.28 | 0.5125 | 0.3912 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.29 | 0.5122 | 0.3850 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 16.36 | 0.4270 | 0.3370 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 5.48 | 0.5195 | 0.3912 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 5.52 | 0.5273 | 0.3595 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 5.50 | 0.5297 | 0.3733 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 5.51 | 0.5292 | 0.3661 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 5.47 | 0.5157 | 0.3924 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 5.52 | 0.5234 | 0.3619 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 5.49 | 0.5266 | 0.3746 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 5.50 | 0.5259 | 0.3677 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.05 | 0.4478 | 0.3222 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.83 | 0.4713 | 0.4382 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.87 | 0.4803 | 0.4175 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 4.85 | 0.4824 | 0.4275 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.86 | 0.4821 | 0.4218 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 4.85 | 0.4742 | 0.4366 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 4.88 | 0.4792 | 0.4179 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 4.86 | 0.4833 | 0.4265 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 4.87 | 0.4822 | 0.4214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.75 | 0.7235 | 0.0843 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.33 | 0.7289 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.10 | 0.7270 | 0.0819 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.25 | 0.7282 | 0.0805 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.88 | 0.7242 | 0.0842 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.36 | 0.7278 | 0.0789 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.29 | 0.7274 | 0.0813 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.35 | 0.7278 | 0.0806 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.68 | 0.7205 | 0.0998 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.90 | 0.7256 | 0.0834 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.26 | 0.7298 | 0.0778 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.12 | 0.7286 | 0.0810 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.20 | 0.7293 | 0.0797 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.98 | 0.7250 | 0.0832 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.45 | 0.7288 | 0.0776 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.33 | 0.7284 | 0.0809 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.42 | 0.7289 | 0.0792 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.70 | 0.7205 | 0.1006 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.07 | 0.7244 | 0.0839 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.64 | 0.7295 | 0.0779 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.49 | 0.7287 | 0.0811 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.59 | 0.7292 | 0.0794 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.12 | 0.7252 | 0.0833 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.49 | 0.7285 | 0.0787 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.35 | 0.7278 | 0.0813 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.42 | 0.7282 | 0.0800 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.41 | 0.7273 | 0.1164 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.13 | 0.7337 | 0.0989 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.89 | 0.7331 | 0.1054 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.04 | 0.7338 | 0.1021 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.39 | 0.7271 | 0.1161 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.07 | 0.7312 | 0.0999 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.01 | 0.7327 | 0.1048 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.05 | 0.7323 | 0.1022 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.77 | 0.7089 | 0.1294 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.53 | 0.7287 | 0.1174 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.05 | 0.7342 | 0.0984 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.91 | 0.7347 | 0.1055 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.98 | 0.7348 | 0.1016 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.44 | 0.7268 | 0.1173 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.11 | 0.7318 | 0.0993 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.00 | 0.7333 | 0.1054 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.09 | 0.7331 | 0.1016 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.76 | 0.7086 | 0.1305 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.88 | 0.7207 | 0.1210 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.71 | 0.7274 | 0.1070 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.45 | 0.7279 | 0.1126 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.60 | 0.7281 | 0.1087 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.13 | 0.7224 | 0.1209 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.67 | 0.7266 | 0.1108 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.50 | 0.7280 | 0.1136 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.60 | 0.7279 | 0.1112 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1270 | None | classic | 2.41 | False | 401717 | 0.321 | 70.8 | 31.91 | 0.07 | 0.004 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1270 | None | classic | 2.41 | False | 401717 | 0.321 | 70.0 | 31.91 | 0.07 | 0.004 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1270 | None | classic | 2.41 | False | 401717 | 0.321 | 47.9 | 31.91 | 0.07 | 0.004 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1270 | None | classic | 2.41 | False | 401717 | 0.321 | 66.7 | 31.91 | 0.07 | 0.004 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1144 | None | classic | 1.96 | False | 620222 | 0.992 | 142.0 | 31.24 | 0.10 | 0.004 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1144 | None | classic | 1.96 | False | 620222 | 0.992 | 139.0 | 31.24 | 0.10 | 0.004 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1144 | None | classic | 1.96 | False | 620222 | 0.992 | 138.5 | 31.24 | 0.10 | 0.004 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1144 | None | classic | 1.96 | False | 620222 | 0.992 | 145.6 | 31.24 | 0.10 | 0.004 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1995513 | 0.804 | 487.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1178 | None | classic | 2.07 | False | 353115 | 0.324 | 83.5 | 31.53 | 0.06 | 0.005 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1178 | None | classic | 2.07 | False | 353115 | 0.324 | 50.4 | 31.53 | 0.06 | 0.005 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1178 | None | classic | 2.07 | False | 353115 | 0.324 | 70.7 | 31.53 | 0.06 | 0.005 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1178 | None | classic | 2.07 | False | 353115 | 0.324 | 69.7 | 31.53 | 0.06 | 0.005 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1146 | None | classic | 1.96 | False | 331881 | 0.327 | 62.8 | 31.11 | 0.15 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1146 | None | classic | 1.96 | False | 331881 | 0.327 | 51.7 | 31.11 | 0.15 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1146 | None | classic | 1.96 | False | 331881 | 0.327 | 59.3 | 31.11 | 0.15 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1146 | None | classic | 1.96 | False | 331881 | 0.327 | 64.1 | 31.11 | 0.15 | 0.007 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2140097 | 0.804 | 124.4 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1094 | None | classic | 1.79 | False | 297134 | 0.873 | 81.2 | 30.78 | 0.07 | 0.004 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1094 | None | classic | 1.79 | False | 297134 | 0.873 | 75.1 | 30.78 | 0.07 | 0.004 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1094 | None | classic | 1.79 | False | 297134 | 0.873 | 80.1 | 30.78 | 0.07 | 0.004 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1094 | None | classic | 1.79 | False | 297134 | 0.873 | 62.7 | 30.78 | 0.07 | 0.004 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1062 | None | classic | 1.69 | False | 254237 | 0.330 | 53.0 | 30.86 | 0.07 | 0.003 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1062 | None | classic | 1.69 | False | 254237 | 0.330 | 53.0 | 30.86 | 0.07 | 0.003 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1062 | None | classic | 1.69 | False | 254237 | 0.330 | 57.7 | 30.86 | 0.07 | 0.003 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1062 | None | classic | 1.69 | False | 254237 | 0.330 | 69.3 | 30.86 | 0.07 | 0.003 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.857 | 0.040 |
| in035 | mask_ent | 0.644 | 0.040 |
| in035 | mask_grad | 0.452 | 0.040 |
| in035 | r_col | 0.848 | 0.040 |
| in035 | r_warp | 0.843 | 0.040 |

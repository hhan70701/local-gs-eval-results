# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 21.6% | 22.86 / 0.0560 | 23.26 / 0.0973 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 21.6% | 22.80 / 0.0559 | 23.36 / 0.0897 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 21.6% | 22.83 / 0.0558 | 23.61 / 0.0888 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 21.5% | 22.81 / 0.0554 | 23.47 / 0.0879 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 21.6% | 22.90 / 0.0546 | 22.85 / 0.1082 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 21.7% | 22.86 / 0.0562 | 23.15 / 0.0994 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 21.7% | 22.90 / 0.0546 | 23.25 / 0.0996 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 21.6% | 22.90 / 0.0546 | 23.27 / 0.0981 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 21.7% | 22.75 / 0.0549 | 20.34 / 0.1401 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 23.2% | 23.21 / 0.0452 | 23.39 / 0.0830 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 23.3% | 23.16 / 0.0440 | 23.72 / 0.0721 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 23.2% | 23.17 / 0.0454 | 23.86 / 0.0763 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 23.2% | 23.16 / 0.0453 | 23.82 / 0.0737 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 23.0% | 23.18 / 0.0448 | 23.31 / 0.0856 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 23.1% | 23.16 / 0.0459 | 23.70 / 0.0775 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 23.0% | 23.16 / 0.0450 | 23.71 / 0.0779 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 23.0% | 23.17 / 0.0455 | 23.76 / 0.0771 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 23.6% | 23.30 / 0.0461 | 20.35 / 0.1426 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 18.7% | 23.23 / 0.0290 | 22.94 / 0.0802 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 20.5% | 23.42 / 0.0302 | 23.15 / 0.0800 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 19.4% | 23.34 / 0.0301 | 23.58 / 0.0797 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 19.8% | 23.38 / 0.0297 | 23.49 / 0.0804 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 19.0% | 23.26 / 0.0299 | 22.83 / 0.0826 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 20.5% | 23.45 / 0.0308 | 23.16 / 0.0780 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 19.7% | 23.37 / 0.0309 | 23.46 / 0.0792 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 20.1% | 23.41 / 0.0310 | 23.36 / 0.0794 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.03 / 0.0931 | 31.40 / 0.0806 | 16.75 / 0.0368 | 34.57 / 0.0266 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.53 / 0.1133 | 30.62 / 0.1002 | 18.69 / 0.0395 | 34.48 / 0.0295 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.72 / 0.1089 | 30.75 / 0.0981 | 18.81 / 0.0361 | 34.62 / 0.0288 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.85 / 0.1107 | 30.74 / 0.0986 | 19.08 / 0.0367 | 34.72 / 0.0290 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.73 / 0.1095 | 30.73 / 0.0982 | 18.85 / 0.0365 | 34.69 / 0.0288 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.30 / 0.1178 | 30.29 / 0.1042 | 18.63 / 0.0411 | 34.40 / 0.0296 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.54 / 0.1120 | 30.59 / 0.1014 | 18.79 / 0.0351 | 34.34 / 0.0295 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.60 / 0.1137 | 30.44 / 0.1020 | 19.03 / 0.0377 | 34.66 / 0.0292 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.60 / 0.1125 | 30.49 / 0.1013 | 19.01 / 0.0360 | 34.46 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.08 / 0.1265 | 30.85 / 0.1064 | 18.24 / 0.0460 | 33.77 / 0.0295 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.45 / 0.1135 | 30.64 / 0.0994 | 18.56 / 0.0393 | 34.32 / 0.0302 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.80 / 0.1061 | 30.95 / 0.0959 | 18.83 / 0.0343 | 34.62 / 0.0290 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.83 / 0.1085 | 30.87 / 0.0967 | 18.96 / 0.0356 | 34.72 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.79 / 0.1070 | 30.90 / 0.0959 | 18.83 / 0.0351 | 34.71 / 0.0289 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.48 / 0.1165 | 30.54 / 0.1024 | 18.73 / 0.0392 | 34.26 / 0.0303 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.82 / 0.1094 | 31.01 / 0.0987 | 18.94 / 0.0335 | 34.61 / 0.0289 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.86 / 0.1109 | 30.85 / 0.0994 | 19.10 / 0.0359 | 34.70 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.86 / 0.1099 | 30.94 / 0.0989 | 19.05 / 0.0349 | 34.65 / 0.0290 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.98 / 0.1301 | 30.76 / 0.1189 | 18.01 / 0.0453 | 32.38 / 0.0286 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.95 / 0.1405 | 30.05 / 0.1273 | 18.41 / 0.0408 | 34.25 / 0.0311 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.33 / 0.1322 | 29.94 / 0.1269 | 18.94 / 0.0347 | 34.53 / 0.0297 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.26 / 0.1369 | 30.01 / 0.1276 | 18.93 / 0.0381 | 34.61 / 0.0302 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.36 / 0.1348 | 29.92 / 0.1279 | 19.07 / 0.0363 | 34.58 / 0.0298 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.83 / 0.1418 | 29.87 / 0.1288 | 18.54 / 0.0407 | 34.33 / 0.0312 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.16 / 0.1338 | 29.94 / 0.1261 | 18.89 / 0.0360 | 34.58 / 0.0298 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.08 / 0.1387 | 30.00 / 0.1284 | 18.94 / 0.0375 | 34.60 / 0.0305 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.12 / 0.1368 | 29.80 / 0.1279 | 18.94 / 0.0369 | 34.60 / 0.0301 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.4%） | — | — | 28.03 / 0.0931 | 31.40 / 0.0806 | 34.57 |
| in035 | rife | 8.4% | 18.7% | 27.95 / 0.1405 | 30.05 / 0.1273 | 34.25 |
| in035 | cnw_cnn | 12.7% | 21.6% | 28.53 / 0.1133 | 30.62 / 0.1002 | 34.48 |
| in035 | cnw_f5 | 13.0% | 23.2% | 28.45 / 0.1135 | 30.64 / 0.0994 | 34.32 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.41 / 0.1036 | +0.01 / +0.0592 (core 8.7%) | +0.71 / +0.0167 (core 13.9%) | +0.55 / +0.0220 (core 14.6%) |
| in035 | 2 | 0-3 | 28.59 / 0.1014 | -1.00 / +0.0636 (core 8.7%) | -0.66 / +0.0299 (core 13.9%) | -0.63 / +0.0268 (core 14.6%) |
| in035 | 4 | 3-5 | 28.09 / 0.0742 | +0.73 / +0.0196 (core 5.5%) | +1.45 / +0.0141 (core 7.0%) | +1.33 / +0.0126 (core 6.8%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.03 / 0.0931 | 31.40 | 34.57 | — |
| in035 | cnw_cnn | 不复核 | —% | 28.53 / 0.1133 | 30.62 | 34.48 | 0/3 |
| in035 | cnw_cnn | oracle | 3.9% | 29.12 / 0.0949 | 31.29 | 34.56 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.72 / 0.1089 | 30.75 | 34.62 | 0/3 |
| in035 | cnw_cnn | oracle | 4.0% | 29.24 / 0.0923 | 31.42 | 34.57 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.85 / 0.1107 | 30.74 | 34.72 | 0/3 |
| in035 | cnw_cnn | oracle | 3.9% | 29.39 / 0.0930 | 31.41 | 34.57 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.73 / 0.1095 | 30.73 | 34.69 | 0/3 |
| in035 | cnw_cnn | oracle | 4.0% | 29.26 / 0.0925 | 31.41 | 34.57 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.30 / 0.1178 | 30.29 | 34.40 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.9% | 29.05 / 0.0967 | 31.23 | 34.55 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.54 / 0.1120 | 30.59 | 34.34 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.9% | 29.23 / 0.0925 | 31.54 | 34.55 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.60 / 0.1137 | 30.44 | 34.66 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.9% | 29.32 / 0.0943 | 31.39 | 34.56 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.60 / 0.1125 | 30.49 | 34.46 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.9% | 29.33 / 0.0933 | 31.47 | 34.56 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 28.08 / 0.1265 | 30.85 | 33.77 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 3.9% | 28.78 / 0.1030 | 31.69 | 34.39 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.45 / 0.1135 | 30.64 | 34.32 | 0/3 |
| in035 | cnw_f5 | oracle | 3.8% | 29.07 / 0.0950 | 31.39 | 34.56 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.80 / 0.1061 | 30.95 | 34.62 | 0/3 |
| in035 | cnw_f5 | oracle | 3.9% | 29.29 / 0.0912 | 31.59 | 34.56 | 2/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.83 / 0.1085 | 30.87 | 34.72 | 0/3 |
| in035 | cnw_f5 | oracle | 3.8% | 29.36 / 0.0922 | 31.54 | 34.57 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.79 / 0.1070 | 30.90 | 34.71 | 0/3 |
| in035 | cnw_f5 | oracle | 3.8% | 29.28 / 0.0913 | 31.55 | 34.56 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.48 / 0.1165 | 30.54 | 34.26 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.8% | 29.15 / 0.0954 | 31.40 | 34.55 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.82 / 0.1094 | 31.01 | 34.61 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.9% | 29.35 / 0.0917 | 31.68 | 34.56 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.86 / 0.1109 | 30.85 | 34.70 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.8% | 29.42 / 0.0928 | 31.56 | 34.56 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.86 / 0.1099 | 30.94 | 34.65 | 0/3 |
| in035 | cnw_f5_mw | oracle | 3.8% | 29.40 / 0.0925 | 31.62 | 34.56 | 1/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.98 / 0.1301 | 30.76 | 32.38 | 0/3 |
| in035 | cnw_f5_pix | oracle | 3.6% | 28.64 / 0.1028 | 31.50 | 34.55 | 0/3 |
| in035 | rife | 不复核 | —% | 27.95 / 0.1405 | 30.05 | 34.25 | 0/3 |
| in035 | rife | oracle | 3.4% | 28.97 / 0.1002 | 31.59 | 34.55 | 0/3 |
| in035 | rife | 不复核 | —% | 28.33 / 0.1322 | 29.94 | 34.53 | 0/3 |
| in035 | rife | oracle | 3.6% | 29.34 / 0.0950 | 31.87 | 34.54 | 1/3 |
| in035 | rife | 不复核 | —% | 28.26 / 0.1369 | 30.01 | 34.61 | 0/3 |
| in035 | rife | oracle | 3.5% | 29.33 / 0.0975 | 31.74 | 34.56 | 0/3 |
| in035 | rife | 不复核 | —% | 28.36 / 0.1348 | 29.92 | 34.58 | 0/3 |
| in035 | rife | oracle | 3.5% | 29.41 / 0.0962 | 31.81 | 34.55 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 27.83 / 0.1418 | 29.87 | 34.33 | 0/3 |
| in035 | rife_mw | oracle | 3.4% | 29.05 / 0.1000 | 31.63 | 34.56 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.16 / 0.1338 | 29.94 | 34.58 | 0/3 |
| in035 | rife_mw | oracle | 3.6% | 29.28 / 0.0958 | 31.85 | 34.55 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.08 / 0.1387 | 30.00 | 34.60 | 0/3 |
| in035 | rife_mw | oracle | 3.5% | 29.30 / 0.0974 | 31.76 | 34.56 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 28.12 / 0.1368 | 29.80 | 34.60 | 0/3 |
| in035 | rife_mw | oracle | 3.5% | 29.31 / 0.0965 | 31.81 | 34.55 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 28.03 / 0.0931 | 31.40 / 0.0806 | — |
| in035 | FF | 0（前馈） | 865×612（61%） | 31.15 | 28.53 / 0.1133 | 30.62 / 0.1002 | 0/3 |
| in035 | 25 | 1.01 s | 865×612（61%） | 32.69 | 28.85 / 0.1107 | 30.74 / 0.0986 | 0/3 |
| in035 | 50 | 2.03 s | 865×612（61%） | 33.17 | 28.73 / 0.1095 | 30.73 / 0.0982 | 0/3 |
| in035 | 100 | 4.08 s | 865×612（61%） | 33.61 | 28.72 / 0.1089 | 30.75 / 0.0981 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.03 / 0.0931 | 31.40 / 0.0806 | 34.57 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 28.53 / 0.1133 | 30.62 / 0.1002 | 34.48 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 29.12 / 0.0949 | 31.29 / 0.0838 | 34.56 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.85 / 0.1107 | 30.74 / 0.0986 | 34.72 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 29.39 / 0.0930 | 31.41 / 0.0830 | 34.57 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 28.73 / 0.1095 | 30.73 / 0.0982 | 34.69 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 29.26 / 0.0925 | 31.41 / 0.0829 | 34.57 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 28.72 / 0.1089 | 30.75 / 0.0981 | 34.62 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 29.24 / 0.0923 | 31.42 / 0.0829 | 34.57 | 2/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 28.30 / 0.1178 | 30.29 / 0.1042 | 34.40 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 29.05 / 0.0967 | 31.23 / 0.0850 | 34.55 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.60 / 0.1137 | 30.44 / 0.1020 | 34.66 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 29.32 / 0.0943 | 31.39 / 0.0841 | 34.56 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.60 / 0.1125 | 30.49 / 0.1013 | 34.46 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 29.33 / 0.0933 | 31.47 / 0.0833 | 34.56 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.54 / 0.1120 | 30.59 / 0.1014 | 34.34 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 29.23 / 0.0925 | 31.54 / 0.0827 | 34.55 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 28.45 / 0.1135 | 30.64 / 0.0994 | 34.32 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 29.07 / 0.0950 | 31.39 / 0.0837 | 34.56 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 28.83 / 0.1085 | 30.87 / 0.0967 | 34.72 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 29.36 / 0.0922 | 31.54 / 0.0825 | 34.57 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 28.79 / 0.1070 | 30.90 / 0.0959 | 34.71 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 29.28 / 0.0913 | 31.55 / 0.0824 | 34.56 | 2/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 28.80 / 0.1061 | 30.95 / 0.0959 | 34.62 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 29.29 / 0.0912 | 31.59 / 0.0824 | 34.56 | 2/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 28.48 / 0.1165 | 30.54 / 0.1024 | 34.26 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 29.15 / 0.0954 | 31.40 / 0.0840 | 34.55 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 28.86 / 0.1109 | 30.85 / 0.0994 | 34.70 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 29.42 / 0.0928 | 31.56 / 0.0829 | 34.56 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 28.86 / 0.1099 | 30.94 / 0.0989 | 34.65 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 29.40 / 0.0925 | 31.62 / 0.0827 | 34.56 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.82 / 0.1094 | 31.01 / 0.0987 | 34.61 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 29.35 / 0.0917 | 31.68 / 0.0824 | 34.56 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 27.95 / 0.1405 | 30.05 / 0.1273 | 34.25 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 28.97 / 0.1002 | 31.59 / 0.0853 | 34.55 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 28.26 / 0.1369 | 30.01 / 0.1276 | 34.61 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 29.33 / 0.0975 | 31.74 / 0.0847 | 34.56 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 28.36 / 0.1348 | 29.92 / 0.1279 | 34.58 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 29.41 / 0.0962 | 31.81 / 0.0845 | 34.55 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 28.33 / 0.1322 | 29.94 / 0.1269 | 34.53 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 29.34 / 0.0950 | 31.87 / 0.0839 | 34.54 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 27.83 / 0.1418 | 29.87 / 0.1288 | 34.33 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 29.05 / 0.1000 | 31.63 / 0.0845 | 34.56 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 28.08 / 0.1387 | 30.00 / 0.1284 | 34.60 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 29.30 / 0.0974 | 31.76 / 0.0838 | 34.56 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 28.12 / 0.1368 | 29.80 / 0.1279 | 34.60 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 29.31 / 0.0965 | 31.81 / 0.0840 | 34.55 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 28.16 / 0.1338 | 29.94 / 0.1261 | 34.58 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 29.28 / 0.0958 | 31.85 / 0.0837 | 34.55 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.40 / 0.0806 | 16.75 / 0.0368 | 34.57 / 0.0266 | 28.03 / 0.0931 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 87.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.40 | 0.8409 | 0.0806 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.90 | 0.6168 | 0.6428 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 5.95 | 0.6096 | 0.6378 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.92 | 0.6170 | 0.6396 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 5.93 | 0.6141 | 0.6377 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.89 | 0.6132 | 0.6464 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.94 | 0.6074 | 0.6402 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.91 | 0.6142 | 0.6423 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 5.92 | 0.6115 | 0.6403 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 9.34 | 0.2523 | 0.6087 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.08 | 0.6183 | 0.6291 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.19 | 0.6138 | 0.6232 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.12 | 0.6207 | 0.6262 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.15 | 0.6184 | 0.6233 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.12 | 0.6142 | 0.6347 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.21 | 0.6116 | 0.6251 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.15 | 0.6175 | 0.6305 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.17 | 0.6160 | 0.6282 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 9.93 | 0.2812 | 0.5930 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.61 | 0.6114 | 0.6520 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.63 | 0.6120 | 0.6423 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.61 | 0.6129 | 0.6500 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.62 | 0.6129 | 0.6460 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.60 | 0.6090 | 0.6536 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.64 | 0.6101 | 0.6426 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.61 | 0.6110 | 0.6514 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.62 | 0.6110 | 0.6468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 31.29 | 0.8400 | 0.0838 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.42 | 0.8400 | 0.0829 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.41 | 0.8403 | 0.0830 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.41 | 0.8401 | 0.0829 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.23 | 0.8395 | 0.0850 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.54 | 0.8409 | 0.0827 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.39 | 0.8404 | 0.0841 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.47 | 0.8407 | 0.0833 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 31.69 | 0.8438 | 0.0838 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 31.39 | 0.8400 | 0.0837 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.59 | 0.8407 | 0.0824 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.54 | 0.8407 | 0.0825 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.55 | 0.8406 | 0.0824 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.40 | 0.8399 | 0.0840 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.68 | 0.8412 | 0.0824 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.56 | 0.8408 | 0.0829 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.62 | 0.8410 | 0.0827 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 31.50 | 0.8426 | 0.0849 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.59 | 0.8412 | 0.0853 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.87 | 0.8426 | 0.0839 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.74 | 0.8419 | 0.0847 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.81 | 0.8424 | 0.0845 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 31.63 | 0.8414 | 0.0845 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.85 | 0.8424 | 0.0837 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.76 | 0.8421 | 0.0838 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.81 | 0.8423 | 0.0840 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 30.62 | 0.8375 | 0.1002 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.75 | 0.8361 | 0.0981 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.74 | 0.8377 | 0.0986 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.73 | 0.8370 | 0.0982 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.29 | 0.8354 | 0.1042 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.59 | 0.8358 | 0.1014 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.44 | 0.8364 | 0.1020 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.49 | 0.8363 | 0.1013 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 30.85 | 0.8411 | 0.1064 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 30.64 | 0.8346 | 0.0994 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.95 | 0.8357 | 0.0959 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.87 | 0.8366 | 0.0967 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.90 | 0.8364 | 0.0959 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.54 | 0.8330 | 0.1024 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.01 | 0.8356 | 0.0987 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.85 | 0.8360 | 0.0994 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.94 | 0.8364 | 0.0989 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 30.76 | 0.8379 | 0.1189 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.05 | 0.8300 | 0.1273 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.94 | 0.8308 | 0.1269 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 30.01 | 0.8312 | 0.1276 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.92 | 0.8312 | 0.1279 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.87 | 0.8291 | 0.1288 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.94 | 0.8307 | 0.1261 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.00 | 0.8315 | 0.1284 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.80 | 0.8309 | 0.1279 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 16.75 | 0.4562 | 0.0368 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 14.85 | 0.5304 | 0.0667 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 15.59 | 0.5372 | 0.0588 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 15.23 | 0.5453 | 0.0621 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 15.33 | 0.5390 | 0.0609 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 14.41 | 0.5081 | 0.0692 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 15.14 | 0.5266 | 0.0590 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 14.74 | 0.5338 | 0.0638 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 14.82 | 0.5311 | 0.0618 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 15.09 | 0.4551 | 0.0731 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 14.66 | 0.5187 | 0.0658 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 15.89 | 0.5298 | 0.0577 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 15.27 | 0.5355 | 0.0609 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 15.53 | 0.5309 | 0.0598 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 14.37 | 0.5136 | 0.0669 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 15.28 | 0.5268 | 0.0586 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.75 | 0.5339 | 0.0624 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.94 | 0.5315 | 0.0604 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.06 | 0.4653 | 0.0708 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.61 | 0.5200 | 0.0812 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 13.12 | 0.5516 | 0.0739 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.83 | 0.5418 | 0.0784 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.94 | 0.5459 | 0.0763 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.73 | 0.5157 | 0.0810 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 13.12 | 0.5403 | 0.0742 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 12.90 | 0.5351 | 0.0778 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 12.97 | 0.5386 | 0.0764 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.69 | 0.5553 | 0.0394 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.82 | 0.5621 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.09 | 0.5725 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.86 | 0.5648 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.64 | 0.5413 | 0.0410 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 18.81 | 0.5563 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.04 | 0.5653 | 0.0375 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.02 | 0.5627 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 18.25 | 0.5155 | 0.0456 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.58 | 0.5458 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.84 | 0.5574 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.98 | 0.5665 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.85 | 0.5602 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.75 | 0.5461 | 0.0390 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 18.96 | 0.5553 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.12 | 0.5680 | 0.0357 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.07 | 0.5628 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 18.01 | 0.5017 | 0.0453 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.41 | 0.5580 | 0.0407 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.93 | 0.5851 | 0.0347 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.93 | 0.5826 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 19.07 | 0.5866 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 18.54 | 0.5535 | 0.0401 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 18.89 | 0.5729 | 0.0358 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 18.94 | 0.5775 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 18.94 | 0.5773 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.69 | 0.5558 | 0.0395 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.81 | 0.5615 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.08 | 0.5719 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.85 | 0.5639 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.63 | 0.5410 | 0.0411 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 18.79 | 0.5550 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.03 | 0.5647 | 0.0377 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.01 | 0.5618 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 18.24 | 0.5111 | 0.0460 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.56 | 0.5459 | 0.0393 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.83 | 0.5566 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.96 | 0.5658 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.83 | 0.5595 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.73 | 0.5455 | 0.0392 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 18.94 | 0.5547 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.10 | 0.5674 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.05 | 0.5622 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 18.01 | 0.4969 | 0.0453 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.41 | 0.5565 | 0.0408 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.94 | 0.5842 | 0.0347 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.93 | 0.5817 | 0.0381 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 19.07 | 0.5857 | 0.0363 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 18.54 | 0.5523 | 0.0407 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 18.89 | 0.5717 | 0.0360 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 18.94 | 0.5761 | 0.0375 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 18.94 | 0.5761 | 0.0369 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 72.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.02 | 0.7941 | 0.0719 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.56 | 0.6006 | 0.4509 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.70 | 0.6037 | 0.4387 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.62 | 0.6118 | 0.4430 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.65 | 0.6089 | 0.4402 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.52 | 0.5955 | 0.4547 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.66 | 0.5985 | 0.4401 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.59 | 0.6073 | 0.4455 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.61 | 0.6041 | 0.4418 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.64 | 0.3516 | 0.4513 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 7.96 | 0.6121 | 0.4227 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.16 | 0.6165 | 0.4080 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.05 | 0.6257 | 0.4133 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.10 | 0.6227 | 0.4102 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 7.97 | 0.6079 | 0.4278 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.16 | 0.6119 | 0.4110 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.05 | 0.6214 | 0.4182 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.09 | 0.6187 | 0.4142 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.50 | 0.3920 | 0.4421 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.81 | 0.6051 | 0.4544 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.07 | 0.6171 | 0.4404 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.92 | 0.6192 | 0.4492 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.98 | 0.6197 | 0.4449 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.88 | 0.5999 | 0.4537 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.13 | 0.6120 | 0.4374 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.98 | 0.6149 | 0.4474 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.03 | 0.6152 | 0.4430 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.26 | 0.7990 | 0.0770 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.42 | 0.8023 | 0.0737 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.53 | 0.8027 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.42 | 0.8022 | 0.0737 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.18 | 0.7971 | 0.0776 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.36 | 0.8009 | 0.0739 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.45 | 0.8014 | 0.0753 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.45 | 0.8012 | 0.0743 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.54 | 0.7945 | 0.0874 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.20 | 0.7982 | 0.0768 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.46 | 0.8022 | 0.0739 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.50 | 0.8026 | 0.0742 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.44 | 0.8023 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.30 | 0.7984 | 0.0772 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.47 | 0.8013 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.54 | 0.8025 | 0.0750 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.51 | 0.8020 | 0.0744 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.38 | 0.7929 | 0.0904 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.12 | 0.7988 | 0.0813 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.55 | 0.8046 | 0.0778 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.51 | 0.8041 | 0.0794 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.61 | 0.8048 | 0.0786 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.16 | 0.7981 | 0.0811 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.47 | 0.8034 | 0.0774 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.45 | 0.8032 | 0.0785 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.48 | 0.8039 | 0.0779 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.20 | 0.7847 | 0.0984 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.44 | 0.7895 | 0.0945 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.53 | 0.7934 | 0.0945 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.46 | 0.7920 | 0.0937 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.92 | 0.7808 | 0.1018 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.21 | 0.7859 | 0.0963 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.20 | 0.7896 | 0.0970 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.25 | 0.7887 | 0.0961 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.01 | 0.7695 | 0.1313 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.09 | 0.7803 | 0.0994 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.48 | 0.7879 | 0.0927 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.48 | 0.7916 | 0.0936 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.47 | 0.7906 | 0.0922 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.08 | 0.7788 | 0.1025 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.41 | 0.7851 | 0.0951 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.37 | 0.7890 | 0.0967 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.43 | 0.7881 | 0.0954 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.61 | 0.7574 | 0.1589 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.71 | 0.7769 | 0.1230 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.70 | 0.7767 | 0.1237 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.02 | 0.7834 | 0.1231 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.93 | 0.7804 | 0.1231 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.62 | 0.7749 | 0.1241 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.70 | 0.7781 | 0.1209 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.01 | 0.7864 | 0.1209 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.87 | 0.7824 | 0.1205 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 54.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.02 | 0.8072 | 0.0660 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 7.84 | 0.6480 | 0.5018 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 7.91 | 0.6453 | 0.4923 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 7.88 | 0.6541 | 0.4968 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 7.90 | 0.6507 | 0.4942 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 7.82 | 0.6410 | 0.5052 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.89 | 0.6403 | 0.4935 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 7.86 | 0.6486 | 0.4981 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 7.87 | 0.6449 | 0.4956 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 10.77 | 0.4135 | 0.4881 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 8.15 | 0.6413 | 0.4849 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 8.30 | 0.6432 | 0.4714 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 8.21 | 0.6504 | 0.4777 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 8.25 | 0.6482 | 0.4743 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 8.13 | 0.6360 | 0.4881 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 8.27 | 0.6401 | 0.4738 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 8.19 | 0.6463 | 0.4813 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 8.22 | 0.6450 | 0.4774 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 11.74 | 0.4417 | 0.4648 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.07 | 0.6253 | 0.5138 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.12 | 0.6361 | 0.5010 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.09 | 0.6352 | 0.5092 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.10 | 0.6359 | 0.5060 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.08 | 0.6226 | 0.5144 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.13 | 0.6322 | 0.5009 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.11 | 0.6322 | 0.5091 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.12 | 0.6330 | 0.5057 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.34 | 0.8129 | 0.0667 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.49 | 0.8149 | 0.0639 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.67 | 0.8162 | 0.0647 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.51 | 0.8152 | 0.0642 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.25 | 0.8104 | 0.0686 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.48 | 0.8147 | 0.0642 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.59 | 0.8150 | 0.0660 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.59 | 0.8149 | 0.0650 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.91 | 0.8112 | 0.0748 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.24 | 0.8110 | 0.0675 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.51 | 0.8142 | 0.0635 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.60 | 0.8151 | 0.0647 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.51 | 0.8145 | 0.0637 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.35 | 0.8107 | 0.0678 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.59 | 0.8144 | 0.0639 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.67 | 0.8151 | 0.0652 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.65 | 0.8148 | 0.0649 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.73 | 0.8093 | 0.0751 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.13 | 0.8125 | 0.0722 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.57 | 0.8181 | 0.0672 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.56 | 0.8171 | 0.0696 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.66 | 0.8179 | 0.0683 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.22 | 0.8127 | 0.0723 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.51 | 0.8167 | 0.0681 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.53 | 0.8167 | 0.0696 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.54 | 0.8170 | 0.0688 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.67 | 0.8071 | 0.0806 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.88 | 0.8082 | 0.0759 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.01 | 0.8121 | 0.0775 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.88 | 0.8104 | 0.0764 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.47 | 0.8022 | 0.0843 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.74 | 0.8062 | 0.0780 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.80 | 0.8091 | 0.0794 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.79 | 0.8078 | 0.0785 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.32 | 0.8080 | 0.0868 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.51 | 0.7994 | 0.0833 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.93 | 0.8047 | 0.0755 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.96 | 0.8078 | 0.0781 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.91 | 0.8068 | 0.0765 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.55 | 0.7968 | 0.0854 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.96 | 0.8034 | 0.0783 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.00 | 0.8064 | 0.0797 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.00 | 0.8059 | 0.0787 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.13 | 0.8044 | 0.0858 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.16 | 0.7976 | 0.1023 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.65 | 0.8052 | 0.0934 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.59 | 0.8054 | 0.0980 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.70 | 0.8059 | 0.0959 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.14 | 0.7960 | 0.1030 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.54 | 0.8036 | 0.0948 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.50 | 0.8050 | 0.0998 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.54 | 0.8047 | 0.0978 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 37.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 34.57 | 0.8591 | 0.0266 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 9.17 | 0.7042 | 0.3063 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 9.21 | 0.6974 | 0.3048 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 9.18 | 0.7040 | 0.3060 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 9.21 | 0.7015 | 0.3050 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 9.26 | 0.7039 | 0.3073 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.32 | 0.6951 | 0.3060 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 9.28 | 0.7043 | 0.3065 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 9.29 | 0.6998 | 0.3060 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 12.57 | 0.3887 | 0.2796 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 15.76 | 0.7235 | 0.2877 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 15.99 | 0.7163 | 0.2852 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 16.43 | 0.7253 | 0.2866 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 16.28 | 0.7218 | 0.2856 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 15.75 | 0.7228 | 0.2885 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 16.03 | 0.7163 | 0.2852 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 16.45 | 0.7247 | 0.2874 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 16.23 | 0.7209 | 0.2864 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 15.80 | 0.4545 | 0.2630 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 15.51 | 0.7228 | 0.2842 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 15.73 | 0.7162 | 0.2804 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 16.15 | 0.7244 | 0.2827 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 16.11 | 0.7221 | 0.2812 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 15.53 | 0.7217 | 0.2849 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 15.94 | 0.7164 | 0.2824 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 16.14 | 0.7234 | 0.2836 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 16.18 | 0.7214 | 0.2828 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 34.56 | 0.8590 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 34.57 | 0.8591 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 34.57 | 0.8590 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 34.57 | 0.8591 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 34.55 | 0.8587 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 34.55 | 0.8589 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 34.56 | 0.8589 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 34.56 | 0.8589 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 34.39 | 0.8580 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 34.56 | 0.8588 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 34.56 | 0.8590 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 34.57 | 0.8590 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 34.56 | 0.8590 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 34.55 | 0.8586 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 34.56 | 0.8589 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 34.56 | 0.8589 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 34.56 | 0.8589 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 34.55 | 0.8588 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 34.55 | 0.8588 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 34.54 | 0.8588 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 34.56 | 0.8589 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 34.55 | 0.8588 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 34.56 | 0.8589 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 34.55 | 0.8589 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 34.56 | 0.8589 | 0.0266 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 34.55 | 0.8589 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 34.48 | 0.8642 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 34.62 | 0.8619 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 34.72 | 0.8642 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 34.69 | 0.8633 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 34.40 | 0.8634 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 34.34 | 0.8605 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 34.66 | 0.8637 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 34.46 | 0.8618 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 33.77 | 0.8640 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 34.32 | 0.8634 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 34.62 | 0.8615 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 34.72 | 0.8645 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 34.71 | 0.8633 | 0.0289 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 34.26 | 0.8631 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 34.61 | 0.8625 | 0.0289 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 34.70 | 0.8644 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 34.65 | 0.8633 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 32.38 | 0.8603 | 0.0286 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 34.25 | 0.8650 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 34.53 | 0.8632 | 0.0297 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 34.61 | 0.8655 | 0.0302 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 34.58 | 0.8646 | 0.0298 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 34.33 | 0.8651 | 0.0312 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 34.58 | 0.8647 | 0.0298 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 34.60 | 0.8664 | 0.0305 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 34.60 | 0.8659 | 0.0301 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.03 | 0.8219 | 0.0931 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.42 | 0.6275 | 0.5794 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.47 | 0.6229 | 0.5695 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.44 | 0.6306 | 0.5744 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.46 | 0.6276 | 0.5708 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.41 | 0.6229 | 0.5824 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.46 | 0.6196 | 0.5716 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.43 | 0.6271 | 0.5759 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.44 | 0.6239 | 0.5729 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 9.96 | 0.3135 | 0.5473 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.63 | 0.6295 | 0.5658 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.73 | 0.6268 | 0.5542 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.66 | 0.6345 | 0.5589 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.69 | 0.6318 | 0.5560 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.66 | 0.6257 | 0.5717 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.75 | 0.6245 | 0.5563 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.69 | 0.6314 | 0.5640 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.71 | 0.6292 | 0.5603 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 10.53 | 0.3430 | 0.5270 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.04 | 0.6189 | 0.5981 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.07 | 0.6220 | 0.5831 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.05 | 0.6236 | 0.5926 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.06 | 0.6231 | 0.5879 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.04 | 0.6169 | 0.5980 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.07 | 0.6194 | 0.5836 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.05 | 0.6216 | 0.5926 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.06 | 0.6211 | 0.5883 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.12 | 0.8249 | 0.0949 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.24 | 0.8259 | 0.0923 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.39 | 0.8267 | 0.0930 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.26 | 0.8262 | 0.0925 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.05 | 0.8235 | 0.0967 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.23 | 0.8259 | 0.0925 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.32 | 0.8260 | 0.0943 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.33 | 0.8260 | 0.0933 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.78 | 0.8241 | 0.1030 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.07 | 0.8241 | 0.0950 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.29 | 0.8258 | 0.0912 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.36 | 0.8264 | 0.0922 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.28 | 0.8260 | 0.0913 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.15 | 0.8239 | 0.0954 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.35 | 0.8260 | 0.0917 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.42 | 0.8264 | 0.0928 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.40 | 0.8262 | 0.0925 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.64 | 0.8232 | 0.1028 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.97 | 0.8250 | 0.1002 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.34 | 0.8280 | 0.0950 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 29.33 | 0.8275 | 0.0975 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.41 | 0.8280 | 0.0962 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 29.05 | 0.8251 | 0.1000 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 29.28 | 0.8273 | 0.0958 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 29.30 | 0.8273 | 0.0974 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 29.31 | 0.8275 | 0.0965 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.53 | 0.8221 | 0.1133 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.72 | 0.8222 | 0.1089 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.85 | 0.8248 | 0.1107 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.73 | 0.8237 | 0.1095 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.30 | 0.8190 | 0.1178 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.54 | 0.8208 | 0.1120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.60 | 0.8227 | 0.1137 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.60 | 0.8219 | 0.1125 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.08 | 0.8205 | 0.1265 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.45 | 0.8183 | 0.1135 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.80 | 0.8208 | 0.1061 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.83 | 0.8229 | 0.1085 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.79 | 0.8222 | 0.1070 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.48 | 0.8168 | 0.1165 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.82 | 0.8202 | 0.1094 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.86 | 0.8221 | 0.1109 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.86 | 0.8217 | 0.1099 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.98 | 0.8187 | 0.1301 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.95 | 0.8156 | 0.1405 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.33 | 0.8194 | 0.1322 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.26 | 0.8198 | 0.1369 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.36 | 0.8200 | 0.1348 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.83 | 0.8144 | 0.1418 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.16 | 0.8183 | 0.1338 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.08 | 0.8193 | 0.1387 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.12 | 0.8190 | 0.1368 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 904 | None | classic | 1.22 | False | 180106 | 0.329 | 75.6 | 32.01 | 0.35 | 0.022 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 904 | None | classic | 1.22 | False | 180106 | 0.329 | 50.8 | 32.01 | 0.35 | 0.022 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 904 | None | classic | 1.22 | False | 180106 | 0.329 | 56.8 | 32.01 | 0.35 | 0.022 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 904 | None | classic | 1.22 | False | 180106 | 0.329 | 70.2 | 32.01 | 0.35 | 0.022 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 872 | None | classic | 1.14 | False | 167203 | 0.330 | 56.4 | 31.56 | 0.27 | 0.007 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 872 | None | classic | 1.14 | False | 167203 | 0.330 | 69.0 | 31.56 | 0.27 | 0.007 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 872 | None | classic | 1.14 | False | 167203 | 0.330 | 60.7 | 31.56 | 0.27 | 0.007 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 872 | None | classic | 1.14 | False | 167203 | 0.330 | 64.0 | 31.56 | 0.27 | 0.007 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 932387 | 0.802 | 455.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 904 | None | classic | 1.22 | False | 180060 | 0.329 | 57.6 | 31.98 | 0.33 | 0.018 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 904 | None | classic | 1.22 | False | 180060 | 0.329 | 46.4 | 31.98 | 0.33 | 0.018 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 904 | None | classic | 1.22 | False | 180060 | 0.329 | 45.8 | 31.98 | 0.33 | 0.018 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 904 | None | classic | 1.22 | False | 180060 | 0.329 | 51.1 | 31.98 | 0.33 | 0.018 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 872 | None | classic | 1.14 | False | 168182 | 0.327 | 80.6 | 31.59 | 0.26 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 872 | None | classic | 1.14 | False | 168182 | 0.327 | 77.9 | 31.59 | 0.26 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 872 | None | classic | 1.14 | False | 168182 | 0.327 | 70.5 | 31.59 | 0.26 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 872 | None | classic | 1.14 | False | 168182 | 0.327 | 67.7 | 31.59 | 0.26 | 0.007 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1158711 | 0.802 | 108.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1067 | None | classic | 1.70 | False | 219367 | 0.858 | 81.5 | 32.86 | 0.25 | 0.010 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1067 | None | classic | 1.70 | False | 219367 | 0.858 | 57.6 | 32.86 | 0.25 | 0.010 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1067 | None | classic | 1.70 | False | 219367 | 0.858 | 84.2 | 32.86 | 0.25 | 0.010 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1067 | None | classic | 1.70 | False | 219367 | 0.858 | 58.0 | 32.86 | 0.25 | 0.010 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1035 | None | classic | 1.60 | False | 206370 | 0.327 | 71.8 | 32.68 | 0.21 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1035 | None | classic | 1.60 | False | 206370 | 0.327 | 66.5 | 32.68 | 0.21 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1035 | None | classic | 1.60 | False | 206370 | 0.327 | 50.5 | 32.68 | 0.21 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1035 | None | classic | 1.60 | False | 206370 | 0.327 | 60.1 | 32.68 | 0.21 | 0.005 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.879 | 0.028 |
| in035 | mask_ent | 0.756 | 0.028 |
| in035 | mask_grad | 0.506 | 0.028 |
| in035 | r_col | 0.774 | 0.028 |
| in035 | r_warp | 0.888 | 0.028 |

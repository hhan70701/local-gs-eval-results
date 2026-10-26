# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 46.8% | 23.59 / 0.0759 | 23.08 / 0.1455 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 47.4% | 23.49 / 0.0764 | 23.89 / 0.1168 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 47.1% | 23.52 / 0.0763 | 23.87 / 0.1303 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 47.2% | 23.53 / 0.0767 | 23.92 / 0.1231 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 46.8% | 23.59 / 0.0759 | 23.08 / 0.1455 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 47.4% | 23.49 / 0.0763 | 23.89 / 0.1168 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 47.1% | 23.52 / 0.0763 | 23.87 / 0.1303 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 47.2% | 23.53 / 0.0767 | 23.92 / 0.1231 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 47.9% | 23.11 / 0.0782 | 23.97 / 0.1258 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 47.7% | 23.52 / 0.0777 | 23.07 / 0.1507 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 48.3% | 23.41 / 0.0794 | 23.67 / 0.1231 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 48.0% | 23.46 / 0.0783 | 23.70 / 0.1385 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 48.1% | 23.46 / 0.0788 | 23.75 / 0.1296 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 47.7% | 23.52 / 0.0777 | 23.07 / 0.1507 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 48.3% | 23.41 / 0.0794 | 23.67 / 0.1232 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 48.0% | 23.46 / 0.0783 | 23.70 / 0.1385 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 48.1% | 23.46 / 0.0788 | 23.75 / 0.1296 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 48.4% | 23.22 / 0.0802 | 23.89 / 0.1274 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 41.8% | 23.68 / 0.0785 | 23.45 / 0.1623 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 43.0% | 23.71 / 0.0800 | 23.74 / 0.1287 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 42.3% | 23.70 / 0.0788 | 23.90 / 0.1449 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 42.5% | 23.72 / 0.0791 | 23.85 / 0.1317 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 41.8% | 23.68 / 0.0785 | 23.45 / 0.1623 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 43.0% | 23.71 / 0.0800 | 23.74 / 0.1287 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 42.3% | 23.70 / 0.0788 | 23.90 / 0.1449 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 42.5% | 23.72 / 0.0791 | 23.85 / 0.1317 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 25.66 / 0.1132 | 26.75 / 0.1238 | 17.16 / 0.0514 | 30.07 / 0.0246 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.42 / 0.1738 | 26.95 / 0.1821 | 18.38 / 0.0555 | 29.61 / 0.0292 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.99 / 0.1485 | 27.29 / 0.1574 | 18.97 / 0.0470 | 30.01 / 0.0271 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.95 / 0.1609 | 27.24 / 0.1703 | 18.89 / 0.0504 | 29.98 / 0.0277 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.00 / 0.1542 | 27.27 / 0.1630 | 18.96 / 0.0486 | 29.98 / 0.0273 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.42 / 0.1738 | 26.95 / 0.1821 | 18.38 / 0.0555 | 29.61 / 0.0292 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.99 / 0.1485 | 27.29 / 0.1574 | 18.97 / 0.0470 | 30.01 / 0.0271 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.95 / 0.1609 | 27.24 / 0.1703 | 18.89 / 0.0504 | 29.98 / 0.0277 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.00 / 0.1542 | 27.27 / 0.1630 | 18.96 / 0.0486 | 29.98 / 0.0273 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.36 / 0.1389 | 28.49 / 0.1332 | 19.96 / 0.0499 | 30.14 / 0.0262 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.51 / 0.1772 | 27.28 / 0.1817 | 18.64 / 0.0581 | 28.97 / 0.0298 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.97 / 0.1524 | 27.58 / 0.1572 | 19.08 / 0.0506 | 29.31 / 0.0272 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.97 / 0.1651 | 27.52 / 0.1697 | 19.01 / 0.0539 | 29.26 / 0.0281 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.00 / 0.1576 | 27.55 / 0.1623 | 19.07 / 0.0522 | 29.25 / 0.0276 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.51 / 0.1772 | 27.28 / 0.1817 | 18.64 / 0.0581 | 28.97 / 0.0298 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.97 / 0.1525 | 27.58 / 0.1572 | 19.08 / 0.0506 | 29.31 / 0.0272 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.97 / 0.1651 | 27.52 / 0.1697 | 19.01 / 0.0539 | 29.26 / 0.0281 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.00 / 0.1576 | 27.55 / 0.1623 | 19.07 / 0.0522 | 29.25 / 0.0276 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.15 / 0.1401 | 28.26 / 0.1339 | 19.75 / 0.0516 | 29.98 / 0.0255 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 25.51 / 0.1849 | 26.85 / 0.2123 | 18.16 / 0.0580 | 30.09 / 0.0284 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.68 / 0.1562 | 27.11 / 0.1701 | 18.34 / 0.0542 | 30.22 / 0.0272 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.75 / 0.1709 | 27.15 / 0.1902 | 18.33 / 0.0553 | 30.26 / 0.0275 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.73 / 0.1610 | 27.14 / 0.1750 | 18.36 / 0.0548 | 30.24 / 0.0273 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.51 / 0.1849 | 26.85 / 0.2123 | 18.16 / 0.0580 | 30.09 / 0.0284 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.68 / 0.1562 | 27.11 / 0.1702 | 18.34 / 0.0543 | 30.22 / 0.0272 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.75 / 0.1709 | 27.15 / 0.1902 | 18.33 / 0.0553 | 30.26 / 0.0275 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.73 / 0.1610 | 27.14 / 0.1750 | 18.36 / 0.0548 | 30.24 / 0.0273 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 10.6%） | — | — | 25.66 / 0.1132 | 26.75 / 0.1238 | 30.07 |
| in035 | rife | 35.3% | 41.8% | 25.51 / 0.1849 | 26.85 / 0.2123 | 30.09 |
| in035 | cnw_cnn | 37.0% | 46.8% | 25.42 / 0.1738 | 26.95 / 0.1821 | 29.61 |
| in035 | cnw_f5 | 37.4% | 47.7% | 25.51 / 0.1772 | 27.28 / 0.1817 | 28.97 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 24.76 / 0.1172 | -0.18 / +0.0896 (core 47.9%) | +0.05 / +0.0724 (core 49.7%) | +0.29 / +0.0734 (core 48.7%) |
| in035 | 2 | 0-3 | 25.28 / 0.1154 | +0.06 / +0.0984 (core 47.9%) | -0.06 / +0.0850 (core 49.7%) | +0.20 / +0.0863 (core 48.7%) |
| in035 | 4 | 3-5 | 26.94 / 0.1070 | -0.33 / +0.0270 (core 6.7%) | -0.71 / +0.0245 (core 9.6%) | -0.94 / +0.0325 (core 12.8%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 25.66 / 0.1132 | 26.75 | 30.07 | — |
| in035 | cnw_cnn | 不复核 | —% | 25.42 / 0.1738 | 26.95 | 29.61 | 0/3 |
| in035 | cnw_cnn | oracle | 8.1% | 26.23 / 0.1224 | 27.85 | 29.95 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 25.99 / 0.1485 | 27.29 | 30.01 | 0/3 |
| in035 | cnw_cnn | oracle | 8.3% | 26.72 / 0.1123 | 28.06 | 30.07 | 2/3 |
| in035 | cnw_cnn | 不复核 | —% | 25.95 / 0.1609 | 27.24 | 29.98 | 0/3 |
| in035 | cnw_cnn | oracle | 8.2% | 26.65 / 0.1171 | 28.04 | 30.06 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.00 / 0.1542 | 27.27 | 29.98 | 0/3 |
| in035 | cnw_cnn | oracle | 8.3% | 26.70 / 0.1149 | 28.06 | 30.06 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.42 / 0.1738 | 26.95 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 8.1% | 26.23 / 0.1224 | 27.85 | 29.95 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.99 / 0.1485 | 27.29 | 30.01 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 8.3% | 26.72 / 0.1123 | 28.05 | 30.07 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 25.95 / 0.1609 | 27.24 | 29.98 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 8.2% | 26.65 / 0.1171 | 28.04 | 30.06 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.00 / 0.1542 | 27.27 | 29.98 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 8.3% | 26.70 / 0.1149 | 28.06 | 30.06 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.36 / 0.1389 | 28.49 | 30.14 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 8.7% | 27.52 / 0.1150 | 28.58 | 30.07 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.51 / 0.1772 | 27.28 | 28.97 | 0/3 |
| in035 | cnw_f5 | oracle | 8.3% | 26.39 / 0.1249 | 28.26 | 29.95 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.97 / 0.1524 | 27.58 | 29.31 | 0/3 |
| in035 | cnw_f5 | oracle | 8.5% | 26.77 / 0.1161 | 28.40 | 30.07 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 25.97 / 0.1651 | 27.52 | 29.26 | 0/3 |
| in035 | cnw_f5 | oracle | 8.4% | 26.71 / 0.1203 | 28.35 | 30.06 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.00 / 0.1576 | 27.55 | 29.25 | 0/3 |
| in035 | cnw_f5 | oracle | 8.4% | 26.76 / 0.1180 | 28.37 | 30.06 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.51 / 0.1772 | 27.28 | 28.97 | 0/3 |
| in035 | cnw_f5_mw | oracle | 8.3% | 26.39 / 0.1249 | 28.26 | 29.95 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.97 / 0.1525 | 27.58 | 29.31 | 0/3 |
| in035 | cnw_f5_mw | oracle | 8.5% | 26.77 / 0.1162 | 28.40 | 30.07 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 25.97 / 0.1651 | 27.52 | 29.26 | 0/3 |
| in035 | cnw_f5_mw | oracle | 8.4% | 26.71 / 0.1203 | 28.35 | 30.06 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.00 / 0.1576 | 27.55 | 29.25 | 0/3 |
| in035 | cnw_f5_mw | oracle | 8.4% | 26.76 / 0.1180 | 28.37 | 30.06 | 1/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.15 / 0.1401 | 28.26 | 29.98 | 0/3 |
| in035 | cnw_f5_pix | oracle | 8.6% | 27.39 / 0.1162 | 28.36 | 30.07 | 1/3 |
| in035 | rife | 不复核 | —% | 25.51 / 0.1849 | 26.85 | 30.09 | 0/3 |
| in035 | rife | oracle | 6.2% | 26.16 / 0.1225 | 27.62 | 30.06 | 0/3 |
| in035 | rife | 不复核 | —% | 25.68 / 0.1562 | 27.11 | 30.22 | 0/3 |
| in035 | rife | oracle | 6.5% | 26.32 / 0.1170 | 27.72 | 30.07 | 0/3 |
| in035 | rife | 不复核 | —% | 25.75 / 0.1709 | 27.15 | 30.26 | 0/3 |
| in035 | rife | oracle | 6.3% | 26.32 / 0.1202 | 27.77 | 30.06 | 0/3 |
| in035 | rife | 不复核 | —% | 25.73 / 0.1610 | 27.14 | 30.24 | 0/3 |
| in035 | rife | oracle | 6.4% | 26.33 / 0.1183 | 27.75 | 30.06 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.51 / 0.1849 | 26.85 | 30.09 | 0/3 |
| in035 | rife_mw | oracle | 6.2% | 26.16 / 0.1225 | 27.62 | 30.06 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.68 / 0.1562 | 27.11 | 30.22 | 0/3 |
| in035 | rife_mw | oracle | 6.5% | 26.32 / 0.1170 | 27.72 | 30.07 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.75 / 0.1709 | 27.15 | 30.26 | 0/3 |
| in035 | rife_mw | oracle | 6.3% | 26.32 / 0.1202 | 27.77 | 30.06 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.73 / 0.1610 | 27.14 | 30.24 | 0/3 |
| in035 | rife_mw | oracle | 6.4% | 26.33 / 0.1183 | 27.75 | 30.06 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 25.66 / 0.1132 | 26.75 / 0.1238 | — |
| in035 | FF | 0（前馈） | 1008×667（64%） | 30.64 | 25.42 / 0.1738 | 26.95 / 0.1821 | 0/3 |
| in035 | 25 | 0.78 s | 1008×667（64%） | 32.85 | 25.95 / 0.1609 | 27.24 / 0.1703 | 0/3 |
| in035 | 50 | 1.53 s | 1008×667（64%） | 33.72 | 26.00 / 0.1542 | 27.27 / 0.1630 | 0/3 |
| in035 | 100 | 3.00 s | 1008×667（64%） | 34.50 | 25.99 / 0.1485 | 27.29 / 0.1574 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 25.66 / 0.1132 | 26.75 / 0.1238 | 30.07 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 25.42 / 0.1738 | 26.95 / 0.1821 | 29.61 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 26.23 / 0.1224 | 27.85 / 0.1249 | 29.95 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 25.95 / 0.1609 | 27.24 / 0.1703 | 29.98 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 26.65 / 0.1171 | 28.04 / 0.1224 | 30.06 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 26.00 / 0.1542 | 27.27 / 0.1630 | 29.98 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 26.70 / 0.1149 | 28.06 / 0.1213 | 30.06 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 25.99 / 0.1485 | 27.29 / 0.1574 | 30.01 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 26.72 / 0.1123 | 28.06 / 0.1202 | 30.07 | 2/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 25.42 / 0.1738 | 26.95 / 0.1821 | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 26.23 / 0.1224 | 27.85 / 0.1249 | 29.95 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 25.95 / 0.1609 | 27.24 / 0.1703 | 29.98 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 26.65 / 0.1171 | 28.04 / 0.1224 | 30.06 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 26.00 / 0.1542 | 27.27 / 0.1630 | 29.98 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 26.70 / 0.1149 | 28.06 / 0.1213 | 30.06 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 25.99 / 0.1485 | 27.29 / 0.1574 | 30.01 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 26.72 / 0.1123 | 28.05 / 0.1202 | 30.07 | 2/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 25.51 / 0.1772 | 27.28 / 0.1817 | 28.97 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 26.39 / 0.1249 | 28.26 / 0.1255 | 29.95 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 25.97 / 0.1651 | 27.52 / 0.1697 | 29.26 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 26.71 / 0.1203 | 28.35 / 0.1227 | 30.06 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.00 / 0.1576 | 27.55 / 0.1623 | 29.25 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 26.76 / 0.1180 | 28.37 / 0.1217 | 30.06 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 25.97 / 0.1524 | 27.58 / 0.1572 | 29.31 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 26.77 / 0.1161 | 28.40 / 0.1210 | 30.07 | 1/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 25.51 / 0.1772 | 27.28 / 0.1817 | 28.97 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 26.39 / 0.1249 | 28.26 / 0.1255 | 29.95 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 25.97 / 0.1651 | 27.52 / 0.1697 | 29.26 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 26.71 / 0.1203 | 28.35 / 0.1227 | 30.06 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.00 / 0.1576 | 27.55 / 0.1623 | 29.25 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 26.76 / 0.1180 | 28.37 / 0.1218 | 30.06 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 25.97 / 0.1525 | 27.58 / 0.1572 | 29.31 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 26.77 / 0.1162 | 28.40 / 0.1210 | 30.07 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 25.51 / 0.1849 | 26.85 / 0.2123 | 30.09 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 26.16 / 0.1225 | 27.62 / 0.1263 | 30.06 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 25.75 / 0.1709 | 27.15 / 0.1902 | 30.26 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 26.32 / 0.1202 | 27.77 / 0.1240 | 30.06 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 25.73 / 0.1610 | 27.14 / 0.1750 | 30.24 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 26.33 / 0.1183 | 27.75 / 0.1227 | 30.06 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 25.68 / 0.1562 | 27.11 / 0.1701 | 30.22 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 26.32 / 0.1170 | 27.72 / 0.1229 | 30.07 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 25.51 / 0.1849 | 26.85 / 0.2123 | 30.09 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 26.16 / 0.1225 | 27.62 / 0.1263 | 30.06 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 25.75 / 0.1709 | 27.15 / 0.1902 | 30.26 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 26.32 / 0.1202 | 27.77 / 0.1240 | 30.06 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 25.73 / 0.1610 | 27.14 / 0.1750 | 30.24 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 26.33 / 0.1183 | 27.75 / 0.1227 | 30.06 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 25.68 / 0.1562 | 27.11 / 0.1702 | 30.22 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 26.32 / 0.1170 | 27.72 / 0.1229 | 30.07 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.75 / 0.1238 | 17.16 / 0.0514 | 30.07 / 0.0246 | 25.66 / 0.1132 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 55.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.75 | 0.7927 | 0.1238 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 13.23 | 0.7484 | 0.4394 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 13.43 | 0.7477 | 0.4015 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 13.30 | 0.7538 | 0.4171 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 13.32 | 0.7514 | 0.4069 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 13.23 | 0.7484 | 0.4394 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.43 | 0.7477 | 0.4015 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 13.30 | 0.7538 | 0.4171 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 13.32 | 0.7514 | 0.4069 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 16.57 | 0.6334 | 0.3706 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 13.07 | 0.7435 | 0.4491 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 13.34 | 0.7434 | 0.4103 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 13.23 | 0.7493 | 0.4277 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 13.28 | 0.7469 | 0.4158 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 13.07 | 0.7435 | 0.4491 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 13.34 | 0.7434 | 0.4103 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 13.23 | 0.7493 | 0.4276 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 13.28 | 0.7469 | 0.4158 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 16.26 | 0.6151 | 0.3782 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.79 | 0.7270 | 0.4769 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 10.88 | 0.7246 | 0.4267 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 10.83 | 0.7317 | 0.4500 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 10.84 | 0.7290 | 0.4331 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 10.79 | 0.7270 | 0.4769 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 10.88 | 0.7246 | 0.4267 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 10.83 | 0.7317 | 0.4500 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 10.84 | 0.7290 | 0.4331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.85 | 0.8106 | 0.1249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.06 | 0.8123 | 0.1202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.04 | 0.8128 | 0.1224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.06 | 0.8126 | 0.1213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.85 | 0.8106 | 0.1249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.05 | 0.8123 | 0.1202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.04 | 0.8128 | 0.1224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.06 | 0.8126 | 0.1213 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.58 | 0.8177 | 0.1119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.26 | 0.8102 | 0.1255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.40 | 0.8112 | 0.1210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.35 | 0.8120 | 0.1227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.37 | 0.8116 | 0.1217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.26 | 0.8102 | 0.1255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.40 | 0.8112 | 0.1210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.35 | 0.8120 | 0.1227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.37 | 0.8116 | 0.1218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.36 | 0.8153 | 0.1132 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.62 | 0.8045 | 0.1263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.72 | 0.8054 | 0.1229 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.77 | 0.8065 | 0.1240 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.75 | 0.8061 | 0.1227 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.62 | 0.8045 | 0.1263 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.72 | 0.8054 | 0.1229 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.77 | 0.8065 | 0.1240 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.75 | 0.8061 | 0.1227 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.95 | 0.8238 | 0.1821 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.29 | 0.8236 | 0.1574 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.24 | 0.8274 | 0.1703 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.27 | 0.8260 | 0.1630 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.95 | 0.8238 | 0.1821 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.29 | 0.8236 | 0.1574 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.24 | 0.8274 | 0.1703 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.27 | 0.8260 | 0.1630 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 28.49 | 0.8305 | 0.1332 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.28 | 0.8222 | 0.1817 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.58 | 0.8222 | 0.1572 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.52 | 0.8258 | 0.1697 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.55 | 0.8243 | 0.1623 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.28 | 0.8222 | 0.1817 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.58 | 0.8222 | 0.1572 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.52 | 0.8258 | 0.1697 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.55 | 0.8243 | 0.1623 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 28.26 | 0.8272 | 0.1339 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.85 | 0.8188 | 0.2123 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.11 | 0.8176 | 0.1701 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.15 | 0.8231 | 0.1902 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.14 | 0.8213 | 0.1750 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.85 | 0.8188 | 0.2123 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.11 | 0.8176 | 0.1702 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.15 | 0.8231 | 0.1902 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.14 | 0.8213 | 0.1750 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 10.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.16 | 0.4793 | 0.0514 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 14.13 | 0.6007 | 0.0841 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 14.59 | 0.6306 | 0.0728 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 14.52 | 0.6287 | 0.0774 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 14.45 | 0.6297 | 0.0753 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 14.13 | 0.6007 | 0.0841 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 14.59 | 0.6306 | 0.0728 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 14.52 | 0.6287 | 0.0774 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 14.45 | 0.6297 | 0.0753 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 18.40 | 0.6593 | 0.0691 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 15.00 | 0.6039 | 0.0863 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 15.93 | 0.6346 | 0.0737 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 15.60 | 0.6286 | 0.0793 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 15.71 | 0.6310 | 0.0766 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 15.00 | 0.6039 | 0.0863 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 15.93 | 0.6346 | 0.0737 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 15.60 | 0.6286 | 0.0793 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 15.71 | 0.6310 | 0.0766 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.27 | 0.6569 | 0.0681 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.05 | 0.5141 | 0.1169 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.57 | 0.5288 | 0.1059 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.32 | 0.5292 | 0.1111 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.40 | 0.5285 | 0.1088 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.05 | 0.5141 | 0.1169 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 12.57 | 0.5288 | 0.1059 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 12.32 | 0.5292 | 0.1111 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 12.40 | 0.5285 | 0.1088 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 18.38 | 0.6261 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.97 | 0.6512 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.89 | 0.6508 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.96 | 0.6514 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.38 | 0.6261 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 18.97 | 0.6512 | 0.0468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 18.89 | 0.6508 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 18.96 | 0.6514 | 0.0485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.97 | 0.6867 | 0.0497 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.64 | 0.6257 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.09 | 0.6438 | 0.0504 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.01 | 0.6442 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.07 | 0.6442 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.64 | 0.6257 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.08 | 0.6438 | 0.0505 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.01 | 0.6442 | 0.0537 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.07 | 0.6441 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.75 | 0.6734 | 0.0515 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.17 | 0.5919 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.35 | 0.5986 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.34 | 0.6022 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.36 | 0.6011 | 0.0545 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 18.17 | 0.5919 | 0.0578 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 18.35 | 0.5985 | 0.0540 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 18.35 | 0.6022 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 18.36 | 0.6011 | 0.0545 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 18.38 | 0.6266 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 18.97 | 0.6512 | 0.0470 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.89 | 0.6510 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 18.96 | 0.6515 | 0.0486 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 18.38 | 0.6266 | 0.0555 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 18.97 | 0.6512 | 0.0470 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 18.89 | 0.6510 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 18.96 | 0.6514 | 0.0486 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.96 | 0.6854 | 0.0499 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.64 | 0.6258 | 0.0581 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 19.08 | 0.6432 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 19.01 | 0.6440 | 0.0539 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 19.07 | 0.6438 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.64 | 0.6258 | 0.0581 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 19.08 | 0.6431 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.01 | 0.6440 | 0.0539 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 19.07 | 0.6438 | 0.0522 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.75 | 0.6721 | 0.0516 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.16 | 0.5917 | 0.0580 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.34 | 0.5978 | 0.0542 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.33 | 0.6020 | 0.0553 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.36 | 0.6006 | 0.0548 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 18.16 | 0.5917 | 0.0580 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 18.34 | 0.5978 | 0.0543 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 18.33 | 0.6020 | 0.0553 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 18.36 | 0.6006 | 0.0548 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 81.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.96 | 0.7294 | 0.0942 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 12.72 | 0.6868 | 0.3133 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 13.08 | 0.6956 | 0.2774 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 12.91 | 0.7015 | 0.2950 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 12.95 | 0.6995 | 0.2853 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 12.72 | 0.6868 | 0.3133 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.08 | 0.6956 | 0.2775 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 12.91 | 0.7015 | 0.2950 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 12.95 | 0.6995 | 0.2853 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.88 | 0.6314 | 0.2574 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 12.65 | 0.6916 | 0.3166 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 13.10 | 0.7006 | 0.2780 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.88 | 0.7059 | 0.2974 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.96 | 0.7039 | 0.2867 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 12.65 | 0.6916 | 0.3166 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 13.10 | 0.7006 | 0.2780 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 12.88 | 0.7059 | 0.2974 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 12.96 | 0.7039 | 0.2867 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.87 | 0.6330 | 0.2572 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.82 | 0.6463 | 0.3673 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 10.05 | 0.6511 | 0.3289 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.92 | 0.6582 | 0.3492 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.96 | 0.6554 | 0.3374 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 9.82 | 0.6463 | 0.3673 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 10.05 | 0.6511 | 0.3289 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.92 | 0.6582 | 0.3492 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.96 | 0.6554 | 0.3374 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.58 | 0.7450 | 0.1053 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.09 | 0.7517 | 0.0959 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.00 | 0.7511 | 0.1006 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.07 | 0.7516 | 0.0984 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.58 | 0.7450 | 0.1053 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.09 | 0.7517 | 0.0959 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.00 | 0.7511 | 0.1006 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.07 | 0.7516 | 0.0984 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.69 | 0.7551 | 0.1022 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.68 | 0.7438 | 0.1075 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.06 | 0.7492 | 0.0987 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.00 | 0.7490 | 0.1032 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.05 | 0.7492 | 0.1008 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.68 | 0.7438 | 0.1075 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.06 | 0.7491 | 0.0988 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.00 | 0.7490 | 0.1032 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.05 | 0.7492 | 0.1009 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.57 | 0.7530 | 0.1037 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.47 | 0.7401 | 0.1041 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.63 | 0.7426 | 0.0987 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.64 | 0.7432 | 0.1019 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.65 | 0.7431 | 0.0999 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.47 | 0.7401 | 0.1041 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.63 | 0.7426 | 0.0987 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.64 | 0.7432 | 0.1019 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.65 | 0.7431 | 0.0999 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.69 | 0.7532 | 0.1542 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.30 | 0.7606 | 0.1304 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.26 | 0.7638 | 0.1421 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.30 | 0.7630 | 0.1355 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.69 | 0.7532 | 0.1542 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.30 | 0.7606 | 0.1304 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.26 | 0.7638 | 0.1421 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.30 | 0.7630 | 0.1356 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.53 | 0.7548 | 0.1403 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.77 | 0.7517 | 0.1569 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.25 | 0.7578 | 0.1332 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.24 | 0.7614 | 0.1457 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.28 | 0.7602 | 0.1384 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.77 | 0.7517 | 0.1569 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.25 | 0.7577 | 0.1333 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.24 | 0.7614 | 0.1457 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.28 | 0.7602 | 0.1385 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.43 | 0.7526 | 0.1415 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.77 | 0.7480 | 0.1638 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.91 | 0.7488 | 0.1383 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.01 | 0.7547 | 0.1507 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.99 | 0.7528 | 0.1414 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.77 | 0.7480 | 0.1638 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.91 | 0.7488 | 0.1382 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.01 | 0.7547 | 0.1507 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.99 | 0.7528 | 0.1414 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 58.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.25 | 0.7084 | 0.0908 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 11.56 | 0.6632 | 0.2924 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.83 | 0.6740 | 0.2655 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.74 | 0.6791 | 0.2787 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.75 | 0.6775 | 0.2720 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 11.56 | 0.6632 | 0.2924 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.83 | 0.6740 | 0.2655 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.74 | 0.6791 | 0.2787 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.75 | 0.6775 | 0.2720 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 19.84 | 0.6486 | 0.2297 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 12.06 | 0.6727 | 0.2942 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.45 | 0.6839 | 0.2652 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.29 | 0.6885 | 0.2799 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.35 | 0.6868 | 0.2724 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 12.06 | 0.6727 | 0.2942 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 12.45 | 0.6839 | 0.2652 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 12.29 | 0.6885 | 0.2799 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 12.35 | 0.6868 | 0.2724 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.70 | 0.6525 | 0.2322 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.57 | 0.6184 | 0.3425 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.79 | 0.6259 | 0.3176 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.70 | 0.6314 | 0.3313 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.74 | 0.6294 | 0.3248 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 9.57 | 0.6184 | 0.3425 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 9.79 | 0.6259 | 0.3175 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.70 | 0.6314 | 0.3313 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.74 | 0.6294 | 0.3248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 24.95 | 0.7295 | 0.0931 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.55 | 0.7378 | 0.0840 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.44 | 0.7371 | 0.0882 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.51 | 0.7377 | 0.0862 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.95 | 0.7295 | 0.0931 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.55 | 0.7378 | 0.0840 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.44 | 0.7371 | 0.0882 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.51 | 0.7377 | 0.0862 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.52 | 0.7472 | 0.0872 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.08 | 0.7287 | 0.0956 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.51 | 0.7358 | 0.0875 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.43 | 0.7353 | 0.0910 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.49 | 0.7358 | 0.0891 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.08 | 0.7287 | 0.0956 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.51 | 0.7358 | 0.0875 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.43 | 0.7353 | 0.0910 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.49 | 0.7358 | 0.0890 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.35 | 0.7444 | 0.0889 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.87 | 0.7239 | 0.0953 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.04 | 0.7269 | 0.0904 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.04 | 0.7275 | 0.0932 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.05 | 0.7274 | 0.0918 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 24.87 | 0.7239 | 0.0953 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.04 | 0.7269 | 0.0904 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.04 | 0.7275 | 0.0932 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.05 | 0.7274 | 0.0918 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.20 | 0.7345 | 0.1243 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.79 | 0.7430 | 0.1079 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.73 | 0.7456 | 0.1160 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.79 | 0.7451 | 0.1115 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.20 | 0.7345 | 0.1243 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.79 | 0.7431 | 0.1079 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 24.73 | 0.7456 | 0.1160 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 24.79 | 0.7451 | 0.1115 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.32 | 0.7543 | 0.1026 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.24 | 0.7334 | 0.1280 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.70 | 0.7407 | 0.1112 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.67 | 0.7435 | 0.1197 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.72 | 0.7428 | 0.1151 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.24 | 0.7334 | 0.1280 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.70 | 0.7407 | 0.1112 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.67 | 0.7435 | 0.1197 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.72 | 0.7428 | 0.1151 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.04 | 0.7502 | 0.1050 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.26 | 0.7297 | 0.1319 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.36 | 0.7309 | 0.1165 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.44 | 0.7358 | 0.1248 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.41 | 0.7341 | 0.1205 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.26 | 0.7297 | 0.1319 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.36 | 0.7309 | 0.1165 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.44 | 0.7358 | 0.1248 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.41 | 0.7341 | 0.1205 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 23.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.07 | 0.6732 | 0.0246 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 5.95 | 0.4935 | 0.1595 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.04 | 0.4970 | 0.1508 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 5.98 | 0.5040 | 0.1552 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.00 | 0.5007 | 0.1527 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 5.95 | 0.4935 | 0.1595 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.04 | 0.4970 | 0.1508 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 5.98 | 0.5040 | 0.1552 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.00 | 0.5007 | 0.1527 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 19.11 | 0.4310 | 0.1114 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.75 | 0.5198 | 0.1539 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.87 | 0.5228 | 0.1431 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.79 | 0.5316 | 0.1489 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.81 | 0.5274 | 0.1459 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.75 | 0.5198 | 0.1539 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.87 | 0.5228 | 0.1431 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.79 | 0.5316 | 0.1489 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.81 | 0.5274 | 0.1459 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.51 | 0.4516 | 0.1106 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.21 | 0.4558 | 0.1744 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.33 | 0.4604 | 0.1665 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.24 | 0.4665 | 0.1711 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.27 | 0.4637 | 0.1685 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.21 | 0.4558 | 0.1744 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.33 | 0.4604 | 0.1665 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.24 | 0.4665 | 0.1711 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.27 | 0.4637 | 0.1685 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.95 | 0.6732 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.07 | 0.6737 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 30.06 | 0.6737 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 30.06 | 0.6737 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.95 | 0.6732 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.07 | 0.6737 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 30.06 | 0.6737 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 30.06 | 0.6737 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 30.07 | 0.6736 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.95 | 0.6732 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.07 | 0.6737 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.06 | 0.6736 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.06 | 0.6736 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.95 | 0.6732 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.07 | 0.6737 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.06 | 0.6736 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.06 | 0.6736 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 30.07 | 0.6736 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.06 | 0.6733 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 30.07 | 0.6733 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 30.06 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 30.06 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 30.06 | 0.6733 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.07 | 0.6733 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.06 | 0.6732 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.06 | 0.6732 | 0.0245 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 29.61 | 0.6777 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 30.01 | 0.6786 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.98 | 0.6794 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.98 | 0.6789 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.61 | 0.6777 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.01 | 0.6786 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.98 | 0.6794 | 0.0277 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.98 | 0.6789 | 0.0273 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 30.14 | 0.6796 | 0.0262 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.97 | 0.6739 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.31 | 0.6750 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.26 | 0.6765 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.25 | 0.6759 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.97 | 0.6739 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.31 | 0.6750 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.26 | 0.6765 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.25 | 0.6759 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.98 | 0.6791 | 0.0255 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.09 | 0.6799 | 0.0284 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 30.22 | 0.6805 | 0.0272 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 30.26 | 0.6820 | 0.0275 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 30.24 | 0.6814 | 0.0273 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 30.09 | 0.6799 | 0.0284 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 30.22 | 0.6805 | 0.0272 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 30.26 | 0.6820 | 0.0275 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 30.24 | 0.6814 | 0.0273 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.66 | 0.7284 | 0.1132 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 10.99 | 0.6685 | 0.3867 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.21 | 0.6745 | 0.3446 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.10 | 0.6806 | 0.3646 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.12 | 0.6784 | 0.3536 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 10.99 | 0.6685 | 0.3867 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.21 | 0.6745 | 0.3446 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.10 | 0.6806 | 0.3646 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.12 | 0.6784 | 0.3536 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 18.24 | 0.6162 | 0.2936 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 11.41 | 0.6748 | 0.3886 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 11.71 | 0.6811 | 0.3434 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 11.57 | 0.6870 | 0.3659 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 11.62 | 0.6845 | 0.3536 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 11.41 | 0.6748 | 0.3886 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 11.71 | 0.6811 | 0.3434 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 11.57 | 0.6870 | 0.3659 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 11.62 | 0.6845 | 0.3536 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.09 | 0.6163 | 0.2935 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.98 | 0.6318 | 0.4240 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.15 | 0.6357 | 0.3816 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.06 | 0.6420 | 0.4037 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.09 | 0.6395 | 0.3909 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 8.98 | 0.6318 | 0.4240 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 9.15 | 0.6357 | 0.3816 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.06 | 0.6420 | 0.4037 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.09 | 0.6395 | 0.3909 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.23 | 0.7424 | 0.1224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.72 | 0.7477 | 0.1123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.65 | 0.7473 | 0.1171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.70 | 0.7477 | 0.1149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.23 | 0.7424 | 0.1224 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.72 | 0.7477 | 0.1123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.65 | 0.7473 | 0.1171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.70 | 0.7477 | 0.1149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.52 | 0.7549 | 0.1150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.39 | 0.7420 | 0.1249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.77 | 0.7465 | 0.1161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.71 | 0.7464 | 0.1203 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.76 | 0.7466 | 0.1180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.39 | 0.7420 | 0.1249 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.77 | 0.7465 | 0.1162 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.71 | 0.7464 | 0.1203 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.76 | 0.7466 | 0.1180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.39 | 0.7530 | 0.1162 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.16 | 0.7385 | 0.1225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.32 | 0.7404 | 0.1170 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.32 | 0.7409 | 0.1202 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.33 | 0.7409 | 0.1183 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.16 | 0.7385 | 0.1225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.32 | 0.7404 | 0.1170 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.32 | 0.7409 | 0.1202 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.33 | 0.7409 | 0.1183 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.42 | 0.7512 | 0.1738 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.99 | 0.7559 | 0.1485 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.95 | 0.7590 | 0.1609 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.00 | 0.7582 | 0.1542 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.42 | 0.7512 | 0.1738 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.99 | 0.7559 | 0.1485 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.95 | 0.7590 | 0.1609 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.00 | 0.7582 | 0.1542 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.36 | 0.7651 | 0.1389 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.51 | 0.7500 | 0.1772 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.97 | 0.7542 | 0.1524 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.97 | 0.7575 | 0.1651 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.00 | 0.7564 | 0.1576 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.51 | 0.7500 | 0.1772 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.97 | 0.7542 | 0.1525 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.97 | 0.7574 | 0.1651 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.00 | 0.7563 | 0.1576 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.15 | 0.7623 | 0.1401 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.51 | 0.7476 | 0.1849 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.68 | 0.7479 | 0.1562 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.75 | 0.7525 | 0.1709 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.73 | 0.7509 | 0.1610 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.51 | 0.7476 | 0.1849 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.68 | 0.7479 | 0.1562 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.75 | 0.7525 | 0.1709 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.73 | 0.7509 | 0.1610 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.172 | 36.6 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.172 | 44.6 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.172 | 36.0 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.172 | 39.5 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.164 | 45.7 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.164 | 40.0 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.164 | 35.4 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.164 | 34.9 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 3727770 | 0.813 | 202.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 400634 | 0.174 | 35.7 | 32.80 | 0.19 | 0.009 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 400634 | 0.174 | 47.6 | 32.80 | 0.19 | 0.009 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 400634 | 0.174 | 47.5 | 32.80 | 0.19 | 0.009 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 400634 | 0.174 | 44.5 | 32.80 | 0.19 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 400634 | 0.162 | 46.0 | 32.80 | 0.19 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 400634 | 0.162 | 37.9 | 32.80 | 0.19 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 400634 | 0.162 | 43.8 | 32.80 | 0.19 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 400634 | 0.162 | 39.4 | 32.80 | 0.19 | 0.009 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 3715966 | 0.813 | 112.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.321 | 41.5 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.321 | 29.1 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.321 | 32.2 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.321 | 36.5 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.164 | 42.8 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.164 | 39.7 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.164 | 38.6 | 32.55 | 0.25 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 402166 | 0.164 | 42.5 | 32.55 | 0.25 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.671 | 0.052 |
| in035 | mask_ent | 0.793 | 0.052 |
| in035 | mask_grad | 0.500 | 0.052 |
| in035 | r_col | 0.630 | 0.052 |
| in035 | r_warp | 0.780 | 0.052 |

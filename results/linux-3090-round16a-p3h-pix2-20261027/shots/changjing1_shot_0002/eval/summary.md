# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 68.5% | 25.18 / 0.0821 | 27.81 / 0.1554 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 69.5% | 25.09 / 0.0852 | 28.73 / 0.1187 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 68.9% | 25.12 / 0.0839 | 28.86 / 0.1315 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 69.1% | 25.09 / 0.0847 | 28.94 / 0.1222 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 69.1% | 25.14 / 0.0842 | 26.77 / 0.1554 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 70.5% | 24.87 / 0.0873 | 26.60 / 0.1221 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 69.8% | 24.98 / 0.0861 | 26.83 / 0.1352 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 70.2% | 24.92 / 0.0870 | 26.62 / 0.1270 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 71.0% | 25.26 / 0.0833 | 26.64 / 0.1384 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 67.7% | 25.41 / 0.0844 | 26.54 / 0.1208 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 8.3% | 18.31 / 0.0432 | 19.46 / 0.0580 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 67.9% | 25.38 / 0.0836 | 26.04 / 0.1268 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 8.5% | 18.23 / 0.0425 | 18.86 / 0.0653 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 71.0% | 25.27 / 0.0838 | 26.92 / 0.1111 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 67.9% | 25.11 / 0.0866 | 26.06 / 0.1194 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 7.9% | 18.95 / 0.0404 | 19.97 / 0.0505 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 68.2% | 25.07 / 0.0847 | 25.71 / 0.1238 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 8.4% | 19.05 / 0.0397 | 19.69 / 0.0578 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 70.8% | 25.09 / 0.0872 | 25.00 / 0.1573 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 69.7% | 25.34 / 0.0813 | 28.25 / 0.1491 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 70.6% | 25.23 / 0.0842 | 28.89 / 0.1170 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 70.1% | 25.27 / 0.0824 | 29.17 / 0.1275 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 70.3% | 25.25 / 0.0839 | 29.17 / 0.1202 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 69.7% | 25.33 / 0.0818 | 26.37 / 0.1551 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 71.2% | 24.91 / 0.0857 | 26.32 / 0.1221 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 70.5% | 25.08 / 0.0836 | 26.44 / 0.1342 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 70.8% | 25.00 / 0.0845 | 26.39 / 0.1264 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 72.4% | 24.94 / 0.0888 | 24.50 / 0.1616 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 16.7% | 22.86 / 0.0396 | 20.84 / 0.1059 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 20.2% | 23.16 / 0.0459 | 19.96 / 0.1215 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 17.6% | 22.93 / 0.0416 | 20.99 / 0.1082 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 18.5% | 23.00 / 0.0438 | 20.82 / 0.1121 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 17.8% | 22.70 / 0.0422 | 20.33 / 0.1134 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 21.6% | 23.08 / 0.0477 | 20.19 / 0.1254 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 19.0% | 22.79 / 0.0441 | 20.65 / 0.1142 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 19.9% | 22.88 / 0.0456 | 20.61 / 0.1170 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 26.45 / 0.1183 | 26.86 / 0.1126 | 16.84 / 0.0586 | 34.86 / 0.0245 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.41 / 0.1927 | 28.34 / 0.2189 | 20.18 / 0.0481 | 33.45 / 0.0314 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.12 / 0.1546 | 29.01 / 0.1780 | 21.37 / 0.0378 | 33.54 / 0.0288 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.07 / 0.1678 | 29.07 / 0.1914 | 21.17 / 0.0420 | 33.65 / 0.0302 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.19 / 0.1582 | 29.15 / 0.1805 | 21.44 / 0.0390 | 33.57 / 0.0293 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.79 / 0.1929 | 27.54 / 0.2211 | 19.76 / 0.0477 | 33.35 / 0.0314 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.93 / 0.1567 | 27.54 / 0.1797 | 20.69 / 0.0379 | 33.81 / 0.0289 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.96 / 0.1702 | 27.68 / 0.1956 | 20.53 / 0.0415 | 33.78 / 0.0296 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.86 / 0.1616 | 27.50 / 0.1849 | 20.72 / 0.0397 | 33.77 / 0.0292 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.44 / 0.1413 | 29.28 / 0.1168 | 19.47 / 0.0614 | 35.52 / 0.0242 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.31 / 0.1462 | 27.03 / 0.1306 | 19.31 / 0.0591 | 32.82 / 0.0302 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.86 / 0.1296 | 26.63 / 0.1191 | 18.74 / 0.0581 | 32.90 / 0.0297 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.17 / 0.1501 | 26.94 / 0.1329 | 19.14 / 0.0610 | 32.96 / 0.0307 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.76 / 0.1318 | 26.57 / 0.1214 | 18.60 / 0.0581 | 33.12 / 0.0303 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.57 / 0.1204 | 29.17 / 0.1202 | 19.54 / 0.0424 | 35.23 / 0.0250 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.38 / 0.1425 | 27.15 / 0.1348 | 19.20 / 0.0535 | 34.04 / 0.0302 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.84 / 0.1253 | 26.69 / 0.1183 | 18.53 / 0.0542 | 33.40 / 0.0298 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.32 / 0.1460 | 27.15 / 0.1350 | 19.10 / 0.0558 | 34.32 / 0.0306 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.80 / 0.1283 | 26.69 / 0.1193 | 18.47 / 0.0556 | 33.79 / 0.0300 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.05 / 0.1577 | 26.78 / 0.1535 | 19.19 / 0.0587 | 31.89 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.74 / 0.1874 | 28.66 / 0.2150 | 20.41 / 0.0450 | 34.20 / 0.0295 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.22 / 0.1526 | 29.00 / 0.1753 | 21.49 / 0.0364 | 33.79 / 0.0278 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.35 / 0.1620 | 29.30 / 0.1867 | 21.35 / 0.0391 | 34.11 / 0.0291 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.35 / 0.1556 | 29.22 / 0.1782 | 21.62 / 0.0367 | 33.91 / 0.0285 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.52 / 0.1933 | 27.29 / 0.2215 | 19.33 / 0.0526 | 33.66 / 0.0298 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.79 / 0.1565 | 27.43 / 0.1783 | 20.25 / 0.0402 | 33.37 / 0.0280 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.74 / 0.1691 | 27.48 / 0.1935 | 19.96 / 0.0449 | 33.44 / 0.0291 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.78 / 0.1614 | 27.46 / 0.1833 | 20.24 / 0.0419 | 33.37 / 0.0283 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.03 / 0.1573 | 26.73 / 0.1544 | 19.12 / 0.0587 | 32.27 / 0.0317 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 25.44 / 0.1887 | 25.23 / 0.1916 | 18.19 / 0.0649 | 34.11 / 0.0331 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.82 / 0.1940 | 24.33 / 0.2051 | 18.54 / 0.0636 | 34.16 / 0.0328 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.49 / 0.1898 | 25.30 / 0.1934 | 18.57 / 0.0654 | 34.17 / 0.0331 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.35 / 0.1907 | 25.08 / 0.1964 | 18.62 / 0.0655 | 34.12 / 0.0330 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.15 / 0.1909 | 24.89 / 0.1943 | 17.75 / 0.0703 | 33.93 / 0.0352 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.72 / 0.1955 | 24.30 / 0.2059 | 18.18 / 0.0669 | 33.84 / 0.0363 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.21 / 0.1907 | 24.97 / 0.1958 | 18.20 / 0.0693 | 33.81 / 0.0356 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.12 / 0.1920 | 24.84 / 0.1974 | 18.27 / 0.0681 | 33.72 / 0.0359 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.3%） | — | — | 26.45 / 0.1183 | 26.86 / 0.1126 | 34.86 |
| in035 | rife | 10.9% | 16.7% | 25.44 / 0.1887 | 25.23 / 0.1916 | 34.11 |
| in035 | cnw_cnn | 56.8% | 68.5% | 28.41 / 0.1927 | 28.34 / 0.2189 | 33.45 |
| in035 | cnw_f5 | 57.2% | 69.7% | 28.74 / 0.1874 | 28.66 / 0.2150 | 34.20 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.21 / 0.1129 | -1.34 / +0.0545 (core 11.6%) | +2.98 / +0.0923 (core 79.8%) | +3.58 / +0.0835 (core 80.2%) |
| in035 | 2 | 0-3 | 26.24 / 0.1144 | -2.01 / +0.0996 (core 11.6%) | +1.87 / +0.1126 (core 79.8%) | +2.26 / +0.1112 (core 80.2%) |
| in035 | 4 | 3-5 | 26.89 / 0.1276 | +0.33 / +0.0570 (core 6.4%) | +1.05 / +0.0181 (core 10.9%) | +1.03 / +0.0126 (core 10.8%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 26.45 / 0.1183 | 26.86 | 34.86 | — |
| in035 | cnw_cnn | 不复核 | —% | 28.41 / 0.1927 | 28.34 | 33.45 | 0/3 |
| in035 | cnw_cnn | oracle | 7.2% | 28.86 / 0.1107 | 28.92 | 34.85 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 29.12 / 0.1546 | 29.01 | 33.54 | 0/3 |
| in035 | cnw_cnn | oracle | 7.5% | 29.66 / 0.1024 | 29.85 | 34.86 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 29.07 / 0.1678 | 29.07 | 33.65 | 0/3 |
| in035 | cnw_cnn | oracle | 7.3% | 29.54 / 0.1060 | 29.79 | 34.86 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 29.19 / 0.1582 | 29.15 | 33.57 | 0/3 |
| in035 | cnw_cnn | oracle | 7.4% | 29.71 / 0.1037 | 29.97 | 34.86 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.79 / 0.1929 | 27.54 | 33.35 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.4% | 28.51 / 0.1118 | 28.51 | 34.82 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.93 / 0.1567 | 27.54 | 33.81 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.9% | 29.08 / 0.1026 | 29.10 | 34.84 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.96 / 0.1702 | 27.68 | 33.78 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.7% | 28.96 / 0.1064 | 29.04 | 34.85 | 2/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.86 / 0.1616 | 27.50 | 33.77 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 7.8% | 29.08 / 0.1044 | 29.15 | 34.85 | 2/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 28.44 / 0.1413 | 29.28 | 35.52 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 7.5% | 28.44 / 0.1259 | 29.18 | 34.87 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 27.31 / 0.1462 | 27.03 | 32.82 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 7.2% | 28.28 / 0.1234 | 28.43 | 34.87 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 26.86 / 0.1296 | 26.63 | 32.90 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 4.5% | 27.86 / 0.1198 | 28.09 | 34.86 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 27.17 / 0.1501 | 26.94 | 32.96 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 7.2% | 28.16 / 0.1254 | 28.41 | 34.86 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 26.76 / 0.1318 | 26.57 | 33.12 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 4.5% | 27.76 / 0.1194 | 28.09 | 34.86 | 2/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 28.57 / 0.1204 | 29.17 | 35.23 | 1/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 7.5% | 28.49 / 0.1058 | 29.01 | 34.88 | 3/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.38 / 0.1425 | 27.15 | 34.04 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 7.3% | 28.22 / 0.1173 | 28.42 | 34.87 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.84 / 0.1253 | 26.69 | 33.40 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 4.2% | 27.71 / 0.1158 | 28.01 | 34.86 | 2/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 27.32 / 0.1460 | 27.15 | 34.32 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 7.3% | 28.15 / 0.1194 | 28.46 | 34.87 | 1/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 26.80 / 0.1283 | 26.69 | 33.79 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 4.2% | 27.68 / 0.1167 | 28.05 | 34.86 | 2/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.05 / 0.1577 | 26.78 | 31.89 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 7.7% | 28.14 / 0.1223 | 28.28 | 34.82 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.74 / 0.1874 | 28.66 | 34.20 | 0/3 |
| in035 | cnw_f5 | oracle | 6.9% | 29.06 / 0.1081 | 29.12 | 34.86 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 29.22 / 0.1526 | 29.00 | 33.79 | 0/3 |
| in035 | cnw_f5 | oracle | 7.2% | 29.73 / 0.1013 | 29.84 | 34.87 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 29.35 / 0.1620 | 29.30 | 34.11 | 0/3 |
| in035 | cnw_f5 | oracle | 7.0% | 29.70 / 0.1035 | 29.89 | 34.87 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 29.35 / 0.1556 | 29.22 | 33.91 | 0/3 |
| in035 | cnw_f5 | oracle | 7.1% | 29.84 / 0.1018 | 30.02 | 34.87 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.52 / 0.1933 | 27.29 | 33.66 | 0/3 |
| in035 | cnw_f5_mw | oracle | 7.1% | 28.16 / 0.1121 | 28.11 | 34.87 | 2/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.79 / 0.1565 | 27.43 | 33.37 | 0/3 |
| in035 | cnw_f5_mw | oracle | 7.6% | 28.84 / 0.1034 | 28.84 | 34.86 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.74 / 0.1691 | 27.48 | 33.44 | 0/3 |
| in035 | cnw_f5_mw | oracle | 7.4% | 28.60 / 0.1071 | 28.65 | 34.86 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.78 / 0.1614 | 27.46 | 33.37 | 0/3 |
| in035 | cnw_f5_mw | oracle | 7.5% | 28.80 / 0.1051 | 28.85 | 34.86 | 3/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.03 / 0.1573 | 26.73 | 32.27 | 0/3 |
| in035 | cnw_f5_pix | oracle | 7.8% | 28.11 / 0.1229 | 28.28 | 34.85 | 0/3 |
| in035 | rife | 不复核 | —% | 25.44 / 0.1887 | 25.23 | 34.11 | 0/3 |
| in035 | rife | oracle | 3.6% | 27.44 / 0.1262 | 27.60 | 34.86 | 0/3 |
| in035 | rife | 不复核 | —% | 24.82 / 0.1940 | 24.33 | 34.16 | 0/3 |
| in035 | rife | oracle | 4.2% | 27.67 / 0.1245 | 27.72 | 34.85 | 1/3 |
| in035 | rife | 不复核 | —% | 25.49 / 0.1898 | 25.30 | 34.17 | 0/3 |
| in035 | rife | oracle | 3.8% | 27.72 / 0.1259 | 27.95 | 34.85 | 0/3 |
| in035 | rife | 不复核 | —% | 25.35 / 0.1907 | 25.08 | 34.12 | 0/3 |
| in035 | rife | oracle | 3.9% | 27.75 / 0.1262 | 27.95 | 34.85 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.15 / 0.1909 | 24.89 | 33.93 | 0/3 |
| in035 | rife_mw | oracle | 4.0% | 27.05 / 0.1311 | 27.13 | 34.85 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 24.72 / 0.1955 | 24.30 | 33.84 | 0/3 |
| in035 | rife_mw | oracle | 4.6% | 27.33 / 0.1285 | 27.39 | 34.84 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.21 / 0.1907 | 24.97 | 33.81 | 0/3 |
| in035 | rife_mw | oracle | 4.3% | 27.36 / 0.1302 | 27.54 | 34.85 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 25.12 / 0.1920 | 24.84 | 33.72 | 0/3 |
| in035 | rife_mw | oracle | 4.4% | 27.41 / 0.1294 | 27.56 | 34.84 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 26.45 / 0.1183 | 26.86 / 0.1126 | — |
| in035 | FF | 0（前馈） | 940×686（62%） | 33.51 | 28.41 / 0.1927 | 28.34 / 0.2189 | 0/3 |
| in035 | 25 | 1.29 s | 940×686（62%） | 36.13 | 29.07 / 0.1678 | 29.07 / 0.1914 | 0/3 |
| in035 | 50 | 2.58 s | 940×686（62%） | 37.26 | 29.19 / 0.1582 | 29.15 / 0.1805 | 0/3 |
| in035 | 100 | 5.15 s | 940×686（62%） | 38.04 | 29.12 / 0.1546 | 29.01 / 0.1780 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 26.45 / 0.1183 | 26.86 / 0.1126 | 34.86 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 28.41 / 0.1927 | 28.34 / 0.2189 | 33.45 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 28.86 / 0.1107 | 28.92 / 0.1174 | 34.85 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 29.07 / 0.1678 | 29.07 / 0.1914 | 33.65 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 29.54 / 0.1060 | 29.79 / 0.1133 | 34.86 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 29.19 / 0.1582 | 29.15 / 0.1805 | 33.57 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 29.71 / 0.1037 | 29.97 / 0.1120 | 34.86 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 29.12 / 0.1546 | 29.01 / 0.1780 | 33.54 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 29.66 / 0.1024 | 29.85 / 0.1119 | 34.86 | 3/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.79 / 0.1929 | 27.54 / 0.2211 | 33.35 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.51 / 0.1118 | 28.51 / 0.1198 | 34.82 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.96 / 0.1702 | 27.68 / 0.1956 | 33.78 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.96 / 0.1064 | 29.04 / 0.1138 | 34.85 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.86 / 0.1616 | 27.50 / 0.1849 | 33.77 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 29.08 / 0.1044 | 29.15 / 0.1121 | 34.85 | 2/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.93 / 0.1567 | 27.54 / 0.1797 | 33.81 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 29.08 / 0.1026 | 29.10 / 0.1112 | 34.84 | 3/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 28.74 / 0.1874 | 28.66 / 0.2150 | 34.20 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 29.06 / 0.1081 | 29.12 / 0.1158 | 34.86 | 3/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 29.35 / 0.1620 | 29.30 / 0.1867 | 34.11 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 29.70 / 0.1035 | 29.89 / 0.1117 | 34.87 | 3/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 29.35 / 0.1556 | 29.22 / 0.1782 | 33.91 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 29.84 / 0.1018 | 30.02 / 0.1113 | 34.87 | 3/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 29.22 / 0.1526 | 29.00 / 0.1753 | 33.79 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 29.73 / 0.1013 | 29.84 / 0.1116 | 34.87 | 3/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.52 / 0.1933 | 27.29 / 0.2215 | 33.66 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.16 / 0.1121 | 28.11 / 0.1196 | 34.87 | 2/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.74 / 0.1691 | 27.48 / 0.1935 | 33.44 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.60 / 0.1071 | 28.65 / 0.1145 | 34.86 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.78 / 0.1614 | 27.46 / 0.1833 | 33.37 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.80 / 0.1051 | 28.85 / 0.1128 | 34.86 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.79 / 0.1565 | 27.43 / 0.1783 | 33.37 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.84 / 0.1034 | 28.84 / 0.1120 | 34.86 | 3/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 25.44 / 0.1887 | 25.23 / 0.1916 | 34.11 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.44 / 0.1262 | 27.60 / 0.1195 | 34.86 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 25.49 / 0.1898 | 25.30 / 0.1934 | 34.17 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.72 / 0.1259 | 27.95 / 0.1198 | 34.85 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 25.35 / 0.1907 | 25.08 / 0.1964 | 34.12 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.75 / 0.1262 | 27.95 / 0.1212 | 34.85 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 24.82 / 0.1940 | 24.33 / 0.2051 | 34.16 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.67 / 0.1245 | 27.72 / 0.1223 | 34.85 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 25.15 / 0.1909 | 24.89 / 0.1943 | 33.93 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 27.05 / 0.1311 | 27.13 / 0.1257 | 34.85 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 25.21 / 0.1907 | 24.97 / 0.1958 | 33.81 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 27.36 / 0.1302 | 27.54 / 0.1257 | 34.85 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 25.12 / 0.1920 | 24.84 / 0.1974 | 33.72 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 27.41 / 0.1294 | 27.56 / 0.1254 | 34.84 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 24.72 / 0.1955 | 24.30 / 0.2059 | 33.84 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 27.33 / 0.1285 | 27.39 / 0.1269 | 34.84 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.86 / 0.1126 | 16.84 / 0.0586 | 34.86 / 0.0245 | 26.45 / 0.1183 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 76.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.86 | 0.8142 | 0.1126 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 16.03 | 0.7844 | 0.3872 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 17.24 | 0.7869 | 0.3377 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 16.52 | 0.7914 | 0.3542 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 16.93 | 0.7909 | 0.3413 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 17.87 | 0.7806 | 0.3863 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 19.81 | 0.7877 | 0.3377 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 19.02 | 0.7902 | 0.3551 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 19.41 | 0.7901 | 0.3429 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 28.21 | 0.8387 | 0.1841 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 24.92 | 0.8441 | 0.2011 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 24.92 | 0.8441 | 0.2011 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 24.77 | 0.8417 | 0.2030 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 24.77 | 0.8417 | 0.2030 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 23.72 | 0.6990 | 0.2720 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 20.70 | 0.7016 | 0.2901 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.70 | 0.7016 | 0.2901 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 20.54 | 0.7011 | 0.2912 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 20.54 | 0.7011 | 0.2912 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 20.71 | 0.6942 | 0.2973 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 15.75 | 0.7789 | 0.3952 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 16.88 | 0.7810 | 0.3474 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 16.20 | 0.7847 | 0.3612 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 16.58 | 0.7840 | 0.3512 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 17.25 | 0.7656 | 0.4019 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.34 | 0.7730 | 0.3520 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 18.37 | 0.7751 | 0.3673 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 18.81 | 0.7752 | 0.3567 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 20.61 | 0.6755 | 0.3094 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.36 | 0.5942 | 0.6874 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.58 | 0.5949 | 0.6780 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 6.42 | 0.5972 | 0.6820 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.49 | 0.5963 | 0.6799 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 6.41 | 0.5930 | 0.6863 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 6.68 | 0.5943 | 0.6804 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 6.49 | 0.5957 | 0.6809 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 6.56 | 0.5954 | 0.6793 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.92 | 0.8239 | 0.1174 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.85 | 0.8302 | 0.1119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.79 | 0.8293 | 0.1133 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.97 | 0.8307 | 0.1120 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.51 | 0.8210 | 0.1198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.10 | 0.8295 | 0.1112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 29.04 | 0.8276 | 0.1138 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.15 | 0.8292 | 0.1121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.18 | 0.8295 | 0.1042 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.43 | 0.8296 | 0.1110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.09 | 0.8242 | 0.1116 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.41 | 0.8286 | 0.1121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 28.09 | 0.8236 | 0.1120 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.01 | 0.8303 | 0.1024 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.42 | 0.8291 | 0.1082 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.01 | 0.8231 | 0.1102 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.46 | 0.8285 | 0.1087 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 28.05 | 0.8227 | 0.1099 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.28 | 0.8284 | 0.1106 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.12 | 0.8253 | 0.1158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.84 | 0.8300 | 0.1116 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.89 | 0.8297 | 0.1117 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.02 | 0.8304 | 0.1113 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.11 | 0.8171 | 0.1196 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.84 | 0.8266 | 0.1120 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.65 | 0.8239 | 0.1145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.85 | 0.8261 | 0.1128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.28 | 0.8282 | 0.1119 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.60 | 0.8145 | 0.1195 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.72 | 0.8136 | 0.1223 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.95 | 0.8151 | 0.1198 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.95 | 0.8145 | 0.1212 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.13 | 0.8114 | 0.1257 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.39 | 0.8105 | 0.1269 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.54 | 0.8118 | 0.1257 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.56 | 0.8117 | 0.1254 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.34 | 0.8423 | 0.2189 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.01 | 0.8460 | 0.1780 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.07 | 0.8494 | 0.1914 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.15 | 0.8493 | 0.1805 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.54 | 0.8369 | 0.2211 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.54 | 0.8442 | 0.1797 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.68 | 0.8453 | 0.1956 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.50 | 0.8455 | 0.1849 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 29.28 | 0.8376 | 0.1168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.03 | 0.8426 | 0.1306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.63 | 0.8197 | 0.1191 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.94 | 0.8406 | 0.1329 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.57 | 0.8190 | 0.1214 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 29.17 | 0.8447 | 0.1202 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.15 | 0.8435 | 0.1348 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.69 | 0.8184 | 0.1183 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.15 | 0.8430 | 0.1350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.69 | 0.8179 | 0.1193 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.78 | 0.8412 | 0.1535 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.66 | 0.8454 | 0.2150 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.00 | 0.8465 | 0.1753 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.30 | 0.8510 | 0.1867 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.22 | 0.8499 | 0.1782 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.29 | 0.8321 | 0.2215 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.43 | 0.8391 | 0.1783 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.48 | 0.8404 | 0.1935 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.46 | 0.8409 | 0.1833 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.73 | 0.8401 | 0.1544 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.23 | 0.7942 | 0.1916 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.33 | 0.7893 | 0.2051 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.30 | 0.7948 | 0.1934 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.08 | 0.7927 | 0.1964 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.89 | 0.7920 | 0.1943 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.30 | 0.7874 | 0.2059 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.97 | 0.7917 | 0.1958 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.84 | 0.7910 | 0.1974 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 16.84 | 0.5177 | 0.0586 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 15.32 | 0.6834 | 0.0630 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 16.87 | 0.7161 | 0.0497 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 16.08 | 0.7111 | 0.0555 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 16.52 | 0.7174 | 0.0521 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 17.92 | 0.6615 | 0.0602 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 19.77 | 0.7104 | 0.0483 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 19.20 | 0.6969 | 0.0534 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 19.54 | 0.7060 | 0.0512 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 19.40 | 0.6349 | 0.0632 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 19.26 | 0.6825 | 0.0610 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 19.26 | 0.6825 | 0.0610 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 19.20 | 0.6655 | 0.0629 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 19.20 | 0.6655 | 0.0629 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 18.60 | 0.6557 | 0.0568 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 17.86 | 0.6649 | 0.0674 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 17.86 | 0.6649 | 0.0674 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 17.79 | 0.6535 | 0.0698 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 17.79 | 0.6535 | 0.0698 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 18.43 | 0.6559 | 0.0718 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 15.14 | 0.6787 | 0.0648 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 16.30 | 0.7098 | 0.0535 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 15.69 | 0.7048 | 0.0588 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 16.03 | 0.7098 | 0.0558 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 16.73 | 0.6134 | 0.0733 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 18.53 | 0.6642 | 0.0581 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 17.91 | 0.6482 | 0.0646 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 18.34 | 0.6591 | 0.0608 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.94 | 0.6425 | 0.0755 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.12 | 0.4507 | 0.1552 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 11.01 | 0.4761 | 0.1403 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 10.47 | 0.4651 | 0.1499 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 10.73 | 0.4685 | 0.1459 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 10.56 | 0.4210 | 0.1551 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 11.58 | 0.4433 | 0.1411 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 11.08 | 0.4288 | 0.1504 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 11.35 | 0.4337 | 0.1466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 20.18 | 0.6886 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.37 | 0.7235 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.17 | 0.7211 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.44 | 0.7283 | 0.0390 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.76 | 0.6601 | 0.0478 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.69 | 0.7155 | 0.0379 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.53 | 0.7011 | 0.0415 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.72 | 0.7127 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.47 | 0.6387 | 0.0614 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.34 | 0.6739 | 0.0588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 18.76 | 0.6284 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.16 | 0.6576 | 0.0602 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 18.62 | 0.6195 | 0.0572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.54 | 0.6735 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.22 | 0.6719 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 18.54 | 0.6147 | 0.0539 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.12 | 0.6604 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 18.49 | 0.6092 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 19.19 | 0.6724 | 0.0586 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 20.40 | 0.6962 | 0.0452 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.49 | 0.7262 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.35 | 0.7251 | 0.0391 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.62 | 0.7294 | 0.0368 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.32 | 0.6352 | 0.0531 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.25 | 0.6917 | 0.0403 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.97 | 0.6750 | 0.0451 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.24 | 0.6879 | 0.0420 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 19.12 | 0.6707 | 0.0586 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.19 | 0.5722 | 0.0645 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.55 | 0.5751 | 0.0631 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.58 | 0.5795 | 0.0647 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.63 | 0.5772 | 0.0650 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 17.76 | 0.5494 | 0.0699 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 18.18 | 0.5472 | 0.0666 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 18.21 | 0.5567 | 0.0689 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 18.27 | 0.5547 | 0.0677 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 20.18 | 0.6910 | 0.0481 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.37 | 0.7236 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.17 | 0.7224 | 0.0420 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 21.44 | 0.7288 | 0.0390 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.76 | 0.6626 | 0.0477 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.69 | 0.7163 | 0.0379 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 20.53 | 0.7026 | 0.0415 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 20.72 | 0.7136 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.47 | 0.6372 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 19.31 | 0.6728 | 0.0591 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 18.74 | 0.6274 | 0.0581 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 19.14 | 0.6538 | 0.0610 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 18.60 | 0.6159 | 0.0581 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.54 | 0.6720 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.20 | 0.6710 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 18.53 | 0.6138 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 19.10 | 0.6563 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 18.47 | 0.6053 | 0.0556 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 19.19 | 0.6702 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 20.41 | 0.6994 | 0.0450 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.49 | 0.7271 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.35 | 0.7270 | 0.0391 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.62 | 0.7306 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 19.33 | 0.6392 | 0.0526 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 20.25 | 0.6931 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 19.96 | 0.6778 | 0.0449 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 20.24 | 0.6897 | 0.0419 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 19.12 | 0.6684 | 0.0587 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.19 | 0.5705 | 0.0649 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.54 | 0.5720 | 0.0636 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.57 | 0.5786 | 0.0654 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.62 | 0.5755 | 0.0655 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 17.75 | 0.5477 | 0.0703 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 18.18 | 0.5439 | 0.0669 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 18.20 | 0.5541 | 0.0693 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 18.27 | 0.5516 | 0.0681 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 87.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.00 | 0.8131 | 0.1014 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 16.47 | 0.8044 | 0.2886 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 17.48 | 0.8091 | 0.2449 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 16.87 | 0.8127 | 0.2609 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 17.18 | 0.8125 | 0.2499 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 17.60 | 0.7993 | 0.2864 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 18.96 | 0.8083 | 0.2447 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 18.29 | 0.8100 | 0.2615 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 18.58 | 0.8104 | 0.2512 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 26.82 | 0.8074 | 0.1935 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 25.50 | 0.8375 | 0.1787 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 25.50 | 0.8375 | 0.1787 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 25.10 | 0.8296 | 0.1876 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 25.10 | 0.8296 | 0.1876 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 23.21 | 0.7433 | 0.2176 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 20.39 | 0.7468 | 0.2465 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.39 | 0.7468 | 0.2465 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 20.13 | 0.7425 | 0.2510 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 20.13 | 0.7425 | 0.2510 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 20.44 | 0.7272 | 0.2697 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 16.28 | 0.8077 | 0.2718 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 17.18 | 0.8123 | 0.2316 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 16.65 | 0.8154 | 0.2452 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 16.94 | 0.8152 | 0.2361 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 17.22 | 0.7927 | 0.2782 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 18.56 | 0.8014 | 0.2384 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 17.93 | 0.8030 | 0.2532 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 18.22 | 0.8034 | 0.2439 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 20.74 | 0.7134 | 0.2631 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.53 | 0.6259 | 0.5492 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.89 | 0.6295 | 0.5323 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.63 | 0.6300 | 0.5420 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.73 | 0.6299 | 0.5381 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.57 | 0.6233 | 0.5483 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.96 | 0.6281 | 0.5344 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.69 | 0.6275 | 0.5415 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.79 | 0.6279 | 0.5381 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.61 | 0.8324 | 0.1005 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.53 | 0.8396 | 0.0923 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.45 | 0.8386 | 0.0962 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.65 | 0.8402 | 0.0938 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.27 | 0.8292 | 0.1018 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.90 | 0.8383 | 0.0926 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.82 | 0.8358 | 0.0964 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.94 | 0.8377 | 0.0941 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.01 | 0.8247 | 0.1243 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.96 | 0.8320 | 0.1156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.48 | 0.8253 | 0.1100 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.83 | 0.8290 | 0.1187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.38 | 0.8239 | 0.1107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.08 | 0.8321 | 0.0993 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.85 | 0.8325 | 0.1088 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.29 | 0.8239 | 0.1052 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.80 | 0.8302 | 0.1108 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.26 | 0.8229 | 0.1060 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.41 | 0.8267 | 0.1246 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.84 | 0.8345 | 0.0990 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.61 | 0.8406 | 0.0921 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.63 | 0.8400 | 0.0946 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.79 | 0.8412 | 0.0934 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.86 | 0.8251 | 0.1027 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.59 | 0.8345 | 0.0945 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.39 | 0.8316 | 0.0988 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.59 | 0.8339 | 0.0965 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.33 | 0.8254 | 0.1252 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.98 | 0.8168 | 0.1102 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.17 | 0.8166 | 0.1099 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.33 | 0.8181 | 0.1101 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.35 | 0.8178 | 0.1094 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.54 | 0.8129 | 0.1173 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.87 | 0.8132 | 0.1159 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.98 | 0.8148 | 0.1170 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.03 | 0.8148 | 0.1160 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.15 | 0.8484 | 0.1766 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.91 | 0.8534 | 0.1394 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.93 | 0.8562 | 0.1527 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.04 | 0.8565 | 0.1433 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.48 | 0.8422 | 0.1772 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.59 | 0.8506 | 0.1414 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.68 | 0.8509 | 0.1553 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.54 | 0.8516 | 0.1464 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 27.40 | 0.8117 | 0.1583 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.75 | 0.8377 | 0.1409 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.30 | 0.8200 | 0.1218 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.43 | 0.8305 | 0.1494 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.05 | 0.8158 | 0.1290 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 27.65 | 0.8356 | 0.1280 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.72 | 0.8407 | 0.1376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.20 | 0.8185 | 0.1171 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.48 | 0.8352 | 0.1435 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.00 | 0.8143 | 0.1234 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.49 | 0.8235 | 0.1787 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.46 | 0.8518 | 0.1745 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.99 | 0.8557 | 0.1391 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.20 | 0.8594 | 0.1503 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.19 | 0.8590 | 0.1432 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.17 | 0.8372 | 0.1803 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.41 | 0.8454 | 0.1441 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.41 | 0.8460 | 0.1583 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.43 | 0.8469 | 0.1494 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.25 | 0.8194 | 0.1837 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.93 | 0.7961 | 0.1662 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.10 | 0.7893 | 0.1778 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.99 | 0.7967 | 0.1680 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.80 | 0.7944 | 0.1692 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.59 | 0.7927 | 0.1701 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.11 | 0.7882 | 0.1778 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.75 | 0.7942 | 0.1699 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.64 | 0.7931 | 0.1713 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.38 | 0.8022 | 0.1001 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 16.62 | 0.7998 | 0.2419 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 17.77 | 0.8091 | 0.2130 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 17.11 | 0.8100 | 0.2269 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 17.49 | 0.8112 | 0.2185 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 18.63 | 0.7967 | 0.2390 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 20.44 | 0.8098 | 0.2119 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 19.75 | 0.8088 | 0.2248 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 20.11 | 0.8105 | 0.2179 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 25.64 | 0.8193 | 0.1515 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 24.38 | 0.8346 | 0.1518 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 24.38 | 0.8346 | 0.1518 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 24.26 | 0.8279 | 0.1550 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 24.26 | 0.8279 | 0.1550 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 22.38 | 0.7436 | 0.2064 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 20.89 | 0.7477 | 0.2188 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.89 | 0.7477 | 0.2188 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 20.78 | 0.7436 | 0.2231 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 20.78 | 0.7436 | 0.2231 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 21.11 | 0.7423 | 0.2275 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 16.35 | 0.8007 | 0.2417 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 17.39 | 0.8097 | 0.2163 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 16.79 | 0.8101 | 0.2289 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 17.13 | 0.8113 | 0.2220 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 18.01 | 0.7851 | 0.2476 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 19.97 | 0.7979 | 0.2197 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 19.11 | 0.7964 | 0.2325 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 19.53 | 0.7984 | 0.2251 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 21.12 | 0.7326 | 0.2268 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.84 | 0.6329 | 0.4850 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.09 | 0.6467 | 0.4635 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.92 | 0.6420 | 0.4774 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.99 | 0.6445 | 0.4714 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.91 | 0.6289 | 0.4837 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.23 | 0.6415 | 0.4632 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 8.03 | 0.6361 | 0.4770 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.11 | 0.6387 | 0.4714 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.15 | 0.8281 | 0.0834 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.09 | 0.8391 | 0.0737 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.88 | 0.8363 | 0.0773 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.08 | 0.8386 | 0.0748 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.80 | 0.8245 | 0.0839 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.43 | 0.8377 | 0.0742 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.32 | 0.8338 | 0.0778 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.48 | 0.8368 | 0.0757 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.60 | 0.8249 | 0.1007 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.38 | 0.8298 | 0.0974 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.90 | 0.8207 | 0.0943 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.24 | 0.8261 | 0.0995 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.78 | 0.8190 | 0.0939 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.70 | 0.8334 | 0.0819 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.33 | 0.8308 | 0.0923 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.75 | 0.8195 | 0.0921 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.27 | 0.8280 | 0.0945 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.71 | 0.8185 | 0.0927 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.26 | 0.8309 | 0.0974 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.36 | 0.8306 | 0.0808 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.20 | 0.8402 | 0.0726 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.08 | 0.8380 | 0.0755 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.24 | 0.8397 | 0.0734 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.50 | 0.8195 | 0.0858 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.17 | 0.8331 | 0.0751 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.95 | 0.8287 | 0.0793 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.18 | 0.8320 | 0.0768 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.22 | 0.8305 | 0.0978 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.53 | 0.8083 | 0.1076 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.82 | 0.8105 | 0.1060 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.86 | 0.8108 | 0.1075 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.91 | 0.8108 | 0.1076 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.09 | 0.8040 | 0.1116 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.46 | 0.8050 | 0.1089 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.49 | 0.8066 | 0.1107 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.57 | 0.8066 | 0.1099 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.67 | 0.8412 | 0.1261 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.65 | 0.8510 | 0.1028 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.49 | 0.8516 | 0.1129 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.71 | 0.8530 | 0.1063 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.13 | 0.8364 | 0.1276 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.53 | 0.8495 | 0.1044 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.44 | 0.8478 | 0.1148 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.46 | 0.8500 | 0.1090 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 26.59 | 0.8233 | 0.1143 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.70 | 0.8366 | 0.1122 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.22 | 0.8166 | 0.1001 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.58 | 0.8300 | 0.1160 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.13 | 0.8141 | 0.1023 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 26.77 | 0.8423 | 0.0926 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.77 | 0.8411 | 0.1065 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.17 | 0.8161 | 0.0977 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.74 | 0.8364 | 0.1103 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.16 | 0.8134 | 0.1005 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.52 | 0.8403 | 0.1191 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.03 | 0.8459 | 0.1218 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.87 | 0.8540 | 0.1004 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.76 | 0.8548 | 0.1092 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.89 | 0.8557 | 0.1041 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.90 | 0.8305 | 0.1290 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.39 | 0.8432 | 0.1047 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.18 | 0.8415 | 0.1156 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.36 | 0.8439 | 0.1097 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.52 | 0.8395 | 0.1188 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 23.89 | 0.7884 | 0.1538 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 23.72 | 0.7892 | 0.1573 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.04 | 0.7918 | 0.1541 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 23.97 | 0.7909 | 0.1545 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 23.48 | 0.7833 | 0.1571 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 23.37 | 0.7836 | 0.1597 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 23.67 | 0.7862 | 0.1577 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 23.64 | 0.7861 | 0.1577 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 19.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 34.86 | 0.8787 | 0.0245 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 24.66 | 0.8346 | 0.1550 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 24.80 | 0.8266 | 0.1504 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 24.95 | 0.8345 | 0.1519 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 24.86 | 0.8318 | 0.1508 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 24.40 | 0.8298 | 0.1544 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 24.99 | 0.8275 | 0.1496 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 24.93 | 0.8298 | 0.1512 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 24.98 | 0.8287 | 0.1503 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 32.35 | 0.8904 | 0.0716 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 28.92 | 0.8707 | 0.0828 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 28.92 | 0.8707 | 0.0828 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 29.10 | 0.8703 | 0.0830 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 29.10 | 0.8703 | 0.0830 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 26.86 | 0.7161 | 0.1510 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 25.72 | 0.7205 | 0.1478 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 25.72 | 0.7205 | 0.1478 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 26.14 | 0.7198 | 0.1481 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 26.14 | 0.7198 | 0.1481 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 24.30 | 0.7000 | 0.1493 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 25.12 | 0.8359 | 0.1530 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 24.98 | 0.8291 | 0.1489 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 25.15 | 0.8370 | 0.1509 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 25.01 | 0.8337 | 0.1497 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 24.57 | 0.8307 | 0.1543 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 24.53 | 0.8199 | 0.1503 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 24.54 | 0.8264 | 0.1515 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 24.51 | 0.8233 | 0.1507 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 24.67 | 0.7131 | 0.1437 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.19 | 0.7167 | 0.2307 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.11 | 0.7200 | 0.2270 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.07 | 0.7200 | 0.2295 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.08 | 0.7193 | 0.2285 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 11.93 | 0.7193 | 0.2304 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 11.93 | 0.7179 | 0.2270 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 11.77 | 0.7198 | 0.2290 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 11.86 | 0.7186 | 0.2280 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 34.85 | 0.8786 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 34.86 | 0.8785 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 34.86 | 0.8786 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 34.86 | 0.8786 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 34.82 | 0.8783 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 34.84 | 0.8782 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 34.85 | 0.8783 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 34.85 | 0.8783 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 34.87 | 0.8789 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 34.87 | 0.8788 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 34.86 | 0.8787 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 34.86 | 0.8788 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 34.86 | 0.8787 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 34.88 | 0.8789 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 34.87 | 0.8789 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 34.86 | 0.8787 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 34.87 | 0.8788 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 34.86 | 0.8787 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 34.82 | 0.8787 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 34.86 | 0.8787 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 34.87 | 0.8787 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 34.87 | 0.8787 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 34.87 | 0.8786 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 34.87 | 0.8785 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 34.86 | 0.8785 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 34.86 | 0.8784 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 34.86 | 0.8784 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 34.85 | 0.8788 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 34.86 | 0.8786 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 34.85 | 0.8785 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 34.85 | 0.8785 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 34.85 | 0.8785 | 0.0246 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 34.85 | 0.8785 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 34.84 | 0.8784 | 0.0248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 34.85 | 0.8785 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 34.84 | 0.8784 | 0.0248 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 33.45 | 0.8866 | 0.0314 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 33.54 | 0.8810 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 33.65 | 0.8868 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 33.57 | 0.8848 | 0.0293 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 33.35 | 0.8826 | 0.0314 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 33.81 | 0.8821 | 0.0289 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 33.78 | 0.8827 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 33.77 | 0.8824 | 0.0292 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 35.52 | 0.8867 | 0.0242 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 32.82 | 0.8718 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 32.90 | 0.8680 | 0.0297 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 32.96 | 0.8716 | 0.0307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 33.12 | 0.8710 | 0.0303 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 35.23 | 0.8869 | 0.0250 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 34.04 | 0.8820 | 0.0302 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 33.40 | 0.8728 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 34.32 | 0.8812 | 0.0306 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 33.79 | 0.8737 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 31.89 | 0.8692 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 34.20 | 0.8897 | 0.0295 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 33.79 | 0.8844 | 0.0278 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 34.11 | 0.8905 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 33.91 | 0.8880 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 33.66 | 0.8853 | 0.0298 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 33.37 | 0.8765 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 33.44 | 0.8809 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 33.37 | 0.8787 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 32.27 | 0.8701 | 0.0317 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 34.11 | 0.8743 | 0.0331 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 34.16 | 0.8760 | 0.0328 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 34.17 | 0.8757 | 0.0331 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 34.12 | 0.8753 | 0.0330 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 33.93 | 0.8737 | 0.0352 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 33.84 | 0.8730 | 0.0363 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 33.81 | 0.8727 | 0.0356 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 33.72 | 0.8720 | 0.0359 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.45 | 0.8242 | 0.1183 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 17.10 | 0.8070 | 0.3307 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 18.34 | 0.8110 | 0.2848 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 17.62 | 0.8141 | 0.3005 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 18.03 | 0.8140 | 0.2894 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 18.89 | 0.8040 | 0.3280 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 20.91 | 0.8117 | 0.2855 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 20.07 | 0.8129 | 0.3011 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 20.48 | 0.8132 | 0.2910 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 27.17 | 0.8421 | 0.1973 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 25.24 | 0.8509 | 0.2056 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 25.24 | 0.8509 | 0.2056 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 25.09 | 0.8463 | 0.2093 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 25.09 | 0.8463 | 0.2093 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 22.70 | 0.7177 | 0.2547 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 20.93 | 0.7250 | 0.2720 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.93 | 0.7250 | 0.2720 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 20.80 | 0.7222 | 0.2761 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 20.80 | 0.7222 | 0.2761 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 21.02 | 0.7184 | 0.2803 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 16.91 | 0.8072 | 0.3295 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 18.08 | 0.8110 | 0.2869 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 17.39 | 0.8135 | 0.2989 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 17.79 | 0.8135 | 0.2907 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 18.36 | 0.7955 | 0.3357 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 20.53 | 0.8027 | 0.2927 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 19.53 | 0.8042 | 0.3063 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 20.00 | 0.8046 | 0.2977 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 21.20 | 0.7149 | 0.2795 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.47 | 0.6458 | 0.5690 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.71 | 0.6512 | 0.5473 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.54 | 0.6507 | 0.5594 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.61 | 0.6511 | 0.5537 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.52 | 0.6447 | 0.5676 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.81 | 0.6500 | 0.5509 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.61 | 0.6487 | 0.5596 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.69 | 0.6495 | 0.5552 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.86 | 0.8398 | 0.1107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.66 | 0.8466 | 0.1024 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.54 | 0.8452 | 0.1060 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.71 | 0.8467 | 0.1037 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.51 | 0.8374 | 0.1118 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.08 | 0.8460 | 0.1026 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.96 | 0.8436 | 0.1064 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 29.08 | 0.8454 | 0.1044 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.44 | 0.8385 | 0.1259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 28.28 | 0.8415 | 0.1234 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 27.86 | 0.8361 | 0.1198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 28.16 | 0.8394 | 0.1254 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 27.76 | 0.8352 | 0.1194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.49 | 0.8433 | 0.1058 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.22 | 0.8418 | 0.1173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.71 | 0.8351 | 0.1158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.15 | 0.8402 | 0.1194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 27.68 | 0.8346 | 0.1167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.14 | 0.8419 | 0.1223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.06 | 0.8415 | 0.1081 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.73 | 0.8473 | 0.1013 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.70 | 0.8462 | 0.1035 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.84 | 0.8474 | 0.1018 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.16 | 0.8337 | 0.1121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.84 | 0.8432 | 0.1034 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.60 | 0.8402 | 0.1071 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.80 | 0.8424 | 0.1051 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 28.11 | 0.8418 | 0.1229 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.44 | 0.8281 | 0.1262 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.67 | 0.8292 | 0.1245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.72 | 0.8293 | 0.1259 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.75 | 0.8293 | 0.1262 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.05 | 0.8252 | 0.1311 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.33 | 0.8257 | 0.1285 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.36 | 0.8264 | 0.1302 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.41 | 0.8264 | 0.1294 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.41 | 0.8567 | 0.1927 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.12 | 0.8616 | 0.1546 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 29.07 | 0.8637 | 0.1678 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 29.19 | 0.8641 | 0.1582 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.79 | 0.8525 | 0.1929 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.93 | 0.8603 | 0.1567 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.96 | 0.8605 | 0.1702 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.86 | 0.8611 | 0.1616 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 28.44 | 0.8420 | 0.1413 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.31 | 0.8516 | 0.1462 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.86 | 0.8318 | 0.1296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.17 | 0.8471 | 0.1501 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.76 | 0.8300 | 0.1318 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 28.57 | 0.8548 | 0.1204 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.38 | 0.8544 | 0.1425 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.84 | 0.8313 | 0.1253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.32 | 0.8512 | 0.1460 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.80 | 0.8295 | 0.1283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.05 | 0.8536 | 0.1577 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.74 | 0.8603 | 0.1874 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 29.22 | 0.8635 | 0.1526 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 29.35 | 0.8664 | 0.1620 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 29.35 | 0.8661 | 0.1556 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.52 | 0.8485 | 0.1933 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.79 | 0.8558 | 0.1565 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.74 | 0.8564 | 0.1691 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.78 | 0.8573 | 0.1614 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.03 | 0.8533 | 0.1573 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.44 | 0.8117 | 0.1887 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.82 | 0.8098 | 0.1940 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.49 | 0.8131 | 0.1898 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.35 | 0.8119 | 0.1907 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.15 | 0.8093 | 0.1909 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.72 | 0.8071 | 0.1955 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.21 | 0.8103 | 0.1907 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.12 | 0.8097 | 0.1920 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1279 | None | classic | 2.45 | False | 294364 | 0.329 | 71.2 | 35.33 | 0.30 | 0.009 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1279 | None | classic | 2.45 | False | 294364 | 0.329 | 66.1 | 35.33 | 0.30 | 0.009 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1279 | None | classic | 2.45 | False | 294364 | 0.329 | 70.2 | 35.33 | 0.30 | 0.009 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1279 | None | classic | 2.45 | False | 294364 | 0.329 | 68.3 | 35.33 | 0.30 | 0.009 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1247 | None | classic | 2.32 | False | 233098 | 0.333 | 67.6 | 33.82 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1247 | None | classic | 2.32 | False | 233098 | 0.333 | 48.0 | 33.82 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1247 | None | classic | 2.32 | False | 233098 | 0.333 | 73.1 | 33.82 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1247 | None | classic | 2.32 | False | 233098 | 0.333 | 66.0 | 33.82 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2880123 | 0.194 | 79.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2880123 | 0.799 | 86.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2880123 | 0.799 | 86.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2878971 | 0.494 | 76.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2878971 | 0.494 | 76.3 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2880123 | 0.194 | 87.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2880123 | 0.799 | 226.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2880123 | 0.799 | 226.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2878971 | 0.494 | 87.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2878971 | 0.494 | 87.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2842333 | 0.799 | 507.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1273 | None | classic | 2.42 | False | 289169 | 0.325 | 66.0 | 35.59 | 0.34 | 0.009 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1273 | None | classic | 2.42 | False | 289169 | 0.325 | 51.9 | 35.59 | 0.34 | 0.009 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1273 | None | classic | 2.42 | False | 289169 | 0.325 | 54.6 | 35.59 | 0.34 | 0.009 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1273 | None | classic | 2.42 | False | 289169 | 0.325 | 70.6 | 35.59 | 0.34 | 0.009 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1241 | None | classic | 2.30 | False | 255986 | 0.331 | 66.2 | 34.11 | 0.17 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1241 | None | classic | 2.30 | False | 255986 | 0.331 | 75.2 | 34.11 | 0.17 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1241 | None | classic | 2.30 | False | 255986 | 0.331 | 65.0 | 34.11 | 0.17 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1241 | None | classic | 2.30 | False | 255986 | 0.331 | 68.3 | 34.11 | 0.17 | 0.006 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 3018311 | 0.799 | 155.8 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1293 | None | classic | 2.50 | False | 320685 | 0.856 | 82.4 | 35.81 | 0.17 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1293 | None | classic | 2.50 | False | 320685 | 0.856 | 80.8 | 35.81 | 0.17 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1293 | None | classic | 2.50 | False | 320685 | 0.856 | 76.7 | 35.81 | 0.17 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1293 | None | classic | 2.50 | False | 320685 | 0.856 | 55.2 | 35.81 | 0.17 | 0.008 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1261 | None | classic | 2.38 | False | 278961 | 0.324 | 65.9 | 34.68 | 0.10 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1261 | None | classic | 2.38 | False | 278961 | 0.324 | 59.2 | 34.68 | 0.10 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1261 | None | classic | 2.38 | False | 278961 | 0.324 | 54.1 | 34.68 | 0.10 | 0.009 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1261 | None | classic | 2.38 | False | 278961 | 0.324 | 73.4 | 34.68 | 0.10 | 0.009 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.718 | 0.052 |
| in035 | mask_ent | 0.760 | 0.052 |
| in035 | mask_grad | 0.472 | 0.052 |
| in035 | r_col | 0.721 | 0.052 |
| in035 | r_warp | 0.784 | 0.052 |

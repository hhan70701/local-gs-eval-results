# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 48.8% | 23.95 / 0.0708 | 23.88 / 0.1305 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 49.1% | 23.84 / 0.0712 | 24.16 / 0.1059 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 48.9% | 23.87 / 0.0713 | 24.09 / 0.1184 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 49.0% | 23.86 / 0.0712 | 24.08 / 0.1123 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 48.8% | 23.97 / 0.0707 | 24.05 / 0.1301 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 49.2% | 23.84 / 0.0713 | 24.25 / 0.1057 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 49.0% | 23.89 / 0.0714 | 24.18 / 0.1184 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 49.1% | 23.88 / 0.0714 | 24.17 / 0.1122 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 50.2% | 23.74 / 0.0730 | 24.68 / 0.1221 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 49.0% | 24.11 / 0.0708 | 23.91 / 0.1340 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 49.3% | 24.03 / 0.0729 | 23.87 / 0.1126 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 49.2% | 24.05 / 0.0721 | 23.94 / 0.1241 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 49.2% | 24.04 / 0.0722 | 23.92 / 0.1177 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 48.9% | 24.09 / 0.0709 | 23.97 / 0.1329 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 49.2% | 24.01 / 0.0730 | 23.92 / 0.1116 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 49.1% | 24.05 / 0.0724 | 24.04 / 0.1237 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 49.1% | 24.04 / 0.0727 | 23.99 / 0.1174 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 49.8% | 23.82 / 0.0736 | 24.73 / 0.1228 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 34.8% | 23.78 / 0.0630 | 23.45 / 0.1166 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 35.7% | 23.75 / 0.0648 | 23.74 / 0.1010 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 35.0% | 23.72 / 0.0644 | 23.61 / 0.1062 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 35.2% | 23.72 / 0.0644 | 23.68 / 0.1025 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 34.8% | 23.76 / 0.0631 | 23.50 / 0.1166 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 35.7% | 23.74 / 0.0649 | 23.78 / 0.1006 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 35.0% | 23.70 / 0.0644 | 23.64 / 0.1061 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 35.2% | 23.71 / 0.0644 | 23.71 / 0.1019 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 26.12 / 0.1075 | 27.92 / 0.1175 | 17.53 / 0.0503 | 31.07 / 0.0213 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.31 / 0.1630 | 28.52 / 0.1785 | 19.08 / 0.0529 | 30.79 / 0.0253 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.46 / 0.1407 | 28.32 / 0.1575 | 19.14 / 0.0473 | 31.07 / 0.0236 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.42 / 0.1516 | 28.22 / 0.1676 | 18.99 / 0.0509 | 31.12 / 0.0241 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.40 / 0.1454 | 28.20 / 0.1615 | 19.08 / 0.0491 | 31.10 / 0.0238 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.43 / 0.1629 | 28.74 / 0.1772 | 19.20 / 0.0524 | 30.80 / 0.0252 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.53 / 0.1406 | 28.39 / 0.1570 | 19.21 / 0.0466 | 31.09 / 0.0235 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.50 / 0.1512 | 28.33 / 0.1670 | 19.06 / 0.0502 | 31.14 / 0.0241 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.47 / 0.1450 | 28.27 / 0.1613 | 19.15 / 0.0484 | 31.12 / 0.0238 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.83 / 0.1343 | 29.63 / 0.1358 | 20.43 / 0.0492 | 31.22 / 0.0227 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.25 / 0.1644 | 29.17 / 0.1767 | 18.78 / 0.0558 | 30.56 / 0.0249 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.14 / 0.1449 | 28.70 / 0.1560 | 18.63 / 0.0521 | 30.71 / 0.0236 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.23 / 0.1548 | 28.81 / 0.1666 | 18.61 / 0.0543 | 30.69 / 0.0242 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.19 / 0.1490 | 28.72 / 0.1605 | 18.61 / 0.0533 | 30.70 / 0.0239 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.32 / 0.1633 | 29.44 / 0.1759 | 18.87 / 0.0549 | 30.54 / 0.0249 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.20 / 0.1437 | 28.89 / 0.1549 | 18.69 / 0.0514 | 30.70 / 0.0235 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.32 / 0.1539 | 29.07 / 0.1656 | 18.71 / 0.0534 | 30.66 / 0.0242 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.26 / 0.1481 | 28.95 / 0.1591 | 18.67 / 0.0526 | 30.68 / 0.0239 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.77 / 0.1333 | 29.44 / 0.1370 | 20.27 / 0.0499 | 31.20 / 0.0224 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.00 / 0.1576 | 27.64 / 0.1765 | 18.48 / 0.0555 | 31.06 / 0.0245 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.05 / 0.1420 | 27.54 / 0.1582 | 18.59 / 0.0533 | 31.08 / 0.0240 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.00 / 0.1481 | 27.56 / 0.1627 | 18.40 / 0.0548 | 31.17 / 0.0239 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.03 / 0.1439 | 27.56 / 0.1579 | 18.50 / 0.0540 | 31.16 / 0.0237 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.04 / 0.1576 | 27.74 / 0.1770 | 18.51 / 0.0554 | 31.06 / 0.0243 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.08 / 0.1419 | 27.58 / 0.1573 | 18.63 / 0.0527 | 31.07 / 0.0240 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.05 / 0.1481 | 27.64 / 0.1632 | 18.44 / 0.0545 | 31.18 / 0.0239 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.07 / 0.1438 | 27.62 / 0.1583 | 18.53 / 0.0536 | 31.17 / 0.0236 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 10.3%） | — | — | 26.12 / 0.1075 | 27.92 / 0.1175 | 31.07 |
| in035 | rife | 27.0% | 34.8% | 26.00 / 0.1576 | 27.64 / 0.1765 | 31.06 |
| in035 | cnw_cnn | 38.4% | 48.8% | 26.31 / 0.1630 | 28.52 / 0.1785 | 30.79 |
| in035 | cnw_f5 | 38.5% | 49.0% | 26.25 / 0.1644 | 29.17 / 0.1767 | 30.56 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 24.80 / 0.1100 | +0.63 / +0.0558 (core 35.6%) | +1.15 / +0.0644 (core 50.8%) | +1.31 / +0.0671 (core 49.9%) |
| in035 | 2 | 0-3 | 25.87 / 0.1117 | -0.29 / +0.0734 (core 35.6%) | +0.22 / +0.0771 (core 50.8%) | +0.18 / +0.0798 (core 49.9%) |
| in035 | 4 | 3-5 | 27.69 / 0.1008 | -0.71 / +0.0212 (core 6.0%) | -0.81 / +0.0250 (core 11.0%) | -1.12 / +0.0238 (core 12.6%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 26.12 / 0.1075 | 27.92 | 31.07 | — |
| in035 | cnw_cnn | 不复核 | —% | 26.31 / 0.1630 | 28.52 | 30.79 | 0/3 |
| in035 | cnw_cnn | oracle | 8.3% | 27.01 / 0.1145 | 29.12 | 31.04 | 0/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.46 / 0.1407 | 28.32 | 31.07 | 0/3 |
| in035 | cnw_cnn | oracle | 8.4% | 27.03 / 0.1070 | 29.01 | 31.06 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.42 / 0.1516 | 28.22 | 31.12 | 0/3 |
| in035 | cnw_cnn | oracle | 8.4% | 26.96 / 0.1116 | 28.83 | 31.06 | 1/3 |
| in035 | cnw_cnn | 不复核 | —% | 26.40 / 0.1454 | 28.20 | 31.10 | 0/3 |
| in035 | cnw_cnn | oracle | 8.4% | 26.99 / 0.1096 | 28.92 | 31.06 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.43 / 0.1629 | 28.74 | 30.80 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 8.3% | 27.10 / 0.1145 | 29.28 | 31.04 | 0/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.53 / 0.1406 | 28.39 | 31.09 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 8.4% | 27.09 / 0.1069 | 29.06 | 31.06 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.50 / 0.1512 | 28.33 | 31.14 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 8.4% | 27.03 / 0.1114 | 28.92 | 31.06 | 1/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.47 / 0.1450 | 28.27 | 31.12 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 8.4% | 27.05 / 0.1092 | 28.98 | 31.06 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 27.83 / 0.1343 | 29.63 | 31.22 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 8.7% | 28.01 / 0.1088 | 29.72 | 31.08 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.25 / 0.1644 | 29.17 | 30.56 | 0/3 |
| in035 | cnw_f5 | oracle | 8.1% | 26.72 / 0.1167 | 29.32 | 31.02 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.14 / 0.1449 | 28.70 | 30.71 | 0/3 |
| in035 | cnw_f5 | oracle | 8.2% | 26.61 / 0.1108 | 28.89 | 31.06 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.23 / 0.1548 | 28.81 | 30.69 | 0/3 |
| in035 | cnw_f5 | oracle | 8.1% | 26.63 / 0.1145 | 28.90 | 31.05 | 0/3 |
| in035 | cnw_f5 | 不复核 | —% | 26.19 / 0.1490 | 28.72 | 30.70 | 0/3 |
| in035 | cnw_f5 | oracle | 8.1% | 26.62 / 0.1126 | 28.86 | 31.06 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.32 / 0.1633 | 29.44 | 30.54 | 0/3 |
| in035 | cnw_f5_mw | oracle | 8.1% | 26.78 / 0.1161 | 29.53 | 31.01 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.20 / 0.1437 | 28.89 | 30.70 | 0/3 |
| in035 | cnw_f5_mw | oracle | 8.2% | 26.65 / 0.1104 | 29.02 | 31.06 | 1/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.32 / 0.1539 | 29.07 | 30.66 | 0/3 |
| in035 | cnw_f5_mw | oracle | 8.1% | 26.70 / 0.1137 | 29.08 | 31.05 | 0/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 26.26 / 0.1481 | 28.95 | 30.68 | 0/3 |
| in035 | cnw_f5_mw | oracle | 8.1% | 26.66 / 0.1122 | 29.02 | 31.06 | 1/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 27.77 / 0.1333 | 29.44 | 31.20 | 0/3 |
| in035 | cnw_f5_pix | oracle | 8.5% | 27.90 / 0.1094 | 29.49 | 31.08 | 0/3 |
| in035 | rife | 不复核 | —% | 26.00 / 0.1576 | 27.64 | 31.06 | 0/3 |
| in035 | rife | oracle | 5.7% | 26.62 / 0.1154 | 28.35 | 31.05 | 0/3 |
| in035 | rife | 不复核 | —% | 26.05 / 0.1420 | 27.54 | 31.08 | 0/3 |
| in035 | rife | oracle | 5.9% | 26.68 / 0.1117 | 28.39 | 31.05 | 0/3 |
| in035 | rife | 不复核 | —% | 26.00 / 0.1481 | 27.56 | 31.17 | 0/3 |
| in035 | rife | oracle | 5.7% | 26.55 / 0.1140 | 28.27 | 31.07 | 0/3 |
| in035 | rife | 不复核 | —% | 26.03 / 0.1439 | 27.56 | 31.16 | 0/3 |
| in035 | rife | oracle | 5.8% | 26.63 / 0.1129 | 28.32 | 31.07 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.04 / 0.1576 | 27.74 | 31.06 | 0/3 |
| in035 | rife_mw | oracle | 5.7% | 26.64 / 0.1152 | 28.40 | 31.05 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.08 / 0.1419 | 27.58 | 31.07 | 0/3 |
| in035 | rife_mw | oracle | 5.9% | 26.72 / 0.1113 | 28.44 | 31.05 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.05 / 0.1481 | 27.64 | 31.18 | 0/3 |
| in035 | rife_mw | oracle | 5.8% | 26.57 / 0.1139 | 28.29 | 31.07 | 0/3 |
| in035 | rife_mw | 不复核 | —% | 26.07 / 0.1438 | 27.62 | 31.17 | 0/3 |
| in035 | rife_mw | oracle | 5.8% | 26.65 / 0.1127 | 28.35 | 31.07 | 0/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 26.12 / 0.1075 | 27.92 / 0.1175 | — |
| in035 | FF | 0（前馈） | 1008×661（64%） | 31.14 | 26.31 / 0.1630 | 28.52 / 0.1785 | 0/3 |
| in035 | 25 | 1.86 s | 1008×661（64%） | 33.21 | 26.42 / 0.1516 | 28.22 / 0.1676 | 0/3 |
| in035 | 50 | 3.73 s | 1008×661（64%） | 34.04 | 26.40 / 0.1454 | 28.20 / 0.1615 | 0/3 |
| in035 | 100 | 7.39 s | 1008×661（64%） | 34.79 | 26.46 / 0.1407 | 28.32 / 0.1575 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 26.12 / 0.1075 | 27.92 / 0.1175 | 31.07 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 26.31 / 0.1630 | 28.52 / 0.1785 | 30.79 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.01 / 0.1145 | 29.12 / 0.1199 | 31.04 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 26.42 / 0.1516 | 28.22 / 0.1676 | 31.12 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 26.96 / 0.1116 | 28.83 / 0.1200 | 31.06 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 26.40 / 0.1454 | 28.20 / 0.1615 | 31.10 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 26.99 / 0.1096 | 28.92 / 0.1192 | 31.06 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 26.46 / 0.1407 | 28.32 / 0.1575 | 31.07 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.03 / 0.1070 | 29.01 / 0.1182 | 31.06 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 26.43 / 0.1629 | 28.74 / 0.1772 | 30.80 | 0/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.10 / 0.1145 | 29.28 / 0.1197 | 31.04 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 26.50 / 0.1512 | 28.33 / 0.1670 | 31.14 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.03 / 0.1114 | 28.92 / 0.1194 | 31.06 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 26.47 / 0.1450 | 28.27 / 0.1613 | 31.12 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.05 / 0.1092 | 28.98 / 0.1189 | 31.06 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 26.53 / 0.1406 | 28.39 / 0.1570 | 31.09 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.09 / 0.1069 | 29.06 / 0.1178 | 31.06 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 26.25 / 0.1644 | 29.17 / 0.1767 | 30.56 | 0/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 26.72 / 0.1167 | 29.32 / 0.1202 | 31.02 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 26.23 / 0.1548 | 28.81 / 0.1666 | 30.69 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 26.63 / 0.1145 | 28.90 / 0.1203 | 31.05 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 26.19 / 0.1490 | 28.72 / 0.1605 | 30.70 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 26.62 / 0.1126 | 28.86 / 0.1200 | 31.06 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 26.14 / 0.1449 | 28.70 / 0.1560 | 30.71 | 0/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 26.61 / 0.1108 | 28.89 / 0.1187 | 31.06 | 1/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 26.32 / 0.1633 | 29.44 / 0.1759 | 30.54 | 0/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 26.78 / 0.1161 | 29.53 / 0.1193 | 31.01 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 26.32 / 0.1539 | 29.07 / 0.1656 | 30.66 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 26.70 / 0.1137 | 29.08 / 0.1192 | 31.05 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 26.26 / 0.1481 | 28.95 / 0.1591 | 30.68 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 26.66 / 0.1122 | 29.02 / 0.1186 | 31.06 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 26.20 / 0.1437 | 28.89 / 0.1549 | 30.70 | 0/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 26.65 / 0.1104 | 29.02 / 0.1178 | 31.06 | 1/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 26.00 / 0.1576 | 27.64 / 0.1765 | 31.06 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 26.62 / 0.1154 | 28.35 / 0.1235 | 31.05 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 26.00 / 0.1481 | 27.56 / 0.1627 | 31.17 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 26.55 / 0.1140 | 28.27 / 0.1234 | 31.07 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 26.03 / 0.1439 | 27.56 / 0.1579 | 31.16 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 26.63 / 0.1129 | 28.32 / 0.1230 | 31.07 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 26.05 / 0.1420 | 27.54 / 0.1582 | 31.08 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 26.68 / 0.1117 | 28.39 / 0.1228 | 31.05 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 26.04 / 0.1576 | 27.74 / 0.1770 | 31.06 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 26.64 / 0.1152 | 28.40 / 0.1236 | 31.05 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 26.05 / 0.1481 | 27.64 / 0.1632 | 31.18 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 26.57 / 0.1139 | 28.29 / 0.1233 | 31.07 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 26.07 / 0.1438 | 27.62 / 0.1583 | 31.17 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 26.65 / 0.1127 | 28.35 / 0.1228 | 31.07 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 26.08 / 0.1419 | 27.58 / 0.1573 | 31.07 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 26.72 / 0.1113 | 28.44 / 0.1222 | 31.05 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.92 / 0.1175 | 17.53 / 0.0503 | 31.07 / 0.0213 | 26.12 / 0.1075 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 57.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.92 | 0.7997 | 0.1175 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 15.24 | 0.7640 | 0.4298 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 15.06 | 0.7579 | 0.3880 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 15.11 | 0.7658 | 0.4010 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 15.07 | 0.7626 | 0.3913 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 15.23 | 0.7643 | 0.4279 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 15.06 | 0.7589 | 0.3866 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 15.14 | 0.7667 | 0.3999 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 15.09 | 0.7634 | 0.3900 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 17.84 | 0.6468 | 0.3655 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 14.84 | 0.7539 | 0.4413 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.77 | 0.7470 | 0.4027 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 14.86 | 0.7559 | 0.4139 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.84 | 0.7521 | 0.4049 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 14.89 | 0.7562 | 0.4412 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.80 | 0.7489 | 0.4020 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.90 | 0.7583 | 0.4139 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.86 | 0.7544 | 0.4047 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 17.33 | 0.6071 | 0.3813 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.04 | 0.6998 | 0.5210 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.03 | 0.6943 | 0.4945 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 9.00 | 0.6990 | 0.5009 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.00 | 0.6968 | 0.4947 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 9.05 | 0.7004 | 0.5215 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 9.03 | 0.6954 | 0.4940 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 9.00 | 0.6997 | 0.5017 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 9.00 | 0.6974 | 0.4956 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 29.12 | 0.8152 | 0.1199 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 29.01 | 0.8139 | 0.1182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.83 | 0.8142 | 0.1200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.92 | 0.8139 | 0.1192 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 29.28 | 0.8157 | 0.1197 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.06 | 0.8142 | 0.1178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.92 | 0.8148 | 0.1194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.98 | 0.8143 | 0.1189 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 29.72 | 0.8202 | 0.1097 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 29.32 | 0.8140 | 0.1202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.89 | 0.8122 | 0.1187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.90 | 0.8136 | 0.1203 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.86 | 0.8127 | 0.1200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.53 | 0.8156 | 0.1193 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 29.02 | 0.8135 | 0.1178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.08 | 0.8152 | 0.1192 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 29.02 | 0.8143 | 0.1186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 29.49 | 0.8184 | 0.1108 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 28.35 | 0.8084 | 0.1235 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.39 | 0.8078 | 0.1228 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.27 | 0.8078 | 0.1234 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.32 | 0.8077 | 0.1230 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 28.40 | 0.8086 | 0.1236 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.44 | 0.8081 | 0.1222 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.29 | 0.8080 | 0.1233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.35 | 0.8079 | 0.1228 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.52 | 0.8303 | 0.1785 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.32 | 0.8253 | 0.1575 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.22 | 0.8298 | 0.1676 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.20 | 0.8277 | 0.1615 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.74 | 0.8310 | 0.1772 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.39 | 0.8262 | 0.1570 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.33 | 0.8308 | 0.1670 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.27 | 0.8285 | 0.1613 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 29.63 | 0.8325 | 0.1358 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 29.17 | 0.8295 | 0.1767 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.70 | 0.8243 | 0.1560 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.81 | 0.8299 | 0.1666 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.72 | 0.8273 | 0.1605 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 29.44 | 0.8316 | 0.1759 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.89 | 0.8262 | 0.1549 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 29.07 | 0.8322 | 0.1656 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.95 | 0.8295 | 0.1591 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 29.44 | 0.8300 | 0.1370 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.64 | 0.8175 | 0.1765 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.54 | 0.8143 | 0.1582 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.56 | 0.8179 | 0.1627 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.56 | 0.8165 | 0.1579 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.74 | 0.8177 | 0.1770 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.58 | 0.8149 | 0.1573 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.64 | 0.8183 | 0.1632 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.62 | 0.8169 | 0.1583 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 10.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.53 | 0.4927 | 0.0503 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 15.28 | 0.6129 | 0.0743 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 15.60 | 0.6282 | 0.0660 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 15.43 | 0.6206 | 0.0706 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 15.44 | 0.6249 | 0.0684 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 15.28 | 0.6170 | 0.0737 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 15.60 | 0.6337 | 0.0653 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 15.47 | 0.6262 | 0.0696 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 15.48 | 0.6303 | 0.0675 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 18.80 | 0.6589 | 0.0673 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 14.44 | 0.5809 | 0.0854 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 14.61 | 0.5890 | 0.0786 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 14.62 | 0.5872 | 0.0823 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 14.58 | 0.5880 | 0.0805 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 14.48 | 0.5881 | 0.0845 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 14.66 | 0.5969 | 0.0772 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 14.71 | 0.5960 | 0.0813 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 14.66 | 0.5962 | 0.0794 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.17 | 0.6387 | 0.0745 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.02 | 0.5086 | 0.1163 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.27 | 0.5233 | 0.1059 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 12.04 | 0.5100 | 0.1127 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.11 | 0.5156 | 0.1095 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 12.03 | 0.5108 | 0.1159 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 12.27 | 0.5262 | 0.1053 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 12.04 | 0.5123 | 0.1124 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 12.10 | 0.5178 | 0.1092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 19.10 | 0.6378 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.16 | 0.6490 | 0.0470 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 19.00 | 0.6425 | 0.0506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.09 | 0.6462 | 0.0489 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.21 | 0.6412 | 0.0521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.21 | 0.6529 | 0.0464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.07 | 0.6471 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.16 | 0.6503 | 0.0482 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.44 | 0.6877 | 0.0491 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 18.79 | 0.6149 | 0.0556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.64 | 0.6184 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.62 | 0.6187 | 0.0542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.61 | 0.6178 | 0.0532 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.88 | 0.6214 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 18.69 | 0.6232 | 0.0513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 18.72 | 0.6261 | 0.0533 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 18.68 | 0.6242 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.27 | 0.6775 | 0.0499 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.50 | 0.5907 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.60 | 0.5954 | 0.0530 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 18.42 | 0.5925 | 0.0544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.51 | 0.5940 | 0.0536 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 18.52 | 0.5928 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 18.64 | 0.5981 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 18.45 | 0.5943 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 18.54 | 0.5961 | 0.0532 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 19.08 | 0.6373 | 0.0529 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 19.14 | 0.6484 | 0.0473 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 18.99 | 0.6419 | 0.0509 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 19.08 | 0.6455 | 0.0491 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 19.20 | 0.6408 | 0.0524 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.21 | 0.6524 | 0.0466 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 19.06 | 0.6465 | 0.0502 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 19.15 | 0.6497 | 0.0484 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.43 | 0.6860 | 0.0492 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 18.78 | 0.6146 | 0.0558 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 18.63 | 0.6182 | 0.0521 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 18.61 | 0.6187 | 0.0543 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 18.61 | 0.6178 | 0.0533 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 18.87 | 0.6212 | 0.0549 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 18.69 | 0.6230 | 0.0514 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 18.71 | 0.6261 | 0.0534 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 18.67 | 0.6242 | 0.0526 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.27 | 0.6756 | 0.0499 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.48 | 0.5894 | 0.0555 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.59 | 0.5941 | 0.0533 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 18.40 | 0.5914 | 0.0548 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.50 | 0.5926 | 0.0540 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 18.51 | 0.5915 | 0.0554 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 18.63 | 0.5967 | 0.0527 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 18.44 | 0.5932 | 0.0545 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 18.53 | 0.5949 | 0.0536 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 81.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.38 | 0.7328 | 0.0880 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 12.60 | 0.6969 | 0.2874 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 12.88 | 0.6992 | 0.2532 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 12.69 | 0.7064 | 0.2688 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 12.75 | 0.7038 | 0.2599 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 12.58 | 0.6973 | 0.2872 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 12.87 | 0.7005 | 0.2530 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 12.69 | 0.7078 | 0.2687 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 12.76 | 0.7052 | 0.2596 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 18.72 | 0.6294 | 0.2427 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 12.36 | 0.6935 | 0.2894 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 12.56 | 0.6938 | 0.2569 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 12.46 | 0.7033 | 0.2710 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 12.48 | 0.6995 | 0.2626 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 12.38 | 0.6953 | 0.2896 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 12.53 | 0.6954 | 0.2565 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 12.47 | 0.7054 | 0.2713 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 12.48 | 0.7014 | 0.2626 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.60 | 0.6251 | 0.2437 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.31 | 0.6203 | 0.3692 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.43 | 0.6227 | 0.3433 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.34 | 0.6273 | 0.3552 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.37 | 0.6252 | 0.3486 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 8.31 | 0.6211 | 0.3692 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.43 | 0.6238 | 0.3428 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 8.34 | 0.6279 | 0.3554 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.36 | 0.6258 | 0.3486 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.21 | 0.7487 | 0.0977 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.26 | 0.7517 | 0.0910 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.17 | 0.7510 | 0.0955 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.21 | 0.7515 | 0.0935 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.30 | 0.7494 | 0.0973 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.30 | 0.7525 | 0.0909 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.23 | 0.7519 | 0.0951 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.26 | 0.7523 | 0.0929 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.07 | 0.7561 | 0.0978 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.88 | 0.7450 | 0.1003 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.78 | 0.7468 | 0.0945 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.78 | 0.7472 | 0.0982 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.78 | 0.7470 | 0.0961 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.94 | 0.7462 | 0.0997 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.81 | 0.7478 | 0.0939 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.85 | 0.7486 | 0.0974 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.82 | 0.7482 | 0.0958 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.98 | 0.7548 | 0.0986 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.79 | 0.7420 | 0.0981 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.86 | 0.7437 | 0.0941 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.72 | 0.7433 | 0.0970 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.79 | 0.7436 | 0.0955 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.81 | 0.7424 | 0.0980 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.89 | 0.7441 | 0.0936 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.74 | 0.7437 | 0.0967 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.82 | 0.7439 | 0.0952 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 25.38 | 0.7573 | 0.1425 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.57 | 0.7608 | 0.1229 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.50 | 0.7644 | 0.1328 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.50 | 0.7632 | 0.1271 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.50 | 0.7583 | 0.1420 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.64 | 0.7621 | 0.1224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.57 | 0.7659 | 0.1324 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.57 | 0.7646 | 0.1268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.86 | 0.7526 | 0.1365 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 25.31 | 0.7542 | 0.1449 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.25 | 0.7556 | 0.1260 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.32 | 0.7611 | 0.1355 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.29 | 0.7588 | 0.1299 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.37 | 0.7558 | 0.1441 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.30 | 0.7569 | 0.1252 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.41 | 0.7630 | 0.1349 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.36 | 0.7606 | 0.1296 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.92 | 0.7526 | 0.1362 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.13 | 0.7455 | 0.1367 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.15 | 0.7460 | 0.1230 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.13 | 0.7497 | 0.1275 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.15 | 0.7484 | 0.1238 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.18 | 0.7460 | 0.1366 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.18 | 0.7466 | 0.1227 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.17 | 0.7501 | 0.1276 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.19 | 0.7488 | 0.1238 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 53.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.50 | 0.7200 | 0.0801 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 12.24 | 0.6924 | 0.2602 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 12.47 | 0.6974 | 0.2387 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 12.34 | 0.7030 | 0.2502 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 12.38 | 0.7014 | 0.2437 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 12.23 | 0.6933 | 0.2600 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 12.46 | 0.6994 | 0.2378 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 12.34 | 0.7050 | 0.2490 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 12.38 | 0.7033 | 0.2428 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 20.51 | 0.6766 | 0.2127 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 11.79 | 0.6798 | 0.2735 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 11.96 | 0.6830 | 0.2536 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 11.90 | 0.6914 | 0.2637 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 11.91 | 0.6882 | 0.2582 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 11.81 | 0.6820 | 0.2731 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 11.97 | 0.6852 | 0.2535 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 11.91 | 0.6940 | 0.2638 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 11.93 | 0.6906 | 0.2583 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 19.58 | 0.6482 | 0.2223 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.85 | 0.6206 | 0.3458 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.98 | 0.6281 | 0.3273 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 8.90 | 0.6291 | 0.3377 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 8.93 | 0.6290 | 0.3327 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 8.85 | 0.6211 | 0.3457 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 8.98 | 0.6293 | 0.3265 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 8.90 | 0.6295 | 0.3374 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 8.93 | 0.6295 | 0.3322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 25.46 | 0.7425 | 0.0814 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 25.56 | 0.7474 | 0.0756 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 25.47 | 0.7460 | 0.0792 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 25.52 | 0.7471 | 0.0777 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 25.57 | 0.7436 | 0.0813 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.63 | 0.7488 | 0.0755 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.55 | 0.7475 | 0.0788 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.60 | 0.7485 | 0.0773 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.67 | 0.7571 | 0.0772 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 25.09 | 0.7368 | 0.0841 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 25.03 | 0.7404 | 0.0791 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 25.04 | 0.7405 | 0.0819 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 25.04 | 0.7407 | 0.0806 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 25.14 | 0.7384 | 0.0833 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 25.07 | 0.7417 | 0.0786 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 25.14 | 0.7424 | 0.0813 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 25.09 | 0.7422 | 0.0800 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.53 | 0.7547 | 0.0780 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.03 | 0.7335 | 0.0842 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.08 | 0.7364 | 0.0815 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 24.95 | 0.7355 | 0.0836 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.02 | 0.7362 | 0.0830 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.04 | 0.7341 | 0.0840 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.12 | 0.7370 | 0.0812 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.97 | 0.7360 | 0.0835 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.05 | 0.7367 | 0.0828 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 24.75 | 0.7473 | 0.1090 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 24.99 | 0.7528 | 0.0948 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 24.93 | 0.7552 | 0.1022 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 24.95 | 0.7549 | 0.0981 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 24.87 | 0.7488 | 0.1087 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.07 | 0.7547 | 0.0947 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 25.02 | 0.7573 | 0.1017 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 25.03 | 0.7568 | 0.0976 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.43 | 0.7629 | 0.0921 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 24.55 | 0.7421 | 0.1107 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 24.50 | 0.7454 | 0.0984 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 24.58 | 0.7500 | 0.1048 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 24.54 | 0.7484 | 0.1012 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 24.61 | 0.7442 | 0.1092 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 24.56 | 0.7471 | 0.0971 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 24.69 | 0.7524 | 0.1038 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 24.62 | 0.7505 | 0.1001 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.31 | 0.7603 | 0.0926 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.42 | 0.7356 | 0.1106 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.52 | 0.7386 | 0.1018 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.42 | 0.7408 | 0.1062 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.47 | 0.7404 | 0.1035 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.44 | 0.7361 | 0.1105 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.55 | 0.7392 | 0.1016 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.45 | 0.7413 | 0.1059 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.50 | 0.7409 | 0.1033 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 23.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.07 | 0.7235 | 0.0213 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 6.39 | 0.5447 | 0.1397 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 6.47 | 0.5471 | 0.1311 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 6.42 | 0.5543 | 0.1355 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 6.44 | 0.5518 | 0.1333 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 6.40 | 0.5436 | 0.1397 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.47 | 0.5471 | 0.1311 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 6.42 | 0.5540 | 0.1354 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 6.44 | 0.5518 | 0.1332 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 18.36 | 0.4614 | 0.1070 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 6.20 | 0.5426 | 0.1492 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 6.23 | 0.5390 | 0.1425 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 6.21 | 0.5489 | 0.1459 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 6.21 | 0.5452 | 0.1442 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 6.21 | 0.5429 | 0.1485 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 6.24 | 0.5390 | 0.1424 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 6.22 | 0.5490 | 0.1454 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 6.23 | 0.5452 | 0.1437 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.09 | 0.4343 | 0.1171 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.02 | 0.4902 | 0.1759 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.10 | 0.4906 | 0.1704 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 5.06 | 0.4965 | 0.1734 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.08 | 0.4945 | 0.1719 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 5.02 | 0.4898 | 0.1758 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 5.10 | 0.4914 | 0.1706 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 5.07 | 0.4968 | 0.1734 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 5.08 | 0.4949 | 0.1718 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 31.04 | 0.7233 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.06 | 0.7237 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.06 | 0.7236 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.06 | 0.7237 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 31.04 | 0.7233 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.06 | 0.7237 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.06 | 0.7236 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.06 | 0.7237 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 31.08 | 0.7239 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 31.02 | 0.7230 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 31.06 | 0.7234 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 31.05 | 0.7232 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 31.06 | 0.7234 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 31.01 | 0.7230 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 31.06 | 0.7234 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 31.05 | 0.7232 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 31.06 | 0.7234 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 31.08 | 0.7238 | 0.0213 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 31.05 | 0.7233 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 31.05 | 0.7235 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 31.07 | 0.7235 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 31.07 | 0.7236 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 31.05 | 0.7234 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.05 | 0.7236 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.07 | 0.7236 | 0.0214 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.07 | 0.7236 | 0.0214 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 30.79 | 0.7272 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 31.07 | 0.7294 | 0.0236 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 31.12 | 0.7307 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 31.10 | 0.7303 | 0.0238 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 30.80 | 0.7272 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.09 | 0.7294 | 0.0235 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 31.14 | 0.7309 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 31.12 | 0.7304 | 0.0238 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 31.22 | 0.7294 | 0.0227 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 30.56 | 0.7257 | 0.0249 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.71 | 0.7272 | 0.0236 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.69 | 0.7290 | 0.0242 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.70 | 0.7284 | 0.0239 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.54 | 0.7258 | 0.0249 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.70 | 0.7272 | 0.0235 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.66 | 0.7289 | 0.0242 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.68 | 0.7282 | 0.0239 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 31.20 | 0.7297 | 0.0224 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.06 | 0.7269 | 0.0245 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 31.08 | 0.7279 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 31.17 | 0.7290 | 0.0239 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 31.16 | 0.7286 | 0.0237 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 31.06 | 0.7268 | 0.0243 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 31.07 | 0.7280 | 0.0240 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 31.18 | 0.7290 | 0.0239 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 31.17 | 0.7287 | 0.0236 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.12 | 0.7461 | 0.1075 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 11.36 | 0.6983 | 0.3593 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 11.53 | 0.6993 | 0.3193 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 11.41 | 0.7059 | 0.3367 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 11.45 | 0.7035 | 0.3266 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 11.36 | 0.6988 | 0.3587 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.53 | 0.7009 | 0.3188 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 11.42 | 0.7074 | 0.3356 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 11.46 | 0.7050 | 0.3254 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 19.00 | 0.6342 | 0.2795 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 11.12 | 0.6885 | 0.3691 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 11.25 | 0.6874 | 0.3328 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 11.18 | 0.6962 | 0.3476 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 11.19 | 0.6926 | 0.3384 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 11.14 | 0.6903 | 0.3689 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 11.23 | 0.6890 | 0.3316 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 11.19 | 0.6981 | 0.3478 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 11.20 | 0.6944 | 0.3382 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 18.57 | 0.6097 | 0.2877 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.90 | 0.6259 | 0.4299 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 7.97 | 0.6275 | 0.4001 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 7.91 | 0.6310 | 0.4132 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.93 | 0.6296 | 0.4057 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 7.90 | 0.6265 | 0.4305 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 7.97 | 0.6287 | 0.3999 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 7.91 | 0.6316 | 0.4138 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 7.93 | 0.6302 | 0.4057 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.01 | 0.7613 | 0.1145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.03 | 0.7635 | 0.1070 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.96 | 0.7629 | 0.1116 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.99 | 0.7634 | 0.1096 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.10 | 0.7621 | 0.1145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.09 | 0.7644 | 0.1069 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.03 | 0.7639 | 0.1114 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.05 | 0.7642 | 0.1092 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 28.01 | 0.7709 | 0.1088 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.72 | 0.7581 | 0.1167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.61 | 0.7595 | 0.1108 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.63 | 0.7600 | 0.1145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.62 | 0.7598 | 0.1126 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.78 | 0.7593 | 0.1161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.65 | 0.7604 | 0.1104 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.70 | 0.7612 | 0.1137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.66 | 0.7608 | 0.1122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.90 | 0.7695 | 0.1094 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.62 | 0.7556 | 0.1154 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.68 | 0.7570 | 0.1117 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.55 | 0.7566 | 0.1140 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.63 | 0.7569 | 0.1129 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.64 | 0.7560 | 0.1152 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.72 | 0.7574 | 0.1113 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.57 | 0.7569 | 0.1139 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.65 | 0.7572 | 0.1127 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.31 | 0.7707 | 0.1630 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.46 | 0.7721 | 0.1407 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.42 | 0.7752 | 0.1516 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.40 | 0.7742 | 0.1454 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.43 | 0.7717 | 0.1629 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.53 | 0.7734 | 0.1406 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.50 | 0.7767 | 0.1512 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.47 | 0.7755 | 0.1450 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 27.83 | 0.7799 | 0.1343 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.25 | 0.7677 | 0.1644 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.14 | 0.7675 | 0.1449 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.23 | 0.7723 | 0.1548 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.19 | 0.7703 | 0.1490 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.32 | 0.7692 | 0.1633 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.20 | 0.7688 | 0.1437 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.32 | 0.7741 | 0.1539 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.26 | 0.7719 | 0.1481 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 27.77 | 0.7785 | 0.1333 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.00 | 0.7602 | 0.1576 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.05 | 0.7607 | 0.1420 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 26.00 | 0.7634 | 0.1481 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.03 | 0.7625 | 0.1439 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 26.04 | 0.7606 | 0.1576 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.08 | 0.7612 | 0.1419 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.05 | 0.7638 | 0.1481 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.07 | 0.7629 | 0.1438 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 418340 | 0.338 | 72.0 | 33.39 | 0.20 | 0.005 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 418340 | 0.338 | 50.7 | 33.39 | 0.20 | 0.005 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 418340 | 0.338 | 56.4 | 33.39 | 0.20 | 0.005 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 418340 | 0.338 | 76.3 | 33.39 | 0.20 | 0.005 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 418530 | 0.326 | 61.5 | 33.44 | 0.19 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 418530 | 0.326 | 64.6 | 33.44 | 0.19 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 418530 | 0.326 | 51.4 | 33.44 | 0.19 | 0.006 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 418530 | 0.326 | 73.2 | 33.44 | 0.19 | 0.006 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 3678872 | 0.812 | 532.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 423571 | 0.331 | 77.8 | 33.23 | 0.10 | 0.007 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 423571 | 0.331 | 57.0 | 33.23 | 0.10 | 0.007 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 423571 | 0.331 | 50.9 | 33.23 | 0.10 | 0.007 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 423571 | 0.331 | 46.1 | 33.23 | 0.10 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 422962 | 0.324 | 68.1 | 33.18 | 0.10 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 422962 | 0.324 | 62.0 | 33.18 | 0.10 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 422962 | 0.324 | 67.1 | 33.18 | 0.10 | 0.008 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 422962 | 0.324 | 66.8 | 33.18 | 0.10 | 0.008 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 3604170 | 0.812 | 159.1 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 423308 | 0.860 | 83.1 | 33.51 | 0.08 | 0.004 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 423308 | 0.860 | 77.7 | 33.51 | 0.08 | 0.004 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 423308 | 0.860 | 77.4 | 33.51 | 0.08 | 0.004 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 423308 | 0.860 | 57.1 | 33.51 | 0.08 | 0.004 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 421511 | 0.330 | 63.8 | 33.53 | 0.07 | 0.004 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 421511 | 0.330 | 63.9 | 33.53 | 0.07 | 0.004 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 421511 | 0.330 | 70.4 | 33.53 | 0.07 | 0.004 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 421511 | 0.330 | 79.6 | 33.53 | 0.07 | 0.004 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.680 | 0.049 |
| in035 | mask_ent | 0.806 | 0.049 |
| in035 | mask_grad | 0.489 | 0.049 |
| in035 | r_col | 0.620 | 0.049 |
| in035 | r_warp | 0.812 | 0.049 |

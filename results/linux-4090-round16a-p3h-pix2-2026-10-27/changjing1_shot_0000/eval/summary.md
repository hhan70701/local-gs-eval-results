# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 81.8% | 23.97 / 0.1169 | 26.82 / 0.1488 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 82.2% | 24.00 / 0.1182 | 27.13 / 0.1301 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 82.2% | 24.00 / 0.1177 | 27.18 / 0.1394 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 82.2% | 24.00 / 0.1177 | 27.16 / 0.1332 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 81.5% | 23.96 / 0.1166 | 26.76 / 0.1482 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 81.7% | 24.00 / 0.1172 | 26.58 / 0.1350 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 81.9% | 23.98 / 0.1173 | 26.73 / 0.1384 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 81.8% | 23.99 / 0.1178 | 26.63 / 0.1344 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 83.9% | 24.00 / 0.1241 | 23.10 / 0.2332 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 78.8% | 23.84 / 0.1262 | 23.72 / 0.2318 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 21.4% | 19.33 / 0.0816 | 18.96 / 0.1605 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 78.8% | 23.83 / 0.1253 | 23.72 / 0.2464 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 20.6% | 19.15 / 0.0790 | 19.01 / 0.1629 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 83.9% | 23.99 / 0.1240 | 23.19 / 0.1759 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 78.1% | 23.84 / 0.1264 | 24.02 / 0.2171 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 21.2% | 19.36 / 0.0811 | 19.27 / 0.1479 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 78.5% | 23.81 / 0.1255 | 23.91 / 0.2214 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 21.1% | 19.29 / 0.0773 | 19.18 / 0.1510 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 83.0% | 23.92 / 0.1245 | 23.55 / 0.2335 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 78.9% | 23.80 / 0.1237 | 26.61 / 0.1524 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 79.3% | 23.82 / 0.1244 | 26.70 / 0.1395 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 79.3% | 23.81 / 0.1239 | 26.81 / 0.1429 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 79.3% | 23.81 / 0.1245 | 26.79 / 0.1410 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 78.7% | 23.78 / 0.1236 | 26.76 / 0.1537 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 78.9% | 23.80 / 0.1243 | 26.75 / 0.1438 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 79.2% | 23.80 / 0.1246 | 26.92 / 0.1437 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 79.1% | 23.80 / 0.1250 | 26.86 / 0.1428 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 81.2% | 23.87 / 0.1260 | 23.93 / 0.2299 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 51.7% | 23.40 / 0.1115 | 24.00 / 0.1516 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 54.4% | 23.56 / 0.1157 | 24.74 / 0.1511 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 52.9% | 23.48 / 0.1119 | 24.42 / 0.1491 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 53.1% | 23.49 / 0.1125 | 24.57 / 0.1470 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 51.5% | 23.41 / 0.1134 | 23.57 / 0.1524 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 53.1% | 23.53 / 0.1138 | 24.03 / 0.1484 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 52.8% | 23.53 / 0.1132 | 23.75 / 0.1538 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 52.8% | 23.52 / 0.1141 | 23.86 / 0.1510 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 24.96 / 0.1359 | 23.49 / 0.1733 | 17.51 / 0.0966 | 34.19 / 0.0162 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.75 / 0.1790 | 26.80 / 0.1868 | 21.48 / 0.0683 | 33.97 / 0.0319 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.22 / 0.1557 | 27.23 / 0.1718 | 22.06 / 0.0587 | 32.04 / 0.0329 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.18 / 0.1670 | 27.05 / 0.1823 | 21.94 / 0.0634 | 33.32 / 0.0324 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.25 / 0.1596 | 27.13 / 0.1756 | 22.04 / 0.0607 | 32.79 / 0.0321 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.75 / 0.1764 | 26.77 / 0.1881 | 21.70 / 0.0671 | 34.19 / 0.0276 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.59 / 0.1597 | 26.82 / 0.1747 | 21.58 / 0.0629 | 31.85 / 0.0328 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.75 / 0.1668 | 26.74 / 0.1825 | 21.63 / 0.0643 | 33.20 / 0.0309 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.67 / 0.1613 | 26.74 / 0.1770 | 21.57 / 0.0635 | 32.33 / 0.0310 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.37 / 0.2006 | 23.21 / 0.2613 | 18.84 / 0.1001 | 33.87 / 0.0195 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.28 / 0.2284 | 24.70 / 0.2524 | 20.40 / 0.1102 | 27.95 / 0.0674 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.09 / 0.1991 | 24.38 / 0.2246 | 20.01 / 0.1090 | 28.67 / 0.0585 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.52 / 0.2368 | 25.03 / 0.2661 | 20.61 / 0.1119 | 26.98 / 0.0674 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.47 / 0.2017 | 24.82 / 0.2379 | 20.23 / 0.1117 | 29.48 / 0.0576 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.57 / 0.1450 | 23.44 / 0.1942 | 18.83 / 0.0819 | 33.38 / 0.0198 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.35 / 0.2146 | 24.56 / 0.2386 | 20.10 / 0.0981 | 28.96 / 0.0674 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.13 / 0.1898 | 24.29 / 0.2118 | 19.75 / 0.0998 | 29.90 / 0.0628 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.41 / 0.2145 | 24.72 / 0.2397 | 20.29 / 0.0968 | 27.82 / 0.0657 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.21 / 0.1897 | 24.45 / 0.2176 | 19.90 / 0.0990 | 29.71 / 0.0604 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.53 / 0.2023 | 24.59 / 0.2574 | 20.86 / 0.1033 | 31.98 / 0.0280 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.53 / 0.1772 | 26.97 / 0.1785 | 21.49 / 0.0667 | 30.47 / 0.0343 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.77 / 0.1600 | 27.23 / 0.1718 | 21.66 / 0.0616 | 30.96 / 0.0331 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.82 / 0.1656 | 27.12 / 0.1757 | 21.67 / 0.0644 | 30.62 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.85 / 0.1610 | 27.19 / 0.1730 | 21.69 / 0.0625 | 30.59 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.66 / 0.1747 | 27.16 / 0.1779 | 21.74 / 0.0644 | 30.77 / 0.0342 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.64 / 0.1592 | 27.35 / 0.1703 | 21.69 / 0.0601 | 30.51 / 0.0340 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.84 / 0.1633 | 27.23 / 0.1740 | 21.79 / 0.0614 | 30.82 / 0.0345 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.80 / 0.1596 | 27.25 / 0.1711 | 21.79 / 0.0602 | 30.74 / 0.0344 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.57 / 0.2019 | 24.57 / 0.2583 | 20.92 / 0.1040 | 31.54 / 0.0311 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 25.49 / 0.1904 | 25.61 / 0.1910 | 20.11 / 0.0780 | 28.04 / 0.0501 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.66 / 0.1859 | 25.47 / 0.1820 | 20.22 / 0.0719 | 27.70 / 0.0555 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.64 / 0.1853 | 25.50 / 0.1852 | 20.20 / 0.0759 | 28.22 / 0.0515 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.66 / 0.1830 | 25.48 / 0.1824 | 20.19 / 0.0752 | 27.90 / 0.0523 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.27 / 0.1907 | 25.23 / 0.1913 | 19.96 / 0.0796 | 28.33 / 0.0464 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.24 / 0.1875 | 25.00 / 0.1851 | 19.84 / 0.0766 | 27.38 / 0.0531 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.24 / 0.1885 | 24.97 / 0.1909 | 19.86 / 0.0796 | 27.94 / 0.0503 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.24 / 0.1868 | 24.96 / 0.1866 | 19.84 / 0.0784 | 27.61 / 0.0511 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 15.3%） | — | — | 24.96 / 0.1359 | 23.49 / 0.1733 | 34.19 |
| in035 | rife | 34.0% | 51.7% | 25.49 / 0.1904 | 25.61 / 0.1910 | 28.04 |
| in035 | cnw_cnn | 59.3% | 81.8% | 27.75 / 0.1790 | 26.80 / 0.1868 | 33.97 |
| in035 | cnw_f5 | 60.4% | 78.9% | 27.53 / 0.1772 | 26.97 / 0.1785 | 30.47 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 24.79 / 0.1237 | +0.90 / +0.0576 (core 34.9%) | +2.13 / +0.0714 (core 70.0%) | +2.13 / +0.0640 (core 72.5%) |
| in035 | 2 | 0-3 | 24.91 / 0.1257 | -0.46 / +0.0580 (core 34.9%) | +3.58 / +0.0516 (core 70.0%) | +2.83 / +0.0646 (core 72.5%) |
| in035 | 4 | 3-5 | 25.19 / 0.1582 | +1.13 / +0.0480 (core 27.1%) | +2.65 / +0.0063 (core 35.2%) | +2.73 / -0.0047 (core 32.2%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 24.96 / 0.1359 | 23.49 | 34.19 | — |
| in035 | cnw_cnn | 不复核 | —% | 27.75 / 0.1790 | 26.80 | 33.97 | 0/3 |
| in035 | cnw_cnn | oracle | 13.5% | 27.99 / 0.1218 | 27.03 | 34.05 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.22 / 0.1557 | 27.23 | 32.04 | 1/3 |
| in035 | cnw_cnn | oracle | 13.5% | 28.43 / 0.1128 | 27.45 | 33.98 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.18 / 0.1670 | 27.05 | 33.32 | 0/3 |
| in035 | cnw_cnn | oracle | 13.5% | 28.34 / 0.1177 | 27.24 | 34.01 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.25 / 0.1596 | 27.13 | 32.79 | 0/3 |
| in035 | cnw_cnn | oracle | 13.5% | 28.41 / 0.1154 | 27.32 | 34.01 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.75 / 0.1764 | 26.77 | 34.19 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 13.5% | 28.12 / 0.1210 | 27.09 | 34.06 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.59 / 0.1597 | 26.82 | 31.85 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 13.5% | 28.03 / 0.1151 | 27.15 | 33.88 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.75 / 0.1668 | 26.74 | 33.20 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 13.5% | 28.08 / 0.1188 | 27.05 | 33.95 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.67 / 0.1613 | 26.74 | 32.33 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 13.5% | 28.03 / 0.1172 | 27.04 | 33.91 | 3/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 25.37 / 0.2006 | 23.21 | 33.87 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 13.7% | 25.86 / 0.1542 | 23.79 | 34.10 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 25.28 / 0.2284 | 24.70 | 27.95 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 13.4% | 27.02 / 0.1628 | 25.43 | 33.94 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 25.09 / 0.1991 | 24.38 | 28.67 | 0/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 9.7% | 26.71 / 0.1563 | 25.04 | 33.99 | 0/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 25.52 / 0.2368 | 25.03 | 26.98 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 13.4% | 27.24 / 0.1659 | 25.67 | 33.94 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 25.47 / 0.2017 | 24.82 | 29.48 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 9.6% | 26.95 / 0.1588 | 25.31 | 33.97 | 0/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 25.57 / 0.1450 | 23.44 | 33.38 | 1/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 13.7% | 25.88 / 0.1299 | 23.84 | 34.05 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 25.35 / 0.2146 | 24.56 | 28.96 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 13.3% | 26.82 / 0.1513 | 25.23 | 34.04 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 25.13 / 0.1898 | 24.29 | 29.90 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 9.5% | 26.54 / 0.1458 | 24.90 | 34.06 | 0/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 25.41 / 0.2145 | 24.72 | 27.82 | 0/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 13.5% | 27.00 / 0.1494 | 25.47 | 34.07 | 1/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 25.21 / 0.1897 | 24.45 | 29.71 | 0/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 9.4% | 26.71 / 0.1447 | 25.11 | 34.07 | 1/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 26.53 / 0.2023 | 24.59 | 31.98 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 14.0% | 27.44 / 0.1556 | 25.78 | 33.94 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.53 / 0.1772 | 26.97 | 30.47 | 1/3 |
| in035 | cnw_f5 | oracle | 13.2% | 27.98 / 0.1207 | 27.15 | 33.91 | 2/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.77 / 0.1600 | 27.23 | 30.96 | 1/3 |
| in035 | cnw_f5 | oracle | 13.2% | 28.14 / 0.1150 | 27.36 | 33.79 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.82 / 0.1656 | 27.12 | 30.62 | 1/3 |
| in035 | cnw_f5 | oracle | 13.2% | 28.16 / 0.1182 | 27.25 | 33.78 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.85 / 0.1610 | 27.19 | 30.59 | 1/3 |
| in035 | cnw_f5 | oracle | 13.2% | 28.17 / 0.1164 | 27.30 | 33.84 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.66 / 0.1747 | 27.16 | 30.77 | 1/3 |
| in035 | cnw_f5_mw | oracle | 13.2% | 28.15 / 0.1176 | 27.35 | 33.96 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.64 / 0.1592 | 27.35 | 30.51 | 1/3 |
| in035 | cnw_f5_mw | oracle | 13.2% | 28.15 / 0.1123 | 27.56 | 33.83 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.84 / 0.1633 | 27.23 | 30.82 | 1/3 |
| in035 | cnw_f5_mw | oracle | 13.2% | 28.25 / 0.1153 | 27.42 | 33.86 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 27.80 / 0.1596 | 27.25 | 30.74 | 1/3 |
| in035 | cnw_f5_mw | oracle | 13.2% | 28.23 / 0.1137 | 27.46 | 33.91 | 3/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 26.57 / 0.2019 | 24.57 | 31.54 | 0/3 |
| in035 | cnw_f5_pix | oracle | 13.5% | 27.49 / 0.1558 | 25.72 | 33.92 | 1/3 |
| in035 | rife | 不复核 | —% | 25.49 / 0.1904 | 25.61 | 28.04 | 0/3 |
| in035 | rife | oracle | 9.8% | 26.89 / 0.1281 | 26.36 | 33.77 | 1/3 |
| in035 | rife | 不复核 | —% | 25.66 / 0.1859 | 25.47 | 27.70 | 0/3 |
| in035 | rife | oracle | 10.1% | 27.04 / 0.1210 | 26.33 | 33.73 | 3/3 |
| in035 | rife | 不复核 | —% | 25.64 / 0.1853 | 25.50 | 28.22 | 0/3 |
| in035 | rife | oracle | 9.9% | 27.01 / 0.1250 | 26.29 | 33.78 | 3/3 |
| in035 | rife | 不复核 | —% | 25.66 / 0.1830 | 25.48 | 27.90 | 0/3 |
| in035 | rife | oracle | 10.0% | 27.01 / 0.1236 | 26.26 | 33.73 | 3/3 |
| in035 | rife_mw | 不复核 | —% | 25.27 / 0.1907 | 25.23 | 28.33 | 0/3 |
| in035 | rife_mw | oracle | 9.7% | 26.72 / 0.1296 | 26.17 | 33.59 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 25.24 / 0.1875 | 25.00 | 27.38 | 0/3 |
| in035 | rife_mw | oracle | 10.0% | 26.68 / 0.1251 | 25.94 | 33.50 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 25.24 / 0.1885 | 24.97 | 27.94 | 0/3 |
| in035 | rife_mw | oracle | 9.8% | 26.68 / 0.1276 | 25.91 | 33.49 | 2/3 |
| in035 | rife_mw | 不复核 | —% | 25.24 / 0.1868 | 24.96 | 27.61 | 0/3 |
| in035 | rife_mw | oracle | 9.9% | 26.66 / 0.1262 | 25.89 | 33.48 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 24.96 / 0.1359 | 23.49 / 0.1733 | — |
| in035 | FF | 0（前馈） | 892×811（70%） | 32.31 | 27.75 / 0.1790 | 26.80 / 0.1868 | 0/3 |
| in035 | 25 | 0.66 s | 892×811（70%） | 34.66 | 28.18 / 0.1670 | 27.05 / 0.1823 | 0/3 |
| in035 | 50 | 1.31 s | 892×811（70%） | 35.58 | 28.25 / 0.1596 | 27.13 / 0.1756 | 0/3 |
| in035 | 100 | 2.59 s | 892×811（70%） | 36.53 | 28.22 / 0.1557 | 27.23 / 0.1718 | 1/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 24.96 / 0.1359 | 23.49 / 0.1733 | 34.19 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 27.75 / 0.1790 | 26.80 / 0.1868 | 33.97 | 0/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.99 / 0.1218 | 27.03 / 0.1430 | 34.05 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.18 / 0.1670 | 27.05 / 0.1823 | 33.32 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 28.34 / 0.1177 | 27.24 / 0.1408 | 34.01 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 28.25 / 0.1596 | 27.13 / 0.1756 | 32.79 | 0/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 28.41 / 0.1154 | 27.32 / 0.1386 | 34.01 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 28.22 / 0.1557 | 27.23 / 0.1718 | 32.04 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 28.43 / 0.1128 | 27.45 / 0.1350 | 33.98 | 3/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.75 / 0.1764 | 26.77 / 0.1881 | 34.19 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 28.12 / 0.1210 | 27.09 / 0.1427 | 34.06 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 27.75 / 0.1668 | 26.74 / 0.1825 | 33.20 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 28.08 / 0.1188 | 27.05 / 0.1413 | 33.95 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 27.67 / 0.1613 | 26.74 / 0.1770 | 32.33 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 28.03 / 0.1172 | 27.04 / 0.1397 | 33.91 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.59 / 0.1597 | 26.82 / 0.1747 | 31.85 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.03 / 0.1151 | 27.15 / 0.1372 | 33.88 | 3/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 27.53 / 0.1772 | 26.97 / 0.1785 | 30.47 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.98 / 0.1207 | 27.15 / 0.1392 | 33.91 | 2/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.82 / 0.1656 | 27.12 / 0.1757 | 30.62 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 28.16 / 0.1182 | 27.25 / 0.1378 | 33.78 | 3/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.85 / 0.1610 | 27.19 / 0.1730 | 30.59 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 28.17 / 0.1164 | 27.30 / 0.1366 | 33.84 | 3/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.77 / 0.1600 | 27.23 / 0.1718 | 30.96 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 28.14 / 0.1150 | 27.36 / 0.1345 | 33.79 | 3/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 27.66 / 0.1747 | 27.16 / 0.1779 | 30.77 | 1/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 28.15 / 0.1176 | 27.35 / 0.1389 | 33.96 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 27.84 / 0.1633 | 27.23 / 0.1740 | 30.82 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 28.25 / 0.1153 | 27.42 / 0.1360 | 33.86 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 27.80 / 0.1596 | 27.25 / 0.1711 | 30.74 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 28.23 / 0.1137 | 27.46 / 0.1349 | 33.91 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 27.64 / 0.1592 | 27.35 / 0.1703 | 30.51 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 28.15 / 0.1123 | 27.56 / 0.1330 | 33.83 | 3/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 25.49 / 0.1904 | 25.61 / 0.1910 | 28.04 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 26.89 / 0.1281 | 26.36 / 0.1477 | 33.77 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 25.64 / 0.1853 | 25.50 / 0.1852 | 28.22 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 27.01 / 0.1250 | 26.29 / 0.1435 | 33.78 | 3/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 25.66 / 0.1830 | 25.48 / 0.1824 | 27.90 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 27.01 / 0.1236 | 26.26 / 0.1412 | 33.73 | 3/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 25.66 / 0.1859 | 25.47 / 0.1820 | 27.70 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 27.04 / 0.1210 | 26.33 / 0.1371 | 33.73 | 3/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 25.27 / 0.1907 | 25.23 / 0.1913 | 28.33 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 26.72 / 0.1296 | 26.17 / 0.1475 | 33.59 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 25.24 / 0.1885 | 24.97 / 0.1909 | 27.94 | 0/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 26.68 / 0.1276 | 25.91 / 0.1462 | 33.49 | 2/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 25.24 / 0.1868 | 24.96 / 0.1866 | 27.61 | 0/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 26.66 / 0.1262 | 25.89 / 0.1433 | 33.48 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 25.24 / 0.1875 | 25.00 / 0.1851 | 27.38 | 0/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 26.68 / 0.1251 | 25.94 / 0.1410 | 33.50 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.49 / 0.1733 | 17.51 / 0.0966 | 34.19 / 0.0162 | 24.96 / 0.1359 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 53.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.49 | 0.7647 | 0.1733 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 23.78 | 0.8260 | 0.2159 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 24.86 | 0.8248 | 0.1961 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 24.15 | 0.8268 | 0.2089 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 24.40 | 0.8263 | 0.2021 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 23.88 | 0.8215 | 0.2166 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 24.83 | 0.8130 | 0.1951 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 24.12 | 0.8194 | 0.2091 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 24.36 | 0.8162 | 0.2011 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 23.21 | 0.7092 | 0.2661 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 24.79 | 0.7477 | 0.2537 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 24.79 | 0.7477 | 0.2537 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 25.09 | 0.7407 | 0.2654 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 25.09 | 0.7407 | 0.2654 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 23.37 | 0.7715 | 0.1991 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 24.21 | 0.7604 | 0.2529 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 24.21 | 0.7604 | 0.2529 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 24.30 | 0.7583 | 0.2512 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 24.30 | 0.7583 | 0.2512 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 24.24 | 0.7644 | 0.2719 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 24.97 | 0.8313 | 0.1988 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 25.44 | 0.8230 | 0.1890 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 25.15 | 0.8284 | 0.1941 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 25.19 | 0.8265 | 0.1905 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 25.26 | 0.8310 | 0.2001 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 25.79 | 0.8217 | 0.1879 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 25.33 | 0.8295 | 0.1937 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 25.42 | 0.8260 | 0.1897 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 24.16 | 0.7621 | 0.2785 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 20.45 | 0.8002 | 0.2502 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 20.69 | 0.7907 | 0.2319 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 20.32 | 0.7974 | 0.2429 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 20.43 | 0.7944 | 0.2378 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 20.34 | 0.7934 | 0.2520 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 20.33 | 0.7787 | 0.2383 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 20.05 | 0.7852 | 0.2475 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 20.13 | 0.7821 | 0.2422 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.03 | 0.8175 | 0.1430 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.45 | 0.8218 | 0.1350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.24 | 0.8199 | 0.1408 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.32 | 0.8210 | 0.1386 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.09 | 0.8155 | 0.1427 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.15 | 0.8155 | 0.1372 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.05 | 0.8153 | 0.1413 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.04 | 0.8150 | 0.1397 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.79 | 0.7684 | 0.2046 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.43 | 0.7789 | 0.2149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.04 | 0.7736 | 0.2064 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.67 | 0.7784 | 0.2240 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.31 | 0.7730 | 0.2168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.84 | 0.7824 | 0.1738 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.23 | 0.7796 | 0.2027 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.90 | 0.7741 | 0.1945 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.47 | 0.7827 | 0.1995 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.11 | 0.7768 | 0.1934 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.78 | 0.7836 | 0.2036 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.15 | 0.8196 | 0.1392 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.36 | 0.8195 | 0.1345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.25 | 0.8195 | 0.1378 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.30 | 0.8195 | 0.1366 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.35 | 0.8199 | 0.1389 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.56 | 0.8212 | 0.1330 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.42 | 0.8211 | 0.1360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.46 | 0.8211 | 0.1349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.72 | 0.7834 | 0.2040 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.36 | 0.8086 | 0.1477 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.33 | 0.8079 | 0.1371 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.29 | 0.8081 | 0.1435 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.26 | 0.8078 | 0.1412 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.17 | 0.8042 | 0.1475 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.94 | 0.8013 | 0.1410 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.91 | 0.8009 | 0.1462 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.89 | 0.8011 | 0.1433 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.80 | 0.8291 | 0.1868 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.23 | 0.8281 | 0.1718 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.05 | 0.8305 | 0.1823 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.13 | 0.8300 | 0.1756 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.77 | 0.8232 | 0.1881 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.82 | 0.8150 | 0.1747 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.74 | 0.8213 | 0.1825 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.74 | 0.8184 | 0.1770 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.21 | 0.7165 | 0.2613 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.70 | 0.7470 | 0.2524 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.38 | 0.7581 | 0.2246 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.03 | 0.7406 | 0.2661 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.82 | 0.7610 | 0.2379 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.44 | 0.7733 | 0.1942 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.56 | 0.7623 | 0.2386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.29 | 0.7611 | 0.2118 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.72 | 0.7592 | 0.2397 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.45 | 0.7625 | 0.2176 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.59 | 0.7676 | 0.2574 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.97 | 0.8330 | 0.1785 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.23 | 0.8262 | 0.1718 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.12 | 0.8314 | 0.1757 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.19 | 0.8297 | 0.1730 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.16 | 0.8324 | 0.1779 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.35 | 0.8246 | 0.1703 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.23 | 0.8319 | 0.1740 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.25 | 0.8289 | 0.1711 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.57 | 0.7674 | 0.2583 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.61 | 0.8123 | 0.1910 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.47 | 0.8042 | 0.1820 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.50 | 0.8101 | 0.1852 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.48 | 0.8079 | 0.1824 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.23 | 0.8046 | 0.1913 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.00 | 0.7924 | 0.1851 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.97 | 0.7975 | 0.1909 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.96 | 0.7952 | 0.1866 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 15.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.51 | 0.4912 | 0.0966 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 21.00 | 0.6911 | 0.0694 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 22.10 | 0.7112 | 0.0578 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 21.81 | 0.7059 | 0.0639 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 21.94 | 0.7089 | 0.0610 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 21.29 | 0.6976 | 0.0686 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 21.79 | 0.6941 | 0.0633 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 21.69 | 0.6983 | 0.0654 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 21.67 | 0.6935 | 0.0643 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 18.82 | 0.5731 | 0.1017 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 20.65 | 0.6023 | 0.1113 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 20.65 | 0.6023 | 0.1113 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 20.66 | 0.5939 | 0.1144 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 20.66 | 0.5939 | 0.1144 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 18.83 | 0.6107 | 0.0828 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 20.04 | 0.5987 | 0.1063 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.04 | 0.5987 | 0.1063 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 19.94 | 0.6007 | 0.1038 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 19.94 | 0.6007 | 0.1038 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 21.20 | 0.6204 | 0.1050 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 20.86 | 0.6902 | 0.0671 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 21.42 | 0.6904 | 0.0624 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 21.38 | 0.6931 | 0.0644 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 21.34 | 0.6905 | 0.0628 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 21.33 | 0.6987 | 0.0660 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 21.78 | 0.6973 | 0.0613 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 21.84 | 0.7043 | 0.0626 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 21.79 | 0.7003 | 0.0615 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 21.37 | 0.6224 | 0.1041 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 17.21 | 0.6387 | 0.0980 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 17.61 | 0.6235 | 0.0928 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 17.37 | 0.6342 | 0.0961 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 17.41 | 0.6278 | 0.0950 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 17.37 | 0.6294 | 0.1001 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 17.69 | 0.6037 | 0.0992 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 17.48 | 0.6152 | 0.1005 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 17.52 | 0.6091 | 0.1005 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 21.48 | 0.6874 | 0.0683 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.06 | 0.7054 | 0.0587 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.94 | 0.7005 | 0.0635 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.03 | 0.7045 | 0.0608 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.70 | 0.6912 | 0.0672 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.58 | 0.6830 | 0.0628 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.63 | 0.6875 | 0.0644 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.57 | 0.6844 | 0.0635 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 18.84 | 0.5878 | 0.1003 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.41 | 0.6049 | 0.1097 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.01 | 0.5882 | 0.1087 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.61 | 0.6015 | 0.1113 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.23 | 0.5837 | 0.1112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 18.83 | 0.6209 | 0.0821 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.11 | 0.6060 | 0.0975 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.75 | 0.5883 | 0.0993 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.29 | 0.6122 | 0.0962 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.90 | 0.5938 | 0.0987 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.88 | 0.6245 | 0.1026 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 21.51 | 0.6892 | 0.0667 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.68 | 0.6883 | 0.0617 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.69 | 0.6909 | 0.0643 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.71 | 0.6896 | 0.0625 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.75 | 0.6961 | 0.0643 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.72 | 0.6912 | 0.0600 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.82 | 0.6981 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.81 | 0.6959 | 0.0601 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.92 | 0.6230 | 0.1036 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.09 | 0.6206 | 0.0781 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.21 | 0.6207 | 0.0719 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.18 | 0.6225 | 0.0759 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.18 | 0.6214 | 0.0752 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 19.94 | 0.6083 | 0.0795 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.83 | 0.5979 | 0.0765 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.84 | 0.5994 | 0.0792 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.83 | 0.5988 | 0.0784 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 21.48 | 0.6863 | 0.0683 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 22.06 | 0.7037 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 21.94 | 0.6989 | 0.0634 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.04 | 0.7028 | 0.0607 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.70 | 0.6899 | 0.0671 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.58 | 0.6814 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 21.63 | 0.6859 | 0.0643 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 21.57 | 0.6827 | 0.0635 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 18.84 | 0.5845 | 0.1001 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 20.40 | 0.5991 | 0.1102 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.01 | 0.5827 | 0.1090 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 20.61 | 0.5959 | 0.1119 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.23 | 0.5787 | 0.1117 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 18.83 | 0.6181 | 0.0819 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.10 | 0.6009 | 0.0981 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.75 | 0.5837 | 0.0998 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 20.29 | 0.6076 | 0.0968 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 19.90 | 0.5895 | 0.0990 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.86 | 0.6187 | 0.1033 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 21.49 | 0.6880 | 0.0667 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.66 | 0.6860 | 0.0616 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 21.67 | 0.6888 | 0.0644 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 21.69 | 0.6873 | 0.0625 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 21.74 | 0.6956 | 0.0644 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 21.69 | 0.6895 | 0.0601 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 21.79 | 0.6968 | 0.0614 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 21.79 | 0.6943 | 0.0602 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.92 | 0.6181 | 0.1040 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.11 | 0.6186 | 0.0780 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.22 | 0.6178 | 0.0719 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.20 | 0.6193 | 0.0759 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.19 | 0.6183 | 0.0752 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 19.96 | 0.6064 | 0.0796 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 19.84 | 0.5946 | 0.0766 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 19.86 | 0.5960 | 0.0796 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 19.84 | 0.5956 | 0.0784 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 91.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.28 | 0.7857 | 0.1292 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 20.36 | 0.8155 | 0.1999 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 22.00 | 0.8201 | 0.1715 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 20.84 | 0.8206 | 0.1864 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 21.26 | 0.8208 | 0.1784 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 20.26 | 0.8098 | 0.2024 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 21.56 | 0.8039 | 0.1774 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 20.64 | 0.8107 | 0.1884 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 21.00 | 0.8075 | 0.1822 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 23.61 | 0.7208 | 0.2358 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 24.91 | 0.7703 | 0.2209 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 24.91 | 0.7703 | 0.2209 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 24.83 | 0.7616 | 0.2386 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 24.83 | 0.7616 | 0.2386 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 23.45 | 0.7741 | 0.1912 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 22.42 | 0.7656 | 0.2445 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 22.42 | 0.7656 | 0.2445 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 22.58 | 0.7626 | 0.2531 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 22.58 | 0.7626 | 0.2531 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 21.60 | 0.7436 | 0.2788 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 21.85 | 0.8140 | 0.1942 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 22.54 | 0.8144 | 0.1736 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 22.22 | 0.8174 | 0.1803 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 22.37 | 0.8168 | 0.1757 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 21.81 | 0.8149 | 0.1958 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 22.44 | 0.8096 | 0.1748 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 22.02 | 0.8177 | 0.1809 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 22.17 | 0.8145 | 0.1766 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 22.04 | 0.7505 | 0.2706 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.17 | 0.7410 | 0.3003 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 14.79 | 0.7324 | 0.2756 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 14.33 | 0.7394 | 0.2887 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 14.48 | 0.7365 | 0.2824 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 14.14 | 0.7310 | 0.3009 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 14.69 | 0.7198 | 0.2816 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 14.28 | 0.7273 | 0.2921 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 14.41 | 0.7241 | 0.2869 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.28 | 0.8243 | 0.1146 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.82 | 0.8293 | 0.1076 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.65 | 0.8276 | 0.1121 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.76 | 0.8288 | 0.1094 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.36 | 0.8233 | 0.1145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.43 | 0.8231 | 0.1096 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.42 | 0.8237 | 0.1128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.41 | 0.8233 | 0.1117 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.03 | 0.7889 | 0.1570 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.32 | 0.7990 | 0.1562 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.03 | 0.7950 | 0.1493 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.53 | 0.7986 | 0.1625 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.26 | 0.7949 | 0.1566 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.04 | 0.8014 | 0.1328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.20 | 0.8014 | 0.1447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.90 | 0.7959 | 0.1405 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.39 | 0.8027 | 0.1468 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.08 | 0.7975 | 0.1426 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.15 | 0.7971 | 0.1626 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.27 | 0.8239 | 0.1140 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.56 | 0.8251 | 0.1086 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.51 | 0.8249 | 0.1117 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.57 | 0.8252 | 0.1107 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.51 | 0.8257 | 0.1129 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.66 | 0.8261 | 0.1068 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.69 | 0.8270 | 0.1093 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.71 | 0.8269 | 0.1083 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.23 | 0.7975 | 0.1606 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.33 | 0.8119 | 0.1241 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.51 | 0.8130 | 0.1162 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.47 | 0.8132 | 0.1203 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.48 | 0.8132 | 0.1191 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.15 | 0.8080 | 0.1253 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.15 | 0.8066 | 0.1196 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.12 | 0.8067 | 0.1235 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.13 | 0.8065 | 0.1223 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.99 | 0.8293 | 0.1574 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.46 | 0.8310 | 0.1389 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.40 | 0.8328 | 0.1476 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.44 | 0.8326 | 0.1422 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.92 | 0.8234 | 0.1581 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.86 | 0.8157 | 0.1445 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.96 | 0.8231 | 0.1483 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.89 | 0.8197 | 0.1452 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.68 | 0.7279 | 0.2299 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.17 | 0.7685 | 0.2136 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.00 | 0.7752 | 0.1810 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.32 | 0.7616 | 0.2290 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.31 | 0.7781 | 0.1898 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.85 | 0.7784 | 0.1710 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.28 | 0.7803 | 0.2003 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.08 | 0.7763 | 0.1740 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.32 | 0.7752 | 0.2101 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.17 | 0.7772 | 0.1797 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.67 | 0.7616 | 0.2458 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.78 | 0.8245 | 0.1578 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.08 | 0.8231 | 0.1449 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.09 | 0.8261 | 0.1482 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.14 | 0.8252 | 0.1454 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.98 | 0.8258 | 0.1573 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.05 | 0.8194 | 0.1441 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.17 | 0.8270 | 0.1465 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.14 | 0.8240 | 0.1443 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.88 | 0.7625 | 0.2442 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.39 | 0.8004 | 0.1699 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.64 | 0.7958 | 0.1602 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.58 | 0.8004 | 0.1641 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.64 | 0.7986 | 0.1611 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.07 | 0.7926 | 0.1716 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.14 | 0.7837 | 0.1662 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.09 | 0.7884 | 0.1695 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.10 | 0.7858 | 0.1673 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 71.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.70 | 0.7774 | 0.1286 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 24.91 | 0.8251 | 0.1695 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 25.88 | 0.8264 | 0.1491 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 25.57 | 0.8294 | 0.1598 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 25.70 | 0.8285 | 0.1536 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 24.92 | 0.8195 | 0.1716 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 25.51 | 0.8097 | 0.1547 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 25.39 | 0.8187 | 0.1635 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 25.43 | 0.8141 | 0.1579 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 24.06 | 0.7414 | 0.1885 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 24.84 | 0.7628 | 0.2020 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 24.84 | 0.7628 | 0.2020 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 24.99 | 0.7514 | 0.2132 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 24.99 | 0.7514 | 0.2132 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 22.90 | 0.7880 | 0.1632 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 23.99 | 0.7762 | 0.2021 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 23.99 | 0.7762 | 0.2021 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 23.83 | 0.7703 | 0.2033 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 23.83 | 0.7703 | 0.2033 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 23.92 | 0.7825 | 0.2174 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 24.58 | 0.8171 | 0.1738 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 25.31 | 0.8127 | 0.1577 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 25.23 | 0.8181 | 0.1636 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 25.26 | 0.8158 | 0.1586 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 24.80 | 0.8167 | 0.1709 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 25.35 | 0.8080 | 0.1583 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 25.36 | 0.8177 | 0.1621 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 25.36 | 0.8134 | 0.1589 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 23.60 | 0.7812 | 0.2150 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 18.87 | 0.7741 | 0.2590 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 19.37 | 0.7641 | 0.2416 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 19.02 | 0.7718 | 0.2505 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 19.14 | 0.7680 | 0.2456 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 18.75 | 0.7666 | 0.2592 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 19.16 | 0.7499 | 0.2466 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 18.92 | 0.7597 | 0.2521 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 19.00 | 0.7547 | 0.2494 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.98 | 0.8218 | 0.1112 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.51 | 0.8265 | 0.1029 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.36 | 0.8258 | 0.1072 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.46 | 0.8265 | 0.1050 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.08 | 0.8208 | 0.1102 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.10 | 0.8190 | 0.1052 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.10 | 0.8208 | 0.1083 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.08 | 0.8197 | 0.1068 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.55 | 0.7909 | 0.1437 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.78 | 0.7954 | 0.1526 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.45 | 0.7909 | 0.1465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.01 | 0.7939 | 0.1550 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.70 | 0.7896 | 0.1485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.60 | 0.8037 | 0.1207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.60 | 0.7973 | 0.1416 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.28 | 0.7914 | 0.1367 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.80 | 0.7986 | 0.1394 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.46 | 0.7928 | 0.1353 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.24 | 0.8016 | 0.1459 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.94 | 0.8208 | 0.1110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.16 | 0.8208 | 0.1054 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.14 | 0.8219 | 0.1085 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.17 | 0.8214 | 0.1067 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.06 | 0.8220 | 0.1072 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.19 | 0.8215 | 0.1030 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.22 | 0.8234 | 0.1055 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.22 | 0.8227 | 0.1041 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.28 | 0.8009 | 0.1465 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.89 | 0.8059 | 0.1188 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.03 | 0.8069 | 0.1116 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.99 | 0.8073 | 0.1156 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.99 | 0.8071 | 0.1143 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.73 | 0.8019 | 0.1203 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.66 | 0.7994 | 0.1155 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.66 | 0.8002 | 0.1180 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.64 | 0.7996 | 0.1167 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 26.67 | 0.8286 | 0.1450 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.25 | 0.8298 | 0.1262 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.13 | 0.8326 | 0.1359 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.22 | 0.8321 | 0.1300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.63 | 0.8229 | 0.1459 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.59 | 0.8127 | 0.1321 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.68 | 0.8213 | 0.1397 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.63 | 0.8173 | 0.1347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.09 | 0.7478 | 0.1854 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.85 | 0.7629 | 0.1979 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.63 | 0.7729 | 0.1745 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.13 | 0.7538 | 0.2070 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.07 | 0.7750 | 0.1773 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.28 | 0.7977 | 0.1307 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.75 | 0.7797 | 0.1805 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.50 | 0.7765 | 0.1614 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.89 | 0.7748 | 0.1826 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.67 | 0.7775 | 0.1636 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.33 | 0.7911 | 0.1835 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.42 | 0.8240 | 0.1462 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.79 | 0.8194 | 0.1329 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.73 | 0.8242 | 0.1379 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.81 | 0.8223 | 0.1339 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.53 | 0.8246 | 0.1430 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.71 | 0.8158 | 0.1329 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.77 | 0.8247 | 0.1361 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.78 | 0.8209 | 0.1330 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.39 | 0.7917 | 0.1818 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.04 | 0.7971 | 0.1651 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.28 | 0.7927 | 0.1527 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.18 | 0.7967 | 0.1589 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.20 | 0.7946 | 0.1553 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.71 | 0.7898 | 0.1668 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.71 | 0.7776 | 0.1587 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.68 | 0.7840 | 0.1629 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.67 | 0.7803 | 0.1603 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 19.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 34.19 | 0.8809 | 0.0162 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 28.18 | 0.8732 | 0.0725 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 27.10 | 0.8638 | 0.0706 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 28.34 | 0.8732 | 0.0705 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 27.82 | 0.8684 | 0.0706 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 28.32 | 0.8658 | 0.0736 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 27.01 | 0.8502 | 0.0734 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 28.34 | 0.8658 | 0.0724 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 27.54 | 0.8593 | 0.0733 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 33.03 | 0.8642 | 0.0316 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 27.00 | 0.8272 | 0.0744 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 27.00 | 0.8272 | 0.0744 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 25.94 | 0.8013 | 0.0761 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 25.94 | 0.8013 | 0.0761 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 24.93 | 0.8249 | 0.0999 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 25.47 | 0.8193 | 0.0943 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 25.47 | 0.8193 | 0.0943 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 24.21 | 0.8047 | 0.0965 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 24.21 | 0.8047 | 0.0965 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 23.90 | 0.8111 | 0.1080 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 24.07 | 0.8304 | 0.0843 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 25.71 | 0.8158 | 0.0777 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 25.04 | 0.8297 | 0.0814 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 25.05 | 0.8232 | 0.0799 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 23.72 | 0.8239 | 0.0849 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 25.49 | 0.8136 | 0.0797 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 24.97 | 0.8281 | 0.0822 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 25.26 | 0.8245 | 0.0815 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 23.55 | 0.7991 | 0.1133 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 17.88 | 0.7871 | 0.1089 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 18.98 | 0.7748 | 0.1030 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 18.28 | 0.7913 | 0.1060 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 18.54 | 0.7850 | 0.1049 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 17.36 | 0.7865 | 0.1092 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 17.89 | 0.7657 | 0.1075 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 17.71 | 0.7866 | 0.1078 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 17.69 | 0.7761 | 0.1075 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 34.05 | 0.8825 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 33.98 | 0.8823 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 34.01 | 0.8827 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 34.01 | 0.8826 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 34.06 | 0.8825 | 0.0171 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 33.88 | 0.8822 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 33.95 | 0.8827 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 33.91 | 0.8825 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 34.10 | 0.8820 | 0.0166 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 33.94 | 0.8819 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 33.99 | 0.8802 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 33.94 | 0.8810 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 33.97 | 0.8800 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 34.05 | 0.8817 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 34.04 | 0.8817 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 34.06 | 0.8802 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 34.07 | 0.8817 | 0.0175 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 34.07 | 0.8804 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 33.94 | 0.8799 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 33.91 | 0.8822 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 33.79 | 0.8817 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 33.78 | 0.8821 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 33.84 | 0.8819 | 0.0168 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 33.96 | 0.8823 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 33.83 | 0.8820 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 33.86 | 0.8822 | 0.0170 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 33.91 | 0.8822 | 0.0169 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 33.92 | 0.8797 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 33.77 | 0.8802 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 33.73 | 0.8806 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 33.78 | 0.8810 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 33.73 | 0.8808 | 0.0174 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 33.59 | 0.8804 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 33.50 | 0.8799 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 33.49 | 0.8801 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 33.48 | 0.8800 | 0.0179 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 33.97 | 0.8935 | 0.0319 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 32.04 | 0.8831 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 33.32 | 0.8913 | 0.0324 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 32.79 | 0.8870 | 0.0321 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 34.19 | 0.8878 | 0.0276 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.85 | 0.8718 | 0.0328 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 33.20 | 0.8859 | 0.0309 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 32.33 | 0.8800 | 0.0310 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 33.87 | 0.8690 | 0.0195 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.95 | 0.8346 | 0.0674 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 28.67 | 0.8523 | 0.0585 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.98 | 0.8102 | 0.0674 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 29.48 | 0.8599 | 0.0576 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 33.38 | 0.8859 | 0.0198 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.96 | 0.8453 | 0.0674 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.90 | 0.8593 | 0.0628 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.82 | 0.8323 | 0.0657 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 29.71 | 0.8609 | 0.0604 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 31.98 | 0.8765 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 30.47 | 0.8685 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 30.96 | 0.8504 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 30.62 | 0.8644 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 30.59 | 0.8580 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 30.77 | 0.8672 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 30.51 | 0.8551 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 30.82 | 0.8677 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 30.74 | 0.8646 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 31.54 | 0.8775 | 0.0311 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.04 | 0.8534 | 0.0501 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.70 | 0.8365 | 0.0555 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.22 | 0.8541 | 0.0515 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.90 | 0.8462 | 0.0523 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 28.33 | 0.8526 | 0.0464 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.38 | 0.8308 | 0.0531 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.94 | 0.8509 | 0.0503 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.61 | 0.8386 | 0.0511 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.96 | 0.8145 | 0.1359 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 24.78 | 0.8457 | 0.2177 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 25.72 | 0.8449 | 0.1895 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 25.51 | 0.8491 | 0.2031 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 25.59 | 0.8476 | 0.1952 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 24.87 | 0.8420 | 0.2196 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 25.42 | 0.8311 | 0.1957 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 25.42 | 0.8408 | 0.2062 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 25.40 | 0.8361 | 0.1998 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 25.33 | 0.7913 | 0.2097 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 25.16 | 0.7985 | 0.2300 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 25.16 | 0.7985 | 0.2300 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 25.26 | 0.7893 | 0.2416 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 25.26 | 0.7893 | 0.2416 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 21.94 | 0.8010 | 0.1994 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 23.20 | 0.8005 | 0.2405 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 23.20 | 0.8005 | 0.2405 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 23.05 | 0.7955 | 0.2416 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 23.05 | 0.7955 | 0.2416 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 22.92 | 0.7930 | 0.2567 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 24.27 | 0.8383 | 0.2202 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 25.00 | 0.8329 | 0.1974 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 24.99 | 0.8391 | 0.2051 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 24.99 | 0.8364 | 0.1986 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 24.56 | 0.8387 | 0.2199 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 25.03 | 0.8286 | 0.1989 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 25.17 | 0.8392 | 0.2049 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 25.12 | 0.8346 | 0.2005 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 22.59 | 0.7876 | 0.2546 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 16.32 | 0.7722 | 0.3028 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 16.79 | 0.7634 | 0.2860 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 16.47 | 0.7700 | 0.2933 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 16.60 | 0.7668 | 0.2894 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 16.29 | 0.7672 | 0.3031 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 16.65 | 0.7513 | 0.2936 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 16.44 | 0.7611 | 0.2965 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 16.52 | 0.7564 | 0.2948 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.99 | 0.8464 | 0.1218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.43 | 0.8496 | 0.1128 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.34 | 0.8494 | 0.1177 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.41 | 0.8498 | 0.1154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.12 | 0.8461 | 0.1210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.03 | 0.8437 | 0.1151 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.08 | 0.8456 | 0.1188 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.03 | 0.8445 | 0.1172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.86 | 0.8262 | 0.1542 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.02 | 0.8294 | 0.1628 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.71 | 0.8266 | 0.1563 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.24 | 0.8279 | 0.1659 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.95 | 0.8251 | 0.1588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.88 | 0.8350 | 0.1299 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.82 | 0.8304 | 0.1513 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.54 | 0.8268 | 0.1458 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.00 | 0.8311 | 0.1494 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.71 | 0.8274 | 0.1447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 27.44 | 0.8336 | 0.1556 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.98 | 0.8460 | 0.1207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.14 | 0.8455 | 0.1150 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.16 | 0.8468 | 0.1182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.17 | 0.8462 | 0.1164 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.15 | 0.8474 | 0.1176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.15 | 0.8459 | 0.1123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.25 | 0.8482 | 0.1153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.23 | 0.8473 | 0.1137 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 27.49 | 0.8333 | 0.1558 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.89 | 0.8338 | 0.1281 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.04 | 0.8345 | 0.1210 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.01 | 0.8350 | 0.1250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.01 | 0.8347 | 0.1236 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.72 | 0.8308 | 0.1296 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.68 | 0.8287 | 0.1251 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.68 | 0.8296 | 0.1276 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.66 | 0.8289 | 0.1262 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.75 | 0.8556 | 0.1790 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.22 | 0.8552 | 0.1557 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.18 | 0.8587 | 0.1670 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.25 | 0.8578 | 0.1596 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.75 | 0.8520 | 0.1764 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.59 | 0.8420 | 0.1597 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.75 | 0.8505 | 0.1668 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.67 | 0.8467 | 0.1613 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.37 | 0.7952 | 0.2006 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.28 | 0.7984 | 0.2284 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.09 | 0.8048 | 0.1991 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.52 | 0.7910 | 0.2368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.47 | 0.8056 | 0.2017 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.57 | 0.8326 | 0.1450 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.35 | 0.8119 | 0.2146 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.13 | 0.8077 | 0.1898 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.41 | 0.8076 | 0.2145 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.21 | 0.8078 | 0.1897 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 26.53 | 0.8279 | 0.2023 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.53 | 0.8518 | 0.1772 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.77 | 0.8462 | 0.1600 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.82 | 0.8521 | 0.1656 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.85 | 0.8496 | 0.1610 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.66 | 0.8528 | 0.1747 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.64 | 0.8429 | 0.1592 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.84 | 0.8523 | 0.1633 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.80 | 0.8484 | 0.1596 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 26.57 | 0.8284 | 0.2019 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.49 | 0.8235 | 0.1904 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.66 | 0.8181 | 0.1859 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.64 | 0.8230 | 0.1853 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.66 | 0.8210 | 0.1830 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.27 | 0.8183 | 0.1907 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.24 | 0.8076 | 0.1875 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.24 | 0.8135 | 0.1885 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.24 | 0.8103 | 0.1868 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1020 | None | classic | 1.56 | False | 184291 | 0.175 | 35.1 | 33.30 | 0.14 | 0.004 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1020 | None | classic | 1.56 | False | 184291 | 0.175 | 32.5 | 33.30 | 0.14 | 0.004 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1020 | None | classic | 1.56 | False | 184291 | 0.175 | 35.3 | 33.30 | 0.14 | 0.004 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1020 | None | classic | 1.56 | False | 184291 | 0.175 | 41.2 | 33.30 | 0.14 | 0.004 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 988 | None | classic | 1.46 | False | 179792 | 0.171 | 36.5 | 32.72 | 0.31 | 0.003 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 988 | None | classic | 1.46 | False | 179792 | 0.171 | 44.1 | 32.72 | 0.31 | 0.003 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 988 | None | classic | 1.46 | False | 179792 | 0.171 | 42.4 | 32.72 | 0.31 | 0.003 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 988 | None | classic | 1.46 | False | 179792 | 0.171 | 35.9 | 32.72 | 0.31 | 0.003 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2132814 | 0.158 | 37.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2132814 | 0.808 | 62.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2132814 | 0.808 | 62.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2132814 | 0.804 | 37.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2132814 | 0.804 | 37.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2132814 | 0.158 | 44.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2132814 | 0.808 | 86.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2132814 | 0.808 | 86.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2132814 | 0.804 | 44.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2132814 | 0.804 | 44.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2052778 | 0.808 | 175.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1021 | None | classic | 1.56 | False | 184497 | 0.177 | 33.9 | 33.23 | 0.15 | 0.004 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1021 | None | classic | 1.56 | False | 184497 | 0.177 | 33.1 | 33.23 | 0.15 | 0.004 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1021 | None | classic | 1.56 | False | 184497 | 0.177 | 30.2 | 33.23 | 0.15 | 0.004 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1021 | None | classic | 1.56 | False | 184497 | 0.177 | 33.5 | 33.23 | 0.15 | 0.004 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 989 | None | classic | 1.46 | False | 176197 | 0.172 | 33.5 | 32.34 | 0.36 | 0.002 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 989 | None | classic | 1.46 | False | 176197 | 0.172 | 35.1 | 32.34 | 0.36 | 0.002 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 989 | None | classic | 1.46 | False | 176197 | 0.172 | 32.6 | 32.34 | 0.36 | 0.002 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 989 | None | classic | 1.46 | False | 176197 | 0.172 | 31.9 | 32.34 | 0.36 | 0.002 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2122483 | 0.808 | 85.7 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1003 | None | classic | 1.50 | False | 188051 | 0.324 | 40.0 | 33.79 | 0.19 | 0.005 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1003 | None | classic | 1.50 | False | 188051 | 0.324 | 35.7 | 33.79 | 0.19 | 0.005 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1003 | None | classic | 1.50 | False | 188051 | 0.324 | 34.9 | 33.79 | 0.19 | 0.005 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1003 | None | classic | 1.50 | False | 188051 | 0.324 | 30.6 | 33.79 | 0.19 | 0.005 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 971 | None | classic | 1.41 | False | 175817 | 0.170 | 37.6 | 32.54 | 0.17 | 0.003 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 971 | None | classic | 1.41 | False | 175817 | 0.170 | 34.9 | 32.54 | 0.17 | 0.003 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 971 | None | classic | 1.41 | False | 175817 | 0.170 | 37.8 | 32.54 | 0.17 | 0.003 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 971 | None | classic | 1.41 | False | 175817 | 0.170 | 34.1 | 32.54 | 0.17 | 0.003 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.716 | 0.089 |
| in035 | mask_ent | 0.647 | 0.089 |
| in035 | mask_grad | 0.363 | 0.089 |
| in035 | r_col | 0.733 | 0.089 |
| in035 | r_warp | 0.848 | 0.089 |

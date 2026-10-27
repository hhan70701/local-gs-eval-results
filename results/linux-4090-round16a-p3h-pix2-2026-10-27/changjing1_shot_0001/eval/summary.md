# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | 93.5% | 24.54 / 0.1687 | 28.66 / 0.1897 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | 93.6% | 24.57 / 0.1672 | 28.18 / 0.1763 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | 93.7% | 24.55 / 0.1681 | 28.67 / 0.1785 | — | — |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | 93.5% | 24.57 / 0.1677 | 28.48 / 0.1763 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | 93.9% | 24.55 / 0.1723 | 28.21 / 0.1956 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 93.9% | 24.57 / 0.1703 | 28.77 / 0.1686 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 94.0% | 24.57 / 0.1710 | 28.71 / 0.1765 | — | — |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 93.8% | 24.58 / 0.1712 | 28.77 / 0.1723 | — | — |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 98.9% | 24.80 / 0.1730 | 23.61 / 0.3023 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 95.0% | 24.52 / 0.1756 | 25.07 / 0.2334 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 20.0% | 19.26 / 0.0946 | 19.23 / 0.1440 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 96.3% | 24.59 / 0.1759 | 24.13 / 0.2605 | — | — |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 21.8% | 19.64 / 0.0985 | 18.46 / 0.1722 | — | — |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 98.8% | 24.77 / 0.1716 | 23.92 / 0.2434 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 93.5% | 24.52 / 0.1720 | 26.08 / 0.2041 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.4% | 19.28 / 0.1045 | 20.33 / 0.1260 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 94.1% | 24.55 / 0.1718 | 25.28 / 0.2265 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 21.7% | 19.56 / 0.1056 | 19.59 / 0.1518 | — | — |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | 97.0% | 24.52 / 0.1704 | 24.32 / 0.2591 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | 95.8% | 24.72 / 0.1754 | 28.82 / 0.1944 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | 96.0% | 24.75 / 0.1748 | 28.27 / 0.1785 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | 96.0% | 24.74 / 0.1742 | 28.73 / 0.1803 | — | — |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | 96.0% | 24.75 / 0.1747 | 28.54 / 0.1771 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | 95.5% | 24.72 / 0.1762 | 29.00 / 0.1925 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 95.8% | 24.72 / 0.1752 | 29.07 / 0.1712 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 95.7% | 24.72 / 0.1753 | 29.23 / 0.1767 | — | — |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 95.7% | 24.73 / 0.1755 | 29.17 / 0.1727 | — | — |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | 99.5% | 24.70 / 0.1821 | 24.58 / 0.2784 | — | — |
| in035 | gs_tokrife448_nat_dil_al_local | 58.7% | 23.42 / 0.1568 | 23.99 / 0.2102 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 65.7% | 23.65 / 0.1583 | 24.47 / 0.2210 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 62.0% | 23.58 / 0.1584 | 24.36 / 0.2101 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 63.4% | 23.61 / 0.1593 | 24.54 / 0.2107 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_local | 58.7% | 23.40 / 0.1590 | 24.08 / 0.2106 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | 65.3% | 23.64 / 0.1609 | 24.48 / 0.2232 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | 61.7% | 23.55 / 0.1621 | 24.27 / 0.2115 | — | — |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | 63.0% | 23.56 / 0.1633 | 24.42 / 0.2144 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 23.95 / 0.1893 | 23.90 / 0.2303 | 17.22 / 0.1504 | 35.38 / 0.0209 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.09 / 0.2127 | 28.51 / 0.2166 | 22.45 / 0.0785 | 36.53 / 0.0465 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.57 / 0.1929 | 28.17 / 0.2130 | 21.96 / 0.0779 | 36.47 / 0.0422 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.15 / 0.1974 | 28.45 / 0.2154 | 22.48 / 0.0767 | 37.10 / 0.0448 |
| in035 | hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.89 / 0.1934 | 28.36 / 0.2130 | 22.26 / 0.0770 | 36.79 / 0.0433 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.77 / 0.2112 | 28.46 / 0.2203 | 21.90 / 0.0797 | 36.43 / 0.0468 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.23 / 0.1834 | 28.50 / 0.2097 | 22.51 / 0.0748 | 36.87 / 0.0408 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.30 / 0.1918 | 28.64 / 0.2130 | 22.51 / 0.0755 | 37.20 / 0.0441 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.32 / 0.1862 | 28.62 / 0.2108 | 22.59 / 0.0752 | 36.99 / 0.0422 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.75 / 0.2572 | 24.89 / 0.3018 | 19.16 / 0.1573 | 34.85 / 0.0251 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.71 / 0.2091 | 27.28 / 0.2273 | 21.49 / 0.1129 | 35.91 / 0.0257 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.81 / 0.2052 | 25.88 / 0.2321 | 20.67 / 0.1325 | 34.16 / 0.0224 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.49 / 0.2259 | 27.74 / 0.2448 | 21.55 / 0.1233 | 36.35 / 0.0296 |
| in035 | hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.66 / 0.2128 | 26.20 / 0.2404 | 20.77 / 0.1357 | 34.74 / 0.0231 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.95 / 0.2025 | 25.24 / 0.2485 | 19.19 / 0.1249 | 34.94 / 0.0288 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.15 / 0.1896 | 27.77 / 0.2193 | 21.66 / 0.1019 | 36.26 / 0.0274 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.16 / 0.1856 | 26.33 / 0.2260 | 20.89 / 0.1216 | 35.20 / 0.0211 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.64 / 0.1933 | 28.14 / 0.2214 | 21.40 / 0.1018 | 36.69 / 0.0280 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.76 / 0.1867 | 26.50 / 0.2253 | 20.66 / 0.1196 | 35.10 / 0.0212 |
| in035 | hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.69 / 0.2232 | 25.24 / 0.2797 | 20.66 / 0.1303 | 36.49 / 0.0290 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.00 / 0.2072 | 28.55 / 0.2044 | 22.23 / 0.0780 | 36.69 / 0.0461 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.56 / 0.1875 | 28.41 / 0.1961 | 21.92 / 0.0790 | 36.41 / 0.0424 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.99 / 0.1925 | 28.58 / 0.2005 | 22.24 / 0.0781 | 37.14 / 0.0446 |
| in035 | hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.81 / 0.1885 | 28.58 / 0.1980 | 22.13 / 0.0777 | 36.80 / 0.0431 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.05 / 0.2053 | 28.66 / 0.2060 | 22.39 / 0.0760 | 36.72 / 0.0455 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.23 / 0.1796 | 28.67 / 0.1953 | 22.41 / 0.0707 | 37.24 / 0.0403 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.32 / 0.1876 | 28.82 / 0.2005 | 22.60 / 0.0726 | 37.58 / 0.0431 |
| in035 | hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.29 / 0.1827 | 28.82 / 0.1972 | 22.55 / 0.0707 | 37.50 / 0.0413 |
| in035 | hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.72 / 0.2250 | 25.08 / 0.2822 | 20.71 / 0.1274 | 36.65 / 0.0294 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 24.95 / 0.2416 | 27.16 / 0.2255 | 20.06 / 0.1061 | 29.10 / 0.0637 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.94 / 0.2440 | 27.43 / 0.2226 | 20.52 / 0.1003 | 28.18 / 0.0767 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.07 / 0.2403 | 27.52 / 0.2235 | 20.34 / 0.1033 | 28.72 / 0.0686 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.12 / 0.2411 | 27.58 / 0.2218 | 20.47 / 0.1024 | 28.58 / 0.0711 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.97 / 0.2420 | 27.28 / 0.2266 | 20.24 / 0.1049 | 29.02 / 0.0641 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.86 / 0.2447 | 27.62 / 0.2200 | 20.54 / 0.1004 | 28.00 / 0.0769 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.95 / 0.2409 | 27.62 / 0.2222 | 20.44 / 0.1037 | 28.55 / 0.0698 |
| in035 | hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.96 / 0.2410 | 27.69 / 0.2186 | 20.55 / 0.1011 | 28.37 / 0.0729 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 18.1%） | — | — | 23.95 / 0.1893 | 23.90 / 0.2303 | 35.38 |
| in035 | rife | 39.3% | 58.7% | 24.95 / 0.2416 | 27.16 / 0.2255 | 29.10 |
| in035 | cnw_cnn | 78.2% | 93.5% | 28.09 / 0.2127 | 28.51 / 0.2166 | 36.53 |
| in035 | cnw_f5 | 81.3% | 95.8% | 28.00 / 0.2072 | 28.55 / 0.2044 | 36.69 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 23.55 / 0.2410 | +2.48 / +0.0009 (core 38.2%) | +6.92 / -0.0150 (core 82.0%) | +6.63 / -0.0277 (core 87.6%) |
| in035 | 2 | 0-3 | 24.98 / 0.1832 | +1.17 / +0.0900 (core 38.2%) | +4.17 / +0.0470 (core 82.0%) | +4.21 / +0.0425 (core 87.6%) |
| in035 | 4 | 3-5 | 23.33 / 0.1436 | -0.67 / +0.0662 (core 28.2%) | +1.34 / +0.0382 (core 60.2%) | +1.33 / +0.0389 (core 59.8%) |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 23.95 / 0.1893 | 23.90 | 35.38 | — |
| in035 | cnw_cnn | 不复核 | —% | 28.09 / 0.2127 | 28.51 | 36.53 | 1/3 |
| in035 | cnw_cnn | oracle | 15.6% | 27.82 / 0.1588 | 28.26 | 35.17 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.57 / 0.1929 | 28.17 | 36.47 | 1/3 |
| in035 | cnw_cnn | oracle | 15.6% | 27.48 / 0.1545 | 27.96 | 34.94 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 28.15 / 0.1974 | 28.45 | 37.10 | 1/3 |
| in035 | cnw_cnn | oracle | 15.6% | 27.81 / 0.1550 | 28.07 | 35.07 | 3/3 |
| in035 | cnw_cnn | 不复核 | —% | 27.89 / 0.1934 | 28.36 | 36.79 | 1/3 |
| in035 | cnw_cnn | oracle | 15.6% | 27.66 / 0.1544 | 28.02 | 35.00 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.77 / 0.2112 | 28.46 | 36.43 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 15.6% | 27.49 / 0.1589 | 28.13 | 35.18 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.23 / 0.1834 | 28.50 | 36.87 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 15.6% | 27.78 / 0.1503 | 28.08 | 35.03 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.30 / 0.1918 | 28.64 | 37.20 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 15.6% | 27.81 / 0.1531 | 28.17 | 35.12 | 3/3 |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.32 / 0.1862 | 28.62 | 36.99 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 15.6% | 27.83 / 0.1516 | 28.13 | 35.06 | 3/3 |
| in035 | cnw_cnn_p3h_flw | 不复核 | —% | 24.75 / 0.2572 | 24.89 | 34.85 | 0/3 |
| in035 | cnw_cnn_p3h_flw | oracle | 14.4% | 25.26 / 0.2180 | 25.66 | 35.37 | 0/3 |
| in035 | cnw_cnn_p3h_fsl | 不复核 | —% | 26.71 / 0.2091 | 27.28 | 35.91 | 1/3 |
| in035 | cnw_cnn_p3h_fsl | oracle | 15.3% | 26.97 / 0.1842 | 27.30 | 35.28 | 2/3 |
| in035 | cnw_cnn_p3h_fsl_g | 不复核 | —% | 25.81 / 0.2052 | 25.88 | 34.16 | 1/3 |
| in035 | cnw_cnn_p3h_fsl_g | oracle | 10.1% | 26.29 / 0.1848 | 26.22 | 35.29 | 2/3 |
| in035 | cnw_cnn_p3h_fss | 不复核 | —% | 26.49 / 0.2259 | 27.74 | 36.35 | 0/3 |
| in035 | cnw_cnn_p3h_fss | oracle | 15.2% | 26.92 / 0.1935 | 27.97 | 35.38 | 1/3 |
| in035 | cnw_cnn_p3h_fss_g | 不复核 | —% | 25.66 / 0.2128 | 26.20 | 34.74 | 0/3 |
| in035 | cnw_cnn_p3h_fss_g | oracle | 10.1% | 26.26 / 0.1880 | 26.75 | 35.39 | 1/3 |
| in035 | cnw_cnn_pix2_flw | 不复核 | —% | 24.95 / 0.2025 | 25.24 | 34.94 | 1/3 |
| in035 | cnw_cnn_pix2_flw | oracle | 14.4% | 25.27 / 0.1804 | 25.83 | 35.38 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.15 / 0.1896 | 27.77 | 36.26 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 15.3% | 27.13 / 0.1690 | 27.49 | 35.24 | 2/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.16 / 0.1856 | 26.33 | 35.20 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 10.3% | 26.48 / 0.1730 | 26.46 | 35.25 | 2/3 |
| in035 | cnw_cnn_pix2_fss | 不复核 | —% | 26.64 / 0.1933 | 28.14 | 36.69 | 1/3 |
| in035 | cnw_cnn_pix2_fss | oracle | 15.2% | 26.84 / 0.1689 | 27.99 | 35.39 | 2/3 |
| in035 | cnw_cnn_pix2_fss_g | 不复核 | —% | 25.76 / 0.1867 | 26.50 | 35.10 | 1/3 |
| in035 | cnw_cnn_pix2_fss_g | oracle | 10.2% | 26.21 / 0.1687 | 26.83 | 35.39 | 2/3 |
| in035 | cnw_cnn_pix | 不复核 | —% | 25.69 / 0.2232 | 25.24 | 36.49 | 0/3 |
| in035 | cnw_cnn_pix | oracle | 15.8% | 26.40 / 0.1901 | 26.49 | 35.34 | 1/3 |
| in035 | cnw_f5 | 不复核 | —% | 28.00 / 0.2072 | 28.55 | 36.69 | 1/3 |
| in035 | cnw_f5 | oracle | 15.6% | 27.72 / 0.1571 | 28.19 | 35.13 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.56 / 0.1875 | 28.41 | 36.41 | 1/3 |
| in035 | cnw_f5 | oracle | 15.6% | 27.43 / 0.1530 | 28.03 | 34.91 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.99 / 0.1925 | 28.58 | 37.14 | 1/3 |
| in035 | cnw_f5 | oracle | 15.6% | 27.67 / 0.1534 | 28.07 | 35.07 | 3/3 |
| in035 | cnw_f5 | 不复核 | —% | 27.81 / 0.1885 | 28.58 | 36.80 | 1/3 |
| in035 | cnw_f5 | oracle | 15.6% | 27.58 / 0.1527 | 28.08 | 35.02 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.05 / 0.2053 | 28.66 | 36.72 | 1/3 |
| in035 | cnw_f5_mw | oracle | 15.5% | 27.82 / 0.1545 | 28.36 | 35.18 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.23 / 0.1796 | 28.67 | 37.24 | 1/3 |
| in035 | cnw_f5_mw | oracle | 15.6% | 27.81 / 0.1483 | 28.23 | 35.05 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.32 / 0.1876 | 28.82 | 37.58 | 1/3 |
| in035 | cnw_f5_mw | oracle | 15.5% | 27.92 / 0.1503 | 28.28 | 35.16 | 3/3 |
| in035 | cnw_f5_mw | 不复核 | —% | 28.29 / 0.1827 | 28.82 | 37.50 | 1/3 |
| in035 | cnw_f5_mw | oracle | 15.6% | 27.87 / 0.1485 | 28.28 | 35.13 | 3/3 |
| in035 | cnw_f5_pix | 不复核 | —% | 25.72 / 0.2250 | 25.08 | 36.65 | 0/3 |
| in035 | cnw_f5_pix | oracle | 15.8% | 26.42 / 0.1890 | 26.43 | 35.34 | 1/3 |
| in035 | rife | 不复核 | —% | 24.95 / 0.2416 | 27.16 | 29.10 | 0/3 |
| in035 | rife | oracle | 13.5% | 26.20 / 0.1806 | 27.43 | 34.89 | 1/3 |
| in035 | rife | 不复核 | —% | 24.94 / 0.2440 | 27.43 | 28.18 | 1/3 |
| in035 | rife | oracle | 14.2% | 26.51 / 0.1755 | 27.59 | 34.54 | 1/3 |
| in035 | rife | 不复核 | —% | 25.07 / 0.2403 | 27.52 | 28.72 | 1/3 |
| in035 | rife | oracle | 13.8% | 26.40 / 0.1779 | 27.56 | 34.78 | 1/3 |
| in035 | rife | 不复核 | —% | 25.12 / 0.2411 | 27.58 | 28.58 | 1/3 |
| in035 | rife | oracle | 13.9% | 26.48 / 0.1767 | 27.61 | 34.72 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 24.97 / 0.2420 | 27.28 | 29.02 | 0/3 |
| in035 | rife_mw | oracle | 13.5% | 26.30 / 0.1807 | 27.52 | 34.71 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 24.86 / 0.2447 | 27.62 | 28.00 | 1/3 |
| in035 | rife_mw | oracle | 14.2% | 26.53 / 0.1750 | 27.60 | 34.50 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 24.95 / 0.2409 | 27.62 | 28.55 | 1/3 |
| in035 | rife_mw | oracle | 13.8% | 26.44 / 0.1768 | 27.54 | 34.65 | 1/3 |
| in035 | rife_mw | 不复核 | —% | 24.96 / 0.2410 | 27.69 | 28.37 | 1/3 |
| in035 | rife_mw | oracle | 13.9% | 26.53 / 0.1744 | 27.61 | 34.61 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 cnw_cnn，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 23.95 / 0.1893 | 23.90 / 0.2303 | — |
| in035 | FF | 0（前馈） | 907×813（71%） | 32.32 | 28.09 / 0.2127 | 28.51 / 0.2166 | 1/3 |
| in035 | 25 | 0.62 s | 907×813（71%） | 34.69 | 28.15 / 0.1974 | 28.45 / 0.2154 | 1/3 |
| in035 | 50 | 1.23 s | 907×813（71%） | 35.51 | 27.89 / 0.1934 | 28.36 / 0.2130 | 1/3 |
| in035 | 100 | 2.44 s | 907×813（71%） | 36.36 | 27.57 / 0.1929 | 28.17 / 0.2130 | 1/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 23.95 / 0.1893 | 23.90 / 0.2303 | 35.38 | — |
| in035 | cnw_cnn | GS 前馈颜色 | 直接 | 28.09 / 0.2127 | 28.51 / 0.2166 | 36.53 | 1/3 |
| in035 | cnw_cnn | GS 前馈颜色 | oracle | 27.82 / 0.1588 | 28.26 / 0.1899 | 35.17 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | 直接 | 28.15 / 0.1974 | 28.45 / 0.2154 | 37.10 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 25 步 | oracle | 27.81 / 0.1550 | 28.07 / 0.1886 | 35.07 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | 直接 | 27.89 / 0.1934 | 28.36 / 0.2130 | 36.79 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 50 步 | oracle | 27.66 / 0.1544 | 28.02 / 0.1880 | 35.00 | 3/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | 直接 | 27.57 / 0.1929 | 28.17 / 0.2130 | 36.47 | 1/3 |
| in035 | cnw_cnn | GS 测试时优化 100 步 | oracle | 27.48 / 0.1545 | 27.96 / 0.1884 | 34.94 | 3/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | 直接 | 27.77 / 0.2112 | 28.46 / 0.2203 | 36.43 | 1/3 |
| in035 | cnw_cnn_mw | GS 前馈颜色 | oracle | 27.49 / 0.1589 | 28.13 / 0.1910 | 35.18 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | 直接 | 28.30 / 0.1918 | 28.64 / 0.2130 | 37.20 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 25 步 | oracle | 27.81 / 0.1531 | 28.17 / 0.1865 | 35.12 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | 直接 | 28.32 / 0.1862 | 28.62 / 0.2108 | 36.99 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 50 步 | oracle | 27.83 / 0.1516 | 28.13 / 0.1856 | 35.06 | 3/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.23 / 0.1834 | 28.50 / 0.2097 | 36.87 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.78 / 0.1503 | 28.08 / 0.1862 | 35.03 | 3/3 |
| in035 | cnw_f5 | GS 前馈颜色 | 直接 | 28.00 / 0.2072 | 28.55 / 0.2044 | 36.69 | 1/3 |
| in035 | cnw_f5 | GS 前馈颜色 | oracle | 27.72 / 0.1571 | 28.19 / 0.1846 | 35.13 | 3/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | 直接 | 27.99 / 0.1925 | 28.58 / 0.2005 | 37.14 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 25 步 | oracle | 27.67 / 0.1534 | 28.07 / 0.1830 | 35.07 | 3/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | 直接 | 27.81 / 0.1885 | 28.58 / 0.1980 | 36.80 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 50 步 | oracle | 27.58 / 0.1527 | 28.08 / 0.1816 | 35.02 | 3/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | 直接 | 27.56 / 0.1875 | 28.41 / 0.1961 | 36.41 | 1/3 |
| in035 | cnw_f5 | GS 测试时优化 100 步 | oracle | 27.43 / 0.1530 | 28.03 / 0.1814 | 34.91 | 3/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | 直接 | 28.05 / 0.2053 | 28.66 / 0.2060 | 36.72 | 1/3 |
| in035 | cnw_f5_mw | GS 前馈颜色 | oracle | 27.82 / 0.1545 | 28.36 / 0.1854 | 35.18 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | 直接 | 28.32 / 0.1876 | 28.82 / 0.2005 | 37.58 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 25 步 | oracle | 27.92 / 0.1503 | 28.28 / 0.1817 | 35.16 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | 直接 | 28.29 / 0.1827 | 28.82 / 0.1972 | 37.50 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 50 步 | oracle | 27.87 / 0.1485 | 28.28 / 0.1802 | 35.13 | 3/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | 直接 | 28.23 / 0.1796 | 28.67 / 0.1953 | 37.24 | 1/3 |
| in035 | cnw_f5_mw | GS 测试时优化 100 步 | oracle | 27.81 / 0.1483 | 28.23 / 0.1797 | 35.05 | 3/3 |
| in035 | rife | GS 前馈颜色 | 直接 | 24.95 / 0.2416 | 27.16 / 0.2255 | 29.10 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 26.20 / 0.1806 | 27.43 / 0.1935 | 34.89 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 25.07 / 0.2403 | 27.52 / 0.2235 | 28.72 | 1/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 26.40 / 0.1779 | 27.56 / 0.1926 | 34.78 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 25.12 / 0.2411 | 27.58 / 0.2218 | 28.58 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 26.48 / 0.1767 | 27.61 / 0.1910 | 34.72 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 24.94 / 0.2440 | 27.43 / 0.2226 | 28.18 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 26.51 / 0.1755 | 27.59 / 0.1907 | 34.54 | 1/3 |
| in035 | rife_mw | GS 前馈颜色 | 直接 | 24.97 / 0.2420 | 27.28 / 0.2266 | 29.02 | 0/3 |
| in035 | rife_mw | GS 前馈颜色 | oracle | 26.30 / 0.1807 | 27.52 / 0.1930 | 34.71 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | 直接 | 24.95 / 0.2409 | 27.62 / 0.2222 | 28.55 | 1/3 |
| in035 | rife_mw | GS 测试时优化 25 步 | oracle | 26.44 / 0.1768 | 27.54 / 0.1922 | 34.65 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | 直接 | 24.96 / 0.2410 | 27.69 / 0.2186 | 28.37 | 1/3 |
| in035 | rife_mw | GS 测试时优化 50 步 | oracle | 26.53 / 0.1744 | 27.61 / 0.1899 | 34.61 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | 直接 | 24.86 / 0.2447 | 27.62 / 0.2200 | 28.00 | 1/3 |
| in035 | rife_mw | GS 测试时优化 100 步 | oracle | 26.53 / 0.1750 | 27.60 / 0.1897 | 34.50 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.90 / 0.2303 | 17.22 / 0.1504 | 35.38 / 0.0209 | 23.95 / 0.1893 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 47.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.90 | 0.8006 | 0.2303 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 22.99 | 0.8441 | 0.2556 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 23.25 | 0.8334 | 0.2432 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 22.79 | 0.8393 | 0.2509 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 22.89 | 0.8368 | 0.2473 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 23.62 | 0.8462 | 0.2516 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 23.75 | 0.8352 | 0.2363 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 23.30 | 0.8418 | 0.2436 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 23.40 | 0.8390 | 0.2401 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 24.71 | 0.7294 | 0.3032 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 27.83 | 0.8078 | 0.2193 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 27.83 | 0.8078 | 0.2193 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 28.24 | 0.7990 | 0.2355 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 28.24 | 0.7990 | 0.2355 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 22.13 | 0.7581 | 0.2686 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 25.36 | 0.8127 | 0.2671 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 25.36 | 0.8127 | 0.2671 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 26.66 | 0.8100 | 0.2545 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 26.66 | 0.8100 | 0.2545 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 24.72 | 0.7983 | 0.2842 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 25.69 | 0.8624 | 0.2112 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 26.13 | 0.8493 | 0.1994 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 25.36 | 0.8579 | 0.2055 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 25.47 | 0.8543 | 0.2020 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 26.12 | 0.8639 | 0.2122 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 26.26 | 0.8546 | 0.1990 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 25.95 | 0.8615 | 0.2058 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 26.01 | 0.8592 | 0.2017 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 25.01 | 0.8002 | 0.2790 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 23.34 | 0.8378 | 0.2481 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 23.64 | 0.8300 | 0.2320 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 23.20 | 0.8351 | 0.2402 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 23.32 | 0.8329 | 0.2369 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 23.38 | 0.8370 | 0.2454 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 23.72 | 0.8288 | 0.2305 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 23.38 | 0.8346 | 0.2376 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 23.49 | 0.8318 | 0.2334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 28.26 | 0.8483 | 0.1899 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.96 | 0.8421 | 0.1884 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.07 | 0.8444 | 0.1886 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.02 | 0.8435 | 0.1880 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.13 | 0.8469 | 0.1910 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.08 | 0.8437 | 0.1862 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.17 | 0.8464 | 0.1865 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.13 | 0.8454 | 0.1856 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.66 | 0.7925 | 0.2550 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.30 | 0.8258 | 0.2083 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.22 | 0.8182 | 0.2159 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.97 | 0.8231 | 0.2225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.75 | 0.8190 | 0.2201 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.83 | 0.8129 | 0.2219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.49 | 0.8320 | 0.1999 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.46 | 0.8231 | 0.2100 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 27.99 | 0.8319 | 0.1982 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.83 | 0.8260 | 0.2031 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.49 | 0.8195 | 0.2333 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 28.19 | 0.8500 | 0.1846 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.03 | 0.8438 | 0.1814 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.07 | 0.8467 | 0.1830 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.08 | 0.8457 | 0.1816 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.36 | 0.8512 | 0.1854 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.23 | 0.8474 | 0.1797 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.28 | 0.8496 | 0.1817 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.28 | 0.8489 | 0.1802 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.43 | 0.8192 | 0.2323 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.43 | 0.8386 | 0.1935 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.59 | 0.8364 | 0.1907 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 27.56 | 0.8369 | 0.1926 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.61 | 0.8370 | 0.1910 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 27.52 | 0.8391 | 0.1930 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.60 | 0.8363 | 0.1897 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.54 | 0.8368 | 0.1922 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.61 | 0.8373 | 0.1899 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.51 | 0.8579 | 0.2166 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 28.17 | 0.8440 | 0.2130 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.45 | 0.8520 | 0.2154 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 28.36 | 0.8491 | 0.2130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 28.46 | 0.8581 | 0.2203 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.50 | 0.8458 | 0.2097 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.64 | 0.8540 | 0.2130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.62 | 0.8513 | 0.2108 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.89 | 0.7357 | 0.3018 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 27.28 | 0.8064 | 0.2273 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.88 | 0.8102 | 0.2321 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 27.74 | 0.7972 | 0.2448 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.20 | 0.8087 | 0.2404 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.24 | 0.7896 | 0.2485 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.77 | 0.8257 | 0.2193 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.33 | 0.8157 | 0.2260 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 28.14 | 0.8173 | 0.2214 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.50 | 0.8165 | 0.2253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.24 | 0.8017 | 0.2797 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.55 | 0.8622 | 0.2044 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 28.41 | 0.8489 | 0.1961 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 28.58 | 0.8573 | 0.2005 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 28.58 | 0.8539 | 0.1980 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.66 | 0.8637 | 0.2060 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.67 | 0.8542 | 0.1953 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.82 | 0.8610 | 0.2005 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.82 | 0.8588 | 0.1972 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.08 | 0.7999 | 0.2822 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.16 | 0.8409 | 0.2255 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.43 | 0.8329 | 0.2226 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 27.52 | 0.8381 | 0.2235 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.58 | 0.8366 | 0.2218 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 27.28 | 0.8399 | 0.2266 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 27.62 | 0.8328 | 0.2200 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 27.62 | 0.8381 | 0.2222 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 27.69 | 0.8366 | 0.2186 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 18.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.22 | 0.5539 | 0.1504 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 23.78 | 0.7583 | 0.0727 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 23.10 | 0.7452 | 0.0710 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 23.45 | 0.7579 | 0.0705 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 23.26 | 0.7521 | 0.0704 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 22.85 | 0.7470 | 0.0739 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 23.16 | 0.7446 | 0.0680 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 23.07 | 0.7523 | 0.0697 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 23.14 | 0.7476 | 0.0689 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 19.21 | 0.5775 | 0.1580 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 21.77 | 0.6719 | 0.1073 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 21.77 | 0.6719 | 0.1073 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 21.83 | 0.6517 | 0.1178 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 21.83 | 0.6517 | 0.1178 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 17.71 | 0.6048 | 0.1339 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 21.59 | 0.6857 | 0.1046 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 21.59 | 0.6857 | 0.1046 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 21.39 | 0.6728 | 0.1038 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 21.39 | 0.6728 | 0.1038 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 20.55 | 0.6666 | 0.1272 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 23.08 | 0.7653 | 0.0724 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 22.44 | 0.7423 | 0.0713 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 22.78 | 0.7618 | 0.0708 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 22.59 | 0.7531 | 0.0704 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 23.29 | 0.7695 | 0.0697 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 23.15 | 0.7612 | 0.0641 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 23.21 | 0.7726 | 0.0663 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 23.15 | 0.7667 | 0.0645 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 20.45 | 0.6683 | 0.1260 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 19.48 | 0.6762 | 0.1115 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 20.13 | 0.6804 | 0.1042 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 19.78 | 0.6871 | 0.1091 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 19.94 | 0.6841 | 0.1074 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 19.49 | 0.6802 | 0.1099 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 20.03 | 0.6783 | 0.1054 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 19.82 | 0.6905 | 0.1079 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 19.91 | 0.6862 | 0.1078 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 22.45 | 0.7398 | 0.0786 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.96 | 0.7200 | 0.0780 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.48 | 0.7353 | 0.0768 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.26 | 0.7282 | 0.0771 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.90 | 0.7289 | 0.0801 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.51 | 0.7245 | 0.0753 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.51 | 0.7325 | 0.0759 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.59 | 0.7283 | 0.0757 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.16 | 0.5905 | 0.1573 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.50 | 0.6667 | 0.1130 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.67 | 0.6418 | 0.1324 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 21.55 | 0.6456 | 0.1235 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.77 | 0.6305 | 0.1361 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.19 | 0.6430 | 0.1250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.67 | 0.6844 | 0.1019 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.89 | 0.6555 | 0.1218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 21.41 | 0.6720 | 0.1021 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.65 | 0.6492 | 0.1200 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 20.70 | 0.6662 | 0.1288 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 22.22 | 0.7406 | 0.0783 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.92 | 0.7156 | 0.0793 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.23 | 0.7338 | 0.0785 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.13 | 0.7255 | 0.0780 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.40 | 0.7473 | 0.0764 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.41 | 0.7356 | 0.0710 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.61 | 0.7466 | 0.0729 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.56 | 0.7408 | 0.0711 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 20.72 | 0.6660 | 0.1269 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 20.06 | 0.6588 | 0.1061 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.51 | 0.6630 | 0.1006 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 20.33 | 0.6633 | 0.1036 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.46 | 0.6635 | 0.1027 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 20.21 | 0.6586 | 0.1051 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.53 | 0.6624 | 0.1006 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.41 | 0.6638 | 0.1039 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.54 | 0.6660 | 0.1014 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 22.45 | 0.7385 | 0.0785 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 21.96 | 0.7187 | 0.0779 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 22.48 | 0.7339 | 0.0767 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 22.26 | 0.7269 | 0.0770 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 21.90 | 0.7271 | 0.0797 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.51 | 0.7231 | 0.0748 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 22.51 | 0.7310 | 0.0755 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 22.59 | 0.7268 | 0.0752 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 19.16 | 0.5878 | 0.1573 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 21.49 | 0.6641 | 0.1129 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 20.67 | 0.6394 | 0.1325 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 21.55 | 0.6410 | 0.1233 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 20.77 | 0.6259 | 0.1357 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 19.19 | 0.6410 | 0.1249 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.66 | 0.6820 | 0.1019 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.89 | 0.6532 | 0.1216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 21.40 | 0.6680 | 0.1018 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 20.66 | 0.6457 | 0.1196 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 20.66 | 0.6619 | 0.1303 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 22.23 | 0.7391 | 0.0780 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 21.92 | 0.7143 | 0.0790 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 22.24 | 0.7325 | 0.0781 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 22.13 | 0.7242 | 0.0777 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 22.39 | 0.7453 | 0.0760 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 22.41 | 0.7343 | 0.0707 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 22.60 | 0.7447 | 0.0726 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 22.55 | 0.7393 | 0.0707 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 20.71 | 0.6624 | 0.1274 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 20.06 | 0.6563 | 0.1061 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.52 | 0.6606 | 0.1003 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 20.34 | 0.6609 | 0.1033 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.47 | 0.6609 | 0.1024 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 20.24 | 0.6568 | 0.1049 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 20.54 | 0.6597 | 0.1004 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 20.44 | 0.6618 | 0.1037 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 20.55 | 0.6638 | 0.1011 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 84.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.70 | 0.7876 | 0.1741 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 17.55 | 0.8046 | 0.2225 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 17.97 | 0.7963 | 0.2087 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 17.69 | 0.8067 | 0.2122 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 17.75 | 0.8028 | 0.2099 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 17.63 | 0.8029 | 0.2215 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 17.97 | 0.8001 | 0.2012 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 17.72 | 0.8066 | 0.2080 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 17.78 | 0.8037 | 0.2048 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 23.18 | 0.7041 | 0.2876 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 24.43 | 0.7758 | 0.2296 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 24.43 | 0.7758 | 0.2296 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 23.89 | 0.7580 | 0.2473 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 23.89 | 0.7580 | 0.2473 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 21.16 | 0.7423 | 0.2355 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 21.28 | 0.7632 | 0.2471 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 21.28 | 0.7632 | 0.2471 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 21.58 | 0.7536 | 0.2483 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 21.58 | 0.7536 | 0.2483 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 20.41 | 0.7270 | 0.2820 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 19.72 | 0.8164 | 0.2021 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 20.59 | 0.8065 | 0.1888 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 19.96 | 0.8177 | 0.1919 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 20.07 | 0.8126 | 0.1899 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 19.81 | 0.8219 | 0.1993 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 20.51 | 0.8201 | 0.1793 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 20.05 | 0.8267 | 0.1869 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 20.17 | 0.8239 | 0.1822 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 21.39 | 0.7349 | 0.2746 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.68 | 0.7458 | 0.3203 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 15.38 | 0.7397 | 0.3040 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 14.91 | 0.7470 | 0.3122 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 15.07 | 0.7440 | 0.3075 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 14.66 | 0.7436 | 0.3211 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 15.28 | 0.7355 | 0.3051 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 14.84 | 0.7448 | 0.3120 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 14.97 | 0.7405 | 0.3093 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.79 | 0.8273 | 0.1493 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.60 | 0.8234 | 0.1477 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.84 | 0.8273 | 0.1475 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.74 | 0.8256 | 0.1474 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.40 | 0.8253 | 0.1506 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.80 | 0.8260 | 0.1445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.74 | 0.8274 | 0.1465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.79 | 0.8265 | 0.1456 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.88 | 0.7758 | 0.2187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.73 | 0.8056 | 0.1767 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.02 | 0.7984 | 0.1771 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.59 | 0.7973 | 0.1861 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.92 | 0.7937 | 0.1817 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.89 | 0.7972 | 0.1748 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.94 | 0.8133 | 0.1635 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.23 | 0.8039 | 0.1670 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.58 | 0.8059 | 0.1637 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.89 | 0.7993 | 0.1638 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.70 | 0.7992 | 0.1941 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.72 | 0.8293 | 0.1484 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.50 | 0.8227 | 0.1466 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.67 | 0.8276 | 0.1453 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.61 | 0.8253 | 0.1453 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.92 | 0.8333 | 0.1469 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.98 | 0.8314 | 0.1418 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.03 | 0.8341 | 0.1439 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.02 | 0.8327 | 0.1421 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.78 | 0.7995 | 0.1906 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.97 | 0.8063 | 0.1674 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.39 | 0.8070 | 0.1630 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.22 | 0.8079 | 0.1640 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.32 | 0.8074 | 0.1622 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.14 | 0.8048 | 0.1679 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.39 | 0.8051 | 0.1635 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.28 | 0.8058 | 0.1638 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.38 | 0.8061 | 0.1622 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.48 | 0.8289 | 0.1773 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.12 | 0.8187 | 0.1710 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.55 | 0.8287 | 0.1706 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.39 | 0.8247 | 0.1695 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.08 | 0.8262 | 0.1798 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.60 | 0.8228 | 0.1637 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.54 | 0.8283 | 0.1684 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.59 | 0.8258 | 0.1662 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.30 | 0.7096 | 0.2844 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 24.75 | 0.7771 | 0.2178 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.24 | 0.7781 | 0.2130 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 24.21 | 0.7599 | 0.2386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 23.79 | 0.7680 | 0.2285 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.64 | 0.7653 | 0.2183 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.47 | 0.7941 | 0.1996 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.80 | 0.7831 | 0.1981 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 24.84 | 0.7768 | 0.2079 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.25 | 0.7729 | 0.2056 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 23.22 | 0.7561 | 0.2572 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 27.40 | 0.8325 | 0.1729 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.99 | 0.8188 | 0.1660 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.39 | 0.8311 | 0.1649 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.23 | 0.8259 | 0.1648 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.65 | 0.8373 | 0.1698 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.78 | 0.8329 | 0.1560 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.89 | 0.8389 | 0.1598 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.86 | 0.8363 | 0.1570 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 23.23 | 0.7522 | 0.2594 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.90 | 0.7935 | 0.2070 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.35 | 0.7884 | 0.2036 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.23 | 0.7943 | 0.2018 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.33 | 0.7920 | 0.2001 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 25.04 | 0.7925 | 0.2052 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.33 | 0.7864 | 0.2022 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.24 | 0.7928 | 0.1997 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.32 | 0.7905 | 0.1990 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 75.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.82 | 0.7896 | 0.1804 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 26.02 | 0.8444 | 0.1839 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 25.77 | 0.8341 | 0.1732 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 25.86 | 0.8440 | 0.1758 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 25.76 | 0.8396 | 0.1738 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 25.67 | 0.8435 | 0.1772 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 26.01 | 0.8382 | 0.1613 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 25.76 | 0.8451 | 0.1669 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 25.83 | 0.8418 | 0.1640 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 23.47 | 0.7405 | 0.2451 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 25.73 | 0.7958 | 0.1910 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 25.73 | 0.7958 | 0.1910 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 25.41 | 0.7824 | 0.2059 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 25.41 | 0.7824 | 0.2059 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 21.48 | 0.7698 | 0.2006 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 25.58 | 0.8127 | 0.1856 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 25.58 | 0.8127 | 0.1856 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 25.33 | 0.8024 | 0.1812 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 25.33 | 0.8024 | 0.1812 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 24.29 | 0.8036 | 0.2059 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 24.91 | 0.8495 | 0.1711 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 25.12 | 0.8355 | 0.1611 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 24.80 | 0.8477 | 0.1630 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 24.78 | 0.8421 | 0.1611 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 25.58 | 0.8514 | 0.1664 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 25.81 | 0.8469 | 0.1516 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 25.60 | 0.8530 | 0.1571 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 25.61 | 0.8502 | 0.1540 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 24.21 | 0.8025 | 0.2057 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 20.35 | 0.7999 | 0.2782 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 20.84 | 0.7954 | 0.2596 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 20.52 | 0.8013 | 0.2690 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 20.65 | 0.7984 | 0.2641 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 20.32 | 0.8000 | 0.2797 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 20.77 | 0.7928 | 0.2627 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 20.47 | 0.8008 | 0.2696 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 20.59 | 0.7970 | 0.2659 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 26.81 | 0.8347 | 0.1479 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.51 | 0.8289 | 0.1443 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 26.83 | 0.8335 | 0.1444 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.69 | 0.8313 | 0.1441 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.47 | 0.8317 | 0.1482 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.81 | 0.8315 | 0.1401 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 26.84 | 0.8336 | 0.1429 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 26.86 | 0.8324 | 0.1416 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.13 | 0.7878 | 0.2069 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.91 | 0.8118 | 0.1736 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.22 | 0.8054 | 0.1747 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.85 | 0.8048 | 0.1823 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.19 | 0.8014 | 0.1775 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.15 | 0.8062 | 0.1703 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.10 | 0.8194 | 0.1590 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.42 | 0.8110 | 0.1632 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.78 | 0.8141 | 0.1582 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.13 | 0.8080 | 0.1588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 25.32 | 0.8132 | 0.1798 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 26.69 | 0.8356 | 0.1465 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.47 | 0.8278 | 0.1431 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.68 | 0.8335 | 0.1431 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.61 | 0.8309 | 0.1427 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.81 | 0.8379 | 0.1438 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 26.84 | 0.8354 | 0.1381 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 26.94 | 0.8384 | 0.1402 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 26.91 | 0.8368 | 0.1385 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 25.34 | 0.8129 | 0.1788 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.19 | 0.8148 | 0.1698 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.57 | 0.8157 | 0.1635 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.43 | 0.8161 | 0.1661 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.53 | 0.8161 | 0.1644 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 25.31 | 0.8142 | 0.1703 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 25.57 | 0.8145 | 0.1634 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 25.47 | 0.8152 | 0.1657 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 25.57 | 0.8153 | 0.1627 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 27.01 | 0.8444 | 0.1740 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 26.53 | 0.8319 | 0.1667 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.09 | 0.8424 | 0.1678 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 26.83 | 0.8377 | 0.1663 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 26.68 | 0.8419 | 0.1733 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.18 | 0.8359 | 0.1577 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.23 | 0.8428 | 0.1628 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.27 | 0.8397 | 0.1601 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 23.61 | 0.7451 | 0.2435 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 25.61 | 0.7948 | 0.1951 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 24.74 | 0.7935 | 0.1942 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 25.37 | 0.7803 | 0.2105 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 24.58 | 0.7865 | 0.2015 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 23.80 | 0.7903 | 0.1878 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.05 | 0.8155 | 0.1736 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.09 | 0.8027 | 0.1755 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 25.53 | 0.8030 | 0.1765 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 24.67 | 0.7974 | 0.1762 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 24.54 | 0.8040 | 0.2061 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 26.90 | 0.8464 | 0.1690 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 26.52 | 0.8312 | 0.1623 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 26.92 | 0.8430 | 0.1631 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 26.75 | 0.8376 | 0.1617 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 26.95 | 0.8482 | 0.1661 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.17 | 0.8423 | 0.1525 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.24 | 0.8481 | 0.1577 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.23 | 0.8456 | 0.1547 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 24.58 | 0.8035 | 0.2079 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.39 | 0.8079 | 0.2145 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.76 | 0.8037 | 0.2082 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.67 | 0.8076 | 0.2099 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.80 | 0.8060 | 0.2078 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.47 | 0.8076 | 0.2169 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.71 | 0.8020 | 0.2098 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.60 | 0.8068 | 0.2113 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.70 | 0.8048 | 0.2078 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 25.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 35.38 | 0.9085 | 0.0209 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 36.40 | 0.9333 | 0.0504 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 36.35 | 0.9295 | 0.0445 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 37.09 | 0.9341 | 0.0472 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 36.73 | 0.9320 | 0.0455 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 36.41 | 0.9344 | 0.0501 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 36.72 | 0.9326 | 0.0427 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 37.17 | 0.9356 | 0.0459 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 36.90 | 0.9343 | 0.0439 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 33.93 | 0.9135 | 0.0280 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 35.58 | 0.9280 | 0.0271 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 35.58 | 0.9280 | 0.0271 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 36.33 | 0.9237 | 0.0314 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 36.33 | 0.9237 | 0.0314 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 33.77 | 0.9206 | 0.0318 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 35.93 | 0.9287 | 0.0292 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 35.93 | 0.9287 | 0.0292 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 36.81 | 0.9270 | 0.0297 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 36.81 | 0.9270 | 0.0297 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 35.37 | 0.9311 | 0.0342 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 32.13 | 0.9313 | 0.0520 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 32.20 | 0.9271 | 0.0465 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 32.78 | 0.9323 | 0.0492 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 32.52 | 0.9304 | 0.0474 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 32.30 | 0.9311 | 0.0511 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 33.03 | 0.9315 | 0.0441 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 33.34 | 0.9343 | 0.0475 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 33.27 | 0.9336 | 0.0452 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 35.14 | 0.9292 | 0.0342 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.78 | 0.8009 | 0.1498 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 15.37 | 0.7940 | 0.1479 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 15.03 | 0.7979 | 0.1492 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 15.24 | 0.7965 | 0.1480 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 14.78 | 0.8008 | 0.1495 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 15.34 | 0.7919 | 0.1492 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 15.02 | 0.7969 | 0.1493 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 15.22 | 0.7946 | 0.1489 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 35.17 | 0.9080 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 34.94 | 0.9076 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 35.07 | 0.9078 | 0.0220 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 35.00 | 0.9077 | 0.0222 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 35.18 | 0.9082 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 35.03 | 0.9079 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 35.12 | 0.9080 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 35.06 | 0.9079 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 35.37 | 0.9085 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 35.28 | 0.9084 | 0.0212 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 35.29 | 0.9082 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 35.38 | 0.9089 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 35.39 | 0.9087 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 35.38 | 0.9085 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 35.24 | 0.9083 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 35.25 | 0.9082 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 35.39 | 0.9088 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 35.39 | 0.9087 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 35.34 | 0.9089 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 35.13 | 0.9082 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 34.91 | 0.9075 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 35.07 | 0.9079 | 0.0220 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 35.02 | 0.9077 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 35.18 | 0.9083 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 35.05 | 0.9078 | 0.0220 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 35.16 | 0.9081 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 35.13 | 0.9080 | 0.0218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 35.34 | 0.9089 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 34.89 | 0.9073 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 34.54 | 0.9067 | 0.0235 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 34.78 | 0.9071 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 34.72 | 0.9070 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 34.71 | 0.9071 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 34.50 | 0.9066 | 0.0233 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 34.65 | 0.9069 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 34.61 | 0.9068 | 0.0231 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 36.53 | 0.9322 | 0.0465 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 36.47 | 0.9287 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 37.10 | 0.9328 | 0.0448 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 36.79 | 0.9310 | 0.0433 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 36.43 | 0.9328 | 0.0468 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 36.87 | 0.9314 | 0.0408 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 37.20 | 0.9338 | 0.0441 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 36.99 | 0.9328 | 0.0422 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 34.85 | 0.9134 | 0.0251 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 35.91 | 0.9267 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 34.16 | 0.9051 | 0.0224 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 36.35 | 0.9228 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 34.74 | 0.9066 | 0.0231 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 34.94 | 0.9197 | 0.0288 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 36.26 | 0.9272 | 0.0274 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 35.20 | 0.9084 | 0.0211 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 36.69 | 0.9256 | 0.0280 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 35.10 | 0.9080 | 0.0212 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 36.49 | 0.9307 | 0.0290 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 36.69 | 0.9325 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 36.41 | 0.9285 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 37.14 | 0.9333 | 0.0446 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 36.80 | 0.9317 | 0.0431 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 36.72 | 0.9319 | 0.0455 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 37.24 | 0.9324 | 0.0403 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 37.58 | 0.9347 | 0.0431 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 37.50 | 0.9341 | 0.0413 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 36.65 | 0.9312 | 0.0294 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.10 | 0.8826 | 0.0637 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.18 | 0.8744 | 0.0767 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.72 | 0.8794 | 0.0686 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.58 | 0.8781 | 0.0711 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 29.02 | 0.8828 | 0.0641 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 28.00 | 0.8733 | 0.0769 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 28.55 | 0.8793 | 0.0698 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 28.37 | 0.8775 | 0.0729 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.95 | 0.8195 | 0.1893 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_local | 27.08 | 0.8692 | 0.2258 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto100_local | 26.77 | 0.8596 | 0.2005 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto25_local | 26.90 | 0.8686 | 0.2070 | 1.00 |
| gs_tokcnw_cnn448_nat_dil_al_tto50_local | 26.79 | 0.8645 | 0.2020 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_local | 26.76 | 0.8681 | 0.2179 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 27.06 | 0.8632 | 0.1881 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | 26.83 | 0.8696 | 0.1974 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | 26.89 | 0.8665 | 0.1914 | 1.00 |
| gs_tokcnw_cnn_p3h_flw448_p3h_al_local | 24.62 | 0.7861 | 0.2591 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | 26.83 | 0.8302 | 0.2051 | 1.00 |
| gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | 26.83 | 0.8302 | 0.2051 | 1.00 |
| gs_tokcnw_cnn_p3h_fss448_p3h_al_local | 26.52 | 0.8199 | 0.2217 | 1.00 |
| gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | 26.52 | 0.8199 | 0.2217 | 1.00 |
| gs_tokcnw_cnn_pix2_flw448_pix2_al_local | 22.67 | 0.8096 | 0.2163 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 26.70 | 0.8433 | 0.2022 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 26.70 | 0.8433 | 0.2022 | 1.00 |
| gs_tokcnw_cnn_pix2_fss448_pix2_al_local | 26.44 | 0.8358 | 0.1987 | 1.00 |
| gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | 26.44 | 0.8358 | 0.1987 | 1.00 |
| gs_tokcnw_cnn_pix448_pix_al_local | 25.45 | 0.8370 | 0.2253 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_local | 25.83 | 0.8731 | 0.2118 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto100_local | 25.97 | 0.8607 | 0.1873 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto25_local | 25.69 | 0.8714 | 0.1939 | 1.00 |
| gs_tokcnw_f5448_nat_dil_al_tto50_local | 25.66 | 0.8665 | 0.1890 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_local | 26.55 | 0.8744 | 0.2084 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | 26.74 | 0.8700 | 0.1796 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | 26.55 | 0.8756 | 0.1888 | 1.00 |
| gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | 26.55 | 0.8730 | 0.1832 | 1.00 |
| gs_tokcnw_f5_pix448_pix_al_local | 25.37 | 0.8364 | 0.2243 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 18.36 | 0.7929 | 0.3222 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 19.09 | 0.7875 | 0.3108 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 18.62 | 0.7926 | 0.3145 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 18.85 | 0.7900 | 0.3122 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_local | 18.32 | 0.7927 | 0.3224 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto100_local | 18.97 | 0.7847 | 0.3108 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto25_local | 18.57 | 0.7918 | 0.3137 | 1.00 |
| gs_tokrife_mw448_nat_dil_al_tto50_local | 18.78 | 0.7883 | 0.3122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_local] | 27.82 | 0.8555 | 0.1588 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.48 | 0.8504 | 0.1545 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 27.81 | 0.8543 | 0.1550 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.66 | 0.8524 | 0.1544 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.49 | 0.8531 | 0.1589 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.78 | 0.8527 | 0.1503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 27.81 | 0.8546 | 0.1531 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 27.83 | 0.8535 | 0.1516 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 25.26 | 0.8203 | 0.2180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.97 | 0.8379 | 0.1842 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 26.29 | 0.8331 | 0.1848 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.92 | 0.8332 | 0.1935 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 26.26 | 0.8304 | 0.1880 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 25.27 | 0.8340 | 0.1804 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.13 | 0.8437 | 0.1690 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.48 | 0.8375 | 0.1730 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.84 | 0.8403 | 0.1689 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 26.21 | 0.8358 | 0.1687 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix448_pix_al_local] | 26.40 | 0.8393 | 0.1901 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_local] | 27.72 | 0.8565 | 0.1571 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.43 | 0.8496 | 0.1530 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.67 | 0.8546 | 0.1534 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.58 | 0.8522 | 0.1527 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_local] | 27.82 | 0.8580 | 0.1545 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 27.81 | 0.8557 | 0.1483 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 27.92 | 0.8582 | 0.1503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 27.87 | 0.8568 | 0.1485 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_f5_pix448_pix_al_local] | 26.42 | 0.8392 | 0.1890 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.20 | 0.8386 | 0.1806 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.51 | 0.8391 | 0.1755 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 26.40 | 0.8395 | 0.1779 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.48 | 0.8393 | 0.1767 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_local] | 26.30 | 0.8384 | 0.1807 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto100_local] | 26.53 | 0.8383 | 0.1750 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto25_local] | 26.44 | 0.8390 | 0.1768 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_mw448_nat_dil_al_tto50_local] | 26.53 | 0.8391 | 0.1744 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_local] | 28.09 | 0.8691 | 0.2127 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto100_local] | 27.57 | 0.8582 | 0.1929 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto25_local] | 28.15 | 0.8675 | 0.1974 | 1.00 |
| hyb_token[gs_tokcnw_cnn448_nat_dil_al_tto50_local] | 27.89 | 0.8633 | 0.1934 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_local] | 27.77 | 0.8668 | 0.2112 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.23 | 0.8617 | 0.1834 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local] | 28.30 | 0.8679 | 0.1918 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local] | 28.32 | 0.8650 | 0.1862 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_flw448_p3h_al_local] | 24.75 | 0.7892 | 0.2572 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl448_p3h_al_local] | 26.71 | 0.8288 | 0.2091 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local] | 25.81 | 0.8239 | 0.2052 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss448_p3h_al_local] | 26.49 | 0.8180 | 0.2259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local] | 25.66 | 0.8187 | 0.2128 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_flw448_pix2_al_local] | 24.95 | 0.8250 | 0.2025 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.15 | 0.8449 | 0.1896 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.16 | 0.8314 | 0.1856 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss448_pix2_al_local] | 26.64 | 0.8358 | 0.1933 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local] | 25.76 | 0.8275 | 0.1867 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix448_pix_al_local] | 25.69 | 0.8373 | 0.2232 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_local] | 28.00 | 0.8710 | 0.2072 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto100_local] | 27.56 | 0.8580 | 0.1875 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto25_local] | 27.99 | 0.8683 | 0.1925 | 1.00 |
| hyb_token[gs_tokcnw_f5448_nat_dil_al_tto50_local] | 27.81 | 0.8635 | 0.1885 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_local] | 28.05 | 0.8721 | 0.2053 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto100_local] | 28.23 | 0.8669 | 0.1796 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto25_local] | 28.32 | 0.8722 | 0.1876 | 1.00 |
| hyb_token[gs_tokcnw_f5_mw448_nat_dil_al_tto50_local] | 28.29 | 0.8698 | 0.1827 | 1.00 |
| hyb_token[gs_tokcnw_f5_pix448_pix_al_local] | 25.72 | 0.8369 | 0.2250 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.95 | 0.8274 | 0.2416 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.94 | 0.8197 | 0.2440 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 25.07 | 0.8257 | 0.2403 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.12 | 0.8233 | 0.2411 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_local] | 24.97 | 0.8274 | 0.2420 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto100_local] | 24.86 | 0.8180 | 0.2447 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto25_local] | 24.95 | 0.8251 | 0.2409 | 1.00 |
| hyb_token[gs_tokrife_mw448_nat_dil_al_tto50_local] | 24.96 | 0.8223 | 0.2410 | 1.00 |

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
| in035 | gs_tokcnw_cnn448_nat_dil_al_local | aligned_int | 1090 | None | classic | 1.78 | False | 193759 | 0.176 | 35.1 | 33.25 | 0.42 | 0.007 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto100_local | aligned_int | 1090 | None | classic | 1.78 | False | 193759 | 0.176 | 32.6 | 33.25 | 0.42 | 0.007 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto25_local | aligned_int | 1090 | None | classic | 1.78 | False | 193759 | 0.176 | 31.3 | 33.25 | 0.42 | 0.007 |
| in035 | gs_tokcnw_cnn448_nat_dil_al_tto50_local | aligned_int | 1090 | None | classic | 1.78 | False | 193759 | 0.176 | 38.2 | 33.25 | 0.42 | 0.007 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_local | aligned_int | 1058 | None | classic | 1.67 | False | 196821 | 0.174 | 50.1 | 33.20 | 0.08 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1058 | None | classic | 1.67 | False | 196821 | 0.174 | 44.1 | 33.20 | 0.08 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto25_local | aligned_int | 1058 | None | classic | 1.67 | False | 196821 | 0.174 | 46.4 | 33.20 | 0.08 | 0.008 |
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto50_local | aligned_int | 1058 | None | classic | 1.67 | False | 196821 | 0.174 | 50.5 | 33.20 | 0.08 | 0.008 |
| in035 | gs_tokcnw_cnn_p3h_flw448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2274454 | 0.247 | 39.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2273496 | 0.800 | 64.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fsl_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2273496 | 0.800 | 64.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2273496 | 0.609 | 39.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_p3h_fss_g448_p3h_al_local | aligned_int | 1920 | None | splat | 0.30 | False | 2273496 | 0.609 | 39.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_flw448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2274454 | 0.247 | 46.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2273496 | 0.800 | 88.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2273496 | 0.800 | 88.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2273496 | 0.609 | 46.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fss_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2273496 | 0.609 | 46.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2145104 | 0.800 | 179.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_f5448_nat_dil_al_local | aligned_int | 1092 | None | classic | 1.78 | False | 205021 | 0.173 | 45.4 | 33.25 | 0.36 | 0.007 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto100_local | aligned_int | 1092 | None | classic | 1.78 | False | 205021 | 0.173 | 40.5 | 33.25 | 0.36 | 0.007 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto25_local | aligned_int | 1092 | None | classic | 1.78 | False | 205021 | 0.173 | 38.0 | 33.25 | 0.36 | 0.007 |
| in035 | gs_tokcnw_f5448_nat_dil_al_tto50_local | aligned_int | 1092 | None | classic | 1.78 | False | 205021 | 0.173 | 33.9 | 33.25 | 0.36 | 0.007 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_local | aligned_int | 1060 | None | classic | 1.68 | False | 195080 | 0.175 | 44.5 | 33.46 | 0.09 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto100_local | aligned_int | 1060 | None | classic | 1.68 | False | 195080 | 0.175 | 45.0 | 33.46 | 0.09 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto25_local | aligned_int | 1060 | None | classic | 1.68 | False | 195080 | 0.175 | 38.7 | 33.46 | 0.09 | 0.006 |
| in035 | gs_tokcnw_f5_mw448_nat_dil_al_tto50_local | aligned_int | 1060 | None | classic | 1.68 | False | 195080 | 0.175 | 44.2 | 33.46 | 0.09 | 0.006 |
| in035 | gs_tokcnw_f5_pix448_pix_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2299423 | 0.800 | 88.7 | — | 0.00 | 0.000 |
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1047 | None | classic | 1.64 | False | 185315 | 0.324 | 56.8 | 32.94 | 0.10 | 0.006 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1047 | None | classic | 1.64 | False | 185315 | 0.324 | 37.5 | 32.94 | 0.10 | 0.006 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1047 | None | classic | 1.64 | False | 185315 | 0.324 | 52.5 | 32.94 | 0.10 | 0.006 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1047 | None | classic | 1.64 | False | 185315 | 0.324 | 38.5 | 32.94 | 0.10 | 0.006 |
| in035 | gs_tokrife_mw448_nat_dil_al_local | aligned_int | 1015 | None | classic | 1.54 | False | 185065 | 0.171 | 47.2 | 32.95 | 0.40 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto100_local | aligned_int | 1015 | None | classic | 1.54 | False | 185065 | 0.171 | 38.2 | 32.95 | 0.40 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto25_local | aligned_int | 1015 | None | classic | 1.54 | False | 185065 | 0.171 | 45.4 | 32.95 | 0.40 | 0.007 |
| in035 | gs_tokrife_mw448_nat_dil_al_tto50_local | aligned_int | 1015 | None | classic | 1.54 | False | 185065 | 0.171 | 39.3 | 32.95 | 0.40 | 0.007 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.721 | 0.107 |
| in035 | mask_ent | 0.552 | 0.107 |
| in035 | mask_grad | 0.365 | 0.107 |
| in035 | r_col | 0.744 | 0.107 |
| in035 | r_warp | 0.799 | 0.107 |

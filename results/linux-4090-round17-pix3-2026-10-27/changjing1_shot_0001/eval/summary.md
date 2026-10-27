# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 93.9% | 24.57 / 0.1703 | 28.77 / 0.1686 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 93.5% | 24.52 / 0.1720 | 26.08 / 0.2041 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 20.4% | 19.28 / 0.1045 | 20.33 / 0.1260 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 96.1% | 24.62 / 0.1731 | 27.95 / 0.1490 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 96.1% | 24.61 / 0.1726 | 26.68 / 0.1815 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 20.4% | 19.26 / 0.1095 | 20.87 / 0.1113 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 23.95 / 0.1893 | — / — | 17.22 / 0.1504 | 35.38 / 0.0209 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.23 / 0.1834 | — / — | 22.51 / 0.0748 | 36.87 / 0.0408 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.15 / 0.1896 | — / — | 21.66 / 0.1019 | 36.26 / 0.0274 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.16 / 0.1856 | — / — | 20.89 / 0.1216 | 35.20 / 0.0211 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.84 / 0.1649 | — / — | 22.05 / 0.0953 | 37.26 / 0.0171 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.86 / 0.1782 | — / — | 21.50 / 0.0980 | 36.80 / 0.0309 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.95 / 0.1839 | — / — | 20.80 / 0.1211 | 34.95 / 0.0216 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 18.1%） | — | — | 23.95 / 0.1893 | — / — | 35.38 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 23.55 / 0.2410 | — | — | — |
| in035 | 2 | 0-3 | 24.98 / 0.1832 | — | — | — |
| in035 | 4 | 3-5 | 23.33 / 0.1436 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 23.95 / 0.1893 | — | 35.38 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.23 / 0.1834 | — | 36.87 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 15.6% | 27.78 / 0.1503 | — | 35.03 | 3/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.15 / 0.1896 | — | 36.26 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 15.3% | 27.13 / 0.1690 | — | 35.24 | 2/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.16 / 0.1856 | — | 35.20 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 10.3% | 26.48 / 0.1730 | — | 35.25 | 2/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.84 / 0.1649 | — | 37.26 | 3/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 15.4% | 27.48 / 0.1636 | — | 35.36 | 3/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 26.86 / 0.1782 | — | 36.80 | 2/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 15.4% | 26.93 / 0.1622 | — | 35.35 | 3/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 25.95 / 0.1839 | — | 34.95 | 2/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 10.2% | 26.34 / 0.1696 | — | 35.35 | 2/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 23.95 / 0.1893 | — / — | 35.38 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.23 / 0.1834 | — / — | 36.87 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.78 / 0.1503 | — / — | 35.03 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 17.22 / 0.1504 | 35.38 / 0.0209 | 23.95 / 0.1893 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 18.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.22 | 0.5539 | 0.1504 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 23.16 | 0.7446 | 0.0680 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 21.59 | 0.6857 | 0.1046 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 21.59 | 0.6857 | 0.1046 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 22.02 | 0.6871 | 0.0949 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 21.41 | 0.6957 | 0.1013 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 21.41 | 0.6957 | 0.1013 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.51 | 0.7245 | 0.0753 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.67 | 0.6844 | 0.1019 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.89 | 0.6555 | 0.1218 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.06 | 0.6867 | 0.0951 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 21.51 | 0.6941 | 0.0978 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.79 | 0.6633 | 0.1211 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.51 | 0.7231 | 0.0748 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.66 | 0.6820 | 0.1019 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.89 | 0.6532 | 0.1216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.05 | 0.6844 | 0.0953 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 21.50 | 0.6921 | 0.0980 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.80 | 0.6610 | 0.1211 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 84.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.70 | 0.7876 | 0.1741 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 17.97 | 0.8001 | 0.2012 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 21.28 | 0.7632 | 0.2471 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 21.28 | 0.7632 | 0.2471 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 21.92 | 0.7595 | 0.2155 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 21.61 | 0.7740 | 0.2312 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 21.61 | 0.7740 | 0.2312 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.80 | 0.8260 | 0.1445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.94 | 0.8133 | 0.1635 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.23 | 0.8039 | 0.1670 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.35 | 0.8148 | 0.1561 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.82 | 0.8166 | 0.1549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.16 | 0.8065 | 0.1620 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.60 | 0.8228 | 0.1637 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.47 | 0.7941 | 0.1996 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.80 | 0.7831 | 0.1981 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.84 | 0.7924 | 0.1632 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.78 | 0.8066 | 0.1774 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.05 | 0.7896 | 0.1878 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 25.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 35.38 | 0.9085 | 0.0209 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 36.72 | 0.9326 | 0.0427 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 35.93 | 0.9287 | 0.0292 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 35.93 | 0.9287 | 0.0292 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 37.23 | 0.9077 | 0.0184 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 36.87 | 0.9328 | 0.0322 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 36.87 | 0.9328 | 0.0322 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 35.03 | 0.9079 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 35.24 | 0.9083 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 35.25 | 0.9082 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 35.36 | 0.9086 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 35.35 | 0.9086 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 35.35 | 0.9084 | 0.0210 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 36.87 | 0.9314 | 0.0408 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 36.26 | 0.9272 | 0.0274 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 35.20 | 0.9084 | 0.0211 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 37.26 | 0.9089 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 36.80 | 0.9309 | 0.0309 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 34.95 | 0.9074 | 0.0216 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.95 | 0.8195 | 0.1893 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 27.06 | 0.8632 | 0.1881 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 26.70 | 0.8433 | 0.2022 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 26.70 | 0.8433 | 0.2022 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 27.26 | 0.8250 | 0.1774 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 26.46 | 0.8506 | 0.1915 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 26.46 | 0.8506 | 0.1915 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.78 | 0.8527 | 0.1503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.13 | 0.8437 | 0.1690 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.48 | 0.8375 | 0.1730 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.48 | 0.8435 | 0.1636 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.93 | 0.8455 | 0.1622 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.34 | 0.8386 | 0.1696 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.23 | 0.8617 | 0.1834 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.15 | 0.8449 | 0.1896 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.16 | 0.8314 | 0.1856 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.84 | 0.8287 | 0.1649 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.86 | 0.8519 | 0.1782 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.95 | 0.8321 | 0.1839 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1058 | None | classic | 1.67 | False | 196821 | 0.174 | 44.1 | 33.20 | 0.08 | 0.008 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2273496 | 0.800 | 101.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2273496 | 0.800 | 101.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1993536 | 0.800 | 11.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1993536 | 0.800 | 7.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1993536 | 0.800 | 7.4 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.721 | 0.107 |
| in035 | mask_ent | 0.552 | 0.107 |
| in035 | mask_grad | 0.365 | 0.107 |
| in035 | r_col | 0.744 | 0.107 |
| in035 | r_warp | 0.799 | 0.107 |

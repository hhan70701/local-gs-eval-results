# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 79.3% | 20.06 / 0.1609 | 22.49 / 0.2287 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 80.2% | 20.08 / 0.1617 | 22.52 / 0.2005 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | 79.2% | 20.09 / 0.1598 | 22.85 / 0.2068 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 79.5% | 20.08 / 0.1594 | 22.71 / 0.2003 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_local | 54.7% | 18.87 / 0.1279 | 21.38 / 0.1680 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | 55.3% | 18.93 / 0.1284 | 21.48 / 0.1451 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | 54.4% | 18.91 / 0.1265 | 21.74 / 0.1480 | — | — |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | 54.5% | 18.91 / 0.1269 | 21.63 / 0.1439 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_local | 36.7% | 18.67 / 0.1049 | 21.25 / 0.1385 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | 36.9% | 18.68 / 0.1067 | 21.40 / 0.1202 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | 36.4% | 18.70 / 0.1035 | 21.66 / 0.1234 | — | — |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | 36.4% | 18.68 / 0.1041 | 21.59 / 0.1192 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 20.11 / 0.1763 | 22.82 / 0.2384 | 14.24 / 0.1294 | 29.18 / 0.0179 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 22.39 / 0.2416 | 24.61 / 0.2267 | 16.83 / 0.0838 | 28.41 / 0.0223 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.49 / 0.2090 | 24.78 / 0.1899 | 17.01 / 0.0791 | 28.42 / 0.0194 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.67 / 0.2204 | 24.85 / 0.2036 | 17.09 / 0.0801 | 28.49 / 0.0202 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.61 / 0.2136 | 24.65 / 0.1981 | 17.06 / 0.0794 | 28.68 / 0.0190 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 22.02 / 0.2162 | 23.83 / 0.2437 | 16.52 / 0.0898 | 28.98 / 0.0214 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 22.10 / 0.1928 | 23.72 / 0.2215 | 16.67 / 0.0854 | 29.03 / 0.0192 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 22.26 / 0.1988 | 23.78 / 0.2290 | 16.74 / 0.0866 | 29.08 / 0.0192 |
| in035 | hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 22.22 / 0.1954 | 23.65 / 0.2270 | 16.72 / 0.0857 | 29.12 / 0.0188 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 21.37 / 0.2112 | 22.31 / 0.2748 | 15.84 / 0.1011 | 28.96 / 0.0198 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 21.46 / 0.1927 | 21.97 / 0.2911 | 15.98 / 0.0970 | 28.91 / 0.0188 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 21.55 / 0.1977 | 22.31 / 0.2683 | 16.01 / 0.0981 | 29.04 / 0.0186 |
| in035 | hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 21.53 / 0.1948 | 22.15 / 0.2722 | 16.01 / 0.0972 | 28.99 / 0.0186 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 23.9%） | — | — | 20.11 / 0.1763 | 22.82 / 0.2384 | 29.18 |
| in035 | rife | 69.5% | 79.3% | 22.39 / 0.2416 | 24.61 / 0.2267 | 28.41 |
| in035 | rife_w30 | 42.0% | 54.7% | 22.02 / 0.2162 | 23.83 / 0.2437 | 28.98 |
| in035 | rife_w40 | 24.5% | 36.7% | 21.37 / 0.2112 | 22.31 / 0.2748 | 28.96 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | rife_w30 | rife_w40 | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 18.41 / 0.2296 | — | +4.05 / +0.0251 (core 77.5%) | +3.36 / +0.0191 (core 53.5%) | +2.12 / +0.0200 (core 30.7%) | — | — | — |
| in035 | 2 | 0-3 | 19.62 / 0.1740 | — | +1.93 / +0.0845 (core 77.5%) | +1.77 / +0.0656 (core 53.5%) | +1.25 / +0.0574 (core 30.7%) | — | — | — |
| in035 | 4 | 3-5 | 22.29 / 0.1254 | — | +0.86 / +0.0861 (core 42.5%) | +0.61 / +0.0348 (core 14.2%) | +0.41 / +0.0271 (core 8.9%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 20.11 / 0.1763 | 22.82 | 29.18 | — |
| in035 | rife | 不复核 | —% | 22.39 / 0.2416 | 24.61 | 28.41 | 0/3 |
| in035 | rife | oracle | 18.9% | 22.37 / 0.1527 | 25.43 | 29.06 | 2/3 |
| in035 | rife | 不复核 | —% | 22.49 / 0.2090 | 24.78 | 28.42 | 1/3 |
| in035 | rife | oracle | 19.1% | 22.54 / 0.1438 | 25.96 | 28.79 | 2/3 |
| in035 | rife | 不复核 | —% | 22.67 / 0.2204 | 24.85 | 28.49 | 0/3 |
| in035 | rife | oracle | 18.9% | 22.62 / 0.1483 | 25.77 | 28.93 | 2/3 |
| in035 | rife | 不复核 | —% | 22.61 / 0.2136 | 24.65 | 28.68 | 1/3 |
| in035 | rife | oracle | 19.0% | 22.59 / 0.1457 | 25.76 | 29.01 | 2/3 |
| in035 | rife_w30 | 不复核 | —% | 22.02 / 0.2162 | 23.83 | 28.98 | 0/3 |
| in035 | rife_w30 | oracle | 14.4% | 22.09 / 0.1520 | 24.34 | 29.21 | 2/3 |
| in035 | rife_w30 | 不复核 | —% | 22.10 / 0.1928 | 23.72 | 29.03 | 1/3 |
| in035 | rife_w30 | oracle | 14.6% | 22.23 / 0.1448 | 24.46 | 29.05 | 2/3 |
| in035 | rife_w30 | 不复核 | —% | 22.26 / 0.1988 | 23.78 | 29.08 | 1/3 |
| in035 | rife_w30 | oracle | 14.4% | 22.31 / 0.1485 | 24.36 | 29.10 | 2/3 |
| in035 | rife_w30 | 不复核 | —% | 22.22 / 0.1954 | 23.65 | 29.12 | 1/3 |
| in035 | rife_w30 | oracle | 14.4% | 22.29 / 0.1464 | 24.34 | 29.09 | 2/3 |
| in035 | rife_w40 | 不复核 | —% | 21.37 / 0.2112 | 22.31 | 28.96 | 0/3 |
| in035 | rife_w40 | oracle | 8.9% | 21.52 / 0.1580 | 23.07 | 29.19 | 2/3 |
| in035 | rife_w40 | 不复核 | —% | 21.46 / 0.1927 | 21.97 | 28.91 | 1/3 |
| in035 | rife_w40 | oracle | 9.0% | 21.66 / 0.1526 | 23.08 | 29.13 | 2/3 |
| in035 | rife_w40 | 不复核 | —% | 21.55 / 0.1977 | 22.31 | 29.04 | 0/3 |
| in035 | rife_w40 | oracle | 8.9% | 21.69 / 0.1551 | 23.09 | 29.16 | 2/3 |
| in035 | rife_w40 | 不复核 | —% | 21.53 / 0.1948 | 22.15 | 28.99 | 1/3 |
| in035 | rife_w40 | oracle | 8.9% | 21.68 / 0.1537 | 23.04 | 29.15 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 20.11 / 0.1763 | 22.82 / 0.2384 | — |
| in035 | FF | 0（前馈） | 1296×1163（87%） | 30.74 | 22.39 / 0.2416 | 24.61 / 0.2267 | 0/3 |
| in035 | 25 | 1.85 s | 1296×1163（87%） | 32.83 | 22.67 / 0.2204 | 24.85 / 0.2036 | 0/3 |
| in035 | 50 | 3.70 s | 1296×1163（87%） | 33.48 | 22.61 / 0.2136 | 24.65 / 0.1981 | 1/3 |
| in035 | 100 | 7.42 s | 1296×1163（87%） | 34.03 | 22.49 / 0.2090 | 24.78 / 0.1899 | 1/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 20.11 / 0.1763 | 22.82 / 0.2384 | 29.18 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 22.39 / 0.2416 | 24.61 / 0.2267 | 28.41 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 22.37 / 0.1527 | 25.43 / 0.1892 | 29.06 | 2/3 |
| in035 | rife | GS 测试时优化 25 步 | 直接 | 22.67 / 0.2204 | 24.85 / 0.2036 | 28.49 | 0/3 |
| in035 | rife | GS 测试时优化 25 步 | oracle | 22.62 / 0.1483 | 25.77 / 0.1692 | 28.93 | 2/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 22.61 / 0.2136 | 24.65 / 0.1981 | 28.68 | 1/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 22.59 / 0.1457 | 25.76 / 0.1628 | 29.01 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 22.49 / 0.2090 | 24.78 / 0.1899 | 28.42 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 22.54 / 0.1438 | 25.96 / 0.1588 | 28.79 | 2/3 |
| in035 | rife_w30 | GS 前馈颜色 | 直接 | 22.02 / 0.2162 | 23.83 / 0.2437 | 28.98 | 0/3 |
| in035 | rife_w30 | GS 前馈颜色 | oracle | 22.09 / 0.1520 | 24.34 / 0.2194 | 29.21 | 2/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | 直接 | 22.26 / 0.1988 | 23.78 / 0.2290 | 29.08 | 1/3 |
| in035 | rife_w30 | GS 测试时优化 25 步 | oracle | 22.31 / 0.1485 | 24.36 / 0.2067 | 29.10 | 2/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | 直接 | 22.22 / 0.1954 | 23.65 / 0.2270 | 29.12 | 1/3 |
| in035 | rife_w30 | GS 测试时优化 50 步 | oracle | 22.29 / 0.1464 | 24.34 / 0.2017 | 29.09 | 2/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | 直接 | 22.10 / 0.1928 | 23.72 / 0.2215 | 29.03 | 1/3 |
| in035 | rife_w30 | GS 测试时优化 100 步 | oracle | 22.23 / 0.1448 | 24.46 / 0.1995 | 29.05 | 2/3 |
| in035 | rife_w40 | GS 前馈颜色 | 直接 | 21.37 / 0.2112 | 22.31 / 0.2748 | 28.96 | 0/3 |
| in035 | rife_w40 | GS 前馈颜色 | oracle | 21.52 / 0.1580 | 23.07 / 0.2416 | 29.19 | 2/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | 直接 | 21.55 / 0.1977 | 22.31 / 0.2683 | 29.04 | 0/3 |
| in035 | rife_w40 | GS 测试时优化 25 步 | oracle | 21.69 / 0.1551 | 23.09 / 0.2375 | 29.16 | 2/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | 直接 | 21.53 / 0.1948 | 22.15 / 0.2722 | 28.99 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 50 步 | oracle | 21.68 / 0.1537 | 23.04 / 0.2354 | 29.15 | 2/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | 直接 | 21.46 / 0.1927 | 21.97 / 0.2911 | 28.91 | 1/3 |
| in035 | rife_w40 | GS 测试时优化 100 步 | oracle | 21.66 / 0.1526 | 23.08 / 0.2430 | 29.13 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.82 / 0.2384 | 14.24 / 0.1294 | 29.18 / 0.0179 | 20.11 / 0.1763 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 2.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.82 | 0.6498 | 0.2384 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 19.43 | 0.7466 | 0.2570 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 20.42 | 0.7630 | 0.2138 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 19.70 | 0.7637 | 0.2399 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 20.09 | 0.7648 | 0.2266 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 19.41 | 0.7426 | 0.2667 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 20.40 | 0.7597 | 0.2215 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 19.68 | 0.7601 | 0.2483 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 20.07 | 0.7615 | 0.2339 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 12.31 | 0.5494 | 0.4550 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 12.13 | 0.5475 | 0.4487 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 11.67 | 0.5484 | 0.4661 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 11.84 | 0.5486 | 0.4579 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.43 | 0.7505 | 0.1892 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.96 | 0.7697 | 0.1588 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 25.77 | 0.7654 | 0.1692 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.76 | 0.7678 | 0.1628 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 24.34 | 0.7037 | 0.2194 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 24.46 | 0.7181 | 0.1995 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 24.36 | 0.7120 | 0.2067 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 24.34 | 0.7144 | 0.2017 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 23.07 | 0.6631 | 0.2416 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 23.08 | 0.6710 | 0.2430 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 23.09 | 0.6694 | 0.2375 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 23.04 | 0.6711 | 0.2354 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.61 | 0.7421 | 0.2267 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.78 | 0.7582 | 0.1899 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 24.85 | 0.7570 | 0.2036 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.65 | 0.7584 | 0.1981 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 23.83 | 0.6885 | 0.2437 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 23.72 | 0.7022 | 0.2215 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 23.78 | 0.6977 | 0.2290 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 23.65 | 0.6997 | 0.2270 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 22.31 | 0.6333 | 0.2748 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 21.97 | 0.6375 | 0.2911 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 22.31 | 0.6396 | 0.2683 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 22.15 | 0.6414 | 0.2722 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 23.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 14.24 | 0.3411 | 0.1294 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.02 | 0.5395 | 0.1069 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 14.19 | 0.5355 | 0.0996 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 14.16 | 0.5485 | 0.1036 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 14.16 | 0.5425 | 0.1018 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 11.89 | 0.5036 | 0.1443 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 11.93 | 0.4989 | 0.1379 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 11.91 | 0.5108 | 0.1420 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 11.90 | 0.5052 | 0.1404 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 8.06 | 0.4244 | 0.1978 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 8.05 | 0.4183 | 0.1927 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 8.03 | 0.4273 | 0.1962 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 8.03 | 0.4230 | 0.1948 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 16.83 | 0.5316 | 0.0840 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 17.01 | 0.5294 | 0.0790 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 17.09 | 0.5397 | 0.0802 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 17.06 | 0.5350 | 0.0793 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 16.52 | 0.4957 | 0.0897 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 16.67 | 0.4964 | 0.0853 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 16.74 | 0.5043 | 0.0867 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 16.72 | 0.5011 | 0.0857 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 15.84 | 0.4479 | 0.1010 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 15.98 | 0.4508 | 0.0967 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 16.01 | 0.4551 | 0.0980 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 16.01 | 0.4536 | 0.0970 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 16.83 | 0.5309 | 0.0838 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 17.01 | 0.5281 | 0.0791 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 17.09 | 0.5386 | 0.0801 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 17.06 | 0.5337 | 0.0794 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 16.52 | 0.4952 | 0.0898 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 16.67 | 0.4956 | 0.0854 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 16.74 | 0.5037 | 0.0866 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 16.72 | 0.5003 | 0.0857 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 15.84 | 0.4471 | 0.1011 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 15.98 | 0.4496 | 0.0970 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 16.01 | 0.4541 | 0.0981 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 16.01 | 0.4524 | 0.0972 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 101.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.04 | 0.6114 | 0.1836 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.39 | 0.6542 | 0.3455 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 14.81 | 0.6391 | 0.3026 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 14.46 | 0.6589 | 0.3202 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 14.56 | 0.6504 | 0.3114 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 11.50 | 0.5967 | 0.3779 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 11.69 | 0.5826 | 0.3431 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 11.48 | 0.6000 | 0.3570 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 11.53 | 0.5924 | 0.3502 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 7.79 | 0.5280 | 0.4226 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 7.78 | 0.5123 | 0.3943 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 7.71 | 0.5276 | 0.4049 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 7.72 | 0.5207 | 0.4002 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 22.19 | 0.6616 | 0.1615 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.34 | 0.6589 | 0.1522 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 22.41 | 0.6636 | 0.1570 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.38 | 0.6614 | 0.1540 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 21.93 | 0.6506 | 0.1601 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 22.06 | 0.6494 | 0.1535 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 22.13 | 0.6527 | 0.1569 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 22.11 | 0.6513 | 0.1548 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 21.39 | 0.6376 | 0.1650 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 21.52 | 0.6381 | 0.1604 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 21.55 | 0.6398 | 0.1628 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 21.54 | 0.6393 | 0.1613 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.05 | 0.6854 | 0.2560 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.09 | 0.6693 | 0.2266 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.31 | 0.6891 | 0.2342 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.21 | 0.6806 | 0.2283 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 21.77 | 0.6637 | 0.2285 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 21.82 | 0.6538 | 0.2078 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 21.99 | 0.6671 | 0.2110 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 21.92 | 0.6614 | 0.2079 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 21.19 | 0.6445 | 0.2194 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 21.28 | 0.6391 | 0.2017 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 21.35 | 0.6477 | 0.2057 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 21.33 | 0.6442 | 0.2030 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 68.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.47 | 0.5893 | 0.1682 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 16.00 | 0.6454 | 0.2538 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 16.05 | 0.6319 | 0.2247 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 16.04 | 0.6504 | 0.2389 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 16.02 | 0.6425 | 0.2305 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 12.62 | 0.5933 | 0.3001 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 12.60 | 0.5805 | 0.2771 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 12.56 | 0.5969 | 0.2890 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 12.56 | 0.5899 | 0.2822 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 8.38 | 0.5241 | 0.3608 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 8.27 | 0.5093 | 0.3404 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 8.25 | 0.5239 | 0.3513 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 8.25 | 0.5173 | 0.3455 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 21.67 | 0.6497 | 0.1384 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 21.87 | 0.6492 | 0.1311 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 21.94 | 0.6535 | 0.1349 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 21.92 | 0.6517 | 0.1329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 21.44 | 0.6376 | 0.1419 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 21.59 | 0.6376 | 0.1362 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 21.67 | 0.6412 | 0.1392 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 21.65 | 0.6399 | 0.1377 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 20.87 | 0.6220 | 0.1521 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 21.00 | 0.6236 | 0.1477 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 21.04 | 0.6255 | 0.1499 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 21.04 | 0.6249 | 0.1488 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.66 | 0.6772 | 0.1942 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.80 | 0.6649 | 0.1687 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 21.96 | 0.6820 | 0.1802 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 21.90 | 0.6747 | 0.1729 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 21.38 | 0.6536 | 0.1842 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 21.47 | 0.6457 | 0.1646 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 21.63 | 0.6581 | 0.1727 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 21.59 | 0.6529 | 0.1675 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 20.72 | 0.6315 | 0.1894 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 20.83 | 0.6270 | 0.1745 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 20.92 | 0.6354 | 0.1808 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 20.90 | 0.6319 | 0.1768 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 3.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.18 | 0.7446 | 0.0179 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 13.63 | 0.4669 | 0.1751 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 13.91 | 0.4886 | 0.1799 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 13.28 | 0.4559 | 0.1811 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 13.34 | 0.4683 | 0.1821 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 13.60 | 0.4659 | 0.1814 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 13.88 | 0.4860 | 0.1859 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 13.24 | 0.4541 | 0.1876 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 13.30 | 0.4661 | 0.1884 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 10.36 | 0.3855 | 0.1973 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 10.72 | 0.4044 | 0.2024 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 10.20 | 0.3771 | 0.2037 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 10.28 | 0.3895 | 0.2046 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.06 | 0.7385 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.79 | 0.7316 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 28.93 | 0.7334 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.01 | 0.7337 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 29.21 | 0.7442 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 29.05 | 0.7390 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 29.10 | 0.7400 | 0.0193 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 29.09 | 0.7402 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 29.19 | 0.7458 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 29.13 | 0.7413 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 29.16 | 0.7425 | 0.0185 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 29.15 | 0.7423 | 0.0185 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.41 | 0.7381 | 0.0223 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.42 | 0.7397 | 0.0194 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 28.49 | 0.7367 | 0.0202 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.68 | 0.7403 | 0.0190 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 28.98 | 0.7374 | 0.0214 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 29.03 | 0.7366 | 0.0192 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 29.08 | 0.7392 | 0.0192 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 29.12 | 0.7394 | 0.0188 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 28.96 | 0.7406 | 0.0198 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 28.91 | 0.7372 | 0.0188 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 29.04 | 0.7413 | 0.0186 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 28.99 | 0.7397 | 0.0186 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.11 | 0.6090 | 0.1763 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 16.30 | 0.6514 | 0.3072 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 16.34 | 0.6351 | 0.2689 | 1.00 |
| gs_tokrife448_nat_dil_al_tto25_local | 16.37 | 0.6554 | 0.2837 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 16.34 | 0.6468 | 0.2756 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_local | 12.22 | 0.5945 | 0.3432 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto100_local | 12.21 | 0.5791 | 0.3125 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto25_local | 12.17 | 0.5971 | 0.3241 | 1.00 |
| gs_tokrife_w30448_nat_dil_al_tto50_local | 12.17 | 0.5893 | 0.3182 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_local | 7.89 | 0.5228 | 0.3970 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto100_local | 7.82 | 0.5066 | 0.3716 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto25_local | 7.80 | 0.5220 | 0.3811 | 1.00 |
| gs_tokrife_w40448_nat_dil_al_tto50_local | 7.80 | 0.5151 | 0.3769 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 22.37 | 0.6631 | 0.1527 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.54 | 0.6608 | 0.1438 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto25_local] | 22.62 | 0.6655 | 0.1483 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.59 | 0.6635 | 0.1457 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_local] | 22.09 | 0.6509 | 0.1520 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto100_local] | 22.23 | 0.6499 | 0.1448 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto25_local] | 22.31 | 0.6534 | 0.1485 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w30448_nat_dil_al_tto50_local] | 22.29 | 0.6520 | 0.1464 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_local] | 21.52 | 0.6373 | 0.1580 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto100_local] | 21.66 | 0.6378 | 0.1526 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto25_local] | 21.69 | 0.6396 | 0.1551 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife_w40448_nat_dil_al_tto50_local] | 21.68 | 0.6390 | 0.1537 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.39 | 0.6918 | 0.2416 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.49 | 0.6767 | 0.2090 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto25_local] | 22.67 | 0.6955 | 0.2204 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.61 | 0.6875 | 0.2136 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_local] | 22.02 | 0.6676 | 0.2162 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto100_local] | 22.10 | 0.6580 | 0.1928 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto25_local] | 22.26 | 0.6711 | 0.1988 | 1.00 |
| hyb_token[gs_tokrife_w30448_nat_dil_al_tto50_local] | 22.22 | 0.6655 | 0.1954 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_local] | 21.37 | 0.6460 | 0.2112 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto100_local] | 21.46 | 0.6403 | 0.1927 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto25_local] | 21.55 | 0.6489 | 0.1977 | 1.00 |
| hyb_token[gs_tokrife_w40448_nat_dil_al_tto50_local] | 21.53 | 0.6453 | 0.1948 | 1.00 |

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
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 41.9 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 33.9 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 32.6 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 34.8 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife_w30448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 29.9 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 35.0 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 35.3 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife_w30448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 34.1 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife_w40448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 30.1 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 35.5 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto25_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 34.4 | 32.50 | 0.26 | 0.008 |
| in035 | gs_tokrife_w40448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 438552 | 0.324 | 33.4 | 32.50 | 0.26 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.597 | 0.150 |
| in035 | mask_ent | 0.707 | 0.150 |
| in035 | mask_grad | 0.416 | 0.150 |
| in035 | r_col | 0.482 | 0.150 |
| in035 | r_warp | 0.742 | 0.150 |

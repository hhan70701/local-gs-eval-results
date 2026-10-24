# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_center448_nat_dil_int_local | 103.1% | 22.76 / 0.0604 | 11.92 / 0.2779 | 11.92 / 0.2779 | 35.20 |
| cam3 | gs_center448_nat_dil_local | 108.5% | 22.79 / 0.0614 | 17.84 / 0.1648 | 19.45 / 0.1343 | 11.10 |
| cam3 | gs_token448_nat_dil_int_local | 101.1% | 22.69 / 0.0617 | 11.80 / 0.2852 | 11.80 / 0.2852 | 27.34 |
| cam3 | gs_token448_nat_dil_local | 105.7% | 22.71 / 0.0622 | 17.88 / 0.1658 | 19.97 / 0.1311 | 7.76 |
| cam5 | gs_center448_nat_dil_int_local | 81.1% | 28.16 / 0.0377 | 11.98 / 0.2693 | 11.98 / 0.2693 | 34.90 |
| cam5 | gs_center448_nat_dil_local | 82.9% | 28.09 / 0.0375 | 20.86 / 0.1112 | 21.53 / 0.1057 | 1.25 |
| cam5 | gs_token448_nat_dil_int_local | 79.3% | 28.10 / 0.0371 | 11.92 / 0.2691 | 11.92 / 0.2691 | 34.31 |
| cam5 | gs_token448_nat_dil_local | 79.3% | 28.07 / 0.0379 | 20.95 / 0.1071 | 21.98 / 0.0994 | 0.99 |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | flow_s0.5_pose | 22.93 / 0.0610 | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 |
| cam3 | hyb_token[gs_center448_nat_dil_int_local] | 12.08 / 0.3067 | 9.91 / 0.4248 | 9.27 / 0.1561 | 13.86 / 0.2590 |
| cam3 | hyb_token[gs_center448_nat_dil_local] | 18.39 / 0.1631 | 14.85 / 0.2432 | 13.63 / 0.1022 | 21.79 / 0.1301 |
| cam3 | hyb_token[gs_token448_nat_dil_int_local] | 12.04 / 0.3038 | 9.69 / 0.4220 | 9.21 / 0.1558 | 13.84 / 0.2578 |
| cam3 | hyb_token[gs_token448_nat_dil_local] | 18.38 / 0.1571 | 14.91 / 0.2218 | 13.58 / 0.1007 | 21.86 / 0.1300 |
| cam3 | hyb_token_ringreg[gs_center448_nat_dil_int_local] | 12.08 / 0.3067 | 9.91 / 0.4248 | 9.27 / 0.1561 | 13.86 / 0.2590 |
| cam3 | hyb_token_ringreg[gs_center448_nat_dil_local] | 20.10 / 0.1412 | 13.18 / 0.2870 | 14.04 / 0.0933 | 24.88 / 0.0943 |
| cam3 | hyb_token_ringreg[gs_token448_nat_dil_int_local] | 12.04 / 0.3038 | 9.69 / 0.4220 | 9.21 / 0.1558 | 13.84 / 0.2578 |
| cam3 | hyb_token_ringreg[gs_token448_nat_dil_local] | 20.54 / 0.1323 | 14.78 / 0.2245 | 14.60 / 0.0873 | 25.02 / 0.0935 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | flow_s0.5_pose | 27.45 / 0.0415 | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 |
| cam5 | hyb_token[gs_center448_nat_dil_int_local] | 12.98 / 0.2778 | 9.63 / 0.4915 | 9.95 / 0.0937 | 13.85 / 0.2589 |
| cam5 | hyb_token[gs_center448_nat_dil_local] | 21.42 / 0.1121 | 16.91 / 0.1791 | 16.04 / 0.0415 | 22.66 / 0.0940 |
| cam5 | hyb_token[gs_token448_nat_dil_int_local] | 13.00 / 0.2754 | 9.53 / 0.4789 | 9.94 / 0.0926 | 13.88 / 0.2571 |
| cam5 | hyb_token[gs_token448_nat_dil_local] | 21.30 / 0.1093 | 16.35 / 0.1790 | 14.31 / 0.0469 | 23.00 / 0.0967 |
| cam5 | hyb_token_ringreg[gs_center448_nat_dil_int_local] | 12.98 / 0.2778 | 9.63 / 0.4915 | 9.95 / 0.0937 | 13.85 / 0.2589 |
| cam5 | hyb_token_ringreg[gs_center448_nat_dil_local] | 21.90 / 0.1080 | 17.38 / 0.1745 | 16.54 / 0.0377 | 23.03 / 0.0892 |
| cam5 | hyb_token_ringreg[gs_token448_nat_dil_int_local] | 13.00 / 0.2754 | 9.53 / 0.4789 | 9.94 / 0.0926 | 13.88 / 0.2571 |
| cam5 | hyb_token_ringreg[gs_token448_nat_dil_local] | 22.19 / 0.1034 | 17.08 / 0.1699 | 15.06 / 0.0399 | 23.76 / 0.0878 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 cam3

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：vggt → `gs_token448_nat_dil`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=6.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 13.02 / 0.2906 | 12.52 / 0.0568 | 32.36 / 0.0269 | 22.18 / 0.0691 |
| flow_s1.0_pose | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 | 22.60 / 0.0629 |
| flow_s0.5_pose | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 | 22.93 / 0.0610 |
| gs_token448_nat_dil | 14.97 / 0.2210 | 13.38 / 0.1054 | 19.51 / 0.1558 | 17.43 / 0.1737 |
| gs_token448_nat_dil+reg | 17.77 / 0.1586 | 18.55 / 0.0443 | 29.54 / 0.0545 | 25.37 / 0.0967 |
| hyb_oracle_fail[gs_token448_nat_dil] | 16.28 / 0.2039 | 13.38 / 0.1054 | 33.30 / 0.0269 | 23.28 / 0.0923 |
| hyb_risktuned[gs_token448_nat_dil] | 14.89 / 0.2353 | 14.46 / 0.0673 | 33.53 / 0.0234 | 22.97 / 0.0773 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 18.47 / 0.1560 | 18.56 / 0.0441 | 33.54 / 0.0234 | 27.12 / 0.0569 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 16.70 / 0.1815 | 17.22 / 0.0434 | 33.54 / 0.0233 | 25.88 / 0.0597 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 16.10 | 0.5746 | 0.1984 | 1.00 |
| flow_s0.5_pose | 14.85 | 0.5040 | 0.2383 | 1.00 |
| flow_s0.5_uniform | 14.21 | 0.5001 | 0.2198 | 1.00 |
| flow_s1.0_oracle | 15.16 | 0.5837 | 0.2651 | 1.00 |
| flow_s1.0_pose | 14.53 | 0.5347 | 0.2724 | 1.00 |
| flow_s1.0_uniform | 13.02 | 0.4647 | 0.2906 | 1.00 |
| gs_center448_nat_dil | 14.89 | 0.4974 | 0.2413 | 1.00 |
| gs_center448_nat_dil+reg | 17.48 | 0.6404 | 0.1872 | 1.00 |
| gs_center448_nat_dil_int | 9.16 | 0.2550 | 0.4955 | 1.00 |
| gs_center448_nat_dil_int+reg | 17.21 | 0.6232 | 0.1894 | 1.00 |
| gs_center448_nat_dil_int_local | 8.98 | 0.2497 | 0.4879 | 1.00 |
| gs_center448_nat_dil_local | 14.81 | 0.4948 | 0.2432 | 1.00 |
| gs_token448_nat_dil | 14.97 | 0.4980 | 0.2210 | 1.00 |
| gs_token448_nat_dil+reg | 17.77 | 0.6675 | 0.1586 | 1.00 |
| gs_token448_nat_dil_int | 8.98 | 0.2494 | 0.4936 | 1.00 |
| gs_token448_nat_dil_int+reg | 17.75 | 0.6611 | 0.1606 | 1.00 |
| gs_token448_nat_dil_int_local | 8.79 | 0.2426 | 0.4851 | 1.00 |
| gs_token448_nat_dil_local | 14.90 | 0.4967 | 0.2219 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 18.22 | 0.6753 | 0.1709 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 16.08 | 0.5622 | 0.2081 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 18.05 | 0.6597 | 0.1743 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 10.95 | 0.3464 | 0.3873 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 18.47 | 0.6947 | 0.1560 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 16.28 | 0.5701 | 0.2039 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 18.57 | 0.6912 | 0.1595 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 10.79 | 0.3407 | 0.3872 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 16.54 | 0.6260 | 0.2052 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 14.60 | 0.4986 | 0.2496 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 16.38 | 0.6109 | 0.2069 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 9.13 | 0.2605 | 0.4926 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 16.76 | 0.6513 | 0.1792 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 14.70 | 0.4995 | 0.2305 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 16.77 | 0.6457 | 0.1807 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 8.96 | 0.2546 | 0.4920 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 16.51 | 0.6405 | 0.2021 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 14.79 | 0.5226 | 0.2471 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 16.33 | 0.6226 | 0.2055 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 9.78 | 0.3078 | 0.4429 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 16.70 | 0.6641 | 0.1815 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 14.89 | 0.5200 | 0.2353 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 16.66 | 0.6561 | 0.1854 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 9.62 | 0.3016 | 0.4419 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 9.91 | 0.3042 | 0.4248 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 14.85 | 0.4957 | 0.2432 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 9.69 | 0.2975 | 0.4220 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 14.91 | 0.4968 | 0.2218 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 9.91 | 0.3042 | 0.4248 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 13.18 | 0.4049 | 0.2870 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 9.69 | 0.2975 | 0.4220 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 14.78 | 0.4905 | 0.2245 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 14.17 | 0.5985 | 0.0457 | 1.00 |
| flow_s0.5_pose | 13.30 | 0.5443 | 0.0482 | 1.00 |
| flow_s0.5_uniform | 13.88 | 0.5654 | 0.0513 | 1.00 |
| flow_s1.0_oracle | 13.03 | 0.5914 | 0.0498 | 1.00 |
| flow_s1.0_pose | 12.70 | 0.5482 | 0.0513 | 1.00 |
| flow_s1.0_uniform | 12.52 | 0.5342 | 0.0568 | 1.00 |
| gs_center448_nat_dil | 13.47 | 0.4451 | 0.1054 | 1.00 |
| gs_center448_nat_dil+reg | 18.03 | 0.6933 | 0.0508 | 1.00 |
| gs_center448_nat_dil_int | 8.82 | 0.2058 | 0.1759 | 1.00 |
| gs_center448_nat_dil_int+reg | 17.94 | 0.6814 | 0.0517 | 0.99 |
| gs_center448_nat_dil_int_local | 8.77 | 0.2054 | 0.1759 | 1.00 |
| gs_center448_nat_dil_local | 13.47 | 0.4435 | 0.1056 | 1.00 |
| gs_token448_nat_dil | 13.38 | 0.4329 | 0.1054 | 1.00 |
| gs_token448_nat_dil+reg | 18.55 | 0.7255 | 0.0443 | 1.00 |
| gs_token448_nat_dil_int | 8.74 | 0.2055 | 0.1763 | 1.00 |
| gs_token448_nat_dil_int+reg | 18.67 | 0.7207 | 0.0443 | 0.99 |
| gs_token448_nat_dil_int_local | 8.70 | 0.2047 | 0.1763 | 1.00 |
| gs_token448_nat_dil_local | 13.38 | 0.4321 | 0.1056 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 18.04 | 0.6878 | 0.0508 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 13.47 | 0.4591 | 0.1054 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 17.96 | 0.6769 | 0.0511 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 8.82 | 0.2061 | 0.1759 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 18.56 | 0.7167 | 0.0441 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 13.38 | 0.4455 | 0.1054 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 18.68 | 0.7134 | 0.0439 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 8.74 | 0.2050 | 0.1763 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 17.27 | 0.6826 | 0.0517 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 13.57 | 0.4596 | 0.0988 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 17.20 | 0.6720 | 0.0516 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 9.02 | 0.2338 | 0.1654 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 17.68 | 0.7122 | 0.0458 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 13.46 | 0.4485 | 0.0993 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 17.76 | 0.7083 | 0.0454 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 8.94 | 0.2336 | 0.1658 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 16.92 | 0.6835 | 0.0460 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 14.40 | 0.5345 | 0.0692 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 16.81 | 0.6729 | 0.0463 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 10.06 | 0.3609 | 0.1115 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 17.22 | 0.7032 | 0.0434 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 14.46 | 0.5309 | 0.0673 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 17.22 | 0.6989 | 0.0431 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 9.97 | 0.3596 | 0.1117 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 9.27 | 0.2590 | 0.1561 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 13.63 | 0.4486 | 0.1022 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 9.21 | 0.2622 | 0.1558 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 13.58 | 0.4398 | 0.1007 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 9.27 | 0.2590 | 0.1561 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 14.04 | 0.4486 | 0.0933 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 9.21 | 0.2622 | 0.1558 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 14.60 | 0.4867 | 0.0873 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.99 | 0.8166 | 0.0498 | 1.00 |
| flow_s0.5_pose | 19.41 | 0.8102 | 0.0518 | 1.00 |
| flow_s0.5_uniform | 19.42 | 0.7885 | 0.0548 | 1.00 |
| flow_s1.0_oracle | 19.19 | 0.8296 | 0.0544 | 1.00 |
| flow_s1.0_pose | 18.94 | 0.8220 | 0.0548 | 1.00 |
| flow_s1.0_uniform | 18.45 | 0.7883 | 0.0601 | 1.00 |
| gs_center448_nat_dil | 14.79 | 0.5282 | 0.1717 | 1.00 |
| gs_center448_nat_dil+reg | 21.66 | 0.7864 | 0.0756 | 0.99 |
| gs_center448_nat_dil_int | 9.58 | 0.3636 | 0.3067 | 1.00 |
| gs_center448_nat_dil_int+reg | 21.63 | 0.7797 | 0.0774 | 0.99 |
| gs_center448_nat_dil_int_local | 9.49 | 0.3614 | 0.3076 | 1.00 |
| gs_center448_nat_dil_local | 14.73 | 0.5259 | 0.1732 | 1.00 |
| gs_token448_nat_dil | 14.85 | 0.5233 | 0.1694 | 1.00 |
| gs_token448_nat_dil+reg | 22.35 | 0.8137 | 0.0671 | 0.99 |
| gs_token448_nat_dil_int | 9.53 | 0.3619 | 0.3055 | 1.00 |
| gs_token448_nat_dil_int+reg | 22.39 | 0.8091 | 0.0686 | 0.99 |
| gs_token448_nat_dil_int_local | 9.45 | 0.3596 | 0.3065 | 1.00 |
| gs_token448_nat_dil_local | 14.80 | 0.5209 | 0.1705 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 23.06 | 0.8473 | 0.0542 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 19.63 | 0.7786 | 0.0801 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 22.99 | 0.8455 | 0.0539 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 15.28 | 0.6865 | 0.1293 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 23.41 | 0.8551 | 0.0511 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 19.55 | 0.7754 | 0.0811 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 23.47 | 0.8557 | 0.0507 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 15.20 | 0.6857 | 0.1297 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 21.70 | 0.7857 | 0.0757 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 14.79 | 0.5258 | 0.1717 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 21.67 | 0.7790 | 0.0768 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 9.58 | 0.3468 | 0.3067 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 22.38 | 0.8125 | 0.0670 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 14.85 | 0.5213 | 0.1694 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 22.42 | 0.8078 | 0.0687 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 9.53 | 0.3454 | 0.3055 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 22.52 | 0.8414 | 0.0505 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 18.59 | 0.7520 | 0.0719 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 22.42 | 0.8373 | 0.0509 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 13.68 | 0.6541 | 0.1240 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 22.92 | 0.8515 | 0.0481 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 18.83 | 0.7534 | 0.0692 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 22.90 | 0.8497 | 0.0484 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 13.61 | 0.6534 | 0.1235 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 10.22 | 0.4203 | 0.2657 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 14.93 | 0.5417 | 0.1615 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 10.18 | 0.4225 | 0.2629 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 15.02 | 0.5393 | 0.1576 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 10.22 | 0.4203 | 0.2657 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 15.95 | 0.5780 | 0.1363 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 10.18 | 0.4225 | 0.2629 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 16.70 | 0.6072 | 0.1266 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 21.88 | 0.8768 | 0.0597 | 1.00 |
| flow_s0.5_pose | 21.24 | 0.8722 | 0.0608 | 1.00 |
| flow_s0.5_uniform | 21.45 | 0.8596 | 0.0657 | 1.00 |
| flow_s1.0_oracle | 21.12 | 0.8872 | 0.0601 | 1.00 |
| flow_s1.0_pose | 20.84 | 0.8820 | 0.0609 | 1.00 |
| flow_s1.0_uniform | 20.48 | 0.8603 | 0.0677 | 1.00 |
| gs_center448_nat_dil | 17.35 | 0.6242 | 0.1950 | 1.00 |
| gs_center448_nat_dil+reg | 23.60 | 0.8461 | 0.0921 | 0.98 |
| gs_center448_nat_dil_int | 10.58 | 0.4474 | 0.3422 | 1.00 |
| gs_center448_nat_dil_int+reg | 23.55 | 0.8389 | 0.0929 | 0.97 |
| gs_center448_nat_dil_int_local | 10.40 | 0.4438 | 0.3442 | 1.00 |
| gs_center448_nat_dil_local | 17.27 | 0.6216 | 0.1969 | 1.00 |
| gs_token448_nat_dil | 17.29 | 0.6181 | 0.1947 | 1.00 |
| gs_token448_nat_dil+reg | 24.13 | 0.8632 | 0.0833 | 0.98 |
| gs_token448_nat_dil_int | 10.52 | 0.4435 | 0.3425 | 1.00 |
| gs_token448_nat_dil_int+reg | 24.19 | 0.8569 | 0.0832 | 0.97 |
| gs_token448_nat_dil_int_local | 10.34 | 0.4404 | 0.3443 | 1.00 |
| gs_token448_nat_dil_local | 17.19 | 0.6152 | 0.1968 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 25.37 | 0.8998 | 0.0578 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 21.90 | 0.8568 | 0.0857 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 25.29 | 0.8980 | 0.0576 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 17.31 | 0.8004 | 0.1303 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 25.73 | 0.9044 | 0.0546 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 21.86 | 0.8551 | 0.0870 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 25.83 | 0.9041 | 0.0538 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 17.22 | 0.7997 | 0.1306 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 23.65 | 0.8656 | 0.0774 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 18.41 | 0.7290 | 0.1402 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 23.62 | 0.8614 | 0.0773 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 12.56 | 0.6021 | 0.2401 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 24.06 | 0.8774 | 0.0721 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 18.35 | 0.7245 | 0.1409 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 24.13 | 0.8744 | 0.0714 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 12.50 | 0.6005 | 0.2403 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 24.15 | 0.8933 | 0.0592 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 21.06 | 0.8459 | 0.0789 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 24.03 | 0.8909 | 0.0592 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 16.06 | 0.7855 | 0.1240 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 24.43 | 0.8982 | 0.0576 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 21.19 | 0.8454 | 0.0778 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 24.43 | 0.8971 | 0.0568 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 15.97 | 0.7848 | 0.1242 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 11.45 | 0.5177 | 0.2882 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 17.75 | 0.6620 | 0.1696 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 11.41 | 0.5185 | 0.2862 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 17.75 | 0.6590 | 0.1679 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 11.45 | 0.5177 | 0.2882 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 18.99 | 0.7106 | 0.1430 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 11.41 | 0.5185 | 0.2862 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 19.54 | 0.7242 | 0.1384 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 32.45 | 0.9592 | 0.0262 | 1.00 |
| flow_s0.5_pose | 32.82 | 0.9610 | 0.0252 | 1.00 |
| flow_s0.5_uniform | 32.06 | 0.9533 | 0.0285 | 1.00 |
| flow_s1.0_oracle | 33.41 | 0.9610 | 0.0236 | 1.00 |
| flow_s1.0_pose | 33.53 | 0.9618 | 0.0233 | 1.00 |
| flow_s1.0_uniform | 32.36 | 0.9509 | 0.0269 | 1.00 |
| gs_center448_nat_dil | 19.54 | 0.7276 | 0.1577 | 1.00 |
| gs_center448_nat_dil+reg | 29.18 | 0.9214 | 0.0636 | 0.98 |
| gs_center448_nat_dil_int | 12.31 | 0.5760 | 0.3153 | 1.00 |
| gs_center448_nat_dil_int+reg | 29.12 | 0.9161 | 0.0636 | 0.97 |
| gs_center448_nat_dil_int_local | 12.06 | 0.5687 | 0.3214 | 1.00 |
| gs_center448_nat_dil_local | 19.33 | 0.7215 | 0.1663 | 1.00 |
| gs_token448_nat_dil | 19.51 | 0.7235 | 0.1558 | 1.00 |
| gs_token448_nat_dil+reg | 29.54 | 0.9307 | 0.0545 | 0.98 |
| gs_token448_nat_dil_int | 12.25 | 0.5719 | 0.3149 | 1.00 |
| gs_token448_nat_dil_int+reg | 29.39 | 0.9250 | 0.0550 | 0.97 |
| gs_token448_nat_dil_int_local | 11.98 | 0.5645 | 0.3217 | 1.00 |
| gs_token448_nat_dil_local | 19.26 | 0.7171 | 0.1654 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 33.54 | 0.9610 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 33.31 | 0.9591 | 0.0265 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 33.53 | 0.9610 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 32.42 | 0.9569 | 0.0316 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 33.54 | 0.9613 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 33.30 | 0.9591 | 0.0269 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 33.54 | 0.9613 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 32.38 | 0.9568 | 0.0318 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 33.47 | 0.9577 | 0.0241 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 31.87 | 0.9389 | 0.0478 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 33.47 | 0.9574 | 0.0242 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 27.62 | 0.9040 | 0.1162 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 33.50 | 0.9586 | 0.0238 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 31.95 | 0.9379 | 0.0501 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 33.49 | 0.9582 | 0.0240 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 27.59 | 0.9036 | 0.1169 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 33.52 | 0.9614 | 0.0234 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 33.39 | 0.9596 | 0.0248 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 33.40 | 0.9597 | 0.0247 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 13.86 | 0.6794 | 0.2590 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 21.79 | 0.8115 | 0.1301 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 13.84 | 0.6797 | 0.2578 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 21.86 | 0.8115 | 0.1300 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 13.86 | 0.6794 | 0.2590 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 24.88 | 0.8668 | 0.0943 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 13.84 | 0.6797 | 0.2578 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 25.02 | 0.8626 | 0.0935 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.53 | 0.9074 | 0.0593 | 1.00 |
| flow_s0.5_pose | 22.93 | 0.9061 | 0.0610 | 1.00 |
| flow_s0.5_uniform | 23.08 | 0.8944 | 0.0652 | 1.00 |
| flow_s1.0_oracle | 22.88 | 0.9145 | 0.0621 | 1.00 |
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| flow_s1.0_uniform | 22.18 | 0.8935 | 0.0691 | 1.00 |
| gs_center448_nat_dil | 17.49 | 0.6590 | 0.1820 | 1.00 |
| gs_center448_nat_dil+reg | 24.82 | 0.8737 | 0.1112 | 0.98 |
| gs_center448_nat_dil_int | 11.01 | 0.4948 | 0.3660 | 1.00 |
| gs_center448_nat_dil_int+reg | 24.73 | 0.8672 | 0.1108 | 0.97 |
| gs_center448_nat_dil_int_local | 10.85 | 0.4898 | 0.3718 | 1.00 |
| gs_center448_nat_dil_local | 17.39 | 0.6546 | 0.1908 | 1.00 |
| gs_token448_nat_dil | 17.43 | 0.6534 | 0.1737 | 1.00 |
| gs_token448_nat_dil+reg | 25.37 | 0.8892 | 0.0967 | 0.98 |
| gs_token448_nat_dil_int | 10.94 | 0.4913 | 0.3637 | 1.00 |
| gs_token448_nat_dil_int+reg | 25.34 | 0.8832 | 0.0960 | 0.97 |
| gs_token448_nat_dil_int_local | 10.78 | 0.4862 | 0.3700 | 1.00 |
| gs_token448_nat_dil_local | 17.32 | 0.6487 | 0.1835 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 26.75 | 0.9225 | 0.0608 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 23.30 | 0.8930 | 0.0919 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 26.67 | 0.9212 | 0.0605 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 19.01 | 0.8563 | 0.1425 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 27.12 | 0.9261 | 0.0569 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 23.28 | 0.8919 | 0.0923 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 27.18 | 0.9257 | 0.0562 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 18.93 | 0.8559 | 0.1428 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 25.01 | 0.8971 | 0.0834 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 19.58 | 0.7987 | 0.1405 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 24.97 | 0.8941 | 0.0829 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 13.93 | 0.7075 | 0.2552 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 25.46 | 0.9065 | 0.0766 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 19.51 | 0.7954 | 0.1399 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 25.48 | 0.9042 | 0.0758 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 13.87 | 0.7067 | 0.2549 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 25.59 | 0.9185 | 0.0610 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 22.84 | 0.8890 | 0.0785 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 25.48 | 0.9169 | 0.0607 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 17.94 | 0.8499 | 0.1266 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 25.88 | 0.9221 | 0.0597 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 22.97 | 0.8888 | 0.0773 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 25.85 | 0.9212 | 0.0590 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 17.86 | 0.8496 | 0.1266 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 12.08 | 0.5823 | 0.3067 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 18.39 | 0.7192 | 0.1631 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 12.04 | 0.5831 | 0.3038 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 18.38 | 0.7170 | 0.1571 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 12.08 | 0.5823 | 0.3067 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 20.10 | 0.7707 | 0.1412 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 12.04 | 0.5831 | 0.3038 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 20.54 | 0.7769 | 0.1323 | 1.00 |

## 设置 cam5

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：vggt → `gs_center448_nat_dil`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=3.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 16.39 / 0.1129 | 15.31 / 0.0249 | 30.29 / 0.0331 | 26.19 / 0.0440 |
| flow_s1.0_pose | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 | 28.00 / 0.0396 |
| flow_s0.5_pose | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 | 27.45 / 0.0415 |
| gs_center448_nat_dil | 16.91 / 0.1791 | 15.96 / 0.0420 | 24.29 / 0.0957 | 22.77 / 0.1127 |
| gs_center448_nat_dil+reg | 17.71 / 0.1768 | 17.09 / 0.0311 | 27.79 / 0.0751 | 25.52 / 0.0983 |
| hyb_oracle_fail[gs_center448_nat_dil] | 18.91 / 0.1475 | 15.96 / 0.0420 | 31.44 / 0.0309 | 27.30 / 0.0529 |
| hyb_risktuned[gs_center448_nat_dil] | 19.47 / 0.1187 | 17.70 / 0.0267 | 31.45 / 0.0305 | 27.44 / 0.0463 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 19.44 / 0.1415 | 17.09 / 0.0311 | 31.46 / 0.0305 | 27.97 / 0.0482 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 20.17 / 0.1144 | 18.17 / 0.0235 | 31.45 / 0.0305 | 27.87 / 0.0449 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 22.32 | 0.8406 | 0.0684 | 1.00 |
| flow_s0.5_pose | 19.65 | 0.7479 | 0.0818 | 1.00 |
| flow_s0.5_uniform | 16.71 | 0.6135 | 0.1070 | 1.00 |
| flow_s1.0_oracle | 23.16 | 0.8541 | 0.0592 | 1.00 |
| flow_s1.0_pose | 20.41 | 0.7569 | 0.0721 | 1.00 |
| flow_s1.0_uniform | 16.39 | 0.5779 | 0.1129 | 1.00 |
| gs_center448_nat_dil | 16.91 | 0.6107 | 0.1791 | 1.00 |
| gs_center448_nat_dil+reg | 17.71 | 0.6502 | 0.1768 | 1.00 |
| gs_center448_nat_dil_int | 9.53 | 0.2745 | 0.5031 | 1.00 |
| gs_center448_nat_dil_int+reg | 17.74 | 0.6527 | 0.1786 | 1.00 |
| gs_center448_nat_dil_int_local | 9.53 | 0.2745 | 0.5031 | 1.00 |
| gs_center448_nat_dil_local | 16.91 | 0.6106 | 0.1791 | 1.00 |
| gs_token448_nat_dil | 16.35 | 0.5692 | 0.1789 | 1.00 |
| gs_token448_nat_dil+reg | 18.86 | 0.7139 | 0.1367 | 1.00 |
| gs_token448_nat_dil_int | 9.40 | 0.2755 | 0.4953 | 1.00 |
| gs_token448_nat_dil_int+reg | 18.55 | 0.6939 | 0.1404 | 1.00 |
| gs_token448_nat_dil_int_local | 9.40 | 0.2755 | 0.4953 | 1.00 |
| gs_token448_nat_dil_local | 16.35 | 0.5692 | 0.1789 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 19.44 | 0.7179 | 0.1415 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 18.91 | 0.6892 | 0.1475 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 19.49 | 0.7208 | 0.1425 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 13.03 | 0.4665 | 0.3246 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 20.47 | 0.7599 | 0.1165 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 17.82 | 0.6598 | 0.1571 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 20.19 | 0.7505 | 0.1199 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 12.95 | 0.4662 | 0.3228 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 18.22 | 0.6800 | 0.1648 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 17.38 | 0.6375 | 0.1677 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 18.22 | 0.6808 | 0.1667 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 10.66 | 0.3385 | 0.4510 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 19.22 | 0.7318 | 0.1256 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 16.93 | 0.6156 | 0.1713 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 18.97 | 0.7163 | 0.1297 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 10.55 | 0.3372 | 0.4483 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 20.17 | 0.7498 | 0.1144 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 19.47 | 0.7116 | 0.1187 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 20.12 | 0.7481 | 0.1169 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 14.04 | 0.5256 | 0.3104 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 20.70 | 0.7772 | 0.0928 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 19.41 | 0.7204 | 0.1102 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 20.56 | 0.7686 | 0.0941 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 14.04 | 0.5242 | 0.3094 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 9.63 | 0.2830 | 0.4915 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 16.91 | 0.6107 | 0.1791 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 9.53 | 0.2883 | 0.4789 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 16.35 | 0.5693 | 0.1790 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 9.63 | 0.2830 | 0.4915 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 17.38 | 0.6336 | 0.1745 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 9.53 | 0.2883 | 0.4789 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 17.08 | 0.6089 | 0.1699 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.18 | 0.7600 | 0.0171 | 1.00 |
| flow_s0.5_pose | 17.06 | 0.6711 | 0.0195 | 1.00 |
| flow_s0.5_uniform | 15.30 | 0.5755 | 0.0247 | 1.00 |
| flow_s1.0_oracle | 19.73 | 0.7659 | 0.0154 | 1.00 |
| flow_s1.0_pose | 17.62 | 0.6745 | 0.0175 | 1.00 |
| flow_s1.0_uniform | 15.31 | 0.5619 | 0.0249 | 1.00 |
| gs_center448_nat_dil | 15.96 | 0.5625 | 0.0420 | 1.00 |
| gs_center448_nat_dil+reg | 17.09 | 0.6487 | 0.0311 | 1.00 |
| gs_center448_nat_dil_int | 9.31 | 0.1699 | 0.1111 | 1.00 |
| gs_center448_nat_dil_int+reg | 17.16 | 0.6517 | 0.0312 | 1.00 |
| gs_center448_nat_dil_int_local | 9.30 | 0.1696 | 0.1113 | 1.00 |
| gs_center448_nat_dil_local | 15.91 | 0.5616 | 0.0432 | 1.00 |
| gs_token448_nat_dil | 14.21 | 0.4861 | 0.0475 | 1.00 |
| gs_token448_nat_dil+reg | 18.04 | 0.6960 | 0.0280 | 1.00 |
| gs_token448_nat_dil_int | 9.25 | 0.1754 | 0.1116 | 1.00 |
| gs_token448_nat_dil_int+reg | 17.83 | 0.6831 | 0.0282 | 1.00 |
| gs_token448_nat_dil_int_local | 9.25 | 0.1753 | 0.1118 | 1.00 |
| gs_token448_nat_dil_local | 14.18 | 0.4858 | 0.0487 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 17.09 | 0.6486 | 0.0311 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 15.96 | 0.5788 | 0.0420 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 17.16 | 0.6512 | 0.0306 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 9.31 | 0.1865 | 0.1111 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 18.04 | 0.6940 | 0.0280 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 14.21 | 0.4827 | 0.0475 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 17.83 | 0.6830 | 0.0278 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 9.25 | 0.1894 | 0.1116 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 17.38 | 0.6652 | 0.0293 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 16.51 | 0.6053 | 0.0363 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 17.43 | 0.6663 | 0.0291 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 10.37 | 0.2891 | 0.0891 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 18.28 | 0.7067 | 0.0264 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 14.78 | 0.5370 | 0.0420 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 18.07 | 0.6950 | 0.0266 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 10.32 | 0.2937 | 0.0894 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 18.17 | 0.7016 | 0.0235 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 17.70 | 0.6643 | 0.0267 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 18.19 | 0.7005 | 0.0234 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 12.64 | 0.4680 | 0.0542 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 18.82 | 0.7278 | 0.0211 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 16.31 | 0.6219 | 0.0283 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 18.67 | 0.7190 | 0.0215 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 12.59 | 0.4697 | 0.0542 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 9.95 | 0.2340 | 0.0937 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 16.04 | 0.5711 | 0.0415 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 9.94 | 0.2455 | 0.0926 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 14.31 | 0.4920 | 0.0469 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 9.95 | 0.2340 | 0.0937 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 16.54 | 0.6024 | 0.0377 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 9.94 | 0.2455 | 0.0926 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 15.06 | 0.5440 | 0.0399 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 17.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.73 | 0.8826 | 0.0204 | 1.00 |
| flow_s0.5_pose | 22.21 | 0.8504 | 0.0224 | 1.00 |
| flow_s0.5_uniform | 20.55 | 0.8064 | 0.0266 | 1.00 |
| flow_s1.0_oracle | 24.76 | 0.8987 | 0.0188 | 1.00 |
| flow_s1.0_pose | 23.17 | 0.8669 | 0.0208 | 1.00 |
| flow_s1.0_uniform | 20.86 | 0.8093 | 0.0253 | 1.00 |
| gs_center448_nat_dil | 18.75 | 0.6696 | 0.0632 | 1.00 |
| gs_center448_nat_dil+reg | 20.85 | 0.7697 | 0.0471 | 1.00 |
| gs_center448_nat_dil_int | 9.77 | 0.3450 | 0.2071 | 1.00 |
| gs_center448_nat_dil_int+reg | 20.87 | 0.7692 | 0.0470 | 0.99 |
| gs_center448_nat_dil_int_local | 9.74 | 0.3446 | 0.2077 | 1.00 |
| gs_center448_nat_dil_local | 18.73 | 0.6684 | 0.0632 | 1.00 |
| gs_token448_nat_dil | 18.14 | 0.6445 | 0.0644 | 1.00 |
| gs_token448_nat_dil+reg | 21.60 | 0.7948 | 0.0407 | 1.00 |
| gs_token448_nat_dil_int | 9.67 | 0.3392 | 0.2077 | 1.00 |
| gs_token448_nat_dil_int+reg | 21.45 | 0.7883 | 0.0411 | 0.99 |
| gs_token448_nat_dil_int_local | 9.64 | 0.3392 | 0.2082 | 1.00 |
| gs_token448_nat_dil_local | 18.14 | 0.6431 | 0.0642 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 23.07 | 0.8551 | 0.0282 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 22.25 | 0.8351 | 0.0316 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 23.10 | 0.8563 | 0.0280 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 16.51 | 0.7125 | 0.0686 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 23.81 | 0.8677 | 0.0255 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 20.84 | 0.8094 | 0.0343 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 23.65 | 0.8656 | 0.0257 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 16.46 | 0.7123 | 0.0686 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 20.86 | 0.7694 | 0.0471 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 18.75 | 0.6701 | 0.0632 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 20.91 | 0.7705 | 0.0468 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 9.77 | 0.3251 | 0.2071 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 21.60 | 0.7942 | 0.0407 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 18.14 | 0.6448 | 0.0644 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 21.49 | 0.7900 | 0.0408 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 9.67 | 0.3191 | 0.2077 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 22.94 | 0.8513 | 0.0283 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 22.00 | 0.8230 | 0.0304 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 22.98 | 0.8512 | 0.0283 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 14.92 | 0.6777 | 0.0691 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 23.43 | 0.8627 | 0.0252 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 21.18 | 0.8122 | 0.0286 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 23.30 | 0.8588 | 0.0254 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 14.89 | 0.6775 | 0.0686 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 10.56 | 0.4206 | 0.1710 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 18.74 | 0.6707 | 0.0624 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 10.50 | 0.4209 | 0.1692 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 18.20 | 0.6463 | 0.0628 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 10.56 | 0.4206 | 0.1710 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 19.34 | 0.7003 | 0.0571 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 10.50 | 0.4209 | 0.1692 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 19.21 | 0.6917 | 0.0543 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 25.73 | 0.9248 | 0.0355 | 1.00 |
| flow_s0.5_pose | 24.65 | 0.9099 | 0.0374 | 1.00 |
| flow_s0.5_uniform | 23.02 | 0.8845 | 0.0430 | 1.00 |
| flow_s1.0_oracle | 26.44 | 0.9323 | 0.0341 | 1.00 |
| flow_s1.0_pose | 25.29 | 0.9172 | 0.0359 | 1.00 |
| flow_s1.0_uniform | 23.35 | 0.8857 | 0.0419 | 1.00 |
| gs_center448_nat_dil | 21.37 | 0.7512 | 0.0885 | 1.00 |
| gs_center448_nat_dil+reg | 23.27 | 0.8444 | 0.0639 | 0.99 |
| gs_center448_nat_dil_int | 10.92 | 0.4309 | 0.2787 | 1.00 |
| gs_center448_nat_dil_int+reg | 23.33 | 0.8461 | 0.0623 | 0.98 |
| gs_center448_nat_dil_int_local | 10.08 | 0.4175 | 0.2938 | 1.00 |
| gs_center448_nat_dil_local | 17.65 | 0.7331 | 0.1166 | 1.00 |
| gs_token448_nat_dil | 20.43 | 0.7555 | 0.0890 | 1.00 |
| gs_token448_nat_dil+reg | 23.92 | 0.8625 | 0.0574 | 1.00 |
| gs_token448_nat_dil_int | 10.83 | 0.4282 | 0.2801 | 1.00 |
| gs_token448_nat_dil_int+reg | 23.86 | 0.8584 | 0.0573 | 0.98 |
| gs_token448_nat_dil_int_local | 10.07 | 0.4164 | 0.2942 | 1.00 |
| gs_token448_nat_dil_local | 17.18 | 0.7326 | 0.1196 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 25.40 | 0.9123 | 0.0420 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 24.71 | 0.9009 | 0.0456 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 25.43 | 0.9128 | 0.0412 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 19.22 | 0.8396 | 0.0766 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 25.99 | 0.9180 | 0.0399 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 23.40 | 0.8900 | 0.0481 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 25.93 | 0.9176 | 0.0397 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 19.18 | 0.8396 | 0.0769 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 24.02 | 0.8847 | 0.0508 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 22.62 | 0.8481 | 0.0595 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 24.05 | 0.8849 | 0.0501 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 14.00 | 0.6758 | 0.1431 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 24.54 | 0.8925 | 0.0478 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 21.63 | 0.8363 | 0.0637 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 24.49 | 0.8909 | 0.0475 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 13.93 | 0.6747 | 0.1437 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 25.14 | 0.9121 | 0.0403 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 24.54 | 0.8999 | 0.0424 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 25.13 | 0.9116 | 0.0402 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 17.85 | 0.8296 | 0.0734 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 25.51 | 0.9156 | 0.0383 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 23.75 | 0.8937 | 0.0429 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 25.45 | 0.9143 | 0.0388 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 17.83 | 0.8301 | 0.0733 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 11.68 | 0.5232 | 0.2242 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 20.48 | 0.7728 | 0.0888 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 11.71 | 0.5278 | 0.2216 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 19.92 | 0.7700 | 0.0890 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 11.68 | 0.5232 | 0.2242 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 20.99 | 0.7947 | 0.0835 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 11.71 | 0.5278 | 0.2216 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 20.78 | 0.8005 | 0.0821 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 31.41 | 0.9667 | 0.0317 | 1.00 |
| flow_s0.5_pose | 31.22 | 0.9653 | 0.0318 | 1.00 |
| flow_s0.5_uniform | 30.53 | 0.9607 | 0.0346 | 1.00 |
| flow_s1.0_oracle | 31.56 | 0.9661 | 0.0302 | 1.00 |
| flow_s1.0_pose | 31.46 | 0.9649 | 0.0305 | 1.00 |
| flow_s1.0_uniform | 30.29 | 0.9592 | 0.0331 | 1.00 |
| gs_center448_nat_dil | 24.29 | 0.8234 | 0.0957 | 1.00 |
| gs_center448_nat_dil+reg | 27.79 | 0.9137 | 0.0751 | 0.99 |
| gs_center448_nat_dil_int | 12.17 | 0.5481 | 0.3408 | 1.00 |
| gs_center448_nat_dil_int+reg | 27.92 | 0.9155 | 0.0752 | 0.98 |
| gs_center448_nat_dil_int_local | 10.49 | 0.5208 | 0.3663 | 1.00 |
| gs_center448_nat_dil_local | 16.35 | 0.7760 | 0.1547 | 1.00 |
| gs_token448_nat_dil | 25.03 | 0.8658 | 0.0955 | 1.00 |
| gs_token448_nat_dil+reg | 28.29 | 0.9265 | 0.0654 | 1.00 |
| gs_token448_nat_dil_int | 12.06 | 0.5456 | 0.3400 | 1.00 |
| gs_token448_nat_dil_int+reg | 28.26 | 0.9227 | 0.0667 | 0.98 |
| gs_token448_nat_dil_int_local | 10.45 | 0.5203 | 0.3661 | 1.00 |
| gs_token448_nat_dil_local | 15.98 | 0.8088 | 0.1590 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 31.46 | 0.9640 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 31.44 | 0.9632 | 0.0309 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 31.46 | 0.9640 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 30.72 | 0.9582 | 0.0384 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 31.46 | 0.9642 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 31.42 | 0.9629 | 0.0318 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 31.46 | 0.9642 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 30.71 | 0.9582 | 0.0385 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 31.38 | 0.9619 | 0.0314 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 31.28 | 0.9592 | 0.0333 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 31.37 | 0.9620 | 0.0314 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 28.15 | 0.9329 | 0.0841 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 31.40 | 0.9624 | 0.0313 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 31.31 | 0.9582 | 0.0353 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 31.39 | 0.9624 | 0.0313 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 28.13 | 0.9326 | 0.0847 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 31.38 | 0.9634 | 0.0324 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 31.46 | 0.9648 | 0.0305 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 31.38 | 0.9634 | 0.0324 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 13.85 | 0.6941 | 0.2589 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 22.66 | 0.8767 | 0.0940 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 13.88 | 0.6966 | 0.2571 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 23.00 | 0.8856 | 0.0967 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 13.85 | 0.6941 | 0.2589 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 23.03 | 0.8884 | 0.0892 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 13.88 | 0.6966 | 0.2571 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 23.76 | 0.8999 | 0.0878 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 28.40 | 0.9528 | 0.0403 | 1.00 |
| flow_s0.5_pose | 27.45 | 0.9461 | 0.0415 | 1.00 |
| flow_s0.5_uniform | 26.08 | 0.9340 | 0.0467 | 1.00 |
| flow_s1.0_oracle | 28.96 | 0.9545 | 0.0383 | 1.00 |
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| flow_s1.0_uniform | 26.19 | 0.9330 | 0.0440 | 1.00 |
| gs_center448_nat_dil | 22.77 | 0.7982 | 0.1127 | 1.00 |
| gs_center448_nat_dil+reg | 25.52 | 0.8899 | 0.0983 | 0.99 |
| gs_center448_nat_dil_int | 11.59 | 0.5098 | 0.3645 | 1.00 |
| gs_center448_nat_dil_int+reg | 25.58 | 0.8909 | 0.0979 | 0.98 |
| gs_center448_nat_dil_int_local | 10.28 | 0.4863 | 0.3900 | 1.00 |
| gs_center448_nat_dil_local | 16.53 | 0.7577 | 0.1712 | 1.00 |
| gs_token448_nat_dil | 22.64 | 0.8288 | 0.1077 | 1.00 |
| gs_token448_nat_dil+reg | 26.14 | 0.9043 | 0.0859 | 1.00 |
| gs_token448_nat_dil_int | 11.49 | 0.5070 | 0.3629 | 1.00 |
| gs_token448_nat_dil_int+reg | 26.05 | 0.9000 | 0.0862 | 0.98 |
| gs_token448_nat_dil_int_local | 10.24 | 0.4853 | 0.3891 | 1.00 |
| gs_token448_nat_dil_local | 16.10 | 0.7802 | 0.1710 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 27.97 | 0.9449 | 0.0482 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 27.30 | 0.9393 | 0.0529 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int+reg] | 27.96 | 0.9451 | 0.0476 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_int] | 22.29 | 0.9107 | 0.0946 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 28.45 | 0.9473 | 0.0459 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 26.48 | 0.9350 | 0.0546 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int+reg] | 28.37 | 0.9472 | 0.0456 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_int] | 22.25 | 0.9108 | 0.0947 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 26.80 | 0.9311 | 0.0588 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 25.59 | 0.9138 | 0.0663 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int+reg] | 26.79 | 0.9311 | 0.0581 | 1.00 |
| hyb_risk[gs_center448_nat_dil_int] | 17.35 | 0.8346 | 0.1647 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 27.29 | 0.9349 | 0.0551 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 24.89 | 0.9081 | 0.0696 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int+reg] | 27.22 | 0.9344 | 0.0545 | 1.00 |
| hyb_risk[gs_token448_nat_dil_int] | 17.26 | 0.8336 | 0.1653 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 27.87 | 0.9459 | 0.0449 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 27.44 | 0.9412 | 0.0463 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int+reg] | 27.84 | 0.9457 | 0.0449 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_int] | 21.67 | 0.9152 | 0.0784 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 28.17 | 0.9474 | 0.0427 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 26.91 | 0.9386 | 0.0464 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int+reg] | 28.11 | 0.9469 | 0.0430 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_int] | 21.65 | 0.9153 | 0.0780 | 1.00 |
| hyb_token[gs_center448_nat_dil_int_local] | 12.98 | 0.6454 | 0.2778 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 21.42 | 0.8428 | 0.1121 | 1.00 |
| hyb_token[gs_token448_nat_dil_int_local] | 13.00 | 0.6478 | 0.2754 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 21.30 | 0.8450 | 0.1093 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_int_local] | 12.98 | 0.6454 | 0.2778 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 21.90 | 0.8585 | 0.1080 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_int_local] | 13.00 | 0.6478 | 0.2754 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 22.19 | 0.8664 | 0.1034 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|
| cam3 | gs_center448_nat_dil | 10.60 | 1.00 |
| cam3 | gs_center448_nat_dil_int | 38.58 | 1.00 |
| cam3 | gs_token448_nat_dil | 9.92 | 1.00 |
| cam3 | gs_token448_nat_dil_int | 38.75 | 1.00 |
| cam5 | gs_center448_nat_dil | 3.30 | 1.00 |
| cam5 | gs_center448_nat_dil_int | 39.95 | 1.00 |
| cam5 | gs_token448_nat_dil | 2.64 | 1.00 |
| cam5 | gs_token448_nat_dil_int | 39.98 | 1.00 |

## 风险阈值扫描（风险区 vs oracle_fail，按 IoU 排序，前 8 名与配置默认值）

| 设置 | warp 阈值 | col 阈值 | 精确率 | 召回率 | IoU | 面积比 |
|---|---:|---:|---:|---:|---:|---:|
| cam3 | 0.20 | 6.0 | 0.444 | 0.710 | 0.377 | 1.66 |
| cam3 | 0.25 | 6.0 | 0.478 | 0.628 | 0.373 | 1.34 |
| cam3 | 0.20 | 不用 | 0.456 | 0.681 | 0.373 | 1.55 |
| cam3 | 0.20 | 4.0 | 0.418 | 0.732 | 0.365 | 1.82 |
| cam3 | 0.25 | 4.0 | 0.440 | 0.664 | 0.364 | 1.55 |
| cam3 | 0.25 | 不用 | 0.499 | 0.592 | 0.364 | 1.22 |
| cam3 | 0.30 | 6.0 | 0.500 | 0.564 | 0.361 | 1.15 |
| cam3 | 0.30 | 4.0 | 0.452 | 0.609 | 0.356 | 1.37 |
| cam3 | 0.08（默认） | 2.0 | 0.225 | 0.941 | 0.221 | 4.88 |
| cam5 | 0.20 | 3.0 | 0.308 | 0.516 | 0.237 | 1.71 |
| cam5 | 0.15 | 3.0 | 0.287 | 0.577 | 0.236 | 2.07 |
| cam5 | 0.12 | 3.0 | 0.271 | 0.659 | 0.235 | 2.57 |
| cam5 | 0.20 | 2.0 | 0.282 | 0.581 | 0.235 | 2.07 |
| cam5 | 0.12 | 不用 | 0.299 | 0.576 | 0.235 | 2.06 |
| cam5 | 0.15 | 2.0 | 0.268 | 0.632 | 0.232 | 2.40 |
| cam5 | 0.25 | 2.0 | 0.285 | 0.544 | 0.231 | 1.90 |
| cam5 | 0.25 | 3.0 | 0.312 | 0.471 | 0.230 | 1.51 |
| cam5 | 0.08（默认） | 2.0 | 0.188 | 0.823 | 0.181 | 4.78 |

## t 估计对比（scale=1.0）

| 设置 | 目标相机 | t_uniform | t_pose (VGGT) | t_posecal (标定) | t_oracle |
|---|---:|---:|---:|---:|---:|
| cam3 | 1 | 0.250 | 0.305 | — | 0.320 |
| cam3 | 2 | 0.500 | 0.551 | — | 0.550 |
| cam3 | 3 | 0.750 | 0.802 | — | 0.760 |
| cam3 | 5 | 0.250 | 0.194 | — | 0.220 |
| cam3 | 6 | 0.500 | 0.463 | — | 0.470 |
| cam3 | 7 | 0.750 | 0.742 | — | 0.740 |
| cam5 | 1 | 0.500 | 0.554 | — | 0.560 |
| cam5 | 3 | 0.500 | 0.559 | — | 0.550 |
| cam5 | 5 | 0.500 | 0.419 | — | 0.450 |
| cam5 | 7 | 0.500 | 0.522 | — | 0.530 |

## AnySplat 运行统计

旋转/光心误差：vggt 行是联合估计与输入视点估计的一致性；calib/calibK 行是标定位姿经 Sim(3) 对齐到AnySplat 输入视点位姿后的残差（反映 AnySplat 自身预测的输入相机几何与真实阵列的偏差）。

| 设置 | 变体 | 位姿来源 | 窗口边长 | 渲染分辨率 | 模式 | eps2d | 3D 滤波 | 高斯数 | 编码 s | 渲染 ms/视点 | 输入视点自渲染 PSNR | 最大旋转误差° | 最大光心误差/基线 |
|---|---|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|
| cam3 | gs_center448_nat_dil | vggt | 1080 | 1080 | classic | 1.74 | False | 432937 | 0.337 | 15.1 | 29.19 | 0.34 | 0.011 |
| cam3 | gs_center448_nat_dil_int | interp | 1080 | 1080 | classic | 1.74 | False | 432937 | 0.337 | 15.2 | 29.19 | 0.34 | 0.011 |
| cam3 | gs_center448_nat_dil_int_local | interp | 1080 | 1080 | classic | 1.74 | False | 432937 | 0.337 | 11.9 | 29.19 | 0.34 | 0.011 |
| cam3 | gs_center448_nat_dil_local | vggt | 1080 | 1080 | classic | 1.74 | False | 432937 | 0.337 | 18.4 | 29.19 | 0.34 | 0.011 |
| cam3 | gs_token448_nat_dil | vggt | 911 | 911 | classic | 1.24 | False | 368915 | 0.810 | 8.2 | 29.04 | 0.34 | 0.010 |
| cam3 | gs_token448_nat_dil_int | interp | 911 | 911 | classic | 1.24 | False | 368915 | 0.810 | 8.7 | 29.04 | 0.34 | 0.010 |
| cam3 | gs_token448_nat_dil_int_local | interp | 911 | 911 | classic | 1.24 | False | 368915 | 0.810 | 10.6 | 29.04 | 0.34 | 0.010 |
| cam3 | gs_token448_nat_dil_local | vggt | 911 | 911 | classic | 1.24 | False | 368915 | 0.810 | 14.0 | 29.04 | 0.34 | 0.010 |
| cam5 | gs_center448_nat_dil | vggt | 1080 | 1080 | classic | 1.74 | False | 639886 | 0.494 | 18.5 | 29.76 | 0.13 | 0.007 |
| cam5 | gs_center448_nat_dil_int | interp | 1080 | 1080 | classic | 1.74 | False | 639886 | 0.494 | 28.4 | 29.76 | 0.13 | 0.007 |
| cam5 | gs_center448_nat_dil_int_local | interp | 1080 | 1080 | classic | 1.74 | False | 639886 | 0.494 | 14.6 | 29.76 | 0.13 | 0.007 |
| cam5 | gs_center448_nat_dil_local | vggt | 1080 | 1080 | classic | 1.74 | False | 639886 | 0.494 | 11.2 | 29.76 | 0.13 | 0.007 |
| cam5 | gs_token448_nat_dil | vggt | 917 | 917 | classic | 1.26 | False | 527784 | 0.522 | 6.5 | 29.36 | 0.13 | 0.008 |
| cam5 | gs_token448_nat_dil_int | interp | 917 | 917 | classic | 1.26 | False | 527784 | 0.522 | 5.4 | 29.36 | 0.13 | 0.008 |
| cam5 | gs_token448_nat_dil_int_local | interp | 917 | 917 | classic | 1.26 | False | 527784 | 0.522 | 4.9 | 29.36 | 0.13 | 0.008 |
| cam5 | gs_token448_nat_dil_local | vggt | 917 | 917 | classic | 1.26 | False | 527784 | 0.522 | 5.2 | 29.36 | 0.13 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| cam3 | g_disp | 0.735 | 0.054 |
| cam3 | mask_ent | 0.523 | 0.054 |
| cam3 | mask_grad | 0.263 | 0.054 |
| cam3 | r_col | 0.885 | 0.054 |
| cam3 | r_warp | 0.921 | 0.054 |
| cam5 | g_disp | 0.750 | 0.018 |
| cam5 | mask_ent | 0.505 | 0.018 |
| cam5 | mask_grad | 0.279 | 0.018 |
| cam5 | r_col | 0.921 | 0.018 |
| cam5 | r_warp | 0.909 | 0.018 |

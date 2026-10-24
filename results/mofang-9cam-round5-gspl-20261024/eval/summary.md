# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_center448_nat_dil_al_local | 51.3% | 20.24 / 0.0584 | 22.09 / 0.1002 | 22.09 / 0.1002 | 0.00 |
| cam3 | gs_center448_nat_dil_alv_local | 51.3% | 20.24 / 0.0584 | 22.07 / 0.0997 | 22.07 / 0.0997 | 0.00 |
| cam3 | gs_center448_nat_dil_local | 53.4% | 20.36 / 0.0576 | 15.22 / 0.1949 | 18.88 / 0.1350 | 7.98 |
| cam3 | gs_token448_nat_dil_al_local | 50.6% | 20.20 / 0.0585 | 22.78 / 0.0894 | 22.78 / 0.0894 | 0.00 |
| cam3 | gs_token448_nat_dil_alv_local | 50.6% | 20.21 / 0.0585 | 22.68 / 0.0890 | 22.68 / 0.0890 | 0.00 |
| cam3 | gs_token448_nat_dil_local | 52.3% | 20.44 / 0.0571 | 15.56 / 0.1848 | 18.69 / 0.1346 | 5.91 |
| cam5 | gs_center448_nat_dil_al_local | 38.9% | 25.64 / 0.0297 | 22.15 / 0.0783 | 21.57 / 0.0804 | 0.81 |
| cam5 | gs_center448_nat_dil_alv_local | 39.0% | 25.64 / 0.0295 | 22.18 / 0.0779 | 21.55 / 0.0808 | 0.83 |
| cam5 | gs_center448_nat_dil_local | 39.5% | 25.56 / 0.0297 | 20.41 / 0.0979 | 20.31 / 0.0929 | 2.55 |
| cam5 | gs_token448_nat_dil_al_local | 38.6% | 25.63 / 0.0295 | 21.86 / 0.0780 | 21.85 / 0.0757 | 0.34 |
| cam5 | gs_token448_nat_dil_alv_local | 38.6% | 25.64 / 0.0294 | 21.60 / 0.0784 | 22.10 / 0.0718 | 1.14 |
| cam5 | gs_token448_nat_dil_local | 38.4% | 25.69 / 0.0294 | 20.18 / 0.0946 | 21.01 / 0.0821 | 1.76 |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | flow_s0.5_pose | 22.93 / 0.0610 | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 |
| cam3 | hyb_token[gs_center448_nat_dil_al_local] | 24.63 / 0.0912 | 16.49 / 0.2117 | 17.29 / 0.0540 | 30.75 / 0.0418 |
| cam3 | hyb_token[gs_center448_nat_dil_alv_local] | 24.55 / 0.0913 | 16.38 / 0.2153 | 17.17 / 0.0541 | 30.75 / 0.0418 |
| cam3 | hyb_token[gs_center448_nat_dil_local] | 18.69 / 0.1486 | 14.19 / 0.2680 | 13.42 / 0.1035 | 23.31 / 0.1093 |
| cam3 | hyb_token[gs_token448_nat_dil_al_local] | 25.27 / 0.0824 | 16.99 / 0.1768 | 17.92 / 0.0481 | 31.17 / 0.0384 |
| cam3 | hyb_token[gs_token448_nat_dil_alv_local] | 25.13 / 0.0823 | 16.65 / 0.1816 | 17.70 / 0.0480 | 31.20 / 0.0381 |
| cam3 | hyb_token[gs_token448_nat_dil_local] | 18.91 / 0.1410 | 14.58 / 0.2343 | 13.59 / 0.0994 | 23.79 / 0.1081 |
| cam3 | hyb_token_ringreg[gs_center448_nat_dil_al_local] | 24.63 / 0.0912 | 16.49 / 0.2117 | 17.29 / 0.0540 | 30.75 / 0.0418 |
| cam3 | hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 24.55 / 0.0913 | 16.38 / 0.2153 | 17.17 / 0.0541 | 30.75 / 0.0418 |
| cam3 | hyb_token_ringreg[gs_center448_nat_dil_local] | 22.17 / 0.1184 | 14.49 / 0.2582 | 15.34 / 0.0790 | 28.05 / 0.0672 |
| cam3 | hyb_token_ringreg[gs_token448_nat_dil_al_local] | 25.27 / 0.0824 | 16.99 / 0.1768 | 17.92 / 0.0481 | 31.17 / 0.0384 |
| cam3 | hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 25.13 / 0.0823 | 16.65 / 0.1816 | 17.70 / 0.0480 | 31.20 / 0.0381 |
| cam3 | hyb_token_ringreg[gs_token448_nat_dil_local] | 21.76 / 0.1160 | 14.09 / 0.2396 | 14.69 / 0.0788 | 28.59 / 0.0712 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | flow_s0.5_pose | 27.45 / 0.0415 | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 |
| cam5 | hyb_token[gs_center448_nat_dil_al_local] | 25.49 / 0.0791 | 17.55 / 0.1887 | 16.87 / 0.0327 | 28.30 / 0.0568 |
| cam5 | hyb_token[gs_center448_nat_dil_alv_local] | 25.55 / 0.0786 | 17.56 / 0.1838 | 16.99 / 0.0324 | 28.36 / 0.0562 |
| cam5 | hyb_token[gs_center448_nat_dil_local] | 24.31 / 0.0891 | 16.74 / 0.1923 | 16.25 / 0.0401 | 26.98 / 0.0692 |
| cam5 | hyb_token[gs_token448_nat_dil_al_local] | 25.12 / 0.0773 | 18.15 / 0.1558 | 16.41 / 0.0338 | 27.97 / 0.0598 |
| cam5 | hyb_token[gs_token448_nat_dil_alv_local] | 24.89 / 0.0777 | 17.55 / 0.1584 | 15.94 / 0.0350 | 27.89 / 0.0598 |
| cam5 | hyb_token[gs_token448_nat_dil_local] | 23.61 / 0.0879 | 16.24 / 0.1900 | 14.50 / 0.0451 | 26.99 / 0.0742 |
| cam5 | hyb_token_ringreg[gs_center448_nat_dil_al_local] | 25.11 / 0.0817 | 16.93 / 0.1961 | 16.55 / 0.0361 | 27.93 / 0.0591 |
| cam5 | hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 25.12 / 0.0816 | 16.96 / 0.1905 | 16.67 / 0.0359 | 27.91 / 0.0590 |
| cam5 | hyb_token_ringreg[gs_center448_nat_dil_local] | 24.32 / 0.0898 | 15.81 / 0.2150 | 15.63 / 0.0431 | 27.31 / 0.0648 |
| cam5 | hyb_token_ringreg[gs_token448_nat_dil_al_local] | 25.18 / 0.0769 | 17.79 / 0.1589 | 16.58 / 0.0335 | 27.87 / 0.0594 |
| cam5 | hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 25.46 / 0.0760 | 17.81 / 0.1575 | 17.11 / 0.0319 | 28.07 / 0.0570 |
| cam5 | hyb_token_ringreg[gs_token448_nat_dil_local] | 24.55 / 0.0837 | 16.54 / 0.1906 | 15.82 / 0.0386 | 27.52 / 0.0665 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 cam3

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：vggt → `gs_token448_nat_dil_al`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=6.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 13.02 / 0.2906 | 12.52 / 0.0568 | 32.36 / 0.0269 | 22.18 / 0.0691 |
| flow_s1.0_pose | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 | 22.60 / 0.0629 |
| flow_s0.5_pose | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 | 22.93 / 0.0610 |
| gs_token448_nat_dil_al | 18.31 / 0.1439 | 18.32 / 0.0461 | 29.09 / 0.0547 | 24.98 / 0.0942 |
| gs_token448_nat_dil_al+reg | 18.31 / 0.1480 | 18.74 / 0.0441 | 29.47 / 0.0521 | 25.39 / 0.0932 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 19.09 / 0.1447 | 18.32 / 0.0461 | 33.53 / 0.0235 | 27.03 / 0.0568 |
| hyb_risktuned[gs_token448_nat_dil_al] | 17.07 / 0.1723 | 17.23 / 0.0429 | 33.54 / 0.0233 | 25.86 / 0.0584 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 19.05 / 0.1481 | 18.74 / 0.0441 | 33.54 / 0.0234 | 27.21 / 0.0561 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 17.06 / 0.1764 | 17.34 / 0.0430 | 33.54 / 0.0233 | 25.93 / 0.0587 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 16.10 | 0.5746 | 0.1984 | 1.00 |
| flow_s0.5_pose | 14.85 | 0.5040 | 0.2383 | 1.00 |
| flow_s0.5_uniform | 14.21 | 0.5001 | 0.2198 | 1.00 |
| flow_s1.0_oracle | 15.16 | 0.5837 | 0.2651 | 1.00 |
| flow_s1.0_pose | 14.53 | 0.5347 | 0.2724 | 1.00 |
| flow_s1.0_uniform | 13.02 | 0.4647 | 0.2906 | 1.00 |
| gs_center448_nat_dil | 14.87 | 0.4943 | 0.2501 | 1.00 |
| gs_center448_nat_dil+reg | 17.57 | 0.6435 | 0.1900 | 1.00 |
| gs_center448_nat_dil_al | 17.82 | 0.6562 | 0.1855 | 1.00 |
| gs_center448_nat_dil_al+reg | 17.57 | 0.6454 | 0.1896 | 1.00 |
| gs_center448_nat_dil_al_local | 17.15 | 0.6359 | 0.2009 | 1.00 |
| gs_center448_nat_dil_alv | 17.62 | 0.6433 | 0.1881 | 1.00 |
| gs_center448_nat_dil_alv+reg | 17.74 | 0.6539 | 0.1877 | 1.00 |
| gs_center448_nat_dil_alv_local | 17.00 | 0.6221 | 0.2047 | 1.00 |
| gs_center448_nat_dil_local | 14.33 | 0.4749 | 0.2634 | 1.00 |
| gs_token448_nat_dil | 15.03 | 0.5006 | 0.2174 | 1.00 |
| gs_token448_nat_dil+reg | 17.96 | 0.6754 | 0.1500 | 1.00 |
| gs_token448_nat_dil_al | 18.31 | 0.6845 | 0.1439 | 1.00 |
| gs_token448_nat_dil_al+reg | 18.31 | 0.6841 | 0.1480 | 1.00 |
| gs_token448_nat_dil_al_local | 17.74 | 0.6657 | 0.1650 | 1.00 |
| gs_token448_nat_dil_alv | 17.75 | 0.6687 | 0.1473 | 1.00 |
| gs_token448_nat_dil_alv+reg | 18.14 | 0.6866 | 0.1476 | 1.00 |
| gs_token448_nat_dil_alv_local | 17.25 | 0.6498 | 0.1705 | 1.00 |
| gs_token448_nat_dil_local | 14.68 | 0.4866 | 0.2338 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 18.31 | 0.6769 | 0.1752 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 16.06 | 0.5599 | 0.2141 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 18.40 | 0.6768 | 0.1743 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 18.64 | 0.6884 | 0.1702 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 18.52 | 0.6860 | 0.1704 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 18.41 | 0.6835 | 0.1703 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 18.65 | 0.7014 | 0.1496 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 16.34 | 0.5737 | 0.2016 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 19.05 | 0.7113 | 0.1481 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 19.09 | 0.7130 | 0.1447 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 18.85 | 0.7088 | 0.1454 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 18.53 | 0.6980 | 0.1464 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 16.65 | 0.6295 | 0.2064 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 14.60 | 0.4956 | 0.2572 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 16.67 | 0.6317 | 0.2058 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 16.89 | 0.6419 | 0.2019 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 16.82 | 0.6398 | 0.2042 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 16.69 | 0.6288 | 0.2045 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 16.90 | 0.6581 | 0.1709 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 14.75 | 0.5021 | 0.2271 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 17.22 | 0.6659 | 0.1691 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 17.24 | 0.6669 | 0.1648 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 17.17 | 0.6693 | 0.1686 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 16.80 | 0.6521 | 0.1684 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 16.63 | 0.6435 | 0.2021 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 14.82 | 0.5202 | 0.2536 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 16.61 | 0.6420 | 0.2036 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 16.82 | 0.6514 | 0.1989 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 16.80 | 0.6526 | 0.2001 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 16.72 | 0.6469 | 0.2007 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 16.81 | 0.6708 | 0.1740 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 14.95 | 0.5237 | 0.2321 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 17.06 | 0.6776 | 0.1764 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 17.07 | 0.6747 | 0.1723 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 17.09 | 0.6789 | 0.1719 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 16.83 | 0.6670 | 0.1732 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 16.49 | 0.6271 | 0.2117 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 16.38 | 0.6147 | 0.2153 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 14.19 | 0.4767 | 0.2680 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 16.99 | 0.6545 | 0.1768 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 16.65 | 0.6418 | 0.1816 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 14.58 | 0.4929 | 0.2343 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 16.49 | 0.6271 | 0.2117 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 16.38 | 0.6147 | 0.2153 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 14.49 | 0.5062 | 0.2582 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 16.99 | 0.6545 | 0.1768 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 16.65 | 0.6418 | 0.1816 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 14.09 | 0.4703 | 0.2396 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 14.17 | 0.5985 | 0.0457 | 1.00 |
| flow_s0.5_pose | 13.30 | 0.5443 | 0.0482 | 1.00 |
| flow_s0.5_uniform | 13.88 | 0.5654 | 0.0513 | 1.00 |
| flow_s1.0_oracle | 13.03 | 0.5914 | 0.0498 | 1.00 |
| flow_s1.0_pose | 12.70 | 0.5482 | 0.0513 | 1.00 |
| flow_s1.0_uniform | 12.52 | 0.5342 | 0.0568 | 1.00 |
| gs_center448_nat_dil | 13.40 | 0.4376 | 0.1070 | 1.00 |
| gs_center448_nat_dil+reg | 18.11 | 0.6960 | 0.0513 | 1.00 |
| gs_center448_nat_dil_al | 17.70 | 0.6838 | 0.0525 | 1.00 |
| gs_center448_nat_dil_al+reg | 18.23 | 0.6944 | 0.0504 | 1.00 |
| gs_center448_nat_dil_al_local | 17.79 | 0.6677 | 0.0549 | 1.00 |
| gs_center448_nat_dil_alv | 17.52 | 0.6809 | 0.0527 | 1.00 |
| gs_center448_nat_dil_alv+reg | 18.28 | 0.6998 | 0.0494 | 1.00 |
| gs_center448_nat_dil_alv_local | 17.66 | 0.6654 | 0.0551 | 1.00 |
| gs_center448_nat_dil_local | 13.40 | 0.4228 | 0.1083 | 1.00 |
| gs_token448_nat_dil | 13.43 | 0.4339 | 0.1042 | 1.00 |
| gs_token448_nat_dil+reg | 18.59 | 0.7273 | 0.0441 | 1.00 |
| gs_token448_nat_dil_al | 18.32 | 0.7166 | 0.0461 | 1.00 |
| gs_token448_nat_dil_al+reg | 18.74 | 0.7289 | 0.0441 | 1.00 |
| gs_token448_nat_dil_al_local | 18.51 | 0.6966 | 0.0491 | 1.00 |
| gs_token448_nat_dil_alv | 18.02 | 0.7086 | 0.0461 | 1.00 |
| gs_token448_nat_dil_alv+reg | 18.73 | 0.7279 | 0.0433 | 1.00 |
| gs_token448_nat_dil_alv_local | 18.25 | 0.6900 | 0.0490 | 1.00 |
| gs_token448_nat_dil_local | 13.55 | 0.4194 | 0.1052 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 18.11 | 0.6898 | 0.0512 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 13.40 | 0.4507 | 0.1070 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 18.23 | 0.6889 | 0.0504 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 17.70 | 0.6760 | 0.0525 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 18.28 | 0.6942 | 0.0494 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 17.52 | 0.6729 | 0.0527 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 18.59 | 0.7184 | 0.0441 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 13.43 | 0.4453 | 0.1042 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 18.74 | 0.7206 | 0.0441 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 18.32 | 0.7064 | 0.0461 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 18.73 | 0.7198 | 0.0433 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 18.02 | 0.6982 | 0.0461 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 17.35 | 0.6852 | 0.0518 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 13.49 | 0.4520 | 0.1004 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 17.44 | 0.6834 | 0.0512 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 17.05 | 0.6745 | 0.0526 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 17.48 | 0.6884 | 0.0505 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 16.91 | 0.6715 | 0.0529 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 17.71 | 0.7136 | 0.0458 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 13.50 | 0.4498 | 0.0982 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 17.84 | 0.7147 | 0.0459 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 17.54 | 0.7053 | 0.0471 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 17.83 | 0.7138 | 0.0453 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 17.29 | 0.6978 | 0.0472 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 17.00 | 0.6857 | 0.0459 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 14.33 | 0.5293 | 0.0700 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 17.05 | 0.6839 | 0.0458 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 16.78 | 0.6767 | 0.0469 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 17.10 | 0.6894 | 0.0453 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 16.70 | 0.6757 | 0.0469 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 17.24 | 0.7050 | 0.0432 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 14.48 | 0.5323 | 0.0668 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 17.34 | 0.7065 | 0.0430 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 17.23 | 0.7007 | 0.0429 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 17.35 | 0.7058 | 0.0425 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 17.05 | 0.6950 | 0.0428 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 17.29 | 0.6687 | 0.0540 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 17.17 | 0.6662 | 0.0541 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 13.42 | 0.4335 | 0.1035 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 17.92 | 0.6994 | 0.0481 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 17.70 | 0.6928 | 0.0480 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 13.59 | 0.4374 | 0.0994 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 17.29 | 0.6687 | 0.0540 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 17.17 | 0.6662 | 0.0541 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 15.34 | 0.5412 | 0.0790 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 17.92 | 0.6994 | 0.0481 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 17.70 | 0.6928 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 14.69 | 0.4979 | 0.0788 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.99 | 0.8166 | 0.0498 | 1.00 |
| flow_s0.5_pose | 19.41 | 0.8102 | 0.0518 | 1.00 |
| flow_s0.5_uniform | 19.42 | 0.7885 | 0.0548 | 1.00 |
| flow_s1.0_oracle | 19.19 | 0.8296 | 0.0544 | 1.00 |
| flow_s1.0_pose | 18.94 | 0.8220 | 0.0548 | 1.00 |
| flow_s1.0_uniform | 18.45 | 0.7883 | 0.0601 | 1.00 |
| gs_center448_nat_dil | 14.74 | 0.5249 | 0.1722 | 1.00 |
| gs_center448_nat_dil+reg | 21.70 | 0.7861 | 0.0762 | 0.99 |
| gs_center448_nat_dil_al | 21.37 | 0.7765 | 0.0764 | 1.00 |
| gs_center448_nat_dil_al+reg | 21.72 | 0.7858 | 0.0749 | 1.00 |
| gs_center448_nat_dil_al_local | 16.40 | 0.7330 | 0.1163 | 1.00 |
| gs_center448_nat_dil_alv | 21.29 | 0.7759 | 0.0763 | 1.00 |
| gs_center448_nat_dil_alv+reg | 21.79 | 0.7886 | 0.0746 | 1.00 |
| gs_center448_nat_dil_alv_local | 16.36 | 0.7325 | 0.1157 | 1.00 |
| gs_center448_nat_dil_local | 13.55 | 0.5002 | 0.1961 | 1.00 |
| gs_token448_nat_dil | 15.01 | 0.5271 | 0.1660 | 1.00 |
| gs_token448_nat_dil+reg | 22.34 | 0.8132 | 0.0666 | 0.99 |
| gs_token448_nat_dil_al | 22.05 | 0.8024 | 0.0667 | 1.00 |
| gs_token448_nat_dil_al+reg | 22.30 | 0.8109 | 0.0662 | 1.00 |
| gs_token448_nat_dil_al_local | 16.44 | 0.7540 | 0.1096 | 1.00 |
| gs_token448_nat_dil_alv | 21.89 | 0.8017 | 0.0665 | 1.00 |
| gs_token448_nat_dil_alv+reg | 22.32 | 0.8125 | 0.0657 | 1.00 |
| gs_token448_nat_dil_alv_local | 16.38 | 0.7541 | 0.1086 | 1.00 |
| gs_token448_nat_dil_local | 13.57 | 0.5007 | 0.1920 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 23.12 | 0.8477 | 0.0543 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 19.56 | 0.7756 | 0.0808 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 23.18 | 0.8476 | 0.0534 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 22.89 | 0.8441 | 0.0548 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 23.21 | 0.8491 | 0.0530 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 22.78 | 0.8438 | 0.0546 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 23.43 | 0.8550 | 0.0509 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 19.59 | 0.7759 | 0.0806 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 23.51 | 0.8558 | 0.0508 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 23.36 | 0.8537 | 0.0515 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 23.48 | 0.8552 | 0.0504 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 23.14 | 0.8514 | 0.0515 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 21.73 | 0.7853 | 0.0762 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 14.74 | 0.5225 | 0.1722 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 21.73 | 0.7838 | 0.0749 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 21.37 | 0.7742 | 0.0764 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 21.79 | 0.7864 | 0.0746 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 21.29 | 0.7736 | 0.0763 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 22.36 | 0.8116 | 0.0667 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 15.01 | 0.5253 | 0.1660 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 22.30 | 0.8085 | 0.0662 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 22.05 | 0.8001 | 0.0667 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 22.32 | 0.8102 | 0.0657 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 21.89 | 0.7993 | 0.0665 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 22.59 | 0.8417 | 0.0506 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 18.55 | 0.7497 | 0.0725 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 22.56 | 0.8402 | 0.0505 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 22.38 | 0.8375 | 0.0505 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 22.64 | 0.8426 | 0.0501 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 22.34 | 0.8377 | 0.0503 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 22.94 | 0.8515 | 0.0476 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 18.91 | 0.7547 | 0.0682 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 22.94 | 0.8511 | 0.0475 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 22.89 | 0.8499 | 0.0470 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 22.96 | 0.8511 | 0.0471 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 22.76 | 0.8488 | 0.0468 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 20.87 | 0.7597 | 0.0870 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 20.84 | 0.7591 | 0.0868 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 14.81 | 0.5352 | 0.1659 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 21.58 | 0.7838 | 0.0789 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 21.47 | 0.7834 | 0.0784 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 15.11 | 0.5408 | 0.1585 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 20.87 | 0.7597 | 0.0870 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 20.84 | 0.7591 | 0.0868 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 17.85 | 0.6498 | 0.1222 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 21.58 | 0.7838 | 0.0789 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 21.47 | 0.7834 | 0.0784 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 17.68 | 0.6441 | 0.1205 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 21.88 | 0.8768 | 0.0597 | 1.00 |
| flow_s0.5_pose | 21.24 | 0.8722 | 0.0608 | 1.00 |
| flow_s0.5_uniform | 21.45 | 0.8596 | 0.0657 | 1.00 |
| flow_s1.0_oracle | 21.12 | 0.8872 | 0.0601 | 1.00 |
| flow_s1.0_pose | 20.84 | 0.8820 | 0.0609 | 1.00 |
| flow_s1.0_uniform | 20.48 | 0.8603 | 0.0677 | 1.00 |
| gs_center448_nat_dil | 17.27 | 0.6217 | 0.1964 | 1.00 |
| gs_center448_nat_dil+reg | 23.61 | 0.8457 | 0.0923 | 0.98 |
| gs_center448_nat_dil_al | 23.26 | 0.8394 | 0.0919 | 1.00 |
| gs_center448_nat_dil_al+reg | 23.74 | 0.8459 | 0.0896 | 1.00 |
| gs_center448_nat_dil_al_local | 22.82 | 0.8252 | 0.1023 | 1.00 |
| gs_center448_nat_dil_alv | 23.16 | 0.8390 | 0.0919 | 1.00 |
| gs_center448_nat_dil_alv+reg | 23.80 | 0.8476 | 0.0886 | 1.00 |
| gs_center448_nat_dil_alv_local | 22.74 | 0.8247 | 0.1023 | 1.00 |
| gs_center448_nat_dil_local | 17.22 | 0.6134 | 0.2016 | 1.00 |
| gs_token448_nat_dil | 17.42 | 0.6217 | 0.1926 | 1.00 |
| gs_token448_nat_dil+reg | 24.14 | 0.8630 | 0.0828 | 0.99 |
| gs_token448_nat_dil_al | 23.85 | 0.8580 | 0.0838 | 1.00 |
| gs_token448_nat_dil_al+reg | 24.21 | 0.8639 | 0.0807 | 1.00 |
| gs_token448_nat_dil_al_local | 23.39 | 0.8416 | 0.0950 | 1.00 |
| gs_token448_nat_dil_alv | 23.68 | 0.8574 | 0.0834 | 1.00 |
| gs_token448_nat_dil_alv+reg | 24.25 | 0.8650 | 0.0799 | 1.00 |
| gs_token448_nat_dil_alv_local | 23.24 | 0.8414 | 0.0944 | 1.00 |
| gs_token448_nat_dil_local | 17.38 | 0.6132 | 0.1977 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 25.38 | 0.9000 | 0.0581 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 21.79 | 0.8547 | 0.0867 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 25.48 | 0.8999 | 0.0572 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 25.07 | 0.8974 | 0.0587 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 25.52 | 0.9008 | 0.0566 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 24.98 | 0.8973 | 0.0588 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 25.74 | 0.9045 | 0.0544 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 21.91 | 0.8554 | 0.0866 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 25.84 | 0.9050 | 0.0538 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 25.67 | 0.9036 | 0.0548 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 25.85 | 0.9046 | 0.0534 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 25.47 | 0.9022 | 0.0549 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 23.68 | 0.8653 | 0.0778 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 18.33 | 0.7264 | 0.1412 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 23.74 | 0.8652 | 0.0765 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 23.29 | 0.8582 | 0.0784 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 23.78 | 0.8663 | 0.0760 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 23.19 | 0.8575 | 0.0787 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 24.06 | 0.8771 | 0.0719 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 18.44 | 0.7263 | 0.1400 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 24.05 | 0.8763 | 0.0709 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 23.80 | 0.8714 | 0.0724 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 24.08 | 0.8769 | 0.0706 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 23.63 | 0.8703 | 0.0725 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 24.19 | 0.8934 | 0.0594 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 21.00 | 0.8444 | 0.0793 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 24.22 | 0.8931 | 0.0589 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 23.95 | 0.8909 | 0.0598 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 24.27 | 0.8942 | 0.0587 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 23.89 | 0.8907 | 0.0600 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 24.44 | 0.8983 | 0.0573 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 21.23 | 0.8459 | 0.0775 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 24.50 | 0.8985 | 0.0566 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 24.42 | 0.8975 | 0.0565 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 24.52 | 0.8981 | 0.0564 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 24.27 | 0.8962 | 0.0565 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 23.46 | 0.8465 | 0.0840 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 23.37 | 0.8457 | 0.0842 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 17.87 | 0.6782 | 0.1570 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 24.10 | 0.8625 | 0.0771 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 23.94 | 0.8615 | 0.0771 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 18.11 | 0.6817 | 0.1532 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 23.46 | 0.8465 | 0.0840 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 23.37 | 0.8457 | 0.0842 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 21.01 | 0.7683 | 0.1165 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 24.10 | 0.8625 | 0.0771 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 23.94 | 0.8615 | 0.0771 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 20.69 | 0.7642 | 0.1161 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 32.45 | 0.9592 | 0.0262 | 1.00 |
| flow_s0.5_pose | 32.82 | 0.9610 | 0.0252 | 1.00 |
| flow_s0.5_uniform | 32.06 | 0.9533 | 0.0285 | 1.00 |
| flow_s1.0_oracle | 33.41 | 0.9610 | 0.0236 | 1.00 |
| flow_s1.0_pose | 33.53 | 0.9618 | 0.0233 | 1.00 |
| flow_s1.0_uniform | 32.36 | 0.9509 | 0.0269 | 1.00 |
| gs_center448_nat_dil | 19.58 | 0.7284 | 0.1574 | 1.00 |
| gs_center448_nat_dil+reg | 29.15 | 0.9215 | 0.0637 | 0.98 |
| gs_center448_nat_dil_al | 28.90 | 0.9194 | 0.0610 | 1.00 |
| gs_center448_nat_dil_al+reg | 29.19 | 0.9205 | 0.0589 | 1.00 |
| gs_center448_nat_dil_al_local | 24.30 | 0.9032 | 0.0811 | 1.00 |
| gs_center448_nat_dil_alv | 28.96 | 0.9204 | 0.0609 | 1.00 |
| gs_center448_nat_dil_alv+reg | 29.30 | 0.9213 | 0.0585 | 1.00 |
| gs_center448_nat_dil_alv_local | 24.34 | 0.9043 | 0.0808 | 1.00 |
| gs_center448_nat_dil_local | 18.90 | 0.7179 | 0.1694 | 1.00 |
| gs_token448_nat_dil | 19.77 | 0.7272 | 0.1527 | 1.00 |
| gs_token448_nat_dil+reg | 29.51 | 0.9305 | 0.0542 | 0.98 |
| gs_token448_nat_dil_al | 29.09 | 0.9269 | 0.0547 | 1.00 |
| gs_token448_nat_dil_al+reg | 29.47 | 0.9296 | 0.0521 | 1.00 |
| gs_token448_nat_dil_al_local | 24.36 | 0.9093 | 0.0756 | 1.00 |
| gs_token448_nat_dil_alv | 29.22 | 0.9288 | 0.0543 | 1.00 |
| gs_token448_nat_dil_alv+reg | 29.57 | 0.9312 | 0.0515 | 1.00 |
| gs_token448_nat_dil_alv_local | 24.42 | 0.9115 | 0.0749 | 1.00 |
| gs_token448_nat_dil_local | 19.00 | 0.7166 | 0.1651 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 33.53 | 0.9610 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 33.32 | 0.9591 | 0.0266 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 33.54 | 0.9611 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 33.53 | 0.9609 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 33.54 | 0.9611 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 33.53 | 0.9609 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 33.54 | 0.9613 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 33.31 | 0.9591 | 0.0269 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 33.54 | 0.9614 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 33.53 | 0.9612 | 0.0235 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 33.54 | 0.9614 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 33.53 | 0.9612 | 0.0235 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 33.46 | 0.9576 | 0.0241 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 31.89 | 0.9388 | 0.0482 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 33.46 | 0.9578 | 0.0240 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 33.44 | 0.9572 | 0.0247 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 33.46 | 0.9578 | 0.0240 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 33.44 | 0.9572 | 0.0246 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 33.50 | 0.9586 | 0.0238 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 32.03 | 0.9384 | 0.0495 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 33.48 | 0.9585 | 0.0239 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 33.46 | 0.9581 | 0.0242 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 33.48 | 0.9586 | 0.0238 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 33.46 | 0.9582 | 0.0242 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 30.75 | 0.9411 | 0.0418 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 30.75 | 0.9412 | 0.0418 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 23.31 | 0.8541 | 0.1093 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 31.17 | 0.9467 | 0.0384 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 31.20 | 0.9470 | 0.0381 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 23.79 | 0.8586 | 0.1081 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 30.75 | 0.9411 | 0.0418 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 30.75 | 0.9412 | 0.0418 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 28.05 | 0.9064 | 0.0672 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 31.17 | 0.9467 | 0.0384 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 31.20 | 0.9470 | 0.0381 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 28.59 | 0.9077 | 0.0712 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.53 | 0.9074 | 0.0593 | 1.00 |
| flow_s0.5_pose | 22.93 | 0.9061 | 0.0610 | 1.00 |
| flow_s0.5_uniform | 23.08 | 0.8944 | 0.0652 | 1.00 |
| flow_s1.0_oracle | 22.88 | 0.9145 | 0.0621 | 1.00 |
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| flow_s1.0_uniform | 22.18 | 0.8935 | 0.0691 | 1.00 |
| gs_center448_nat_dil | 17.46 | 0.6580 | 0.1823 | 1.00 |
| gs_center448_nat_dil+reg | 24.84 | 0.8735 | 0.1110 | 0.98 |
| gs_center448_nat_dil_al | 24.45 | 0.8686 | 0.1052 | 1.00 |
| gs_center448_nat_dil_al+reg | 24.92 | 0.8734 | 0.1056 | 1.00 |
| gs_center448_nat_dil_al_local | 22.90 | 0.8549 | 0.1276 | 1.00 |
| gs_center448_nat_dil_alv | 24.37 | 0.8688 | 0.1053 | 1.00 |
| gs_center448_nat_dil_alv+reg | 24.98 | 0.8747 | 0.1051 | 1.00 |
| gs_center448_nat_dil_alv_local | 22.87 | 0.8552 | 0.1277 | 1.00 |
| gs_center448_nat_dil_local | 17.18 | 0.6488 | 0.1967 | 1.00 |
| gs_token448_nat_dil | 17.60 | 0.6566 | 0.1708 | 1.00 |
| gs_token448_nat_dil+reg | 25.36 | 0.8889 | 0.0966 | 0.99 |
| gs_token448_nat_dil_al | 24.98 | 0.8825 | 0.0942 | 1.00 |
| gs_token448_nat_dil_al+reg | 25.39 | 0.8880 | 0.0932 | 1.00 |
| gs_token448_nat_dil_al_local | 23.31 | 0.8671 | 0.1181 | 1.00 |
| gs_token448_nat_dil_alv | 24.87 | 0.8830 | 0.0937 | 1.00 |
| gs_token448_nat_dil_alv+reg | 25.43 | 0.8896 | 0.0926 | 1.00 |
| gs_token448_nat_dil_alv_local | 23.25 | 0.8680 | 0.1175 | 1.00 |
| gs_token448_nat_dil_local | 17.29 | 0.6474 | 0.1861 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 26.80 | 0.9226 | 0.0612 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 23.24 | 0.8919 | 0.0929 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 26.86 | 0.9225 | 0.0601 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 26.54 | 0.9211 | 0.0617 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 26.90 | 0.9231 | 0.0596 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 26.45 | 0.9211 | 0.0617 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 27.13 | 0.9261 | 0.0567 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 23.33 | 0.8921 | 0.0915 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 27.21 | 0.9263 | 0.0561 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 27.03 | 0.9252 | 0.0568 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 27.21 | 0.9260 | 0.0557 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 26.84 | 0.9242 | 0.0567 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 25.04 | 0.8968 | 0.0837 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 19.51 | 0.7971 | 0.1414 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 25.08 | 0.8966 | 0.0816 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 24.69 | 0.8921 | 0.0827 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 25.12 | 0.8974 | 0.0813 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 24.60 | 0.8918 | 0.0829 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 25.45 | 0.9062 | 0.0764 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 19.61 | 0.7965 | 0.1383 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 25.44 | 0.9051 | 0.0749 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 25.17 | 0.9014 | 0.0753 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 25.47 | 0.9058 | 0.0747 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 25.02 | 0.9008 | 0.0752 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 25.65 | 0.9186 | 0.0611 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 22.79 | 0.8880 | 0.0790 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 25.67 | 0.9183 | 0.0605 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 25.47 | 0.9171 | 0.0612 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 25.71 | 0.9190 | 0.0603 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 25.41 | 0.9170 | 0.0612 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 25.88 | 0.9220 | 0.0594 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 23.01 | 0.8890 | 0.0768 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 25.93 | 0.9220 | 0.0587 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 25.86 | 0.9213 | 0.0584 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 25.94 | 0.9218 | 0.0584 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 25.72 | 0.9206 | 0.0582 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 24.63 | 0.8818 | 0.0912 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 24.55 | 0.8814 | 0.0913 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 18.69 | 0.7470 | 0.1486 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 25.27 | 0.8938 | 0.0824 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 25.13 | 0.8934 | 0.0823 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 18.91 | 0.7503 | 0.1410 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 24.63 | 0.8818 | 0.0912 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 24.55 | 0.8814 | 0.0913 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 22.17 | 0.8225 | 0.1184 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 25.27 | 0.8938 | 0.0824 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 25.13 | 0.8934 | 0.0823 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 21.76 | 0.8188 | 0.1160 | 1.00 |

## 设置 cam5

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：vggt → `gs_token448_nat_dil_al`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=3.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 16.39 / 0.1129 | 15.31 / 0.0249 | 30.29 / 0.0331 | 26.19 / 0.0440 |
| flow_s1.0_pose | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 | 28.00 / 0.0396 |
| flow_s0.5_pose | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 | 27.45 / 0.0415 |
| gs_token448_nat_dil_al | 18.34 / 0.1402 | 16.31 / 0.0337 | 27.18 / 0.0721 | 24.79 / 0.0881 |
| gs_token448_nat_dil_al+reg | 18.88 / 0.1348 | 17.92 / 0.0277 | 28.21 / 0.0652 | 26.09 / 0.0846 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 19.83 / 0.1188 | 16.31 / 0.0337 | 31.44 / 0.0310 | 27.61 / 0.0477 |
| hyb_risktuned[gs_token448_nat_dil_al] | 20.54 / 0.0924 | 17.90 / 0.0226 | 31.45 / 0.0305 | 27.78 / 0.0434 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 20.47 / 0.1145 | 17.92 / 0.0277 | 31.46 / 0.0305 | 28.35 / 0.0454 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 20.73 / 0.0909 | 18.62 / 0.0217 | 31.45 / 0.0305 | 28.05 / 0.0428 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 22.32 | 0.8406 | 0.0684 | 1.00 |
| flow_s0.5_pose | 19.65 | 0.7479 | 0.0818 | 1.00 |
| flow_s0.5_uniform | 16.71 | 0.6135 | 0.1070 | 1.00 |
| flow_s1.0_oracle | 23.16 | 0.8541 | 0.0592 | 1.00 |
| flow_s1.0_pose | 20.41 | 0.7569 | 0.0721 | 1.00 |
| flow_s1.0_uniform | 16.39 | 0.5779 | 0.1129 | 1.00 |
| gs_center448_nat_dil | 16.95 | 0.6113 | 0.1802 | 1.00 |
| gs_center448_nat_dil+reg | 17.59 | 0.6414 | 0.1782 | 1.00 |
| gs_center448_nat_dil_al | 17.67 | 0.6479 | 0.1762 | 1.00 |
| gs_center448_nat_dil_al+reg | 17.71 | 0.6488 | 0.1788 | 1.00 |
| gs_center448_nat_dil_al_local | 17.50 | 0.6410 | 0.1894 | 1.00 |
| gs_center448_nat_dil_alv | 17.74 | 0.6598 | 0.1721 | 1.00 |
| gs_center448_nat_dil_alv+reg | 17.84 | 0.6619 | 0.1752 | 1.00 |
| gs_center448_nat_dil_alv_local | 17.54 | 0.6539 | 0.1833 | 1.00 |
| gs_center448_nat_dil_local | 16.71 | 0.6039 | 0.1918 | 1.00 |
| gs_token448_nat_dil | 16.30 | 0.5692 | 0.1773 | 1.00 |
| gs_token448_nat_dil+reg | 18.86 | 0.7140 | 0.1369 | 1.00 |
| gs_token448_nat_dil_al | 18.34 | 0.6751 | 0.1402 | 1.00 |
| gs_token448_nat_dil_al+reg | 18.88 | 0.7111 | 0.1348 | 1.00 |
| gs_token448_nat_dil_al_local | 18.08 | 0.6591 | 0.1594 | 1.00 |
| gs_token448_nat_dil_alv | 17.74 | 0.6612 | 0.1428 | 1.00 |
| gs_token448_nat_dil_alv+reg | 18.67 | 0.7103 | 0.1358 | 1.00 |
| gs_token448_nat_dil_alv_local | 17.49 | 0.6467 | 0.1609 | 1.00 |
| gs_token448_nat_dil_local | 16.09 | 0.5509 | 0.1986 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 19.41 | 0.7139 | 0.1459 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 19.03 | 0.6941 | 0.1505 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 19.49 | 0.7201 | 0.1444 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 19.50 | 0.7221 | 0.1425 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 19.64 | 0.7247 | 0.1419 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 19.62 | 0.7249 | 0.1407 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 20.49 | 0.7609 | 0.1155 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 17.76 | 0.6596 | 0.1539 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 20.47 | 0.7613 | 0.1145 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 19.83 | 0.7408 | 0.1188 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 20.23 | 0.7562 | 0.1155 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 19.22 | 0.7237 | 0.1208 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 18.11 | 0.6724 | 0.1664 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 17.43 | 0.6396 | 0.1700 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 18.21 | 0.6792 | 0.1678 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 18.18 | 0.6787 | 0.1656 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 18.29 | 0.6881 | 0.1640 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 18.19 | 0.6859 | 0.1612 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 19.23 | 0.7322 | 0.1263 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 16.89 | 0.6153 | 0.1700 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 19.26 | 0.7308 | 0.1258 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 18.79 | 0.7049 | 0.1325 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 19.03 | 0.7289 | 0.1258 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 18.18 | 0.6883 | 0.1346 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 20.11 | 0.7459 | 0.1148 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 19.58 | 0.7175 | 0.1194 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 20.17 | 0.7521 | 0.1166 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 20.17 | 0.7524 | 0.1147 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 20.12 | 0.7531 | 0.1143 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 20.06 | 0.7513 | 0.1120 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 20.70 | 0.7780 | 0.0928 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 19.35 | 0.7186 | 0.1104 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 20.73 | 0.7780 | 0.0909 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 20.54 | 0.7699 | 0.0924 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 20.55 | 0.7760 | 0.0924 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 20.03 | 0.7548 | 0.0974 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 17.55 | 0.6433 | 0.1887 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 17.56 | 0.6547 | 0.1838 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 16.74 | 0.6048 | 0.1923 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 18.15 | 0.6634 | 0.1558 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 17.55 | 0.6497 | 0.1584 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 16.24 | 0.5634 | 0.1900 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 16.93 | 0.6116 | 0.1961 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 16.96 | 0.6213 | 0.1905 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 15.81 | 0.5514 | 0.2150 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 17.79 | 0.6429 | 0.1589 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 17.81 | 0.6533 | 0.1575 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 16.54 | 0.5767 | 0.1906 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.18 | 0.7600 | 0.0171 | 1.00 |
| flow_s0.5_pose | 17.06 | 0.6711 | 0.0195 | 1.00 |
| flow_s0.5_uniform | 15.30 | 0.5755 | 0.0247 | 1.00 |
| flow_s1.0_oracle | 19.73 | 0.7659 | 0.0154 | 1.00 |
| flow_s1.0_pose | 17.62 | 0.6745 | 0.0175 | 1.00 |
| flow_s1.0_uniform | 15.31 | 0.5619 | 0.0249 | 1.00 |
| gs_center448_nat_dil | 16.14 | 0.5734 | 0.0403 | 1.00 |
| gs_center448_nat_dil+reg | 17.08 | 0.6474 | 0.0308 | 1.00 |
| gs_center448_nat_dil_al | 16.84 | 0.6375 | 0.0319 | 1.00 |
| gs_center448_nat_dil_al+reg | 17.11 | 0.6501 | 0.0309 | 1.00 |
| gs_center448_nat_dil_al_local | 16.83 | 0.6315 | 0.0330 | 1.00 |
| gs_center448_nat_dil_alv | 17.00 | 0.6440 | 0.0318 | 1.00 |
| gs_center448_nat_dil_alv+reg | 17.22 | 0.6554 | 0.0309 | 1.00 |
| gs_center448_nat_dil_alv_local | 16.94 | 0.6366 | 0.0329 | 1.00 |
| gs_center448_nat_dil_local | 16.09 | 0.5657 | 0.0416 | 1.00 |
| gs_token448_nat_dil | 14.19 | 0.4878 | 0.0463 | 1.00 |
| gs_token448_nat_dil+reg | 18.08 | 0.6978 | 0.0277 | 1.00 |
| gs_token448_nat_dil_al | 16.31 | 0.6236 | 0.0337 | 1.00 |
| gs_token448_nat_dil_al+reg | 17.92 | 0.6902 | 0.0277 | 1.00 |
| gs_token448_nat_dil_al_local | 16.34 | 0.6149 | 0.0354 | 1.00 |
| gs_token448_nat_dil_alv | 15.80 | 0.6002 | 0.0351 | 1.00 |
| gs_token448_nat_dil_alv+reg | 17.79 | 0.6882 | 0.0280 | 1.00 |
| gs_token448_nat_dil_alv_local | 15.85 | 0.5921 | 0.0368 | 1.00 |
| gs_token448_nat_dil_local | 14.37 | 0.4744 | 0.0474 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 17.08 | 0.6472 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 16.14 | 0.5878 | 0.0403 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 17.11 | 0.6494 | 0.0309 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 16.84 | 0.6377 | 0.0319 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 17.22 | 0.6542 | 0.0309 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 17.00 | 0.6441 | 0.0318 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 18.08 | 0.6957 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 14.19 | 0.4836 | 0.0463 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 17.92 | 0.6883 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 16.31 | 0.6191 | 0.0337 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 17.79 | 0.6858 | 0.0280 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 15.80 | 0.5949 | 0.0351 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 17.37 | 0.6628 | 0.0292 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 16.67 | 0.6136 | 0.0353 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 17.40 | 0.6653 | 0.0293 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 17.16 | 0.6557 | 0.0300 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 17.49 | 0.6697 | 0.0293 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 17.27 | 0.6608 | 0.0301 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 18.31 | 0.7078 | 0.0264 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 14.77 | 0.5378 | 0.0410 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 18.13 | 0.7001 | 0.0267 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 16.86 | 0.6523 | 0.0301 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 17.99 | 0.6982 | 0.0268 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 16.36 | 0.6307 | 0.0310 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 18.13 | 0.7003 | 0.0235 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 17.79 | 0.6698 | 0.0260 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 18.13 | 0.7004 | 0.0235 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 18.00 | 0.6959 | 0.0235 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 18.09 | 0.7011 | 0.0236 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 17.98 | 0.6965 | 0.0236 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 18.83 | 0.7284 | 0.0212 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 16.27 | 0.6188 | 0.0283 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 18.62 | 0.7203 | 0.0217 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 17.90 | 0.6954 | 0.0226 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 18.52 | 0.7186 | 0.0218 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 17.47 | 0.6767 | 0.0235 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 16.87 | 0.6387 | 0.0327 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 16.99 | 0.6442 | 0.0324 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 16.25 | 0.5852 | 0.0401 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 16.41 | 0.6240 | 0.0338 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 15.94 | 0.6035 | 0.0350 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 14.50 | 0.4987 | 0.0451 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 16.55 | 0.6012 | 0.0361 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 16.67 | 0.6044 | 0.0359 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 15.63 | 0.5352 | 0.0431 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 16.58 | 0.6236 | 0.0335 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 17.11 | 0.6473 | 0.0319 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 15.82 | 0.5576 | 0.0386 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 17.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.73 | 0.8826 | 0.0204 | 1.00 |
| flow_s0.5_pose | 22.21 | 0.8504 | 0.0224 | 1.00 |
| flow_s0.5_uniform | 20.55 | 0.8064 | 0.0266 | 1.00 |
| flow_s1.0_oracle | 24.76 | 0.8987 | 0.0188 | 1.00 |
| flow_s1.0_pose | 23.17 | 0.8669 | 0.0208 | 1.00 |
| flow_s1.0_uniform | 20.86 | 0.8093 | 0.0253 | 1.00 |
| gs_center448_nat_dil | 19.06 | 0.6824 | 0.0609 | 1.00 |
| gs_center448_nat_dil+reg | 20.84 | 0.7696 | 0.0467 | 1.00 |
| gs_center448_nat_dil_al | 20.51 | 0.7566 | 0.0469 | 1.00 |
| gs_center448_nat_dil_al+reg | 20.86 | 0.7704 | 0.0463 | 1.00 |
| gs_center448_nat_dil_al_local | 19.17 | 0.7332 | 0.0555 | 1.00 |
| gs_center448_nat_dil_alv | 20.54 | 0.7600 | 0.0466 | 1.00 |
| gs_center448_nat_dil_alv+reg | 20.91 | 0.7737 | 0.0461 | 1.00 |
| gs_center448_nat_dil_alv_local | 19.13 | 0.7367 | 0.0552 | 1.00 |
| gs_center448_nat_dil_local | 18.12 | 0.6620 | 0.0679 | 1.00 |
| gs_token448_nat_dil | 18.22 | 0.6518 | 0.0626 | 1.00 |
| gs_token448_nat_dil+reg | 21.63 | 0.7962 | 0.0406 | 1.00 |
| gs_token448_nat_dil_al | 20.25 | 0.7493 | 0.0463 | 1.00 |
| gs_token448_nat_dil_al+reg | 21.57 | 0.7949 | 0.0400 | 1.00 |
| gs_token448_nat_dil_al_local | 18.83 | 0.7230 | 0.0564 | 1.00 |
| gs_token448_nat_dil_alv | 19.94 | 0.7419 | 0.0468 | 1.00 |
| gs_token448_nat_dil_alv+reg | 21.47 | 0.7938 | 0.0403 | 1.00 |
| gs_token448_nat_dil_alv_local | 18.57 | 0.7159 | 0.0568 | 1.00 |
| gs_token448_nat_dil_local | 17.38 | 0.6298 | 0.0715 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 23.06 | 0.8544 | 0.0281 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 22.41 | 0.8379 | 0.0311 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 23.08 | 0.8553 | 0.0280 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 22.89 | 0.8529 | 0.0282 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 23.15 | 0.8563 | 0.0280 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 22.97 | 0.8540 | 0.0281 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 23.83 | 0.8681 | 0.0254 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 20.84 | 0.8105 | 0.0338 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 23.70 | 0.8667 | 0.0255 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 22.67 | 0.8512 | 0.0278 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 23.59 | 0.8653 | 0.0254 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 22.25 | 0.8438 | 0.0280 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 20.85 | 0.7692 | 0.0467 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 19.06 | 0.6827 | 0.0609 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 20.86 | 0.7697 | 0.0463 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 20.51 | 0.7560 | 0.0469 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 20.91 | 0.7728 | 0.0461 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 20.54 | 0.7593 | 0.0466 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 21.63 | 0.7956 | 0.0406 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 18.22 | 0.6521 | 0.0626 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 21.57 | 0.7945 | 0.0400 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 20.25 | 0.7495 | 0.0463 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 21.47 | 0.7933 | 0.0403 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 19.94 | 0.7422 | 0.0468 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 22.90 | 0.8502 | 0.0281 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 22.14 | 0.8268 | 0.0296 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 22.93 | 0.8513 | 0.0279 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 22.83 | 0.8492 | 0.0277 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 22.91 | 0.8521 | 0.0278 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 22.80 | 0.8494 | 0.0277 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 23.44 | 0.8633 | 0.0253 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 21.18 | 0.8127 | 0.0286 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 23.34 | 0.8614 | 0.0252 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 22.78 | 0.8507 | 0.0256 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 23.27 | 0.8611 | 0.0253 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 22.44 | 0.8444 | 0.0259 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 20.32 | 0.7465 | 0.0495 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 20.32 | 0.7496 | 0.0492 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 18.90 | 0.6746 | 0.0628 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 20.07 | 0.7361 | 0.0489 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 19.78 | 0.7288 | 0.0494 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 18.27 | 0.6478 | 0.0632 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 19.77 | 0.7156 | 0.0534 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 19.74 | 0.7164 | 0.0536 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 18.54 | 0.6667 | 0.0623 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 20.20 | 0.7353 | 0.0486 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 20.35 | 0.7399 | 0.0472 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 19.15 | 0.6767 | 0.0567 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 25.73 | 0.9248 | 0.0355 | 1.00 |
| flow_s0.5_pose | 24.65 | 0.9099 | 0.0374 | 1.00 |
| flow_s0.5_uniform | 23.02 | 0.8845 | 0.0430 | 1.00 |
| flow_s1.0_oracle | 26.44 | 0.9323 | 0.0341 | 1.00 |
| flow_s1.0_pose | 25.29 | 0.9172 | 0.0359 | 1.00 |
| flow_s1.0_uniform | 23.35 | 0.8857 | 0.0419 | 1.00 |
| gs_center448_nat_dil | 21.65 | 0.7642 | 0.0843 | 1.00 |
| gs_center448_nat_dil+reg | 23.27 | 0.8446 | 0.0628 | 1.00 |
| gs_center448_nat_dil_al | 22.87 | 0.8352 | 0.0651 | 1.00 |
| gs_center448_nat_dil_al+reg | 23.28 | 0.8454 | 0.0628 | 1.00 |
| gs_center448_nat_dil_al_local | 18.42 | 0.8023 | 0.1006 | 1.00 |
| gs_center448_nat_dil_alv | 22.94 | 0.8378 | 0.0646 | 1.00 |
| gs_center448_nat_dil_alv+reg | 23.34 | 0.8481 | 0.0621 | 1.00 |
| gs_center448_nat_dil_alv_local | 18.43 | 0.8047 | 0.1001 | 1.00 |
| gs_center448_nat_dil_local | 18.12 | 0.7386 | 0.1152 | 1.00 |
| gs_token448_nat_dil | 20.53 | 0.7619 | 0.0870 | 1.00 |
| gs_token448_nat_dil+reg | 23.93 | 0.8636 | 0.0575 | 1.00 |
| gs_token448_nat_dil_al | 22.40 | 0.8291 | 0.0673 | 1.00 |
| gs_token448_nat_dil_al+reg | 23.86 | 0.8620 | 0.0572 | 1.00 |
| gs_token448_nat_dil_al_local | 18.24 | 0.7954 | 0.1013 | 1.00 |
| gs_token448_nat_dil_alv | 22.12 | 0.8249 | 0.0680 | 1.00 |
| gs_token448_nat_dil_alv+reg | 23.79 | 0.8617 | 0.0576 | 1.00 |
| gs_token448_nat_dil_alv_local | 18.15 | 0.7913 | 0.1020 | 1.00 |
| gs_token448_nat_dil_local | 17.50 | 0.7304 | 0.1195 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 25.39 | 0.9121 | 0.0418 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 24.86 | 0.9025 | 0.0447 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 25.37 | 0.9123 | 0.0417 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 25.19 | 0.9110 | 0.0418 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 25.39 | 0.9126 | 0.0416 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 25.24 | 0.9113 | 0.0417 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 26.01 | 0.9181 | 0.0398 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 23.36 | 0.8903 | 0.0475 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 25.87 | 0.9179 | 0.0395 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 24.93 | 0.9101 | 0.0420 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 25.77 | 0.9171 | 0.0398 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 24.51 | 0.9063 | 0.0430 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 24.01 | 0.8844 | 0.0505 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 22.84 | 0.8531 | 0.0580 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 24.00 | 0.8843 | 0.0506 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 23.65 | 0.8788 | 0.0514 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 24.02 | 0.8855 | 0.0504 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 23.69 | 0.8801 | 0.0512 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 24.54 | 0.8928 | 0.0478 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 21.68 | 0.8390 | 0.0625 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 24.46 | 0.8923 | 0.0472 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 23.32 | 0.8748 | 0.0524 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 24.36 | 0.8916 | 0.0477 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 22.99 | 0.8704 | 0.0531 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 25.12 | 0.9118 | 0.0401 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 24.63 | 0.9014 | 0.0417 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 25.09 | 0.9118 | 0.0401 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 25.01 | 0.9109 | 0.0400 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 25.07 | 0.9122 | 0.0401 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 24.99 | 0.9111 | 0.0400 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 25.50 | 0.9157 | 0.0383 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 23.71 | 0.8936 | 0.0426 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 25.38 | 0.9148 | 0.0383 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 24.96 | 0.9104 | 0.0392 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 25.31 | 0.9145 | 0.0384 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 24.62 | 0.9071 | 0.0399 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 22.90 | 0.8458 | 0.0628 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 22.94 | 0.8481 | 0.0621 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 21.84 | 0.7972 | 0.0739 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 22.44 | 0.8381 | 0.0644 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 22.16 | 0.8341 | 0.0652 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 20.89 | 0.7848 | 0.0782 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 22.63 | 0.8302 | 0.0656 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 22.64 | 0.8304 | 0.0651 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 21.72 | 0.7994 | 0.0735 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 22.70 | 0.8388 | 0.0639 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 22.96 | 0.8438 | 0.0625 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 21.95 | 0.8062 | 0.0716 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 31.41 | 0.9667 | 0.0317 | 1.00 |
| flow_s0.5_pose | 31.22 | 0.9653 | 0.0318 | 1.00 |
| flow_s0.5_uniform | 30.53 | 0.9607 | 0.0346 | 1.00 |
| flow_s1.0_oracle | 31.56 | 0.9661 | 0.0302 | 1.00 |
| flow_s1.0_pose | 31.46 | 0.9649 | 0.0305 | 1.00 |
| flow_s1.0_uniform | 30.29 | 0.9592 | 0.0331 | 1.00 |
| gs_center448_nat_dil | 24.77 | 0.8371 | 0.0928 | 1.00 |
| gs_center448_nat_dil+reg | 27.84 | 0.9142 | 0.0739 | 0.99 |
| gs_center448_nat_dil_al | 27.58 | 0.9112 | 0.0728 | 1.00 |
| gs_center448_nat_dil_al+reg | 27.84 | 0.9143 | 0.0727 | 1.00 |
| gs_center448_nat_dil_al_local | 16.50 | 0.8467 | 0.1431 | 1.00 |
| gs_center448_nat_dil_alv | 27.66 | 0.9130 | 0.0723 | 1.00 |
| gs_center448_nat_dil_alv+reg | 27.96 | 0.9162 | 0.0721 | 1.00 |
| gs_center448_nat_dil_alv_local | 16.51 | 0.8486 | 0.1426 | 1.00 |
| gs_center448_nat_dil_local | 16.42 | 0.7835 | 0.1573 | 1.00 |
| gs_token448_nat_dil | 25.25 | 0.8706 | 0.0932 | 1.00 |
| gs_token448_nat_dil+reg | 28.31 | 0.9272 | 0.0651 | 1.00 |
| gs_token448_nat_dil_al | 27.18 | 0.9123 | 0.0721 | 1.00 |
| gs_token448_nat_dil_al+reg | 28.21 | 0.9253 | 0.0652 | 1.00 |
| gs_token448_nat_dil_al_local | 16.40 | 0.8476 | 0.1433 | 1.00 |
| gs_token448_nat_dil_alv | 27.14 | 0.9124 | 0.0723 | 1.00 |
| gs_token448_nat_dil_alv+reg | 28.24 | 0.9257 | 0.0650 | 1.00 |
| gs_token448_nat_dil_alv_local | 16.43 | 0.8479 | 0.1434 | 1.00 |
| gs_token448_nat_dil_local | 16.08 | 0.8083 | 0.1621 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 31.45 | 0.9640 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 31.43 | 0.9632 | 0.0309 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 31.46 | 0.9640 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 31.45 | 0.9639 | 0.0306 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 31.46 | 0.9640 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 31.45 | 0.9639 | 0.0306 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 31.46 | 0.9642 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 31.42 | 0.9629 | 0.0318 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 31.46 | 0.9643 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 31.44 | 0.9636 | 0.0310 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 31.46 | 0.9643 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 31.43 | 0.9635 | 0.0310 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 31.38 | 0.9619 | 0.0314 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 31.29 | 0.9595 | 0.0331 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 31.38 | 0.9619 | 0.0314 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 31.36 | 0.9616 | 0.0317 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 31.38 | 0.9620 | 0.0314 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 31.36 | 0.9617 | 0.0316 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 31.40 | 0.9624 | 0.0313 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 31.32 | 0.9586 | 0.0349 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 31.40 | 0.9624 | 0.0312 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 31.35 | 0.9615 | 0.0322 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 31.40 | 0.9624 | 0.0313 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 31.36 | 0.9615 | 0.0322 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 31.46 | 0.9648 | 0.0305 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 28.30 | 0.9359 | 0.0568 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 28.36 | 0.9368 | 0.0562 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 26.98 | 0.9139 | 0.0692 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 27.97 | 0.9337 | 0.0598 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 27.89 | 0.9336 | 0.0598 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 26.99 | 0.9134 | 0.0742 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 27.93 | 0.9320 | 0.0591 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 27.91 | 0.9320 | 0.0590 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 27.31 | 0.9236 | 0.0648 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 27.87 | 0.9330 | 0.0594 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 28.07 | 0.9343 | 0.0570 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 27.52 | 0.9214 | 0.0665 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 28.40 | 0.9528 | 0.0403 | 1.00 |
| flow_s0.5_pose | 27.45 | 0.9461 | 0.0415 | 1.00 |
| flow_s0.5_uniform | 26.08 | 0.9340 | 0.0467 | 1.00 |
| flow_s1.0_oracle | 28.96 | 0.9545 | 0.0383 | 1.00 |
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| flow_s1.0_uniform | 26.19 | 0.9330 | 0.0440 | 1.00 |
| gs_center448_nat_dil | 23.17 | 0.8118 | 0.1097 | 1.00 |
| gs_center448_nat_dil+reg | 25.56 | 0.8904 | 0.0969 | 0.99 |
| gs_center448_nat_dil_al | 25.22 | 0.8856 | 0.0940 | 1.00 |
| gs_center448_nat_dil_al+reg | 25.57 | 0.8906 | 0.0954 | 1.00 |
| gs_center448_nat_dil_al_local | 16.85 | 0.8307 | 0.1640 | 1.00 |
| gs_center448_nat_dil_alv | 25.30 | 0.8877 | 0.0937 | 1.00 |
| gs_center448_nat_dil_alv+reg | 25.66 | 0.8928 | 0.0948 | 1.00 |
| gs_center448_nat_dil_alv_local | 16.87 | 0.8328 | 0.1637 | 1.00 |
| gs_center448_nat_dil_local | 16.67 | 0.7659 | 0.1744 | 1.00 |
| gs_token448_nat_dil | 22.79 | 0.8339 | 0.1057 | 1.00 |
| gs_token448_nat_dil+reg | 26.17 | 0.9051 | 0.0856 | 1.00 |
| gs_token448_nat_dil_al | 24.79 | 0.8848 | 0.0881 | 1.00 |
| gs_token448_nat_dil_al+reg | 26.09 | 0.9035 | 0.0846 | 1.00 |
| gs_token448_nat_dil_al_local | 16.76 | 0.8295 | 0.1592 | 1.00 |
| gs_token448_nat_dil_alv | 24.58 | 0.8833 | 0.0885 | 1.00 |
| gs_token448_nat_dil_alv+reg | 26.06 | 0.9035 | 0.0850 | 1.00 |
| gs_token448_nat_dil_alv_local | 16.74 | 0.8281 | 0.1595 | 1.00 |
| gs_token448_nat_dil_local | 16.26 | 0.7805 | 0.1750 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 27.97 | 0.9449 | 0.0480 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 27.43 | 0.9400 | 0.0520 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al+reg] | 27.95 | 0.9450 | 0.0481 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_al] | 27.81 | 0.9444 | 0.0478 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv+reg] | 27.98 | 0.9452 | 0.0480 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_alv] | 27.85 | 0.9446 | 0.0477 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil+reg] | 28.46 | 0.9474 | 0.0456 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil] | 26.45 | 0.9354 | 0.0539 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al+reg] | 28.35 | 0.9475 | 0.0454 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_al] | 27.61 | 0.9438 | 0.0477 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv+reg] | 28.28 | 0.9471 | 0.0456 | 1.00 |
| hyb_oracle_fail[gs_token448_nat_dil_alv] | 27.26 | 0.9421 | 0.0484 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 26.81 | 0.9312 | 0.0583 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 25.80 | 0.9159 | 0.0650 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al+reg] | 26.80 | 0.9311 | 0.0584 | 1.00 |
| hyb_risk[gs_center448_nat_dil_al] | 26.52 | 0.9287 | 0.0586 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv+reg] | 26.83 | 0.9317 | 0.0581 | 1.00 |
| hyb_risk[gs_center448_nat_dil_alv] | 26.56 | 0.9293 | 0.0583 | 1.00 |
| hyb_risk[gs_token448_nat_dil+reg] | 27.29 | 0.9351 | 0.0551 | 1.00 |
| hyb_risk[gs_token448_nat_dil] | 24.94 | 0.9097 | 0.0682 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al+reg] | 27.22 | 0.9350 | 0.0543 | 1.00 |
| hyb_risk[gs_token448_nat_dil_al] | 26.35 | 0.9277 | 0.0577 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv+reg] | 27.16 | 0.9347 | 0.0549 | 1.00 |
| hyb_risk[gs_token448_nat_dil_alv] | 26.08 | 0.9261 | 0.0582 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 27.86 | 0.9458 | 0.0448 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 27.54 | 0.9418 | 0.0458 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al+reg] | 27.82 | 0.9458 | 0.0448 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_al] | 27.77 | 0.9455 | 0.0445 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv+reg] | 27.81 | 0.9460 | 0.0448 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_alv] | 27.75 | 0.9455 | 0.0444 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil+reg] | 28.16 | 0.9474 | 0.0427 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil] | 26.88 | 0.9387 | 0.0462 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al+reg] | 28.05 | 0.9472 | 0.0428 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_al] | 27.78 | 0.9457 | 0.0434 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv+reg] | 28.00 | 0.9470 | 0.0429 | 1.00 |
| hyb_risktuned[gs_token448_nat_dil_alv] | 27.49 | 0.9445 | 0.0438 | 1.00 |
| hyb_token[gs_center448_nat_dil_al_local] | 25.49 | 0.9062 | 0.0791 | 1.00 |
| hyb_token[gs_center448_nat_dil_alv_local] | 25.55 | 0.9075 | 0.0786 | 1.00 |
| hyb_token[gs_center448_nat_dil_local] | 24.31 | 0.8764 | 0.0891 | 1.00 |
| hyb_token[gs_token448_nat_dil_al_local] | 25.12 | 0.9026 | 0.0773 | 1.00 |
| hyb_token[gs_token448_nat_dil_alv_local] | 24.89 | 0.9010 | 0.0777 | 1.00 |
| hyb_token[gs_token448_nat_dil_local] | 23.61 | 0.8699 | 0.0879 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_al_local] | 25.11 | 0.8978 | 0.0817 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_alv_local] | 25.12 | 0.8979 | 0.0816 | 1.00 |
| hyb_token_ringreg[gs_center448_nat_dil_local] | 24.32 | 0.8829 | 0.0898 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_al_local] | 25.18 | 0.9018 | 0.0769 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_alv_local] | 25.46 | 0.9039 | 0.0760 | 1.00 |
| hyb_token_ringreg[gs_token448_nat_dil_local] | 24.55 | 0.8835 | 0.0837 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|
| cam3 | gs_center448_nat_dil | 10.57 | 1.00 |
| cam3 | gs_center448_nat_dil_al | 1.18 | 1.00 |
| cam3 | gs_center448_nat_dil_alv | 1.15 | 1.00 |
| cam3 | gs_token448_nat_dil | 9.47 | 1.00 |
| cam3 | gs_token448_nat_dil_al | 0.54 | 0.83 |
| cam3 | gs_token448_nat_dil_alv | 0.60 | 0.83 |
| cam5 | gs_center448_nat_dil | 2.88 | 1.00 |
| cam5 | gs_center448_nat_dil_al | 1.05 | 1.00 |
| cam5 | gs_center448_nat_dil_alv | 1.02 | 1.00 |
| cam5 | gs_token448_nat_dil | 2.53 | 1.00 |
| cam5 | gs_token448_nat_dil_al | 1.34 | 1.00 |
| cam5 | gs_token448_nat_dil_alv | 1.44 | 1.00 |

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
| cam3 | gs_center448_nat_dil | vggt | 1080 | 1080 | classic | 1.74 | False | 432956 | 0.333 | 20.7 | 29.17 | 0.37 | 0.010 |
| cam3 | gs_center448_nat_dil_al | aligned_int | 1080 | None | classic | 2.72 | False | 432956 | 0.333 | 42.7 | 29.17 | 0.37 | 0.010 |
| cam3 | gs_center448_nat_dil_al_local | aligned_int | 1080 | None | classic | 2.72 | False | 432956 | 0.333 | 42.4 | 29.17 | 0.37 | 0.010 |
| cam3 | gs_center448_nat_dil_alv | aligned_vggt | 1080 | None | classic | 2.72 | False | 432956 | 0.333 | 32.9 | 29.17 | 0.37 | 0.010 |
| cam3 | gs_center448_nat_dil_alv_local | aligned_vggt | 1080 | None | classic | 2.72 | False | 432956 | 0.333 | 42.6 | 29.17 | 0.37 | 0.010 |
| cam3 | gs_center448_nat_dil_local | vggt | 1080 | 1080 | classic | 1.74 | False | 432956 | 0.333 | 35.8 | 29.17 | 0.37 | 0.010 |
| cam3 | gs_token448_nat_dil | vggt | 911 | 911 | classic | 1.24 | False | 368407 | 0.812 | 23.2 | 29.15 | 0.33 | 0.011 |
| cam3 | gs_token448_nat_dil_al | aligned_int | 911 | None | classic | 1.94 | False | 368407 | 0.812 | 41.0 | 29.15 | 0.33 | 0.011 |
| cam3 | gs_token448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368407 | 0.812 | 44.9 | 29.15 | 0.33 | 0.011 |
| cam3 | gs_token448_nat_dil_alv | aligned_vggt | 911 | None | classic | 1.94 | False | 368407 | 0.812 | 34.7 | 29.15 | 0.33 | 0.011 |
| cam3 | gs_token448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368407 | 0.812 | 42.3 | 29.15 | 0.33 | 0.011 |
| cam3 | gs_token448_nat_dil_local | vggt | 911 | 911 | classic | 1.24 | False | 368407 | 0.812 | 37.0 | 29.15 | 0.33 | 0.011 |
| cam5 | gs_center448_nat_dil | vggt | 1080 | 1080 | classic | 1.74 | False | 638686 | 0.504 | 20.2 | 29.83 | 0.15 | 0.007 |
| cam5 | gs_center448_nat_dil_al | aligned_int | 1080 | None | classic | 2.72 | False | 638686 | 0.504 | 24.2 | 29.83 | 0.15 | 0.007 |
| cam5 | gs_center448_nat_dil_al_local | aligned_int | 1080 | None | classic | 2.72 | False | 638686 | 0.504 | 42.9 | 29.83 | 0.15 | 0.007 |
| cam5 | gs_center448_nat_dil_alv | aligned_vggt | 1080 | None | classic | 2.72 | False | 638686 | 0.504 | 26.8 | 29.83 | 0.15 | 0.007 |
| cam5 | gs_center448_nat_dil_alv_local | aligned_vggt | 1080 | None | classic | 2.72 | False | 638686 | 0.504 | 43.4 | 29.83 | 0.15 | 0.007 |
| cam5 | gs_center448_nat_dil_local | vggt | 1080 | 1080 | classic | 1.74 | False | 638686 | 0.504 | 34.6 | 29.83 | 0.15 | 0.007 |
| cam5 | gs_token448_nat_dil | vggt | 917 | 917 | classic | 1.26 | False | 528340 | 0.517 | 18.3 | 29.47 | 0.12 | 0.007 |
| cam5 | gs_token448_nat_dil_al | aligned_int | 917 | None | classic | 1.96 | False | 528340 | 0.517 | 23.6 | 29.47 | 0.12 | 0.007 |
| cam5 | gs_token448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 528340 | 0.517 | 43.4 | 29.47 | 0.12 | 0.007 |
| cam5 | gs_token448_nat_dil_alv | aligned_vggt | 917 | None | classic | 1.96 | False | 528340 | 0.517 | 22.5 | 29.47 | 0.12 | 0.007 |
| cam5 | gs_token448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 528340 | 0.517 | 42.6 | 29.47 | 0.12 | 0.007 |
| cam5 | gs_token448_nat_dil_local | vggt | 917 | 917 | classic | 1.26 | False | 528340 | 0.517 | 32.3 | 29.47 | 0.12 | 0.007 |

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

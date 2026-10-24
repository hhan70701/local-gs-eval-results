# 局部 GS 质量验证结果汇总（第二轮：Mip 滤波 + ROI + 配准诊断）

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## 设置 cam3

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：vggt → `gs_center448_nat_mip`，calib → `gs_roi448_nat_mip_cal`，calibK → `gs_center448_nat_mip_calK`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=6.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 13.02 / 0.2906 | 12.52 / 0.0568 | 32.36 / 0.0269 | 22.18 / 0.0691 |
| flow_s1.0_pose | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 | 22.60 / 0.0629 |
| flow_s1.0_posecal | 12.50 / 0.2972 | 12.32 / 0.0627 | 31.83 / 0.0279 | 21.96 / 0.0708 |
| flow_s0.5_pose | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 | 22.93 / 0.0610 |
| flow_s0.5_posecal | 11.87 / 0.2892 | 12.44 / 0.0623 | 31.26 / 0.0302 | 21.89 / 0.0712 |
| gs_center448_nat_mip | 14.95 / 0.2402 | 13.36 / 0.1075 | 19.43 / 0.1601 | 17.34 / 0.1813 |
| gs_center448_nat_mip+reg | 17.54 / 0.1822 | 18.03 / 0.0517 | 29.03 / 0.0617 | 24.75 / 0.1076 |
| hyb_oracle_fail[gs_center448_nat_mip] | 16.13 / 0.2091 | 13.36 / 0.1075 | 33.30 / 0.0267 | 23.22 / 0.0932 |
| hyb_risktuned[gs_center448_nat_mip] | 14.84 / 0.2451 | 14.35 / 0.0694 | 33.53 / 0.0234 | 22.80 / 0.0788 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 18.27 / 0.1706 | 18.04 / 0.0515 | 33.53 / 0.0233 | 26.75 / 0.0613 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 16.51 / 0.1964 | 16.95 / 0.0464 | 33.54 / 0.0233 | 25.59 / 0.0609 |
| gs_roi448_nat_mip_cal | 11.39 / 0.3589 | 9.96 / 0.2265 | 13.75 / 0.2547 | 12.04 / 0.3243 |
| gs_roi448_nat_mip_cal+reg | 14.72 / 0.2328 | 15.66 / 0.0864 | 24.53 / 0.0823 | 20.51 / 0.1492 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 12.76 / 0.3268 | 10.73 / 0.1127 | 33.00 / 0.0275 | 20.77 / 0.1006 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 11.69 / 0.3479 | 11.81 / 0.0776 | 33.51 / 0.0239 | 20.13 / 0.0942 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 15.77 / 0.2189 | 16.13 / 0.0522 | 33.52 / 0.0236 | 25.26 / 0.0610 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 14.51 / 0.2454 | 15.59 / 0.0473 | 33.53 / 0.0233 | 24.49 / 0.0609 |
| gs_center448_nat_mip_calK | 9.56 / 0.5233 | 9.44 / 0.1697 | 10.78 / 0.3202 | 10.01 / 0.3856 |
| gs_center448_nat_mip_calK+reg | 15.66 / 0.2228 | 16.65 / 0.0595 | 28.44 / 0.0641 | 23.49 / 0.1145 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 11.36 / 0.4223 | 9.44 / 0.1697 | 32.64 / 0.0303 | 19.46 / 0.1382 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 10.21 / 0.4724 | 10.87 / 0.1099 | 33.41 / 0.0249 | 18.10 / 0.1272 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 16.63 / 0.2055 | 16.69 / 0.0574 | 33.53 / 0.0233 | 25.78 / 0.0654 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 15.06 / 0.2341 | 16.07 / 0.0502 | 33.54 / 0.0233 | 24.81 / 0.0639 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 16.10 | 0.5746 | 0.1984 | 1.00 |
| flow_s0.5_pose | 14.85 | 0.5040 | 0.2383 | 1.00 |
| flow_s0.5_posecal | 11.87 | 0.3807 | 0.2892 | 1.00 |
| flow_s0.5_uniform | 14.21 | 0.5001 | 0.2198 | 1.00 |
| flow_s1.0_oracle | 15.16 | 0.5837 | 0.2651 | 1.00 |
| flow_s1.0_pose | 14.53 | 0.5347 | 0.2724 | 1.00 |
| flow_s1.0_posecal | 12.50 | 0.4452 | 0.2972 | 1.00 |
| flow_s1.0_uniform | 13.02 | 0.4647 | 0.2906 | 1.00 |
| gs_center448_nat_dil | 14.95 | 0.4982 | 0.2409 | 1.00 |
| gs_center448_nat_dil+reg | 17.60 | 0.6484 | 0.1821 | 1.00 |
| gs_center448_nat_dil_cal | 10.69 | 0.3095 | 0.4211 | 1.00 |
| gs_center448_nat_dil_cal+reg | 15.66 | 0.5331 | 0.2247 | 1.00 |
| gs_center448_nat_dil_calK | 9.55 | 0.2905 | 0.5223 | 1.00 |
| gs_center448_nat_dil_calK+reg | 15.62 | 0.5289 | 0.2225 | 1.00 |
| gs_center448_nat_mip | 14.95 | 0.4952 | 0.2402 | 1.00 |
| gs_center448_nat_mip+reg | 17.54 | 0.6463 | 0.1822 | 1.00 |
| gs_center448_nat_mip_cal | 10.70 | 0.3070 | 0.4211 | 1.00 |
| gs_center448_nat_mip_cal+reg | 15.59 | 0.5280 | 0.2256 | 1.00 |
| gs_center448_nat_mip_calK | 9.56 | 0.2917 | 0.5233 | 1.00 |
| gs_center448_nat_mip_calK+reg | 15.66 | 0.5317 | 0.2228 | 1.00 |
| gs_roi448_nat_dil | 13.97 | 0.4430 | 0.2458 | 1.00 |
| gs_roi448_nat_dil+reg | 17.26 | 0.6487 | 0.1700 | 1.00 |
| gs_roi448_nat_dil_cal | 11.38 | 0.3320 | 0.3586 | 1.00 |
| gs_roi448_nat_dil_cal+reg | 14.74 | 0.4877 | 0.2318 | 1.00 |
| gs_roi448_nat_dil_calK | 8.80 | 0.3520 | 0.6734 | 1.00 |
| gs_roi448_nat_dil_calK+reg | 8.82 | 0.3546 | 0.6761 | 1.00 |
| gs_roi448_nat_mip | 13.97 | 0.4427 | 0.2463 | 1.00 |
| gs_roi448_nat_mip+reg | 17.26 | 0.6486 | 0.1710 | 1.00 |
| gs_roi448_nat_mip_cal | 11.39 | 0.3321 | 0.3589 | 1.00 |
| gs_roi448_nat_mip_cal+reg | 14.72 | 0.4871 | 0.2328 | 1.00 |
| gs_roi448_nat_mip_calK | 8.80 | 0.3527 | 0.6723 | 1.00 |
| gs_roi448_nat_mip_calK+reg | 8.82 | 0.3552 | 0.6758 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 18.35 | 0.6829 | 0.1697 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 16.15 | 0.5654 | 0.2084 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 16.68 | 0.5936 | 0.2085 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 16.58 | 0.5864 | 0.2056 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 11.36 | 0.3888 | 0.4218 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 12.39 | 0.4213 | 0.3385 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 18.27 | 0.6793 | 0.1706 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 16.13 | 0.5617 | 0.2091 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 16.61 | 0.5893 | 0.2101 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 16.63 | 0.5888 | 0.2055 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 11.36 | 0.3895 | 0.4223 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 12.39 | 0.4194 | 0.3380 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 18.11 | 0.6849 | 0.1650 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 15.21 | 0.5352 | 0.2240 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 15.79 | 0.5546 | 0.2185 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 11.02 | 0.4113 | 0.4721 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 11.01 | 0.4104 | 0.4709 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 12.75 | 0.4153 | 0.3267 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 18.11 | 0.6848 | 0.1654 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 15.21 | 0.5350 | 0.2239 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 15.77 | 0.5544 | 0.2189 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 11.02 | 0.4116 | 0.4720 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 11.01 | 0.4106 | 0.4706 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 12.76 | 0.4153 | 0.3268 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 16.63 | 0.6333 | 0.2002 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 14.67 | 0.4996 | 0.2492 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 15.09 | 0.5250 | 0.2389 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 15.04 | 0.5209 | 0.2359 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 9.59 | 0.3010 | 0.5144 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 10.68 | 0.3195 | 0.4195 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 16.58 | 0.6314 | 0.2001 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 14.67 | 0.4970 | 0.2486 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 15.04 | 0.5202 | 0.2398 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 15.08 | 0.5236 | 0.2362 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 9.60 | 0.3021 | 0.5153 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 10.69 | 0.3170 | 0.4197 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 16.34 | 0.6339 | 0.1880 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 13.42 | 0.4366 | 0.2597 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 14.28 | 0.4837 | 0.2456 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 8.85 | 0.3647 | 0.6603 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 8.84 | 0.3622 | 0.6578 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 11.34 | 0.3398 | 0.3590 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 16.33 | 0.6335 | 0.1892 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 13.42 | 0.4362 | 0.2602 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 14.26 | 0.4830 | 0.2469 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 8.86 | 0.3653 | 0.6598 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 8.84 | 0.3630 | 0.6566 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 11.35 | 0.3398 | 0.3595 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 16.55 | 0.6465 | 0.1971 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 14.83 | 0.5223 | 0.2455 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 15.06 | 0.5402 | 0.2387 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 15.02 | 0.5362 | 0.2340 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 10.20 | 0.3444 | 0.4717 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 11.23 | 0.3727 | 0.3840 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 16.51 | 0.6449 | 0.1964 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 14.84 | 0.5196 | 0.2451 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 15.03 | 0.5365 | 0.2392 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 15.06 | 0.5387 | 0.2341 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 10.21 | 0.3454 | 0.4724 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 11.24 | 0.3705 | 0.3835 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 16.52 | 0.6579 | 0.1887 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 13.66 | 0.4779 | 0.2572 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 14.52 | 0.5219 | 0.2444 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 9.62 | 0.3936 | 0.5734 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 9.62 | 0.3923 | 0.5746 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 11.68 | 0.3657 | 0.3476 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 16.50 | 0.6578 | 0.1898 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 13.66 | 0.4774 | 0.2580 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 14.51 | 0.5212 | 0.2454 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 9.63 | 0.3944 | 0.5733 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 9.62 | 0.3928 | 0.5736 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 11.69 | 0.3656 | 0.3479 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 14.17 | 0.5985 | 0.0457 | 1.00 |
| flow_s0.5_pose | 13.30 | 0.5443 | 0.0482 | 1.00 |
| flow_s0.5_posecal | 12.44 | 0.4831 | 0.0623 | 1.00 |
| flow_s0.5_uniform | 13.88 | 0.5654 | 0.0513 | 1.00 |
| flow_s1.0_oracle | 13.03 | 0.5914 | 0.0498 | 1.00 |
| flow_s1.0_pose | 12.70 | 0.5482 | 0.0513 | 1.00 |
| flow_s1.0_posecal | 12.32 | 0.5219 | 0.0627 | 1.00 |
| flow_s1.0_uniform | 12.52 | 0.5342 | 0.0568 | 1.00 |
| gs_center448_nat_dil | 13.36 | 0.4388 | 0.1074 | 1.00 |
| gs_center448_nat_dil+reg | 18.17 | 0.7031 | 0.0505 | 1.00 |
| gs_center448_nat_dil_cal | 10.32 | 0.2849 | 0.1572 | 1.00 |
| gs_center448_nat_dil_cal+reg | 17.07 | 0.6461 | 0.0543 | 1.00 |
| gs_center448_nat_dil_calK | 9.44 | 0.2473 | 0.1697 | 1.00 |
| gs_center448_nat_dil_calK+reg | 16.58 | 0.6330 | 0.0600 | 0.98 |
| gs_center448_nat_mip | 13.36 | 0.4358 | 0.1075 | 1.00 |
| gs_center448_nat_mip+reg | 18.03 | 0.7003 | 0.0517 | 1.00 |
| gs_center448_nat_mip_cal | 10.31 | 0.2832 | 0.1575 | 1.00 |
| gs_center448_nat_mip_cal+reg | 16.95 | 0.6423 | 0.0555 | 1.00 |
| gs_center448_nat_mip_calK | 9.44 | 0.2480 | 0.1697 | 1.00 |
| gs_center448_nat_mip_calK+reg | 16.65 | 0.6358 | 0.0595 | 0.98 |
| gs_roi448_nat_dil | 12.74 | 0.3870 | 0.1605 | 0.83 |
| gs_roi448_nat_dil+reg | 17.30 | 0.6675 | 0.0818 | 0.83 |
| gs_roi448_nat_dil_cal | 9.95 | 0.2568 | 0.2267 | 0.83 |
| gs_roi448_nat_dil_cal+reg | 15.69 | 0.5855 | 0.0859 | 0.84 |
| gs_roi448_nat_dil_calK | 8.59 | 0.2957 | 0.2685 | 0.83 |
| gs_roi448_nat_dil_calK+reg | 8.69 | 0.2993 | 0.2426 | 0.86 |
| gs_roi448_nat_mip | 12.74 | 0.3871 | 0.1605 | 0.83 |
| gs_roi448_nat_mip+reg | 17.28 | 0.6668 | 0.0821 | 0.83 |
| gs_roi448_nat_mip_cal | 9.96 | 0.2568 | 0.2265 | 0.83 |
| gs_roi448_nat_mip_cal+reg | 15.66 | 0.5846 | 0.0864 | 0.84 |
| gs_roi448_nat_mip_calK | 8.59 | 0.2960 | 0.2684 | 0.83 |
| gs_roi448_nat_mip_calK+reg | 8.70 | 0.2984 | 0.2423 | 0.86 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 18.18 | 0.6966 | 0.0503 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 13.36 | 0.4521 | 0.1074 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 17.08 | 0.6407 | 0.0541 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 16.63 | 0.6280 | 0.0579 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 9.44 | 0.2639 | 0.1697 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 10.32 | 0.2854 | 0.1572 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 18.04 | 0.6928 | 0.0515 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 13.36 | 0.4488 | 0.1075 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 16.95 | 0.6362 | 0.0552 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 16.69 | 0.6308 | 0.0574 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 9.44 | 0.2646 | 0.1697 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 10.31 | 0.2836 | 0.1575 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 17.63 | 0.6815 | 0.0464 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 13.32 | 0.4469 | 0.0842 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 16.16 | 0.6135 | 0.0519 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 9.31 | 0.3429 | 0.1401 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 9.34 | 0.3530 | 0.1330 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 10.72 | 0.3477 | 0.1128 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 17.61 | 0.6807 | 0.0465 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 13.33 | 0.4470 | 0.0841 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 16.13 | 0.6127 | 0.0522 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 9.32 | 0.3423 | 0.1399 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 9.34 | 0.3531 | 0.1330 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 10.73 | 0.3478 | 0.1127 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 17.40 | 0.6920 | 0.0512 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 13.47 | 0.4545 | 0.1006 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 16.46 | 0.6372 | 0.0549 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 16.09 | 0.6272 | 0.0584 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 9.64 | 0.2699 | 0.1606 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 10.51 | 0.3100 | 0.1477 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 17.29 | 0.6897 | 0.0523 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 13.47 | 0.4518 | 0.1008 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 16.36 | 0.6339 | 0.0558 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 16.14 | 0.6298 | 0.0580 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 9.64 | 0.2705 | 0.1606 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 10.50 | 0.3083 | 0.1479 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 17.05 | 0.6736 | 0.0469 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 13.21 | 0.4571 | 0.0813 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 15.77 | 0.6112 | 0.0521 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 9.40 | 0.3777 | 0.1344 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 9.40 | 0.3864 | 0.1285 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 10.93 | 0.3600 | 0.1085 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 17.03 | 0.6729 | 0.0470 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 13.21 | 0.4572 | 0.0812 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 15.74 | 0.6104 | 0.0523 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 9.40 | 0.3770 | 0.1343 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 9.40 | 0.3866 | 0.1285 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 10.94 | 0.3600 | 0.1085 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 17.03 | 0.6907 | 0.0460 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 14.35 | 0.5326 | 0.0693 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 16.19 | 0.6401 | 0.0495 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 16.03 | 0.6339 | 0.0504 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 10.87 | 0.3868 | 0.1098 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 11.41 | 0.4189 | 0.0987 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 16.95 | 0.6886 | 0.0464 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 14.35 | 0.5303 | 0.0694 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 16.13 | 0.6370 | 0.0499 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 16.07 | 0.6362 | 0.0502 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 10.87 | 0.3872 | 0.1099 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 11.41 | 0.4178 | 0.0987 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 16.93 | 0.6847 | 0.0417 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 13.87 | 0.5215 | 0.0592 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 15.62 | 0.6203 | 0.0471 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 10.16 | 0.4566 | 0.1011 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 10.12 | 0.4624 | 0.0984 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 11.80 | 0.4340 | 0.0776 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 16.92 | 0.6842 | 0.0417 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 13.88 | 0.5215 | 0.0592 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 15.59 | 0.6197 | 0.0473 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 10.16 | 0.4561 | 0.1009 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 10.12 | 0.4626 | 0.0983 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 11.81 | 0.4340 | 0.0776 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.99 | 0.8166 | 0.0498 | 1.00 |
| flow_s0.5_pose | 19.41 | 0.8102 | 0.0518 | 1.00 |
| flow_s0.5_posecal | 18.06 | 0.7574 | 0.0623 | 1.00 |
| flow_s0.5_uniform | 19.42 | 0.7885 | 0.0548 | 1.00 |
| flow_s1.0_oracle | 19.19 | 0.8296 | 0.0544 | 1.00 |
| flow_s1.0_pose | 18.94 | 0.8220 | 0.0548 | 1.00 |
| flow_s1.0_posecal | 18.08 | 0.7714 | 0.0631 | 1.00 |
| flow_s1.0_uniform | 18.45 | 0.7883 | 0.0601 | 1.00 |
| gs_center448_nat_dil | 14.69 | 0.5230 | 0.1737 | 1.00 |
| gs_center448_nat_dil+reg | 21.80 | 0.7912 | 0.0747 | 0.99 |
| gs_center448_nat_dil_cal | 11.31 | 0.4188 | 0.2634 | 1.00 |
| gs_center448_nat_dil_cal+reg | 20.83 | 0.7660 | 0.0779 | 0.99 |
| gs_center448_nat_dil_calK | 9.23 | 0.3711 | 0.3194 | 1.00 |
| gs_center448_nat_dil_calK+reg | 20.35 | 0.7549 | 0.0810 | 0.96 |
| gs_center448_nat_mip | 14.73 | 0.5215 | 0.1726 | 1.00 |
| gs_center448_nat_mip+reg | 21.70 | 0.7902 | 0.0743 | 0.99 |
| gs_center448_nat_mip_cal | 11.33 | 0.4175 | 0.2629 | 1.00 |
| gs_center448_nat_mip_cal+reg | 20.72 | 0.7636 | 0.0776 | 0.99 |
| gs_center448_nat_mip_calK | 9.23 | 0.3720 | 0.3198 | 1.00 |
| gs_center448_nat_mip_calK+reg | 20.42 | 0.7573 | 0.0811 | 0.96 |
| gs_roi448_nat_dil | 14.55 | 0.5150 | 0.1984 | 0.69 |
| gs_roi448_nat_dil+reg | 19.51 | 0.7345 | 0.1090 | 0.69 |
| gs_roi448_nat_dil_cal | 10.78 | 0.3906 | 0.3120 | 0.69 |
| gs_roi448_nat_dil_cal+reg | 18.53 | 0.7167 | 0.1101 | 0.70 |
| gs_roi448_nat_dil_calK | 9.09 | 0.4075 | 0.4339 | 0.69 |
| gs_roi448_nat_dil_calK+reg | 9.52 | 0.4213 | 0.3970 | 0.74 |
| gs_roi448_nat_mip | 14.56 | 0.5151 | 0.1986 | 0.69 |
| gs_roi448_nat_mip+reg | 19.51 | 0.7347 | 0.1093 | 0.69 |
| gs_roi448_nat_mip_cal | 10.79 | 0.3907 | 0.3120 | 0.69 |
| gs_roi448_nat_mip_cal+reg | 18.50 | 0.7158 | 0.1111 | 0.70 |
| gs_roi448_nat_mip_calK | 9.09 | 0.4081 | 0.4339 | 0.69 |
| gs_roi448_nat_mip_calK+reg | 9.52 | 0.4212 | 0.3972 | 0.74 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 23.16 | 0.8493 | 0.0540 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 19.53 | 0.7763 | 0.0812 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 22.36 | 0.8339 | 0.0563 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 22.07 | 0.8301 | 0.0581 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 15.78 | 0.6973 | 0.1256 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 16.68 | 0.7098 | 0.1174 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 23.08 | 0.8480 | 0.0546 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 19.54 | 0.7754 | 0.0814 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 22.28 | 0.8323 | 0.0567 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 22.12 | 0.8309 | 0.0580 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 15.78 | 0.6974 | 0.1256 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 16.68 | 0.7094 | 0.1175 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 22.70 | 0.8463 | 0.0497 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 19.40 | 0.7873 | 0.0703 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 21.58 | 0.8279 | 0.0533 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 15.71 | 0.7333 | 0.1150 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 15.69 | 0.7358 | 0.1105 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 17.14 | 0.7492 | 0.0909 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 22.69 | 0.8460 | 0.0498 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 19.41 | 0.7874 | 0.0703 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 21.57 | 0.8276 | 0.0535 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 15.71 | 0.7332 | 0.1148 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 15.69 | 0.7359 | 0.1104 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 17.15 | 0.7493 | 0.0909 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 21.83 | 0.7904 | 0.0748 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 14.69 | 0.5205 | 0.1737 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 20.85 | 0.7653 | 0.0783 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 20.48 | 0.7586 | 0.0802 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 9.23 | 0.3518 | 0.3195 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 11.31 | 0.4067 | 0.2634 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 21.74 | 0.7894 | 0.0744 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 14.73 | 0.5191 | 0.1728 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 20.74 | 0.7629 | 0.0780 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 20.55 | 0.7608 | 0.0801 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 9.23 | 0.3527 | 0.3199 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 11.33 | 0.4056 | 0.2631 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 21.00 | 0.7857 | 0.0708 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 16.13 | 0.6290 | 0.1234 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 20.16 | 0.7708 | 0.0727 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 10.78 | 0.5273 | 0.2586 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 10.66 | 0.5436 | 0.2435 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 12.42 | 0.5432 | 0.1790 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 20.99 | 0.7857 | 0.0709 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 16.14 | 0.6291 | 0.1235 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 20.15 | 0.7703 | 0.0732 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 10.78 | 0.5268 | 0.2591 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 10.66 | 0.5439 | 0.2434 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 12.43 | 0.5433 | 0.1790 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 22.63 | 0.8437 | 0.0501 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 18.56 | 0.7508 | 0.0718 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 21.62 | 0.8239 | 0.0532 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 21.53 | 0.8224 | 0.0530 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 13.67 | 0.6499 | 0.1309 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 15.09 | 0.6791 | 0.1117 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 22.57 | 0.8429 | 0.0500 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 18.60 | 0.7502 | 0.0715 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 21.57 | 0.8225 | 0.0531 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 21.57 | 0.8235 | 0.0529 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 13.67 | 0.6502 | 0.1311 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 15.10 | 0.6784 | 0.1116 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 22.30 | 0.8446 | 0.0460 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 18.92 | 0.7739 | 0.0622 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 21.09 | 0.8247 | 0.0502 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 14.06 | 0.7139 | 0.1282 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 13.99 | 0.7146 | 0.1253 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 15.83 | 0.7164 | 0.0907 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 22.29 | 0.8446 | 0.0461 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 18.93 | 0.7740 | 0.0622 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 21.07 | 0.8244 | 0.0504 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 14.06 | 0.7140 | 0.1282 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 13.99 | 0.7148 | 0.1253 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 15.84 | 0.7165 | 0.0907 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 21.88 | 0.8768 | 0.0597 | 1.00 |
| flow_s0.5_pose | 21.24 | 0.8722 | 0.0608 | 1.00 |
| flow_s0.5_posecal | 20.21 | 0.8389 | 0.0732 | 1.00 |
| flow_s0.5_uniform | 21.45 | 0.8596 | 0.0657 | 1.00 |
| flow_s1.0_oracle | 21.12 | 0.8872 | 0.0601 | 1.00 |
| flow_s1.0_pose | 20.84 | 0.8820 | 0.0609 | 1.00 |
| flow_s1.0_posecal | 20.19 | 0.8497 | 0.0716 | 1.00 |
| flow_s1.0_uniform | 20.48 | 0.8603 | 0.0677 | 1.00 |
| gs_center448_nat_dil | 17.20 | 0.6197 | 0.1972 | 1.00 |
| gs_center448_nat_dil+reg | 23.67 | 0.8484 | 0.0903 | 0.98 |
| gs_center448_nat_dil_cal | 12.64 | 0.5038 | 0.2984 | 1.00 |
| gs_center448_nat_dil_cal+reg | 22.76 | 0.8330 | 0.0948 | 0.98 |
| gs_center448_nat_dil_calK | 10.03 | 0.4694 | 0.3434 | 1.00 |
| gs_center448_nat_dil_calK+reg | 21.97 | 0.8195 | 0.1007 | 0.93 |
| gs_center448_nat_mip | 17.21 | 0.6176 | 0.1969 | 1.00 |
| gs_center448_nat_mip+reg | 23.50 | 0.8470 | 0.0915 | 0.98 |
| gs_center448_nat_mip_cal | 12.62 | 0.5020 | 0.2985 | 1.00 |
| gs_center448_nat_mip_cal+reg | 22.59 | 0.8305 | 0.0959 | 0.98 |
| gs_center448_nat_mip_calK | 10.03 | 0.4705 | 0.3436 | 1.00 |
| gs_center448_nat_mip_calK+reg | 22.06 | 0.8217 | 0.1002 | 0.93 |
| gs_roi448_nat_dil | 15.82 | 0.5813 | 0.2237 | 0.54 |
| gs_roi448_nat_dil+reg | 20.49 | 0.7754 | 0.1274 | 0.54 |
| gs_roi448_nat_dil_cal | 11.74 | 0.4467 | 0.3193 | 0.54 |
| gs_roi448_nat_dil_cal+reg | 19.38 | 0.7708 | 0.1286 | 0.55 |
| gs_roi448_nat_dil_calK | 8.94 | 0.4311 | 0.4788 | 0.54 |
| gs_roi448_nat_dil_calK+reg | 9.38 | 0.4507 | 0.4408 | 0.61 |
| gs_roi448_nat_mip | 15.81 | 0.5812 | 0.2239 | 0.54 |
| gs_roi448_nat_mip+reg | 20.46 | 0.7755 | 0.1273 | 0.54 |
| gs_roi448_nat_mip_cal | 11.74 | 0.4467 | 0.3194 | 0.54 |
| gs_roi448_nat_mip_cal+reg | 19.34 | 0.7700 | 0.1303 | 0.55 |
| gs_roi448_nat_mip_calK | 8.95 | 0.4316 | 0.4786 | 0.54 |
| gs_roi448_nat_mip_calK+reg | 9.39 | 0.4507 | 0.4413 | 0.61 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 25.45 | 0.9010 | 0.0576 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 21.81 | 0.8553 | 0.0867 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 24.59 | 0.8921 | 0.0606 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 24.21 | 0.8902 | 0.0626 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 17.77 | 0.8082 | 0.1254 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 18.74 | 0.8154 | 0.1192 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 25.33 | 0.9003 | 0.0582 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 21.82 | 0.8548 | 0.0868 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 24.48 | 0.8912 | 0.0611 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 24.27 | 0.8906 | 0.0624 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 17.77 | 0.8083 | 0.1254 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 18.73 | 0.8151 | 0.1195 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 25.06 | 0.8992 | 0.0549 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 21.77 | 0.8629 | 0.0759 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 23.81 | 0.8895 | 0.0594 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 17.67 | 0.8316 | 0.1115 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 17.65 | 0.8338 | 0.1074 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 19.28 | 0.8411 | 0.0922 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 25.05 | 0.8991 | 0.0549 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 21.78 | 0.8630 | 0.0758 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 23.79 | 0.8893 | 0.0595 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 17.68 | 0.8316 | 0.1113 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 17.66 | 0.8339 | 0.1073 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 19.29 | 0.8412 | 0.0922 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 23.71 | 0.8675 | 0.0768 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 18.26 | 0.7250 | 0.1421 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 22.82 | 0.8535 | 0.0807 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 22.39 | 0.8499 | 0.0841 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 12.39 | 0.6174 | 0.2384 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 14.55 | 0.6464 | 0.2087 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 23.58 | 0.8668 | 0.0774 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 18.28 | 0.7238 | 0.1418 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 22.69 | 0.8519 | 0.0812 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 22.46 | 0.8512 | 0.0839 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 12.39 | 0.6179 | 0.2384 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 14.54 | 0.6455 | 0.2086 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 23.38 | 0.8666 | 0.0715 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 19.13 | 0.7807 | 0.1143 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 22.37 | 0.8580 | 0.0765 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 13.17 | 0.7039 | 0.2078 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 13.05 | 0.7169 | 0.2015 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 15.84 | 0.7344 | 0.1481 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 23.36 | 0.8666 | 0.0715 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 19.13 | 0.7807 | 0.1144 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 22.34 | 0.8577 | 0.0768 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 13.18 | 0.7036 | 0.2080 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 13.05 | 0.7170 | 0.2015 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 15.84 | 0.7344 | 0.1481 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 24.21 | 0.8943 | 0.0590 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 20.99 | 0.8447 | 0.0792 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 23.34 | 0.8837 | 0.0621 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 23.17 | 0.8826 | 0.0624 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 16.13 | 0.7875 | 0.1231 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 17.67 | 0.8060 | 0.1096 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 24.12 | 0.8938 | 0.0592 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 21.02 | 0.8442 | 0.0791 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 23.26 | 0.8827 | 0.0622 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 23.22 | 0.8833 | 0.0624 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 16.13 | 0.7877 | 0.1231 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 17.66 | 0.8055 | 0.1096 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 24.10 | 0.8947 | 0.0547 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 21.04 | 0.8546 | 0.0714 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 22.95 | 0.8845 | 0.0606 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 16.13 | 0.8180 | 0.1216 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 16.08 | 0.8194 | 0.1193 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 18.43 | 0.8279 | 0.0912 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 24.09 | 0.8946 | 0.0548 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 21.05 | 0.8546 | 0.0713 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 22.92 | 0.8843 | 0.0607 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 16.13 | 0.8179 | 0.1214 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 16.08 | 0.8195 | 0.1192 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 18.43 | 0.8278 | 0.0912 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 32.45 | 0.9592 | 0.0262 | 1.00 |
| flow_s0.5_pose | 32.82 | 0.9610 | 0.0252 | 1.00 |
| flow_s0.5_posecal | 31.26 | 0.9444 | 0.0302 | 1.00 |
| flow_s0.5_uniform | 32.06 | 0.9533 | 0.0285 | 1.00 |
| flow_s1.0_oracle | 33.41 | 0.9610 | 0.0236 | 1.00 |
| flow_s1.0_pose | 33.53 | 0.9618 | 0.0233 | 1.00 |
| flow_s1.0_posecal | 31.83 | 0.9464 | 0.0279 | 1.00 |
| flow_s1.0_uniform | 32.36 | 0.9509 | 0.0269 | 1.00 |
| gs_center448_nat_dil | 19.47 | 0.7267 | 0.1604 | 1.00 |
| gs_center448_nat_dil+reg | 29.26 | 0.9220 | 0.0616 | 0.98 |
| gs_center448_nat_dil_cal | 14.47 | 0.6178 | 0.2646 | 1.00 |
| gs_center448_nat_dil_cal+reg | 29.22 | 0.9210 | 0.0625 | 0.98 |
| gs_center448_nat_dil_calK | 10.77 | 0.5822 | 0.3198 | 1.00 |
| gs_center448_nat_dil_calK+reg | 28.29 | 0.9158 | 0.0642 | 0.91 |
| gs_center448_nat_mip | 19.43 | 0.7246 | 0.1601 | 1.00 |
| gs_center448_nat_mip+reg | 29.03 | 0.9209 | 0.0617 | 0.98 |
| gs_center448_nat_mip_cal | 14.45 | 0.6156 | 0.2645 | 1.00 |
| gs_center448_nat_mip_cal+reg | 28.95 | 0.9195 | 0.0630 | 0.98 |
| gs_center448_nat_mip_calK | 10.78 | 0.5835 | 0.3202 | 1.00 |
| gs_center448_nat_mip_calK+reg | 28.44 | 0.9173 | 0.0641 | 0.91 |
| gs_roi448_nat_dil | 18.91 | 0.7283 | 0.1676 | 0.45 |
| gs_roi448_nat_dil+reg | 23.22 | 0.8488 | 0.0885 | 0.44 |
| gs_roi448_nat_dil_cal | 13.75 | 0.6046 | 0.2546 | 0.45 |
| gs_roi448_nat_dil_cal+reg | 24.59 | 0.8888 | 0.0814 | 0.46 |
| gs_roi448_nat_dil_calK | 9.34 | 0.5013 | 0.4224 | 0.45 |
| gs_roi448_nat_dil_calK+reg | 9.81 | 0.5340 | 0.3936 | 0.53 |
| gs_roi448_nat_mip | 18.90 | 0.7280 | 0.1680 | 0.45 |
| gs_roi448_nat_mip+reg | 23.20 | 0.8487 | 0.0883 | 0.44 |
| gs_roi448_nat_mip_cal | 13.75 | 0.6046 | 0.2547 | 0.45 |
| gs_roi448_nat_mip_cal+reg | 24.53 | 0.8880 | 0.0823 | 0.46 |
| gs_roi448_nat_mip_calK | 9.34 | 0.5020 | 0.4224 | 0.45 |
| gs_roi448_nat_mip_calK+reg | 9.81 | 0.5342 | 0.3947 | 0.53 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 33.53 | 0.9610 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 33.30 | 0.9590 | 0.0267 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 33.54 | 0.9611 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 33.53 | 0.9610 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 32.64 | 0.9578 | 0.0303 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 32.86 | 0.9574 | 0.0299 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 33.53 | 0.9610 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 33.30 | 0.9590 | 0.0267 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 33.54 | 0.9611 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 33.53 | 0.9610 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 32.64 | 0.9578 | 0.0303 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 32.87 | 0.9574 | 0.0299 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 33.49 | 0.9611 | 0.0237 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 33.24 | 0.9599 | 0.0264 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 33.52 | 0.9612 | 0.0236 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 33.01 | 0.9587 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 33.12 | 0.9591 | 0.0274 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 33.00 | 0.9593 | 0.0276 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 33.49 | 0.9611 | 0.0237 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 33.24 | 0.9599 | 0.0263 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 33.52 | 0.9612 | 0.0236 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 33.01 | 0.9587 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 33.12 | 0.9591 | 0.0274 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 33.00 | 0.9593 | 0.0275 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 33.47 | 0.9578 | 0.0240 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 31.83 | 0.9381 | 0.0491 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 33.45 | 0.9575 | 0.0242 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 33.42 | 0.9571 | 0.0247 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 27.62 | 0.9072 | 0.1119 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 29.63 | 0.9156 | 0.0930 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 33.46 | 0.9576 | 0.0241 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 31.83 | 0.9379 | 0.0493 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 33.44 | 0.9573 | 0.0244 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 33.43 | 0.9573 | 0.0246 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 27.61 | 0.9072 | 0.1118 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 29.63 | 0.9155 | 0.0931 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 33.20 | 0.9570 | 0.0273 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 32.35 | 0.9461 | 0.0450 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 33.38 | 0.9577 | 0.0265 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 29.14 | 0.9200 | 0.0938 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 29.14 | 0.9233 | 0.0911 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 30.48 | 0.9362 | 0.0641 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 33.20 | 0.9570 | 0.0273 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 32.35 | 0.9460 | 0.0450 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 33.37 | 0.9576 | 0.0266 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 29.13 | 0.9199 | 0.0940 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 29.14 | 0.9233 | 0.0911 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 30.49 | 0.9362 | 0.0641 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 33.41 | 0.9600 | 0.0249 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 33.47 | 0.9604 | 0.0246 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 33.41 | 0.9600 | 0.0249 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 33.47 | 0.9604 | 0.0246 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 33.46 | 0.9602 | 0.0251 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 33.47 | 0.9604 | 0.0249 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 33.51 | 0.9612 | 0.0239 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 33.53 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 33.46 | 0.9602 | 0.0251 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 33.47 | 0.9604 | 0.0249 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 33.51 | 0.9612 | 0.0239 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.53 | 0.9074 | 0.0593 | 1.00 |
| flow_s0.5_pose | 22.93 | 0.9061 | 0.0610 | 1.00 |
| flow_s0.5_posecal | 21.89 | 0.8775 | 0.0712 | 1.00 |
| flow_s0.5_uniform | 23.08 | 0.8944 | 0.0652 | 1.00 |
| flow_s1.0_oracle | 22.88 | 0.9145 | 0.0621 | 1.00 |
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| flow_s1.0_posecal | 21.96 | 0.8841 | 0.0708 | 1.00 |
| flow_s1.0_uniform | 22.18 | 0.8935 | 0.0691 | 1.00 |
| gs_center448_nat_dil | 17.36 | 0.6559 | 0.1833 | 1.00 |
| gs_center448_nat_dil+reg | 24.92 | 0.8756 | 0.1087 | 0.98 |
| gs_center448_nat_dil_cal | 12.95 | 0.5442 | 0.3149 | 1.00 |
| gs_center448_nat_dil_cal+reg | 24.11 | 0.8662 | 0.1123 | 0.98 |
| gs_center448_nat_dil_calK | 10.01 | 0.5058 | 0.3841 | 1.00 |
| gs_center448_nat_dil_calK+reg | 23.39 | 0.8572 | 0.1137 | 0.93 |
| gs_center448_nat_mip | 17.34 | 0.6536 | 0.1813 | 1.00 |
| gs_center448_nat_mip+reg | 24.75 | 0.8743 | 0.1076 | 0.98 |
| gs_center448_nat_mip_cal | 12.93 | 0.5421 | 0.3135 | 1.00 |
| gs_center448_nat_mip_cal+reg | 23.94 | 0.8642 | 0.1111 | 0.98 |
| gs_center448_nat_mip_calK | 10.01 | 0.5070 | 0.3856 | 1.00 |
| gs_center448_nat_mip_calK+reg | 23.49 | 0.8591 | 0.1145 | 0.93 |
| gs_roi448_nat_dil | 16.15 | 0.6237 | 0.2129 | 0.54 |
| gs_roi448_nat_dil+reg | 21.01 | 0.7959 | 0.1430 | 0.53 |
| gs_roi448_nat_dil_cal | 12.04 | 0.5031 | 0.3241 | 0.54 |
| gs_roi448_nat_dil_cal+reg | 20.55 | 0.8107 | 0.1478 | 0.55 |
| gs_roi448_nat_dil_calK | 9.01 | 0.4455 | 0.6048 | 0.54 |
| gs_roi448_nat_dil_calK+reg | 9.49 | 0.4744 | 0.5564 | 0.61 |
| gs_roi448_nat_mip | 16.14 | 0.6235 | 0.2132 | 0.54 |
| gs_roi448_nat_mip+reg | 20.99 | 0.7958 | 0.1427 | 0.53 |
| gs_roi448_nat_mip_cal | 12.04 | 0.5031 | 0.3243 | 0.54 |
| gs_roi448_nat_mip_cal+reg | 20.51 | 0.8099 | 0.1492 | 0.55 |
| gs_roi448_nat_mip_calK | 9.01 | 0.4461 | 0.6058 | 0.54 |
| gs_roi448_nat_mip_calK+reg | 9.49 | 0.4745 | 0.5583 | 0.61 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 26.85 | 0.9233 | 0.0606 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 23.22 | 0.8920 | 0.0931 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 26.06 | 0.9173 | 0.0634 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 25.73 | 0.9160 | 0.0655 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 19.46 | 0.8611 | 0.1382 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 20.45 | 0.8657 | 0.1300 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 26.75 | 0.9228 | 0.0613 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 23.22 | 0.8917 | 0.0932 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 25.96 | 0.9167 | 0.0639 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 25.78 | 0.9163 | 0.0654 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 19.46 | 0.8612 | 0.1382 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 20.44 | 0.8655 | 0.1301 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 26.42 | 0.9220 | 0.0564 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 23.24 | 0.8974 | 0.0790 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 25.28 | 0.9150 | 0.0609 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 19.48 | 0.8761 | 0.1249 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 19.47 | 0.8774 | 0.1197 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 20.76 | 0.8810 | 0.1006 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 26.40 | 0.9220 | 0.0565 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 23.25 | 0.8974 | 0.0789 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 25.26 | 0.9149 | 0.0610 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 19.49 | 0.8761 | 0.1247 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 19.47 | 0.8774 | 0.1197 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 20.77 | 0.8810 | 0.1006 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 25.09 | 0.8986 | 0.0825 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 19.42 | 0.7957 | 0.1424 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 24.33 | 0.8899 | 0.0855 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 23.95 | 0.8875 | 0.0881 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 13.76 | 0.7167 | 0.2562 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 15.90 | 0.7394 | 0.2175 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 24.97 | 0.8979 | 0.0825 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 19.43 | 0.7948 | 0.1420 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 24.20 | 0.8887 | 0.0854 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 24.01 | 0.8884 | 0.0881 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 13.75 | 0.7171 | 0.2566 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 15.89 | 0.7387 | 0.2172 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 24.60 | 0.8965 | 0.0738 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 20.11 | 0.8324 | 0.1137 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 23.80 | 0.8918 | 0.0776 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 14.78 | 0.7754 | 0.2365 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 14.66 | 0.7830 | 0.2266 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 16.80 | 0.7970 | 0.1551 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 24.58 | 0.8965 | 0.0738 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 20.12 | 0.8324 | 0.1138 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 23.78 | 0.8915 | 0.0779 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 14.79 | 0.7752 | 0.2367 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 14.66 | 0.7831 | 0.2266 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 16.81 | 0.7970 | 0.1551 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 25.67 | 0.9193 | 0.0607 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 22.78 | 0.8882 | 0.0788 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 24.91 | 0.9124 | 0.0635 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 24.77 | 0.9117 | 0.0640 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 18.10 | 0.8503 | 0.1271 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 19.53 | 0.8615 | 0.1126 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 25.59 | 0.9189 | 0.0609 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 22.80 | 0.8878 | 0.0788 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 24.84 | 0.9118 | 0.0636 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 24.81 | 0.9121 | 0.0639 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 18.10 | 0.8504 | 0.1272 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 19.53 | 0.8612 | 0.1125 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 25.58 | 0.9197 | 0.0560 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 22.71 | 0.8943 | 0.0714 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 24.51 | 0.9127 | 0.0608 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 17.98 | 0.8688 | 0.1322 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 17.92 | 0.8691 | 0.1302 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 20.12 | 0.8744 | 0.0942 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 25.57 | 0.9197 | 0.0561 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 22.72 | 0.8943 | 0.0714 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 24.49 | 0.9125 | 0.0609 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 17.99 | 0.8688 | 0.1321 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 17.92 | 0.8692 | 0.1302 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 20.13 | 0.8744 | 0.0942 | 1.00 |

## 设置 cam5

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：vggt → `gs_roi448_nat_dil`，calib → `gs_center448_nat_mip_cal`，calibK → `gs_center448_nat_mip_calK`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=3.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 16.39 / 0.1129 | 15.31 / 0.0249 | 30.29 / 0.0331 | 26.19 / 0.0440 |
| flow_s1.0_pose | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 | 28.00 / 0.0396 |
| flow_s1.0_posecal | 14.33 / 0.1964 | 14.05 / 0.0348 | 28.45 / 0.0441 | 24.59 / 0.0528 |
| flow_s0.5_pose | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 | 27.45 / 0.0415 |
| flow_s0.5_posecal | 13.87 / 0.1964 | 13.69 / 0.0365 | 28.38 / 0.0457 | 24.27 / 0.0560 |
| gs_roi448_nat_dil | 17.17 / 0.1534 | 14.07 / 0.0998 | 18.25 / 0.1702 | 17.31 / 0.1654 |
| gs_roi448_nat_dil+reg | 18.73 / 0.1363 | 17.71 / 0.0494 | 27.01 / 0.0799 | 24.68 / 0.1048 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 18.49 / 0.1329 | 14.63 / 0.0457 | 31.20 / 0.0334 | 26.50 / 0.0536 |
| hyb_risktuned[gs_roi448_nat_dil] | 19.89 / 0.1054 | 17.70 / 0.0239 | 31.45 / 0.0305 | 27.30 / 0.0436 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 20.13 / 0.1201 | 18.08 / 0.0241 | 31.45 / 0.0307 | 28.46 / 0.0433 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 20.81 / 0.0946 | 19.20 / 0.0186 | 31.46 / 0.0305 | 28.43 / 0.0406 |
| gs_center448_nat_mip_cal | 12.02 / 0.3730 | 11.02 / 0.0963 | 15.71 / 0.2486 | 14.83 / 0.2604 |
| gs_center448_nat_mip_cal+reg | 15.97 / 0.2177 | 15.72 / 0.0343 | 27.32 / 0.0749 | 24.75 / 0.0964 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 15.04 / 0.2547 | 11.02 / 0.0963 | 31.15 / 0.0360 | 23.95 / 0.0834 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 16.28 / 0.2181 | 14.22 / 0.0467 | 31.43 / 0.0318 | 24.14 / 0.0657 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 17.75 / 0.1752 | 15.72 / 0.0343 | 31.44 / 0.0308 | 27.27 / 0.0495 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 19.36 / 0.1299 | 17.62 / 0.0252 | 31.45 / 0.0306 | 27.53 / 0.0458 |
| gs_center448_nat_mip_calK | 9.79 / 0.5143 | 9.34 / 0.1085 | 10.95 / 0.3409 | 10.50 / 0.3654 |
| gs_center448_nat_mip_calK+reg | 16.00 / 0.2130 | 15.46 / 0.0373 | 26.99 / 0.0824 | 24.39 / 0.1044 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 13.17 / 0.3341 | 9.34 / 0.1085 | 30.73 / 0.0380 | 22.31 / 0.0929 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 13.78 / 0.3149 | 12.58 / 0.0557 | 31.33 / 0.0331 | 21.49 / 0.0777 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 17.75 / 0.1708 | 15.49 / 0.0360 | 31.44 / 0.0308 | 27.12 / 0.0510 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 19.26 / 0.1305 | 17.57 / 0.0252 | 31.45 / 0.0306 | 27.45 / 0.0460 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 22.32 | 0.8406 | 0.0684 | 1.00 |
| flow_s0.5_pose | 19.65 | 0.7479 | 0.0818 | 1.00 |
| flow_s0.5_posecal | 13.87 | 0.4627 | 0.1964 | 1.00 |
| flow_s0.5_uniform | 16.71 | 0.6135 | 0.1070 | 1.00 |
| flow_s1.0_oracle | 23.16 | 0.8541 | 0.0592 | 1.00 |
| flow_s1.0_pose | 20.41 | 0.7569 | 0.0721 | 1.00 |
| flow_s1.0_posecal | 14.33 | 0.4797 | 0.1964 | 1.00 |
| flow_s1.0_uniform | 16.39 | 0.5779 | 0.1129 | 1.00 |
| gs_center448_nat_dil | 17.12 | 0.6182 | 0.1762 | 1.00 |
| gs_center448_nat_dil+reg | 17.71 | 0.6472 | 0.1791 | 1.00 |
| gs_center448_nat_dil_cal | 12.02 | 0.3723 | 0.3746 | 1.00 |
| gs_center448_nat_dil_cal+reg | 16.06 | 0.5475 | 0.2179 | 1.00 |
| gs_center448_nat_dil_calK | 9.79 | 0.2944 | 0.5132 | 1.00 |
| gs_center448_nat_dil_calK+reg | 15.98 | 0.5416 | 0.2122 | 1.00 |
| gs_center448_nat_mip | 17.13 | 0.6169 | 0.1744 | 1.00 |
| gs_center448_nat_mip+reg | 17.73 | 0.6487 | 0.1758 | 1.00 |
| gs_center448_nat_mip_cal | 12.02 | 0.3705 | 0.3730 | 1.00 |
| gs_center448_nat_mip_cal+reg | 15.97 | 0.5414 | 0.2177 | 1.00 |
| gs_center448_nat_mip_calK | 9.79 | 0.2951 | 0.5143 | 1.00 |
| gs_center448_nat_mip_calK+reg | 16.00 | 0.5431 | 0.2130 | 1.00 |
| gs_roi448_nat_dil | 17.17 | 0.6323 | 0.1534 | 1.00 |
| gs_roi448_nat_dil+reg | 18.73 | 0.7122 | 0.1363 | 1.00 |
| gs_roi448_nat_dil_cal | 10.71 | 0.2610 | 0.3499 | 1.00 |
| gs_roi448_nat_dil_cal+reg | 16.68 | 0.5929 | 0.1779 | 1.00 |
| gs_roi448_nat_dil_calK | 8.96 | 0.3559 | 0.6690 | 1.00 |
| gs_roi448_nat_dil_calK+reg | 9.00 | 0.3503 | 0.6547 | 0.95 |
| gs_roi448_nat_mip | 17.16 | 0.6317 | 0.1537 | 1.00 |
| gs_roi448_nat_mip+reg | 18.49 | 0.7047 | 0.1385 | 1.00 |
| gs_roi448_nat_mip_cal | 10.72 | 0.2612 | 0.3495 | 1.00 |
| gs_roi448_nat_mip_cal+reg | 16.64 | 0.5920 | 0.1788 | 1.00 |
| gs_roi448_nat_mip_calK | 8.96 | 0.3565 | 0.6682 | 1.00 |
| gs_roi448_nat_mip_calK+reg | 9.00 | 0.3506 | 0.6546 | 0.95 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 19.42 | 0.7179 | 0.1439 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 19.08 | 0.6973 | 0.1454 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 17.85 | 0.6656 | 0.1745 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 17.73 | 0.6598 | 0.1707 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 13.17 | 0.4790 | 0.3340 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 15.03 | 0.5481 | 0.2551 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 19.44 | 0.7177 | 0.1428 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 19.08 | 0.6955 | 0.1452 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 17.75 | 0.6616 | 0.1752 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 17.75 | 0.6607 | 0.1708 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 13.17 | 0.4792 | 0.3341 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 15.04 | 0.5472 | 0.2547 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 20.13 | 0.7513 | 0.1201 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 18.49 | 0.6999 | 0.1329 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 18.63 | 0.6964 | 0.1510 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 13.12 | 0.4791 | 0.3354 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 12.79 | 0.4608 | 0.3443 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 14.04 | 0.4812 | 0.2790 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 19.96 | 0.7475 | 0.1222 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 18.48 | 0.6992 | 0.1332 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 18.60 | 0.6959 | 0.1519 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 13.12 | 0.4791 | 0.3354 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 12.79 | 0.4609 | 0.3441 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 14.05 | 0.4814 | 0.2789 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 18.23 | 0.6785 | 0.1658 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 17.59 | 0.6466 | 0.1647 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 16.77 | 0.6015 | 0.2046 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 16.68 | 0.5940 | 0.2008 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 10.78 | 0.3528 | 0.4498 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 13.01 | 0.4335 | 0.3180 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 18.25 | 0.6791 | 0.1625 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 17.61 | 0.6449 | 0.1628 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 16.69 | 0.5959 | 0.2057 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 16.70 | 0.5951 | 0.2016 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 10.78 | 0.3533 | 0.4504 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 13.02 | 0.4319 | 0.3166 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 19.23 | 0.7300 | 0.1255 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 17.77 | 0.6644 | 0.1464 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 17.35 | 0.6297 | 0.1762 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 10.37 | 0.3923 | 0.5269 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 10.26 | 0.3801 | 0.5326 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 11.56 | 0.3288 | 0.3379 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 19.02 | 0.7242 | 0.1275 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 17.76 | 0.6636 | 0.1467 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 17.32 | 0.6286 | 0.1776 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 10.37 | 0.3924 | 0.5270 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 10.26 | 0.3803 | 0.5322 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 11.58 | 0.3291 | 0.3374 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 20.17 | 0.7497 | 0.1161 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 19.64 | 0.7209 | 0.1161 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 19.44 | 0.7209 | 0.1283 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 19.25 | 0.7120 | 0.1300 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 13.78 | 0.5310 | 0.3146 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 16.26 | 0.6148 | 0.2191 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 20.19 | 0.7498 | 0.1138 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 19.67 | 0.7196 | 0.1146 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 19.36 | 0.7172 | 0.1299 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 19.26 | 0.7126 | 0.1305 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 13.78 | 0.5313 | 0.3149 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 16.28 | 0.6138 | 0.2181 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 20.81 | 0.7770 | 0.0946 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 19.89 | 0.7458 | 0.1054 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 19.35 | 0.7246 | 0.1193 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 13.73 | 0.5545 | 0.3624 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 13.58 | 0.5534 | 0.3668 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 14.71 | 0.5111 | 0.2401 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 20.67 | 0.7741 | 0.0958 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 19.88 | 0.7454 | 0.1054 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 19.31 | 0.7241 | 0.1205 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 13.73 | 0.5546 | 0.3628 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 13.58 | 0.5536 | 0.3666 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 14.73 | 0.5116 | 0.2398 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.18 | 0.7600 | 0.0171 | 1.00 |
| flow_s0.5_pose | 17.06 | 0.6711 | 0.0195 | 1.00 |
| flow_s0.5_posecal | 13.69 | 0.4565 | 0.0365 | 1.00 |
| flow_s0.5_uniform | 15.30 | 0.5755 | 0.0247 | 1.00 |
| flow_s1.0_oracle | 19.73 | 0.7659 | 0.0154 | 1.00 |
| flow_s1.0_pose | 17.62 | 0.6745 | 0.0175 | 1.00 |
| flow_s1.0_posecal | 14.05 | 0.4797 | 0.0348 | 1.00 |
| flow_s1.0_uniform | 15.31 | 0.5619 | 0.0249 | 1.00 |
| gs_center448_nat_dil | 16.33 | 0.5875 | 0.0383 | 1.00 |
| gs_center448_nat_dil+reg | 17.13 | 0.6551 | 0.0303 | 1.00 |
| gs_center448_nat_dil_cal | 11.02 | 0.2378 | 0.0960 | 1.00 |
| gs_center448_nat_dil_cal+reg | 15.76 | 0.5825 | 0.0344 | 1.00 |
| gs_center448_nat_dil_calK | 9.34 | 0.1525 | 0.1086 | 1.00 |
| gs_center448_nat_dil_calK+reg | 15.43 | 0.5755 | 0.0375 | 0.99 |
| gs_center448_nat_mip | 16.32 | 0.5869 | 0.0383 | 1.00 |
| gs_center448_nat_mip+reg | 17.12 | 0.6557 | 0.0305 | 1.00 |
| gs_center448_nat_mip_cal | 11.02 | 0.2363 | 0.0963 | 1.00 |
| gs_center448_nat_mip_cal+reg | 15.72 | 0.5814 | 0.0343 | 1.00 |
| gs_center448_nat_mip_calK | 9.34 | 0.1527 | 0.1085 | 1.00 |
| gs_center448_nat_mip_calK+reg | 15.46 | 0.5768 | 0.0373 | 0.99 |
| gs_roi448_nat_dil | 14.07 | 0.4843 | 0.0998 | 0.85 |
| gs_roi448_nat_dil+reg | 17.71 | 0.6863 | 0.0494 | 0.85 |
| gs_roi448_nat_dil_cal | 10.44 | 0.1503 | 0.1631 | 0.85 |
| gs_roi448_nat_dil_cal+reg | 15.87 | 0.5603 | 0.0574 | 0.87 |
| gs_roi448_nat_dil_calK | 8.86 | 0.1885 | 0.1925 | 0.85 |
| gs_roi448_nat_dil_calK+reg | 9.08 | 0.1999 | 0.1518 | 0.86 |
| gs_roi448_nat_mip | 14.07 | 0.4836 | 0.0997 | 0.85 |
| gs_roi448_nat_mip+reg | 17.55 | 0.6788 | 0.0505 | 0.85 |
| gs_roi448_nat_mip_cal | 10.46 | 0.1508 | 0.1629 | 0.85 |
| gs_roi448_nat_mip_cal+reg | 15.82 | 0.5583 | 0.0580 | 0.87 |
| gs_roi448_nat_mip_calK | 8.86 | 0.1887 | 0.1925 | 0.85 |
| gs_roi448_nat_mip_calK+reg | 9.08 | 0.2002 | 0.1518 | 0.86 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 17.13 | 0.6536 | 0.0303 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 16.33 | 0.5995 | 0.0383 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 15.76 | 0.5810 | 0.0344 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 15.45 | 0.5726 | 0.0361 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 9.34 | 0.1903 | 0.1086 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 11.02 | 0.2679 | 0.0960 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 17.12 | 0.6533 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 16.32 | 0.5973 | 0.0383 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 15.72 | 0.5797 | 0.0343 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 15.49 | 0.5739 | 0.0360 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 9.34 | 0.1904 | 0.1085 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 11.02 | 0.2667 | 0.0963 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 18.08 | 0.7072 | 0.0241 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 14.63 | 0.5403 | 0.0457 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 16.25 | 0.6011 | 0.0315 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 9.70 | 0.2822 | 0.0887 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 9.54 | 0.2729 | 0.0848 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 11.10 | 0.2905 | 0.0717 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 17.92 | 0.7012 | 0.0245 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 14.63 | 0.5395 | 0.0457 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 16.20 | 0.5992 | 0.0318 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 9.71 | 0.2823 | 0.0887 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 9.54 | 0.2730 | 0.0847 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 11.11 | 0.2909 | 0.0716 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 17.43 | 0.6706 | 0.0287 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 16.81 | 0.6242 | 0.0339 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 16.26 | 0.6084 | 0.0319 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 16.09 | 0.6084 | 0.0323 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 10.32 | 0.2713 | 0.0886 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 12.19 | 0.3360 | 0.0761 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 17.42 | 0.6708 | 0.0288 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 16.80 | 0.6230 | 0.0338 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 16.21 | 0.6075 | 0.0319 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 16.12 | 0.6093 | 0.0322 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 10.32 | 0.2714 | 0.0886 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 12.16 | 0.3346 | 0.0766 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 18.41 | 0.7223 | 0.0225 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 15.88 | 0.5963 | 0.0363 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 16.74 | 0.6177 | 0.0289 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 10.24 | 0.3570 | 0.0762 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 10.26 | 0.3614 | 0.0725 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 11.83 | 0.3320 | 0.0603 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 18.26 | 0.7163 | 0.0229 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 15.86 | 0.5956 | 0.0363 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 16.69 | 0.6162 | 0.0292 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 10.25 | 0.3571 | 0.0762 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 10.26 | 0.3616 | 0.0725 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 11.84 | 0.3322 | 0.0602 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 18.20 | 0.7055 | 0.0232 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 17.86 | 0.6761 | 0.0254 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 17.66 | 0.6707 | 0.0249 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 17.55 | 0.6667 | 0.0253 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 12.58 | 0.4569 | 0.0557 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 14.22 | 0.5089 | 0.0466 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 18.17 | 0.7044 | 0.0234 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 17.82 | 0.6742 | 0.0254 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 17.62 | 0.6690 | 0.0252 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 17.57 | 0.6673 | 0.0252 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 12.58 | 0.4569 | 0.0557 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 14.22 | 0.5085 | 0.0467 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 19.20 | 0.7421 | 0.0186 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 17.70 | 0.6694 | 0.0239 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 17.74 | 0.6663 | 0.0243 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 11.71 | 0.4884 | 0.0549 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 11.91 | 0.4913 | 0.0531 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 13.84 | 0.4730 | 0.0408 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 19.11 | 0.7384 | 0.0188 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 17.69 | 0.6691 | 0.0239 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 17.71 | 0.6656 | 0.0245 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 11.72 | 0.4884 | 0.0549 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 11.92 | 0.4913 | 0.0531 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 13.85 | 0.4731 | 0.0407 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 17.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.73 | 0.8826 | 0.0204 | 1.00 |
| flow_s0.5_pose | 22.21 | 0.8504 | 0.0224 | 1.00 |
| flow_s0.5_posecal | 18.48 | 0.7401 | 0.0379 | 1.00 |
| flow_s0.5_uniform | 20.55 | 0.8064 | 0.0266 | 1.00 |
| flow_s1.0_oracle | 24.76 | 0.8987 | 0.0188 | 1.00 |
| flow_s1.0_pose | 23.17 | 0.8669 | 0.0208 | 1.00 |
| flow_s1.0_posecal | 18.97 | 0.7548 | 0.0351 | 1.00 |
| flow_s1.0_uniform | 20.86 | 0.8093 | 0.0253 | 1.00 |
| gs_center448_nat_dil | 19.35 | 0.6943 | 0.0583 | 1.00 |
| gs_center448_nat_dil+reg | 20.98 | 0.7738 | 0.0460 | 1.00 |
| gs_center448_nat_dil_cal | 12.27 | 0.4009 | 0.1630 | 1.00 |
| gs_center448_nat_dil_cal+reg | 19.83 | 0.7376 | 0.0497 | 1.00 |
| gs_center448_nat_dil_calK | 9.06 | 0.3254 | 0.2134 | 1.00 |
| gs_center448_nat_dil_calK+reg | 19.69 | 0.7355 | 0.0503 | 0.97 |
| gs_center448_nat_mip | 19.41 | 0.6960 | 0.0572 | 1.00 |
| gs_center448_nat_mip+reg | 20.96 | 0.7758 | 0.0450 | 1.00 |
| gs_center448_nat_mip_cal | 12.24 | 0.3992 | 0.1630 | 1.00 |
| gs_center448_nat_mip_cal+reg | 19.83 | 0.7391 | 0.0483 | 1.00 |
| gs_center448_nat_mip_calK | 9.06 | 0.3258 | 0.2135 | 1.00 |
| gs_center448_nat_mip_calK+reg | 19.71 | 0.7360 | 0.0507 | 0.97 |
| gs_roi448_nat_dil | 16.30 | 0.5870 | 0.1270 | 0.73 |
| gs_roi448_nat_dil+reg | 21.13 | 0.7897 | 0.0601 | 0.75 |
| gs_roi448_nat_dil_cal | 10.70 | 0.3366 | 0.2531 | 0.73 |
| gs_roi448_nat_dil_cal+reg | 19.33 | 0.7249 | 0.0637 | 0.76 |
| gs_roi448_nat_dil_calK | 9.32 | 0.3909 | 0.3278 | 0.73 |
| gs_roi448_nat_dil_calK+reg | 9.56 | 0.3962 | 0.2704 | 0.79 |
| gs_roi448_nat_mip | 16.30 | 0.5870 | 0.1270 | 0.73 |
| gs_roi448_nat_mip+reg | 20.99 | 0.7876 | 0.0606 | 0.75 |
| gs_roi448_nat_mip_cal | 10.72 | 0.3374 | 0.2529 | 0.73 |
| gs_roi448_nat_mip_cal+reg | 19.27 | 0.7241 | 0.0645 | 0.76 |
| gs_roi448_nat_mip_calK | 9.32 | 0.3914 | 0.3277 | 0.73 |
| gs_roi448_nat_mip_calK+reg | 9.56 | 0.3968 | 0.2703 | 0.79 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 23.12 | 0.8567 | 0.0276 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 22.54 | 0.8414 | 0.0302 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 22.14 | 0.8423 | 0.0299 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 21.99 | 0.8404 | 0.0297 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 16.43 | 0.7108 | 0.0679 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 18.28 | 0.7444 | 0.0579 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 23.12 | 0.8564 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 22.54 | 0.8407 | 0.0302 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 22.09 | 0.8421 | 0.0296 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 22.02 | 0.8407 | 0.0298 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 16.43 | 0.7109 | 0.0679 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 18.25 | 0.7437 | 0.0582 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 23.91 | 0.8724 | 0.0235 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 21.78 | 0.8329 | 0.0317 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 22.49 | 0.8481 | 0.0266 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 16.39 | 0.7316 | 0.0620 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 16.41 | 0.7331 | 0.0603 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 17.86 | 0.7490 | 0.0493 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 23.79 | 0.8711 | 0.0237 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 21.77 | 0.8325 | 0.0317 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 22.44 | 0.8475 | 0.0268 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 16.40 | 0.7316 | 0.0620 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 16.41 | 0.7331 | 0.0603 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 17.87 | 0.7491 | 0.0493 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 20.99 | 0.7737 | 0.0460 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 19.35 | 0.6946 | 0.0583 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 19.83 | 0.7371 | 0.0497 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 19.78 | 0.7404 | 0.0488 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 9.06 | 0.2982 | 0.2133 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 12.27 | 0.3867 | 0.1630 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 20.97 | 0.7756 | 0.0452 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 19.41 | 0.6962 | 0.0576 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 19.84 | 0.7386 | 0.0485 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 19.81 | 0.7410 | 0.0490 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 9.06 | 0.2986 | 0.2135 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 12.24 | 0.3852 | 0.1629 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 22.23 | 0.8271 | 0.0349 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 17.66 | 0.6802 | 0.0676 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 20.32 | 0.7756 | 0.0408 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 10.59 | 0.4841 | 0.1705 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 10.66 | 0.5125 | 0.1604 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 12.08 | 0.4871 | 0.1264 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 22.09 | 0.8254 | 0.0353 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 17.67 | 0.6801 | 0.0676 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 20.26 | 0.7749 | 0.0411 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 10.59 | 0.4845 | 0.1704 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 10.66 | 0.5128 | 0.1603 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 12.09 | 0.4878 | 0.1263 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 23.02 | 0.8537 | 0.0277 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 22.28 | 0.8312 | 0.0293 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 22.27 | 0.8349 | 0.0296 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 22.30 | 0.8365 | 0.0289 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 13.69 | 0.6714 | 0.0724 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 17.05 | 0.7182 | 0.0548 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 23.01 | 0.8536 | 0.0275 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 22.30 | 0.8312 | 0.0292 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 22.30 | 0.8358 | 0.0292 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 22.31 | 0.8367 | 0.0290 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 13.68 | 0.6715 | 0.0724 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 17.08 | 0.7182 | 0.0547 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 24.01 | 0.8741 | 0.0229 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 22.11 | 0.8308 | 0.0261 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 22.48 | 0.8451 | 0.0255 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 13.86 | 0.7008 | 0.0752 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 13.55 | 0.6996 | 0.0746 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 16.02 | 0.7100 | 0.0464 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 23.92 | 0.8730 | 0.0230 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 22.11 | 0.8307 | 0.0261 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 22.43 | 0.8447 | 0.0257 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 13.87 | 0.7010 | 0.0751 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 13.55 | 0.6997 | 0.0746 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 16.04 | 0.7104 | 0.0463 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 25.73 | 0.9248 | 0.0355 | 1.00 |
| flow_s0.5_pose | 24.65 | 0.9099 | 0.0374 | 1.00 |
| flow_s0.5_posecal | 21.29 | 0.8439 | 0.0534 | 1.00 |
| flow_s0.5_uniform | 23.02 | 0.8845 | 0.0430 | 1.00 |
| flow_s1.0_oracle | 26.44 | 0.9323 | 0.0341 | 1.00 |
| flow_s1.0_pose | 25.29 | 0.9172 | 0.0359 | 1.00 |
| flow_s1.0_posecal | 21.63 | 0.8494 | 0.0512 | 1.00 |
| flow_s1.0_uniform | 23.35 | 0.8857 | 0.0419 | 1.00 |
| gs_center448_nat_dil | 21.89 | 0.7738 | 0.0813 | 1.00 |
| gs_center448_nat_dil+reg | 23.34 | 0.8459 | 0.0624 | 1.00 |
| gs_center448_nat_dil_cal | 13.95 | 0.5254 | 0.2115 | 1.00 |
| gs_center448_nat_dil_cal+reg | 22.42 | 0.8279 | 0.0672 | 1.00 |
| gs_center448_nat_dil_calK | 10.05 | 0.4380 | 0.2674 | 1.00 |
| gs_center448_nat_dil_calK+reg | 21.87 | 0.8232 | 0.0725 | 0.94 |
| gs_center448_nat_mip | 21.89 | 0.7754 | 0.0810 | 1.00 |
| gs_center448_nat_mip+reg | 23.23 | 0.8475 | 0.0632 | 1.00 |
| gs_center448_nat_mip_cal | 13.85 | 0.5223 | 0.2122 | 1.00 |
| gs_center448_nat_mip_cal+reg | 22.38 | 0.8293 | 0.0669 | 1.00 |
| gs_center448_nat_mip_calK | 10.05 | 0.4387 | 0.2674 | 1.00 |
| gs_center448_nat_mip_calK+reg | 21.91 | 0.8238 | 0.0723 | 0.94 |
| gs_roi448_nat_dil | 17.27 | 0.6287 | 0.1311 | 0.56 |
| gs_roi448_nat_dil+reg | 22.71 | 0.8315 | 0.0693 | 0.58 |
| gs_roi448_nat_dil_cal | 11.79 | 0.4065 | 0.2482 | 0.56 |
| gs_roi448_nat_dil_cal+reg | 21.22 | 0.7927 | 0.0754 | 0.61 |
| gs_roi448_nat_dil_calK | 9.20 | 0.4328 | 0.3718 | 0.56 |
| gs_roi448_nat_dil_calK+reg | 9.56 | 0.4440 | 0.3588 | 0.67 |
| gs_roi448_nat_mip | 17.26 | 0.6287 | 0.1311 | 0.56 |
| gs_roi448_nat_mip+reg | 22.57 | 0.8315 | 0.0705 | 0.58 |
| gs_roi448_nat_mip_cal | 11.80 | 0.4067 | 0.2481 | 0.56 |
| gs_roi448_nat_mip_cal+reg | 21.15 | 0.7928 | 0.0751 | 0.60 |
| gs_roi448_nat_mip_calK | 9.21 | 0.4334 | 0.3717 | 0.56 |
| gs_roi448_nat_mip_calK+reg | 9.57 | 0.4446 | 0.3588 | 0.67 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 25.45 | 0.9132 | 0.0415 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 24.94 | 0.9041 | 0.0441 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 24.66 | 0.9068 | 0.0437 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 24.41 | 0.9054 | 0.0446 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 19.20 | 0.8382 | 0.0754 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 20.95 | 0.8555 | 0.0677 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 25.40 | 0.9130 | 0.0416 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 24.95 | 0.9040 | 0.0439 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 24.63 | 0.9069 | 0.0436 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 24.44 | 0.9055 | 0.0446 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 19.20 | 0.8382 | 0.0754 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 20.92 | 0.8551 | 0.0679 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 26.18 | 0.9206 | 0.0375 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 24.42 | 0.9014 | 0.0438 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 24.83 | 0.9093 | 0.0406 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 19.28 | 0.8512 | 0.0707 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 19.10 | 0.8509 | 0.0675 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 20.72 | 0.8604 | 0.0574 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 26.05 | 0.9201 | 0.0379 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 24.40 | 0.9012 | 0.0438 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 24.78 | 0.9090 | 0.0408 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 19.28 | 0.8512 | 0.0706 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 19.10 | 0.8509 | 0.0675 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 20.73 | 0.8604 | 0.0573 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 24.08 | 0.8858 | 0.0501 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 23.04 | 0.8574 | 0.0567 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 23.34 | 0.8737 | 0.0530 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 23.13 | 0.8746 | 0.0542 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 13.51 | 0.6743 | 0.1388 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 16.85 | 0.7257 | 0.1167 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 24.01 | 0.8862 | 0.0502 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 23.04 | 0.8575 | 0.0564 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 23.27 | 0.8739 | 0.0528 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 23.16 | 0.8748 | 0.0542 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 13.51 | 0.6745 | 0.1389 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 16.78 | 0.7245 | 0.1171 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 25.07 | 0.9059 | 0.0426 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 22.07 | 0.8515 | 0.0589 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 23.63 | 0.8870 | 0.0463 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 14.30 | 0.7436 | 0.1253 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 14.39 | 0.7584 | 0.1188 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 16.90 | 0.7682 | 0.0904 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 24.95 | 0.9054 | 0.0429 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 22.06 | 0.8514 | 0.0589 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 23.57 | 0.8866 | 0.0464 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 14.30 | 0.7437 | 0.1253 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 14.39 | 0.7585 | 0.1187 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 16.91 | 0.7684 | 0.0904 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 25.18 | 0.9129 | 0.0400 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 24.73 | 0.9032 | 0.0414 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 24.82 | 0.9071 | 0.0412 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 24.68 | 0.9068 | 0.0415 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 17.67 | 0.8311 | 0.0723 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 20.37 | 0.8538 | 0.0607 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 25.16 | 0.9128 | 0.0401 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 24.71 | 0.9028 | 0.0413 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 24.76 | 0.9070 | 0.0413 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 24.70 | 0.9070 | 0.0415 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 17.67 | 0.8311 | 0.0723 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 20.36 | 0.8536 | 0.0607 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 25.99 | 0.9204 | 0.0363 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 24.36 | 0.8998 | 0.0407 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 24.70 | 0.9086 | 0.0389 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 17.08 | 0.8378 | 0.0776 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 16.94 | 0.8372 | 0.0764 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 20.01 | 0.8506 | 0.0556 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 25.91 | 0.9200 | 0.0365 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 24.34 | 0.8997 | 0.0407 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 24.65 | 0.9084 | 0.0390 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 17.08 | 0.8378 | 0.0776 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 16.94 | 0.8373 | 0.0764 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 20.02 | 0.8507 | 0.0556 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 31.41 | 0.9667 | 0.0317 | 1.00 |
| flow_s0.5_pose | 31.22 | 0.9653 | 0.0318 | 1.00 |
| flow_s0.5_posecal | 28.38 | 0.9403 | 0.0457 | 1.00 |
| flow_s0.5_uniform | 30.53 | 0.9607 | 0.0346 | 1.00 |
| flow_s1.0_oracle | 31.56 | 0.9661 | 0.0302 | 1.00 |
| flow_s1.0_pose | 31.46 | 0.9649 | 0.0305 | 1.00 |
| flow_s1.0_posecal | 28.45 | 0.9390 | 0.0441 | 1.00 |
| flow_s1.0_uniform | 30.29 | 0.9592 | 0.0331 | 1.00 |
| gs_center448_nat_dil | 25.10 | 0.8455 | 0.0893 | 1.00 |
| gs_center448_nat_dil+reg | 27.87 | 0.9138 | 0.0733 | 0.99 |
| gs_center448_nat_dil_cal | 15.77 | 0.6460 | 0.2491 | 1.00 |
| gs_center448_nat_dil_cal+reg | 27.41 | 0.9105 | 0.0771 | 1.00 |
| gs_center448_nat_dil_calK | 10.95 | 0.5589 | 0.3401 | 1.00 |
| gs_center448_nat_dil_calK+reg | 26.94 | 0.9110 | 0.0818 | 0.93 |
| gs_center448_nat_mip | 24.99 | 0.8453 | 0.0878 | 1.00 |
| gs_center448_nat_mip+reg | 27.64 | 0.9146 | 0.0722 | 0.99 |
| gs_center448_nat_mip_cal | 15.71 | 0.6434 | 0.2486 | 1.00 |
| gs_center448_nat_mip_cal+reg | 27.32 | 0.9112 | 0.0749 | 1.00 |
| gs_center448_nat_mip_calK | 10.95 | 0.5599 | 0.3409 | 1.00 |
| gs_center448_nat_mip_calK+reg | 26.99 | 0.9114 | 0.0824 | 0.93 |
| gs_roi448_nat_dil | 18.25 | 0.6935 | 0.1702 | 0.48 |
| gs_roi448_nat_dil+reg | 27.01 | 0.9013 | 0.0799 | 0.51 |
| gs_roi448_nat_dil_cal | 12.24 | 0.5421 | 0.2982 | 0.48 |
| gs_roi448_nat_dil_cal+reg | 26.01 | 0.8904 | 0.0876 | 0.53 |
| gs_roi448_nat_dil_calK | 9.60 | 0.4912 | 0.4799 | 0.48 |
| gs_roi448_nat_dil_calK+reg | 10.01 | 0.5199 | 0.4715 | 0.59 |
| gs_roi448_nat_mip | 18.26 | 0.6937 | 0.1702 | 0.48 |
| gs_roi448_nat_mip+reg | 26.87 | 0.9016 | 0.0808 | 0.51 |
| gs_roi448_nat_mip_cal | 12.25 | 0.5421 | 0.2984 | 0.48 |
| gs_roi448_nat_mip_cal+reg | 26.00 | 0.8908 | 0.0885 | 0.53 |
| gs_roi448_nat_mip_calK | 9.60 | 0.4917 | 0.4800 | 0.48 |
| gs_roi448_nat_mip_calK+reg | 10.01 | 0.5206 | 0.4719 | 0.59 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 31.46 | 0.9640 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 31.44 | 0.9634 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 31.44 | 0.9636 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 31.44 | 0.9633 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 30.73 | 0.9589 | 0.0381 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 31.15 | 0.9596 | 0.0360 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 31.46 | 0.9640 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 31.45 | 0.9634 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 31.44 | 0.9636 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 31.44 | 0.9634 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 30.73 | 0.9589 | 0.0380 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 31.15 | 0.9596 | 0.0360 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 31.45 | 0.9641 | 0.0307 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 31.20 | 0.9620 | 0.0334 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 31.42 | 0.9639 | 0.0309 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 31.01 | 0.9602 | 0.0352 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 30.89 | 0.9600 | 0.0357 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 30.90 | 0.9609 | 0.0356 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 31.44 | 0.9641 | 0.0307 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 31.21 | 0.9620 | 0.0334 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 31.42 | 0.9639 | 0.0309 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 31.01 | 0.9602 | 0.0352 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 30.89 | 0.9600 | 0.0357 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 30.91 | 0.9609 | 0.0356 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 31.38 | 0.9619 | 0.0314 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 31.32 | 0.9598 | 0.0327 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 31.31 | 0.9613 | 0.0318 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 31.30 | 0.9614 | 0.0320 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 28.20 | 0.9331 | 0.0824 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 29.91 | 0.9398 | 0.0674 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 31.38 | 0.9620 | 0.0314 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 31.31 | 0.9598 | 0.0328 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 31.30 | 0.9613 | 0.0318 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 31.30 | 0.9614 | 0.0319 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 28.20 | 0.9331 | 0.0824 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 29.89 | 0.9396 | 0.0676 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 31.39 | 0.9627 | 0.0314 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 30.99 | 0.9566 | 0.0392 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 31.22 | 0.9620 | 0.0319 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 28.93 | 0.9394 | 0.0746 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 28.95 | 0.9419 | 0.0713 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 29.54 | 0.9473 | 0.0593 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 31.38 | 0.9627 | 0.0315 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 30.99 | 0.9566 | 0.0392 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 31.21 | 0.9620 | 0.0319 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 28.93 | 0.9394 | 0.0745 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 28.95 | 0.9419 | 0.0713 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 29.54 | 0.9473 | 0.0593 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 31.33 | 0.9630 | 0.0331 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 31.43 | 0.9636 | 0.0318 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 31.33 | 0.9630 | 0.0331 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 31.43 | 0.9636 | 0.0318 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 31.38 | 0.9631 | 0.0326 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 31.38 | 0.9630 | 0.0328 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 31.42 | 0.9640 | 0.0313 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 31.45 | 0.9648 | 0.0305 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 31.38 | 0.9631 | 0.0326 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 31.38 | 0.9630 | 0.0328 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 31.42 | 0.9640 | 0.0313 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 28.40 | 0.9528 | 0.0403 | 1.00 |
| flow_s0.5_pose | 27.45 | 0.9461 | 0.0415 | 1.00 |
| flow_s0.5_posecal | 24.27 | 0.9079 | 0.0560 | 1.00 |
| flow_s0.5_uniform | 26.08 | 0.9340 | 0.0467 | 1.00 |
| flow_s1.0_oracle | 28.96 | 0.9545 | 0.0383 | 1.00 |
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| flow_s1.0_posecal | 24.59 | 0.9090 | 0.0528 | 1.00 |
| flow_s1.0_uniform | 26.19 | 0.9330 | 0.0440 | 1.00 |
| gs_center448_nat_dil | 23.47 | 0.8207 | 0.1070 | 1.00 |
| gs_center448_nat_dil+reg | 25.60 | 0.8905 | 0.0958 | 0.99 |
| gs_center448_nat_dil_cal | 14.89 | 0.6050 | 0.2620 | 1.00 |
| gs_center448_nat_dil_cal+reg | 24.83 | 0.8833 | 0.0996 | 1.00 |
| gs_center448_nat_dil_calK | 10.50 | 0.5170 | 0.3642 | 1.00 |
| gs_center448_nat_dil_calK+reg | 24.35 | 0.8818 | 0.1033 | 0.94 |
| gs_center448_nat_mip | 23.39 | 0.8204 | 0.1040 | 1.00 |
| gs_center448_nat_mip+reg | 25.46 | 0.8914 | 0.0940 | 0.99 |
| gs_center448_nat_mip_cal | 14.83 | 0.6024 | 0.2604 | 1.00 |
| gs_center448_nat_mip_cal+reg | 24.75 | 0.8838 | 0.0964 | 1.00 |
| gs_center448_nat_mip_calK | 10.50 | 0.5179 | 0.3654 | 1.00 |
| gs_center448_nat_mip_calK+reg | 24.39 | 0.8823 | 0.1044 | 0.94 |
| gs_roi448_nat_dil | 17.31 | 0.6608 | 0.1654 | 0.52 |
| gs_roi448_nat_dil+reg | 24.68 | 0.8746 | 0.1048 | 0.55 |
| gs_roi448_nat_dil_cal | 11.77 | 0.4928 | 0.3167 | 0.52 |
| gs_roi448_nat_dil_cal+reg | 23.37 | 0.8552 | 0.1139 | 0.57 |
| gs_roi448_nat_dil_calK | 9.40 | 0.4596 | 0.5890 | 0.52 |
| gs_roi448_nat_dil_calK+reg | 9.80 | 0.4867 | 0.5647 | 0.63 |
| gs_roi448_nat_mip | 17.31 | 0.6609 | 0.1654 | 0.52 |
| gs_roi448_nat_mip+reg | 24.55 | 0.8744 | 0.1059 | 0.55 |
| gs_roi448_nat_mip_cal | 11.78 | 0.4930 | 0.3167 | 0.52 |
| gs_roi448_nat_mip_cal+reg | 23.32 | 0.8553 | 0.1147 | 0.57 |
| gs_roi448_nat_mip_calK | 9.40 | 0.4601 | 0.5899 | 0.52 |
| gs_roi448_nat_mip_calK+reg | 9.80 | 0.4874 | 0.5660 | 0.62 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 28.01 | 0.9453 | 0.0477 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 27.55 | 0.9409 | 0.0511 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal+reg] | 27.31 | 0.9425 | 0.0497 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK+reg] | 27.10 | 0.9417 | 0.0510 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_calK] | 22.31 | 0.9112 | 0.0930 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil_cal] | 23.95 | 0.9183 | 0.0833 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 27.98 | 0.9452 | 0.0477 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 27.54 | 0.9408 | 0.0508 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal+reg] | 27.27 | 0.9425 | 0.0495 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK+reg] | 27.12 | 0.9418 | 0.0510 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_calK] | 22.31 | 0.9112 | 0.0929 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip_cal] | 23.95 | 0.9181 | 0.0834 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 28.46 | 0.9479 | 0.0433 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 26.50 | 0.9369 | 0.0536 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal+reg] | 27.32 | 0.9438 | 0.0471 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK+reg] | 22.66 | 0.9178 | 0.0842 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_calK] | 22.49 | 0.9176 | 0.0814 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil_cal] | 23.73 | 0.9206 | 0.0711 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 28.37 | 0.9477 | 0.0436 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 26.50 | 0.9369 | 0.0535 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal+reg] | 27.29 | 0.9437 | 0.0473 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK+reg] | 22.67 | 0.9179 | 0.0842 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_calK] | 22.49 | 0.9177 | 0.0814 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip_cal] | 23.74 | 0.9206 | 0.0710 | 1.00 |
| hyb_risk[gs_center448_nat_dil+reg] | 26.85 | 0.9316 | 0.0577 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 25.96 | 0.9179 | 0.0635 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal+reg] | 26.20 | 0.9269 | 0.0603 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK+reg] | 26.02 | 0.9272 | 0.0608 | 1.00 |
| hyb_risk[gs_center448_nat_dil_calK] | 17.02 | 0.8341 | 0.1595 | 1.00 |
| hyb_risk[gs_center448_nat_dil_cal] | 20.10 | 0.8536 | 0.1315 | 1.00 |
| hyb_risk[gs_center448_nat_mip+reg] | 26.80 | 0.9319 | 0.0574 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 25.94 | 0.9177 | 0.0631 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal+reg] | 26.12 | 0.9269 | 0.0598 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK+reg] | 26.04 | 0.9273 | 0.0610 | 1.00 |
| hyb_risk[gs_center448_nat_mip_calK] | 17.02 | 0.8342 | 0.1596 | 1.00 |
| hyb_risk[gs_center448_nat_mip_cal] | 20.03 | 0.8531 | 0.1316 | 1.00 |
| hyb_risk[gs_roi448_nat_dil+reg] | 27.57 | 0.9401 | 0.0490 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 24.34 | 0.9108 | 0.0687 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal+reg] | 26.30 | 0.9329 | 0.0533 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK+reg] | 17.94 | 0.8652 | 0.1501 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_calK] | 18.07 | 0.8718 | 0.1440 | 1.00 |
| hyb_risk[gs_roi448_nat_dil_cal] | 19.84 | 0.8755 | 0.1087 | 1.00 |
| hyb_risk[gs_roi448_nat_mip+reg] | 27.47 | 0.9399 | 0.0494 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 24.33 | 0.9108 | 0.0686 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal+reg] | 26.25 | 0.9328 | 0.0535 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK+reg] | 17.94 | 0.8653 | 0.1501 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_calK] | 18.07 | 0.8719 | 0.1439 | 1.00 |
| hyb_risk[gs_roi448_nat_mip_cal] | 19.85 | 0.8755 | 0.1086 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil+reg] | 27.89 | 0.9462 | 0.0446 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 27.60 | 0.9425 | 0.0455 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal+reg] | 27.60 | 0.9443 | 0.0458 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK+reg] | 27.44 | 0.9441 | 0.0460 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_calK] | 21.49 | 0.9157 | 0.0776 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil_cal] | 24.15 | 0.9234 | 0.0658 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip+reg] | 27.88 | 0.9462 | 0.0447 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 27.58 | 0.9423 | 0.0456 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal+reg] | 27.53 | 0.9442 | 0.0458 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK+reg] | 27.45 | 0.9441 | 0.0460 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_calK] | 21.49 | 0.9158 | 0.0777 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip_cal] | 24.14 | 0.9233 | 0.0657 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil+reg] | 28.43 | 0.9488 | 0.0406 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 27.30 | 0.9413 | 0.0436 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal+reg] | 27.40 | 0.9452 | 0.0431 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK+reg] | 21.04 | 0.9185 | 0.0851 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_calK] | 20.94 | 0.9185 | 0.0839 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil_cal] | 23.54 | 0.9228 | 0.0595 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip+reg] | 28.38 | 0.9487 | 0.0408 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 27.28 | 0.9412 | 0.0436 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal+reg] | 27.36 | 0.9451 | 0.0432 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK+reg] | 21.04 | 0.9185 | 0.0851 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_calK] | 20.94 | 0.9185 | 0.0839 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip_cal] | 23.55 | 0.9228 | 0.0595 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|
| cam3 | gs_center448_nat_dil | 10.63 | 1.00 |
| cam3 | gs_center448_nat_dil_cal | 26.49 | 1.00 |
| cam3 | gs_center448_nat_dil_calK | 57.35 | 1.00 |
| cam3 | gs_center448_nat_mip | 10.62 | 1.00 |
| cam3 | gs_center448_nat_mip_cal | 26.51 | 1.00 |
| cam3 | gs_center448_nat_mip_calK | 57.38 | 1.00 |
| cam3 | gs_roi448_nat_dil | 9.20 | 1.00 |
| cam3 | gs_roi448_nat_dil_cal | 21.40 | 1.00 |
| cam3 | gs_roi448_nat_dil_calK | 57.56 | 0.83 |
| cam3 | gs_roi448_nat_mip | 9.24 | 1.00 |
| cam3 | gs_roi448_nat_mip_cal | 21.45 | 1.00 |
| cam3 | gs_roi448_nat_mip_calK | 57.49 | 0.83 |
| cam5 | gs_center448_nat_dil | 2.66 | 1.00 |
| cam5 | gs_center448_nat_dil_cal | 18.45 | 1.00 |
| cam5 | gs_center448_nat_dil_calK | 49.07 | 1.00 |
| cam5 | gs_center448_nat_mip | 2.65 | 1.00 |
| cam5 | gs_center448_nat_mip_cal | 18.53 | 1.00 |
| cam5 | gs_center448_nat_mip_calK | 49.10 | 1.00 |
| cam5 | gs_roi448_nat_dil | 7.77 | 1.00 |
| cam5 | gs_roi448_nat_dil_cal | 20.90 | 1.00 |
| cam5 | gs_roi448_nat_dil_calK | 69.72 | 1.00 |
| cam5 | gs_roi448_nat_mip | 7.78 | 1.00 |
| cam5 | gs_roi448_nat_mip_cal | 20.85 | 1.00 |
| cam5 | gs_roi448_nat_mip_calK | 69.94 | 1.00 |

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
| cam3 | 1 | 0.250 | 0.305 | 0.304 | 0.320 |
| cam3 | 2 | 0.500 | 0.551 | 0.603 | 0.550 |
| cam3 | 3 | 0.750 | 0.802 | 0.870 | 0.760 |
| cam3 | 5 | 0.250 | 0.194 | 0.211 | 0.220 |
| cam3 | 6 | 0.500 | 0.463 | 0.492 | 0.470 |
| cam3 | 7 | 0.750 | 0.742 | 0.696 | 0.740 |
| cam5 | 1 | 0.500 | 0.554 | 0.505 | 0.560 |
| cam5 | 3 | 0.500 | 0.559 | 0.669 | 0.550 |
| cam5 | 5 | 0.500 | 0.419 | 0.430 | 0.450 |
| cam5 | 7 | 0.500 | 0.522 | 0.398 | 0.530 |

## AnySplat 运行统计

旋转/光心误差：vggt 行是联合估计与输入视点估计的一致性；calib/calibK 行是标定位姿经 Sim(3) 对齐到AnySplat 输入视点位姿后的残差（反映 AnySplat 自身预测的输入相机几何与真实阵列的偏差）。

| 设置 | 变体 | 位姿来源 | 窗口边长 | 渲染分辨率 | 模式 | eps2d | 3D 滤波 | 高斯数 | 编码 s | 渲染 ms/视点 | 输入视点自渲染 PSNR | 最大旋转误差° | 最大光心误差/基线 |
|---|---|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|
| cam3 | gs_center448_nat_dil | vggt | 1080 | 1080 | classic | 1.74 | False | 432640 | 0.823 | 11.6 | 29.26 | 0.38 | 0.010 |
| cam3 | gs_center448_nat_dil_cal | calib | 1080 | 1080 | classic | 1.74 | False | 432640 | 0.823 | 9.7 | 29.26 | 1.77 | 0.029 |
| cam3 | gs_center448_nat_dil_calK | calibK | 1080 | 1080 | classic | 1.74 | False | 432640 | 0.823 | 9.0 | 29.26 | 1.77 | 0.029 |
| cam3 | gs_center448_nat_mip | vggt | 1080 | 1080 | antialiased | 0.10 | True | 432640 | 0.823 | 14.0 | 29.26 | 0.38 | 0.010 |
| cam3 | gs_center448_nat_mip_cal | calib | 1080 | 1080 | antialiased | 0.10 | True | 432640 | 0.823 | 10.3 | 29.26 | 1.77 | 0.029 |
| cam3 | gs_center448_nat_mip_calK | calibK | 1080 | 1080 | antialiased | 0.10 | True | 432640 | 0.823 | 18.2 | 29.26 | 1.77 | 0.029 |
| cam3 | gs_roi448_nat_dil | vggt | 543 | 543 | classic | 0.44 | False | 183447 | 0.336 | 3.1 | 26.67 | 0.54 | 0.020 |
| cam3 | gs_roi448_nat_dil_cal | calib | 543 | 543 | classic | 0.44 | False | 183447 | 0.336 | 2.5 | 26.67 | 1.13 | 0.115 |
| cam3 | gs_roi448_nat_dil_calK | calibK | 543 | 543 | classic | 0.44 | False | 183447 | 0.336 | 2.3 | 26.67 | 1.13 | 0.115 |
| cam3 | gs_roi448_nat_mip | vggt | 543 | 543 | antialiased | 0.10 | True | 183447 | 0.336 | 2.6 | 26.67 | 0.54 | 0.020 |
| cam3 | gs_roi448_nat_mip_cal | calib | 543 | 543 | antialiased | 0.10 | True | 183447 | 0.336 | 2.8 | 26.67 | 1.13 | 0.115 |
| cam3 | gs_roi448_nat_mip_calK | calibK | 543 | 543 | antialiased | 0.10 | True | 183447 | 0.336 | 2.9 | 26.67 | 1.13 | 0.115 |
| cam5 | gs_center448_nat_dil | vggt | 1080 | 1080 | classic | 1.74 | False | 637973 | 0.521 | 10.7 | 29.82 | 0.14 | 0.008 |
| cam5 | gs_center448_nat_dil_cal | calib | 1080 | 1080 | classic | 1.74 | False | 637973 | 0.521 | 13.9 | 29.82 | 1.35 | 0.045 |
| cam5 | gs_center448_nat_dil_calK | calibK | 1080 | 1080 | classic | 1.74 | False | 637973 | 0.521 | 18.6 | 29.82 | 1.35 | 0.045 |
| cam5 | gs_center448_nat_mip | vggt | 1080 | 1080 | antialiased | 0.10 | True | 637973 | 0.521 | 20.0 | 29.82 | 0.14 | 0.008 |
| cam5 | gs_center448_nat_mip_cal | calib | 1080 | 1080 | antialiased | 0.10 | True | 637973 | 0.521 | 19.1 | 29.82 | 1.35 | 0.045 |
| cam5 | gs_center448_nat_mip_calK | calibK | 1080 | 1080 | antialiased | 0.10 | True | 637973 | 0.521 | 25.3 | 29.82 | 1.35 | 0.045 |
| cam5 | gs_roi448_nat_dil | vggt | 543 | 543 | classic | 0.44 | False | 269851 | 0.500 | 3.5 | 27.42 | 0.17 | 0.010 |
| cam5 | gs_roi448_nat_dil_cal | calib | 543 | 543 | classic | 0.44 | False | 269851 | 0.500 | 3.2 | 27.42 | 0.86 | 0.131 |
| cam5 | gs_roi448_nat_dil_calK | calibK | 543 | 543 | classic | 0.44 | False | 269851 | 0.500 | 3.0 | 27.42 | 0.86 | 0.131 |
| cam5 | gs_roi448_nat_mip | vggt | 543 | 543 | antialiased | 0.10 | True | 269851 | 0.500 | 3.5 | 27.42 | 0.17 | 0.010 |
| cam5 | gs_roi448_nat_mip_cal | calib | 543 | 543 | antialiased | 0.10 | True | 269851 | 0.500 | 3.4 | 27.42 | 0.86 | 0.131 |
| cam5 | gs_roi448_nat_mip_calK | calibK | 543 | 543 | antialiased | 0.10 | True | 269851 | 0.500 | 3.2 | 27.42 | 0.86 | 0.131 |

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

# 局部 GS 质量验证结果汇总（第二轮：Mip 滤波 + ROI + 配准诊断）

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## 设置 cam3

物体区 PSNR 最好的 GS 变体：`gs_center448_nat_dil`；整幅裁剪中最好的：`gs_center448_nat_dil`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=4.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 13.02 / 0.2906 | 13.28 / 0.0595 | 32.96 / 0.0256 | 22.18 / 0.0691 |
| flow_s1.0_pose | 14.53 / 0.2724 | 13.82 / 0.0533 | 33.36 / 0.0240 | 22.60 / 0.0629 |
| flow_s0.5_pose | 14.85 / 0.2383 | 14.41 / 0.0509 | 32.85 / 0.0252 | 22.93 / 0.0610 |
| gs_center448_nat_dil | 14.74 / 0.2478 | 13.35 / 0.1311 | 19.79 / 0.1575 | 17.49 / 0.1818 |
| gs_center448_nat_dil+reg | 17.44 / 0.1882 | 18.51 / 0.0600 | 29.31 / 0.0600 | 24.89 / 0.1095 |
| hyb_oracle_fail[gs_center448_nat_dil] | 15.60 / 0.2253 | 13.35 / 0.1311 | 32.39 / 0.0336 | 22.23 / 0.1078 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 17.97 / 0.1843 | 18.52 / 0.0602 | 32.97 / 0.0257 | 26.35 / 0.0684 |
| hyb_risktuned[gs_center448_nat_dil] | 14.35 / 0.2658 | 15.06 / 0.0761 | 32.96 / 0.0256 | 22.66 / 0.0835 |
| hyb_risk[gs_center448_nat_dil] | 14.47 / 0.2564 | 13.75 / 0.1166 | 31.65 / 0.0486 | 19.55 / 0.1426 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 16.10 | 0.5746 | 0.1984 | 1.00 |
| flow_s0.5_pose | 14.85 | 0.5040 | 0.2383 | 1.00 |
| flow_s0.5_uniform | 14.21 | 0.5001 | 0.2198 | 1.00 |
| flow_s1.0_oracle | 15.16 | 0.5837 | 0.2651 | 1.00 |
| flow_s1.0_pose | 14.53 | 0.5347 | 0.2724 | 1.00 |
| flow_s1.0_uniform | 13.02 | 0.4647 | 0.2906 | 1.00 |
| gs_center448_in | 14.74 | 0.4896 | 0.2494 | 1.00 |
| gs_center448_in+reg | 17.44 | 0.6405 | 0.1916 | 1.00 |
| gs_center448_nat | 14.67 | 0.4708 | 0.2485 | 1.00 |
| gs_center448_nat+reg | 16.96 | 0.6202 | 0.1913 | 1.00 |
| gs_center448_nat_dil | 14.74 | 0.4896 | 0.2478 | 1.00 |
| gs_center448_nat_dil+reg | 17.44 | 0.6399 | 0.1882 | 1.00 |
| gs_center448_nat_mip | 8.95 | 0.3141 | 0.6357 | 1.00 |
| gs_center448_nat_mip+reg | 10.83 | 0.2821 | 0.5277 | 0.74 |
| gs_center448_nat_mip2d | 14.63 | 0.4673 | 0.2526 | 1.00 |
| gs_center448_nat_mip2d+reg | 16.69 | 0.6085 | 0.1975 | 1.00 |
| gs_roi448_in | 13.95 | 0.4416 | 0.2468 | 1.00 |
| gs_roi448_in+reg | 17.62 | 0.6588 | 0.1654 | 1.00 |
| gs_roi448_nat | 13.95 | 0.4405 | 0.2468 | 1.00 |
| gs_roi448_nat+reg | 17.57 | 0.6568 | 0.1657 | 1.00 |
| gs_roi448_nat_dil | 13.96 | 0.4421 | 0.2474 | 1.00 |
| gs_roi448_nat_dil+reg | 17.60 | 0.6582 | 0.1665 | 1.00 |
| gs_roi448_nat_mip | 9.56 | 0.3304 | 0.6143 | 1.00 |
| gs_roi448_nat_mip+reg | 9.57 | 0.3335 | 0.6143 | 1.00 |
| gs_roi448_nat_mip2d | 13.93 | 0.4377 | 0.2473 | 1.00 |
| gs_roi448_nat_mip2d+reg | 17.59 | 0.6572 | 0.1645 | 1.00 |
| hyb_oracle_fail[gs_center448_in+reg] | 17.97 | 0.6539 | 0.1866 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 15.60 | 0.5310 | 0.2262 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 17.45 | 0.6305 | 0.1890 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 15.42 | 0.5097 | 0.2290 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 17.97 | 0.6534 | 0.1843 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 15.60 | 0.5305 | 0.2253 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 12.56 | 0.3956 | 0.4227 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 17.18 | 0.6188 | 0.1965 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 15.36 | 0.5058 | 0.2356 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 12.27 | 0.4016 | 0.4276 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 18.05 | 0.6654 | 0.1698 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 14.84 | 0.4877 | 0.2332 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 18.00 | 0.6638 | 0.1708 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 14.83 | 0.4866 | 0.2334 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 18.04 | 0.6652 | 0.1707 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 14.85 | 0.4882 | 0.2336 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 11.46 | 0.3727 | 0.4526 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 17.99 | 0.6617 | 0.1709 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 14.79 | 0.4839 | 0.2328 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 11.46 | 0.3714 | 0.4555 | 1.00 |
| hyb_risk[gs_center448_in] | 14.46 | 0.4903 | 0.2577 | 1.00 |
| hyb_risk[gs_center448_nat] | 14.40 | 0.4726 | 0.2589 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 14.47 | 0.4903 | 0.2564 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 14.37 | 0.4694 | 0.2655 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 11.13 | 0.3702 | 0.4977 | 1.00 |
| hyb_risk[gs_roi448_in] | 13.41 | 0.4349 | 0.2630 | 1.00 |
| hyb_risk[gs_roi448_nat] | 13.40 | 0.4337 | 0.2636 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 13.42 | 0.4353 | 0.2637 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 13.38 | 0.4306 | 0.2650 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 10.26 | 0.3449 | 0.5523 | 1.00 |
| hyb_risktuned[gs_center448_in] | 14.34 | 0.4928 | 0.2670 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 14.29 | 0.4756 | 0.2681 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 14.35 | 0.4929 | 0.2658 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 14.27 | 0.4724 | 0.2746 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 11.22 | 0.3741 | 0.4929 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 13.23 | 0.4367 | 0.2671 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 13.23 | 0.4355 | 0.2677 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 13.24 | 0.4372 | 0.2677 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 13.21 | 0.4320 | 0.2698 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 10.33 | 0.3444 | 0.5408 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 11.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 15.04 | 0.6394 | 0.0484 | 1.00 |
| flow_s0.5_pose | 14.41 | 0.6245 | 0.0509 | 1.00 |
| flow_s0.5_uniform | 14.52 | 0.5790 | 0.0553 | 1.00 |
| flow_s1.0_oracle | 14.04 | 0.6517 | 0.0518 | 1.00 |
| flow_s1.0_pose | 13.82 | 0.6412 | 0.0533 | 1.00 |
| flow_s1.0_uniform | 13.28 | 0.5474 | 0.0595 | 1.00 |
| gs_center448_in | 13.33 | 0.4109 | 0.1315 | 1.00 |
| gs_center448_in+reg | 18.51 | 0.7082 | 0.0604 | 0.99 |
| gs_center448_nat | 13.22 | 0.3915 | 0.1344 | 1.00 |
| gs_center448_nat+reg | 17.48 | 0.6756 | 0.0717 | 0.99 |
| gs_center448_nat_dil | 13.35 | 0.4113 | 0.1311 | 1.00 |
| gs_center448_nat_dil+reg | 18.51 | 0.7077 | 0.0600 | 0.99 |
| gs_center448_nat_mip | 8.93 | 0.2569 | 0.2197 | 1.00 |
| gs_center448_nat_mip+reg | 10.07 | 0.2419 | 0.1974 | 0.88 |
| gs_center448_nat_mip2d | 13.19 | 0.3869 | 0.1364 | 1.00 |
| gs_center448_nat_mip2d+reg | 16.96 | 0.6565 | 0.0800 | 0.99 |
| gs_roi448_in | 12.92 | 0.3755 | 0.1662 | 0.79 |
| gs_roi448_in+reg | 17.37 | 0.6538 | 0.0880 | 0.79 |
| gs_roi448_nat | 12.92 | 0.3748 | 0.1664 | 0.79 |
| gs_roi448_nat+reg | 17.33 | 0.6517 | 0.0888 | 0.79 |
| gs_roi448_nat_dil | 12.94 | 0.3763 | 0.1664 | 0.79 |
| gs_roi448_nat_dil+reg | 17.38 | 0.6537 | 0.0883 | 0.79 |
| gs_roi448_nat_mip | 9.24 | 0.2805 | 0.2665 | 0.79 |
| gs_roi448_nat_mip+reg | 9.28 | 0.2788 | 0.2663 | 0.79 |
| gs_roi448_nat_mip2d | 12.90 | 0.3726 | 0.1669 | 0.79 |
| gs_roi448_nat_mip2d+reg | 17.24 | 0.6492 | 0.0893 | 0.79 |
| hyb_oracle_fail[gs_center448_in+reg] | 18.53 | 0.7003 | 0.0606 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 13.33 | 0.4271 | 0.1315 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 17.54 | 0.6658 | 0.0731 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 13.24 | 0.4067 | 0.1353 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 18.52 | 0.7000 | 0.0602 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 13.35 | 0.4275 | 0.1311 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 11.82 | 0.3965 | 0.1284 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 17.09 | 0.6468 | 0.0817 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 13.24 | 0.4022 | 0.1375 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 11.39 | 0.4040 | 0.1416 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 17.77 | 0.6728 | 0.0575 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 13.71 | 0.4563 | 0.0995 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 17.75 | 0.6715 | 0.0578 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 13.71 | 0.4558 | 0.0996 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 17.79 | 0.6730 | 0.0577 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 13.73 | 0.4569 | 0.0996 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 10.67 | 0.3753 | 0.1318 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 17.67 | 0.6687 | 0.0581 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 13.70 | 0.4541 | 0.0997 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 10.62 | 0.3761 | 0.1322 | 1.00 |
| hyb_risk[gs_center448_in] | 13.74 | 0.4533 | 0.1170 | 1.00 |
| hyb_risk[gs_center448_nat] | 13.68 | 0.4360 | 0.1203 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 13.75 | 0.4536 | 0.1166 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 13.67 | 0.4322 | 0.1222 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 11.64 | 0.4316 | 0.1244 | 1.00 |
| hyb_risk[gs_roi448_in] | 13.74 | 0.4774 | 0.0948 | 1.00 |
| hyb_risk[gs_roi448_nat] | 13.74 | 0.4769 | 0.0949 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 13.75 | 0.4780 | 0.0949 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 13.73 | 0.4754 | 0.0951 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 10.76 | 0.4190 | 0.1246 | 1.00 |
| hyb_risktuned[gs_center448_in] | 15.06 | 0.5525 | 0.0763 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 14.99 | 0.5386 | 0.0782 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 15.06 | 0.5526 | 0.0761 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 14.99 | 0.5358 | 0.0792 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 12.29 | 0.4920 | 0.0934 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 14.47 | 0.5423 | 0.0683 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 14.47 | 0.5417 | 0.0683 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 14.48 | 0.5427 | 0.0683 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 14.46 | 0.5403 | 0.0685 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 11.56 | 0.4851 | 0.0943 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.99 | 0.8157 | 0.0503 | 1.00 |
| flow_s0.5_pose | 19.41 | 0.8090 | 0.0522 | 1.00 |
| flow_s0.5_uniform | 19.41 | 0.7875 | 0.0549 | 1.00 |
| flow_s1.0_oracle | 19.20 | 0.8289 | 0.0553 | 1.00 |
| flow_s1.0_pose | 18.94 | 0.8213 | 0.0560 | 1.00 |
| flow_s1.0_uniform | 18.44 | 0.7877 | 0.0604 | 1.00 |
| gs_center448_in | 14.83 | 0.5296 | 0.1733 | 1.00 |
| gs_center448_in+reg | 21.81 | 0.7909 | 0.0775 | 0.99 |
| gs_center448_nat | 14.94 | 0.5144 | 0.1733 | 1.00 |
| gs_center448_nat+reg | 20.73 | 0.7605 | 0.0858 | 0.99 |
| gs_center448_nat_dil | 14.85 | 0.5309 | 0.1721 | 1.00 |
| gs_center448_nat_dil+reg | 21.80 | 0.7914 | 0.0754 | 0.99 |
| gs_center448_nat_mip | 8.27 | 0.3926 | 0.3858 | 1.00 |
| gs_center448_nat_mip+reg | 9.40 | 0.3839 | 0.3663 | 0.90 |
| gs_center448_nat_mip2d | 14.95 | 0.5089 | 0.1784 | 1.00 |
| gs_center448_nat_mip2d+reg | 20.10 | 0.7409 | 0.0988 | 0.99 |
| gs_roi448_in | 14.64 | 0.5175 | 0.1944 | 0.70 |
| gs_roi448_in+reg | 19.51 | 0.7295 | 0.1081 | 0.70 |
| gs_roi448_nat | 14.65 | 0.5173 | 0.1948 | 0.70 |
| gs_roi448_nat+reg | 19.48 | 0.7284 | 0.1095 | 0.70 |
| gs_roi448_nat_dil | 14.66 | 0.5184 | 0.1950 | 0.70 |
| gs_roi448_nat_dil+reg | 19.51 | 0.7296 | 0.1085 | 0.70 |
| gs_roi448_nat_mip | 8.98 | 0.4139 | 0.4217 | 0.70 |
| gs_roi448_nat_mip+reg | 9.01 | 0.4171 | 0.4221 | 0.70 |
| gs_roi448_nat_mip2d | 14.64 | 0.5153 | 0.1957 | 0.70 |
| gs_roi448_nat_mip2d+reg | 19.44 | 0.7270 | 0.1082 | 0.70 |
| hyb_oracle_fail[gs_center448_in+reg] | 22.67 | 0.8279 | 0.0601 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 18.76 | 0.7325 | 0.0944 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 22.03 | 0.8135 | 0.0668 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 18.73 | 0.7253 | 0.0981 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 22.66 | 0.8278 | 0.0597 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 18.77 | 0.7327 | 0.0942 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 17.09 | 0.7143 | 0.1043 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 21.73 | 0.8064 | 0.0718 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 18.73 | 0.7237 | 0.1007 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 16.82 | 0.7154 | 0.1084 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 22.05 | 0.8187 | 0.0562 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 18.91 | 0.7450 | 0.0806 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 22.04 | 0.8183 | 0.0563 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 18.91 | 0.7449 | 0.0808 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 22.06 | 0.8188 | 0.0564 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 18.92 | 0.7453 | 0.0807 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 16.05 | 0.7034 | 0.1099 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 21.98 | 0.8170 | 0.0566 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 18.90 | 0.7443 | 0.0809 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 16.00 | 0.7033 | 0.1102 | 1.00 |
| hyb_risk[gs_center448_in] | 14.83 | 0.5272 | 0.1733 | 1.00 |
| hyb_risk[gs_center448_nat] | 14.97 | 0.5126 | 0.1753 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 14.85 | 0.5284 | 0.1721 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 15.04 | 0.5076 | 0.1823 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 12.26 | 0.5558 | 0.2353 | 1.00 |
| hyb_risk[gs_roi448_in] | 16.20 | 0.6223 | 0.1239 | 1.00 |
| hyb_risk[gs_roi448_nat] | 16.21 | 0.6222 | 0.1242 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 16.21 | 0.6229 | 0.1242 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 16.22 | 0.6209 | 0.1245 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 11.88 | 0.5784 | 0.2080 | 1.00 |
| hyb_risktuned[gs_center448_in] | 18.50 | 0.7326 | 0.0765 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 18.62 | 0.7248 | 0.0784 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 18.52 | 0.7331 | 0.0759 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 18.66 | 0.7223 | 0.0814 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 15.77 | 0.7068 | 0.1121 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 18.76 | 0.7521 | 0.0653 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 18.77 | 0.7519 | 0.0654 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 18.77 | 0.7524 | 0.0654 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 18.77 | 0.7510 | 0.0658 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 14.78 | 0.7052 | 0.1134 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 53.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 21.94 | 0.8774 | 0.0595 | 1.00 |
| flow_s0.5_pose | 21.30 | 0.8729 | 0.0607 | 1.00 |
| flow_s0.5_uniform | 21.47 | 0.8600 | 0.0660 | 1.00 |
| flow_s1.0_oracle | 21.23 | 0.8879 | 0.0598 | 1.00 |
| flow_s1.0_pose | 20.92 | 0.8826 | 0.0608 | 1.00 |
| flow_s1.0_uniform | 20.53 | 0.8603 | 0.0681 | 1.00 |
| gs_center448_in | 17.31 | 0.6239 | 0.1991 | 1.00 |
| gs_center448_in+reg | 23.61 | 0.8477 | 0.0937 | 0.98 |
| gs_center448_nat | 17.21 | 0.6040 | 0.2021 | 1.00 |
| gs_center448_nat+reg | 22.42 | 0.8202 | 0.1110 | 0.98 |
| gs_center448_nat_dil | 17.33 | 0.6248 | 0.1983 | 1.00 |
| gs_center448_nat_dil+reg | 23.61 | 0.8479 | 0.0928 | 0.98 |
| gs_center448_nat_mip | 7.28 | 0.4499 | 0.4482 | 1.00 |
| gs_center448_nat_mip+reg | 9.02 | 0.4735 | 0.4201 | 0.90 |
| gs_center448_nat_mip2d | 17.13 | 0.5969 | 0.2073 | 1.00 |
| gs_center448_nat_mip2d+reg | 21.74 | 0.8032 | 0.1260 | 0.98 |
| gs_roi448_in | 15.71 | 0.5793 | 0.2211 | 0.54 |
| gs_roi448_in+reg | 20.35 | 0.7694 | 0.1285 | 0.54 |
| gs_roi448_nat | 15.70 | 0.5788 | 0.2214 | 0.54 |
| gs_roi448_nat+reg | 20.31 | 0.7691 | 0.1309 | 0.54 |
| gs_roi448_nat_dil | 15.72 | 0.5801 | 0.2215 | 0.54 |
| gs_roi448_nat_dil+reg | 20.37 | 0.7702 | 0.1292 | 0.54 |
| gs_roi448_nat_mip | 7.94 | 0.4247 | 0.4721 | 0.54 |
| gs_roi448_nat_mip+reg | 7.91 | 0.4273 | 0.4717 | 0.54 |
| gs_roi448_nat_mip2d | 15.66 | 0.5768 | 0.2222 | 0.54 |
| gs_roi448_nat_mip2d+reg | 20.22 | 0.7676 | 0.1297 | 0.54 |
| hyb_oracle_fail[gs_center448_in+reg] | 24.94 | 0.8855 | 0.0646 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 21.21 | 0.8264 | 0.1021 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 24.22 | 0.8780 | 0.0709 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 21.16 | 0.8225 | 0.1043 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 24.93 | 0.8855 | 0.0645 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 21.22 | 0.8266 | 0.1019 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 19.10 | 0.8119 | 0.1088 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 23.90 | 0.8739 | 0.0755 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 21.16 | 0.8215 | 0.1059 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 18.54 | 0.8060 | 0.1175 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 24.41 | 0.8803 | 0.0621 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 21.27 | 0.8370 | 0.0856 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 24.39 | 0.8801 | 0.0622 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 21.27 | 0.8369 | 0.0857 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 24.42 | 0.8804 | 0.0623 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 21.28 | 0.8372 | 0.0857 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 18.00 | 0.8096 | 0.1112 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 24.31 | 0.8794 | 0.0625 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 21.26 | 0.8366 | 0.0858 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 17.96 | 0.8097 | 0.1114 | 1.00 |
| hyb_risk[gs_center448_in] | 18.38 | 0.7239 | 0.1445 | 1.00 |
| hyb_risk[gs_center448_nat] | 18.36 | 0.7144 | 0.1466 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 18.39 | 0.7243 | 0.1439 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 18.36 | 0.7116 | 0.1503 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 14.37 | 0.7012 | 0.1923 | 1.00 |
| hyb_risk[gs_roi448_in] | 19.05 | 0.7699 | 0.1179 | 1.00 |
| hyb_risk[gs_roi448_nat] | 19.05 | 0.7697 | 0.1181 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 19.06 | 0.7702 | 0.1180 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 19.04 | 0.7689 | 0.1184 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 14.12 | 0.7332 | 0.1791 | 1.00 |
| hyb_risktuned[gs_center448_in] | 20.96 | 0.8319 | 0.0850 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 20.97 | 0.8272 | 0.0863 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 20.97 | 0.8321 | 0.0847 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 20.98 | 0.8260 | 0.0878 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 17.77 | 0.8124 | 0.1090 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 20.85 | 0.8388 | 0.0753 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 20.85 | 0.8387 | 0.0754 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 20.86 | 0.8390 | 0.0754 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 20.83 | 0.8383 | 0.0756 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 16.71 | 0.8088 | 0.1139 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 64.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 32.67 | 0.9599 | 0.0256 | 1.00 |
| flow_s0.5_pose | 32.85 | 0.9613 | 0.0252 | 1.00 |
| flow_s0.5_uniform | 32.51 | 0.9556 | 0.0267 | 1.00 |
| flow_s1.0_oracle | 33.51 | 0.9611 | 0.0238 | 1.00 |
| flow_s1.0_pose | 33.36 | 0.9615 | 0.0240 | 1.00 |
| flow_s1.0_uniform | 32.96 | 0.9534 | 0.0256 | 1.00 |
| gs_center448_in | 19.77 | 0.7318 | 0.1587 | 1.00 |
| gs_center448_in+reg | 29.31 | 0.9234 | 0.0612 | 0.98 |
| gs_center448_nat | 19.42 | 0.7098 | 0.1614 | 1.00 |
| gs_center448_nat+reg | 27.17 | 0.8978 | 0.0738 | 0.98 |
| gs_center448_nat_dil | 19.79 | 0.7327 | 0.1575 | 1.00 |
| gs_center448_nat_dil+reg | 29.31 | 0.9234 | 0.0600 | 0.98 |
| gs_center448_nat_mip | 6.72 | 0.5319 | 0.4305 | 1.00 |
| gs_center448_nat_mip+reg | 8.04 | 0.5612 | 0.4088 | 0.91 |
| gs_center448_nat_mip2d | 19.22 | 0.7007 | 0.1676 | 1.00 |
| gs_center448_nat_mip2d+reg | 25.94 | 0.8824 | 0.0880 | 0.98 |
| gs_roi448_in | 19.15 | 0.7384 | 0.1613 | 0.45 |
| gs_roi448_in+reg | 23.27 | 0.8510 | 0.0888 | 0.44 |
| gs_roi448_nat | 19.12 | 0.7372 | 0.1620 | 0.45 |
| gs_roi448_nat+reg | 23.12 | 0.8497 | 0.0920 | 0.44 |
| gs_roi448_nat_dil | 19.16 | 0.7389 | 0.1614 | 0.45 |
| gs_roi448_nat_dil+reg | 23.30 | 0.8516 | 0.0890 | 0.44 |
| gs_roi448_nat_mip | 7.83 | 0.5212 | 0.4010 | 0.45 |
| gs_roi448_nat_mip+reg | 7.86 | 0.5256 | 0.4011 | 0.44 |
| gs_roi448_nat_mip2d | 19.01 | 0.7339 | 0.1636 | 0.45 |
| gs_roi448_nat_mip2d+reg | 23.09 | 0.8476 | 0.0903 | 0.44 |
| hyb_oracle_fail[gs_center448_in+reg] | 32.97 | 0.9523 | 0.0257 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 32.39 | 0.9458 | 0.0336 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 32.96 | 0.9516 | 0.0259 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 32.32 | 0.9454 | 0.0343 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 32.97 | 0.9523 | 0.0257 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 32.39 | 0.9458 | 0.0336 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 32.57 | 0.9475 | 0.0318 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 32.95 | 0.9511 | 0.0262 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 32.33 | 0.9453 | 0.0343 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 32.17 | 0.9451 | 0.0347 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 32.91 | 0.9520 | 0.0263 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 32.58 | 0.9494 | 0.0304 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 32.91 | 0.9520 | 0.0263 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 32.58 | 0.9494 | 0.0304 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 32.91 | 0.9520 | 0.0263 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 32.58 | 0.9494 | 0.0304 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 32.46 | 0.9479 | 0.0320 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 32.91 | 0.9520 | 0.0263 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 32.57 | 0.9494 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 32.46 | 0.9479 | 0.0320 | 1.00 |
| hyb_risk[gs_center448_in] | 31.65 | 0.9320 | 0.0487 | 1.00 |
| hyb_risk[gs_center448_nat] | 31.62 | 0.9304 | 0.0501 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 31.65 | 0.9320 | 0.0486 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 31.61 | 0.9297 | 0.0507 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 29.08 | 0.9098 | 0.0911 | 1.00 |
| hyb_risk[gs_roi448_in] | 32.10 | 0.9388 | 0.0451 | 1.00 |
| hyb_risk[gs_roi448_nat] | 32.10 | 0.9388 | 0.0452 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 32.10 | 0.9389 | 0.0451 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 32.08 | 0.9386 | 0.0454 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 29.75 | 0.9220 | 0.0774 | 1.00 |
| hyb_risktuned[gs_center448_in] | 32.96 | 0.9531 | 0.0256 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 32.96 | 0.9530 | 0.0256 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 32.96 | 0.9531 | 0.0256 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 32.96 | 0.9530 | 0.0256 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 32.93 | 0.9519 | 0.0262 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 32.96 | 0.9531 | 0.0256 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 32.96 | 0.9531 | 0.0256 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 32.96 | 0.9531 | 0.0256 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 32.96 | 0.9531 | 0.0256 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 32.91 | 0.9524 | 0.0268 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.53 | 0.9074 | 0.0593 | 1.00 |
| flow_s0.5_pose | 22.93 | 0.9061 | 0.0610 | 1.00 |
| flow_s0.5_uniform | 23.08 | 0.8944 | 0.0652 | 1.00 |
| flow_s1.0_oracle | 22.88 | 0.9145 | 0.0621 | 1.00 |
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| flow_s1.0_uniform | 22.18 | 0.8935 | 0.0691 | 1.00 |
| gs_center448_in | 17.48 | 0.6585 | 0.1854 | 1.00 |
| gs_center448_in+reg | 24.90 | 0.8756 | 0.1133 | 0.98 |
| gs_center448_nat | 17.28 | 0.6376 | 0.1837 | 1.00 |
| gs_center448_nat+reg | 23.41 | 0.8481 | 0.1193 | 0.98 |
| gs_center448_nat_dil | 17.49 | 0.6594 | 0.1818 | 1.00 |
| gs_center448_nat_dil+reg | 24.89 | 0.8757 | 0.1095 | 0.98 |
| gs_center448_nat_mip | 7.13 | 0.4764 | 0.5355 | 1.00 |
| gs_center448_nat_mip+reg | 8.43 | 0.4941 | 0.5141 | 0.91 |
| gs_center448_nat_mip2d | 17.16 | 0.6300 | 0.1930 | 1.00 |
| gs_center448_nat_mip2d+reg | 22.58 | 0.8315 | 0.1338 | 0.98 |
| gs_roi448_in | 16.18 | 0.6250 | 0.2080 | 0.54 |
| gs_roi448_in+reg | 20.94 | 0.7924 | 0.1434 | 0.54 |
| gs_roi448_nat | 16.17 | 0.6241 | 0.2085 | 0.54 |
| gs_roi448_nat+reg | 20.87 | 0.7913 | 0.1474 | 0.54 |
| gs_roi448_nat_dil | 16.19 | 0.6257 | 0.2087 | 0.54 |
| gs_roi448_nat_dil+reg | 20.96 | 0.7929 | 0.1442 | 0.53 |
| gs_roi448_nat_mip | 8.19 | 0.4581 | 0.5580 | 0.54 |
| gs_roi448_nat_mip+reg | 8.22 | 0.4618 | 0.5573 | 0.54 |
| gs_roi448_nat_mip2d | 16.12 | 0.6214 | 0.2095 | 0.54 |
| gs_roi448_nat_mip2d+reg | 20.82 | 0.7893 | 0.1444 | 0.54 |
| hyb_oracle_fail[gs_center448_in+reg] | 26.35 | 0.9097 | 0.0688 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 22.22 | 0.8635 | 0.1081 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 25.61 | 0.9039 | 0.0763 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 22.15 | 0.8603 | 0.1114 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 26.35 | 0.9096 | 0.0684 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 22.23 | 0.8637 | 0.1078 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 20.82 | 0.8600 | 0.1174 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 25.29 | 0.9007 | 0.0823 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 22.15 | 0.8596 | 0.1140 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 20.40 | 0.8592 | 0.1238 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 25.75 | 0.9053 | 0.0636 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 22.66 | 0.8732 | 0.0894 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 25.73 | 0.9052 | 0.0638 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 22.66 | 0.8732 | 0.0895 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 25.76 | 0.9054 | 0.0638 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 22.67 | 0.8733 | 0.0895 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 19.76 | 0.8571 | 0.1210 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 25.67 | 0.9048 | 0.0642 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 22.65 | 0.8730 | 0.0896 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 19.73 | 0.8570 | 0.1214 | 1.00 |
| hyb_risk[gs_center448_in] | 19.54 | 0.7929 | 0.1437 | 1.00 |
| hyb_risk[gs_center448_nat] | 19.50 | 0.7857 | 0.1477 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 19.55 | 0.7933 | 0.1426 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 19.51 | 0.7836 | 0.1540 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 16.38 | 0.7895 | 0.2035 | 1.00 |
| hyb_risk[gs_roi448_in] | 20.14 | 0.8231 | 0.1162 | 1.00 |
| hyb_risk[gs_roi448_nat] | 20.14 | 0.8229 | 0.1165 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 20.15 | 0.8233 | 0.1165 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 20.13 | 0.8224 | 0.1167 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 15.85 | 0.7959 | 0.1966 | 1.00 |
| hyb_risktuned[gs_center448_in] | 22.65 | 0.8756 | 0.0840 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 22.64 | 0.8721 | 0.0867 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 22.66 | 0.8757 | 0.0835 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 22.65 | 0.8713 | 0.0888 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 19.78 | 0.8657 | 0.1119 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 22.52 | 0.8800 | 0.0747 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 22.52 | 0.8799 | 0.0749 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 22.53 | 0.8800 | 0.0749 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 22.51 | 0.8796 | 0.0750 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 18.71 | 0.8620 | 0.1181 | 1.00 |

## 设置 cam5

物体区 PSNR 最好的 GS 变体：`gs_roi448_nat_dil`；整幅裁剪中最好的：`gs_center448_in`。调优风险阈值（扫描 IoU 最优）：warp=0.12, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 16.39 / 0.1129 | 16.23 / 0.0245 | 30.99 / 0.0316 | 26.19 / 0.0440 |
| flow_s1.0_pose | 20.41 / 0.0721 | 19.36 / 0.0188 | 31.36 / 0.0305 | 28.00 / 0.0396 |
| flow_s0.5_pose | 19.65 / 0.0818 | 18.59 / 0.0212 | 31.32 / 0.0317 | 27.45 / 0.0415 |
| gs_center448_in | 16.98 / 0.1794 | 16.46 / 0.0488 | 24.59 / 0.0976 | 22.92 / 0.1148 |
| gs_center448_in+reg | 17.69 / 0.1778 | 17.57 / 0.0367 | 28.07 / 0.0760 | 25.61 / 0.1007 |
| hyb_oracle_fail[gs_center448_in] | 17.55 / 0.1728 | 16.46 / 0.0488 | 30.97 / 0.0322 | 26.51 / 0.0576 |
| hyb_oracle_fail[gs_center448_in+reg] | 18.13 / 0.1697 | 17.57 / 0.0367 | 31.00 / 0.0316 | 27.22 / 0.0529 |
| hyb_risktuned[gs_center448_in] | 17.29 / 0.1659 | 17.21 / 0.0349 | 30.99 / 0.0317 | 26.37 / 0.0541 |
| hyb_risk[gs_center448_in] | 17.10 / 0.1779 | 16.88 / 0.0418 | 30.91 / 0.0339 | 25.57 / 0.0667 |
| gs_roi448_nat_dil | 17.49 / 0.1516 | 14.90 / 0.1231 | 18.53 / 0.1646 | 17.51 / 0.1628 |
| gs_roi448_nat_dil+reg | 19.00 / 0.1372 | 18.52 / 0.0575 | 27.24 / 0.0807 | 24.77 / 0.1064 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 17.88 / 0.1514 | 15.25 / 0.0525 | 30.78 / 0.0345 | 25.68 / 0.0570 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 19.37 / 0.1346 | 18.70 / 0.0293 | 31.00 / 0.0316 | 27.73 / 0.0473 |
| hyb_risktuned[gs_roi448_nat_dil] | 17.74 / 0.1461 | 17.01 / 0.0333 | 30.99 / 0.0319 | 25.97 / 0.0519 |
| hyb_risk[gs_roi448_nat_dil] | 17.70 / 0.1537 | 16.37 / 0.0425 | 30.67 / 0.0397 | 24.36 / 0.0692 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 22.32 | 0.8406 | 0.0684 | 1.00 |
| flow_s0.5_pose | 19.65 | 0.7479 | 0.0818 | 1.00 |
| flow_s0.5_uniform | 16.71 | 0.6135 | 0.1070 | 1.00 |
| flow_s1.0_oracle | 23.16 | 0.8541 | 0.0592 | 1.00 |
| flow_s1.0_pose | 20.41 | 0.7569 | 0.0721 | 1.00 |
| flow_s1.0_uniform | 16.39 | 0.5779 | 0.1129 | 1.00 |
| gs_center448_in | 16.98 | 0.6165 | 0.1794 | 1.00 |
| gs_center448_in+reg | 17.69 | 0.6488 | 0.1778 | 1.00 |
| gs_center448_nat | 16.86 | 0.6001 | 0.1812 | 1.00 |
| gs_center448_nat+reg | 17.54 | 0.6475 | 0.1754 | 1.00 |
| gs_center448_nat_dil | 16.97 | 0.6157 | 0.1774 | 1.00 |
| gs_center448_nat_dil+reg | 17.68 | 0.6473 | 0.1754 | 1.00 |
| gs_center448_nat_mip | 9.50 | 0.3211 | 0.6233 | 1.00 |
| gs_center448_nat_mip+reg | 11.20 | 0.2831 | 0.5896 | 0.81 |
| gs_center448_nat_mip2d | 16.75 | 0.5933 | 0.1881 | 1.00 |
| gs_center448_nat_mip2d+reg | 17.29 | 0.6344 | 0.1827 | 1.00 |
| gs_roi448_in | 17.49 | 0.6513 | 0.1505 | 1.00 |
| gs_roi448_in+reg | 19.04 | 0.7251 | 0.1359 | 1.00 |
| gs_roi448_nat | 17.47 | 0.6495 | 0.1507 | 1.00 |
| gs_roi448_nat+reg | 18.83 | 0.7188 | 0.1370 | 1.00 |
| gs_roi448_nat_dil | 17.49 | 0.6514 | 0.1516 | 1.00 |
| gs_roi448_nat_dil+reg | 19.00 | 0.7233 | 0.1372 | 1.00 |
| gs_roi448_nat_mip | 10.01 | 0.3445 | 0.6181 | 1.00 |
| gs_roi448_nat_mip+reg | 10.08 | 0.3501 | 0.6169 | 1.00 |
| gs_roi448_nat_mip2d | 17.41 | 0.6456 | 0.1507 | 1.00 |
| gs_roi448_nat_mip2d+reg | 18.70 | 0.7148 | 0.1376 | 1.00 |
| hyb_oracle_fail[gs_center448_in+reg] | 18.13 | 0.6489 | 0.1697 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 17.55 | 0.6244 | 0.1728 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 18.02 | 0.6465 | 0.1736 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 17.41 | 0.6101 | 0.1774 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 18.11 | 0.6474 | 0.1683 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 17.55 | 0.6232 | 0.1721 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 13.29 | 0.3600 | 0.3984 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 17.81 | 0.6360 | 0.1787 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 17.30 | 0.6043 | 0.1835 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 13.59 | 0.3947 | 0.3471 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 19.41 | 0.7133 | 0.1330 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 17.87 | 0.6463 | 0.1502 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 19.21 | 0.7074 | 0.1348 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 17.85 | 0.6448 | 0.1516 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 19.37 | 0.7113 | 0.1346 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 17.88 | 0.6464 | 0.1514 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 12.92 | 0.3763 | 0.3949 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 19.09 | 0.7043 | 0.1367 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 17.79 | 0.6424 | 0.1528 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 12.83 | 0.3724 | 0.3926 | 1.00 |
| hyb_risk[gs_center448_in] | 17.10 | 0.6091 | 0.1779 | 1.00 |
| hyb_risk[gs_center448_nat] | 17.04 | 0.5944 | 0.1774 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 17.10 | 0.6083 | 0.1764 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 16.94 | 0.5879 | 0.1832 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 13.14 | 0.4015 | 0.3861 | 1.00 |
| hyb_risk[gs_roi448_in] | 17.69 | 0.6455 | 0.1527 | 1.00 |
| hyb_risk[gs_roi448_nat] | 17.68 | 0.6439 | 0.1530 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 17.70 | 0.6456 | 0.1537 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 17.62 | 0.6405 | 0.1520 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 12.33 | 0.3951 | 0.4432 | 1.00 |
| hyb_risktuned[gs_center448_in] | 17.29 | 0.6104 | 0.1659 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 17.22 | 0.5969 | 0.1645 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 17.29 | 0.6099 | 0.1644 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 17.12 | 0.5909 | 0.1696 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 13.90 | 0.4485 | 0.3329 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 17.74 | 0.6445 | 0.1454 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 17.72 | 0.6430 | 0.1454 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 17.74 | 0.6445 | 0.1461 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 17.67 | 0.6401 | 0.1444 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 13.08 | 0.4387 | 0.3904 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 20.62 | 0.8233 | 0.0188 | 1.00 |
| flow_s0.5_pose | 18.59 | 0.7438 | 0.0212 | 1.00 |
| flow_s0.5_uniform | 16.33 | 0.6045 | 0.0263 | 1.00 |
| flow_s1.0_oracle | 21.48 | 0.8456 | 0.0166 | 1.00 |
| flow_s1.0_pose | 19.36 | 0.7667 | 0.0188 | 1.00 |
| flow_s1.0_uniform | 16.23 | 0.5746 | 0.0245 | 1.00 |
| gs_center448_in | 16.46 | 0.5925 | 0.0488 | 1.00 |
| gs_center448_in+reg | 17.57 | 0.6633 | 0.0367 | 1.00 |
| gs_center448_nat | 16.09 | 0.5698 | 0.0522 | 1.00 |
| gs_center448_nat+reg | 17.16 | 0.6553 | 0.0403 | 1.00 |
| gs_center448_nat_dil | 16.45 | 0.5901 | 0.0485 | 1.00 |
| gs_center448_nat_dil+reg | 17.56 | 0.6622 | 0.0366 | 1.00 |
| gs_center448_nat_mip | 10.04 | 0.2246 | 0.1263 | 1.00 |
| gs_center448_nat_mip+reg | 10.90 | 0.2018 | 0.1267 | 0.91 |
| gs_center448_nat_mip2d | 15.87 | 0.5617 | 0.0554 | 1.00 |
| gs_center448_nat_mip2d+reg | 16.71 | 0.6291 | 0.0466 | 1.00 |
| gs_roi448_in | 14.88 | 0.5244 | 0.1228 | 0.89 |
| gs_roi448_in+reg | 18.56 | 0.7147 | 0.0568 | 0.90 |
| gs_roi448_nat | 14.86 | 0.5227 | 0.1234 | 0.89 |
| gs_roi448_nat+reg | 18.38 | 0.7094 | 0.0583 | 0.90 |
| gs_roi448_nat_dil | 14.90 | 0.5252 | 0.1231 | 0.89 |
| gs_roi448_nat_dil+reg | 18.52 | 0.7132 | 0.0575 | 0.90 |
| gs_roi448_nat_mip | 9.96 | 0.2461 | 0.2380 | 0.89 |
| gs_roi448_nat_mip+reg | 10.05 | 0.2521 | 0.2378 | 0.89 |
| gs_roi448_nat_mip2d | 14.79 | 0.5183 | 0.1240 | 0.89 |
| gs_roi448_nat_mip2d+reg | 18.24 | 0.7063 | 0.0600 | 0.90 |
| hyb_oracle_fail[gs_center448_in+reg] | 17.57 | 0.6583 | 0.0367 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 16.46 | 0.5958 | 0.0488 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 17.17 | 0.6470 | 0.0403 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 16.09 | 0.5685 | 0.0524 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 17.56 | 0.6572 | 0.0366 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 16.45 | 0.5936 | 0.0485 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 12.56 | 0.3612 | 0.0849 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 16.77 | 0.6234 | 0.0469 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 15.90 | 0.5595 | 0.0564 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 13.01 | 0.4042 | 0.0706 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 18.73 | 0.7213 | 0.0291 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 15.23 | 0.5541 | 0.0524 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 18.57 | 0.7162 | 0.0296 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 15.21 | 0.5523 | 0.0526 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 18.70 | 0.7198 | 0.0293 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 15.25 | 0.5547 | 0.0525 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 10.91 | 0.3014 | 0.0898 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 18.43 | 0.7130 | 0.0301 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 15.14 | 0.5483 | 0.0528 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 10.80 | 0.2973 | 0.0897 | 1.00 |
| hyb_risk[gs_center448_in] | 16.88 | 0.6117 | 0.0418 | 1.00 |
| hyb_risk[gs_center448_nat] | 16.67 | 0.5952 | 0.0442 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 16.87 | 0.6100 | 0.0417 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 16.53 | 0.5899 | 0.0464 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 13.65 | 0.4471 | 0.0565 | 1.00 |
| hyb_risk[gs_roi448_in] | 16.36 | 0.6078 | 0.0423 | 1.00 |
| hyb_risk[gs_roi448_nat] | 16.33 | 0.6062 | 0.0426 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 16.37 | 0.6082 | 0.0425 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 16.25 | 0.6024 | 0.0429 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 11.82 | 0.3937 | 0.0736 | 1.00 |
| hyb_risktuned[gs_center448_in] | 17.21 | 0.6238 | 0.0349 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 17.00 | 0.6083 | 0.0365 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 17.21 | 0.6226 | 0.0348 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 16.90 | 0.6033 | 0.0384 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 14.21 | 0.4841 | 0.0485 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 17.00 | 0.6283 | 0.0333 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 16.98 | 0.6269 | 0.0334 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 17.01 | 0.6285 | 0.0333 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 16.91 | 0.6237 | 0.0334 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 12.52 | 0.4488 | 0.0610 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 16.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.58 | 0.8814 | 0.0201 | 1.00 |
| flow_s0.5_pose | 22.04 | 0.8474 | 0.0219 | 1.00 |
| flow_s0.5_uniform | 20.39 | 0.8038 | 0.0261 | 1.00 |
| flow_s1.0_oracle | 24.59 | 0.8971 | 0.0184 | 1.00 |
| flow_s1.0_pose | 22.99 | 0.8635 | 0.0202 | 1.00 |
| flow_s1.0_uniform | 20.69 | 0.8071 | 0.0252 | 1.00 |
| gs_center448_in | 18.80 | 0.6750 | 0.0621 | 1.00 |
| gs_center448_in+reg | 20.82 | 0.7711 | 0.0464 | 1.00 |
| gs_center448_nat | 18.70 | 0.6599 | 0.0632 | 1.00 |
| gs_center448_nat+reg | 20.28 | 0.7547 | 0.0479 | 1.00 |
| gs_center448_nat_dil | 18.80 | 0.6752 | 0.0614 | 1.00 |
| gs_center448_nat_dil+reg | 20.82 | 0.7721 | 0.0454 | 1.00 |
| gs_center448_nat_mip | 8.44 | 0.3406 | 0.2331 | 1.00 |
| gs_center448_nat_mip+reg | 9.41 | 0.3124 | 0.2415 | 0.89 |
| gs_center448_nat_mip2d | 18.44 | 0.6473 | 0.0694 | 1.00 |
| gs_center448_nat_mip2d+reg | 19.67 | 0.7246 | 0.0571 | 1.00 |
| gs_roi448_in | 16.36 | 0.5920 | 0.1248 | 0.73 |
| gs_roi448_in+reg | 21.14 | 0.7883 | 0.0606 | 0.74 |
| gs_roi448_nat | 16.36 | 0.5914 | 0.1251 | 0.73 |
| gs_roi448_nat+reg | 21.00 | 0.7866 | 0.0613 | 0.75 |
| gs_roi448_nat_dil | 16.38 | 0.5928 | 0.1252 | 0.73 |
| gs_roi448_nat_dil+reg | 21.12 | 0.7878 | 0.0613 | 0.74 |
| gs_roi448_nat_mip | 9.56 | 0.3856 | 0.3007 | 0.73 |
| gs_roi448_nat_mip+reg | 9.62 | 0.3842 | 0.3002 | 0.73 |
| gs_roi448_nat_mip2d | 16.33 | 0.5889 | 0.1258 | 0.73 |
| gs_roi448_nat_mip2d+reg | 20.86 | 0.7851 | 0.0625 | 0.75 |
| hyb_oracle_fail[gs_center448_in+reg] | 22.02 | 0.8285 | 0.0320 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 21.19 | 0.8035 | 0.0354 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 21.77 | 0.8226 | 0.0332 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 21.01 | 0.7945 | 0.0372 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 22.01 | 0.8282 | 0.0319 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 21.18 | 0.8030 | 0.0353 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 17.51 | 0.7101 | 0.0593 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 21.53 | 0.8156 | 0.0356 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 20.89 | 0.7913 | 0.0393 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 18.02 | 0.7356 | 0.0505 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 23.06 | 0.8501 | 0.0276 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 20.75 | 0.7989 | 0.0361 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 22.93 | 0.8482 | 0.0278 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 20.73 | 0.7981 | 0.0363 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 23.03 | 0.8495 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 20.76 | 0.7991 | 0.0362 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 16.30 | 0.6908 | 0.0640 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 22.82 | 0.8467 | 0.0280 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 20.65 | 0.7962 | 0.0366 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 16.15 | 0.6895 | 0.0637 | 1.00 |
| hyb_risk[gs_center448_in] | 18.80 | 0.6740 | 0.0621 | 1.00 |
| hyb_risk[gs_center448_nat] | 18.72 | 0.6593 | 0.0638 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 18.80 | 0.6742 | 0.0614 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 18.53 | 0.6478 | 0.0717 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 14.18 | 0.5890 | 0.1129 | 1.00 |
| hyb_risk[gs_roi448_in] | 17.69 | 0.6813 | 0.0662 | 1.00 |
| hyb_risk[gs_roi448_nat] | 17.69 | 0.6809 | 0.0664 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 17.71 | 0.6819 | 0.0664 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 17.67 | 0.6791 | 0.0666 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 11.93 | 0.5373 | 0.1304 | 1.00 |
| hyb_risktuned[gs_center448_in] | 20.38 | 0.7598 | 0.0390 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 20.30 | 0.7496 | 0.0391 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 20.38 | 0.7600 | 0.0385 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 20.19 | 0.7413 | 0.0436 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 16.16 | 0.6713 | 0.0717 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 20.03 | 0.7653 | 0.0351 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 20.02 | 0.7648 | 0.0352 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 20.04 | 0.7656 | 0.0352 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 19.98 | 0.7632 | 0.0353 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 13.27 | 0.6292 | 0.0862 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 25.75 | 0.9254 | 0.0358 | 1.00 |
| flow_s0.5_pose | 24.70 | 0.9115 | 0.0375 | 1.00 |
| flow_s0.5_uniform | 23.08 | 0.8860 | 0.0426 | 1.00 |
| flow_s1.0_oracle | 26.47 | 0.9327 | 0.0346 | 1.00 |
| flow_s1.0_pose | 25.35 | 0.9185 | 0.0361 | 1.00 |
| flow_s1.0_uniform | 23.41 | 0.8875 | 0.0417 | 1.00 |
| gs_center448_in | 21.48 | 0.7578 | 0.0882 | 1.00 |
| gs_center448_in+reg | 23.39 | 0.8476 | 0.0640 | 1.00 |
| gs_center448_nat | 21.08 | 0.7468 | 0.0943 | 1.00 |
| gs_center448_nat+reg | 22.39 | 0.8324 | 0.0757 | 1.00 |
| gs_center448_nat_dil | 21.48 | 0.7576 | 0.0878 | 1.00 |
| gs_center448_nat_dil+reg | 23.39 | 0.8483 | 0.0636 | 1.00 |
| gs_center448_nat_mip | 7.43 | 0.4369 | 0.3598 | 1.00 |
| gs_center448_nat_mip+reg | 8.92 | 0.4415 | 0.3814 | 0.88 |
| gs_center448_nat_mip2d | 20.71 | 0.7390 | 0.1018 | 1.00 |
| gs_center448_nat_mip2d+reg | 21.65 | 0.8059 | 0.0873 | 1.00 |
| gs_roi448_in | 17.36 | 0.6366 | 0.1335 | 0.56 |
| gs_roi448_in+reg | 22.82 | 0.8332 | 0.0706 | 0.58 |
| gs_roi448_nat | 17.34 | 0.6361 | 0.1339 | 0.56 |
| gs_roi448_nat+reg | 22.72 | 0.8337 | 0.0702 | 0.58 |
| gs_roi448_nat_dil | 17.38 | 0.6376 | 0.1337 | 0.56 |
| gs_roi448_nat_dil+reg | 22.82 | 0.8329 | 0.0707 | 0.58 |
| gs_roi448_nat_mip | 7.93 | 0.4187 | 0.3671 | 0.56 |
| gs_roi448_nat_mip+reg | 7.78 | 0.4157 | 0.3708 | 0.58 |
| gs_roi448_nat_mip2d | 17.28 | 0.6340 | 0.1346 | 0.56 |
| gs_roi448_nat_mip2d+reg | 22.55 | 0.8326 | 0.0720 | 0.58 |
| hyb_oracle_fail[gs_center448_in+reg] | 24.58 | 0.8980 | 0.0472 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 23.80 | 0.8838 | 0.0514 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 24.23 | 0.8945 | 0.0482 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 23.62 | 0.8795 | 0.0525 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 24.57 | 0.8978 | 0.0470 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 23.80 | 0.8836 | 0.0513 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 20.29 | 0.8334 | 0.0719 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 23.98 | 0.8907 | 0.0504 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 23.49 | 0.8779 | 0.0541 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 20.80 | 0.8469 | 0.0644 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 25.46 | 0.9092 | 0.0413 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 23.37 | 0.8828 | 0.0495 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 25.33 | 0.9084 | 0.0416 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 23.34 | 0.8825 | 0.0496 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 25.44 | 0.9089 | 0.0415 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 23.38 | 0.8829 | 0.0495 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 19.00 | 0.8259 | 0.0739 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 25.22 | 0.9076 | 0.0418 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 23.27 | 0.8817 | 0.0497 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 18.87 | 0.8252 | 0.0739 | 1.00 |
| hyb_risk[gs_center448_in] | 22.63 | 0.8453 | 0.0606 | 1.00 |
| hyb_risk[gs_center448_nat] | 22.38 | 0.8385 | 0.0632 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 22.63 | 0.8451 | 0.0604 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 22.21 | 0.8353 | 0.0666 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 18.09 | 0.7982 | 0.0890 | 1.00 |
| hyb_risk[gs_roi448_in] | 21.96 | 0.8482 | 0.0607 | 1.00 |
| hyb_risk[gs_roi448_nat] | 21.94 | 0.8479 | 0.0608 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 21.97 | 0.8485 | 0.0608 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 21.89 | 0.8472 | 0.0609 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 15.49 | 0.7736 | 0.1016 | 1.00 |
| hyb_risktuned[gs_center448_in] | 23.51 | 0.8724 | 0.0508 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 23.28 | 0.8670 | 0.0516 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 23.51 | 0.8723 | 0.0506 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 23.16 | 0.8648 | 0.0537 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 19.76 | 0.8380 | 0.0684 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 23.07 | 0.8723 | 0.0494 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 23.05 | 0.8721 | 0.0495 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 23.08 | 0.8725 | 0.0495 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 22.99 | 0.8714 | 0.0495 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 16.42 | 0.8053 | 0.0849 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 31.52 | 0.9667 | 0.0314 | 1.00 |
| flow_s0.5_pose | 31.32 | 0.9651 | 0.0317 | 1.00 |
| flow_s0.5_uniform | 30.95 | 0.9621 | 0.0336 | 1.00 |
| flow_s1.0_oracle | 31.57 | 0.9660 | 0.0302 | 1.00 |
| flow_s1.0_pose | 31.36 | 0.9646 | 0.0305 | 1.00 |
| flow_s1.0_uniform | 30.99 | 0.9612 | 0.0316 | 1.00 |
| gs_center448_in | 24.59 | 0.8328 | 0.0976 | 1.00 |
| gs_center448_in+reg | 28.07 | 0.9158 | 0.0760 | 0.99 |
| gs_center448_nat | 23.61 | 0.8167 | 0.0976 | 1.00 |
| gs_center448_nat+reg | 26.11 | 0.8993 | 0.0783 | 0.99 |
| gs_center448_nat_dil | 24.58 | 0.8328 | 0.0949 | 1.00 |
| gs_center448_nat_dil+reg | 28.07 | 0.9164 | 0.0734 | 0.99 |
| gs_center448_nat_mip | 6.68 | 0.5240 | 0.4526 | 1.00 |
| gs_center448_nat_mip+reg | 7.77 | 0.5396 | 0.4889 | 0.87 |
| gs_center448_nat_mip2d | 22.98 | 0.8076 | 0.1103 | 1.00 |
| gs_center448_nat_mip2d+reg | 24.65 | 0.8716 | 0.0932 | 1.00 |
| gs_roi448_in | 18.51 | 0.7026 | 0.1641 | 0.48 |
| gs_roi448_in+reg | 27.25 | 0.9031 | 0.0805 | 0.50 |
| gs_roi448_nat | 18.52 | 0.7023 | 0.1640 | 0.48 |
| gs_roi448_nat+reg | 27.24 | 0.9038 | 0.0797 | 0.50 |
| gs_roi448_nat_dil | 18.53 | 0.7034 | 0.1646 | 0.48 |
| gs_roi448_nat_dil+reg | 27.24 | 0.9033 | 0.0807 | 0.50 |
| gs_roi448_nat_mip | 8.13 | 0.4921 | 0.4471 | 0.48 |
| gs_roi448_nat_mip+reg | 7.97 | 0.4883 | 0.4614 | 0.50 |
| gs_roi448_nat_mip2d | 18.52 | 0.7007 | 0.1638 | 0.48 |
| gs_roi448_nat_mip2d+reg | 26.94 | 0.9020 | 0.0806 | 0.50 |
| hyb_oracle_fail[gs_center448_in+reg] | 31.00 | 0.9599 | 0.0316 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 30.97 | 0.9586 | 0.0322 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 30.99 | 0.9596 | 0.0316 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 30.96 | 0.9581 | 0.0324 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 31.00 | 0.9599 | 0.0316 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 30.97 | 0.9586 | 0.0322 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 30.61 | 0.9556 | 0.0375 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 30.96 | 0.9590 | 0.0319 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 30.94 | 0.9578 | 0.0327 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 30.62 | 0.9564 | 0.0363 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 31.00 | 0.9604 | 0.0316 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 30.78 | 0.9572 | 0.0345 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 31.00 | 0.9604 | 0.0316 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 30.78 | 0.9571 | 0.0345 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 31.00 | 0.9604 | 0.0316 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 30.78 | 0.9572 | 0.0345 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 30.17 | 0.9530 | 0.0402 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 31.00 | 0.9604 | 0.0316 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 30.78 | 0.9571 | 0.0346 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 30.17 | 0.9529 | 0.0403 | 1.00 |
| hyb_risk[gs_center448_in] | 30.91 | 0.9562 | 0.0339 | 1.00 |
| hyb_risk[gs_center448_nat] | 30.88 | 0.9555 | 0.0344 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 30.91 | 0.9562 | 0.0339 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 30.86 | 0.9550 | 0.0348 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 29.99 | 0.9481 | 0.0519 | 1.00 |
| hyb_risk[gs_roi448_in] | 30.67 | 0.9538 | 0.0398 | 1.00 |
| hyb_risk[gs_roi448_nat] | 30.67 | 0.9538 | 0.0397 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 30.67 | 0.9538 | 0.0397 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 30.67 | 0.9538 | 0.0398 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 29.46 | 0.9432 | 0.0603 | 1.00 |
| hyb_risktuned[gs_center448_in] | 30.99 | 0.9605 | 0.0317 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 30.99 | 0.9604 | 0.0317 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 30.99 | 0.9605 | 0.0317 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 30.99 | 0.9603 | 0.0318 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 30.81 | 0.9576 | 0.0367 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 30.99 | 0.9601 | 0.0319 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 30.99 | 0.9601 | 0.0319 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 30.99 | 0.9601 | 0.0319 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 30.99 | 0.9601 | 0.0319 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 30.44 | 0.9549 | 0.0427 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 28.40 | 0.9528 | 0.0403 | 1.00 |
| flow_s0.5_pose | 27.45 | 0.9461 | 0.0415 | 1.00 |
| flow_s0.5_uniform | 26.08 | 0.9340 | 0.0467 | 1.00 |
| flow_s1.0_oracle | 28.96 | 0.9545 | 0.0383 | 1.00 |
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| flow_s1.0_uniform | 26.19 | 0.9330 | 0.0440 | 1.00 |
| gs_center448_in | 22.92 | 0.8064 | 0.1148 | 1.00 |
| gs_center448_in+reg | 25.61 | 0.8914 | 0.1007 | 0.99 |
| gs_center448_nat | 22.15 | 0.7893 | 0.1111 | 1.00 |
| gs_center448_nat+reg | 24.25 | 0.8748 | 0.0989 | 0.99 |
| gs_center448_nat_dil | 22.92 | 0.8063 | 0.1107 | 1.00 |
| gs_center448_nat_dil+reg | 25.61 | 0.8920 | 0.0967 | 0.99 |
| gs_center448_nat_mip | 6.87 | 0.4907 | 0.5250 | 1.00 |
| gs_center448_nat_mip+reg | 7.96 | 0.4963 | 0.5726 | 0.87 |
| gs_center448_nat_mip2d | 21.62 | 0.7800 | 0.1246 | 1.00 |
| gs_center448_nat_mip2d+reg | 23.13 | 0.8471 | 0.1129 | 1.00 |
| gs_roi448_in | 17.50 | 0.6677 | 0.1621 | 0.52 |
| gs_roi448_in+reg | 24.79 | 0.8753 | 0.1055 | 0.54 |
| gs_roi448_nat | 17.50 | 0.6673 | 0.1619 | 0.52 |
| gs_roi448_nat+reg | 24.70 | 0.8754 | 0.1048 | 0.55 |
| gs_roi448_nat_dil | 17.51 | 0.6686 | 0.1628 | 0.52 |
| gs_roi448_nat_dil+reg | 24.77 | 0.8753 | 0.1064 | 0.54 |
| gs_roi448_nat_mip | 8.35 | 0.4574 | 0.5415 | 0.52 |
| gs_roi448_nat_mip+reg | 8.23 | 0.4549 | 0.5529 | 0.54 |
| gs_roi448_nat_mip2d | 17.49 | 0.6655 | 0.1615 | 0.52 |
| gs_roi448_nat_mip2d+reg | 24.48 | 0.8739 | 0.1056 | 0.54 |
| hyb_oracle_fail[gs_center448_in+reg] | 27.22 | 0.9365 | 0.0529 | 1.00 |
| hyb_oracle_fail[gs_center448_in] | 26.51 | 0.9288 | 0.0576 | 1.00 |
| hyb_oracle_fail[gs_center448_nat+reg] | 26.91 | 0.9353 | 0.0540 | 1.00 |
| hyb_oracle_fail[gs_center448_nat] | 26.26 | 0.9263 | 0.0592 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil+reg] | 27.22 | 0.9364 | 0.0526 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_dil] | 26.51 | 0.9287 | 0.0575 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip+reg] | 23.54 | 0.9091 | 0.0836 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d+reg] | 26.60 | 0.9331 | 0.0573 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip2d] | 26.11 | 0.9255 | 0.0618 | 1.00 |
| hyb_oracle_fail[gs_center448_nat_mip] | 23.95 | 0.9151 | 0.0735 | 1.00 |
| hyb_oracle_fail[gs_roi448_in+reg] | 27.75 | 0.9406 | 0.0471 | 1.00 |
| hyb_oracle_fail[gs_roi448_in] | 25.67 | 0.9252 | 0.0569 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat+reg] | 27.64 | 0.9403 | 0.0474 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat] | 25.65 | 0.9251 | 0.0570 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil+reg] | 27.73 | 0.9405 | 0.0473 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_dil] | 25.68 | 0.9253 | 0.0570 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip+reg] | 22.17 | 0.9024 | 0.0863 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d+reg] | 27.56 | 0.9401 | 0.0475 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip2d] | 25.60 | 0.9248 | 0.0570 | 1.00 |
| hyb_oracle_fail[gs_roi448_nat_mip] | 22.08 | 0.9023 | 0.0861 | 1.00 |
| hyb_risk[gs_center448_in] | 25.57 | 0.9110 | 0.0667 | 1.00 |
| hyb_risk[gs_center448_nat] | 25.27 | 0.9073 | 0.0691 | 1.00 |
| hyb_risk[gs_center448_nat_dil] | 25.57 | 0.9110 | 0.0663 | 1.00 |
| hyb_risk[gs_center448_nat_mip2d] | 25.08 | 0.9056 | 0.0743 | 1.00 |
| hyb_risk[gs_center448_nat_mip] | 21.65 | 0.8956 | 0.0993 | 1.00 |
| hyb_risk[gs_roi448_in] | 24.35 | 0.9081 | 0.0691 | 1.00 |
| hyb_risk[gs_roi448_nat] | 24.34 | 0.9079 | 0.0691 | 1.00 |
| hyb_risk[gs_roi448_nat_dil] | 24.36 | 0.9082 | 0.0692 | 1.00 |
| hyb_risk[gs_roi448_nat_mip2d] | 24.30 | 0.9076 | 0.0690 | 1.00 |
| hyb_risk[gs_roi448_nat_mip] | 19.32 | 0.8786 | 0.1218 | 1.00 |
| hyb_risktuned[gs_center448_in] | 26.37 | 0.9264 | 0.0541 | 1.00 |
| hyb_risktuned[gs_center448_nat] | 26.18 | 0.9242 | 0.0548 | 1.00 |
| hyb_risktuned[gs_center448_nat_dil] | 26.37 | 0.9264 | 0.0539 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip2d] | 26.08 | 0.9234 | 0.0576 | 1.00 |
| hyb_risktuned[gs_center448_nat_mip] | 23.20 | 0.9141 | 0.0750 | 1.00 |
| hyb_risktuned[gs_roi448_in] | 25.96 | 0.9260 | 0.0518 | 1.00 |
| hyb_risktuned[gs_roi448_nat] | 25.95 | 0.9259 | 0.0519 | 1.00 |
| hyb_risktuned[gs_roi448_nat_dil] | 25.97 | 0.9261 | 0.0519 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip2d] | 25.89 | 0.9256 | 0.0517 | 1.00 |
| hyb_risktuned[gs_roi448_nat_mip] | 20.47 | 0.9019 | 0.0922 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|
| cam3 | gs_center448_in | 10.48 | 1.00 |
| cam3 | gs_center448_nat | 10.33 | 1.00 |
| cam3 | gs_center448_nat_dil | 10.49 | 1.00 |
| cam3 | gs_center448_nat_mip | 227.46 | 1.00 |
| cam3 | gs_center448_nat_mip2d | 10.26 | 1.00 |
| cam3 | gs_roi448_in | 8.29 | 1.00 |
| cam3 | gs_roi448_nat | 8.31 | 1.00 |
| cam3 | gs_roi448_nat_dil | 8.31 | 1.00 |
| cam3 | gs_roi448_nat_mip | 2.60 | 1.00 |
| cam3 | gs_roi448_nat_mip2d | 8.40 | 1.00 |
| cam5 | gs_center448_in | 3.05 | 1.00 |
| cam5 | gs_center448_nat | 2.95 | 1.00 |
| cam5 | gs_center448_nat_dil | 3.05 | 1.00 |
| cam5 | gs_center448_nat_mip | 79.59 | 1.00 |
| cam5 | gs_center448_nat_mip2d | 2.44 | 1.00 |
| cam5 | gs_roi448_in | 7.50 | 1.00 |
| cam5 | gs_roi448_nat | 7.48 | 1.00 |
| cam5 | gs_roi448_nat_dil | 7.49 | 1.00 |
| cam5 | gs_roi448_nat_mip | 14.65 | 1.00 |
| cam5 | gs_roi448_nat_mip2d | 7.52 | 1.00 |

## 风险阈值扫描（风险区 vs oracle_fail，按 IoU 排序，前 8 名与配置默认值）

| 设置 | warp 阈值 | col 阈值 | 精确率 | 召回率 | IoU | 面积比 |
|---|---:|---:|---:|---:|---:|---:|
| cam3 | 0.20 | 4.0 | 0.458 | 0.631 | 0.353 | 1.48 |
| cam3 | 0.20 | 6.0 | 0.476 | 0.605 | 0.349 | 1.37 |
| cam3 | 0.15 | 6.0 | 0.426 | 0.698 | 0.349 | 1.81 |
| cam3 | 0.15 | 不用 | 0.434 | 0.687 | 0.349 | 1.76 |
| cam3 | 0.15 | 4.0 | 0.415 | 0.715 | 0.348 | 1.90 |
| cam3 | 0.25 | 4.0 | 0.481 | 0.574 | 0.347 | 1.26 |
| cam3 | 0.20 | 3.0 | 0.435 | 0.649 | 0.345 | 1.61 |
| cam3 | 0.20 | 不用 | 0.494 | 0.586 | 0.345 | 1.29 |
| cam3 | 0.08（默认） | 2.0 | 0.275 | 0.890 | 0.264 | 3.91 |
| cam5 | 0.12 | 2.0 | 0.338 | 0.583 | 0.271 | 1.73 |
| cam5 | 0.15 | 2.0 | 0.355 | 0.529 | 0.269 | 1.47 |
| cam5 | 0.10 | 不用 | 0.334 | 0.539 | 0.261 | 1.64 |
| cam5 | 0.12 | 3.0 | 0.343 | 0.517 | 0.260 | 1.51 |
| cam5 | 0.12 | 不用 | 0.379 | 0.449 | 0.259 | 1.18 |
| cam5 | 0.10 | 2.0 | 0.303 | 0.632 | 0.259 | 2.11 |
| cam5 | 0.08 | 不用 | 0.288 | 0.691 | 0.256 | 2.51 |
| cam5 | 0.10 | 6.0 | 0.322 | 0.545 | 0.254 | 1.73 |
| cam5 | 0.08（默认） | 2.0 | 0.268 | 0.743 | 0.246 | 2.88 |

## t 估计对比（scale=1.0）

| 设置 | 目标相机 | t_uniform | t_pose | t_oracle |
|---|---:|---:|---:|---:|
| cam3 | 1 | 0.250 | 0.305 | 0.320 |
| cam3 | 2 | 0.500 | 0.551 | 0.550 |
| cam3 | 3 | 0.750 | 0.802 | 0.760 |
| cam3 | 5 | 0.250 | 0.194 | 0.220 |
| cam3 | 6 | 0.500 | 0.463 | 0.470 |
| cam3 | 7 | 0.750 | 0.742 | 0.740 |
| cam5 | 1 | 0.500 | 0.554 | 0.560 |
| cam5 | 3 | 0.500 | 0.559 | 0.550 |
| cam5 | 5 | 0.500 | 0.419 | 0.450 |
| cam5 | 7 | 0.500 | 0.522 | 0.530 |

## AnySplat 运行统计

| 设置 | 变体 | 窗口边长 | 渲染分辨率 | 模式 | eps2d | 3D 滤波 | 高斯数 | 编码 s | 渲染 ms/视点 | 输入视点自渲染 PSNR | 最大旋转误差° | 最大光心误差/基线 |
|---|---|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|
| cam3 | gs_center448_in | 1080 | 448 | classic | 0.30 | False | 432575 | 0.817 | 2.7 | 29.28 | 0.37 | 0.008 |
| cam3 | gs_center448_nat | 1080 | 1080 | classic | 0.30 | False | 432575 | 0.817 | 7.7 | 29.28 | 0.37 | 0.008 |
| cam3 | gs_center448_nat_dil | 1080 | 1080 | classic | 1.74 | False | 432575 | 0.817 | 7.4 | 29.28 | 0.37 | 0.008 |
| cam3 | gs_center448_nat_mip | 1080 | 1080 | antialiased | 0.10 | True | 432575 | 0.817 | 107.6 | 29.28 | 0.37 | 0.008 |
| cam3 | gs_center448_nat_mip2d | 1080 | 1080 | antialiased | 0.10 | False | 432575 | 0.817 | 6.4 | 29.28 | 0.37 | 0.008 |
| cam3 | gs_roi448_in | 543 | 448 | classic | 0.30 | False | 182994 | 0.332 | 2.4 | 26.63 | 0.51 | 0.019 |
| cam3 | gs_roi448_nat | 543 | 543 | classic | 0.30 | False | 182994 | 0.332 | 2.4 | 26.63 | 0.51 | 0.019 |
| cam3 | gs_roi448_nat_dil | 543 | 543 | classic | 0.44 | False | 182994 | 0.332 | 2.3 | 26.63 | 0.51 | 0.019 |
| cam3 | gs_roi448_nat_mip | 543 | 543 | antialiased | 0.10 | True | 182994 | 0.332 | 2.3 | 26.63 | 0.51 | 0.019 |
| cam3 | gs_roi448_nat_mip2d | 543 | 543 | antialiased | 0.10 | False | 182994 | 0.332 | 2.5 | 26.63 | 0.51 | 0.019 |
| cam5 | gs_center448_in | 1080 | 448 | classic | 0.30 | False | 640053 | 0.526 | 3.2 | 29.86 | 0.14 | 0.007 |
| cam5 | gs_center448_nat | 1080 | 1080 | classic | 0.30 | False | 640053 | 0.526 | 7.3 | 29.86 | 0.14 | 0.007 |
| cam5 | gs_center448_nat_dil | 1080 | 1080 | classic | 1.74 | False | 640053 | 0.526 | 7.4 | 29.86 | 0.14 | 0.007 |
| cam5 | gs_center448_nat_mip | 1080 | 1080 | antialiased | 0.10 | True | 640053 | 0.526 | 6.8 | 29.86 | 0.14 | 0.007 |
| cam5 | gs_center448_nat_mip2d | 1080 | 1080 | antialiased | 0.10 | False | 640053 | 0.526 | 7.0 | 29.86 | 0.14 | 0.007 |
| cam5 | gs_roi448_in | 543 | 448 | classic | 0.30 | False | 269310 | 0.503 | 2.5 | 27.36 | 0.16 | 0.010 |
| cam5 | gs_roi448_nat | 543 | 543 | classic | 0.30 | False | 269310 | 0.503 | 2.7 | 27.36 | 0.16 | 0.010 |
| cam5 | gs_roi448_nat_dil | 543 | 543 | classic | 0.44 | False | 269310 | 0.503 | 2.7 | 27.36 | 0.16 | 0.010 |
| cam5 | gs_roi448_nat_mip | 543 | 543 | antialiased | 0.10 | True | 269310 | 0.503 | 2.8 | 27.36 | 0.16 | 0.010 |
| cam5 | gs_roi448_nat_mip2d | 543 | 543 | antialiased | 0.10 | False | 269310 | 0.503 | 3.1 | 27.36 | 0.16 | 0.010 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| cam3 | g_disp | 0.685 | 0.067 |
| cam3 | mask_ent | 0.537 | 0.067 |
| cam3 | mask_grad | 0.253 | 0.067 |
| cam3 | r_col | 0.844 | 0.067 |
| cam3 | r_warp | 0.898 | 0.067 |
| cam5 | g_disp | 0.711 | 0.031 |
| cam5 | mask_ent | 0.548 | 0.031 |
| cam5 | mask_grad | 0.257 | 0.031 |
| cam5 | r_col | 0.875 | 0.031 |
| cam5 | r_warp | 0.879 | 0.031 |

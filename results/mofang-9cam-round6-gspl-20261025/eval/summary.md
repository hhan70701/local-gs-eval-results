# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| cam3 | gs_tokr5448_nat_dil_al_local | 50.7% | 20.21 / 0.0585 | 22.84 / 0.0890 | 22.84 / 0.0890 | 0.00 |
| cam3 | gs_tokr5448_nat_dil_alv_local | 50.7% | 20.22 / 0.0586 | 22.76 / 0.0889 | 22.76 / 0.0889 | 0.00 |
| cam3 | gs_tokrife448_nat_dil_al_local | 19.9% | 16.71 / 0.0642 | 21.26 / 0.0588 | 21.16 / 0.0595 | 0.27 |
| cam3 | gs_tokrife448_nat_dil_alv_local | 19.8% | 16.72 / 0.0644 | 21.25 / 0.0589 | 21.13 / 0.0588 | 0.27 |
| cam3 | gs_tokstrict448_nat_dil_al_local | 15.9% | 15.87 / 0.0914 | 21.18 / 0.0727 | 20.95 / 0.0740 | 0.29 |
| cam3 | gs_tokstrict448_nat_dil_alv_local | 15.8% | 15.88 / 0.0913 | 20.77 / 0.0724 | 20.64 / 0.0737 | 0.36 |
| cam5 | gs_tokr5448_nat_dil_al_local | 38.6% | 25.63 / 0.0297 | 21.87 / 0.0770 | 22.14 / 0.0735 | 0.78 |
| cam5 | gs_tokr5448_nat_dil_alv_local | 38.6% | 25.64 / 0.0298 | 21.63 / 0.0775 | 22.15 / 0.0713 | 1.05 |
| cam5 | gs_tokrife448_nat_dil_al_local | 15.1% | 23.40 / 0.0375 | 22.41 / 0.0597 | 22.21 / 0.0611 | 1.44 |
| cam5 | gs_tokrife448_nat_dil_alv_local | 15.1% | 23.41 / 0.0379 | 22.24 / 0.0595 | 22.59 / 0.0582 | 0.61 |
| cam5 | gs_tokstrict448_nat_dil_al_local | 9.9% | 22.43 / 0.0668 | 15.64 / 0.2285 | 16.81 / 0.1982 | 10.27 |
| cam5 | gs_tokstrict448_nat_dil_alv_local | 9.9% | 22.43 / 0.0689 | 15.47 / 0.2287 | 17.54 / 0.1870 | 6.69 |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| cam3 | flow_s1.0_pose | 22.60 / 0.0629 | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 |
| cam3 | flow_s0.5_pose | 22.93 / 0.0610 | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_al_local] | 25.32 / 0.0826 | 17.09 / 0.1789 | 18.00 / 0.0480 | 31.22 / 0.0383 |
| cam3 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.21 / 0.0823 | 16.76 / 0.1825 | 17.80 / 0.0478 | 31.26 / 0.0380 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_al_local] | 26.15 / 0.0579 | 16.83 / 0.1789 | 18.20 / 0.0397 | 33.08 / 0.0265 |
| cam3 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 26.10 / 0.0581 | 16.62 / 0.1863 | 18.16 / 0.0401 | 33.07 / 0.0266 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 26.31 / 0.0558 | 17.01 / 0.1891 | 18.36 / 0.0392 | 33.30 / 0.0252 |
| cam3 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.98 / 0.0565 | 16.12 / 0.1983 | 17.91 / 0.0400 | 33.29 / 0.0253 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.32 / 0.0826 | 17.09 / 0.1789 | 18.00 / 0.0480 | 31.22 / 0.0383 |
| cam3 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.21 / 0.0823 | 16.76 / 0.1825 | 17.80 / 0.0478 | 31.26 / 0.0380 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 26.06 / 0.0582 | 16.76 / 0.1805 | 18.12 / 0.0406 | 33.07 / 0.0266 |
| cam3 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 26.04 / 0.0582 | 16.61 / 0.1859 | 18.11 / 0.0408 | 33.07 / 0.0266 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 26.11 / 0.0563 | 16.77 / 0.1915 | 18.12 / 0.0400 | 33.25 / 0.0253 |
| cam3 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.87 / 0.0569 | 16.09 / 0.2010 | 17.81 / 0.0409 | 33.26 / 0.0254 |
| cam5 | flow_s1.0_pose | 28.00 / 0.0396 | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 |
| cam5 | flow_s0.5_pose | 27.45 / 0.0415 | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_al_local] | 25.14 / 0.0771 | 18.15 / 0.1529 | 16.39 / 0.0338 | 28.02 / 0.0597 |
| cam5 | hyb_token[gs_tokr5448_nat_dil_alv_local] | 24.94 / 0.0773 | 17.62 / 0.1566 | 15.97 / 0.0350 | 27.95 / 0.0595 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.81 / 0.0474 | 19.15 / 0.1322 | 18.67 / 0.0205 | 30.58 / 0.0361 |
| cam5 | hyb_token[gs_tokrife448_nat_dil_alv_local] | 27.76 / 0.0473 | 18.95 / 0.1341 | 18.54 / 0.0206 | 30.65 / 0.0359 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_al_local] | 24.00 / 0.0617 | 16.17 / 0.1854 | 14.83 / 0.0364 | 27.68 / 0.0463 |
| cam5 | hyb_token[gs_tokstrict448_nat_dil_alv_local] | 23.89 / 0.0614 | 16.01 / 0.1860 | 14.70 / 0.0359 | 27.60 / 0.0465 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.51 / 0.0766 | 17.91 / 0.1553 | 17.05 / 0.0325 | 28.14 / 0.0580 |
| cam5 | hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.54 / 0.0755 | 17.86 / 0.1554 | 17.12 / 0.0318 | 28.20 / 0.0565 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 27.65 / 0.0482 | 19.00 / 0.1307 | 18.62 / 0.0219 | 30.45 / 0.0361 |
| cam5 | hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 27.84 / 0.0468 | 19.42 / 0.1275 | 18.91 / 0.0200 | 30.57 / 0.0356 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 24.68 / 0.0626 | 16.06 / 0.1864 | 15.69 / 0.0335 | 27.82 / 0.0476 |
| cam5 | hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.43 / 0.0589 | 16.63 / 0.1788 | 15.78 / 0.0328 | 29.18 / 0.0433 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| cam3 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.2%） | — | — | 22.60 / 0.0629 | 14.53 / 0.2724 | 33.53 |
| cam3 | r5 | 30.7% | 50.7% | 25.32 / 0.0826 | 17.09 / 0.1789 | 31.22 |
| cam3 | rife | 10.8% | 19.9% | 26.15 / 0.0579 | 16.83 / 0.1789 | 33.08 |
| cam3 | strict | 8.4% | 15.9% | 26.31 / 0.0558 | 17.01 / 0.1891 | 33.30 |
| cam5 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.2%） | — | — | 28.00 / 0.0396 | 20.41 / 0.0721 | 31.46 |
| cam5 | r5 | 15.7% | 38.6% | 25.14 / 0.0771 | 18.15 / 0.1529 | 28.02 |
| cam5 | rife | 3.9% | 15.1% | 27.81 / 0.0474 | 19.15 / 0.1322 | 30.58 |
| cam5 | strict | 2.4% | 9.9% | 24.00 / 0.0617 | 16.17 / 0.1854 | 27.68 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 cam3

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：aligned_int → `gs_tokr5448_nat_dil_al`，aligned_vggt → `gs_tokr5448_nat_dil_alv`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=6.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 13.02 / 0.2906 | 12.52 / 0.0568 | 32.36 / 0.0269 | 22.18 / 0.0691 |
| flow_s1.0_pose | 14.53 / 0.2724 | 12.70 / 0.0513 | 33.53 / 0.0233 | 22.60 / 0.0629 |
| flow_s0.5_pose | 14.85 / 0.2383 | 13.30 / 0.0482 | 32.82 / 0.0252 | 22.93 / 0.0610 |
| gs_tokr5448_nat_dil_al | 18.35 / 0.1466 | 18.39 / 0.0458 | 29.15 / 0.0545 | 25.04 / 0.0940 |
| gs_tokr5448_nat_dil_al+reg | 18.35 / 0.1522 | 18.74 / 0.0443 | 29.50 / 0.0524 | 25.40 / 0.0941 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 19.19 / 0.1491 | 18.39 / 0.0458 | 33.53 / 0.0235 | 27.05 / 0.0569 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 17.17 / 0.1749 | 17.28 / 0.0427 | 33.54 / 0.0233 | 25.89 / 0.0584 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 19.11 / 0.1544 | 18.74 / 0.0443 | 33.54 / 0.0234 | 27.20 / 0.0568 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 17.12 / 0.1805 | 17.37 / 0.0431 | 33.54 / 0.0233 | 25.96 / 0.0591 |
| gs_tokr5448_nat_dil_alv | 17.81 / 0.1501 | 18.11 / 0.0458 | 29.30 / 0.0540 | 24.94 / 0.0935 |
| gs_tokr5448_nat_dil_alv+reg | 18.28 / 0.1507 | 18.78 / 0.0435 | 29.59 / 0.0515 | 25.47 / 0.0934 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 18.63 / 0.1508 | 18.11 / 0.0458 | 33.53 / 0.0235 | 26.88 / 0.0568 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 16.95 / 0.1752 | 17.11 / 0.0426 | 33.54 / 0.0233 | 25.77 / 0.0583 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 19.00 / 0.1507 | 18.78 / 0.0435 | 33.54 / 0.0234 | 27.23 / 0.0563 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 17.21 / 0.1747 | 17.40 / 0.0428 | 33.54 / 0.0233 | 25.99 / 0.0589 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 16.10 | 0.5746 | 0.1984 | 1.00 |
| flow_s0.5_pose | 14.85 | 0.5040 | 0.2383 | 1.00 |
| flow_s0.5_uniform | 14.21 | 0.5001 | 0.2198 | 1.00 |
| flow_s1.0_oracle | 15.16 | 0.5837 | 0.2651 | 1.00 |
| flow_s1.0_pose | 14.53 | 0.5347 | 0.2724 | 1.00 |
| flow_s1.0_uniform | 13.02 | 0.4647 | 0.2906 | 1.00 |
| gs_tokr5448_nat_dil_al | 18.35 | 0.6855 | 0.1466 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 18.35 | 0.6838 | 0.1522 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 17.80 | 0.6654 | 0.1671 | 1.00 |
| gs_tokr5448_nat_dil_alv | 17.81 | 0.6729 | 0.1501 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 18.28 | 0.6911 | 0.1507 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.33 | 0.6538 | 0.1716 | 1.00 |
| gs_tokrife448_nat_dil_al | 18.02 | 0.6629 | 0.1504 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 17.87 | 0.6550 | 0.1552 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 17.32 | 0.6353 | 0.1760 | 1.00 |
| gs_tokrife448_nat_dil_alv | 17.80 | 0.6583 | 0.1513 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 18.25 | 0.6761 | 0.1474 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 17.05 | 0.6285 | 0.1831 | 1.00 |
| gs_tokstrict448_nat_dil_al | 18.14 | 0.6695 | 0.1513 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 18.14 | 0.6695 | 0.1513 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 17.29 | 0.6360 | 0.1906 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 17.07 | 0.6209 | 0.1622 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 17.07 | 0.6209 | 0.1622 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 16.35 | 0.5868 | 0.2058 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 19.11 | 0.7120 | 0.1544 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 19.19 | 0.7143 | 0.1491 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 19.00 | 0.7138 | 0.1507 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 18.63 | 0.7016 | 0.1508 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 18.56 | 0.6859 | 0.1479 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 18.77 | 0.6940 | 0.1478 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 18.95 | 0.7060 | 0.1421 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 18.56 | 0.6915 | 0.1487 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 18.88 | 0.7014 | 0.1481 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 18.88 | 0.7014 | 0.1481 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 17.92 | 0.6657 | 0.1591 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 17.92 | 0.6657 | 0.1591 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 17.26 | 0.6656 | 0.1734 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 17.31 | 0.6678 | 0.1678 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 17.27 | 0.6732 | 0.1722 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 16.88 | 0.6559 | 0.1715 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 16.93 | 0.6415 | 0.1729 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 17.07 | 0.6494 | 0.1683 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 17.22 | 0.6609 | 0.1650 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 16.82 | 0.6430 | 0.1686 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 17.17 | 0.6553 | 0.1707 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 17.17 | 0.6553 | 0.1707 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 16.12 | 0.6062 | 0.1817 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 16.12 | 0.6062 | 0.1817 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 17.12 | 0.6766 | 0.1805 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 17.17 | 0.6759 | 0.1749 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 17.21 | 0.6826 | 0.1747 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 16.95 | 0.6709 | 0.1752 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 16.88 | 0.6586 | 0.1731 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 17.02 | 0.6645 | 0.1688 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 17.25 | 0.6767 | 0.1659 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 16.91 | 0.6633 | 0.1698 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 17.11 | 0.6699 | 0.1749 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 17.11 | 0.6699 | 0.1749 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 16.23 | 0.6280 | 0.1825 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 16.23 | 0.6280 | 0.1825 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 17.09 | 0.6544 | 0.1789 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 16.76 | 0.6453 | 0.1825 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 16.83 | 0.6334 | 0.1789 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 16.62 | 0.6284 | 0.1863 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 17.01 | 0.6392 | 0.1891 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 16.12 | 0.5953 | 0.1983 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 17.09 | 0.6544 | 0.1789 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 16.76 | 0.6453 | 0.1825 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 16.76 | 0.6303 | 0.1805 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 16.61 | 0.6288 | 0.1859 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 16.77 | 0.6265 | 0.1915 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 16.09 | 0.5939 | 0.2010 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 14.17 | 0.5985 | 0.0457 | 1.00 |
| flow_s0.5_pose | 13.30 | 0.5443 | 0.0482 | 1.00 |
| flow_s0.5_uniform | 13.88 | 0.5654 | 0.0513 | 1.00 |
| flow_s1.0_oracle | 13.03 | 0.5914 | 0.0498 | 1.00 |
| flow_s1.0_pose | 12.70 | 0.5482 | 0.0513 | 1.00 |
| flow_s1.0_uniform | 12.52 | 0.5342 | 0.0568 | 1.00 |
| gs_tokr5448_nat_dil_al | 18.39 | 0.7184 | 0.0458 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 18.74 | 0.7279 | 0.0443 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.59 | 0.6968 | 0.0489 | 1.00 |
| gs_tokr5448_nat_dil_alv | 18.11 | 0.7131 | 0.0458 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 18.78 | 0.7305 | 0.0435 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.35 | 0.6929 | 0.0488 | 1.00 |
| gs_tokrife448_nat_dil_al | 18.18 | 0.7164 | 0.0460 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 18.62 | 0.7262 | 0.0425 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.78 | 0.6010 | 0.1027 | 1.00 |
| gs_tokrife448_nat_dil_alv | 18.05 | 0.7169 | 0.0463 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 18.78 | 0.7349 | 0.0420 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 12.76 | 0.6016 | 0.1032 | 1.00 |
| gs_tokstrict448_nat_dil_al | 17.41 | 0.6935 | 0.0565 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 17.41 | 0.6935 | 0.0565 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 11.37 | 0.5440 | 0.1298 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 17.00 | 0.6774 | 0.0574 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 17.00 | 0.6774 | 0.0574 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 11.28 | 0.5275 | 0.1307 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 18.74 | 0.7192 | 0.0443 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 18.39 | 0.7081 | 0.0458 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 18.78 | 0.7218 | 0.0435 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 18.11 | 0.7025 | 0.0458 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 18.62 | 0.7177 | 0.0425 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 18.18 | 0.7063 | 0.0459 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 18.78 | 0.7262 | 0.0420 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 18.05 | 0.7063 | 0.0462 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 17.41 | 0.6859 | 0.0565 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 17.41 | 0.6859 | 0.0565 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 17.00 | 0.6694 | 0.0574 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 17.00 | 0.6694 | 0.0574 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 17.84 | 0.7137 | 0.0461 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 17.60 | 0.7070 | 0.0466 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 17.87 | 0.7163 | 0.0454 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 17.38 | 0.7019 | 0.0467 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 17.74 | 0.7141 | 0.0443 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 17.44 | 0.7072 | 0.0470 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 17.85 | 0.7215 | 0.0441 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 17.33 | 0.7070 | 0.0473 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 16.83 | 0.6842 | 0.0572 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 16.83 | 0.6842 | 0.0572 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 16.45 | 0.6680 | 0.0580 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 16.45 | 0.6680 | 0.0580 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 17.37 | 0.7057 | 0.0431 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 17.28 | 0.7017 | 0.0427 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 17.40 | 0.7082 | 0.0428 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 17.11 | 0.6983 | 0.0426 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 17.25 | 0.7045 | 0.0416 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 17.22 | 0.7040 | 0.0418 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 17.43 | 0.7131 | 0.0414 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 17.16 | 0.7042 | 0.0418 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 16.99 | 0.6933 | 0.0473 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 16.99 | 0.6933 | 0.0473 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 16.65 | 0.6796 | 0.0478 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 16.65 | 0.6796 | 0.0478 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 18.00 | 0.6996 | 0.0480 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 17.80 | 0.6958 | 0.0478 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.20 | 0.7034 | 0.0397 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 18.16 | 0.7043 | 0.0401 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 18.36 | 0.7042 | 0.0392 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 17.91 | 0.6895 | 0.0400 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 18.00 | 0.6996 | 0.0480 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.80 | 0.6958 | 0.0478 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 18.12 | 0.6979 | 0.0406 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 18.11 | 0.6998 | 0.0408 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 18.12 | 0.6947 | 0.0400 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 17.81 | 0.6857 | 0.0409 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.99 | 0.8166 | 0.0498 | 1.00 |
| flow_s0.5_pose | 19.41 | 0.8102 | 0.0518 | 1.00 |
| flow_s0.5_uniform | 19.42 | 0.7885 | 0.0548 | 1.00 |
| flow_s1.0_oracle | 19.19 | 0.8296 | 0.0544 | 1.00 |
| flow_s1.0_pose | 18.94 | 0.8220 | 0.0548 | 1.00 |
| flow_s1.0_uniform | 18.45 | 0.7883 | 0.0601 | 1.00 |
| gs_tokr5448_nat_dil_al | 22.12 | 0.8041 | 0.0667 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 22.32 | 0.8111 | 0.0668 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 16.46 | 0.7552 | 0.1096 | 1.00 |
| gs_tokr5448_nat_dil_alv | 21.97 | 0.8043 | 0.0663 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 22.39 | 0.8144 | 0.0661 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 16.40 | 0.7562 | 0.1086 | 1.00 |
| gs_tokrife448_nat_dil_al | 19.77 | 0.7937 | 0.0781 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 20.02 | 0.8043 | 0.0762 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.93 | 0.6269 | 0.2478 | 1.00 |
| gs_tokrife448_nat_dil_alv | 19.73 | 0.7930 | 0.0779 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 20.15 | 0.8089 | 0.0750 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 9.92 | 0.6263 | 0.2475 | 1.00 |
| gs_tokstrict448_nat_dil_al | 17.02 | 0.7611 | 0.1082 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 17.02 | 0.7611 | 0.1082 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 8.67 | 0.5712 | 0.2914 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 16.93 | 0.7562 | 0.1085 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 16.93 | 0.7562 | 0.1085 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 8.64 | 0.5660 | 0.2916 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 23.52 | 0.8554 | 0.0513 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 23.40 | 0.8541 | 0.0515 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 23.52 | 0.8558 | 0.0508 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 23.20 | 0.8522 | 0.0515 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 23.43 | 0.8552 | 0.0493 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 23.28 | 0.8529 | 0.0509 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 23.55 | 0.8571 | 0.0492 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 23.19 | 0.8524 | 0.0510 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 22.66 | 0.8420 | 0.0559 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 22.66 | 0.8420 | 0.0559 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 22.36 | 0.8383 | 0.0564 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 22.36 | 0.8383 | 0.0564 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 22.32 | 0.8088 | 0.0668 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 22.12 | 0.8018 | 0.0667 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 22.39 | 0.8121 | 0.0661 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 21.97 | 0.8020 | 0.0663 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 22.11 | 0.8067 | 0.0683 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 21.72 | 0.7960 | 0.0707 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 22.19 | 0.8109 | 0.0673 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 21.58 | 0.7951 | 0.0707 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 18.32 | 0.7587 | 0.0980 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 18.32 | 0.7587 | 0.0980 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 18.17 | 0.7537 | 0.0983 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 18.17 | 0.7537 | 0.0983 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 22.97 | 0.8513 | 0.0477 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 22.94 | 0.8505 | 0.0470 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 23.03 | 0.8523 | 0.0473 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 22.82 | 0.8499 | 0.0468 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 23.03 | 0.8523 | 0.0449 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 23.00 | 0.8512 | 0.0448 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 23.21 | 0.8550 | 0.0445 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 22.95 | 0.8516 | 0.0447 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 22.09 | 0.8398 | 0.0498 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 22.09 | 0.8398 | 0.0498 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 21.82 | 0.8358 | 0.0499 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 21.82 | 0.8358 | 0.0499 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 21.64 | 0.7852 | 0.0789 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 21.54 | 0.7857 | 0.0783 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.56 | 0.8322 | 0.0523 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 22.49 | 0.8323 | 0.0518 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 22.68 | 0.8399 | 0.0492 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 22.36 | 0.8362 | 0.0488 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 21.64 | 0.7852 | 0.0789 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 21.54 | 0.7857 | 0.0783 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 22.47 | 0.8295 | 0.0526 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 22.44 | 0.8299 | 0.0522 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 22.49 | 0.8370 | 0.0496 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 22.27 | 0.8342 | 0.0490 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 52.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 21.88 | 0.8768 | 0.0597 | 1.00 |
| flow_s0.5_pose | 21.24 | 0.8722 | 0.0608 | 1.00 |
| flow_s0.5_uniform | 21.45 | 0.8596 | 0.0657 | 1.00 |
| flow_s1.0_oracle | 21.12 | 0.8872 | 0.0601 | 1.00 |
| flow_s1.0_pose | 20.84 | 0.8820 | 0.0609 | 1.00 |
| flow_s1.0_uniform | 20.48 | 0.8603 | 0.0677 | 1.00 |
| gs_tokr5448_nat_dil_al | 23.90 | 0.8590 | 0.0829 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 24.21 | 0.8643 | 0.0810 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 23.42 | 0.8426 | 0.0941 | 1.00 |
| gs_tokr5448_nat_dil_alv | 23.76 | 0.8592 | 0.0823 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 24.28 | 0.8664 | 0.0799 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 23.29 | 0.8432 | 0.0933 | 1.00 |
| gs_tokrife448_nat_dil_al | 16.60 | 0.8339 | 0.1046 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 16.71 | 0.8402 | 0.1006 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.09 | 0.6642 | 0.2810 | 1.00 |
| gs_tokrife448_nat_dil_alv | 16.63 | 0.8336 | 0.1051 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 16.76 | 0.8441 | 0.1006 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 9.09 | 0.6640 | 0.2816 | 1.00 |
| gs_tokstrict448_nat_dil_al | 13.33 | 0.7764 | 0.1507 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 13.33 | 0.7764 | 0.1507 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 8.27 | 0.6178 | 0.3250 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 13.31 | 0.7734 | 0.1517 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 13.31 | 0.7734 | 0.1517 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 8.26 | 0.6145 | 0.3264 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 25.83 | 0.9045 | 0.0545 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 25.70 | 0.9037 | 0.0549 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 25.86 | 0.9049 | 0.0539 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 25.52 | 0.9027 | 0.0548 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 25.73 | 0.9052 | 0.0523 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 25.54 | 0.9037 | 0.0541 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 25.86 | 0.9064 | 0.0522 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 25.47 | 0.9037 | 0.0542 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 24.69 | 0.8960 | 0.0600 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 24.69 | 0.8960 | 0.0600 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 24.41 | 0.8940 | 0.0607 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 24.41 | 0.8940 | 0.0607 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 24.06 | 0.8763 | 0.0714 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 23.84 | 0.8721 | 0.0722 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 24.12 | 0.8778 | 0.0708 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 23.70 | 0.8717 | 0.0721 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 24.00 | 0.8776 | 0.0702 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 23.68 | 0.8721 | 0.0735 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 24.06 | 0.8798 | 0.0704 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 23.56 | 0.8715 | 0.0741 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 20.17 | 0.8425 | 0.0929 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 20.17 | 0.8425 | 0.0929 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 20.01 | 0.8394 | 0.0940 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 20.01 | 0.8394 | 0.0940 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 24.53 | 0.8984 | 0.0571 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 24.45 | 0.8977 | 0.0567 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 24.56 | 0.8987 | 0.0570 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 24.32 | 0.8968 | 0.0567 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 24.51 | 0.8993 | 0.0551 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 24.45 | 0.8986 | 0.0554 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 24.66 | 0.9008 | 0.0551 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 24.42 | 0.8987 | 0.0555 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 23.58 | 0.8918 | 0.0590 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 23.58 | 0.8918 | 0.0590 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 23.33 | 0.8894 | 0.0594 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 23.33 | 0.8894 | 0.0594 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 24.14 | 0.8632 | 0.0769 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 24.01 | 0.8630 | 0.0768 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.96 | 0.8917 | 0.0566 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 24.93 | 0.8915 | 0.0569 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 25.01 | 0.8956 | 0.0544 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 24.67 | 0.8929 | 0.0555 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 24.14 | 0.8632 | 0.0769 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 24.01 | 0.8630 | 0.0768 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 24.89 | 0.8905 | 0.0569 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 24.88 | 0.8904 | 0.0573 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 24.80 | 0.8936 | 0.0548 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 24.55 | 0.8913 | 0.0557 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 32.45 | 0.9592 | 0.0262 | 1.00 |
| flow_s0.5_pose | 32.82 | 0.9610 | 0.0252 | 1.00 |
| flow_s0.5_uniform | 32.06 | 0.9533 | 0.0285 | 1.00 |
| flow_s1.0_oracle | 33.41 | 0.9610 | 0.0236 | 1.00 |
| flow_s1.0_pose | 33.53 | 0.9618 | 0.0233 | 1.00 |
| flow_s1.0_uniform | 32.36 | 0.9509 | 0.0269 | 1.00 |
| gs_tokr5448_nat_dil_al | 29.15 | 0.9279 | 0.0545 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 29.50 | 0.9307 | 0.0524 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 24.38 | 0.9104 | 0.0752 | 1.00 |
| gs_tokr5448_nat_dil_alv | 29.30 | 0.9300 | 0.0540 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 29.59 | 0.9325 | 0.0515 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 24.46 | 0.9128 | 0.0743 | 1.00 |
| gs_tokrife448_nat_dil_al | 15.62 | 0.8843 | 0.0820 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 15.65 | 0.8866 | 0.0798 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.42 | 0.6621 | 0.3053 | 1.00 |
| gs_tokrife448_nat_dil_alv | 15.65 | 0.8851 | 0.0819 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 15.69 | 0.8894 | 0.0792 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 7.42 | 0.6620 | 0.3054 | 1.00 |
| gs_tokstrict448_nat_dil_al | 12.81 | 0.8292 | 0.1362 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 12.81 | 0.8292 | 0.1362 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 6.92 | 0.6402 | 0.3503 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 12.81 | 0.8289 | 0.1365 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 12.81 | 0.8289 | 0.1365 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 6.92 | 0.6398 | 0.3505 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 33.54 | 0.9613 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 33.53 | 0.9611 | 0.0235 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 33.54 | 0.9613 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 33.53 | 0.9611 | 0.0235 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 33.54 | 0.9614 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 33.54 | 0.9612 | 0.0234 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 33.54 | 0.9614 | 0.0233 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 33.54 | 0.9612 | 0.0235 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 33.52 | 0.9609 | 0.0236 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 33.52 | 0.9609 | 0.0236 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 33.52 | 0.9608 | 0.0237 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 33.52 | 0.9608 | 0.0237 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 33.48 | 0.9585 | 0.0239 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 33.46 | 0.9582 | 0.0243 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 33.49 | 0.9586 | 0.0238 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 33.46 | 0.9583 | 0.0242 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 33.40 | 0.9579 | 0.0247 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 33.37 | 0.9575 | 0.0251 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 33.40 | 0.9581 | 0.0246 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 33.37 | 0.9576 | 0.0251 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 31.68 | 0.9476 | 0.0376 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 31.68 | 0.9476 | 0.0376 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 31.68 | 0.9476 | 0.0377 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 31.68 | 0.9476 | 0.0377 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 33.54 | 0.9618 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 33.54 | 0.9617 | 0.0233 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 33.53 | 0.9615 | 0.0234 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 31.22 | 0.9471 | 0.0383 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 31.26 | 0.9475 | 0.0380 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 33.08 | 0.9590 | 0.0265 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 33.07 | 0.9590 | 0.0266 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 33.30 | 0.9600 | 0.0252 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 33.29 | 0.9599 | 0.0253 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 31.22 | 0.9471 | 0.0383 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 31.26 | 0.9475 | 0.0380 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 33.07 | 0.9590 | 0.0266 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 33.07 | 0.9590 | 0.0266 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 33.25 | 0.9600 | 0.0253 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 33.26 | 0.9599 | 0.0254 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.53 | 0.9074 | 0.0593 | 1.00 |
| flow_s0.5_pose | 22.93 | 0.9061 | 0.0610 | 1.00 |
| flow_s0.5_uniform | 23.08 | 0.8944 | 0.0652 | 1.00 |
| flow_s1.0_oracle | 22.88 | 0.9145 | 0.0621 | 1.00 |
| flow_s1.0_pose | 22.60 | 0.9115 | 0.0629 | 1.00 |
| flow_s1.0_uniform | 22.18 | 0.8935 | 0.0691 | 1.00 |
| gs_tokr5448_nat_dil_al | 25.04 | 0.8838 | 0.0940 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 25.40 | 0.8891 | 0.0941 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 23.35 | 0.8682 | 0.1181 | 1.00 |
| gs_tokr5448_nat_dil_alv | 24.94 | 0.8848 | 0.0935 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 25.47 | 0.8913 | 0.0934 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 23.31 | 0.8698 | 0.1172 | 1.00 |
| gs_tokrife448_nat_dil_al | 16.79 | 0.8538 | 0.1165 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 16.87 | 0.8589 | 0.1144 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.45 | 0.6606 | 0.3536 | 1.00 |
| gs_tokrife448_nat_dil_alv | 16.81 | 0.8540 | 0.1165 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 16.92 | 0.8628 | 0.1148 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 8.45 | 0.6603 | 0.3540 | 1.00 |
| gs_tokstrict448_nat_dil_al | 13.92 | 0.8070 | 0.1700 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 13.92 | 0.8070 | 0.1700 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.74 | 0.6248 | 0.4082 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 13.91 | 0.8048 | 0.1704 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 13.91 | 0.8048 | 0.1704 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.73 | 0.6224 | 0.4091 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 27.20 | 0.9262 | 0.0568 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 27.05 | 0.9253 | 0.0569 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 27.23 | 0.9263 | 0.0563 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 26.88 | 0.9245 | 0.0568 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 27.07 | 0.9258 | 0.0542 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 26.92 | 0.9249 | 0.0560 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 27.20 | 0.9268 | 0.0542 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 26.84 | 0.9249 | 0.0559 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 26.29 | 0.9209 | 0.0618 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 26.29 | 0.9209 | 0.0618 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 26.02 | 0.9195 | 0.0624 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 26.02 | 0.9195 | 0.0624 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 25.46 | 0.9055 | 0.0757 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 25.22 | 0.9020 | 0.0753 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 25.52 | 0.9067 | 0.0754 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 25.09 | 0.9019 | 0.0752 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 25.33 | 0.9047 | 0.0740 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 25.03 | 0.9010 | 0.0762 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 25.41 | 0.9066 | 0.0744 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 24.91 | 0.9006 | 0.0765 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 22.02 | 0.8821 | 0.0965 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 22.02 | 0.8821 | 0.0965 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 21.86 | 0.8800 | 0.0971 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 21.86 | 0.8800 | 0.0971 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 25.96 | 0.9222 | 0.0591 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 25.89 | 0.9215 | 0.0584 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 25.99 | 0.9223 | 0.0589 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 25.77 | 0.9209 | 0.0583 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 25.91 | 0.9219 | 0.0565 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 25.87 | 0.9216 | 0.0566 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 26.03 | 0.9230 | 0.0564 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 25.83 | 0.9216 | 0.0564 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 25.27 | 0.9181 | 0.0604 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 25.27 | 0.9181 | 0.0604 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 25.02 | 0.9166 | 0.0606 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 25.02 | 0.9166 | 0.0606 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 25.32 | 0.8945 | 0.0826 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 25.21 | 0.8946 | 0.0823 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.15 | 0.9166 | 0.0579 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 26.10 | 0.9164 | 0.0581 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 26.31 | 0.9196 | 0.0558 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 25.98 | 0.9177 | 0.0565 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.32 | 0.8945 | 0.0826 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.21 | 0.8946 | 0.0823 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 26.06 | 0.9156 | 0.0582 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 26.04 | 0.9155 | 0.0582 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 26.11 | 0.9185 | 0.0563 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.87 | 0.9169 | 0.0569 | 1.00 |

## 设置 cam5

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：aligned_int → `gs_tokrife448_nat_dil_al`，aligned_vggt → `gs_tokrife448_nat_dil_alv`。调优风险阈值（扫描 IoU 最优）：warp=0.2, col=3.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_uniform | 16.39 / 0.1129 | 15.31 / 0.0249 | 30.29 / 0.0331 | 26.19 / 0.0440 |
| flow_s1.0_pose | 20.41 / 0.0721 | 17.62 / 0.0175 | 31.46 / 0.0305 | 28.00 / 0.0396 |
| flow_s0.5_pose | 19.65 / 0.0818 | 17.06 / 0.0195 | 31.22 / 0.0318 | 27.45 / 0.0415 |
| gs_tokrife448_nat_dil_al | 19.20 / 0.1260 | 18.14 / 0.0270 | 18.20 / 0.0886 | 18.52 / 0.1025 |
| gs_tokrife448_nat_dil_al+reg | 19.49 / 0.1218 | 18.48 / 0.0271 | 18.29 / 0.0877 | 18.63 / 0.1034 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 20.77 / 0.1062 | 18.14 / 0.0270 | 31.44 / 0.0307 | 28.50 / 0.0448 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 21.09 / 0.0785 | 19.26 / 0.0188 | 31.45 / 0.0305 | 28.41 / 0.0411 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 21.04 / 0.1052 | 18.48 / 0.0271 | 31.45 / 0.0306 | 28.62 / 0.0452 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 21.17 / 0.0787 | 19.28 / 0.0194 | 31.45 / 0.0305 | 28.41 / 0.0413 |
| gs_tokrife448_nat_dil_alv | 19.09 / 0.1258 | 18.04 / 0.0273 | 18.16 / 0.0889 | 18.47 / 0.1024 |
| gs_tokrife448_nat_dil_alv+reg | 19.18 / 0.1236 | 18.16 / 0.0277 | 18.24 / 0.0879 | 18.56 / 0.1036 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 20.66 / 0.1066 | 18.04 / 0.0273 | 31.44 / 0.0308 | 28.44 / 0.0448 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 20.86 / 0.0800 | 19.12 / 0.0190 | 31.46 / 0.0305 | 28.30 / 0.0411 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 20.73 / 0.1056 | 18.16 / 0.0277 | 31.45 / 0.0306 | 28.48 / 0.0454 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 20.87 / 0.0810 | 19.06 / 0.0197 | 31.46 / 0.0305 | 28.27 / 0.0413 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 22.32 | 0.8406 | 0.0684 | 1.00 |
| flow_s0.5_pose | 19.65 | 0.7479 | 0.0818 | 1.00 |
| flow_s0.5_uniform | 16.71 | 0.6135 | 0.1070 | 1.00 |
| flow_s1.0_oracle | 23.16 | 0.8541 | 0.0592 | 1.00 |
| flow_s1.0_pose | 20.41 | 0.7569 | 0.0721 | 1.00 |
| flow_s1.0_uniform | 16.39 | 0.5779 | 0.1129 | 1.00 |
| gs_tokr5448_nat_dil_al | 18.32 | 0.6736 | 0.1389 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 18.85 | 0.7100 | 0.1332 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.07 | 0.6581 | 0.1585 | 1.00 |
| gs_tokr5448_nat_dil_alv | 17.81 | 0.6642 | 0.1414 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 18.67 | 0.7112 | 0.1345 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 17.56 | 0.6500 | 0.1595 | 1.00 |
| gs_tokrife448_nat_dil_al | 19.20 | 0.7222 | 0.1260 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 19.49 | 0.7392 | 0.1218 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 18.75 | 0.7037 | 0.1478 | 1.00 |
| gs_tokrife448_nat_dil_alv | 19.09 | 0.7234 | 0.1258 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 19.18 | 0.7290 | 0.1236 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 18.65 | 0.7062 | 0.1462 | 1.00 |
| gs_tokstrict448_nat_dil_al | 15.85 | 0.5502 | 0.2043 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 16.92 | 0.6182 | 0.1855 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 14.89 | 0.5142 | 0.2556 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 15.76 | 0.5628 | 0.2010 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 16.84 | 0.5995 | 0.1838 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 14.89 | 0.5215 | 0.2558 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 20.41 | 0.7603 | 0.1150 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 19.80 | 0.7398 | 0.1194 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 20.21 | 0.7560 | 0.1156 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 19.27 | 0.7253 | 0.1203 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 21.04 | 0.7787 | 0.1052 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 20.77 | 0.7738 | 0.1062 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 20.73 | 0.7674 | 0.1056 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 20.66 | 0.7687 | 0.1066 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 18.81 | 0.7008 | 0.1473 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 17.29 | 0.6448 | 0.1672 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 18.59 | 0.6871 | 0.1453 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 17.25 | 0.6592 | 0.1612 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 19.22 | 0.7300 | 0.1247 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 18.76 | 0.7041 | 0.1314 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 19.03 | 0.7296 | 0.1248 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 18.23 | 0.6911 | 0.1333 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 19.97 | 0.7569 | 0.1119 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 19.75 | 0.7478 | 0.1151 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 19.63 | 0.7457 | 0.1146 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 19.58 | 0.7452 | 0.1156 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 17.44 | 0.6408 | 0.1721 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 16.40 | 0.5870 | 0.1883 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 17.35 | 0.6250 | 0.1691 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 16.29 | 0.6014 | 0.1856 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 20.72 | 0.7772 | 0.0899 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 20.52 | 0.7686 | 0.0914 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 20.54 | 0.7759 | 0.0921 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 20.05 | 0.7554 | 0.0972 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 21.17 | 0.7975 | 0.0787 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 21.09 | 0.7960 | 0.0785 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 20.87 | 0.7899 | 0.0810 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 20.86 | 0.7914 | 0.0800 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 18.76 | 0.6997 | 0.1328 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 18.11 | 0.6799 | 0.1380 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 18.63 | 0.6879 | 0.1309 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 18.03 | 0.6922 | 0.1349 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 18.15 | 0.6629 | 0.1529 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 17.62 | 0.6530 | 0.1566 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.15 | 0.7209 | 0.1322 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 18.95 | 0.7196 | 0.1341 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 16.17 | 0.5767 | 0.1854 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 16.01 | 0.5828 | 0.1860 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 17.91 | 0.6492 | 0.1553 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.86 | 0.6574 | 0.1554 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 19.00 | 0.7165 | 0.1307 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 19.42 | 0.7428 | 0.1275 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 16.06 | 0.5772 | 0.1864 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 16.63 | 0.6042 | 0.1788 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 19.18 | 0.7600 | 0.0171 | 1.00 |
| flow_s0.5_pose | 17.06 | 0.6711 | 0.0195 | 1.00 |
| flow_s0.5_uniform | 15.30 | 0.5755 | 0.0247 | 1.00 |
| flow_s1.0_oracle | 19.73 | 0.7659 | 0.0154 | 1.00 |
| flow_s1.0_pose | 17.62 | 0.6745 | 0.0175 | 1.00 |
| flow_s1.0_uniform | 15.31 | 0.5619 | 0.0249 | 1.00 |
| gs_tokr5448_nat_dil_al | 16.27 | 0.6224 | 0.0337 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 17.91 | 0.6902 | 0.0276 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 16.32 | 0.6145 | 0.0354 | 1.00 |
| gs_tokr5448_nat_dil_alv | 15.82 | 0.6020 | 0.0350 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 17.79 | 0.6884 | 0.0279 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 15.88 | 0.5941 | 0.0367 | 1.00 |
| gs_tokrife448_nat_dil_al | 18.14 | 0.7145 | 0.0270 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 18.48 | 0.7212 | 0.0271 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.60 | 0.5639 | 0.0709 | 1.00 |
| gs_tokrife448_nat_dil_alv | 18.04 | 0.7098 | 0.0273 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 18.16 | 0.7083 | 0.0277 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 12.56 | 0.5600 | 0.0711 | 1.00 |
| gs_tokstrict448_nat_dil_al | 12.98 | 0.4052 | 0.0700 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 15.01 | 0.4752 | 0.0576 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 10.50 | 0.3264 | 0.0991 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 12.83 | 0.4190 | 0.0697 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 14.84 | 0.4552 | 0.0583 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 10.50 | 0.3413 | 0.0984 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 17.91 | 0.6882 | 0.0276 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 16.27 | 0.6173 | 0.0337 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 17.79 | 0.6859 | 0.0279 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 15.82 | 0.5962 | 0.0350 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 18.48 | 0.7185 | 0.0271 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 18.14 | 0.7107 | 0.0270 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 18.16 | 0.7057 | 0.0277 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 18.04 | 0.7061 | 0.0273 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 15.04 | 0.5235 | 0.0571 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 13.00 | 0.4287 | 0.0694 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 14.86 | 0.5049 | 0.0578 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 12.84 | 0.4383 | 0.0691 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 18.10 | 0.6996 | 0.0266 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 16.81 | 0.6509 | 0.0302 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 17.98 | 0.6978 | 0.0269 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 16.37 | 0.6319 | 0.0310 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 18.85 | 0.7343 | 0.0244 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 18.68 | 0.7310 | 0.0237 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 18.58 | 0.7233 | 0.0248 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 18.60 | 0.7268 | 0.0239 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 15.71 | 0.5375 | 0.0465 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 13.88 | 0.4841 | 0.0544 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 15.53 | 0.5196 | 0.0470 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 13.69 | 0.4982 | 0.0538 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 18.61 | 0.7198 | 0.0217 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 17.87 | 0.6939 | 0.0227 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 18.50 | 0.7181 | 0.0219 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 17.48 | 0.6774 | 0.0236 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 19.28 | 0.7491 | 0.0194 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 19.26 | 0.7489 | 0.0188 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 19.06 | 0.7413 | 0.0197 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 19.12 | 0.7439 | 0.0190 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 17.14 | 0.6169 | 0.0300 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 15.94 | 0.5937 | 0.0345 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 16.97 | 0.6035 | 0.0308 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 15.68 | 0.6020 | 0.0336 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 16.39 | 0.6234 | 0.0338 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 15.97 | 0.6054 | 0.0350 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.67 | 0.7291 | 0.0205 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 18.54 | 0.7227 | 0.0206 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 14.83 | 0.5558 | 0.0364 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 14.70 | 0.5637 | 0.0359 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 17.05 | 0.6413 | 0.0325 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 17.12 | 0.6492 | 0.0318 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 18.62 | 0.7203 | 0.0219 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 18.91 | 0.7398 | 0.0200 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 15.69 | 0.5636 | 0.0335 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 15.78 | 0.5750 | 0.0328 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 17.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 23.73 | 0.8826 | 0.0204 | 1.00 |
| flow_s0.5_pose | 22.21 | 0.8504 | 0.0224 | 1.00 |
| flow_s0.5_uniform | 20.55 | 0.8064 | 0.0266 | 1.00 |
| flow_s1.0_oracle | 24.76 | 0.8987 | 0.0188 | 1.00 |
| flow_s1.0_pose | 23.17 | 0.8669 | 0.0208 | 1.00 |
| flow_s1.0_uniform | 20.86 | 0.8093 | 0.0253 | 1.00 |
| gs_tokr5448_nat_dil_al | 20.24 | 0.7489 | 0.0461 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 21.57 | 0.7954 | 0.0398 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.84 | 0.7232 | 0.0562 | 1.00 |
| gs_tokr5448_nat_dil_alv | 19.97 | 0.7434 | 0.0464 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 21.48 | 0.7945 | 0.0400 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.58 | 0.7174 | 0.0565 | 1.00 |
| gs_tokrife448_nat_dil_al | 21.24 | 0.7893 | 0.0411 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 21.42 | 0.7993 | 0.0400 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.78 | 0.5887 | 0.1741 | 1.00 |
| gs_tokrife448_nat_dil_alv | 21.14 | 0.7875 | 0.0414 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 21.22 | 0.7931 | 0.0406 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 9.77 | 0.5866 | 0.1744 | 1.00 |
| gs_tokstrict448_nat_dil_al | 14.54 | 0.5354 | 0.1186 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 15.54 | 0.5812 | 0.1041 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 8.36 | 0.4150 | 0.2126 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 14.42 | 0.5386 | 0.1189 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 15.49 | 0.5723 | 0.1041 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 8.38 | 0.4195 | 0.2124 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 23.67 | 0.8666 | 0.0255 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 22.63 | 0.8507 | 0.0278 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 23.57 | 0.8652 | 0.0254 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 22.25 | 0.8441 | 0.0281 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 24.28 | 0.8762 | 0.0244 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 24.18 | 0.8756 | 0.0241 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 24.08 | 0.8722 | 0.0246 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 24.11 | 0.8737 | 0.0241 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 21.45 | 0.8191 | 0.0374 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 19.92 | 0.7905 | 0.0431 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 21.30 | 0.8139 | 0.0375 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 19.74 | 0.7948 | 0.0425 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 21.57 | 0.7949 | 0.0398 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 20.24 | 0.7492 | 0.0461 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 21.48 | 0.7940 | 0.0400 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 19.97 | 0.7437 | 0.0464 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 21.57 | 0.7976 | 0.0397 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 21.39 | 0.7886 | 0.0408 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 21.35 | 0.7913 | 0.0403 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 21.28 | 0.7864 | 0.0411 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 16.20 | 0.5830 | 0.0958 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 15.06 | 0.5358 | 0.1114 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 16.13 | 0.5741 | 0.0957 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 14.93 | 0.5388 | 0.1116 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 23.34 | 0.8613 | 0.0250 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 22.76 | 0.8501 | 0.0255 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 23.26 | 0.8610 | 0.0250 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 22.45 | 0.8449 | 0.0258 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 23.92 | 0.8725 | 0.0232 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 23.96 | 0.8724 | 0.0230 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 23.71 | 0.8689 | 0.0235 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 23.80 | 0.8703 | 0.0232 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 20.66 | 0.7962 | 0.0327 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 19.92 | 0.7797 | 0.0349 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 20.51 | 0.7903 | 0.0327 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 19.64 | 0.7826 | 0.0349 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 20.08 | 0.7367 | 0.0486 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 19.82 | 0.7307 | 0.0489 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.82 | 0.8470 | 0.0295 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 22.63 | 0.8445 | 0.0298 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 18.47 | 0.7543 | 0.0431 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 18.29 | 0.7569 | 0.0430 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 20.37 | 0.7392 | 0.0477 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 20.37 | 0.7413 | 0.0469 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 22.59 | 0.8399 | 0.0312 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 22.96 | 0.8511 | 0.0293 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 19.18 | 0.7589 | 0.0433 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 19.38 | 0.7688 | 0.0399 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 25.73 | 0.9248 | 0.0355 | 1.00 |
| flow_s0.5_pose | 24.65 | 0.9099 | 0.0374 | 1.00 |
| flow_s0.5_uniform | 23.02 | 0.8845 | 0.0430 | 1.00 |
| flow_s1.0_oracle | 26.44 | 0.9323 | 0.0341 | 1.00 |
| flow_s1.0_pose | 25.29 | 0.9172 | 0.0359 | 1.00 |
| flow_s1.0_uniform | 23.35 | 0.8857 | 0.0419 | 1.00 |
| gs_tokr5448_nat_dil_al | 22.38 | 0.8284 | 0.0672 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 23.87 | 0.8620 | 0.0565 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 18.23 | 0.7950 | 0.1012 | 1.00 |
| gs_tokr5448_nat_dil_alv | 22.13 | 0.8250 | 0.0678 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 23.80 | 0.8617 | 0.0569 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 18.15 | 0.7917 | 0.1018 | 1.00 |
| gs_tokrife448_nat_dil_al | 19.11 | 0.8321 | 0.0764 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 19.22 | 0.8406 | 0.0748 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.50 | 0.6206 | 0.2566 | 1.00 |
| gs_tokrife448_nat_dil_alv | 19.06 | 0.8313 | 0.0764 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 19.14 | 0.8381 | 0.0752 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 8.50 | 0.6205 | 0.2564 | 1.00 |
| gs_tokstrict448_nat_dil_al | 12.54 | 0.6196 | 0.1902 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 12.98 | 0.6518 | 0.1804 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.97 | 0.5289 | 0.2924 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 12.53 | 0.6217 | 0.1908 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 12.95 | 0.6468 | 0.1809 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.97 | 0.5317 | 0.2927 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 25.86 | 0.9179 | 0.0394 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 24.90 | 0.9098 | 0.0421 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 25.76 | 0.9170 | 0.0396 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 24.52 | 0.9064 | 0.0430 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 26.38 | 0.9216 | 0.0385 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 26.31 | 0.9215 | 0.0382 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 26.16 | 0.9195 | 0.0389 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 26.19 | 0.9204 | 0.0383 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 23.84 | 0.8930 | 0.0501 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 22.34 | 0.8765 | 0.0546 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 23.66 | 0.8897 | 0.0502 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 22.21 | 0.8793 | 0.0547 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 24.46 | 0.8922 | 0.0469 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 23.29 | 0.8743 | 0.0524 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 24.36 | 0.8916 | 0.0473 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 23.00 | 0.8707 | 0.0530 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 24.64 | 0.8952 | 0.0464 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 24.50 | 0.8921 | 0.0470 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 24.46 | 0.8927 | 0.0468 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 24.41 | 0.8912 | 0.0470 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 20.71 | 0.8076 | 0.0758 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 19.30 | 0.7817 | 0.0837 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 20.61 | 0.8034 | 0.0760 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 19.17 | 0.7843 | 0.0842 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 25.37 | 0.9147 | 0.0382 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 24.93 | 0.9100 | 0.0392 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 25.29 | 0.9144 | 0.0383 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 24.61 | 0.9071 | 0.0398 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 25.95 | 0.9200 | 0.0367 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 25.95 | 0.9199 | 0.0367 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 25.78 | 0.9184 | 0.0368 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 25.81 | 0.9189 | 0.0367 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 23.81 | 0.8912 | 0.0445 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 22.53 | 0.8783 | 0.0469 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 23.71 | 0.8888 | 0.0449 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 22.32 | 0.8806 | 0.0471 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 22.41 | 0.8376 | 0.0644 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 22.18 | 0.8345 | 0.0650 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.36 | 0.9093 | 0.0408 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 25.25 | 0.9088 | 0.0408 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 21.33 | 0.8619 | 0.0546 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 21.16 | 0.8638 | 0.0546 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 22.93 | 0.8425 | 0.0636 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 22.97 | 0.8439 | 0.0621 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 25.20 | 0.9058 | 0.0420 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 25.42 | 0.9121 | 0.0404 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 21.65 | 0.8575 | 0.0571 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 22.28 | 0.8695 | 0.0517 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 84.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 31.41 | 0.9667 | 0.0317 | 1.00 |
| flow_s0.5_pose | 31.22 | 0.9653 | 0.0318 | 1.00 |
| flow_s0.5_uniform | 30.53 | 0.9607 | 0.0346 | 1.00 |
| flow_s1.0_oracle | 31.56 | 0.9661 | 0.0302 | 1.00 |
| flow_s1.0_pose | 31.46 | 0.9649 | 0.0305 | 1.00 |
| flow_s1.0_uniform | 30.29 | 0.9592 | 0.0331 | 1.00 |
| gs_tokr5448_nat_dil_al | 27.19 | 0.9122 | 0.0718 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 28.24 | 0.9253 | 0.0650 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 16.39 | 0.8478 | 0.1436 | 1.00 |
| gs_tokr5448_nat_dil_alv | 27.16 | 0.9125 | 0.0720 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 28.26 | 0.9256 | 0.0648 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 16.42 | 0.8482 | 0.1436 | 1.00 |
| gs_tokrife448_nat_dil_al | 18.20 | 0.8778 | 0.0886 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 18.29 | 0.8849 | 0.0877 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.29 | 0.6362 | 0.3761 | 1.00 |
| gs_tokrife448_nat_dil_alv | 18.16 | 0.8777 | 0.0889 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 18.24 | 0.8850 | 0.0879 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 7.28 | 0.6364 | 0.3759 | 1.00 |
| gs_tokstrict448_nat_dil_al | 12.71 | 0.7284 | 0.2549 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 12.95 | 0.7405 | 0.2407 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.01 | 0.5989 | 0.4109 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 12.70 | 0.7278 | 0.2554 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 12.95 | 0.7403 | 0.2407 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.01 | 0.5986 | 0.4111 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 31.46 | 0.9643 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 31.44 | 0.9636 | 0.0309 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 31.46 | 0.9643 | 0.0305 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 31.43 | 0.9635 | 0.0310 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 31.45 | 0.9641 | 0.0306 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 31.44 | 0.9639 | 0.0307 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 31.45 | 0.9640 | 0.0306 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 31.44 | 0.9639 | 0.0308 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 31.35 | 0.9625 | 0.0325 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 31.22 | 0.9614 | 0.0340 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 31.35 | 0.9625 | 0.0325 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 31.19 | 0.9613 | 0.0342 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 31.40 | 0.9624 | 0.0312 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 31.35 | 0.9615 | 0.0322 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 31.40 | 0.9624 | 0.0313 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 31.36 | 0.9615 | 0.0322 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 31.37 | 0.9619 | 0.0315 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 31.36 | 0.9616 | 0.0319 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 31.38 | 0.9619 | 0.0315 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 31.37 | 0.9616 | 0.0318 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 30.71 | 0.9528 | 0.0416 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 30.38 | 0.9491 | 0.0483 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 30.72 | 0.9528 | 0.0415 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 30.37 | 0.9491 | 0.0483 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 31.45 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 31.46 | 0.9649 | 0.0305 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 31.45 | 0.9647 | 0.0306 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 31.45 | 0.9648 | 0.0306 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 31.45 | 0.9647 | 0.0306 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 28.02 | 0.9338 | 0.0597 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 27.95 | 0.9339 | 0.0595 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.58 | 0.9588 | 0.0361 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 30.65 | 0.9591 | 0.0359 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 27.68 | 0.9509 | 0.0463 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 27.60 | 0.9505 | 0.0465 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 28.14 | 0.9344 | 0.0580 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 28.20 | 0.9347 | 0.0565 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 30.45 | 0.9592 | 0.0361 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 30.57 | 0.9598 | 0.0356 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 27.82 | 0.9493 | 0.0476 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 29.18 | 0.9532 | 0.0433 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s0.5_oracle | 28.40 | 0.9528 | 0.0403 | 1.00 |
| flow_s0.5_pose | 27.45 | 0.9461 | 0.0415 | 1.00 |
| flow_s0.5_uniform | 26.08 | 0.9340 | 0.0467 | 1.00 |
| flow_s1.0_oracle | 28.96 | 0.9545 | 0.0383 | 1.00 |
| flow_s1.0_pose | 28.00 | 0.9479 | 0.0396 | 1.00 |
| flow_s1.0_uniform | 26.19 | 0.9330 | 0.0440 | 1.00 |
| gs_tokr5448_nat_dil_al | 24.79 | 0.8848 | 0.0880 | 1.00 |
| gs_tokr5448_nat_dil_al+reg | 26.12 | 0.9036 | 0.0843 | 1.00 |
| gs_tokr5448_nat_dil_al_local | 16.75 | 0.8296 | 0.1595 | 1.00 |
| gs_tokr5448_nat_dil_alv | 24.60 | 0.8836 | 0.0883 | 1.00 |
| gs_tokr5448_nat_dil_alv+reg | 26.08 | 0.9036 | 0.0845 | 1.00 |
| gs_tokr5448_nat_dil_alv_local | 16.74 | 0.8286 | 0.1598 | 1.00 |
| gs_tokrife448_nat_dil_al | 18.52 | 0.8629 | 0.1025 | 1.00 |
| gs_tokrife448_nat_dil_al+reg | 18.63 | 0.8706 | 0.1034 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.68 | 0.6324 | 0.4079 | 1.00 |
| gs_tokrife448_nat_dil_alv | 18.47 | 0.8624 | 0.1024 | 1.00 |
| gs_tokrife448_nat_dil_alv+reg | 18.56 | 0.8698 | 0.1036 | 1.00 |
| gs_tokrife448_nat_dil_alv_local | 7.68 | 0.6323 | 0.4076 | 1.00 |
| gs_tokstrict448_nat_dil_al | 12.91 | 0.6932 | 0.2600 | 1.00 |
| gs_tokstrict448_nat_dil_al+reg | 13.33 | 0.7156 | 0.2549 | 1.00 |
| gs_tokstrict448_nat_dil_al_local | 7.29 | 0.5710 | 0.4586 | 1.00 |
| gs_tokstrict448_nat_dil_alv | 12.90 | 0.6938 | 0.2597 | 1.00 |
| gs_tokstrict448_nat_dil_alv+reg | 13.33 | 0.7140 | 0.2548 | 1.00 |
| gs_tokstrict448_nat_dil_alv_local | 7.29 | 0.5721 | 0.4585 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al+reg] | 28.35 | 0.9475 | 0.0454 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_al] | 27.59 | 0.9437 | 0.0478 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv+reg] | 28.28 | 0.9471 | 0.0456 | 1.00 |
| hyb_oracle_fail[gs_tokr5448_nat_dil_alv] | 27.26 | 0.9422 | 0.0484 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al+reg] | 28.62 | 0.9484 | 0.0452 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_al] | 28.50 | 0.9481 | 0.0448 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv+reg] | 28.48 | 0.9477 | 0.0454 | 1.00 |
| hyb_oracle_fail[gs_tokrife448_nat_dil_alv] | 28.44 | 0.9477 | 0.0448 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al+reg] | 26.54 | 0.9358 | 0.0602 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_al] | 25.24 | 0.9278 | 0.0666 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv+reg] | 26.45 | 0.9346 | 0.0604 | 1.00 |
| hyb_oracle_fail[gs_tokstrict448_nat_dil_alv] | 25.13 | 0.9289 | 0.0665 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al+reg] | 27.23 | 0.9351 | 0.0540 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_al] | 26.33 | 0.9277 | 0.0576 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv+reg] | 27.17 | 0.9348 | 0.0545 | 1.00 |
| hyb_risk[gs_tokr5448_nat_dil_alv] | 26.09 | 0.9264 | 0.0580 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al+reg] | 27.29 | 0.9354 | 0.0533 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_al] | 27.16 | 0.9338 | 0.0532 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv+reg] | 27.17 | 0.9345 | 0.0535 | 1.00 |
| hyb_risk[gs_tokrife448_nat_dil_alv] | 27.10 | 0.9335 | 0.0532 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al+reg] | 23.79 | 0.8959 | 0.0850 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_al] | 22.26 | 0.8813 | 0.0947 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv+reg] | 23.75 | 0.8945 | 0.0847 | 1.00 |
| hyb_risk[gs_tokstrict448_nat_dil_alv] | 22.14 | 0.8826 | 0.0946 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al+reg] | 28.05 | 0.9471 | 0.0427 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_al] | 27.75 | 0.9456 | 0.0433 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv+reg] | 27.99 | 0.9470 | 0.0428 | 1.00 |
| hyb_risktuned[gs_tokr5448_nat_dil_alv] | 27.49 | 0.9445 | 0.0437 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al+reg] | 28.41 | 0.9488 | 0.0413 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_al] | 28.41 | 0.9487 | 0.0411 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv+reg] | 28.27 | 0.9482 | 0.0413 | 1.00 |
| hyb_risktuned[gs_tokrife448_nat_dil_alv] | 28.30 | 0.9484 | 0.0411 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al+reg] | 26.73 | 0.9381 | 0.0489 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_al] | 25.69 | 0.9328 | 0.0518 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv+reg] | 26.66 | 0.9372 | 0.0490 | 1.00 |
| hyb_risktuned[gs_tokstrict448_nat_dil_alv] | 25.52 | 0.9338 | 0.0515 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_al_local] | 25.14 | 0.9027 | 0.0771 | 1.00 |
| hyb_token[gs_tokr5448_nat_dil_alv_local] | 24.94 | 0.9015 | 0.0773 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.81 | 0.9420 | 0.0474 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_alv_local] | 27.76 | 0.9419 | 0.0473 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_al_local] | 24.00 | 0.9187 | 0.0617 | 1.00 |
| hyb_token[gs_tokstrict448_nat_dil_alv_local] | 23.89 | 0.9194 | 0.0614 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_al_local] | 25.51 | 0.9043 | 0.0766 | 1.00 |
| hyb_token_ringreg[gs_tokr5448_nat_dil_alv_local] | 25.54 | 0.9044 | 0.0755 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_al_local] | 27.65 | 0.9406 | 0.0482 | 1.00 |
| hyb_token_ringreg[gs_tokrife448_nat_dil_alv_local] | 27.84 | 0.9430 | 0.0468 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_al_local] | 24.68 | 0.9189 | 0.0626 | 1.00 |
| hyb_token_ringreg[gs_tokstrict448_nat_dil_alv_local] | 25.43 | 0.9251 | 0.0589 | 1.00 |

## GS 配准残差（ECC 平移→仿射→单应，前景除物体区；越大说明目标相机位姿/内参误差越大）

| 设置 | 变体 | 平均位移 px | 成功率 |
|---|---|---:|---:|
| cam3 | gs_tokr5448_nat_dil_al | 0.61 | 1.00 |
| cam3 | gs_tokr5448_nat_dil_alv | 0.71 | 1.00 |
| cam3 | gs_tokrife448_nat_dil_al | 0.65 | 1.00 |
| cam3 | gs_tokrife448_nat_dil_alv | 0.76 | 1.00 |
| cam3 | gs_tokstrict448_nat_dil_al | 0.00 | 0.00 |
| cam3 | gs_tokstrict448_nat_dil_alv | 0.00 | 0.00 |
| cam5 | gs_tokr5448_nat_dil_al | 1.33 | 1.00 |
| cam5 | gs_tokr5448_nat_dil_alv | 1.42 | 1.00 |
| cam5 | gs_tokrife448_nat_dil_al | 0.62 | 0.50 |
| cam5 | gs_tokrife448_nat_dil_alv | 0.61 | 0.50 |
| cam5 | gs_tokstrict448_nat_dil_al | 5.55 | 1.00 |
| cam5 | gs_tokstrict448_nat_dil_alv | 5.57 | 1.00 |

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
| cam3 | gs_tokr5448_nat_dil_al | aligned_int | 911 | None | classic | 1.94 | False | 368633 | 0.823 | 43.9 | 29.15 | 0.32 | 0.011 |
| cam3 | gs_tokr5448_nat_dil_al_local | aligned_int | 911 | None | classic | 1.94 | False | 368633 | 0.823 | 72.8 | 29.15 | 0.32 | 0.011 |
| cam3 | gs_tokr5448_nat_dil_alv | aligned_vggt | 911 | None | classic | 1.94 | False | 368633 | 0.823 | 42.6 | 29.15 | 0.32 | 0.011 |
| cam3 | gs_tokr5448_nat_dil_alv_local | aligned_vggt | 911 | None | classic | 1.94 | False | 368633 | 0.823 | 42.3 | 29.15 | 0.32 | 0.011 |
| cam3 | gs_tokrife448_nat_dil_al | aligned_int | 726 | None | classic | 1.23 | False | 312491 | 0.332 | 31.6 | 28.28 | 0.38 | 0.005 |
| cam3 | gs_tokrife448_nat_dil_al_local | aligned_int | 726 | None | classic | 1.23 | False | 312491 | 0.332 | 41.5 | 28.28 | 0.38 | 0.005 |
| cam3 | gs_tokrife448_nat_dil_alv | aligned_vggt | 726 | None | classic | 1.23 | False | 312491 | 0.332 | 32.7 | 28.28 | 0.38 | 0.005 |
| cam3 | gs_tokrife448_nat_dil_alv_local | aligned_vggt | 726 | None | classic | 1.23 | False | 312491 | 0.332 | 46.9 | 28.28 | 0.38 | 0.005 |
| cam3 | gs_tokstrict448_nat_dil_al | aligned_int | 576 | None | classic | 0.78 | False | 209627 | 0.335 | 28.8 | 27.03 | 0.81 | 0.031 |
| cam3 | gs_tokstrict448_nat_dil_al_local | aligned_int | 576 | None | classic | 0.78 | False | 209627 | 0.335 | 42.4 | 27.03 | 0.81 | 0.031 |
| cam3 | gs_tokstrict448_nat_dil_alv | aligned_vggt | 576 | None | classic | 0.78 | False | 209627 | 0.335 | 31.7 | 27.03 | 0.81 | 0.031 |
| cam3 | gs_tokstrict448_nat_dil_alv_local | aligned_vggt | 576 | None | classic | 0.78 | False | 209627 | 0.335 | 41.3 | 27.03 | 0.81 | 0.031 |
| cam5 | gs_tokr5448_nat_dil_al | aligned_int | 917 | None | classic | 1.96 | False | 528485 | 0.519 | 39.9 | 29.47 | 0.12 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_al_local | aligned_int | 917 | None | classic | 1.96 | False | 528485 | 0.519 | 43.7 | 29.47 | 0.12 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_alv | aligned_vggt | 917 | None | classic | 1.96 | False | 528485 | 0.519 | 23.4 | 29.47 | 0.12 | 0.007 |
| cam5 | gs_tokr5448_nat_dil_alv_local | aligned_vggt | 917 | None | classic | 1.96 | False | 528485 | 0.519 | 46.1 | 29.47 | 0.12 | 0.007 |
| cam5 | gs_tokrife448_nat_dil_al | aligned_int | 617 | None | classic | 0.89 | False | 357227 | 0.500 | 27.7 | 27.82 | 0.23 | 0.013 |
| cam5 | gs_tokrife448_nat_dil_al_local | aligned_int | 617 | None | classic | 0.89 | False | 357227 | 0.500 | 43.6 | 27.82 | 0.23 | 0.013 |
| cam5 | gs_tokrife448_nat_dil_alv | aligned_vggt | 617 | None | classic | 0.89 | False | 357227 | 0.500 | 27.9 | 27.82 | 0.23 | 0.013 |
| cam5 | gs_tokrife448_nat_dil_alv_local | aligned_vggt | 617 | None | classic | 0.89 | False | 357227 | 0.500 | 43.1 | 27.82 | 0.23 | 0.013 |
| cam5 | gs_tokstrict448_nat_dil_al | aligned_int | 448 | None | classic | 0.47 | False | 186830 | 0.496 | 33.6 | 21.24 | 0.24 | 0.006 |
| cam5 | gs_tokstrict448_nat_dil_al_local | aligned_int | 448 | None | classic | 0.47 | False | 186830 | 0.496 | 44.1 | 21.24 | 0.24 | 0.006 |
| cam5 | gs_tokstrict448_nat_dil_alv | aligned_vggt | 448 | None | classic | 0.47 | False | 186830 | 0.496 | 31.5 | 21.24 | 0.24 | 0.006 |
| cam5 | gs_tokstrict448_nat_dil_alv_local | aligned_vggt | 448 | None | classic | 0.47 | False | 186830 | 0.496 | 43.1 | 21.24 | 0.24 | 0.006 |

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

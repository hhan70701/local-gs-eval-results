# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.6% | 22.95 / 0.0152 | 22.97 / 0.0204 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 8.2% | 22.14 / 0.0148 | 20.76 / 0.0275 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 3.2% | 19.08 / 0.0126 | 17.38 / 0.0214 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 9.7% | 23.02 / 0.0156 | 21.91 / 0.0201 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 9.6% | 23.00 / 0.0156 | 21.92 / 0.0239 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 3.1% | 19.10 / 0.0119 | 17.66 / 0.0184 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.69 / 0.0550 | — / — | 18.99 / 0.0156 | 29.70 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.18 / 0.0587 | — / — | 21.15 / 0.0148 | 29.65 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.36 / 0.0617 | — / — | 18.88 / 0.0189 | 29.68 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.35 / 0.0603 | — / — | 18.85 / 0.0188 | 29.68 / 0.0362 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.39 / 0.0598 | — / — | 19.01 / 0.0175 | 29.68 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.42 / 0.0611 | — / — | 19.04 / 0.0178 | 29.68 / 0.0372 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.41 / 0.0590 | — / — | 19.01 / 0.0176 | 29.67 / 0.0364 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.7%） | — | — | 27.69 / 0.0550 | — / — | 29.70 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.99 / 0.0551 | — | — | — |
| in035 | 2 | 0-3 | 27.48 / 0.0541 | — | — | — |
| in035 | 4 | 3-5 | 28.60 / 0.0559 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.69 / 0.0550 | — | 29.70 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.18 / 0.0587 | — | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.3% | 28.38 / 0.0549 | — | 29.70 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.36 / 0.0617 | — | 29.68 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.1% | 27.58 / 0.0585 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.35 / 0.0603 | — | 29.68 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.6% | 27.56 / 0.0584 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.39 / 0.0598 | — | 29.68 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.1% | 27.63 / 0.0571 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.42 / 0.0611 | — | 29.68 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.1% | 27.64 / 0.0577 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.41 / 0.0590 | — | 29.67 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.6% | 27.62 / 0.0574 | — | 29.71 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.69 / 0.0550 | — / — | 29.70 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.18 / 0.0587 | — / — | 29.65 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.38 / 0.0549 | — / — | 29.70 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 18.99 / 0.0156 | 29.70 / 0.0360 | 27.69 / 0.0550 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.99 | 0.6014 | 0.0156 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.07 | 0.3901 | 0.0895 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.07 | 0.3332 | 0.0686 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.07 | 0.3332 | 0.0686 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.13 | 0.3527 | 0.0663 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.13 | 0.3375 | 0.0667 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.13 | 0.3375 | 0.0667 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.17 | 0.7147 | 0.0147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 18.88 | 0.6634 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 18.85 | 0.6555 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.01 | 0.6789 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.03 | 0.6653 | 0.0178 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.01 | 0.6583 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.15 | 0.7134 | 0.0148 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 18.88 | 0.6639 | 0.0189 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 18.85 | 0.6557 | 0.0188 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.01 | 0.6801 | 0.0175 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.04 | 0.6659 | 0.0178 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.01 | 0.6590 | 0.0176 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 27.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.14 | 0.7574 | 0.0232 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.82 | 0.4541 | 0.1845 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.51 | 0.3784 | 0.1554 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.51 | 0.3784 | 0.1554 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.58 | 0.3953 | 0.1468 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.59 | 0.3892 | 0.1508 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.59 | 0.3892 | 0.1508 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.64 | 0.7840 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.87 | 0.7688 | 0.0257 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.82 | 0.7653 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.02 | 0.7728 | 0.0242 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.01 | 0.7697 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.96 | 0.7662 | 0.0246 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.33 | 0.7768 | 0.0263 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.19 | 0.7582 | 0.0329 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.19 | 0.7559 | 0.0296 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.36 | 0.7682 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.36 | 0.7626 | 0.0291 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.33 | 0.7579 | 0.0272 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.70 | 0.7061 | 0.0360 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.58 | 0.2220 | 0.3559 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.68 | 0.1210 | 0.2851 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.68 | 0.1210 | 0.2851 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.74 | 0.1264 | 0.2813 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.74 | 0.1282 | 0.2834 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.74 | 0.1282 | 0.2834 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.70 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.71 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.71 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.71 | 0.7063 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.71 | 0.7062 | 0.0360 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.71 | 0.7062 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.65 | 0.7064 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.68 | 0.7065 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.68 | 0.7060 | 0.0362 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.68 | 0.7060 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.68 | 0.7067 | 0.0372 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.67 | 0.7059 | 0.0364 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.69 | 0.7108 | 0.0550 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.98 | 0.2671 | 0.4216 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.84 | 0.1779 | 0.3846 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.84 | 0.1779 | 0.3846 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.90 | 0.1843 | 0.3757 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.90 | 0.1852 | 0.3802 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.90 | 0.1852 | 0.3802 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.38 | 0.7191 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.58 | 0.7151 | 0.0585 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.56 | 0.7141 | 0.0584 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.63 | 0.7161 | 0.0571 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.64 | 0.7152 | 0.0577 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.62 | 0.7142 | 0.0574 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.18 | 0.7191 | 0.0587 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.36 | 0.7142 | 0.0617 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.35 | 0.7122 | 0.0603 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.39 | 0.7149 | 0.0598 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.42 | 0.7148 | 0.0611 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.41 | 0.7125 | 0.0590 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 653 | None | classic | 0.31 | False | 368286 | 0.984 | 198.4 | 29.95 | 0.30 | 0.011 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1100970 | 0.789 | 190.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1100970 | 0.789 | 190.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 850539 | 0.789 | 7.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 850539 | 0.789 | 10.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 850539 | 0.789 | 10.7 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.736 | 0.021 |
| in035 | mask_ent | 0.708 | 0.021 |
| in035 | mask_grad | 0.472 | 0.021 |
| in035 | r_col | 0.770 | 0.021 |
| in035 | r_warp | 0.874 | 0.021 |

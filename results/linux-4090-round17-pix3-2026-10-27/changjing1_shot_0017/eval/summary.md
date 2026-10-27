# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.6% | 23.27 / 0.0137 | 22.71 / 0.0175 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 8.8% | 22.72 / 0.0140 | 21.07 / 0.0259 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 3.2% | 21.10 / 0.0086 | 17.16 / 0.0178 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.6% | 23.73 / 0.0154 | 23.56 / 0.0197 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.6% | 23.69 / 0.0154 | 22.89 / 0.0233 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 3.6% | 21.03 / 0.0090 | 19.14 / 0.0149 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.22 / 0.0554 | — / — | 19.68 / 0.0157 | 29.88 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.38 / 0.0579 | — / — | 20.86 / 0.0140 | 29.57 / 0.0366 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.78 / 0.0629 | — / — | 19.85 / 0.0182 | 29.57 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.80 / 0.0610 | — / — | 19.70 / 0.0177 | 29.59 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.10 / 0.0591 | — / — | 20.24 / 0.0168 | 29.69 / 0.0364 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.98 / 0.0613 | — / — | 20.11 / 0.0174 | 29.58 / 0.0371 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.99 / 0.0589 | — / — | 19.92 / 0.0168 | 29.64 / 0.0362 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 8.3%） | — | — | 27.22 / 0.0554 | — / — | 29.88 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.34 / 0.0552 | — | — | — |
| in035 | 2 | 0-3 | 26.62 / 0.0580 | — | — | — |
| in035 | 4 | 3-5 | 28.71 / 0.0530 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.22 / 0.0554 | — | 29.88 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.38 / 0.0579 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 27.77 / 0.0541 | — | 29.86 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 26.78 / 0.0629 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.6% | 27.19 / 0.0580 | — | 29.84 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.80 / 0.0610 | — | 29.59 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.6% | 27.14 / 0.0575 | — | 29.84 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.10 / 0.0591 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.9% | 27.40 / 0.0558 | — | 29.89 | 2/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 26.98 / 0.0613 | — | 29.58 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.9% | 27.34 / 0.0569 | — | 29.86 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 26.99 / 0.0589 | — | 29.64 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.6% | 27.28 / 0.0563 | — | 29.86 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.22 / 0.0554 | — / — | 29.88 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.38 / 0.0579 | — / — | 29.57 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.77 / 0.0541 | — / — | 29.86 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.68 / 0.0157 | 29.88 / 0.0349 | 27.22 / 0.0554 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 8.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.68 | 0.6581 | 0.0157 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.76 | 0.4258 | 0.0877 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.34 | 0.4057 | 0.0659 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.34 | 0.4057 | 0.0659 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.00 | 0.4745 | 0.0589 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.94 | 0.4387 | 0.0599 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.94 | 0.4387 | 0.0599 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.88 | 0.7088 | 0.0139 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.86 | 0.6787 | 0.0182 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.70 | 0.6651 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.24 | 0.7020 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.11 | 0.6873 | 0.0173 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.93 | 0.6725 | 0.0167 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.86 | 0.7073 | 0.0140 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.85 | 0.6775 | 0.0182 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.70 | 0.6643 | 0.0177 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.24 | 0.7019 | 0.0168 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.11 | 0.6865 | 0.0174 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.92 | 0.6721 | 0.0168 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 27.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.06 | 0.7560 | 0.0229 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.18 | 0.4870 | 0.2077 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.77 | 0.3664 | 0.1661 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.77 | 0.3664 | 0.1661 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.02 | 0.4052 | 0.1541 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.99 | 0.3874 | 0.1584 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.99 | 0.3874 | 0.1584 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.25 | 0.7745 | 0.0216 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.03 | 0.7586 | 0.0255 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.94 | 0.7553 | 0.0250 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.41 | 0.7673 | 0.0227 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.32 | 0.7624 | 0.0237 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.22 | 0.7590 | 0.0234 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.22 | 0.7576 | 0.0257 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.07 | 0.7371 | 0.0316 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.17 | 0.7423 | 0.0285 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.75 | 0.7530 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.51 | 0.7436 | 0.0282 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.55 | 0.7463 | 0.0264 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 77.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.88 | 0.7314 | 0.0349 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.96 | 0.3371 | 0.3727 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.39 | 0.1858 | 0.2870 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.39 | 0.1858 | 0.2870 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.69 | 0.2060 | 0.2745 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.67 | 0.2057 | 0.2787 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.67 | 0.2057 | 0.2787 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.86 | 0.7312 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.84 | 0.7312 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.84 | 0.7311 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.89 | 0.7319 | 0.0349 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.86 | 0.7315 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.86 | 0.7313 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.57 | 0.7296 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.57 | 0.7304 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.59 | 0.7301 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.69 | 0.7314 | 0.0364 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.58 | 0.7311 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.64 | 0.7305 | 0.0362 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.22 | 0.7317 | 0.0554 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.48 | 0.3591 | 0.4369 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.59 | 0.2272 | 0.3794 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.59 | 0.2272 | 0.3794 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.91 | 0.2537 | 0.3584 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.90 | 0.2493 | 0.3655 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.90 | 0.2493 | 0.3655 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.77 | 0.7356 | 0.0541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.19 | 0.7322 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.14 | 0.7310 | 0.0575 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.40 | 0.7351 | 0.0558 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.34 | 0.7334 | 0.0569 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.28 | 0.7319 | 0.0563 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.38 | 0.7311 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.78 | 0.7276 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.80 | 0.7276 | 0.0610 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.10 | 0.7319 | 0.0591 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.98 | 0.7296 | 0.0613 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.99 | 0.7290 | 0.0589 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 850 | None | classic | 1.08 | False | 363650 | 0.356 | 68.0 | 28.19 | 0.11 | 0.019 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1311100 | 0.810 | 91.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1311100 | 0.810 | 91.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 996258 | 0.810 | 9.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 996258 | 0.810 | 7.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 996258 | 0.810 | 7.8 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.589 | 0.030 |
| in035 | mask_ent | 0.728 | 0.030 |
| in035 | mask_grad | 0.416 | 0.030 |
| in035 | r_col | 0.777 | 0.030 |
| in035 | r_warp | 0.850 | 0.030 |

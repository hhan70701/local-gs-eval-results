# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.2% | 23.75 / 0.0105 | 21.63 / 0.0196 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 6.3% | 23.03 / 0.0103 | 20.66 / 0.0220 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.6% | 19.95 / 0.0074 | 17.66 / 0.0146 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 9.3% | 24.24 / 0.0113 | 21.91 / 0.0191 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 9.3% | 24.16 / 0.0116 | 22.00 / 0.0207 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.9% | 20.51 / 0.0068 | 18.29 / 0.0125 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.68 / 0.0491 | — / — | 19.74 / 0.0112 | 29.91 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.35 / 0.0535 | — / — | 19.85 / 0.0120 | 29.66 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.14 / 0.0551 | — / — | 19.30 / 0.0150 | 29.85 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.21 / 0.0537 | — / — | 19.48 / 0.0145 | 29.86 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.09 / 0.0541 | — / — | 19.12 / 0.0142 | 29.84 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.18 / 0.0548 | — / — | 19.35 / 0.0136 | 29.81 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.25 / 0.0523 | — / — | 19.54 / 0.0132 | 29.85 / 0.0351 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.8%） | — | — | 27.68 / 0.0491 | — / — | 29.91 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.53 / 0.0510 | — | — | — |
| in035 | 2 | 0-3 | 27.11 / 0.0483 | — | — | — |
| in035 | 4 | 3-5 | 29.40 / 0.0479 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.68 / 0.0491 | — | 29.91 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.35 / 0.0535 | — | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.1% | 27.76 / 0.0501 | — | 29.90 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.14 / 0.0551 | — | 29.85 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.9% | 27.31 / 0.0525 | — | 29.90 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.21 / 0.0537 | — | 29.86 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.2% | 27.34 / 0.0520 | — | 29.90 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.09 / 0.0541 | — | 29.84 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.1% | 27.25 / 0.0518 | — | 29.90 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.18 / 0.0548 | — | 29.81 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.0% | 27.35 / 0.0512 | — | 29.90 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.25 / 0.0523 | — | 29.85 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.3% | 27.38 / 0.0506 | — | 29.90 | 1/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.68 / 0.0491 | — / — | 29.91 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.35 / 0.0535 | — / — | 29.66 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.76 / 0.0501 | — / — | 29.90 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.74 / 0.0112 | 29.91 / 0.0339 | 27.68 / 0.0491 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.74 | 0.6486 | 0.0112 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.91 | 0.3147 | 0.0911 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.25 | 0.2599 | 0.0587 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.25 | 0.2599 | 0.0587 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.52 | 0.2943 | 0.0553 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.56 | 0.2833 | 0.0549 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 11.56 | 0.2833 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.87 | 0.6704 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.30 | 0.6375 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.48 | 0.6415 | 0.0145 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.12 | 0.6447 | 0.0141 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.35 | 0.6422 | 0.0136 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.54 | 0.6467 | 0.0132 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.85 | 0.6695 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.30 | 0.6371 | 0.0150 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.48 | 0.6410 | 0.0145 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.12 | 0.6450 | 0.0142 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.35 | 0.6420 | 0.0136 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.54 | 0.6463 | 0.0132 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 29.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.75 | 0.7592 | 0.0184 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.15 | 0.4258 | 0.2302 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.14 | 0.3045 | 0.1739 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.14 | 0.3045 | 0.1739 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.26 | 0.3279 | 0.1655 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.27 | 0.3219 | 0.1667 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.27 | 0.3219 | 0.1667 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.81 | 0.7640 | 0.0198 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.14 | 0.7527 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.24 | 0.7526 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.02 | 0.7563 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.20 | 0.7551 | 0.0207 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.31 | 0.7546 | 0.0202 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.57 | 0.7407 | 0.0236 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.72 | 0.7420 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.93 | 0.7469 | 0.0239 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 24.75 | 0.7504 | 0.0235 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.84 | 0.7478 | 0.0239 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.00 | 0.7492 | 0.0224 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.91 | 0.7355 | 0.0339 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.90 | 0.3180 | 0.3863 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.22 | 0.1625 | 0.2859 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.22 | 0.1625 | 0.2859 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.59 | 0.1894 | 0.2749 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.57 | 0.1899 | 0.2788 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.57 | 0.1899 | 0.2788 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.90 | 0.7355 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.90 | 0.7355 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.90 | 0.7354 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.90 | 0.7354 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.90 | 0.7354 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.90 | 0.7353 | 0.0340 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.66 | 0.7335 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.85 | 0.7355 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.86 | 0.7352 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.84 | 0.7349 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.81 | 0.7350 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.85 | 0.7349 | 0.0351 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.68 | 0.7307 | 0.0491 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.21 | 0.3230 | 0.4461 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.40 | 0.1863 | 0.3772 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.40 | 0.1863 | 0.3772 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.73 | 0.2124 | 0.3613 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.73 | 0.2116 | 0.3663 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.73 | 0.2116 | 0.3663 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.76 | 0.7318 | 0.0501 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.31 | 0.7283 | 0.0525 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.34 | 0.7282 | 0.0520 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.25 | 0.7291 | 0.0518 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.35 | 0.7289 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.38 | 0.7287 | 0.0506 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.35 | 0.7269 | 0.0535 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.14 | 0.7270 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.21 | 0.7272 | 0.0537 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.09 | 0.7278 | 0.0541 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.18 | 0.7274 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.25 | 0.7276 | 0.0523 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 860 | None | classic | 1.11 | False | 349921 | 0.348 | 74.8 | 28.53 | 0.13 | 0.026 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1011738 | 0.815 | 85.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1011738 | 0.815 | 85.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 775776 | 0.815 | 8.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 775776 | 0.815 | 6.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 775776 | 0.815 | 6.6 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.577 | 0.025 |
| in035 | mask_ent | 0.735 | 0.025 |
| in035 | mask_grad | 0.435 | 0.025 |
| in035 | r_col | 0.675 | 0.025 |
| in035 | r_warp | 0.838 | 0.025 |

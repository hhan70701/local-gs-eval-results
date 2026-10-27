# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.4% | 24.52 / 0.0148 | 22.24 / 0.0279 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.1% | 24.06 / 0.0145 | 22.21 / 0.0319 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 3.3% | 20.00 / 0.0098 | 17.58 / 0.0219 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.2% | 24.73 / 0.0160 | 23.25 / 0.0242 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.1% | 24.66 / 0.0159 | 23.28 / 0.0293 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 3.5% | 20.06 / 0.0101 | 18.15 / 0.0175 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.02 / 0.0578 | — / — | 19.50 / 0.0172 | 29.74 / 0.0344 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.94 / 0.0668 | — / — | 20.31 / 0.0180 | 29.60 / 0.0365 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.70 / 0.0673 | — / — | 19.85 / 0.0212 | 29.60 / 0.0351 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.68 / 0.0638 | — / — | 19.75 / 0.0211 | 29.59 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.73 / 0.0629 | — / — | 19.86 / 0.0193 | 29.63 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.74 / 0.0669 | — / — | 20.01 / 0.0204 | 29.63 / 0.0355 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.71 / 0.0627 | — / — | 19.90 / 0.0206 | 29.61 / 0.0347 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.5%） | — | — | 28.02 / 0.0578 | — / — | 29.74 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.77 / 0.0623 | — | — | — |
| in035 | 2 | 0-3 | 28.34 / 0.0530 | — | — | — |
| in035 | 4 | 3-5 | 28.94 / 0.0581 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.02 / 0.0578 | — | 29.74 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.94 / 0.0668 | — | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 28.27 / 0.0597 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.70 / 0.0673 | — | 29.60 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.4% | 28.03 / 0.0622 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.68 / 0.0638 | — | 29.59 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.5% | 27.99 / 0.0616 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.73 / 0.0629 | — | 29.63 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.4% | 28.05 / 0.0603 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.74 / 0.0669 | — | 29.63 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.4% | 28.08 / 0.0615 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.71 / 0.0627 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.6% | 28.03 / 0.0611 | — | 29.73 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.02 / 0.0578 | — / — | 29.74 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.94 / 0.0668 | — / — | 29.60 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.27 / 0.0597 | — / — | 29.73 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.50 / 0.0172 | 29.74 / 0.0344 | 28.02 / 0.0578 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.50 | 0.5831 | 0.0172 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.95 | 0.4616 | 0.0935 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.62 | 0.4172 | 0.0635 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.62 | 0.4172 | 0.0635 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.65 | 0.4461 | 0.0579 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.68 | 0.4231 | 0.0608 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.68 | 0.4231 | 0.0608 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.33 | 0.6649 | 0.0179 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.86 | 0.6482 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.76 | 0.6246 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.87 | 0.6654 | 0.0192 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.02 | 0.6512 | 0.0204 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.91 | 0.6283 | 0.0205 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.31 | 0.6650 | 0.0180 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.85 | 0.6465 | 0.0212 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.75 | 0.6230 | 0.0211 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.86 | 0.6647 | 0.0193 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.01 | 0.6499 | 0.0204 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.90 | 0.6273 | 0.0206 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 38.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.37 | 0.7729 | 0.0297 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.68 | 0.5640 | 0.2292 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.64 | 0.4826 | 0.1898 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.64 | 0.4826 | 0.1898 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.92 | 0.5076 | 0.1765 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 14.85 | 0.4990 | 0.1832 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 14.85 | 0.4990 | 0.1832 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.59 | 0.7831 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.39 | 0.7845 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.32 | 0.7799 | 0.0335 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.48 | 0.7887 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.52 | 0.7856 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.42 | 0.7807 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.11 | 0.7693 | 0.0410 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.32 | 0.7703 | 0.0445 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.36 | 0.7675 | 0.0402 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.56 | 0.7792 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.54 | 0.7743 | 0.0412 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.54 | 0.7704 | 0.0372 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 71.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.74 | 0.7047 | 0.0344 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.72 | 0.3013 | 0.3529 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.14 | 0.1727 | 0.2573 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.14 | 0.1727 | 0.2573 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.26 | 0.1858 | 0.2502 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.26 | 0.1875 | 0.2541 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.26 | 0.1875 | 0.2541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.73 | 0.7047 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.73 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.73 | 0.7046 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.73 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.73 | 0.7047 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.73 | 0.7046 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.60 | 0.7047 | 0.0365 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.60 | 0.7048 | 0.0351 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.59 | 0.7042 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.63 | 0.7046 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.63 | 0.7054 | 0.0355 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.61 | 0.7041 | 0.0347 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.02 | 0.7204 | 0.0578 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.70 | 0.3814 | 0.4245 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.75 | 0.2794 | 0.3587 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.75 | 0.2794 | 0.3587 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.90 | 0.2947 | 0.3403 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.89 | 0.2933 | 0.3519 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.89 | 0.2933 | 0.3519 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.27 | 0.7256 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.03 | 0.7255 | 0.0622 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.99 | 0.7237 | 0.0616 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.05 | 0.7267 | 0.0603 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.08 | 0.7256 | 0.0615 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.03 | 0.7236 | 0.0611 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.94 | 0.7238 | 0.0668 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.70 | 0.7239 | 0.0673 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.68 | 0.7214 | 0.0638 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.73 | 0.7253 | 0.0629 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.74 | 0.7245 | 0.0669 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.71 | 0.7215 | 0.0627 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 905 | None | classic | 1.22 | False | 732752 | 0.688 | 113.3 | 28.90 | 0.13 | 0.017 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1519252 | 0.797 | 93.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1519252 | 0.797 | 93.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1151962 | 0.797 | 9.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1151962 | 0.797 | 7.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1151962 | 0.797 | 7.1 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.741 | 0.019 |
| in035 | mask_ent | 0.634 | 0.019 |
| in035 | mask_grad | 0.460 | 0.019 |
| in035 | r_col | 0.839 | 0.019 |
| in035 | r_warp | 0.874 | 0.019 |

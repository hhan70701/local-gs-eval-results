# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 19.1% | 25.26 / 0.0196 | 23.81 / 0.0319 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.0% | 24.57 / 0.0191 | 22.22 / 0.0520 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 5.3% | 21.09 / 0.0136 | 18.31 / 0.0363 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 18.9% | 25.33 / 0.0211 | 24.16 / 0.0294 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 18.9% | 25.30 / 0.0210 | 23.88 / 0.0385 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 4.8% | 20.87 / 0.0126 | 18.91 / 0.0223 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.76 / 0.0513 | — / — | 19.75 / 0.0167 | 29.67 / 0.0267 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.63 / 0.0632 | — / — | 20.86 / 0.0162 | 29.26 / 0.0300 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.20 / 0.0684 | — / — | 19.98 / 0.0241 | 29.62 / 0.0272 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.27 / 0.0627 | — / — | 19.89 / 0.0233 | 29.62 / 0.0268 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.67 / 0.0583 | — / — | 20.68 / 0.0187 | 29.69 / 0.0270 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.56 / 0.0639 | — / — | 20.62 / 0.0202 | 29.57 / 0.0281 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.59 / 0.0575 | — / — | 20.41 / 0.0199 | 29.62 / 0.0269 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.3%） | — | — | 27.76 / 0.0513 | — / — | 29.67 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.51 / 0.0569 | — | — | — |
| in035 | 2 | 0-3 | 27.39 / 0.0519 | — | — | — |
| in035 | 4 | 3-5 | 29.38 / 0.0452 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.76 / 0.0513 | — | 29.67 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.63 / 0.0632 | — | 29.26 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.6% | 28.17 / 0.0523 | — | 29.65 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.20 / 0.0684 | — | 29.62 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 3.3% | 27.68 / 0.0589 | — | 29.67 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.27 / 0.0627 | — | 29.62 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 2.4% | 27.65 / 0.0580 | — | 29.67 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.67 / 0.0583 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 3.3% | 28.02 / 0.0538 | — | 29.68 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.56 / 0.0639 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 3.3% | 27.96 / 0.0555 | — | 29.67 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.59 / 0.0575 | — | 29.62 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 2.3% | 27.89 / 0.0548 | — | 29.67 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.76 / 0.0513 | — / — | 29.67 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.63 / 0.0632 | — / — | 29.26 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.17 / 0.0523 | — / — | 29.65 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.75 / 0.0167 | 29.67 / 0.0267 | 27.76 / 0.0513 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.3%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.75 | 0.6006 | 0.0167 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.48 | 0.5504 | 0.0532 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.15 | 0.4860 | 0.0441 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.15 | 0.4860 | 0.0441 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.69 | 0.5556 | 0.0357 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 15.62 | 0.5268 | 0.0382 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 15.62 | 0.5268 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.87 | 0.6807 | 0.0161 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.99 | 0.6325 | 0.0239 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.90 | 0.6210 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.70 | 0.6791 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.64 | 0.6588 | 0.0201 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.43 | 0.6397 | 0.0198 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.86 | 0.6799 | 0.0162 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.98 | 0.6299 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.89 | 0.6196 | 0.0233 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.68 | 0.6776 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.62 | 0.6570 | 0.0202 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.41 | 0.6387 | 0.0199 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 45.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.59 | 0.7718 | 0.0287 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.44 | 0.5814 | 0.2019 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.28 | 0.4916 | 0.1794 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.28 | 0.4916 | 0.1794 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.71 | 0.5365 | 0.1521 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 15.59 | 0.5209 | 0.1621 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 15.59 | 0.5209 | 0.1621 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.07 | 0.7834 | 0.0315 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.42 | 0.7728 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.39 | 0.7713 | 0.0364 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.01 | 0.7838 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.92 | 0.7798 | 0.0334 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.80 | 0.7763 | 0.0325 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.89 | 0.7737 | 0.0412 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.10 | 0.7493 | 0.0565 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.29 | 0.7556 | 0.0479 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.00 | 0.7752 | 0.0370 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.80 | 0.7668 | 0.0437 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.85 | 0.7664 | 0.0371 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 65.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.67 | 0.7076 | 0.0267 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.06 | 0.3859 | 0.2485 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.50 | 0.3408 | 0.1751 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.50 | 0.3408 | 0.1751 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.97 | 0.3584 | 0.1669 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 15.95 | 0.3622 | 0.1734 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 15.95 | 0.3622 | 0.1734 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.65 | 0.7075 | 0.0269 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.67 | 0.7078 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.67 | 0.7077 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.68 | 0.7078 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.67 | 0.7078 | 0.0267 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.67 | 0.7076 | 0.0267 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.26 | 0.7056 | 0.0300 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.62 | 0.7087 | 0.0272 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.62 | 0.7074 | 0.0268 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.69 | 0.7089 | 0.0270 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.57 | 0.7091 | 0.0281 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.62 | 0.7072 | 0.0269 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.76 | 0.7224 | 0.0513 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.26 | 0.4589 | 0.3146 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.92 | 0.4151 | 0.2552 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.92 | 0.4151 | 0.2552 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 16.39 | 0.4381 | 0.2313 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 16.35 | 0.4369 | 0.2464 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 16.35 | 0.4369 | 0.2464 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.17 | 0.7280 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.68 | 0.7241 | 0.0589 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.65 | 0.7231 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.02 | 0.7286 | 0.0538 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.96 | 0.7266 | 0.0555 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.89 | 0.7249 | 0.0548 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.63 | 0.7243 | 0.0632 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.20 | 0.7194 | 0.0684 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.27 | 0.7195 | 0.0627 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.67 | 0.7267 | 0.0583 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.56 | 0.7247 | 0.0639 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.59 | 0.7222 | 0.0575 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1206 | None | classic | 2.17 | False | 406157 | 0.669 | 120.0 | 29.54 | 0.09 | 0.011 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1929088 | 0.803 | 211.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1929088 | 0.803 | 211.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1417244 | 0.803 | 8.5 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1417244 | 0.803 | 8.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1417244 | 0.803 | 8.6 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.783 | 0.023 |
| in035 | mask_ent | 0.691 | 0.023 |
| in035 | mask_grad | 0.508 | 0.023 |
| in035 | r_col | 0.824 | 0.023 |
| in035 | r_warp | 0.891 | 0.023 |

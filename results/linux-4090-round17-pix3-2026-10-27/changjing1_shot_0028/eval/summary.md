# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.8% | 23.17 / 0.0127 | 23.60 / 0.0164 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 6.8% | 22.50 / 0.0118 | 22.52 / 0.0186 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.2% | 19.17 / 0.0082 | 19.33 / 0.0112 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.3% | 23.87 / 0.0134 | 24.55 / 0.0126 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.3% | 23.95 / 0.0131 | 24.68 / 0.0151 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.7% | 20.02 / 0.0085 | 20.96 / 0.0078 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.80 / 0.0480 | — / — | 19.50 / 0.0114 | 29.86 / 0.0326 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 / 0.0516 | — / — | 20.75 / 0.0113 | 29.71 / 0.0343 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.76 / 0.0517 | — / — | 19.89 / 0.0135 | 29.73 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.77 / 0.0502 | — / — | 19.80 / 0.0131 | 29.74 / 0.0335 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.87 / 0.0499 | — / — | 20.02 / 0.0122 | 29.84 / 0.0331 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.90 / 0.0507 | — / — | 20.14 / 0.0121 | 29.85 / 0.0336 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.88 / 0.0491 | — / — | 20.02 / 0.0121 | 29.83 / 0.0329 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.0%） | — | — | 27.80 / 0.0480 | — / — | 29.86 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.35 / 0.0458 | — | — | — |
| in035 | 2 | 0-3 | 27.76 / 0.0467 | — | — | — |
| in035 | 4 | 3-5 | 28.29 / 0.0515 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.80 / 0.0480 | — | 29.86 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.95 / 0.0516 | — | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.9% | 28.19 / 0.0481 | — | 29.86 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.76 / 0.0517 | — | 29.73 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.7% | 27.89 / 0.0498 | — | 29.84 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.77 / 0.0502 | — | 29.74 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.1% | 27.87 / 0.0492 | — | 29.84 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.87 / 0.0499 | — | 29.84 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.9% | 27.96 / 0.0486 | — | 29.87 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.90 / 0.0507 | — | 29.85 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 1.8% | 28.01 / 0.0486 | — | 29.87 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.88 / 0.0491 | — | 29.83 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.1% | 27.96 / 0.0483 | — | 29.86 | 1/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.80 / 0.0480 | — / — | 29.86 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.95 / 0.0516 | — / — | 29.71 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.19 / 0.0481 | — / — | 29.86 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.50 / 0.0114 | 29.86 / 0.0326 | 27.80 / 0.0480 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.50 | 0.6235 | 0.0114 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.28 | 0.3501 | 0.0956 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.74 | 0.3025 | 0.0615 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.74 | 0.3025 | 0.0615 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.97 | 0.3333 | 0.0576 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.02 | 0.3340 | 0.0580 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.02 | 0.3340 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.76 | 0.6898 | 0.0113 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.89 | 0.6662 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.81 | 0.6576 | 0.0131 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.03 | 0.6718 | 0.0122 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.15 | 0.6772 | 0.0120 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.03 | 0.6663 | 0.0120 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.75 | 0.6895 | 0.0113 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.89 | 0.6655 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.80 | 0.6571 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.02 | 0.6716 | 0.0122 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.14 | 0.6768 | 0.0121 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.02 | 0.6658 | 0.0121 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 29.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.78 | 0.7696 | 0.0209 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.61 | 0.4570 | 0.2100 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.67 | 0.3316 | 0.1645 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.67 | 0.3316 | 0.1645 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.81 | 0.3585 | 0.1544 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.83 | 0.3554 | 0.1572 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.83 | 0.3554 | 0.1572 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.70 | 0.7824 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.08 | 0.7768 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.02 | 0.7752 | 0.0217 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.17 | 0.7782 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.25 | 0.7799 | 0.0211 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.19 | 0.7779 | 0.0209 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.06 | 0.7711 | 0.0241 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.87 | 0.7665 | 0.0258 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.95 | 0.7713 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.06 | 0.7734 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.07 | 0.7737 | 0.0229 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.08 | 0.7745 | 0.0216 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.86 | 0.7338 | 0.0326 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.66 | 0.3020 | 0.3696 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.95 | 0.1373 | 0.2794 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.95 | 0.1373 | 0.2794 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.31 | 0.1627 | 0.2669 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.31 | 0.1661 | 0.2699 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.31 | 0.1661 | 0.2699 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.86 | 0.7339 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.84 | 0.7337 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.84 | 0.7337 | 0.0328 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.87 | 0.7340 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.87 | 0.7341 | 0.0326 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.86 | 0.7339 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.71 | 0.7323 | 0.0343 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.73 | 0.7330 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.74 | 0.7328 | 0.0335 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.84 | 0.7329 | 0.0331 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.85 | 0.7345 | 0.0336 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.83 | 0.7334 | 0.0329 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.80 | 0.7373 | 0.0480 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.08 | 0.3201 | 0.4278 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.08 | 0.1752 | 0.3677 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.08 | 0.1752 | 0.3677 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.42 | 0.1999 | 0.3495 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.42 | 0.2028 | 0.3541 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.42 | 0.2028 | 0.3541 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.19 | 0.7407 | 0.0481 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.89 | 0.7392 | 0.0498 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.87 | 0.7387 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.96 | 0.7396 | 0.0486 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.01 | 0.7404 | 0.0486 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.96 | 0.7394 | 0.0483 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 | 0.7376 | 0.0516 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.76 | 0.7375 | 0.0517 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.77 | 0.7373 | 0.0502 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.87 | 0.7375 | 0.0499 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.90 | 0.7394 | 0.0507 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.88 | 0.7383 | 0.0491 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 792 | None | classic | 0.30 | False | 515713 | 0.489 | 114.1 | 27.49 | 0.21 | 0.027 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1042606 | 0.800 | 86.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1042606 | 0.800 | 86.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 823392 | 0.800 | 10.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 823392 | 0.800 | 7.8 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 823392 | 0.800 | 7.8 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.687 | 0.021 |
| in035 | mask_ent | 0.670 | 0.021 |
| in035 | mask_grad | 0.468 | 0.021 |
| in035 | r_col | 0.802 | 0.021 |
| in035 | r_warp | 0.848 | 0.021 |

# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.8% | 25.79 / 0.0094 | 20.88 / 0.0187 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 4.1% | 25.31 / 0.0089 | 23.91 / 0.0226 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 1.1% | 21.29 / 0.0061 | 20.79 / 0.0143 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 4.5% | 25.58 / 0.0090 | 25.86 / 0.0126 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 4.5% | 25.59 / 0.0093 | 24.55 / 0.0149 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 1.3% | 21.18 / 0.0059 | 20.95 / 0.0081 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.18 / 0.0517 | — / — | 20.95 / 0.0114 | 29.75 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.48 / 0.0550 | — / — | 20.11 / 0.0124 | 29.61 / 0.0386 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.23 / 0.0551 | — / — | 21.29 / 0.0132 | 29.74 / 0.0378 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.24 / 0.0529 | — / — | 21.18 / 0.0123 | 29.75 / 0.0376 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.41 / 0.0527 | — / — | 21.64 / 0.0110 | 29.76 / 0.0378 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.25 / 0.0538 | — / — | 21.35 / 0.0119 | 29.74 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.25 / 0.0521 | — / — | 21.22 / 0.0112 | 29.74 / 0.0378 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.7%） | — | — | 28.18 / 0.0517 | — / — | 29.75 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.39 / 0.0542 | — | — | — |
| in035 | 2 | 0-3 | 28.60 / 0.0519 | — | — | — |
| in035 | 4 | 3-5 | 28.56 / 0.0489 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.18 / 0.0517 | — | 29.75 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.48 / 0.0550 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.3% | 27.78 / 0.0524 | — | 29.74 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.23 / 0.0551 | — | 29.74 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 1.2% | 28.29 / 0.0534 | — | 29.75 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.24 / 0.0529 | — | 29.75 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.4% | 28.26 / 0.0524 | — | 29.75 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 28.41 / 0.0527 | — | 29.76 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.2% | 28.43 / 0.0517 | — | 29.75 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 28.25 / 0.0538 | — | 29.74 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 1.2% | 28.32 / 0.0523 | — | 29.75 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 28.25 / 0.0521 | — | 29.74 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.5% | 28.28 / 0.0516 | — | 29.75 | 2/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.18 / 0.0517 | — / — | 29.75 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.48 / 0.0550 | — / — | 29.61 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.78 / 0.0524 | — / — | 29.74 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 20.95 / 0.0114 | 29.75 / 0.0376 | 28.18 / 0.0517 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.95 | 0.7269 | 0.0114 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.25 | 0.2594 | 0.1100 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.54 | 0.2912 | 0.0744 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.54 | 0.2912 | 0.0744 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.62 | 0.3236 | 0.0715 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.57 | 0.2981 | 0.0731 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 10.57 | 0.2981 | 0.0731 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.12 | 0.7043 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.29 | 0.7467 | 0.0132 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 21.18 | 0.7396 | 0.0123 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.63 | 0.7639 | 0.0110 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 21.35 | 0.7517 | 0.0119 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 21.21 | 0.7423 | 0.0112 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.11 | 0.7034 | 0.0124 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.29 | 0.7464 | 0.0132 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 21.18 | 0.7395 | 0.0123 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.64 | 0.7642 | 0.0110 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 21.35 | 0.7515 | 0.0119 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 21.22 | 0.7422 | 0.0112 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 22.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.41 | 0.7779 | 0.0165 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.04 | 0.4088 | 0.2112 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.78 | 0.2835 | 0.1574 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 11.78 | 0.2835 | 0.1574 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 11.86 | 0.3144 | 0.1493 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 11.82 | 0.2974 | 0.1521 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 11.82 | 0.2974 | 0.1521 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.49 | 0.7676 | 0.0180 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.72 | 0.7830 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.62 | 0.7809 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.15 | 0.7914 | 0.0167 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.80 | 0.7864 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.68 | 0.7832 | 0.0166 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.79 | 0.7545 | 0.0203 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.35 | 0.7726 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.48 | 0.7777 | 0.0190 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.02 | 0.7899 | 0.0181 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.50 | 0.7811 | 0.0191 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.52 | 0.7814 | 0.0172 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 79.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.75 | 0.7113 | 0.0376 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.95 | 0.3039 | 0.4065 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.57 | 0.1698 | 0.3003 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.57 | 0.1698 | 0.3003 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.69 | 0.1748 | 0.2944 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.67 | 0.1784 | 0.3002 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.67 | 0.1784 | 0.3002 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.74 | 0.7113 | 0.0377 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.75 | 0.7115 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.75 | 0.7113 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.75 | 0.7115 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.75 | 0.7115 | 0.0376 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.75 | 0.7114 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.61 | 0.7105 | 0.0386 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.74 | 0.7116 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.75 | 0.7114 | 0.0376 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.76 | 0.7118 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.74 | 0.7118 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.74 | 0.7114 | 0.0378 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.18 | 0.7209 | 0.0517 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.26 | 0.3113 | 0.4569 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.38 | 0.1962 | 0.3767 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.38 | 0.1962 | 0.3767 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.49 | 0.2050 | 0.3655 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.47 | 0.2044 | 0.3733 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.47 | 0.2044 | 0.3733 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.78 | 0.7180 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.29 | 0.7226 | 0.0534 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.26 | 0.7218 | 0.0524 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.43 | 0.7245 | 0.0517 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.32 | 0.7233 | 0.0523 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.28 | 0.7223 | 0.0516 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.48 | 0.7151 | 0.0550 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.23 | 0.7219 | 0.0551 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.24 | 0.7216 | 0.0529 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.41 | 0.7246 | 0.0527 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.25 | 0.7229 | 0.0538 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.25 | 0.7221 | 0.0521 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 995 | None | classic | 1.48 | False | 185178 | 0.173 | 35.5 | 28.61 | 0.25 | 0.011 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 697890 | 0.790 | 80.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 697890 | 0.790 | 80.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 496159 | 0.790 | 8.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 496159 | 0.790 | 7.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 496159 | 0.790 | 7.2 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.611 | 0.020 |
| in035 | mask_ent | 0.754 | 0.020 |
| in035 | mask_grad | 0.428 | 0.020 |
| in035 | r_col | 0.689 | 0.020 |
| in035 | r_warp | 0.863 | 0.020 |

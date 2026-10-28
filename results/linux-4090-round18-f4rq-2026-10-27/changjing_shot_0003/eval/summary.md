# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.1% | 23.31 / 0.0370 | 24.94 / 0.0424 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 8.6% | 23.23 / 0.0350 | 26.64 / 0.0292 | — | — |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | 19.1% | 25.92 / 0.0316 | 27.28 / 0.0403 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 19.4% | 25.95 / 0.0310 | 26.64 / 0.0426 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 3.9% | 20.96 / 0.0182 | 21.66 / 0.0268 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 19.4% | 25.93 / 0.0307 | 26.77 / 0.0442 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 19.4% | 25.94 / 0.0308 | 26.79 / 0.0426 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.80 / 0.0823 | — / — | 18.96 / 0.0235 | 29.29 / 0.0447 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.05 / 0.0883 | — / — | 20.49 / 0.0187 | 29.29 / 0.0457 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.54 / 0.0822 | — / — | 21.58 / 0.0195 | 29.31 / 0.0448 |
| in035 | hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.55 / 0.0855 | — / — | 22.04 / 0.0188 | 29.26 / 0.0460 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.21 / 0.0891 | — / — | 21.97 / 0.0189 | 28.97 / 0.0490 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.08 / 0.0875 | — / — | 21.55 / 0.0196 | 28.94 / 0.0487 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.24 / 0.0916 | — / — | 21.89 / 0.0190 | 28.97 / 0.0500 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.25 / 0.0899 | — / — | 21.95 / 0.0189 | 28.97 / 0.0495 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.7%） | — | — | 27.80 / 0.0823 | — / — | 29.29 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 | f4rq |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.87 / 0.0834 | — | — | — | — |
| in035 | 2 | 0-3 | 28.08 / 0.0845 | — | — | — | — |
| in035 | 4 | 3-5 | 28.46 / 0.0791 | — | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.80 / 0.0823 | — | 29.29 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.05 / 0.0883 | — | 29.29 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.0% | 28.24 / 0.0800 | — | 29.29 | 3/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 28.54 / 0.0822 | — | 29.31 | 2/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.8% | 28.54 / 0.0795 | — | 29.29 | 3/3 |
| in035 | f4rq_pix3_fsl | 不复核 | —% | 28.55 / 0.0855 | — | 29.26 | 1/3 |
| in035 | f4rq_pix3_fsl | oracle | 2.2% | 28.65 / 0.0790 | — | 29.29 | 3/3 |
| in035 | f4rq_pix3bg_fsl | 不复核 | —% | 28.21 / 0.0891 | — | 28.97 | 0/3 |
| in035 | f4rq_pix3bg_fsl | oracle | 2.2% | 28.63 / 0.0791 | — | 29.28 | 3/3 |
| in035 | f4rq_pix3bg_fsl_g | 不复核 | —% | 28.08 / 0.0875 | — | 28.94 | 0/3 |
| in035 | f4rq_pix3bg_fsl_g | oracle | 1.4% | 28.53 / 0.0791 | — | 29.28 | 3/3 |
| in035 | f4rq_pix3bg_fsl_s25 | 不复核 | —% | 28.24 / 0.0916 | — | 28.97 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s25 | oracle | 2.2% | 28.61 / 0.0790 | — | 29.28 | 3/3 |
| in035 | f4rq_pix3bg_fsl_s50 | 不复核 | —% | 28.25 / 0.0899 | — | 28.97 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s50 | oracle | 2.2% | 28.62 / 0.0789 | — | 29.28 | 3/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.80 / 0.0823 | — / — | 29.29 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.05 / 0.0883 | — / — | 29.29 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.24 / 0.0800 | — / — | 29.29 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 18.96 / 0.0235 | 29.29 / 0.0447 | 27.80 / 0.0823 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.96 | 0.5870 | 0.0235 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 7.28 | 0.4586 | 0.1130 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.00 | 0.4956 | 0.0593 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 16.10 | 0.5748 | 0.0477 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 16.18 | 0.5757 | 0.0477 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 16.18 | 0.5757 | 0.0477 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 16.13 | 0.5715 | 0.0481 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 16.16 | 0.5753 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.52 | 0.6781 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.57 | 0.7073 | 0.0195 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 22.05 | 0.7247 | 0.0188 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 21.98 | 0.7223 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 21.55 | 0.7029 | 0.0196 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 21.90 | 0.7205 | 0.0189 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 21.96 | 0.7226 | 0.0189 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.49 | 0.6777 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.58 | 0.7074 | 0.0195 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 22.04 | 0.7220 | 0.0188 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 21.97 | 0.7192 | 0.0189 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 21.55 | 0.7007 | 0.0196 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 21.89 | 0.7171 | 0.0190 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 21.95 | 0.7193 | 0.0189 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 39.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.37 | 0.6930 | 0.0409 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.91 | 0.4588 | 0.2957 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 16.10 | 0.3899 | 0.1889 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 20.04 | 0.5667 | 0.1337 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 20.19 | 0.5702 | 0.1334 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 20.19 | 0.5702 | 0.1334 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 20.20 | 0.5763 | 0.1367 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 20.20 | 0.5743 | 0.1341 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.30 | 0.7047 | 0.0388 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.01 | 0.7101 | 0.0382 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.19 | 0.7125 | 0.0398 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.17 | 0.7123 | 0.0398 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 27.90 | 0.7078 | 0.0392 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.13 | 0.7121 | 0.0397 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.17 | 0.7124 | 0.0397 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.87 | 0.7042 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.97 | 0.7115 | 0.0403 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 27.41 | 0.7049 | 0.0477 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 27.13 | 0.7018 | 0.0498 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.88 | 0.6944 | 0.0474 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 27.20 | 0.7060 | 0.0517 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 27.21 | 0.7047 | 0.0502 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 63.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.29 | 0.6481 | 0.0447 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.30 | 0.2700 | 0.4350 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.03 | 0.2046 | 0.2755 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 16.08 | 0.2881 | 0.2310 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 16.07 | 0.2910 | 0.2319 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 16.07 | 0.2910 | 0.2319 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 16.06 | 0.2947 | 0.2351 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 16.06 | 0.2930 | 0.2331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 29.28 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 29.28 | 0.6480 | 0.0448 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 29.28 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 29.28 | 0.6481 | 0.0447 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.29 | 0.6492 | 0.0457 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.31 | 0.6492 | 0.0448 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 29.26 | 0.6490 | 0.0460 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.97 | 0.6481 | 0.0490 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.94 | 0.6467 | 0.0487 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.97 | 0.6488 | 0.0500 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.97 | 0.6485 | 0.0495 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.80 | 0.6599 | 0.0823 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.05 | 0.3343 | 0.5367 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.90 | 0.2830 | 0.3876 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 17.36 | 0.3917 | 0.3250 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 17.35 | 0.3940 | 0.3240 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 17.35 | 0.3940 | 0.3240 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 17.35 | 0.3988 | 0.3308 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 17.35 | 0.3968 | 0.3261 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.24 | 0.6644 | 0.0800 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.54 | 0.6662 | 0.0795 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.65 | 0.6674 | 0.0790 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.63 | 0.6673 | 0.0791 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.53 | 0.6657 | 0.0791 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.61 | 0.6672 | 0.0790 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.62 | 0.6673 | 0.0789 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.05 | 0.6650 | 0.0883 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.54 | 0.6673 | 0.0822 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.55 | 0.6680 | 0.0855 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.21 | 0.6667 | 0.0891 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.08 | 0.6625 | 0.0875 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.24 | 0.6685 | 0.0916 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.25 | 0.6678 | 0.0899 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 946 | None | classic | 1.34 | False | 173772 | 0.171 | 33.8 | 29.90 | 0.15 | 0.006 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 889300 | 0.796 | 10.0 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1711825 | 0.796 | 1.6 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1785504 | 0.796 | 1.7 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1785504 | 0.796 | 1.7 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1785504 | 0.796 | 1.7 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1785504 | 0.796 | 1.7 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.772 | 0.018 |
| in035 | mask_ent | 0.753 | 0.018 |
| in035 | mask_grad | 0.485 | 0.018 |
| in035 | r_col | 0.698 | 0.018 |
| in035 | r_warp | 0.870 | 0.018 |

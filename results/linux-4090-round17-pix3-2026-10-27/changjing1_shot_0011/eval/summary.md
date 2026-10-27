# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 13.4% | 24.43 / 0.0156 | 22.15 / 0.0234 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 11.3% | 23.79 / 0.0149 | 21.23 / 0.0376 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 4.7% | 20.93 / 0.0117 | 18.08 / 0.0309 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.8% | 24.57 / 0.0161 | 23.14 / 0.0235 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.7% | 24.55 / 0.0158 | 22.49 / 0.0304 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 4.7% | 20.89 / 0.0118 | 18.52 / 0.0250 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.05 / 0.0485 | — / — | 19.87 / 0.0131 | 29.77 / 0.0313 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.64 / 0.0542 | — / — | 19.76 / 0.0135 | 29.69 / 0.0326 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.25 / 0.0617 | — / — | 19.34 / 0.0192 | 29.78 / 0.0317 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.29 / 0.0586 | — / — | 19.32 / 0.0189 | 29.77 / 0.0313 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.59 / 0.0530 | — / — | 19.79 / 0.0149 | 29.76 / 0.0317 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.37 / 0.0585 | — / — | 19.66 / 0.0173 | 29.77 / 0.0322 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.39 / 0.0557 | — / — | 19.63 / 0.0170 | 29.77 / 0.0315 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.4%） | — | — | 28.05 / 0.0485 | — / — | 29.77 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.48 / 0.0497 | — | — | — |
| in035 | 2 | 0-3 | 27.72 / 0.0480 | — | — | — |
| in035 | 4 | 3-5 | 28.96 / 0.0477 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.05 / 0.0485 | — | 29.77 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.64 / 0.0542 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.8% | 28.01 / 0.0492 | — | 29.77 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.25 / 0.0617 | — | 29.78 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.7% | 27.68 / 0.0549 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.29 / 0.0586 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 2.1% | 27.67 / 0.0543 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.59 / 0.0530 | — | 29.76 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.8% | 27.86 / 0.0503 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.37 / 0.0585 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.7% | 27.77 / 0.0529 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.39 / 0.0557 | — | 29.77 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 2.1% | 27.75 / 0.0525 | — | 29.77 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.05 / 0.0485 | — / — | 29.77 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.64 / 0.0542 | — / — | 29.69 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.01 / 0.0492 | — / — | 29.77 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.87 / 0.0131 | 29.77 / 0.0313 | 28.05 / 0.0485 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.87 | 0.6189 | 0.0131 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.52 | 0.4391 | 0.0652 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.33 | 0.3848 | 0.0486 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.33 | 0.3848 | 0.0486 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.48 | 0.4363 | 0.0440 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.50 | 0.4025 | 0.0457 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.50 | 0.4025 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.79 | 0.6460 | 0.0135 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.36 | 0.6238 | 0.0191 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.34 | 0.6190 | 0.0187 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.80 | 0.6644 | 0.0149 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.67 | 0.6343 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.64 | 0.6257 | 0.0169 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.76 | 0.6433 | 0.0135 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.34 | 0.6218 | 0.0192 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.32 | 0.6173 | 0.0189 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.79 | 0.6639 | 0.0149 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.66 | 0.6331 | 0.0173 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.63 | 0.6247 | 0.0170 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 32.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.11 | 0.7602 | 0.0214 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.04 | 0.4741 | 0.1736 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.24 | 0.4039 | 0.1567 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.24 | 0.4039 | 0.1567 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.45 | 0.4479 | 0.1368 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 14.37 | 0.4263 | 0.1446 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 14.37 | 0.4263 | 0.1446 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.75 | 0.7620 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.46 | 0.7554 | 0.0281 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.43 | 0.7541 | 0.0274 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.87 | 0.7668 | 0.0232 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.68 | 0.7583 | 0.0258 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.63 | 0.7556 | 0.0255 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.43 | 0.7473 | 0.0271 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 24.20 | 0.7334 | 0.0391 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 24.35 | 0.7378 | 0.0342 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.04 | 0.7567 | 0.0266 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 24.55 | 0.7421 | 0.0320 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 24.62 | 0.7417 | 0.0301 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 76.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.77 | 0.7188 | 0.0313 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.94 | 0.2703 | 0.3038 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.52 | 0.1759 | 0.2437 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.52 | 0.1759 | 0.2437 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.59 | 0.1854 | 0.2369 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.60 | 0.1885 | 0.2408 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.60 | 0.1885 | 0.2408 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.69 | 0.7189 | 0.0326 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.78 | 0.7197 | 0.0317 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.77 | 0.7188 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.76 | 0.7190 | 0.0317 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.77 | 0.7196 | 0.0322 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.77 | 0.7188 | 0.0315 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.05 | 0.7219 | 0.0485 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.54 | 0.3189 | 0.3586 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.00 | 0.2389 | 0.3248 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.00 | 0.2389 | 0.3248 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.09 | 0.2540 | 0.3054 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.09 | 0.2518 | 0.3158 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.09 | 0.2518 | 0.3158 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.01 | 0.7240 | 0.0492 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.68 | 0.7208 | 0.0549 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.67 | 0.7203 | 0.0543 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.86 | 0.7240 | 0.0503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.77 | 0.7213 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.75 | 0.7204 | 0.0525 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.64 | 0.7213 | 0.0542 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.25 | 0.7174 | 0.0617 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.29 | 0.7167 | 0.0586 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.59 | 0.7218 | 0.0530 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.37 | 0.7185 | 0.0585 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.39 | 0.7174 | 0.0557 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 855 | None | classic | 0.41 | False | 451441 | 0.518 | 89.3 | 32.11 | 0.25 | 0.008 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1352612 | 0.808 | 87.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1352612 | 0.808 | 87.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 983881 | 0.808 | 10.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 983881 | 0.808 | 7.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 983881 | 0.808 | 7.4 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.793 | 0.019 |
| in035 | mask_ent | 0.677 | 0.019 |
| in035 | mask_grad | 0.486 | 0.019 |
| in035 | r_col | 0.857 | 0.019 |
| in035 | r_warp | 0.917 | 0.019 |

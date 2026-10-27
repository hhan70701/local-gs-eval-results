# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 18.2% | 22.06 / 0.0238 | 21.75 / 0.0376 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.6% | 21.46 / 0.0244 | 21.29 / 0.0409 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 5.8% | 18.81 / 0.0180 | 18.53 / 0.0283 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 18.6% | 22.24 / 0.0258 | 22.87 / 0.0311 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 18.5% | 22.21 / 0.0259 | 22.48 / 0.0366 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 5.6% | 18.62 / 0.0179 | 19.08 / 0.0230 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 26.36 / 0.0567 | — / — | 18.85 / 0.0187 | 29.73 / 0.0343 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.72 / 0.0626 | — / — | 20.05 / 0.0187 | 29.55 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.27 / 0.0670 | — / — | 19.31 / 0.0231 | 29.46 / 0.0360 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.35 / 0.0638 | — / — | 19.37 / 0.0223 | 29.51 / 0.0356 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.66 / 0.0609 | — / — | 19.83 / 0.0202 | 29.72 / 0.0345 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.46 / 0.0643 | — / — | 19.57 / 0.0216 | 29.50 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.55 / 0.0607 | — / — | 19.61 / 0.0206 | 29.64 / 0.0349 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 9.8%） | — | — | 26.36 / 0.0567 | — / — | 29.73 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 25.93 / 0.0565 | — | — | — |
| in035 | 2 | 0-3 | 25.43 / 0.0610 | — | — | — |
| in035 | 4 | 3-5 | 27.73 / 0.0526 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 26.36 / 0.0567 | — | 29.73 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 26.72 / 0.0626 | — | 29.55 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 5.4% | 26.99 / 0.0580 | — | 29.70 | 1/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 26.27 / 0.0670 | — | 29.46 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 5.0% | 26.56 / 0.0613 | — | 29.69 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 26.35 / 0.0638 | — | 29.51 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 2.9% | 26.59 / 0.0604 | — | 29.70 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 26.66 / 0.0609 | — | 29.72 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 5.3% | 26.84 / 0.0583 | — | 29.74 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 26.46 / 0.0643 | — | 29.50 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 5.3% | 26.71 / 0.0597 | — | 29.70 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 26.55 / 0.0607 | — | 29.64 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 2.9% | 26.72 / 0.0586 | — | 29.72 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 26.36 / 0.0567 | — / — | 29.73 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 26.72 / 0.0626 | — / — | 29.55 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 26.99 / 0.0580 | — / — | 29.70 | 1/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 18.85 / 0.0187 | 29.73 / 0.0343 | 26.36 / 0.0567 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 9.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.85 | 0.5620 | 0.0187 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.73 | 0.4865 | 0.0800 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.42 | 0.4238 | 0.0628 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.42 | 0.4238 | 0.0628 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.70 | 0.4706 | 0.0589 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 14.57 | 0.4385 | 0.0612 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 14.57 | 0.4385 | 0.0612 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.06 | 0.6536 | 0.0186 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.32 | 0.5963 | 0.0231 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.37 | 0.5923 | 0.0223 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.83 | 0.6297 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.58 | 0.6075 | 0.0215 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.61 | 0.6015 | 0.0206 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.05 | 0.6523 | 0.0187 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 19.31 | 0.5952 | 0.0231 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 19.37 | 0.5920 | 0.0223 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.83 | 0.6293 | 0.0202 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 19.57 | 0.6065 | 0.0216 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 19.61 | 0.6013 | 0.0206 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 31.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.35 | 0.7094 | 0.0264 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.80 | 0.4915 | 0.1735 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.61 | 0.4229 | 0.1518 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.61 | 0.4229 | 0.1518 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.72 | 0.4455 | 0.1414 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 14.70 | 0.4395 | 0.1452 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 14.70 | 0.4395 | 0.1452 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 24.30 | 0.7403 | 0.0273 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.58 | 0.7195 | 0.0310 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 23.57 | 0.7150 | 0.0301 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 23.91 | 0.7275 | 0.0285 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 23.83 | 0.7244 | 0.0292 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 23.80 | 0.7189 | 0.0286 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 23.06 | 0.7216 | 0.0346 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 23.17 | 0.7046 | 0.0385 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 23.27 | 0.7048 | 0.0341 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 23.62 | 0.7175 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 23.52 | 0.7143 | 0.0333 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 23.56 | 0.7116 | 0.0306 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 74.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.73 | 0.7262 | 0.0343 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.95 | 0.2988 | 0.3159 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.81 | 0.2031 | 0.2557 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.81 | 0.2031 | 0.2557 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.93 | 0.2177 | 0.2458 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.92 | 0.2167 | 0.2512 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.92 | 0.2167 | 0.2512 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.70 | 0.7256 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.69 | 0.7256 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.70 | 0.7259 | 0.0344 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.74 | 0.7266 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.70 | 0.7258 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.72 | 0.7261 | 0.0344 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.55 | 0.7242 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.46 | 0.7243 | 0.0360 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.51 | 0.7244 | 0.0356 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.72 | 0.7264 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.50 | 0.7247 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.64 | 0.7255 | 0.0349 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.36 | 0.7141 | 0.0567 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.61 | 0.3464 | 0.3760 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.27 | 0.2622 | 0.3434 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.27 | 0.2622 | 0.3434 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.38 | 0.2791 | 0.3264 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.37 | 0.2753 | 0.3355 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.37 | 0.2753 | 0.3355 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.99 | 0.7234 | 0.0580 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.56 | 0.7166 | 0.0613 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.59 | 0.7158 | 0.0604 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.84 | 0.7208 | 0.0583 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.71 | 0.7182 | 0.0597 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.72 | 0.7171 | 0.0586 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.72 | 0.7205 | 0.0626 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.27 | 0.7126 | 0.0670 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.35 | 0.7124 | 0.0638 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.66 | 0.7184 | 0.0609 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.46 | 0.7149 | 0.0643 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.55 | 0.7147 | 0.0607 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 838 | None | classic | 0.43 | False | 508642 | 0.976 | 187.3 | 31.28 | 0.25 | 0.001 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1414493 | 0.793 | 201.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1414493 | 0.793 | 201.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1061268 | 0.793 | 8.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1061268 | 0.793 | 8.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1061268 | 0.793 | 8.4 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.696 | 0.041 |
| in035 | mask_ent | 0.703 | 0.041 |
| in035 | mask_grad | 0.427 | 0.041 |
| in035 | r_col | 0.837 | 0.041 |
| in035 | r_warp | 0.873 | 0.041 |

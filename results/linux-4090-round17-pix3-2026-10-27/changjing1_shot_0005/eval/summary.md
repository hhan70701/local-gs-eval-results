# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.1% | 26.71 / 0.0329 | 25.76 / 0.0510 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 4.5% | 26.44 / 0.0323 | 24.50 / 0.0737 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 1.6% | 23.66 / 0.0353 | 21.93 / 0.0641 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 5.5% | 26.60 / 0.0342 | 26.29 / 0.0533 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 5.5% | 26.59 / 0.0336 | 25.47 / 0.0595 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 1.5% | 23.31 / 0.0300 | 21.38 / 0.0572 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 31.25 / 0.0654 | — / — | 21.17 / 0.0158 | 32.59 / 0.0406 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.16 / 0.0682 | — / — | 22.23 / 0.0155 | 32.50 / 0.0418 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.17 / 0.0700 | — / — | 22.15 / 0.0181 | 32.64 / 0.0407 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.22 / 0.0673 | — / — | 22.00 / 0.0171 | 32.60 / 0.0406 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 31.40 / 0.0661 | — / — | 22.60 / 0.0154 | 32.65 / 0.0406 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 31.38 / 0.0675 | — / — | 22.74 / 0.0154 | 32.67 / 0.0411 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 31.32 / 0.0656 | — / — | 22.18 / 0.0153 | 32.60 / 0.0406 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 2.7%） | — | — | 31.25 / 0.0654 | — / — | 32.59 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 29.75 / 0.0739 | — | — | — |
| in035 | 2 | 0-3 | 31.42 / 0.0621 | — | — | — |
| in035 | 4 | 3-5 | 32.60 / 0.0603 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 31.25 / 0.0654 | — | 32.59 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 31.16 / 0.0682 | — | 32.50 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 0.8% | 31.42 / 0.0640 | — | 32.59 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 31.17 / 0.0700 | — | 32.64 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 0.7% | 31.42 / 0.0658 | — | 32.59 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 31.22 / 0.0673 | — | 32.60 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.4% | 31.39 / 0.0653 | — | 32.59 | 2/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 31.40 / 0.0661 | — | 32.65 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 0.8% | 31.51 / 0.0646 | — | 32.59 | 3/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 31.38 / 0.0675 | — | 32.67 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 0.8% | 31.53 / 0.0643 | — | 32.60 | 3/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 31.32 / 0.0656 | — | 32.60 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.4% | 31.43 / 0.0644 | — | 32.59 | 3/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 31.25 / 0.0654 | — / — | 32.59 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 31.16 / 0.0682 | — / — | 32.50 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 31.42 / 0.0640 | — / — | 32.59 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 21.17 / 0.0158 | 32.59 / 0.0406 | 31.25 / 0.0654 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 2.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 21.17 | 0.6195 | 0.0158 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 11.58 | 0.6010 | 0.0924 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.19 | 0.5007 | 0.0740 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.19 | 0.5007 | 0.0740 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.50 | 0.5507 | 0.0700 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 15.49 | 0.5407 | 0.0695 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 15.49 | 0.5407 | 0.0695 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.21 | 0.6916 | 0.0156 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.13 | 0.6470 | 0.0183 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.00 | 0.6408 | 0.0172 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.57 | 0.6811 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 22.72 | 0.6809 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 22.18 | 0.6543 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.23 | 0.6916 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 22.15 | 0.6465 | 0.0181 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 22.00 | 0.6402 | 0.0171 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.60 | 0.6815 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 22.74 | 0.6808 | 0.0154 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 22.18 | 0.6537 | 0.0153 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 41.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.71 | 0.8138 | 0.0317 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.34 | 0.5396 | 0.3735 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.62 | 0.2338 | 0.3425 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.62 | 0.2338 | 0.3425 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.66 | 0.2566 | 0.3332 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.64 | 0.2498 | 0.3339 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 10.64 | 0.2498 | 0.3339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.96 | 0.8168 | 0.0316 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.01 | 0.8146 | 0.0338 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.96 | 0.8144 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 30.18 | 0.8178 | 0.0321 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 30.24 | 0.8179 | 0.0320 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 30.04 | 0.8159 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.21 | 0.8071 | 0.0366 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.89 | 0.8019 | 0.0424 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.16 | 0.8076 | 0.0381 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.62 | 0.8118 | 0.0367 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.12 | 0.8086 | 0.0378 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.13 | 0.8095 | 0.0358 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 68.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 32.59 | 0.8225 | 0.0406 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.65 | 0.5358 | 0.5342 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 9.10 | 0.1504 | 0.4817 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 9.10 | 0.1504 | 0.4817 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 9.12 | 0.1533 | 0.4756 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 9.12 | 0.1562 | 0.4794 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 9.12 | 0.1562 | 0.4794 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.59 | 0.8226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 32.59 | 0.8226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 32.59 | 0.8225 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 32.59 | 0.8226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 32.60 | 0.8227 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 32.59 | 0.8225 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 32.50 | 0.8221 | 0.0418 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 32.64 | 0.8236 | 0.0407 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 32.60 | 0.8227 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 32.65 | 0.8237 | 0.0406 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 32.67 | 0.8243 | 0.0411 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 32.60 | 0.8227 | 0.0406 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 31.25 | 0.8156 | 0.0654 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.73 | 0.5375 | 0.6221 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 9.08 | 0.1561 | 0.5839 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 9.08 | 0.1561 | 0.5839 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 9.10 | 0.1632 | 0.5716 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 9.09 | 0.1637 | 0.5778 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 9.09 | 0.1637 | 0.5778 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.42 | 0.8169 | 0.0640 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.42 | 0.8159 | 0.0658 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.39 | 0.8156 | 0.0653 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 31.51 | 0.8170 | 0.0646 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 31.53 | 0.8171 | 0.0643 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 31.43 | 0.8162 | 0.0644 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 31.16 | 0.8148 | 0.0682 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 31.17 | 0.8141 | 0.0700 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 31.22 | 0.8145 | 0.0673 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 31.40 | 0.8168 | 0.0661 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 31.38 | 0.8165 | 0.0675 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 31.32 | 0.8154 | 0.0656 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 591 | None | classic | 0.52 | False | 115382 | 0.171 | 27.7 | 30.92 | 0.20 | 0.014 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 451754 | 0.804 | 78.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 451754 | 0.804 | 78.7 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 311972 | 0.804 | 8.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 311972 | 0.804 | 7.9 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 311972 | 0.804 | 7.9 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.852 | 0.009 |
| in035 | mask_ent | 0.779 | 0.009 |
| in035 | mask_grad | 0.507 | 0.009 |
| in035 | r_col | 0.644 | 0.009 |
| in035 | r_warp | 0.880 | 0.009 |

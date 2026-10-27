# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 21.9% | 24.74 / 0.0353 | 26.18 / 0.0477 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 19.9% | 24.33 / 0.0352 | 24.96 / 0.0659 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 3.9% | 18.89 / 0.0266 | 20.08 / 0.0398 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 23.6% | 25.34 / 0.0368 | 27.06 / 0.0373 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 23.6% | 25.31 / 0.0369 | 26.99 / 0.0523 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 3.8% | 19.35 / 0.0278 | 21.83 / 0.0260 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.99 / 0.0657 | — / — | 18.40 / 0.0218 | 30.12 / 0.0305 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.68 / 0.0757 | — / — | 20.82 / 0.0195 | 30.08 / 0.0314 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.38 / 0.0843 | — / — | 20.08 / 0.0247 | 30.05 / 0.0318 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.52 / 0.0730 | — / — | 20.06 / 0.0230 | 30.05 / 0.0317 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.78 / 0.0686 | — / — | 20.05 / 0.0221 | 30.11 / 0.0313 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.76 / 0.0778 | — / — | 20.25 / 0.0221 | 30.08 / 0.0315 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.79 / 0.0664 | — / — | 20.17 / 0.0213 | 30.11 / 0.0308 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.8%） | — | — | 27.99 / 0.0657 | — / — | 30.12 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.46 / 0.0702 | — | — | — |
| in035 | 2 | 0-3 | 27.34 / 0.0684 | — | — | — |
| in035 | 4 | 3-5 | 29.18 / 0.0583 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.99 / 0.0657 | — | 30.12 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.68 / 0.0757 | — | 30.08 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 3.1% | 29.02 / 0.0638 | — | 30.12 | 3/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.38 / 0.0843 | — | 30.05 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 3.0% | 28.80 / 0.0694 | — | 30.12 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.52 / 0.0730 | — | 30.05 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 2.2% | 28.80 / 0.0674 | — | 30.12 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 28.78 / 0.0686 | — | 30.11 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 3.0% | 28.82 / 0.0665 | — | 30.12 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 28.76 / 0.0778 | — | 30.08 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 3.0% | 28.90 / 0.0668 | — | 30.12 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 28.79 / 0.0664 | — | 30.11 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 2.1% | 28.87 / 0.0656 | — | 30.12 | 2/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.99 / 0.0657 | — / — | 30.12 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.68 / 0.0757 | — / — | 30.08 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 29.02 / 0.0638 | — / — | 30.12 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 18.40 / 0.0218 | 30.12 / 0.0305 | 27.99 / 0.0657 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.40 | 0.5665 | 0.0218 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 9.57 | 0.4983 | 0.0819 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.32 | 0.4538 | 0.0721 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.32 | 0.4538 | 0.0721 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.32 | 0.4466 | 0.0693 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.35 | 0.4565 | 0.0695 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.35 | 0.4565 | 0.0695 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.83 | 0.6841 | 0.0194 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.08 | 0.6608 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.06 | 0.6522 | 0.0230 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.05 | 0.6485 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.25 | 0.6620 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.17 | 0.6502 | 0.0213 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.82 | 0.6839 | 0.0195 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.08 | 0.6602 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.06 | 0.6520 | 0.0230 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.05 | 0.6482 | 0.0221 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.25 | 0.6616 | 0.0221 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.17 | 0.6501 | 0.0213 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 50.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.55 | 0.7800 | 0.0369 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.22 | 0.5886 | 0.2163 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.30 | 0.5272 | 0.2065 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.30 | 0.5272 | 0.2065 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.40 | 0.5300 | 0.1823 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 14.38 | 0.5405 | 0.1946 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 14.38 | 0.5405 | 0.1946 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.12 | 0.7918 | 0.0362 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.70 | 0.7903 | 0.0418 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.71 | 0.7897 | 0.0398 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.74 | 0.7892 | 0.0384 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.88 | 0.7916 | 0.0386 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.83 | 0.7899 | 0.0375 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.38 | 0.7918 | 0.0484 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.96 | 0.7838 | 0.0596 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.27 | 0.7859 | 0.0469 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.67 | 0.7859 | 0.0401 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.65 | 0.7925 | 0.0504 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.70 | 0.7887 | 0.0392 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 55.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.12 | 0.7280 | 0.0305 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.97 | 0.2513 | 0.3138 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.09 | 0.1584 | 0.2642 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.09 | 0.1584 | 0.2642 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.49 | 0.1806 | 0.2574 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.48 | 0.1842 | 0.2606 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.48 | 0.1842 | 0.2606 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.12 | 0.7280 | 0.0306 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 30.12 | 0.7280 | 0.0305 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 30.08 | 0.7280 | 0.0314 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 30.05 | 0.7277 | 0.0318 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 30.05 | 0.7276 | 0.0317 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 30.11 | 0.7273 | 0.0313 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 30.08 | 0.7280 | 0.0315 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 30.11 | 0.7279 | 0.0308 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.99 | 0.7586 | 0.0657 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.99 | 0.4300 | 0.4061 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.15 | 0.3651 | 0.3743 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.15 | 0.3651 | 0.3743 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.51 | 0.3770 | 0.3492 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.50 | 0.3854 | 0.3636 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.50 | 0.3854 | 0.3636 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.02 | 0.7656 | 0.0638 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.80 | 0.7645 | 0.0694 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.80 | 0.7641 | 0.0674 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.82 | 0.7640 | 0.0665 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.90 | 0.7650 | 0.0668 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.87 | 0.7642 | 0.0656 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.68 | 0.7677 | 0.0757 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.38 | 0.7632 | 0.0843 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.52 | 0.7625 | 0.0730 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.78 | 0.7621 | 0.0686 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.76 | 0.7664 | 0.0778 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.79 | 0.7637 | 0.0664 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1056 | None | classic | 0.39 | False | 764336 | 0.691 | 120.2 | 31.00 | 0.15 | 0.010 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1433417 | 0.807 | 90.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1433417 | 0.807 | 90.4 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1128117 | 0.807 | 9.6 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1128117 | 0.807 | 7.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1128117 | 0.807 | 7.2 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.819 | 0.024 |
| in035 | mask_ent | 0.684 | 0.024 |
| in035 | mask_grad | 0.467 | 0.024 |
| in035 | r_col | 0.787 | 0.024 |
| in035 | r_warp | 0.864 | 0.024 |

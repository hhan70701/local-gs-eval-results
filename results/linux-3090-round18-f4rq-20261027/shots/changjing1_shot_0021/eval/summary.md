# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 12.4% | 18.45 / 0.0292 | 17.62 / 0.0433 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.2% | 17.51 / 0.0376 | 17.38 / 0.0474 | — | — |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | 31.2% | 19.00 / 0.0416 | 18.87 / 0.0635 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 32.5% | 19.15 / 0.0397 | 18.95 / 0.0670 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 10.8% | 16.79 / 0.0239 | 16.19 / 0.0498 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 32.4% | 19.14 / 0.0396 | 19.05 / 0.0678 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 32.4% | 19.14 / 0.0395 | 18.99 / 0.0675 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 22.74 / 0.0688 | — / — | 14.97 / 0.0348 | 29.91 / 0.0341 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.63 / 0.0742 | — / — | 15.17 / 0.0371 | 29.68 / 0.0361 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.67 / 0.0730 | — / — | 15.18 / 0.0373 | 29.79 / 0.0349 |
| in035 | hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 22.51 / 0.0848 | — / — | 15.53 / 0.0399 | 28.83 / 0.0430 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 22.45 / 0.0892 | — / — | 15.53 / 0.0401 | 28.54 / 0.0451 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 22.41 / 0.0864 | — / — | 15.37 / 0.0414 | 28.57 / 0.0429 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 22.53 / 0.0899 | — / — | 15.57 / 0.0391 | 28.63 / 0.0461 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 22.48 / 0.0900 | — / — | 15.53 / 0.0395 | 28.55 / 0.0460 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 12.2%） | — | — | 22.74 / 0.0688 | — / — | 29.91 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 | f4rq |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 20.93 / 0.0680 | — | — | — | — |
| in035 | 2 | 0-3 | 19.48 / 0.0817 | — | — | — | — |
| in035 | 4 | 3-5 | 27.82 / 0.0567 | — | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 22.74 / 0.0688 | — | 29.91 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 22.63 / 0.0742 | — | 29.68 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 4.8% | 22.80 / 0.0711 | — | 29.88 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 22.67 / 0.0730 | — | 29.79 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 6.6% | 22.78 / 0.0703 | — | 29.88 | 0/3 |
| in035 | f4rq_pix3_fsl | 不复核 | —% | 22.51 / 0.0848 | — | 28.83 | 0/3 |
| in035 | f4rq_pix3_fsl | oracle | 9.5% | 22.85 / 0.0725 | — | 29.82 | 1/3 |
| in035 | f4rq_pix3bg_fsl | 不复核 | —% | 22.45 / 0.0892 | — | 28.54 | 0/3 |
| in035 | f4rq_pix3bg_fsl | oracle | 9.5% | 22.85 / 0.0725 | — | 29.81 | 1/3 |
| in035 | f4rq_pix3bg_fsl_g | 不复核 | —% | 22.41 / 0.0864 | — | 28.57 | 0/3 |
| in035 | f4rq_pix3bg_fsl_g | oracle | 4.9% | 22.78 / 0.0736 | — | 29.80 | 1/3 |
| in035 | f4rq_pix3bg_fsl_s25 | 不复核 | —% | 22.53 / 0.0899 | — | 28.63 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s25 | oracle | 9.5% | 22.90 / 0.0719 | — | 29.83 | 1/3 |
| in035 | f4rq_pix3bg_fsl_s50 | 不复核 | —% | 22.48 / 0.0900 | — | 28.55 | 0/3 |
| in035 | f4rq_pix3bg_fsl_s50 | oracle | 9.5% | 22.87 / 0.0725 | — | 29.80 | 1/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 22.74 / 0.0688 | — / — | 29.91 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 22.63 / 0.0742 | — / — | 29.68 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 22.80 / 0.0711 | — / — | 29.88 | 0/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 14.97 / 0.0348 | 29.91 / 0.0341 | 22.74 / 0.0688 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 12.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 14.97 | 0.5468 | 0.0348 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 8.52 | 0.4282 | 0.1192 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.43 | 0.4566 | 0.0835 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 12.84 | 0.4971 | 0.0699 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 12.84 | 0.4981 | 0.0691 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 12.84 | 0.4981 | 0.0691 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 12.88 | 0.5014 | 0.0685 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 12.85 | 0.4976 | 0.0689 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 15.17 | 0.5803 | 0.0371 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 15.18 | 0.5923 | 0.0373 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 15.53 | 0.6019 | 0.0398 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 15.53 | 0.6016 | 0.0400 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 15.36 | 0.5815 | 0.0413 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 15.57 | 0.6060 | 0.0390 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 15.53 | 0.6020 | 0.0394 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 15.17 | 0.5799 | 0.0371 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 15.18 | 0.5921 | 0.0373 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 15.53 | 0.6013 | 0.0399 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 15.53 | 0.6010 | 0.0401 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 15.37 | 0.5815 | 0.0414 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 15.57 | 0.6053 | 0.0391 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 15.53 | 0.6013 | 0.0395 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 33.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.58 | 0.7122 | 0.0379 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.76 | 0.4744 | 0.2268 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.16 | 0.4055 | 0.1770 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 14.49 | 0.5193 | 0.1290 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 14.75 | 0.5404 | 0.1233 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 14.75 | 0.5404 | 0.1233 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 14.79 | 0.5429 | 0.1241 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 14.77 | 0.5415 | 0.1235 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.70 | 0.7226 | 0.0406 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.67 | 0.7247 | 0.0396 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 19.87 | 0.7217 | 0.0414 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 19.87 | 0.7213 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 19.79 | 0.7140 | 0.0424 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 19.92 | 0.7239 | 0.0409 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 19.88 | 0.7220 | 0.0414 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 19.27 | 0.7089 | 0.0461 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 19.48 | 0.7137 | 0.0444 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 19.48 | 0.6914 | 0.0522 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 19.40 | 0.6831 | 0.0580 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 19.38 | 0.6782 | 0.0569 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 19.47 | 0.6863 | 0.0582 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 19.44 | 0.6844 | 0.0580 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 73.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.91 | 0.7219 | 0.0341 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.58 | 0.3104 | 0.3672 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.57 | 0.1553 | 0.2680 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 15.25 | 0.3584 | 0.2070 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 15.25 | 0.3670 | 0.2060 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 15.25 | 0.3670 | 0.2060 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 15.26 | 0.3706 | 0.2089 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 15.25 | 0.3688 | 0.2077 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.88 | 0.7217 | 0.0345 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.88 | 0.7217 | 0.0343 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 29.82 | 0.7214 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 29.81 | 0.7214 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 29.80 | 0.7212 | 0.0350 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 29.83 | 0.7214 | 0.0348 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 29.80 | 0.7213 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.68 | 0.7213 | 0.0361 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.79 | 0.7212 | 0.0349 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 28.83 | 0.7134 | 0.0430 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 28.54 | 0.7095 | 0.0451 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 28.57 | 0.7115 | 0.0429 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 28.63 | 0.7101 | 0.0461 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 28.55 | 0.7097 | 0.0460 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.74 | 0.7087 | 0.0688 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.38 | 0.3457 | 0.4414 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.61 | 0.2257 | 0.3654 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 14.67 | 0.3957 | 0.2806 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 14.67 | 0.4046 | 0.2790 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 14.67 | 0.4046 | 0.2790 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 14.70 | 0.4082 | 0.2816 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 14.68 | 0.4061 | 0.2808 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.80 | 0.7120 | 0.0711 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.78 | 0.7133 | 0.0703 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 22.85 | 0.7114 | 0.0725 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 22.85 | 0.7114 | 0.0725 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 22.78 | 0.7086 | 0.0736 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 22.90 | 0.7123 | 0.0719 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 22.87 | 0.7114 | 0.0725 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.63 | 0.7099 | 0.0742 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.67 | 0.7107 | 0.0730 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 22.51 | 0.6977 | 0.0848 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 22.45 | 0.6934 | 0.0892 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 22.41 | 0.6931 | 0.0864 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 22.53 | 0.6952 | 0.0899 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 22.48 | 0.6940 | 0.0900 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 877 | None | classic | 1.15 | False | 389297 | 0.660 | 113.2 | 27.94 | 0.12 | 0.030 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1013333 | 0.818 | 8.2 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1945622 | 0.818 | 3.4 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2158340 | 0.818 | 3.6 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2158340 | 0.818 | 3.6 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2158340 | 0.818 | 3.6 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2158340 | 0.818 | 3.6 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.553 | 0.073 |
| in035 | mask_ent | 0.728 | 0.073 |
| in035 | mask_grad | 0.405 | 0.073 |
| in035 | r_col | 0.876 | 0.073 |
| in035 | r_warp | 0.854 | 0.073 |

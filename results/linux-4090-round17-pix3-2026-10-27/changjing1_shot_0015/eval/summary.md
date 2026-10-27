# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.0% | 24.75 / 0.0060 | 21.76 / 0.0099 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 5.0% | 24.07 / 0.0068 | 20.84 / 0.0159 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 1.9% | 20.50 / 0.0047 | 17.15 / 0.0106 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 7.2% | 25.22 / 0.0080 | 22.45 / 0.0142 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 7.1% | 25.18 / 0.0078 | 22.28 / 0.0154 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.4% | 21.21 / 0.0079 | 17.90 / 0.0168 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 28.08 / 0.0539 | — / — | 20.66 / 0.0139 | 29.61 / 0.0359 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 / 0.0552 | — / — | 21.33 / 0.0131 | 29.49 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.61 / 0.0579 | — / — | 20.14 / 0.0155 | 29.59 / 0.0369 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.62 / 0.0562 | — / — | 20.15 / 0.0153 | 29.58 / 0.0368 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.54 / 0.0585 | — / — | 20.12 / 0.0155 | 29.57 / 0.0380 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.59 / 0.0592 | — / — | 20.23 / 0.0152 | 29.57 / 0.0383 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.59 / 0.0575 | — / — | 20.18 / 0.0152 | 29.56 / 0.0379 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 5.7%） | — | — | 28.08 / 0.0539 | — / — | 29.61 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 27.40 / 0.0537 | — | — | — |
| in035 | 2 | 0-3 | 27.60 / 0.0563 | — | — | — |
| in035 | 4 | 3-5 | 29.23 / 0.0517 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 28.08 / 0.0539 | — | 29.61 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.95 / 0.0552 | — | 29.49 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 1.0% | 28.30 / 0.0529 | — | 29.61 | 2/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 27.61 / 0.0579 | — | 29.59 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 0.9% | 27.78 / 0.0551 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 27.62 / 0.0562 | — | 29.58 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 0.7% | 27.78 / 0.0548 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.54 / 0.0585 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 1.1% | 27.75 / 0.0550 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 27.59 / 0.0592 | — | 29.57 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 1.1% | 27.81 / 0.0548 | — | 29.61 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 27.59 / 0.0575 | — | 29.56 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 0.8% | 27.80 / 0.0547 | — | 29.61 | 0/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 28.08 / 0.0539 | — / — | 29.61 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.95 / 0.0552 | — / — | 29.49 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 28.30 / 0.0529 | — / — | 29.61 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 20.66 / 0.0139 | 29.61 / 0.0359 | 28.08 / 0.0539 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 5.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.66 | 0.6326 | 0.0139 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.30 | 0.2461 | 0.1362 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 10.92 | 0.1578 | 0.0887 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 10.92 | 0.1578 | 0.0887 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 10.96 | 0.1686 | 0.0867 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 10.99 | 0.1681 | 0.0866 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 10.99 | 0.1681 | 0.0866 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.35 | 0.6642 | 0.0130 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.15 | 0.6298 | 0.0155 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.16 | 0.6298 | 0.0153 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.12 | 0.6319 | 0.0154 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.24 | 0.6334 | 0.0152 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.19 | 0.6295 | 0.0152 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 21.33 | 0.6628 | 0.0131 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 20.14 | 0.6293 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.15 | 0.6293 | 0.0153 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 20.12 | 0.6314 | 0.0155 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 20.23 | 0.6330 | 0.0152 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 20.18 | 0.6292 | 0.0152 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 28.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.66 | 0.7605 | 0.0213 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 4.57 | 0.4076 | 0.2385 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.54 | 0.2588 | 0.1833 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.54 | 0.2588 | 0.1833 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.72 | 0.2850 | 0.1757 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.67 | 0.2742 | 0.1776 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.67 | 0.2742 | 0.1776 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.09 | 0.7693 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 26.12 | 0.7587 | 0.0229 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 26.11 | 0.7581 | 0.0225 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.12 | 0.7605 | 0.0221 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 26.21 | 0.7605 | 0.0220 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 26.15 | 0.7586 | 0.0219 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 25.63 | 0.7567 | 0.0240 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 25.27 | 0.7474 | 0.0283 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 25.43 | 0.7504 | 0.0253 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 25.39 | 0.7520 | 0.0252 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 25.32 | 0.7493 | 0.0258 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 25.36 | 0.7490 | 0.0246 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 78.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.61 | 0.7063 | 0.0359 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.29 | 0.2794 | 0.3992 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.40 | 0.1176 | 0.2957 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.40 | 0.1176 | 0.2957 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.48 | 0.1219 | 0.2940 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.48 | 0.1232 | 0.2952 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.48 | 0.1232 | 0.2952 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.61 | 0.7064 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.61 | 0.7064 | 0.0359 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.61 | 0.7063 | 0.0359 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.49 | 0.7059 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.59 | 0.7065 | 0.0369 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.58 | 0.7061 | 0.0368 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.57 | 0.7060 | 0.0380 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.57 | 0.7065 | 0.0383 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.56 | 0.7056 | 0.0379 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 28.08 | 0.7093 | 0.0539 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.61 | 0.2910 | 0.4685 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 12.45 | 0.1455 | 0.4059 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 12.45 | 0.1455 | 0.4059 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 12.54 | 0.1527 | 0.4007 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 12.54 | 0.1528 | 0.4029 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 12.54 | 0.1528 | 0.4029 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.30 | 0.7114 | 0.0529 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.78 | 0.7086 | 0.0551 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.78 | 0.7084 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.75 | 0.7088 | 0.0550 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.81 | 0.7089 | 0.0548 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.80 | 0.7083 | 0.0547 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 | 0.7091 | 0.0552 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.61 | 0.7074 | 0.0579 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.62 | 0.7071 | 0.0562 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.54 | 0.7069 | 0.0585 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.59 | 0.7074 | 0.0592 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.59 | 0.7063 | 0.0575 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 676 | None | classic | 0.30 | False | 660446 | 0.687 | 120.1 | 31.39 | 0.37 | 0.021 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 836425 | 0.821 | 82.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 836425 | 0.821 | 82.1 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 637074 | 0.821 | 10.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 637074 | 0.821 | 7.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 637074 | 0.821 | 7.2 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.691 | 0.018 |
| in035 | mask_ent | 0.756 | 0.018 |
| in035 | mask_grad | 0.475 | 0.018 |
| in035 | r_col | 0.701 | 0.018 |
| in035 | r_warp | 0.861 | 0.018 |

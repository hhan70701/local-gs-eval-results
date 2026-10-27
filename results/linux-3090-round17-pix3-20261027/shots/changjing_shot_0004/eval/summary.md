# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 10.1% | 23.85 / 0.0201 | 23.87 / 0.0238 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 8.4% | 23.10 / 0.0193 | 23.58 / 0.0399 | — | — |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 2.4% | 19.15 / 0.0180 | 20.28 / 0.0293 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 9.5% | 23.59 / 0.0193 | 25.56 / 0.0199 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 9.4% | 23.55 / 0.0193 | 24.93 / 0.0260 | — | — |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 2.3% | 18.96 / 0.0143 | 21.37 / 0.0154 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.80 / 0.0722 | — / — | 19.68 / 0.0231 | 29.42 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.73 / 0.0760 | — / — | 20.50 / 0.0199 | 29.35 / 0.0350 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.02 / 0.0826 | — / — | 21.03 / 0.0259 | 29.39 / 0.0349 |
| in035 | hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.02 / 0.0776 | — / — | 20.87 / 0.0247 | 29.38 / 0.0347 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.32 / 0.0722 | — / — | 21.50 / 0.0207 | 29.44 / 0.0339 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.19 / 0.0775 | — / — | 21.32 / 0.0235 | 29.42 / 0.0345 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.16 / 0.0728 | — / — | 21.05 / 0.0227 | 29.42 / 0.0340 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 6.2%） | — | — | 27.80 / 0.0722 | — / — | 29.42 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 |
|---|---|---|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.85 / 0.0723 | — | — | — |
| in035 | 2 | 0-3 | 27.88 / 0.0733 | — | — | — |
| in035 | 4 | 3-5 | 28.67 / 0.0709 | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.80 / 0.0722 | — | 29.42 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 27.73 / 0.0760 | — | 29.35 | 0/3 |
| in035 | cnw_cnn_mw | oracle | 2.5% | 27.95 / 0.0704 | — | 29.40 | 3/3 |
| in035 | cnw_cnn_pix2_fsl | 不复核 | —% | 28.02 / 0.0826 | — | 29.39 | 0/3 |
| in035 | cnw_cnn_pix2_fsl | oracle | 2.4% | 28.20 / 0.0756 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_pix2_fsl_g | 不复核 | —% | 28.02 / 0.0776 | — | 29.38 | 0/3 |
| in035 | cnw_cnn_pix2_fsl_g | oracle | 1.4% | 28.16 / 0.0741 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 28.32 / 0.0722 | — | 29.44 | 1/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 2.5% | 28.36 / 0.0704 | — | 29.42 | 3/3 |
| in035 | cnw_cnn_pix3n_fsl | 不复核 | —% | 28.19 / 0.0775 | — | 29.42 | 0/3 |
| in035 | cnw_cnn_pix3n_fsl | oracle | 2.5% | 28.29 / 0.0728 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | 不复核 | —% | 28.16 / 0.0728 | — | 29.42 | 1/3 |
| in035 | cnw_cnn_pix3n_fsl_g | oracle | 1.4% | 28.22 / 0.0718 | — | 29.42 | 2/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.80 / 0.0722 | — / — | 29.42 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 27.73 / 0.0760 | — / — | 29.35 | 0/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.95 / 0.0704 | — / — | 29.40 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 19.68 / 0.0231 | 29.42 / 0.0339 | 27.80 / 0.0722 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 6.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.68 | 0.6246 | 0.0231 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 6.85 | 0.4219 | 0.1232 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 13.77 | 0.4400 | 0.0820 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 13.77 | 0.4400 | 0.0820 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 13.92 | 0.4802 | 0.0750 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 13.87 | 0.4552 | 0.0792 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 13.87 | 0.4552 | 0.0792 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.49 | 0.6817 | 0.0199 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.00 | 0.6849 | 0.0259 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.85 | 0.6751 | 0.0247 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.47 | 0.7165 | 0.0208 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 21.30 | 0.6988 | 0.0236 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 21.03 | 0.6824 | 0.0227 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 20.50 | 0.6817 | 0.0199 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 21.03 | 0.6849 | 0.0259 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 20.87 | 0.6755 | 0.0247 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 21.50 | 0.7170 | 0.0207 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 21.32 | 0.6987 | 0.0235 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 21.05 | 0.6824 | 0.0227 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 45.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.83 | 0.7006 | 0.0432 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 5.01 | 0.4557 | 0.2991 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 15.46 | 0.3736 | 0.2257 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 15.46 | 0.3736 | 0.2257 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.77 | 0.4003 | 0.2018 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 15.73 | 0.3945 | 0.2147 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 15.73 | 0.3945 | 0.2147 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.24 | 0.7083 | 0.0416 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.55 | 0.7082 | 0.0474 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.48 | 0.7067 | 0.0457 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.86 | 0.7144 | 0.0419 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.73 | 0.7112 | 0.0443 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.60 | 0.7084 | 0.0433 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 26.86 | 0.7066 | 0.0467 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 27.10 | 0.7021 | 0.0584 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 27.21 | 0.7045 | 0.0505 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.73 | 0.7157 | 0.0441 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 27.46 | 0.7100 | 0.0497 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 27.45 | 0.7075 | 0.0445 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 58.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.42 | 0.6770 | 0.0339 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 2.87 | 0.2987 | 0.3586 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.01 | 0.2035 | 0.2347 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.01 | 0.2035 | 0.2347 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 14.26 | 0.2143 | 0.2229 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 14.25 | 0.2184 | 0.2302 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 14.25 | 0.2184 | 0.2302 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.40 | 0.6769 | 0.0340 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.42 | 0.6771 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.42 | 0.6770 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.42 | 0.6772 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.42 | 0.6771 | 0.0339 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.42 | 0.6770 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 29.35 | 0.6765 | 0.0350 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 29.39 | 0.6772 | 0.0349 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 29.38 | 0.6768 | 0.0347 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 29.44 | 0.6777 | 0.0339 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 29.42 | 0.6775 | 0.0345 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 29.42 | 0.6771 | 0.0340 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.80 | 0.6802 | 0.0722 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 3.51 | 0.3502 | 0.4803 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | 14.78 | 0.2735 | 0.3882 | 1.00 |
| gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | 14.78 | 0.2735 | 0.3882 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 15.09 | 0.2894 | 0.3622 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | 15.07 | 0.2903 | 0.3798 | 1.00 |
| gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | 15.07 | 0.2903 | 0.3798 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.95 | 0.6833 | 0.0704 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.20 | 0.6841 | 0.0756 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.16 | 0.6833 | 0.0741 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.36 | 0.6870 | 0.0704 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.29 | 0.6854 | 0.0728 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.22 | 0.6840 | 0.0718 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.73 | 0.6824 | 0.0760 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl448_pix2_al_local] | 28.02 | 0.6832 | 0.0826 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local] | 28.02 | 0.6825 | 0.0776 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 28.32 | 0.6879 | 0.0722 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local] | 28.19 | 0.6858 | 0.0775 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local] | 28.16 | 0.6838 | 0.0728 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 777 | None | classic | 0.90 | False | 247355 | 0.665 | 107.0 | 29.29 | 0.10 | 0.008 |
| in035 | gs_tokcnw_cnn_pix2_fsl448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1105406 | 0.794 | 193.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix2_fsl_g448_pix2_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1105406 | 0.794 | 193.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 821961 | 0.794 | 8.0 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 821961 | 0.794 | 8.2 | — | 0.00 | 0.000 |
| in035 | gs_tokcnw_cnn_pix3n_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 821961 | 0.794 | 8.2 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.764 | 0.021 |
| in035 | mask_ent | 0.756 | 0.021 |
| in035 | mask_grad | 0.480 | 0.021 |
| in035 | r_col | 0.676 | 0.021 |
| in035 | r_warp | 0.880 | 0.021 |

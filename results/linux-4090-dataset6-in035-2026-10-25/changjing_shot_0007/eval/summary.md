# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 41.7% | 23.78 / 0.0778 | 23.67 / 0.1580 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 43.5% | 23.78 / 0.0803 | 23.94 / 0.1310 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | 45.1% | 23.83 / 0.0834 | 23.50 / 0.1433 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 42.7% | 23.81 / 0.0785 | 24.17 / 0.1300 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 25.66 / 0.1132 | 26.75 / 0.1238 | 17.16 / 0.0511 | 30.07 / 0.0245 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 25.60 / 0.1819 | 26.78 / 0.2084 | 18.26 / 0.0556 | 30.11 / 0.0283 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.74 / 0.1576 | 26.99 / 0.1788 | 18.50 / 0.0516 | 29.91 / 0.0286 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 25.61 / 0.1600 | 26.79 / 0.1878 | 18.45 / 0.0514 | 29.73 / 0.0297 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.85 / 0.1586 | 27.00 / 0.1768 | 18.55 / 0.0520 | 30.15 / 0.0283 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 10.6%） | — | — | 25.66 / 0.1132 | 26.75 / 0.1238 | 30.07 |
| in035 | rife | 35.3% | 41.7% | 25.60 / 0.1819 | 26.78 / 0.2084 | 30.11 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 24.76 / 0.1172 | — | -0.06 / +0.0854 (core 47.9%) | — | — | — |
| in035 | 2 | 0-3 | 25.28 / 0.1154 | — | +0.23 / +0.0948 (core 47.9%) | — | — | — |
| in035 | 4 | 3-5 | 26.94 / 0.1070 | — | -0.35 / +0.0260 (core 6.7%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 25.66 / 0.1132 | 26.75 | 30.07 | — |
| in035 | rife | 不复核 | —% | 25.60 / 0.1819 | 26.78 | 30.11 | 0/3 |
| in035 | rife | oracle | 6.1% | 26.26 / 0.1211 | 27.64 | 30.07 | 0/3 |
| in035 | rife | 不复核 | —% | 25.74 / 0.1576 | 26.99 | 29.91 | 0/3 |
| in035 | rife | oracle | 6.6% | 26.46 / 0.1152 | 27.78 | 30.07 | 1/3 |
| in035 | rife | 不复核 | —% | 25.61 / 0.1600 | 26.79 | 29.73 | 0/3 |
| in035 | rife | oracle | 6.8% | 26.39 / 0.1147 | 27.72 | 30.07 | 2/3 |
| in035 | rife | 不复核 | —% | 25.85 / 0.1586 | 27.00 | 30.15 | 0/3 |
| in035 | rife | oracle | 6.4% | 26.50 / 0.1161 | 27.76 | 30.07 | 1/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 25.66 / 0.1132 | 26.75 / 0.1238 | — |
| in035 | FF | 0（前馈） | 991×661（63%） | 30.58 | 25.60 / 0.1819 | 26.78 / 0.2084 | 0/3 |
| in035 | 50 | 1.30 s | 991×661（63%） | 34.14 | 25.85 / 0.1586 | 27.00 / 0.1768 | 0/3 |
| in035 | 100 | 2.55 s | 991×661（63%） | 35.06 | 25.74 / 0.1576 | 26.99 / 0.1788 | 0/3 |
| in035 | 200 | 5.04 s | 991×661（63%） | 36.18 | 25.61 / 0.1600 | 26.79 / 0.1878 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 25.66 / 0.1132 | 26.75 / 0.1238 | 30.07 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 25.60 / 0.1819 | 26.78 / 0.2084 | 30.11 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 26.26 / 0.1211 | 27.64 / 0.1250 | 30.07 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 25.85 / 0.1586 | 27.00 / 0.1768 | 30.15 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 26.50 / 0.1161 | 27.76 / 0.1218 | 30.07 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 25.74 / 0.1576 | 26.99 / 0.1788 | 29.91 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 26.46 / 0.1152 | 27.78 / 0.1231 | 30.07 | 1/3 |
| in035 | rife | GS 测试时优化 200 步 | 直接 | 25.61 / 0.1600 | 26.79 / 0.1878 | 29.73 | 0/3 |
| in035 | rife | GS 测试时优化 200 步 | oracle | 26.39 / 0.1147 | 27.72 / 0.1248 | 30.07 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.75 / 0.1238 | 17.16 / 0.0511 | 30.07 / 0.0245 | 25.66 / 0.1132 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 55.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.75 | 0.7927 | 0.1238 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 10.79 | 0.7298 | 0.4724 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 11.11 | 0.7203 | 0.4319 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 11.37 | 0.7079 | 0.4363 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 10.95 | 0.7279 | 0.4329 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.64 | 0.8066 | 0.1250 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.78 | 0.8067 | 0.1231 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 27.72 | 0.8056 | 0.1248 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.76 | 0.8075 | 0.1218 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 26.78 | 0.8218 | 0.2084 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.99 | 0.8140 | 0.1788 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 26.79 | 0.8051 | 0.1878 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.00 | 0.8202 | 0.1768 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 10.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.16 | 0.4793 | 0.0511 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 12.02 | 0.5239 | 0.1137 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 12.75 | 0.5487 | 0.0983 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 13.27 | 0.5588 | 0.0914 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.44 | 0.5427 | 0.1033 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 18.27 | 0.5988 | 0.0553 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 18.51 | 0.6090 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 18.46 | 0.6082 | 0.0512 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 18.56 | 0.6108 | 0.0516 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 18.26 | 0.5985 | 0.0556 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 18.50 | 0.6080 | 0.0516 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 18.45 | 0.6067 | 0.0514 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 18.55 | 0.6101 | 0.0520 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 81.8%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.96 | 0.7294 | 0.0942 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.83 | 0.6502 | 0.3643 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 10.25 | 0.6488 | 0.3254 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 10.67 | 0.6410 | 0.3152 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 10.06 | 0.6559 | 0.3334 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 25.56 | 0.7422 | 0.1028 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.78 | 0.7447 | 0.0971 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 25.67 | 0.7434 | 0.0975 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.83 | 0.7456 | 0.0978 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.86 | 0.7513 | 0.1604 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.96 | 0.7470 | 0.1389 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 24.67 | 0.7375 | 0.1473 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.13 | 0.7536 | 0.1395 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 58.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 24.25 | 0.7084 | 0.0907 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 9.58 | 0.6236 | 0.3393 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.98 | 0.6255 | 0.3079 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 10.26 | 0.6176 | 0.2990 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.83 | 0.6312 | 0.3171 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.99 | 0.7267 | 0.0933 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.24 | 0.7301 | 0.0881 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 25.17 | 0.7293 | 0.0873 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.27 | 0.7308 | 0.0896 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.43 | 0.7337 | 0.1288 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.52 | 0.7301 | 0.1150 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 24.39 | 0.7232 | 0.1165 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.62 | 0.7356 | 0.1175 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 23.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 30.07 | 0.6732 | 0.0245 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 5.20 | 0.4599 | 0.1743 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 5.52 | 0.4506 | 0.1638 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 5.80 | 0.4404 | 0.1616 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 5.36 | 0.4589 | 0.1666 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 30.07 | 0.6733 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 30.07 | 0.6734 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 30.07 | 0.6736 | 0.0245 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 30.07 | 0.6733 | 0.0245 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 30.11 | 0.6802 | 0.0283 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.91 | 0.6774 | 0.0286 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 29.73 | 0.6750 | 0.0297 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 30.15 | 0.6797 | 0.0283 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 25.66 | 0.7284 | 0.1132 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 8.98 | 0.6362 | 0.4209 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 9.32 | 0.6325 | 0.3782 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 9.57 | 0.6226 | 0.3713 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 9.18 | 0.6398 | 0.3857 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.26 | 0.7404 | 0.1211 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 26.46 | 0.7424 | 0.1152 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 26.39 | 0.7418 | 0.1147 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 26.50 | 0.7430 | 0.1161 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.60 | 0.7506 | 0.1819 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 25.74 | 0.7461 | 0.1576 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 25.61 | 0.7394 | 0.1600 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 25.85 | 0.7514 | 0.1586 | 1.00 |

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
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.315 | 45.8 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.315 | 34.4 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.315 | 37.5 | 32.90 | 0.20 | 0.008 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 399182 | 0.315 | 34.7 | 32.90 | 0.20 | 0.008 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.671 | 0.052 |
| in035 | mask_ent | 0.793 | 0.052 |
| in035 | mask_grad | 0.500 | 0.052 |
| in035 | r_col | 0.630 | 0.052 |
| in035 | r_warp | 0.780 | 0.052 |

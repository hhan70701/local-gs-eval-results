# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 9.6% | 24.08 / 0.0291 | 22.72 / 0.0667 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 10.7% | 24.46 / 0.0313 | 24.89 / 0.0533 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | 11.1% | 24.48 / 0.0327 | 24.56 / 0.0574 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 10.5% | 24.44 / 0.0307 | 25.00 / 0.0550 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 27.80 / 0.0823 | 33.66 / 0.0298 | 18.96 / 0.0235 | 29.29 / 0.0446 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 27.26 / 0.1000 | 31.11 / 0.0629 | 19.40 / 0.0205 | 29.17 / 0.0483 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.80 / 0.0942 | 32.55 / 0.0511 | 20.49 / 0.0180 | 29.26 / 0.0466 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 27.76 / 0.0937 | 32.02 / 0.0592 | 20.48 / 0.0186 | 29.25 / 0.0471 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.79 / 0.0953 | 32.37 / 0.0552 | 20.40 / 0.0178 | 29.26 / 0.0467 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 4.7%） | — | — | 27.80 / 0.0823 | 33.66 / 0.0298 | 29.29 |
| in035 | rife | 5.4% | 9.6% | 27.26 / 0.1000 | 31.11 / 0.0629 | 29.17 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 26.87 / 0.0833 | — | -0.52 / +0.0212 (core 5.4%) | — | — | — |
| in035 | 2 | 0-3 | 28.08 / 0.0845 | — | -1.00 / +0.0216 (core 5.4%) | — | — | — |
| in035 | 4 | 3-5 | 28.46 / 0.0791 | — | -0.11 / +0.0103 (core 3.3%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 27.80 / 0.0823 | 33.66 | 29.29 | — |
| in035 | rife | 不复核 | —% | 27.26 / 0.1000 | 31.11 | 29.17 | 0/3 |
| in035 | rife | oracle | 1.8% | 27.85 / 0.0814 | 32.00 | 29.29 | 2/3 |
| in035 | rife | 不复核 | —% | 27.80 / 0.0942 | 32.55 | 29.26 | 0/3 |
| in035 | rife | oracle | 1.8% | 28.20 / 0.0793 | 33.23 | 29.29 | 3/3 |
| in035 | rife | 不复核 | —% | 27.76 / 0.0937 | 32.02 | 29.25 | 0/3 |
| in035 | rife | oracle | 1.9% | 28.20 / 0.0791 | 33.06 | 29.29 | 3/3 |
| in035 | rife | 不复核 | —% | 27.79 / 0.0953 | 32.37 | 29.26 | 0/3 |
| in035 | rife | oracle | 1.8% | 28.18 / 0.0793 | 33.20 | 29.29 | 3/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 27.80 / 0.0823 | 33.66 / 0.0298 | — |
| in035 | FF | 0（前馈） | 993×635（58%） | 28.33 | 27.26 / 0.1000 | 31.11 / 0.0629 | 0/3 |
| in035 | 50 | 1.18 s | 993×635（58%） | 29.83 | 27.79 / 0.0953 | 32.37 / 0.0552 | 0/3 |
| in035 | 100 | 2.30 s | 993×635（58%） | 30.29 | 27.80 / 0.0942 | 32.55 / 0.0511 | 0/3 |
| in035 | 200 | 4.55 s | 993×635（58%） | 30.73 | 27.76 / 0.0937 | 32.02 / 0.0592 | 0/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 27.80 / 0.0823 | 33.66 / 0.0298 | 29.29 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 27.26 / 0.1000 | 31.11 / 0.0629 | 29.17 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 27.85 / 0.0814 | 32.00 / 0.0355 | 29.29 | 2/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 27.79 / 0.0953 | 32.37 / 0.0552 | 29.26 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 28.18 / 0.0793 | 33.20 / 0.0334 | 29.29 | 3/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 27.80 / 0.0942 | 32.55 / 0.0511 | 29.26 | 0/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 28.20 / 0.0793 | 33.23 / 0.0331 | 29.29 | 3/3 |
| in035 | rife | GS 测试时优化 200 步 | 直接 | 27.76 / 0.0937 | 32.02 / 0.0592 | 29.25 | 0/3 |
| in035 | rife | GS 测试时优化 200 步 | oracle | 28.20 / 0.0791 | 33.06 / 0.0336 | 29.29 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 33.66 / 0.0298 | 18.96 / 0.0235 | 29.29 / 0.0446 | 27.80 / 0.0823 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 2.2%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 33.66 | 0.9063 | 0.0298 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 11.93 | 0.6799 | 0.4107 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 13.21 | 0.6842 | 0.3534 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 14.37 | 0.6618 | 0.3375 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.86 | 0.7008 | 0.3641 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 32.00 | 0.8988 | 0.0355 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 33.23 | 0.9044 | 0.0331 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 33.06 | 0.9036 | 0.0336 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 33.20 | 0.9042 | 0.0334 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 31.11 | 0.8894 | 0.0629 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 32.55 | 0.9043 | 0.0511 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 32.02 | 0.8974 | 0.0592 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 32.37 | 0.9043 | 0.0552 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 4.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 18.96 | 0.5870 | 0.0235 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 7.52 | 0.4043 | 0.1143 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 8.15 | 0.4689 | 0.1023 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 8.45 | 0.4749 | 0.0974 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 7.90 | 0.4536 | 0.1061 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 19.44 | 0.6374 | 0.0202 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 20.53 | 0.6706 | 0.0177 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 20.52 | 0.6680 | 0.0184 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 20.44 | 0.6656 | 0.0176 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 19.40 | 0.6356 | 0.0205 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 20.49 | 0.6695 | 0.0180 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 20.48 | 0.6668 | 0.0186 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 20.40 | 0.6650 | 0.0178 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 39.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.37 | 0.6930 | 0.0409 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 6.03 | 0.4801 | 0.3040 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 6.40 | 0.4967 | 0.2804 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 6.66 | 0.4887 | 0.2724 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 6.24 | 0.5019 | 0.2864 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.55 | 0.6981 | 0.0439 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.33 | 0.7051 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 27.32 | 0.7043 | 0.0404 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.29 | 0.7046 | 0.0406 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.39 | 0.6821 | 0.0623 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.30 | 0.6933 | 0.0557 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 26.09 | 0.6882 | 0.0569 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.34 | 0.6950 | 0.0562 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 43.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 26.64 | 0.6524 | 0.0480 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 4.10 | 0.3716 | 0.4456 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 4.34 | 0.3877 | 0.4261 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 4.51 | 0.3790 | 0.4205 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 4.22 | 0.3920 | 0.4316 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 26.72 | 0.6553 | 0.0475 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 27.38 | 0.6603 | 0.0449 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 27.37 | 0.6597 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 27.34 | 0.6599 | 0.0448 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 25.81 | 0.6458 | 0.0616 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 26.69 | 0.6538 | 0.0562 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 26.61 | 0.6508 | 0.0559 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 26.66 | 0.6548 | 0.0568 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 63.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.29 | 0.6481 | 0.0446 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 2.29 | 0.2635 | 0.4392 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 2.39 | 0.2661 | 0.4255 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 2.52 | 0.2600 | 0.4221 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 2.34 | 0.2692 | 0.4292 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.29 | 0.6481 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 29.29 | 0.6482 | 0.0446 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 29.29 | 0.6482 | 0.0447 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 29.17 | 0.6465 | 0.0483 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 29.26 | 0.6478 | 0.0466 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 29.25 | 0.6474 | 0.0471 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 29.26 | 0.6478 | 0.0467 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 27.80 | 0.6599 | 0.0823 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 3.15 | 0.3280 | 0.5611 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 3.30 | 0.3354 | 0.5337 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 3.44 | 0.3290 | 0.5273 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 3.23 | 0.3388 | 0.5406 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 27.85 | 0.6612 | 0.0814 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.20 | 0.6634 | 0.0793 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 28.20 | 0.6631 | 0.0791 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.18 | 0.6632 | 0.0793 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 27.26 | 0.6561 | 0.1000 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 27.80 | 0.6603 | 0.0942 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 27.76 | 0.6589 | 0.0937 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 27.79 | 0.6607 | 0.0953 | 1.00 |

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
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 306506 | 0.320 | 43.2 | 30.95 | 0.06 | 0.015 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 306506 | 0.320 | 32.2 | 30.95 | 0.06 | 0.015 |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | aligned_int | 1296 | None | classic | 2.51 | False | 306506 | 0.320 | 30.1 | 30.95 | 0.06 | 0.015 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 306506 | 0.320 | 31.0 | 30.95 | 0.06 | 0.015 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.772 | 0.018 |
| in035 | mask_ent | 0.753 | 0.018 |
| in035 | mask_grad | 0.485 | 0.018 |
| in035 | r_col | 0.698 | 0.018 |
| in035 | r_warp | 0.870 | 0.018 |

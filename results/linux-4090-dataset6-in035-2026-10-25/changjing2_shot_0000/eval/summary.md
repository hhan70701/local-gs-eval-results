# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokrife448_nat_dil_al_local | 78.9% | 20.03 / 0.1606 | 22.56 / 0.2308 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | 80.2% | 20.03 / 0.1620 | 22.47 / 0.2072 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | 81.5% | 20.05 / 0.1660 | 22.35 / 0.2033 | — | — |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | 79.5% | 20.04 / 0.1605 | 22.82 / 0.2067 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 20.11 / 0.1764 | 22.82 / 0.2384 | 14.24 / 0.1295 | 29.18 / 0.0178 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_local] | 22.49 / 0.2419 | 24.21 / 0.2201 | 16.98 / 0.0823 | 28.24 / 0.0233 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.57 / 0.2138 | 24.17 / 0.1967 | 17.18 / 0.0776 | 28.03 / 0.0221 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 22.42 / 0.2059 | 23.76 / 0.1920 | 17.14 / 0.0760 | 28.52 / 0.0204 |
| in035 | hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.78 / 0.2189 | 24.23 / 0.1961 | 17.30 / 0.0786 | 28.34 / 0.0213 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 23.9%） | — | — | 20.11 / 0.1764 | 22.82 / 0.2384 | 29.18 |
| in035 | rife | 69.5% | 78.9% | 22.49 / 0.2419 | 24.21 / 0.2201 | 28.24 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | r5 | rife | strict | rife_g | strict_g |
|---|---|---|---:|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 18.41 / 0.2296 | — | +4.48 / +0.0266 (core 77.5%) | — | — | — |
| in035 | 2 | 0-3 | 19.62 / 0.1740 | — | +1.98 / +0.0866 (core 77.5%) | — | — | — |
| in035 | 4 | 3-5 | 22.29 / 0.1254 | — | +0.69 / +0.0835 (core 42.5%) | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 20.11 / 0.1764 | 22.82 | 29.18 | — |
| in035 | rife | 不复核 | —% | 22.49 / 0.2419 | 24.21 | 28.24 | 0/3 |
| in035 | rife | oracle | 18.9% | 22.51 / 0.1526 | 24.94 | 29.12 | 2/3 |
| in035 | rife | 不复核 | —% | 22.57 / 0.2138 | 24.17 | 28.03 | 1/3 |
| in035 | rife | oracle | 19.2% | 22.69 / 0.1449 | 25.30 | 28.79 | 2/3 |
| in035 | rife | 不复核 | —% | 22.42 / 0.2059 | 23.76 | 28.52 | 1/3 |
| in035 | rife | oracle | 19.4% | 22.65 / 0.1430 | 25.34 | 29.02 | 2/3 |
| in035 | rife | 不复核 | —% | 22.78 / 0.2189 | 24.23 | 28.34 | 0/3 |
| in035 | rife | oracle | 19.1% | 22.80 / 0.1471 | 25.19 | 28.91 | 2/3 |

### 测试时优化：步数–耗时–质量（第十一轮；token 变体 rife，_al，直接贴回，不用真值）

| 设置 | 步数 | TTO 累计耗时 | 监督区域 | 输入 PSNR | fg PSNR / LPIPS | object PSNR / LPIPS | 不差目标数 |
|---|---:|---:|---|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | — | 20.11 / 0.1764 | 22.82 / 0.2384 | — |
| in035 | FF | 0（前馈） | 1008×911（86%） | 31.63 | 22.49 / 0.2419 | 24.21 / 0.2201 | 0/3 |
| in035 | 50 | 1.60 s | 1008×911（86%） | 35.71 | 22.78 / 0.2189 | 24.23 / 0.1961 | 0/3 |
| in035 | 100 | 3.16 s | 1008×911（86%） | 36.93 | 22.57 / 0.2138 | 24.17 / 0.1967 | 1/3 |
| in035 | 200 | 6.27 s | 1008×911（86%） | 38.14 | 22.42 / 0.2059 | 23.76 / 0.1920 | 1/3 |

TTO 累计耗时 = 从优化开始到该检查点的墙钟时间（GPU 同步），不含前馈编码与目标视点渲染；输入 PSNR 只在监督区域内计算，FF 行为第 1 步优化前的值。

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 20.11 / 0.1764 | 22.82 / 0.2384 | 29.18 | — |
| in035 | rife | GS 前馈颜色 | 直接 | 22.49 / 0.2419 | 24.21 / 0.2201 | 28.24 | 0/3 |
| in035 | rife | GS 前馈颜色 | oracle | 22.51 / 0.1526 | 24.94 / 0.1892 | 29.12 | 2/3 |
| in035 | rife | GS 测试时优化 50 步 | 直接 | 22.78 / 0.2189 | 24.23 / 0.1961 | 28.34 | 0/3 |
| in035 | rife | GS 测试时优化 50 步 | oracle | 22.80 / 0.1471 | 25.19 / 0.1717 | 28.91 | 2/3 |
| in035 | rife | GS 测试时优化 100 步 | 直接 | 22.57 / 0.2138 | 24.17 / 0.1967 | 28.03 | 1/3 |
| in035 | rife | GS 测试时优化 100 步 | oracle | 22.69 / 0.1449 | 25.30 / 0.1661 | 28.79 | 2/3 |
| in035 | rife | GS 测试时优化 200 步 | 直接 | 22.42 / 0.2059 | 23.76 / 0.1920 | 28.52 | 1/3 |
| in035 | rife | GS 测试时优化 200 步 | oracle | 22.65 / 0.1430 | 25.34 / 0.1553 | 29.02 | 2/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.82 / 0.2384 | 14.24 / 0.1295 | 29.18 / 0.0178 | 20.11 / 0.1764 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 2.4%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 22.82 | 0.6498 | 0.2384 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 18.76 | 0.7283 | 0.2626 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 19.80 | 0.7313 | 0.2233 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 21.08 | 0.7261 | 0.2126 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 19.29 | 0.7362 | 0.2318 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 24.94 | 0.7356 | 0.1892 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 25.30 | 0.7485 | 0.1661 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 25.34 | 0.7502 | 0.1553 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 25.19 | 0.7493 | 0.1717 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 24.21 | 0.7236 | 0.2201 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 24.17 | 0.7265 | 0.1967 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 23.76 | 0.7220 | 0.1920 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 24.23 | 0.7311 | 0.1961 | 1.00 |

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 23.9%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 14.24 | 0.3411 | 0.1295 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 13.93 | 0.5349 | 0.1057 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 14.31 | 0.5344 | 0.0968 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 14.52 | 0.5260 | 0.0939 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 14.20 | 0.5455 | 0.0996 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 16.97 | 0.5342 | 0.0825 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 17.18 | 0.5319 | 0.0777 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 17.14 | 0.5243 | 0.0760 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 17.30 | 0.5435 | 0.0787 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 16.98 | 0.5333 | 0.0823 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 17.18 | 0.5307 | 0.0776 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 17.14 | 0.5230 | 0.0760 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 17.30 | 0.5423 | 0.0786 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 101.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.04 | 0.6114 | 0.1836 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 14.41 | 0.6534 | 0.3477 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 15.10 | 0.6325 | 0.3064 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 15.86 | 0.6217 | 0.2895 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 14.74 | 0.6467 | 0.3166 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 22.33 | 0.6631 | 0.1617 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.47 | 0.6599 | 0.1544 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 22.46 | 0.6567 | 0.1525 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.58 | 0.6641 | 0.1564 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.17 | 0.6854 | 0.2563 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.11 | 0.6618 | 0.2324 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 22.06 | 0.6485 | 0.2229 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.35 | 0.6780 | 0.2347 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 68.6%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 19.48 | 0.5892 | 0.1680 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 15.83 | 0.6434 | 0.2539 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 16.08 | 0.6237 | 0.2243 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 16.43 | 0.6108 | 0.2176 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 15.96 | 0.6390 | 0.2311 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 21.79 | 0.6512 | 0.1385 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.01 | 0.6508 | 0.1310 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 21.97 | 0.6470 | 0.1293 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.13 | 0.6555 | 0.1330 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 21.74 | 0.6770 | 0.1934 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 21.88 | 0.6580 | 0.1704 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 21.74 | 0.6429 | 0.1661 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.08 | 0.6737 | 0.1743 | 1.00 |

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 3.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 29.18 | 0.7444 | 0.0178 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 13.95 | 0.4484 | 0.1688 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 13.62 | 0.4284 | 0.1849 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 15.34 | 0.4675 | 0.1805 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 12.99 | 0.4271 | 0.1861 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 29.12 | 0.7344 | 0.0181 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 28.79 | 0.7234 | 0.0212 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 29.02 | 0.7266 | 0.0200 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 28.91 | 0.7234 | 0.0204 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 28.24 | 0.7167 | 0.0233 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 28.03 | 0.7080 | 0.0221 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 28.52 | 0.7222 | 0.0204 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 28.34 | 0.7121 | 0.0213 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 20.11 | 0.6090 | 0.1764 | 1.00 |
| gs_tokrife448_nat_dil_al_local | 16.21 | 0.6498 | 0.3097 | 1.00 |
| gs_tokrife448_nat_dil_al_tto100_local | 16.46 | 0.6277 | 0.2737 | 1.00 |
| gs_tokrife448_nat_dil_al_tto200_local | 16.79 | 0.6163 | 0.2643 | 1.00 |
| gs_tokrife448_nat_dil_al_tto50_local | 16.35 | 0.6427 | 0.2816 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_local] | 22.51 | 0.6646 | 0.1526 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto100_local] | 22.69 | 0.6618 | 0.1449 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto200_local] | 22.65 | 0.6583 | 0.1430 | 1.00 |
| hyb_tokchk_oracle[gs_tokrife448_nat_dil_al_tto50_local] | 22.80 | 0.6662 | 0.1471 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_local] | 22.49 | 0.6917 | 0.2419 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto100_local] | 22.57 | 0.6693 | 0.2138 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto200_local] | 22.42 | 0.6544 | 0.2059 | 1.00 |
| hyb_token[gs_tokrife448_nat_dil_al_tto50_local] | 22.78 | 0.6851 | 0.2189 | 1.00 |

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
| in035 | gs_tokrife448_nat_dil_al_local | aligned_int | 1296 | None | classic | 2.51 | False | 441053 | 0.315 | 44.7 | 32.67 | 0.22 | 0.006 |
| in035 | gs_tokrife448_nat_dil_al_tto100_local | aligned_int | 1296 | None | classic | 2.51 | False | 441053 | 0.315 | 43.0 | 32.67 | 0.22 | 0.006 |
| in035 | gs_tokrife448_nat_dil_al_tto200_local | aligned_int | 1296 | None | classic | 2.51 | False | 441053 | 0.315 | 38.9 | 32.67 | 0.22 | 0.006 |
| in035 | gs_tokrife448_nat_dil_al_tto50_local | aligned_int | 1296 | None | classic | 2.51 | False | 441053 | 0.315 | 35.3 | 32.67 | 0.22 | 0.006 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.597 | 0.150 |
| in035 | mask_ent | 0.707 | 0.150 |
| in035 | mask_grad | 0.416 | 0.150 |
| in035 | r_col | 0.482 | 0.150 |
| in035 | r_warp | 0.742 | 0.150 |

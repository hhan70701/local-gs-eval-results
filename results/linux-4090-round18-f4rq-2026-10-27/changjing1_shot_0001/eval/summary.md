# 局部 GS 质量验证结果汇总

指标为各留出相机的平均值；PSNR/SSIM 越高越好，LPIPS 越低越好。`覆盖` = 该方法有渲染结果的像素占区域的比例（ROI 渲染只覆盖局部）。`+reg` 表示用真值做 ECC 单应配准后的 GS（诊断用上限，不是可部署的方法）。

## Token 局部 GS 贴回（主结果：输入相机标记 → 局部 GS → 虚拟视点贴回，全程不用真值）

`flow_s1.0_pose` 为纯光流；`hyb_token[v]` 直接贴回；`hyb_token_ringreg[v]` 先在贴回区外环用光流结果配准 GS 块（不用真值）再贴回。真值只用于计算指标。

### 贴回区内（同一组像素）

| 设置 | 局部变体 | 贴回区占前景 | 光流 PSNR / LPIPS | 直接贴回 PSNR / LPIPS | 环带配准 PSNR / LPIPS | 环带位移 px |
|---|---|---:|---:|---:|---:|---:|
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 93.9% | 24.57 / 0.1703 | 28.77 / 0.1686 | — | — |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 96.1% | 24.62 / 0.1731 | 27.95 / 0.1490 | — | — |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | 103.2% | 24.72 / 0.1706 | 27.61 / 0.1585 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 102.9% | 24.73 / 0.1666 | 27.65 / 0.1575 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 21.2% | 19.26 / 0.0994 | 22.07 / 0.0862 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 103.0% | 24.73 / 0.1670 | 27.26 / 0.1591 | — | — |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 102.9% | 24.73 / 0.1665 | 27.46 / 0.1585 | — | — |

### 整图与物体区（PSNR / LPIPS）

| 设置 | 方法 | fg | object | oracle_fail | rest |
|---|---|---:|---:|---:|---:|
| in035 | flow_s1.0_pose | 23.95 / 0.1893 | — / — | 17.22 / 0.1504 | 35.38 / 0.0209 |
| in035 | hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.23 / 0.1834 | — / — | 22.51 / 0.0748 | 36.87 / 0.0408 |
| in035 | hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.84 / 0.1649 | — / — | 22.05 / 0.0953 | 37.26 / 0.0171 |
| in035 | hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 27.76 / 0.1673 | — / — | 22.01 / 0.0959 | 37.20 / 0.0175 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 27.77 / 0.1660 | — / — | 22.01 / 0.0955 | 37.21 / 0.0174 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.64 / 0.1775 | — / — | 21.20 / 0.1183 | 35.33 / 0.0209 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 27.41 / 0.1637 | — / — | 21.78 / 0.0976 | 36.57 / 0.0156 |
| in035 | hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 27.62 / 0.1681 | — / — | 21.90 / 0.0980 | 36.73 / 0.0165 |

### Token 变体对比（`_al` 对齐域、光心按 t 插值 = 可部署设置）

输入 core = 输入相机上贴回核心区占前景比例（各输入相机平均）；oracle_fail 面积供对照（真值定义的光流失败区）。

| 设置 | token 变体 | 输入 core | 贴回区占前景 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR |
|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 `flow_s1.0_pose`（oracle_fail 占前景 18.1%） | — | — | 23.95 / 0.1893 | — / — | 35.38 |

### 逐目标视点（fg ΔPSNR / ΔLPIPS 相对纯光流；输入对 core = 该目标所在相机对的 token 面积，带 * 表示该对被门限关闭、等价纯光流）

| 设置 | 目标 | 相机对 | 光流 fg PSNR / LPIPS | rife | cnw_cnn | cnw_f5 | f4rq |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 1 | 0-3 | 23.55 / 0.2410 | — | — | — | — |
| in035 | 2 | 0-3 | 24.98 / 0.1832 | — | — | — | — |
| in035 | 4 | 3-5 | 23.33 / 0.1436 | — | — | — | — |

### 目标侧光流风险复核（第八轮：贴回区 = token core ∩ 目标视点光流风险区，不用真值；oracle = core ∩ 真值失败区）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流（门限关闭/贴回区为空时恰好等于光流）。

| 设置 | token 变体 | 复核 | 贴回区占前景 | fg PSNR / LPIPS | object PSNR | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| in035 | 纯光流 | — | — | 23.95 / 0.1893 | — | 35.38 | — |
| in035 | cnw_cnn_mw | 不复核 | —% | 28.23 / 0.1834 | — | 36.87 | 1/3 |
| in035 | cnw_cnn_mw | oracle | 15.6% | 27.78 / 0.1503 | — | 35.03 | 3/3 |
| in035 | cnw_cnn_pix3_fsl | 不复核 | —% | 27.84 / 0.1649 | — | 37.26 | 3/3 |
| in035 | cnw_cnn_pix3_fsl | oracle | 15.4% | 27.48 / 0.1636 | — | 35.36 | 3/3 |
| in035 | f4rq_pix3_fsl | 不复核 | —% | 27.76 / 0.1673 | — | 37.20 | 3/3 |
| in035 | f4rq_pix3_fsl | oracle | 16.2% | 27.44 / 0.1635 | — | 35.35 | 3/3 |
| in035 | f4rq_pix3bg_fsl | 不复核 | —% | 27.77 / 0.1660 | — | 37.21 | 3/3 |
| in035 | f4rq_pix3bg_fsl | oracle | 16.2% | 27.44 / 0.1629 | — | 35.36 | 3/3 |
| in035 | f4rq_pix3bg_fsl_g | 不复核 | —% | 26.64 / 0.1775 | — | 35.33 | 2/3 |
| in035 | f4rq_pix3bg_fsl_g | oracle | 10.8% | 26.75 / 0.1690 | — | 35.37 | 2/3 |
| in035 | f4rq_pix3bg_fsl_s25 | 不复核 | —% | 27.41 / 0.1637 | — | 36.57 | 3/3 |
| in035 | f4rq_pix3bg_fsl_s25 | oracle | 16.2% | 27.24 / 0.1637 | — | 35.36 | 3/3 |
| in035 | f4rq_pix3bg_fsl_s50 | 不复核 | —% | 27.62 / 0.1681 | — | 36.73 | 3/3 |
| in035 | f4rq_pix3bg_fsl_s50 | oracle | 16.2% | 27.35 / 0.1649 | — | 35.35 | 3/3 |

### 颜色来源对比（第九轮输入纹理 / 第十轮测试时优化：同一 token 贴回区；oracle = 只贴 core ∩ 真值失败区）

| 设置 | token 变体 | 颜色来源 | 贴回 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---|---:|---:|---:|---:|
| in035 | — | 纯光流 | — | 23.95 / 0.1893 | — / — | 35.38 | — |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | 直接 | 28.23 / 0.1834 | — / — | 36.87 | 1/3 |
| in035 | cnw_cnn_mw | GS 测试时优化 100 步 | oracle | 27.78 / 0.1503 | — / — | 35.03 | 3/3 |

## 其余诊断（整窗口 GS、用真值配准的上限等）

## 设置 in035

按目标位姿来源分别选出物体区 PSNR 最好的 GS 变体：。调优风险阈值（扫描 IoU 最优）：warp=0.08, col=2.0。

### 关键对比

| 方法 | object PSNR / LPIPS | oracle_fail PSNR / LPIPS | rest PSNR / LPIPS | fg PSNR / LPIPS |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | — / — | 17.22 / 0.1504 | 35.38 / 0.0209 | 23.95 / 0.1893 |

### 区域 `object`：物体级区域（真值中的魔方 + 周围 40 px，含手和遮挡带）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `oracle_fail`：光流失败区（用真值误差定义，等价于完美检测器）（平均占前景 18.1%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 17.22 | 0.5539 | 0.1504 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 23.16 | 0.7446 | 0.0680 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 22.02 | 0.6871 | 0.0949 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 22.32 | 0.6895 | 0.0915 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 22.32 | 0.6908 | 0.0910 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 22.32 | 0.6908 | 0.0910 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 22.04 | 0.6951 | 0.0946 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 22.21 | 0.6913 | 0.0936 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.51 | 0.7245 | 0.0753 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.06 | 0.6867 | 0.0951 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 22.01 | 0.6844 | 0.0959 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 22.01 | 0.6855 | 0.0954 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 21.18 | 0.6597 | 0.1187 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 21.78 | 0.6901 | 0.0976 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 21.90 | 0.6862 | 0.0980 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 22.51 | 0.7231 | 0.0748 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 22.05 | 0.6844 | 0.0953 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 22.01 | 0.6833 | 0.0959 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 22.01 | 0.6844 | 0.0955 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 21.20 | 0.6590 | 0.1183 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 21.78 | 0.6889 | 0.0976 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 21.90 | 0.6850 | 0.0980 | 1.00 |

### 区域 `risk`：自检风险区（仅用光流自身信号、配置中的固定阈值）（平均占前景 84.5%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.70 | 0.7876 | 0.1741 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 17.97 | 0.8001 | 0.2012 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 21.92 | 0.7595 | 0.2155 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 24.23 | 0.7759 | 0.1864 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 24.24 | 0.7763 | 0.1855 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 24.24 | 0.7763 | 0.1855 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 24.06 | 0.7784 | 0.1923 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 24.16 | 0.7759 | 0.1898 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.80 | 0.8260 | 0.1445 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.35 | 0.8148 | 0.1561 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 27.32 | 0.8145 | 0.1558 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 27.33 | 0.8148 | 0.1555 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.56 | 0.8071 | 0.1605 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 27.13 | 0.8158 | 0.1547 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 27.24 | 0.8149 | 0.1564 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.60 | 0.8228 | 0.1637 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 26.84 | 0.7924 | 0.1632 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 26.59 | 0.7923 | 0.1647 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 26.63 | 0.7929 | 0.1639 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 25.74 | 0.7962 | 0.1734 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 26.28 | 0.7951 | 0.1670 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 26.46 | 0.7927 | 0.1669 | 1.00 |

### 区域 `edge`：深度边缘带（视差水平梯度）（平均占前景 —%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|

### 区域 `rest`：前景中其余区域（光流应当可靠）（平均占前景 25.7%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 35.38 | 0.9085 | 0.0209 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 36.72 | 0.9326 | 0.0427 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 37.23 | 0.9077 | 0.0184 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 37.05 | 0.9056 | 0.0188 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 37.08 | 0.9055 | 0.0187 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 37.08 | 0.9055 | 0.0187 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 36.41 | 0.9095 | 0.0167 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 36.58 | 0.9059 | 0.0176 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 35.03 | 0.9079 | 0.0219 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 35.36 | 0.9086 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 35.35 | 0.9085 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 35.36 | 0.9085 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 35.37 | 0.9086 | 0.0209 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 35.36 | 0.9086 | 0.0210 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 35.35 | 0.9085 | 0.0210 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 36.87 | 0.9314 | 0.0408 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 37.26 | 0.9089 | 0.0171 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 37.20 | 0.9061 | 0.0175 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 37.21 | 0.9060 | 0.0174 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 35.33 | 0.9089 | 0.0209 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 36.57 | 0.9097 | 0.0156 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 36.73 | 0.9063 | 0.0165 | 1.00 |

### 区域 `fg`：整个前景（人+魔方）（平均占前景 100.0%）

| 方法 | PSNR | SSIM | LPIPS | 覆盖 |
|---|---:|---:|---:|---:|
| flow_s1.0_pose | 23.95 | 0.8195 | 0.1893 | 1.00 |
| gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | 27.06 | 0.8632 | 0.1881 | 1.00 |
| gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | 27.26 | 0.8250 | 0.1774 | 1.00 |
| gs_tokf4rq_pix3_fsl448_pix3_al_local | 27.91 | 0.8261 | 0.1643 | 1.00 |
| gs_tokf4rq_pix3bg_fsl448_pix3_al_local | 27.91 | 0.8264 | 0.1633 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | 27.91 | 0.8264 | 0.1633 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | 27.51 | 0.8329 | 0.1629 | 1.00 |
| gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | 27.77 | 0.8277 | 0.1655 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 27.78 | 0.8527 | 0.1503 | 1.00 |
| hyb_tokchk_oracle[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.48 | 0.8435 | 0.1636 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 27.44 | 0.8430 | 0.1635 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 27.44 | 0.8433 | 0.1629 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.75 | 0.8384 | 0.1690 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 27.24 | 0.8441 | 0.1637 | 1.00 |
| hyb_tokchk_oracle[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 27.35 | 0.8432 | 0.1649 | 1.00 |
| hyb_token[gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local] | 28.23 | 0.8617 | 0.1834 | 1.00 |
| hyb_token[gs_tokcnw_cnn_pix3_fsl448_pix3_al_local] | 27.84 | 0.8287 | 0.1649 | 1.00 |
| hyb_token[gs_tokf4rq_pix3_fsl448_pix3_al_local] | 27.76 | 0.8266 | 0.1673 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl448_pix3_al_local] | 27.77 | 0.8269 | 0.1660 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local] | 26.64 | 0.8337 | 0.1775 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local] | 27.41 | 0.8333 | 0.1637 | 1.00 |
| hyb_token[gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local] | 27.62 | 0.8282 | 0.1681 | 1.00 |

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
| in035 | gs_tokcnw_cnn_mw448_nat_dil_al_tto100_local | aligned_int | 1058 | None | classic | 1.67 | False | 196821 | 0.174 | 44.1 | 33.20 | 0.08 | 0.008 |
| in035 | gs_tokcnw_cnn_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 1993536 | 0.800 | 11.0 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2239613 | 0.800 | 1.9 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2242050 | 0.800 | 2.0 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_g448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2242050 | 0.800 | 2.0 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s25448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2242050 | 0.800 | 2.0 | — | 0.00 | 0.000 |
| in035 | gs_tokf4rq_pix3bg_fsl_s50448_pix3_al_local | aligned_int | 1920 | None | gsplat | 0.30 | False | 2242050 | 0.800 | 2.0 | — | 0.00 | 0.000 |

## 光流自身信号预测“光流失败”的 AUC（标签 = oracle_fail，0.5 = 随机）

| 设置 | 信号 | 平均 AUC | 前景失败率 |
|---|---|---:|---:|
| in035 | g_disp | 0.721 | 0.107 |
| in035 | mask_ent | 0.552 | 0.107 |
| in035 | mask_grad | 0.365 | 0.107 |
| in035 | r_col | 0.744 | 0.107 |
| in035 | r_warp | 0.799 | 0.107 |

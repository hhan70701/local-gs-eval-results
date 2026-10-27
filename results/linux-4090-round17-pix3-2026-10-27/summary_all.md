# 第十七轮汇总（每个目标视点等权；直接 = 不用真值的贴回，oracle = 只贴真值失败区，诊断用）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流。失败区按可见性拆开：两侧可见 = 两个输入视角都看得到（联合优化能约束），单侧可见 = 只有一个输入视角看得到（深度只能靠背景先验）。失败区几栏都是 oracle 贴回的结果。

## 全部场景（69 个目标视点）

| 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 | 失败区 | 失败区·两侧可见 | 失败区·单侧可见 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 纯光流 | 27.64 / 0.0696 | — | — | — | 19.54 / 0.0268 | 19.69 / 0.0295 | 18.45 / 0.0270 |
| cnw_cnn_mw (TTO 100) | 27.95 / 0.0768 | 6/69 | 28.26 / 0.0668 | 34/69 | 20.66 / 0.0212 | 20.85 / 0.0202 | 19.83 / 0.0178 |
| cnw_cnn_pix2_fsl | 27.74 / 0.0805 | 4/69 | 28.05 / 0.0716 | 8/69 | 20.36 / 0.0266 | 21.43 / 0.0183 | 18.51 / 0.0244 |
| cnw_cnn_pix2_fsl_g | 27.67 / 0.0761 | 7/69 | 27.97 / 0.0709 | 11/69 | 20.19 / 0.0272 | 20.96 / 0.0216 | 18.51 / 0.0259 |
| cnw_cnn_pix3n_fsl | 27.95 / 0.0760 | 4/69 | 28.15 / 0.0692 | 15/69 | 20.58 / 0.0244 | 21.68 / 0.0169 | 18.92 / 0.0205 |
| cnw_cnn_pix3n_fsl_g | 27.85 / 0.0719 | 9/69 | 28.05 / 0.0691 | 21/69 | 20.34 / 0.0255 | 21.12 / 0.0205 | 18.79 / 0.0228 |
| cnw_cnn_pix3_fsl | 28.05 / 0.0728 | 11/69 | 28.20 / 0.0689 | 23/69 | 20.64 / 0.0240 | 21.86 / 0.0173 | 19.14 / 0.0190 |

## 第七轮试点场景（检测 CNN 未用其训练）（9 个目标视点）

| 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 | 失败区 | 失败区·两侧可见 | 失败区·单侧可见 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 纯光流 | 24.75 / 0.1081 | — | — | — | 17.48 / 0.0682 | 17.36 / 0.0710 | 18.49 / 0.0605 |
| cnw_cnn_mw (TTO 100) | 27.07 / 0.1052 | 4/9 | 27.07 / 0.0921 | 7/9 | 20.58 / 0.0397 | 21.01 / 0.0300 | 20.84 / 0.0237 |
| cnw_cnn_pix2_fsl | 26.23 / 0.1074 | 4/9 | 26.32 / 0.0985 | 5/9 | 19.59 / 0.0491 | 20.69 / 0.0257 | 19.17 / 0.0351 |
| cnw_cnn_pix2_fsl_g | 25.91 / 0.1053 | 4/9 | 26.09 / 0.0997 | 5/9 | 19.32 / 0.0556 | 19.92 / 0.0405 | 19.05 / 0.0439 |
| cnw_cnn_pix3n_fsl | 26.16 / 0.1034 | 4/9 | 26.30 / 0.0958 | 5/9 | 19.60 / 0.0475 | 20.38 / 0.0251 | 19.43 / 0.0313 |
| cnw_cnn_pix3n_fsl_g | 25.87 / 0.1044 | 4/9 | 26.09 / 0.0981 | 4/9 | 19.34 / 0.0552 | 19.79 / 0.0400 | 19.22 / 0.0419 |
| cnw_cnn_pix3_fsl | 26.21 / 0.1016 | 5/9 | 26.18 / 0.0993 | 5/9 | 19.38 / 0.0494 | 20.38 / 0.0304 | 19.63 / 0.0304 |

# 六路数据集：局部 GS 验证汇总

token 变体 cnw_cnn_mw, cnw_cnn_pix2_fsl, cnw_cnn_pix2_fsl_g, cnw_cnn_pix3n_fsl, cnw_cnn_pix3n_fsl_g, cnw_cnn_pix3_fsl，`_al` 对齐域；PSNR / LPIPS 为各目标视点平均；不差目标数 = fg 的 PSNR 不低于且 LPIPS 不高于纯光流的目标数；贴回区 = 实际贴回面积占前景比例；oracle 只贴 core ∩ 真值失败区（诊断用）。object = 真值中最大的高饱和色块膨胀 40 px（没有彩色物体的场景为空，记为 —）。

## in035：全部场景合计（23 组场景，每个目标视点等权）

| token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| — | 纯光流 | — | — | 27.64 / 0.0696 | — | 30.55 | — |
| cnw_cnn_mw | TTO 100 步 | 直接 | 18.8% | 27.95 / 0.0768 | — | 30.38 | 6/69 |
| cnw_cnn_mw | TTO 100 步 | oracle | 3.6% | 28.26 / 0.0668 | — | 30.52 | 34/69 |
| cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 17.1% | 27.74 / 0.0805 | — | 30.30 | 4/69 |
| cnw_cnn_pix2_fsl | 前馈 FF | oracle | 3.4% | 28.05 / 0.0716 | — | 30.54 | 8/69 |
| cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 4.8% | 27.67 / 0.0761 | — | 30.28 | 7/69 |
| cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 2.4% | 27.97 / 0.0709 | — | 30.54 | 11/69 |
| cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 19.2% | 27.95 / 0.0760 | — | 30.51 | 4/69 |
| cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 3.5% | 28.15 / 0.0692 | — | 30.54 | 15/69 |
| cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 4.8% | 27.85 / 0.0719 | — | 30.46 | 9/69 |
| cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 2.4% | 28.05 / 0.0691 | — | 30.54 | 21/69 |
| cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 19.2% | 28.05 / 0.0728 | — | 30.51 | 11/69 |
| cnw_cnn_pix3_fsl | 前馈 FF | oracle | 3.5% | 28.20 / 0.0689 | — | 30.55 | 23/69 |

## in035：第七轮试点场景合计（检测 CNN 未用它们训练，cnw_cnn 只看这一张表）（3 组场景，每个目标视点等权）

| token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| — | 纯光流 | — | — | 24.75 / 0.1081 | — | 31.74 | — |
| cnw_cnn_mw | TTO 100 步 | 直接 | 38.6% | 27.07 / 0.1052 | — | 32.12 | 4/9 |
| cnw_cnn_mw | TTO 100 步 | oracle | 8.6% | 27.07 / 0.0921 | — | 31.61 | 7/9 |
| cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 37.3% | 26.23 / 0.1074 | — | 31.97 | 4/9 |
| cnw_cnn_pix2_fsl | 前馈 FF | oracle | 8.4% | 26.32 / 0.0985 | — | 31.68 | 5/9 |
| cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 10.7% | 25.91 / 0.1053 | — | 31.62 | 4/9 |
| cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 6.3% | 26.09 / 0.0997 | — | 31.68 | 5/9 |
| cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 39.1% | 26.16 / 0.1034 | — | 32.14 | 4/9 |
| cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 8.4% | 26.30 / 0.0958 | — | 31.72 | 5/9 |
| cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 10.8% | 25.87 / 0.1044 | — | 31.53 | 4/9 |
| cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 6.3% | 26.09 / 0.0981 | — | 31.72 | 4/9 |
| cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 39.1% | 26.21 / 0.1016 | — | 32.28 | 5/9 |
| cnw_cnn_pix3_fsl | 前馈 FF | oracle | 8.4% | 26.18 / 0.0993 | — | 31.72 | 5/9 |

## in035：逐场景

| 场景 | token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 | TTO 累计耗时 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| changjing/shot_0000 | — | 纯光流 | — | — | 28.76 / 0.0522 | — | 29.88 | — | — |
| changjing/shot_0000 | cnw_cnn_mw | TTO 100 步 | 直接 | 3.0% | 28.38 / 0.0541 | — | 29.81 | 0/3 | 3.12 s |
| changjing/shot_0000 | cnw_cnn_mw | TTO 100 步 | oracle | 0.5% | 28.64 / 0.0527 | — | 29.88 | 1/3 | 3.12 s |
| changjing/shot_0000 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 2.5% | 28.69 / 0.0538 | — | 29.85 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 0.4% | 28.77 / 0.0527 | — | 29.88 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 0.4% | 28.73 / 0.0530 | — | 29.87 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.2% | 28.76 / 0.0525 | — | 29.88 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 3.0% | 28.70 / 0.0538 | — | 29.85 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 0.5% | 28.79 / 0.0527 | — | 29.88 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 0.4% | 28.74 / 0.0528 | — | 29.87 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.2% | 28.77 / 0.0524 | — | 29.88 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 3.0% | 28.77 / 0.0536 | — | 29.88 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 0.5% | 28.79 / 0.0528 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | — | 纯光流 | — | — | 29.05 / 0.0551 | — | 29.88 | — | — |
| changjing/shot_0001 | cnw_cnn_mw | TTO 100 步 | 直接 | 1.6% | 28.30 / 0.0578 | — | 29.74 | 1/3 | 2.45 s |
| changjing/shot_0001 | cnw_cnn_mw | TTO 100 步 | oracle | 0.5% | 28.54 / 0.0565 | — | 29.84 | 1/3 | 2.45 s |
| changjing/shot_0001 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 1.4% | 29.07 / 0.0567 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 0.5% | 29.11 / 0.0558 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 0.5% | 29.08 / 0.0559 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.3% | 29.10 / 0.0556 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 1.4% | 29.05 / 0.0565 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 0.5% | 29.10 / 0.0555 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 0.6% | 29.07 / 0.0556 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.3% | 29.08 / 0.0555 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 1.4% | 29.16 / 0.0558 | — | 29.88 | 0/3 | — |
| changjing/shot_0001 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 0.5% | 29.16 / 0.0554 | — | 29.88 | 0/3 | — |
| changjing/shot_0003 | — | 纯光流 | — | — | 27.80 / 0.0823 | — | 29.29 | — | — |
| changjing/shot_0003 | cnw_cnn_mw | TTO 100 步 | 直接 | 9.1% | 28.05 / 0.0883 | — | 29.29 | 0/3 | 2.03 s |
| changjing/shot_0003 | cnw_cnn_mw | TTO 100 步 | oracle | 2.0% | 28.24 / 0.0800 | — | 29.29 | 3/3 | 2.03 s |
| changjing/shot_0003 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 7.1% | 28.17 / 0.0944 | — | 29.24 | 0/3 | — |
| changjing/shot_0003 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.8% | 28.34 / 0.0847 | — | 29.29 | 0/3 | — |
| changjing/shot_0003 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.5% | 28.18 / 0.0893 | — | 29.23 | 0/3 | — |
| changjing/shot_0003 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.3% | 28.31 / 0.0840 | — | 29.29 | 0/3 | — |
| changjing/shot_0003 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 8.7% | 28.42 / 0.0882 | — | 29.31 | 0/3 | — |
| changjing/shot_0003 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.8% | 28.45 / 0.0811 | — | 29.29 | 2/3 | — |
| changjing/shot_0003 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.4% | 28.36 / 0.0831 | — | 29.29 | 1/3 | — |
| changjing/shot_0003 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.2% | 28.40 / 0.0807 | — | 29.29 | 2/3 | — |
| changjing/shot_0003 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 8.6% | 28.54 / 0.0822 | — | 29.31 | 2/3 | — |
| changjing/shot_0003 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.8% | 28.54 / 0.0795 | — | 29.29 | 3/3 | — |
| changjing/shot_0005 | — | 纯光流 | — | — | 28.18 / 0.0517 | — | 29.75 | — | — |
| changjing/shot_0005 | cnw_cnn_mw | TTO 100 步 | 直接 | 4.8% | 27.48 / 0.0550 | — | 29.61 | 0/3 | 2.28 s |
| changjing/shot_0005 | cnw_cnn_mw | TTO 100 步 | oracle | 1.3% | 27.78 / 0.0524 | — | 29.74 | 0/3 | 2.28 s |
| changjing/shot_0005 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 4.1% | 28.23 / 0.0551 | — | 29.74 | 0/3 | — |
| changjing/shot_0005 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.2% | 28.29 / 0.0534 | — | 29.75 | 0/3 | — |
| changjing/shot_0005 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 0.7% | 28.24 / 0.0529 | — | 29.75 | 1/3 | — |
| changjing/shot_0005 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.4% | 28.26 / 0.0524 | — | 29.75 | 1/3 | — |
| changjing/shot_0005 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 4.5% | 28.25 / 0.0538 | — | 29.74 | 0/3 | — |
| changjing/shot_0005 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.2% | 28.32 / 0.0523 | — | 29.75 | 0/3 | — |
| changjing/shot_0005 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 0.9% | 28.25 / 0.0521 | — | 29.74 | 1/3 | — |
| changjing/shot_0005 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.5% | 28.28 / 0.0516 | — | 29.75 | 2/3 | — |
| changjing/shot_0005 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 4.5% | 28.41 / 0.0527 | — | 29.76 | 0/3 | — |
| changjing/shot_0005 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.2% | 28.43 / 0.0517 | — | 29.75 | 1/3 | — |
| changjing/shot_0007 | — | 纯光流 | — | — | 25.66 / 0.1132 | — | 30.07 | — | — |
| changjing/shot_0007 | cnw_cnn_mw | TTO 100 步 | 直接 | 47.4% | 25.99 / 0.1485 | — | 30.01 | 0/3 | 3.01 s |
| changjing/shot_0007 | cnw_cnn_mw | TTO 100 步 | oracle | 8.3% | 26.72 / 0.1123 | — | 30.07 | 2/3 | 3.01 s |
| changjing/shot_0007 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 45.0% | 26.47 / 0.1431 | — | 30.18 | 0/3 | — |
| changjing/shot_0007 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 8.4% | 27.21 / 0.1226 | — | 30.07 | 0/3 | — |
| changjing/shot_0007 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 12.1% | 26.26 / 0.1336 | — | 30.04 | 0/3 | — |
| changjing/shot_0007 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 6.4% | 27.04 / 0.1223 | — | 30.07 | 0/3 | — |
| changjing/shot_0007 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 47.5% | 27.55 / 0.1324 | — | 30.22 | 0/3 | — |
| changjing/shot_0007 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 8.4% | 27.68 / 0.1135 | — | 30.07 | 1/3 | — |
| changjing/shot_0007 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 11.3% | 27.25 / 0.1188 | — | 30.08 | 0/3 | — |
| changjing/shot_0007 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 6.2% | 27.47 / 0.1132 | — | 30.07 | 1/3 | — |
| changjing/shot_0007 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 47.6% | 27.88 / 0.1198 | — | 30.17 | 0/3 | — |
| changjing/shot_0007 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 8.4% | 27.87 / 0.1155 | — | 30.08 | 0/3 | — |
| changjing/shot_0009 | — | 纯光流 | — | — | 28.61 / 0.0671 | — | 31.02 | — | — |
| changjing/shot_0009 | cnw_cnn_mw | TTO 100 步 | 直接 | 9.8% | 27.96 / 0.0802 | — | 30.66 | 0/3 | 4.58 s |
| changjing/shot_0009 | cnw_cnn_mw | TTO 100 步 | oracle | 2.5% | 28.58 / 0.0705 | — | 31.01 | 0/3 | 4.58 s |
| changjing/shot_0009 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 8.0% | 28.70 / 0.0834 | — | 30.96 | 0/3 | — |
| changjing/shot_0009 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.3% | 28.99 / 0.0734 | — | 31.03 | 0/3 | — |
| changjing/shot_0009 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.9% | 28.75 / 0.0771 | — | 30.94 | 0/3 | — |
| changjing/shot_0009 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.6% | 28.96 / 0.0722 | — | 31.02 | 0/3 | — |
| changjing/shot_0009 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 11.1% | 29.15 / 0.0749 | — | 30.97 | 0/3 | — |
| changjing/shot_0009 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.4% | 29.26 / 0.0693 | — | 31.02 | 0/3 | — |
| changjing/shot_0009 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.8% | 29.15 / 0.0697 | — | 30.97 | 0/3 | — |
| changjing/shot_0009 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.5% | 29.20 / 0.0686 | — | 31.03 | 0/3 | — |
| changjing/shot_0009 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 11.1% | 29.20 / 0.0718 | — | 30.97 | 0/3 | — |
| changjing/shot_0009 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.4% | 29.29 / 0.0687 | — | 31.03 | 1/3 | — |
| changjing/shot_0011 | — | 纯光流 | — | — | 27.99 / 0.0657 | — | 30.12 | — | — |
| changjing/shot_0011 | cnw_cnn_mw | TTO 100 步 | 直接 | 21.9% | 28.68 / 0.0757 | — | 30.08 | 0/3 | 5.01 s |
| changjing/shot_0011 | cnw_cnn_mw | TTO 100 步 | oracle | 3.1% | 29.02 / 0.0638 | — | 30.12 | 3/3 | 5.01 s |
| changjing/shot_0011 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 19.9% | 28.38 / 0.0843 | — | 30.05 | 0/3 | — |
| changjing/shot_0011 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 3.0% | 28.80 / 0.0694 | — | 30.12 | 0/3 | — |
| changjing/shot_0011 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 3.9% | 28.52 / 0.0730 | — | 30.05 | 0/3 | — |
| changjing/shot_0011 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 2.2% | 28.80 / 0.0674 | — | 30.12 | 0/3 | — |
| changjing/shot_0011 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 23.6% | 28.76 / 0.0778 | — | 30.08 | 0/3 | — |
| changjing/shot_0011 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 3.0% | 28.90 / 0.0668 | — | 30.12 | 1/3 | — |
| changjing/shot_0011 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 3.8% | 28.79 / 0.0664 | — | 30.11 | 1/3 | — |
| changjing/shot_0011 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 2.1% | 28.87 / 0.0656 | — | 30.12 | 2/3 | — |
| changjing/shot_0011 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 23.6% | 28.78 / 0.0686 | — | 30.11 | 0/3 | — |
| changjing/shot_0011 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 3.0% | 28.82 / 0.0665 | — | 30.12 | 1/3 | — |
| changjing1/shot_0000 | — | 纯光流 | — | — | 24.96 / 0.1359 | — | 34.19 | — | — |
| changjing1/shot_0000 | cnw_cnn_mw | TTO 100 步 | 直接 | 81.7% | 27.59 / 0.1597 | — | 31.85 | 1/3 | 2.41 s |
| changjing1/shot_0000 | cnw_cnn_mw | TTO 100 步 | oracle | 13.5% | 28.03 / 0.1151 | — | 33.88 | 3/3 | 2.41 s |
| changjing1/shot_0000 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 78.1% | 25.35 / 0.2146 | — | 28.96 | 0/3 | — |
| changjing1/shot_0000 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 13.3% | 26.82 / 0.1513 | — | 34.04 | 0/3 | — |
| changjing1/shot_0000 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 21.2% | 25.13 / 0.1898 | — | 29.90 | 0/3 | — |
| changjing1/shot_0000 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 9.5% | 26.54 / 0.1458 | — | 34.06 | 0/3 | — |
| changjing1/shot_0000 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 82.1% | 26.82 / 0.1687 | — | 33.15 | 0/3 | — |
| changjing1/shot_0000 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 13.4% | 27.22 / 0.1399 | — | 34.03 | 0/3 | — |
| changjing1/shot_0000 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 18.9% | 26.47 / 0.1473 | — | 34.03 | 0/3 | — |
| changjing1/shot_0000 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 9.3% | 26.89 / 0.1364 | — | 34.04 | 1/3 | — |
| changjing1/shot_0000 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 82.2% | 27.71 / 0.1600 | — | 32.35 | 0/3 | — |
| changjing1/shot_0000 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 13.3% | 28.11 / 0.1320 | — | 33.98 | 2/3 | — |
| changjing1/shot_0001 | — | 纯光流 | — | — | 23.95 / 0.1893 | — | 35.38 | — | — |
| changjing1/shot_0001 | cnw_cnn_mw | TTO 100 步 | 直接 | 93.9% | 28.23 / 0.1834 | — | 36.87 | 1/3 | 2.57 s |
| changjing1/shot_0001 | cnw_cnn_mw | TTO 100 步 | oracle | 15.6% | 27.78 / 0.1503 | — | 35.03 | 3/3 | 2.57 s |
| changjing1/shot_0001 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 93.5% | 27.15 / 0.1896 | — | 36.26 | 1/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 15.3% | 27.13 / 0.1690 | — | 35.24 | 2/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 20.4% | 26.16 / 0.1856 | — | 35.20 | 1/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 10.3% | 26.48 / 0.1730 | — | 35.25 | 2/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 96.1% | 26.86 / 0.1782 | — | 36.80 | 2/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 15.4% | 26.93 / 0.1622 | — | 35.35 | 3/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 20.4% | 25.95 / 0.1839 | — | 34.95 | 2/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 10.2% | 26.34 / 0.1696 | — | 35.35 | 2/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 96.1% | 27.84 / 0.1649 | — | 37.26 | 3/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 15.4% | 27.48 / 0.1636 | — | 35.36 | 3/3 | — |
| changjing1/shot_0003 | — | 纯光流 | — | — | 30.70 / 0.0739 | — | 32.23 | — | — |
| changjing1/shot_0003 | cnw_cnn_mw | TTO 100 步 | 直接 | 29.5% | 31.35 / 0.1016 | — | 32.03 | 0/3 | 2.24 s |
| changjing1/shot_0003 | cnw_cnn_mw | TTO 100 步 | oracle | 2.4% | 31.66 / 0.0736 | — | 32.24 | 2/3 | 2.24 s |
| changjing1/shot_0003 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 26.7% | 31.85 / 0.0821 | — | 32.29 | 0/3 | — |
| changjing1/shot_0003 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.2% | 31.75 / 0.0736 | — | 32.24 | 1/3 | — |
| changjing1/shot_0003 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.7% | 31.28 / 0.0749 | — | 32.21 | 1/3 | — |
| changjing1/shot_0003 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.1% | 31.43 / 0.0733 | — | 32.23 | 1/3 | — |
| changjing1/shot_0003 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 27.9% | 31.93 / 0.0832 | — | 32.26 | 0/3 | — |
| changjing1/shot_0003 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.3% | 31.77 / 0.0729 | — | 32.25 | 1/3 | — |
| changjing1/shot_0003 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.9% | 31.30 / 0.0746 | — | 32.17 | 1/3 | — |
| changjing1/shot_0003 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.2% | 31.45 / 0.0728 | — | 32.23 | 1/3 | — |
| changjing1/shot_0003 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 28.0% | 32.01 / 0.0821 | — | 32.26 | 1/3 | — |
| changjing1/shot_0003 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.2% | 31.90 / 0.0731 | — | 32.25 | 2/3 | — |
| changjing1/shot_0005 | — | 纯光流 | — | — | 31.25 / 0.0654 | — | 32.59 | — | — |
| changjing1/shot_0005 | cnw_cnn_mw | TTO 100 步 | 直接 | 6.1% | 31.16 / 0.0682 | — | 32.50 | 0/3 | 1.28 s |
| changjing1/shot_0005 | cnw_cnn_mw | TTO 100 步 | oracle | 0.8% | 31.42 / 0.0640 | — | 32.59 | 2/3 | 1.28 s |
| changjing1/shot_0005 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 4.5% | 31.17 / 0.0700 | — | 32.64 | 0/3 | — |
| changjing1/shot_0005 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 0.7% | 31.42 / 0.0658 | — | 32.59 | 0/3 | — |
| changjing1/shot_0005 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 1.6% | 31.22 / 0.0673 | — | 32.60 | 1/3 | — |
| changjing1/shot_0005 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.4% | 31.39 / 0.0653 | — | 32.59 | 2/3 | — |
| changjing1/shot_0005 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 5.5% | 31.38 / 0.0675 | — | 32.67 | 0/3 | — |
| changjing1/shot_0005 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 0.8% | 31.53 / 0.0643 | — | 32.60 | 3/3 | — |
| changjing1/shot_0005 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 1.5% | 31.32 / 0.0656 | — | 32.60 | 1/3 | — |
| changjing1/shot_0005 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.4% | 31.43 / 0.0644 | — | 32.59 | 3/3 | — |
| changjing1/shot_0005 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 5.5% | 31.40 / 0.0661 | — | 32.65 | 1/3 | — |
| changjing1/shot_0005 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 0.8% | 31.51 / 0.0646 | — | 32.59 | 3/3 | — |
| changjing1/shot_0007 | — | 纯光流 | — | — | 28.35 / 0.0496 | — | 29.69 | — | — |
| changjing1/shot_0007 | cnw_cnn_mw | TTO 100 步 | 直接 | 5.9% | 28.22 / 0.0511 | — | 29.61 | 0/3 | 3.30 s |
| changjing1/shot_0007 | cnw_cnn_mw | TTO 100 步 | oracle | 1.2% | 28.43 / 0.0491 | — | 29.67 | 1/3 | 3.30 s |
| changjing1/shot_0007 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 4.7% | 27.62 / 0.0563 | — | 29.65 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.1% | 27.86 / 0.0527 | — | 29.69 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.2% | 27.67 / 0.0541 | — | 29.65 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.7% | 27.88 / 0.0518 | — | 29.69 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 6.1% | 27.61 / 0.0562 | — | 29.67 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.1% | 27.82 / 0.0527 | — | 29.69 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.5% | 27.63 / 0.0539 | — | 29.66 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.7% | 27.82 / 0.0521 | — | 29.69 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 6.1% | 27.61 / 0.0552 | — | 29.67 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.1% | 27.79 / 0.0524 | — | 29.69 | 0/3 | — |
| changjing1/shot_0009 | — | 纯光流 | — | — | 28.10 / 0.0441 | — | 30.11 | — | — |
| changjing1/shot_0009 | cnw_cnn_mw | TTO 100 步 | 直接 | 10.9% | 27.38 / 0.0485 | — | 30.03 | 0/3 | 3.33 s |
| changjing1/shot_0009 | cnw_cnn_mw | TTO 100 步 | oracle | 2.0% | 27.69 / 0.0451 | — | 30.11 | 0/3 | 3.33 s |
| changjing1/shot_0009 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 9.1% | 27.48 / 0.0531 | — | 29.98 | 0/3 | — |
| changjing1/shot_0009 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.9% | 27.93 / 0.0484 | — | 30.12 | 0/3 | — |
| changjing1/shot_0009 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 3.1% | 27.55 / 0.0493 | — | 29.96 | 0/3 | — |
| changjing1/shot_0009 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.2% | 27.94 / 0.0472 | — | 30.11 | 0/3 | — |
| changjing1/shot_0009 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 10.8% | 27.73 / 0.0502 | — | 29.91 | 0/3 | — |
| changjing1/shot_0009 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.1% | 28.05 / 0.0463 | — | 30.12 | 0/3 | — |
| changjing1/shot_0009 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.9% | 27.75 / 0.0469 | — | 29.89 | 0/3 | — |
| changjing1/shot_0009 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.2% | 28.02 / 0.0457 | — | 30.11 | 1/3 | — |
| changjing1/shot_0009 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 10.8% | 27.79 / 0.0472 | — | 29.93 | 0/3 | — |
| changjing1/shot_0009 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.1% | 28.06 / 0.0452 | — | 30.12 | 0/3 | — |
| changjing1/shot_0011 | — | 纯光流 | — | — | 28.05 / 0.0485 | — | 29.77 | — | — |
| changjing1/shot_0011 | cnw_cnn_mw | TTO 100 步 | 直接 | 13.4% | 27.64 / 0.0542 | — | 29.69 | 0/3 | 3.75 s |
| changjing1/shot_0011 | cnw_cnn_mw | TTO 100 步 | oracle | 2.8% | 28.01 / 0.0492 | — | 29.77 | 2/3 | 3.75 s |
| changjing1/shot_0011 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 11.3% | 27.25 / 0.0617 | — | 29.78 | 0/3 | — |
| changjing1/shot_0011 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.7% | 27.68 / 0.0549 | — | 29.77 | 0/3 | — |
| changjing1/shot_0011 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 4.7% | 27.29 / 0.0586 | — | 29.77 | 0/3 | — |
| changjing1/shot_0011 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 2.1% | 27.67 / 0.0543 | — | 29.77 | 0/3 | — |
| changjing1/shot_0011 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 13.7% | 27.37 / 0.0585 | — | 29.77 | 0/3 | — |
| changjing1/shot_0011 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.7% | 27.77 / 0.0529 | — | 29.77 | 0/3 | — |
| changjing1/shot_0011 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 4.7% | 27.39 / 0.0557 | — | 29.77 | 0/3 | — |
| changjing1/shot_0011 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 2.1% | 27.75 / 0.0525 | — | 29.77 | 0/3 | — |
| changjing1/shot_0011 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 13.8% | 27.59 / 0.0530 | — | 29.76 | 0/3 | — |
| changjing1/shot_0011 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.8% | 27.86 / 0.0503 | — | 29.77 | 0/3 | — |
| changjing1/shot_0013 | — | 纯光流 | — | — | 28.02 / 0.0578 | — | 29.74 | — | — |
| changjing1/shot_0013 | cnw_cnn_mw | TTO 100 步 | 直接 | 13.4% | 27.94 / 0.0668 | — | 29.60 | 0/3 | 4.94 s |
| changjing1/shot_0013 | cnw_cnn_mw | TTO 100 步 | oracle | 2.5% | 28.27 / 0.0597 | — | 29.73 | 0/3 | 4.94 s |
| changjing1/shot_0013 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 11.1% | 27.70 / 0.0673 | — | 29.60 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.4% | 28.03 / 0.0622 | — | 29.73 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 3.3% | 27.68 / 0.0638 | — | 29.59 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.5% | 27.99 / 0.0616 | — | 29.73 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 13.1% | 27.74 / 0.0669 | — | 29.63 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.4% | 28.08 / 0.0615 | — | 29.73 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 3.5% | 27.71 / 0.0627 | — | 29.61 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.6% | 28.03 / 0.0611 | — | 29.73 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 13.2% | 27.73 / 0.0629 | — | 29.63 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.4% | 28.05 / 0.0603 | — | 29.73 | 0/3 | — |
| changjing1/shot_0015 | — | 纯光流 | — | — | 28.08 / 0.0539 | — | 29.61 | — | — |
| changjing1/shot_0015 | cnw_cnn_mw | TTO 100 步 | 直接 | 6.0% | 27.95 / 0.0552 | — | 29.49 | 0/3 | 3.92 s |
| changjing1/shot_0015 | cnw_cnn_mw | TTO 100 步 | oracle | 1.0% | 28.30 / 0.0529 | — | 29.61 | 2/3 | 3.92 s |
| changjing1/shot_0015 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 5.0% | 27.61 / 0.0579 | — | 29.59 | 0/3 | — |
| changjing1/shot_0015 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 0.9% | 27.78 / 0.0551 | — | 29.61 | 0/3 | — |
| changjing1/shot_0015 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 1.9% | 27.62 / 0.0562 | — | 29.58 | 0/3 | — |
| changjing1/shot_0015 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.7% | 27.78 / 0.0548 | — | 29.61 | 0/3 | — |
| changjing1/shot_0015 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 7.1% | 27.59 / 0.0592 | — | 29.57 | 0/3 | — |
| changjing1/shot_0015 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.1% | 27.81 / 0.0548 | — | 29.61 | 0/3 | — |
| changjing1/shot_0015 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.4% | 27.59 / 0.0575 | — | 29.56 | 0/3 | — |
| changjing1/shot_0015 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.8% | 27.80 / 0.0547 | — | 29.61 | 0/3 | — |
| changjing1/shot_0015 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 7.2% | 27.54 / 0.0585 | — | 29.57 | 0/3 | — |
| changjing1/shot_0015 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.1% | 27.75 / 0.0550 | — | 29.61 | 0/3 | — |
| changjing1/shot_0017 | — | 纯光流 | — | — | 27.22 / 0.0554 | — | 29.88 | — | — |
| changjing1/shot_0017 | cnw_cnn_mw | TTO 100 步 | 直接 | 10.6% | 27.38 / 0.0579 | — | 29.57 | 0/3 | 3.29 s |
| changjing1/shot_0017 | cnw_cnn_mw | TTO 100 步 | oracle | 2.8% | 27.77 / 0.0541 | — | 29.86 | 2/3 | 3.29 s |
| changjing1/shot_0017 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 8.8% | 26.78 / 0.0629 | — | 29.57 | 0/3 | — |
| changjing1/shot_0017 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.6% | 27.19 / 0.0580 | — | 29.84 | 0/3 | — |
| changjing1/shot_0017 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 3.2% | 26.80 / 0.0610 | — | 29.59 | 0/3 | — |
| changjing1/shot_0017 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.6% | 27.14 / 0.0575 | — | 29.84 | 0/3 | — |
| changjing1/shot_0017 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 12.6% | 26.98 / 0.0613 | — | 29.58 | 0/3 | — |
| changjing1/shot_0017 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.9% | 27.34 / 0.0569 | — | 29.86 | 0/3 | — |
| changjing1/shot_0017 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 3.6% | 26.99 / 0.0589 | — | 29.64 | 0/3 | — |
| changjing1/shot_0017 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.6% | 27.28 / 0.0563 | — | 29.86 | 0/3 | — |
| changjing1/shot_0017 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 12.6% | 27.10 / 0.0591 | — | 29.69 | 0/3 | — |
| changjing1/shot_0017 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.9% | 27.40 / 0.0558 | — | 29.89 | 2/3 | — |
| changjing1/shot_0020 | — | 纯光流 | — | — | 28.20 / 0.0540 | — | 29.79 | — | — |
| changjing1/shot_0020 | cnw_cnn_mw | TTO 100 步 | 直接 | 10.0% | 27.83 / 0.0614 | — | 29.60 | 0/3 | 3.49 s |
| changjing1/shot_0020 | cnw_cnn_mw | TTO 100 步 | oracle | 1.8% | 28.19 / 0.0565 | — | 29.78 | 0/3 | 3.49 s |
| changjing1/shot_0020 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 7.8% | 27.35 / 0.0618 | — | 29.48 | 0/3 | — |
| changjing1/shot_0020 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.7% | 27.87 / 0.0575 | — | 29.78 | 0/3 | — |
| changjing1/shot_0020 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.0% | 27.37 / 0.0602 | — | 29.52 | 0/3 | — |
| changjing1/shot_0020 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.7% | 27.83 / 0.0570 | — | 29.78 | 0/3 | — |
| changjing1/shot_0020 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 10.9% | 27.47 / 0.0624 | — | 29.57 | 0/3 | — |
| changjing1/shot_0020 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.9% | 27.99 / 0.0571 | — | 29.79 | 0/3 | — |
| changjing1/shot_0020 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.1% | 27.47 / 0.0602 | — | 29.67 | 0/3 | — |
| changjing1/shot_0020 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.7% | 27.89 / 0.0569 | — | 29.79 | 0/3 | — |
| changjing1/shot_0020 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 11.0% | 27.47 / 0.0596 | — | 29.71 | 0/3 | — |
| changjing1/shot_0020 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.0% | 28.01 / 0.0557 | — | 29.82 | 0/3 | — |
| changjing1/shot_0022 | — | 纯光流 | — | — | 21.54 / 0.0828 | — | 29.95 | — | — |
| changjing1/shot_0022 | cnw_cnn_mw | TTO 100 步 | 直接 | 18.8% | 24.59 / 0.0780 | — | 29.68 | 3/3 | 3.52 s |
| changjing1/shot_0022 | cnw_cnn_mw | TTO 100 步 | oracle | 9.9% | 24.80 / 0.0732 | — | 29.94 | 3/3 | 3.52 s |
| changjing1/shot_0022 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 16.0% | 22.84 / 0.0789 | — | 29.80 | 3/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 9.4% | 23.05 / 0.0739 | — | 29.93 | 3/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 11.2% | 22.83 / 0.0771 | — | 29.79 | 3/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 8.5% | 23.04 / 0.0735 | — | 29.93 | 3/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 18.1% | 22.92 / 0.0782 | — | 29.78 | 2/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 9.5% | 23.17 / 0.0724 | — | 29.92 | 2/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 11.6% | 22.91 / 0.0765 | — | 29.76 | 2/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 8.6% | 23.16 / 0.0722 | — | 29.92 | 2/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 18.2% | 22.02 / 0.0862 | — | 29.71 | 2/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 9.5% | 22.26 / 0.0817 | — | 29.92 | 2/3 | — |
| changjing1/shot_0024 | — | 纯光流 | — | — | 27.68 / 0.0491 | — | 29.91 | — | — |
| changjing1/shot_0024 | cnw_cnn_mw | TTO 100 步 | 直接 | 8.2% | 27.35 / 0.0535 | — | 29.66 | 0/3 | 2.82 s |
| changjing1/shot_0024 | cnw_cnn_mw | TTO 100 步 | oracle | 2.1% | 27.76 / 0.0501 | — | 29.90 | 1/3 | 2.82 s |
| changjing1/shot_0024 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 6.3% | 27.14 / 0.0551 | — | 29.85 | 0/3 | — |
| changjing1/shot_0024 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.9% | 27.31 / 0.0525 | — | 29.90 | 0/3 | — |
| changjing1/shot_0024 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.6% | 27.21 / 0.0537 | — | 29.86 | 0/3 | — |
| changjing1/shot_0024 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.2% | 27.34 / 0.0520 | — | 29.90 | 0/3 | — |
| changjing1/shot_0024 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 9.3% | 27.18 / 0.0548 | — | 29.81 | 0/3 | — |
| changjing1/shot_0024 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.0% | 27.35 / 0.0512 | — | 29.90 | 0/3 | — |
| changjing1/shot_0024 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.9% | 27.25 / 0.0523 | — | 29.85 | 0/3 | — |
| changjing1/shot_0024 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.3% | 27.38 / 0.0506 | — | 29.90 | 1/3 | — |
| changjing1/shot_0024 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 9.3% | 27.09 / 0.0541 | — | 29.84 | 0/3 | — |
| changjing1/shot_0024 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.1% | 27.25 / 0.0518 | — | 29.90 | 0/3 | — |
| changjing1/shot_0026 | — | 纯光流 | — | — | 28.36 / 0.0499 | — | 30.03 | — | — |
| changjing1/shot_0026 | cnw_cnn_mw | TTO 100 步 | 直接 | 8.1% | 28.06 / 0.0547 | — | 29.88 | 0/3 | 3.67 s |
| changjing1/shot_0026 | cnw_cnn_mw | TTO 100 步 | oracle | 1.3% | 28.40 / 0.0501 | — | 30.03 | 0/3 | 3.67 s |
| changjing1/shot_0026 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 6.0% | 27.57 / 0.0571 | — | 29.78 | 0/3 | — |
| changjing1/shot_0026 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.2% | 28.07 / 0.0527 | — | 30.02 | 0/3 | — |
| changjing1/shot_0026 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.4% | 27.60 / 0.0551 | — | 29.79 | 0/3 | — |
| changjing1/shot_0026 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.9% | 28.07 / 0.0524 | — | 30.02 | 0/3 | — |
| changjing1/shot_0026 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 7.7% | 27.63 / 0.0558 | — | 29.81 | 0/3 | — |
| changjing1/shot_0026 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.2% | 28.12 / 0.0515 | — | 30.02 | 0/3 | — |
| changjing1/shot_0026 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.5% | 27.65 / 0.0532 | — | 29.81 | 0/3 | — |
| changjing1/shot_0026 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.9% | 28.10 / 0.0513 | — | 30.02 | 0/3 | — |
| changjing1/shot_0026 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 7.7% | 27.57 / 0.0541 | — | 29.80 | 0/3 | — |
| changjing1/shot_0026 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.2% | 28.08 / 0.0511 | — | 30.02 | 0/3 | — |
| changjing1/shot_0028 | — | 纯光流 | — | — | 27.80 / 0.0480 | — | 29.86 | — | — |
| changjing1/shot_0028 | cnw_cnn_mw | TTO 100 步 | 直接 | 8.8% | 27.95 / 0.0516 | — | 29.71 | 0/3 | 3.51 s |
| changjing1/shot_0028 | cnw_cnn_mw | TTO 100 步 | oracle | 1.9% | 28.19 / 0.0481 | — | 29.86 | 1/3 | 3.51 s |
| changjing1/shot_0028 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 6.8% | 27.76 / 0.0517 | — | 29.73 | 0/3 | — |
| changjing1/shot_0028 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.7% | 27.89 / 0.0498 | — | 29.84 | 0/3 | — |
| changjing1/shot_0028 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.2% | 27.77 / 0.0502 | — | 29.74 | 0/3 | — |
| changjing1/shot_0028 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.1% | 27.87 / 0.0492 | — | 29.84 | 0/3 | — |
| changjing1/shot_0028 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 10.3% | 27.90 / 0.0507 | — | 29.85 | 0/3 | — |
| changjing1/shot_0028 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.8% | 28.01 / 0.0486 | — | 29.87 | 0/3 | — |
| changjing1/shot_0028 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.7% | 27.88 / 0.0491 | — | 29.83 | 0/3 | — |
| changjing1/shot_0028 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.1% | 27.96 / 0.0483 | — | 29.86 | 1/3 | — |
| changjing1/shot_0028 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 10.3% | 27.87 / 0.0499 | — | 29.84 | 0/3 | — |
| changjing1/shot_0028 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.9% | 27.96 / 0.0486 | — | 29.87 | 0/3 | — |
| changjing1/shot_0030 | — | 纯光流 | — | — | 27.35 / 0.0570 | — | 29.98 | — | — |
| changjing1/shot_0030 | cnw_cnn_mw | TTO 100 步 | 直接 | 10.3% | 27.49 / 0.0610 | — | 29.82 | 0/3 | 5.01 s |
| changjing1/shot_0030 | cnw_cnn_mw | TTO 100 步 | oracle | 2.5% | 27.70 / 0.0576 | — | 29.94 | 2/3 | 5.01 s |
| changjing1/shot_0030 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 8.4% | 27.64 / 0.0603 | — | 29.95 | 0/3 | — |
| changjing1/shot_0030 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.3% | 27.83 / 0.0567 | — | 29.98 | 2/3 | — |
| changjing1/shot_0030 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.6% | 27.54 / 0.0583 | — | 29.94 | 0/3 | — |
| changjing1/shot_0030 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.3% | 27.70 / 0.0567 | — | 29.98 | 2/3 | — |
| changjing1/shot_0030 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 10.5% | 27.83 / 0.0598 | — | 29.94 | 0/3 | — |
| changjing1/shot_0030 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.8% | 28.01 / 0.0560 | — | 29.98 | 2/3 | — |
| changjing1/shot_0030 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.9% | 27.68 / 0.0576 | — | 29.93 | 0/3 | — |
| changjing1/shot_0030 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.4% | 27.83 / 0.0558 | — | 29.98 | 2/3 | — |
| changjing1/shot_0030 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 10.6% | 27.97 / 0.0569 | — | 29.93 | 2/3 | — |
| changjing1/shot_0030 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.8% | 28.15 / 0.0546 | — | 30.00 | 3/3 | — |

## 耗时

| 场景 | 设置 | token 变体 | 编码窗口边长 | 编码 | 监督框面积 | TTO 各检查点累计 | 各步骤墙钟时间 |
|---|---|---|---:|---:|---:|---|---|
| changjing/shot_0000 | in035 | cnw_cnn_mw | 617+468+448 | 0.53 s | 49% | 25: 0.80s, 50: 1.58s, 100: 3.12s | pixgs 5s, evaluate 28s, validate 1s |
| changjing/shot_0001 | in035 | cnw_cnn_mw | 597+448+448 | 0.53 s | 32% | 25: 0.63s, 50: 1.24s, 100: 2.45s | pixgs 5s, evaluate 27s, validate 1s |
| changjing/shot_0003 | in035 | cnw_cnn_mw | 946 | 0.17 s | 69% | 25: 0.53s, 50: 1.03s, 100: 2.03s | pixgs 6s, evaluate 33s, validate 2s |
| changjing/shot_0005 | in035 | cnw_cnn_mw | 995 | 0.17 s | 71% | 25: 0.59s, 50: 1.15s, 100: 2.28s | pixgs 6s, evaluate 29s, validate 1s |
| changjing/shot_0007 | in035 | cnw_cnn_mw | 1296 | 0.16 s | 64% | 25: 0.77s, 50: 1.53s, 100: 3.01s | pixgs 8s, evaluate 33s, validate 2s |
| changjing/shot_0009 | in035 | cnw_cnn_mw | 513+1126+448+448 | 0.69 s | 40% | 25: 1.17s, 50: 2.31s, 100: 4.58s | pixgs 6s, evaluate 33s, validate 2s |
| changjing/shot_0011 | in035 | cnw_cnn_mw | 513+1056+612+448 | 0.69 s | 49% | 25: 1.28s, 50: 2.53s, 100: 5.01s | pixgs 6s, evaluate 31s, validate 2s |
| changjing1/shot_0000 | in035 | cnw_cnn_mw | 988 | 0.17 s | 74% | 25: 0.62s, 50: 1.22s, 100: 2.41s | pixgs 7s, evaluate 23s, validate 2s |
| changjing1/shot_0001 | in035 | cnw_cnn_mw | 1058 | 0.17 s | 75% | 25: 0.65s, 50: 1.30s, 100: 2.57s | pixgs 7s, evaluate 23s, validate 2s |
| changjing1/shot_0003 | in035 | cnw_cnn_mw | 1101 | 0.18 s | 65% | 25: 0.57s, 50: 1.13s, 100: 2.24s | pixgs 6s, evaluate 26s, validate 2s |
| changjing1/shot_0005 | in035 | cnw_cnn_mw | 591 | 0.17 s | 62% | 25: 0.33s, 50: 0.65s, 100: 1.28s | pixgs 5s, evaluate 23s, validate 1s |
| changjing1/shot_0007 | in035 | cnw_cnn_mw | 448+648+468 | 0.52 s | 62% | 25: 0.84s, 50: 1.67s, 100: 3.30s | pixgs 6s, evaluate 32s, validate 2s |
| changjing1/shot_0009 | in035 | cnw_cnn_mw | 511+612+700 | 0.51 s | 54% | 25: 0.85s, 50: 1.69s, 100: 3.33s | pixgs 6s, evaluate 32s, validate 2s |
| changjing1/shot_0011 | in035 | cnw_cnn_mw | 521+855+499 | 0.52 s | 49% | 25: 0.96s, 50: 1.90s, 100: 3.75s | pixgs 6s, evaluate 32s, validate 2s |
| changjing1/shot_0013 | in035 | cnw_cnn_mw | 905+448+506+448 | 0.69 s | 39% | 25: 1.26s, 50: 2.50s, 100: 4.94s | pixgs 6s, evaluate 33s, validate 2s |
| changjing1/shot_0015 | in035 | cnw_cnn_mw | 448+676+498+448 | 0.69 s | 42% | 25: 1.00s, 50: 1.99s, 100: 3.92s | pixgs 6s, evaluate 32s, validate 2s |
| changjing1/shot_0017 | in035 | cnw_cnn_mw | 850+453 | 0.36 s | 63% | 25: 0.84s, 50: 1.66s, 100: 3.29s | pixgs 6s, evaluate 32s, validate 2s |
| changjing1/shot_0020 | in035 | cnw_cnn_mw | 956+476 | 0.35 s | 58% | 25: 0.89s, 50: 1.76s, 100: 3.49s | pixgs 6s, evaluate 32s, validate 2s |
| changjing1/shot_0022 | in035 | cnw_cnn_mw | 1064+471 | 0.33 s | 58% | 25: 0.89s, 50: 1.77s, 100: 3.52s | pixgs 6s, evaluate 32s, validate 2s |
| changjing1/shot_0024 | in035 | cnw_cnn_mw | 860+458 | 0.35 s | 54% | 25: 0.71s, 50: 1.42s, 100: 2.82s | pixgs 6s, evaluate 31s, validate 2s |
| changjing1/shot_0026 | in035 | cnw_cnn_mw | 448+893+448 | 0.50 s | 54% | 25: 0.93s, 50: 1.85s, 100: 3.67s | pixgs 6s, evaluate 32s, validate 2s |
| changjing1/shot_0028 | in035 | cnw_cnn_mw | 448+792+464 | 0.49 s | 63% | 25: 0.90s, 50: 1.77s, 100: 3.51s | pixgs 6s, evaluate 31s, validate 2s |
| changjing1/shot_0030 | in035 | cnw_cnn_mw | 735+647+456+557 | 0.66 s | 61% | 25: 1.27s, 50: 2.52s, 100: 5.01s | pixgs 6s, evaluate 33s, validate 2s |

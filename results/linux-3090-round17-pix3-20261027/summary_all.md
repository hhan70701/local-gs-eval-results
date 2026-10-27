# 第十七轮汇总（每个目标视点等权；直接 = 不用真值的贴回，oracle = 只贴真值失败区，诊断用）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流。失败区按可见性拆开：两侧可见 = 两个输入视角都看得到（联合优化能约束），单侧可见 = 只有一个输入视角看得到（深度只能靠背景先验）。失败区几栏都是 oracle 贴回的结果。

## 全部场景（69 个目标视点）

| 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 | 失败区 | 失败区·两侧可见 | 失败区·单侧可见 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 纯光流 | 27.29 / 0.0635 | — | — | — | 19.22 / 0.0216 | 19.57 / 0.0217 | 17.77 / 0.0221 |
| cnw_cnn_mw (TTO 100) | 27.29 / 0.0740 | 0/69 | 27.71 / 0.0635 | 26/69 | 20.10 / 0.0205 | 20.47 / 0.0184 | 19.22 / 0.0170 |
| cnw_cnn_pix2_fsl | 27.11 / 0.0766 | 0/69 | 27.56 / 0.0679 | 4/69 | 19.80 / 0.0254 | 20.88 / 0.0166 | 17.81 / 0.0232 |
| cnw_cnn_pix2_fsl_g | 27.10 / 0.0722 | 0/69 | 27.50 / 0.0672 | 4/69 | 19.70 / 0.0250 | 20.53 / 0.0177 | 17.84 / 0.0234 |
| cnw_cnn_pix3n_fsl | 27.41 / 0.0731 | 0/69 | 27.71 / 0.0656 | 9/69 | 20.08 / 0.0232 | 21.24 / 0.0152 | 18.18 / 0.0197 |
| cnw_cnn_pix3n_fsl_g | 27.38 / 0.0680 | 4/69 | 27.63 / 0.0652 | 10/69 | 19.92 / 0.0231 | 20.77 / 0.0167 | 18.10 / 0.0204 |
| cnw_cnn_pix3_fsl | 27.54 / 0.0687 | 5/69 | 27.76 / 0.0650 | 16/69 | 20.18 / 0.0227 | 21.46 / 0.0155 | 18.29 / 0.0185 |

## 第七轮试点场景（检测 CNN 未用其训练）（9 个目标视点）

| 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 | 失败区 | 失败区·两侧可见 | 失败区·单侧可见 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 纯光流 | 25.21 / 0.0617 | — | — | — | 17.73 / 0.0269 | 17.49 / 0.0240 | 17.80 / 0.0160 |
| cnw_cnn_mw (TTO 100) | 25.22 / 0.0712 | 0/9 | 25.53 / 0.0638 | 1/9 | 18.36 / 0.0281 | 18.31 / 0.0250 | 18.88 / 0.0139 |
| cnw_cnn_pix2_fsl | 25.12 / 0.0733 | 0/9 | 25.55 / 0.0662 | 0/9 | 18.43 / 0.0314 | 18.69 / 0.0210 | 17.50 / 0.0186 |
| cnw_cnn_pix2_fsl_g | 25.14 / 0.0699 | 0/9 | 25.52 / 0.0656 | 0/9 | 18.36 / 0.0311 | 18.55 / 0.0214 | 17.52 / 0.0183 |
| cnw_cnn_pix3n_fsl | 25.40 / 0.0706 | 0/9 | 25.68 / 0.0634 | 1/9 | 18.66 / 0.0289 | 18.87 / 0.0201 | 17.89 / 0.0155 |
| cnw_cnn_pix3n_fsl_g | 25.42 / 0.0659 | 1/9 | 25.63 / 0.0630 | 1/9 | 18.52 / 0.0289 | 18.64 / 0.0209 | 17.81 / 0.0159 |
| cnw_cnn_pix3_fsl | 25.58 / 0.0650 | 1/9 | 25.82 / 0.0615 | 2/9 | 18.92 / 0.0270 | 19.39 / 0.0190 | 17.98 / 0.0140 |

# 六路数据集：局部 GS 验证汇总

token 变体 cnw_cnn_mw, cnw_cnn_pix2_fsl, cnw_cnn_pix2_fsl_g, cnw_cnn_pix3n_fsl, cnw_cnn_pix3n_fsl_g, cnw_cnn_pix3_fsl，`_al` 对齐域；PSNR / LPIPS 为各目标视点平均；不差目标数 = fg 的 PSNR 不低于且 LPIPS 不高于纯光流的目标数；贴回区 = 实际贴回面积占前景比例；oracle 只贴 core ∩ 真值失败区（诊断用）。object = 真值中最大的高饱和色块膨胀 40 px（没有彩色物体的场景为空，记为 —）。

## in035：全部场景合计（23 组场景，每个目标视点等权）

| token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| — | 纯光流 | — | — | 27.29 / 0.0635 | — | 30.22 | — |
| cnw_cnn_mw | TTO 100 步 | 直接 | 18.1% | 27.29 / 0.0740 | — | 29.96 | 0/69 |
| cnw_cnn_mw | TTO 100 步 | oracle | 3.5% | 27.71 / 0.0635 | — | 30.20 | 26/69 |
| cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 16.0% | 27.11 / 0.0766 | — | 30.10 | 0/69 |
| cnw_cnn_pix2_fsl | 前馈 FF | oracle | 3.3% | 27.56 / 0.0679 | — | 30.22 | 4/69 |
| cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 4.4% | 27.10 / 0.0722 | — | 30.07 | 0/69 |
| cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 2.1% | 27.50 / 0.0672 | — | 30.22 | 4/69 |
| cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 18.6% | 27.41 / 0.0731 | — | 30.07 | 0/69 |
| cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 3.5% | 27.71 / 0.0656 | — | 30.21 | 9/69 |
| cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 4.3% | 27.38 / 0.0680 | — | 30.10 | 4/69 |
| cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 2.1% | 27.63 / 0.0652 | — | 30.22 | 10/69 |
| cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 18.7% | 27.54 / 0.0687 | — | 30.13 | 5/69 |
| cnw_cnn_pix3_fsl | 前馈 FF | oracle | 3.5% | 27.76 / 0.0650 | — | 30.22 | 16/69 |

## in035：第七轮试点场景合计（检测 CNN 未用它们训练，cnw_cnn 只看这一张表）（3 组场景，每个目标视点等权）

| token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| — | 纯光流 | — | — | 25.21 / 0.0617 | — | 29.70 | — |
| cnw_cnn_mw | TTO 100 步 | 直接 | 17.7% | 25.22 / 0.0712 | — | 29.44 | 0/9 |
| cnw_cnn_mw | TTO 100 步 | oracle | 5.5% | 25.53 / 0.0638 | — | 29.67 | 1/9 |
| cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 15.2% | 25.12 / 0.0733 | — | 29.54 | 0/9 |
| cnw_cnn_pix2_fsl | 前馈 FF | oracle | 5.1% | 25.55 / 0.0662 | — | 29.68 | 0/9 |
| cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 5.5% | 25.14 / 0.0699 | — | 29.58 | 0/9 |
| cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 3.1% | 25.52 / 0.0656 | — | 29.69 | 0/9 |
| cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 18.8% | 25.40 / 0.0706 | — | 29.52 | 0/9 |
| cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 6.0% | 25.68 / 0.0634 | — | 29.68 | 1/9 |
| cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 5.5% | 25.42 / 0.0659 | — | 29.58 | 1/9 |
| cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 3.3% | 25.63 / 0.0630 | — | 29.68 | 1/9 |
| cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 18.8% | 25.58 / 0.0650 | — | 29.54 | 1/9 |
| cnw_cnn_pix3_fsl | 前馈 FF | oracle | 6.0% | 25.82 / 0.0615 | — | 29.68 | 2/9 |

## in035：逐场景

| 场景 | token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 | TTO 累计耗时 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| changjing/shot_0002 | — | 纯光流 | — | — | 28.19 / 0.0732 | — | 29.20 | — | — |
| changjing/shot_0002 | cnw_cnn_mw | TTO 100 步 | 直接 | 2.2% | 28.24 / 0.0746 | — | 29.21 | 0/3 | 7.67 s |
| changjing/shot_0002 | cnw_cnn_mw | TTO 100 步 | oracle | 0.5% | 28.28 / 0.0734 | — | 29.21 | 1/3 | 7.67 s |
| changjing/shot_0002 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 1.8% | 28.29 / 0.0751 | — | 29.21 | 0/3 | — |
| changjing/shot_0002 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 0.4% | 28.30 / 0.0739 | — | 29.20 | 0/3 | — |
| changjing/shot_0002 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 0.6% | 28.28 / 0.0745 | — | 29.20 | 0/3 | — |
| changjing/shot_0002 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.3% | 28.30 / 0.0740 | — | 29.20 | 0/3 | — |
| changjing/shot_0002 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 2.1% | 28.30 / 0.0756 | — | 29.22 | 0/3 | — |
| changjing/shot_0002 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 0.4% | 28.30 / 0.0736 | — | 29.20 | 0/3 | — |
| changjing/shot_0002 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 0.6% | 28.29 / 0.0738 | — | 29.20 | 0/3 | — |
| changjing/shot_0002 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.3% | 28.30 / 0.0734 | — | 29.20 | 0/3 | — |
| changjing/shot_0002 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 2.1% | 28.36 / 0.0741 | — | 29.21 | 0/3 | — |
| changjing/shot_0002 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 0.4% | 28.36 / 0.0732 | — | 29.20 | 2/3 | — |
| changjing/shot_0004 | — | 纯光流 | — | — | 27.80 / 0.0722 | — | 29.42 | — | — |
| changjing/shot_0004 | cnw_cnn_mw | TTO 100 步 | 直接 | 10.1% | 27.73 / 0.0760 | — | 29.35 | 0/3 | 5.50 s |
| changjing/shot_0004 | cnw_cnn_mw | TTO 100 步 | oracle | 2.5% | 27.95 / 0.0704 | — | 29.40 | 3/3 | 5.50 s |
| changjing/shot_0004 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 8.4% | 28.02 / 0.0826 | — | 29.39 | 0/3 | — |
| changjing/shot_0004 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.4% | 28.20 / 0.0756 | — | 29.42 | 1/3 | — |
| changjing/shot_0004 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.4% | 28.02 / 0.0776 | — | 29.38 | 0/3 | — |
| changjing/shot_0004 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.4% | 28.16 / 0.0741 | — | 29.42 | 1/3 | — |
| changjing/shot_0004 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 9.4% | 28.19 / 0.0775 | — | 29.42 | 0/3 | — |
| changjing/shot_0004 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.5% | 28.29 / 0.0728 | — | 29.42 | 1/3 | — |
| changjing/shot_0004 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.3% | 28.16 / 0.0728 | — | 29.42 | 1/3 | — |
| changjing/shot_0004 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.4% | 28.22 / 0.0718 | — | 29.42 | 2/3 | — |
| changjing/shot_0004 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 9.5% | 28.32 / 0.0722 | — | 29.44 | 1/3 | — |
| changjing/shot_0004 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.5% | 28.36 / 0.0704 | — | 29.42 | 3/3 | — |
| changjing/shot_0006 | — | 纯光流 | — | — | 28.06 / 0.0495 | — | 29.80 | — | — |
| changjing/shot_0006 | cnw_cnn_mw | TTO 100 步 | 直接 | 3.4% | 28.00 / 0.0506 | — | 29.77 | 0/3 | 5.06 s |
| changjing/shot_0006 | cnw_cnn_mw | TTO 100 步 | oracle | 0.8% | 28.17 / 0.0495 | — | 29.80 | 2/3 | 5.06 s |
| changjing/shot_0006 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 3.0% | 28.00 / 0.0534 | — | 29.79 | 0/3 | — |
| changjing/shot_0006 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 0.8% | 28.10 / 0.0517 | — | 29.80 | 0/3 | — |
| changjing/shot_0006 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 1.2% | 28.06 / 0.0522 | — | 29.80 | 0/3 | — |
| changjing/shot_0006 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.6% | 28.12 / 0.0513 | — | 29.80 | 0/3 | — |
| changjing/shot_0006 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 3.0% | 28.10 / 0.0513 | — | 29.80 | 0/3 | — |
| changjing/shot_0006 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 0.8% | 28.16 / 0.0502 | — | 29.80 | 0/3 | — |
| changjing/shot_0006 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 1.1% | 28.14 / 0.0505 | — | 29.80 | 0/3 | — |
| changjing/shot_0006 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.6% | 28.17 / 0.0501 | — | 29.80 | 0/3 | — |
| changjing/shot_0006 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 3.0% | 28.10 / 0.0504 | — | 29.81 | 0/3 | — |
| changjing/shot_0006 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 0.8% | 28.15 / 0.0499 | — | 29.80 | 1/3 | — |
| changjing/shot_0008 | — | 纯光流 | — | — | 26.12 / 0.1075 | — | 31.07 | — | — |
| changjing/shot_0008 | cnw_cnn_mw | TTO 100 步 | 直接 | 49.2% | 26.53 / 0.1406 | — | 31.09 | 0/3 | 7.49 s |
| changjing/shot_0008 | cnw_cnn_mw | TTO 100 步 | oracle | 8.4% | 27.09 / 0.1069 | — | 31.06 | 1/3 | 7.49 s |
| changjing/shot_0008 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 46.7% | 26.86 / 0.1388 | — | 30.98 | 0/3 | — |
| changjing/shot_0008 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 8.4% | 27.64 / 0.1157 | — | 31.08 | 0/3 | — |
| changjing/shot_0008 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 11.7% | 26.67 / 0.1269 | — | 30.88 | 0/3 | — |
| changjing/shot_0008 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 6.1% | 27.48 / 0.1145 | — | 31.08 | 0/3 | — |
| changjing/shot_0008 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 49.9% | 28.01 / 0.1265 | — | 31.25 | 0/3 | — |
| changjing/shot_0008 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 8.4% | 28.18 / 0.1081 | — | 31.08 | 1/3 | — |
| changjing/shot_0008 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 10.9% | 27.73 / 0.1120 | — | 31.08 | 0/3 | — |
| changjing/shot_0008 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 6.0% | 28.00 / 0.1076 | — | 31.08 | 2/3 | — |
| changjing/shot_0008 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 50.0% | 28.56 / 0.1149 | — | 31.23 | 0/3 | — |
| changjing/shot_0008 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 8.4% | 28.57 / 0.1100 | — | 31.08 | 1/3 | — |
| changjing/shot_0010 | — | 纯光流 | — | — | 26.21 / 0.0825 | — | 29.57 | — | — |
| changjing/shot_0010 | cnw_cnn_mw | TTO 100 步 | 直接 | 36.6% | 27.07 / 0.0999 | — | 29.57 | 0/3 | 8.65 s |
| changjing/shot_0010 | cnw_cnn_mw | TTO 100 步 | oracle | 5.7% | 27.36 / 0.0789 | — | 29.56 | 2/3 | 8.65 s |
| changjing/shot_0010 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 35.4% | 24.48 / 0.1302 | — | 29.53 | 0/3 | — |
| changjing/shot_0010 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 5.5% | 26.54 / 0.1003 | — | 29.56 | 0/3 | — |
| changjing/shot_0010 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 10.5% | 24.46 / 0.1246 | — | 29.48 | 0/3 | — |
| changjing/shot_0010 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 4.5% | 26.52 / 0.0997 | — | 29.56 | 0/3 | — |
| changjing/shot_0010 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 37.0% | 26.53 / 0.1178 | — | 29.55 | 0/3 | — |
| changjing/shot_0010 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 5.5% | 27.18 / 0.0944 | — | 29.56 | 0/3 | — |
| changjing/shot_0010 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 8.3% | 26.54 / 0.1075 | — | 29.48 | 0/3 | — |
| changjing/shot_0010 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 4.3% | 27.13 / 0.0940 | — | 29.56 | 0/3 | — |
| changjing/shot_0010 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 37.0% | 27.29 / 0.0962 | — | 29.60 | 0/3 | — |
| changjing/shot_0010 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 5.5% | 27.42 / 0.0892 | — | 29.57 | 0/3 | — |
| changjing/shot_0012 | — | 纯光流 | — | — | 27.97 / 0.0729 | — | 29.89 | — | — |
| changjing/shot_0012 | cnw_cnn_mw | TTO 100 步 | 直接 | 20.8% | 28.12 / 0.0889 | — | 29.77 | 0/3 | 7.90 s |
| changjing/shot_0012 | cnw_cnn_mw | TTO 100 步 | oracle | 2.6% | 28.50 / 0.0750 | — | 29.87 | 0/3 | 7.90 s |
| changjing/shot_0012 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 18.3% | 28.70 / 0.0968 | — | 29.88 | 0/3 | — |
| changjing/shot_0012 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.4% | 28.99 / 0.0807 | — | 29.89 | 0/3 | — |
| changjing/shot_0012 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 3.5% | 28.74 / 0.0847 | — | 29.87 | 0/3 | — |
| changjing/shot_0012 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.7% | 28.92 / 0.0792 | — | 29.89 | 0/3 | — |
| changjing/shot_0012 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 21.0% | 28.95 / 0.0882 | — | 29.88 | 0/3 | — |
| changjing/shot_0012 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.5% | 29.06 / 0.0773 | — | 29.89 | 0/3 | — |
| changjing/shot_0012 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 3.4% | 28.90 / 0.0779 | — | 29.89 | 0/3 | — |
| changjing/shot_0012 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.6% | 28.97 / 0.0761 | — | 29.89 | 0/3 | — |
| changjing/shot_0012 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 21.0% | 28.92 / 0.0813 | — | 29.89 | 0/3 | — |
| changjing/shot_0012 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.5% | 28.99 / 0.0776 | — | 29.89 | 0/3 | — |
| changjing1/shot_0002 | — | 纯光流 | — | — | 26.45 / 0.1183 | — | 34.86 | — | — |
| changjing1/shot_0002 | cnw_cnn_mw | TTO 100 步 | 直接 | 70.5% | 27.93 / 0.1567 | — | 33.81 | 0/3 | 6.17 s |
| changjing1/shot_0002 | cnw_cnn_mw | TTO 100 步 | oracle | 7.9% | 29.08 / 0.1026 | — | 34.84 | 3/3 | 6.17 s |
| changjing1/shot_0002 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 67.9% | 27.38 / 0.1425 | — | 34.04 | 0/3 | — |
| changjing1/shot_0002 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 7.3% | 28.22 / 0.1173 | — | 34.87 | 1/3 | — |
| changjing1/shot_0002 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 7.9% | 26.84 / 0.1253 | — | 33.40 | 0/3 | — |
| changjing1/shot_0002 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 4.2% | 27.71 / 0.1158 | — | 34.86 | 2/3 | — |
| changjing1/shot_0002 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 71.3% | 27.52 / 0.1341 | — | 33.27 | 0/3 | — |
| changjing1/shot_0002 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 7.2% | 28.40 / 0.1101 | — | 34.86 | 3/3 | — |
| changjing1/shot_0002 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 7.8% | 26.92 / 0.1162 | — | 33.20 | 1/3 | — |
| changjing1/shot_0002 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 4.1% | 27.83 / 0.1107 | — | 34.86 | 3/3 | — |
| changjing1/shot_0002 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 71.3% | 27.80 / 0.1274 | — | 33.46 | 0/3 | — |
| changjing1/shot_0002 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 7.2% | 28.62 / 0.1162 | — | 34.86 | 2/3 | — |
| changjing1/shot_0004 | — | 纯光流 | — | — | 28.03 / 0.0931 | — | 34.57 | — | — |
| changjing1/shot_0004 | cnw_cnn_mw | TTO 100 步 | 直接 | 21.7% | 28.54 / 0.1120 | — | 34.34 | 0/3 | 4.44 s |
| changjing1/shot_0004 | cnw_cnn_mw | TTO 100 步 | oracle | 3.9% | 29.23 / 0.0925 | — | 34.55 | 1/3 | 4.44 s |
| changjing1/shot_0004 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 19.4% | 28.32 / 0.1249 | — | 34.65 | 0/3 | — |
| changjing1/shot_0004 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 3.8% | 28.88 / 0.1044 | — | 34.56 | 0/3 | — |
| changjing1/shot_0004 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 6.9% | 28.34 / 0.1204 | — | 34.54 | 0/3 | — |
| changjing1/shot_0004 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 2.9% | 28.84 / 0.1035 | — | 34.56 | 0/3 | — |
| changjing1/shot_0004 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 29.7% | 28.72 / 0.1191 | — | 34.46 | 0/3 | — |
| changjing1/shot_0004 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 4.0% | 29.02 / 0.1025 | — | 34.54 | 0/3 | — |
| changjing1/shot_0004 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 7.9% | 28.64 / 0.1101 | — | 34.52 | 0/3 | — |
| changjing1/shot_0004 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 3.0% | 28.96 / 0.1016 | — | 34.55 | 0/3 | — |
| changjing1/shot_0004 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 29.7% | 28.63 / 0.1154 | — | 34.62 | 0/3 | — |
| changjing1/shot_0004 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 4.0% | 28.94 / 0.1028 | — | 34.55 | 0/3 | — |
| changjing1/shot_0006 | — | 纯光流 | — | — | 28.61 / 0.0491 | — | 29.71 | — | — |
| changjing1/shot_0006 | cnw_cnn_mw | TTO 100 步 | 直接 | 5.0% | 28.43 / 0.0506 | — | 29.67 | 0/3 | 6.01 s |
| changjing1/shot_0006 | cnw_cnn_mw | TTO 100 步 | oracle | 1.0% | 28.62 / 0.0491 | — | 29.71 | 1/3 | 6.01 s |
| changjing1/shot_0006 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 3.8% | 27.88 / 0.0528 | — | 29.71 | 0/3 | — |
| changjing1/shot_0006 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 0.8% | 28.12 / 0.0509 | — | 29.71 | 0/3 | — |
| changjing1/shot_0006 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 1.5% | 27.90 / 0.0520 | — | 29.70 | 0/3 | — |
| changjing1/shot_0006 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.6% | 28.11 / 0.0508 | — | 29.71 | 0/3 | — |
| changjing1/shot_0006 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 4.6% | 27.96 / 0.0525 | — | 29.70 | 0/3 | — |
| changjing1/shot_0006 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 0.8% | 28.20 / 0.0506 | — | 29.71 | 0/3 | — |
| changjing1/shot_0006 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 1.5% | 27.98 / 0.0515 | — | 29.70 | 0/3 | — |
| changjing1/shot_0006 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.6% | 28.19 / 0.0506 | — | 29.71 | 0/3 | — |
| changjing1/shot_0006 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 4.7% | 27.84 / 0.0526 | — | 29.70 | 0/3 | — |
| changjing1/shot_0006 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 0.8% | 28.09 / 0.0507 | — | 29.71 | 0/3 | — |
| changjing1/shot_0008 | — | 纯光流 | — | — | 28.74 / 0.0512 | — | 29.73 | — | — |
| changjing1/shot_0008 | cnw_cnn_mw | TTO 100 步 | 直接 | 3.5% | 28.60 / 0.0524 | — | 29.71 | 0/3 | 6.81 s |
| changjing1/shot_0008 | cnw_cnn_mw | TTO 100 步 | oracle | 0.5% | 28.75 / 0.0509 | — | 29.73 | 1/3 | 6.81 s |
| changjing1/shot_0008 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 2.8% | 28.03 / 0.0540 | — | 29.72 | 0/3 | — |
| changjing1/shot_0008 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 0.5% | 28.19 / 0.0525 | — | 29.73 | 0/3 | — |
| changjing1/shot_0008 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 1.3% | 28.05 / 0.0531 | — | 29.73 | 0/3 | — |
| changjing1/shot_0008 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.3% | 28.19 / 0.0521 | — | 29.73 | 0/3 | — |
| changjing1/shot_0008 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 3.2% | 28.06 / 0.0545 | — | 29.64 | 0/3 | — |
| changjing1/shot_0008 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 0.5% | 28.28 / 0.0526 | — | 29.70 | 0/3 | — |
| changjing1/shot_0008 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 1.4% | 28.07 / 0.0533 | — | 29.64 | 0/3 | — |
| changjing1/shot_0008 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.3% | 28.27 / 0.0521 | — | 29.70 | 0/3 | — |
| changjing1/shot_0008 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 3.2% | 28.03 / 0.0545 | — | 29.68 | 0/3 | — |
| changjing1/shot_0008 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 0.5% | 28.21 / 0.0528 | — | 29.71 | 0/3 | — |
| changjing1/shot_0010 | — | 纯光流 | — | — | 28.23 / 0.0449 | — | 29.72 | — | — |
| changjing1/shot_0010 | cnw_cnn_mw | TTO 100 步 | 直接 | 7.9% | 27.22 / 0.0523 | — | 29.57 | 0/3 | 7.32 s |
| changjing1/shot_0010 | cnw_cnn_mw | TTO 100 步 | oracle | 1.4% | 27.76 / 0.0469 | — | 29.73 | 0/3 | 7.32 s |
| changjing1/shot_0010 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 6.5% | 27.76 / 0.0506 | — | 29.72 | 0/3 | — |
| changjing1/shot_0010 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.2% | 28.07 / 0.0470 | — | 29.72 | 0/3 | — |
| changjing1/shot_0010 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.4% | 27.82 / 0.0482 | — | 29.71 | 0/3 | — |
| changjing1/shot_0010 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.9% | 28.07 / 0.0466 | — | 29.72 | 0/3 | — |
| changjing1/shot_0010 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 7.8% | 27.77 / 0.0491 | — | 29.70 | 0/3 | — |
| changjing1/shot_0010 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.3% | 28.04 / 0.0460 | — | 29.73 | 0/3 | — |
| changjing1/shot_0010 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.2% | 27.80 / 0.0474 | — | 29.70 | 0/3 | — |
| changjing1/shot_0010 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.8% | 28.02 / 0.0459 | — | 29.72 | 0/3 | — |
| changjing1/shot_0010 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 7.7% | 27.85 / 0.0476 | — | 29.73 | 0/3 | — |
| changjing1/shot_0010 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.3% | 28.08 / 0.0458 | — | 29.73 | 0/3 | — |
| changjing1/shot_0012 | — | 纯光流 | — | — | 27.76 / 0.0513 | — | 29.67 | — | — |
| changjing1/shot_0012 | cnw_cnn_mw | TTO 100 步 | 直接 | 19.1% | 27.63 / 0.0632 | — | 29.26 | 0/3 | 7.76 s |
| changjing1/shot_0012 | cnw_cnn_mw | TTO 100 步 | oracle | 3.6% | 28.17 / 0.0523 | — | 29.65 | 1/3 | 7.76 s |
| changjing1/shot_0012 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 15.0% | 27.20 / 0.0684 | — | 29.62 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 3.3% | 27.68 / 0.0589 | — | 29.67 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 5.3% | 27.27 / 0.0627 | — | 29.62 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 2.4% | 27.65 / 0.0580 | — | 29.67 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 18.9% | 27.56 / 0.0639 | — | 29.57 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 3.3% | 27.96 / 0.0555 | — | 29.67 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 4.8% | 27.59 / 0.0575 | — | 29.62 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 2.3% | 27.89 / 0.0548 | — | 29.67 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 18.9% | 27.67 / 0.0583 | — | 29.69 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 3.3% | 28.02 / 0.0538 | — | 29.68 | 0/3 | — |
| changjing1/shot_0014 | — | 纯光流 | — | — | 27.69 / 0.0550 | — | 29.70 | — | — |
| changjing1/shot_0014 | cnw_cnn_mw | TTO 100 步 | 直接 | 10.6% | 28.18 / 0.0587 | — | 29.65 | 0/3 | 6.33 s |
| changjing1/shot_0014 | cnw_cnn_mw | TTO 100 步 | oracle | 2.3% | 28.38 / 0.0549 | — | 29.70 | 1/3 | 6.33 s |
| changjing1/shot_0014 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 8.2% | 27.36 / 0.0617 | — | 29.68 | 0/3 | — |
| changjing1/shot_0014 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.1% | 27.58 / 0.0585 | — | 29.71 | 0/3 | — |
| changjing1/shot_0014 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 3.2% | 27.35 / 0.0603 | — | 29.68 | 0/3 | — |
| changjing1/shot_0014 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.6% | 27.56 / 0.0584 | — | 29.71 | 0/3 | — |
| changjing1/shot_0014 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 9.6% | 27.42 / 0.0611 | — | 29.68 | 0/3 | — |
| changjing1/shot_0014 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.1% | 27.64 / 0.0577 | — | 29.71 | 0/3 | — |
| changjing1/shot_0014 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 3.1% | 27.41 / 0.0590 | — | 29.67 | 0/3 | — |
| changjing1/shot_0014 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.6% | 27.62 / 0.0574 | — | 29.71 | 0/3 | — |
| changjing1/shot_0014 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 9.7% | 27.39 / 0.0598 | — | 29.68 | 0/3 | — |
| changjing1/shot_0014 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.1% | 27.63 / 0.0571 | — | 29.71 | 0/3 | — |
| changjing1/shot_0016 | — | 纯光流 | — | — | 27.87 / 0.0511 | — | 29.48 | — | — |
| changjing1/shot_0016 | cnw_cnn_mw | TTO 100 步 | 直接 | 13.4% | 27.37 / 0.0571 | — | 29.34 | 0/3 | 6.79 s |
| changjing1/shot_0016 | cnw_cnn_mw | TTO 100 步 | oracle | 2.4% | 27.79 / 0.0506 | — | 29.48 | 2/3 | 6.79 s |
| changjing1/shot_0016 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 11.0% | 27.29 / 0.0602 | — | 29.48 | 0/3 | — |
| changjing1/shot_0016 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.3% | 27.77 / 0.0543 | — | 29.49 | 0/3 | — |
| changjing1/shot_0016 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 4.3% | 27.35 / 0.0577 | — | 29.48 | 0/3 | — |
| changjing1/shot_0016 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.7% | 27.78 / 0.0540 | — | 29.49 | 0/3 | — |
| changjing1/shot_0016 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 13.1% | 27.54 / 0.0573 | — | 29.47 | 0/3 | — |
| changjing1/shot_0016 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.4% | 27.87 / 0.0528 | — | 29.49 | 0/3 | — |
| changjing1/shot_0016 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 3.8% | 27.59 / 0.0547 | — | 29.48 | 0/3 | — |
| changjing1/shot_0016 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.7% | 27.86 / 0.0527 | — | 29.49 | 0/3 | — |
| changjing1/shot_0016 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 13.1% | 27.71 / 0.0527 | — | 29.48 | 0/3 | — |
| changjing1/shot_0016 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.4% | 27.93 / 0.0510 | — | 29.49 | 1/3 | — |
| changjing1/shot_0018 | — | 纯光流 | — | — | 27.69 / 0.0527 | — | 29.90 | — | — |
| changjing1/shot_0018 | cnw_cnn_mw | TTO 100 步 | 直接 | 7.7% | 27.29 / 0.0580 | — | 29.79 | 0/3 | 8.06 s |
| changjing1/shot_0018 | cnw_cnn_mw | TTO 100 步 | oracle | 1.6% | 27.57 / 0.0535 | — | 29.90 | 0/3 | 8.06 s |
| changjing1/shot_0018 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 6.0% | 26.92 / 0.0599 | — | 29.71 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.4% | 27.38 / 0.0565 | — | 29.89 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.2% | 26.96 / 0.0581 | — | 29.72 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.9% | 27.37 / 0.0559 | — | 29.89 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 7.2% | 27.01 / 0.0612 | — | 29.73 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.5% | 27.43 / 0.0553 | — | 29.90 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.4% | 27.00 / 0.0583 | — | 29.73 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.9% | 27.39 / 0.0552 | — | 29.89 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 7.3% | 26.96 / 0.0598 | — | 29.75 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.5% | 27.41 / 0.0551 | — | 29.90 | 0/3 | — |
| changjing1/shot_0019 | — | 纯光流 | — | — | 27.98 / 0.0463 | — | 29.75 | — | — |
| changjing1/shot_0019 | cnw_cnn_mw | TTO 100 步 | 直接 | 9.8% | 27.87 / 0.0487 | — | 29.65 | 0/3 | 7.12 s |
| changjing1/shot_0019 | cnw_cnn_mw | TTO 100 步 | oracle | 1.7% | 28.08 / 0.0460 | — | 29.75 | 2/3 | 7.12 s |
| changjing1/shot_0019 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 7.8% | 27.20 / 0.0519 | — | 29.51 | 0/3 | — |
| changjing1/shot_0019 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.5% | 27.65 / 0.0491 | — | 29.73 | 1/3 | — |
| changjing1/shot_0019 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 1.7% | 27.23 / 0.0498 | — | 29.54 | 0/3 | — |
| changjing1/shot_0019 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.7% | 27.62 / 0.0486 | — | 29.73 | 1/3 | — |
| changjing1/shot_0019 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 11.7% | 27.34 / 0.0519 | — | 29.57 | 0/3 | — |
| changjing1/shot_0019 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.8% | 27.76 / 0.0488 | — | 29.73 | 1/3 | — |
| changjing1/shot_0019 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 1.9% | 27.35 / 0.0496 | — | 29.67 | 0/3 | — |
| changjing1/shot_0019 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.7% | 27.68 / 0.0484 | — | 29.73 | 0/3 | — |
| changjing1/shot_0019 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 11.7% | 27.36 / 0.0508 | — | 29.71 | 1/3 | — |
| changjing1/shot_0019 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.8% | 27.70 / 0.0484 | — | 29.75 | 1/3 | — |
| changjing1/shot_0021 | — | 纯光流 | — | — | 22.74 / 0.0688 | — | 29.91 | — | — |
| changjing1/shot_0021 | cnw_cnn_mw | TTO 100 步 | 直接 | 12.4% | 22.63 / 0.0742 | — | 29.68 | 0/3 | 6.79 s |
| changjing1/shot_0021 | cnw_cnn_mw | TTO 100 步 | oracle | 4.8% | 22.80 / 0.0711 | — | 29.88 | 0/3 | 6.79 s |
| changjing1/shot_0021 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 9.9% | 22.57 / 0.0760 | — | 29.79 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 4.2% | 22.71 / 0.0717 | — | 29.89 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 4.0% | 22.57 / 0.0740 | — | 29.81 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 2.2% | 22.68 / 0.0714 | — | 29.90 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 15.2% | 22.71 / 0.0752 | — | 29.80 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 6.6% | 22.81 / 0.0707 | — | 29.89 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 4.7% | 22.69 / 0.0731 | — | 29.79 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 2.7% | 22.77 / 0.0708 | — | 29.89 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 15.2% | 22.67 / 0.0730 | — | 29.79 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 6.6% | 22.78 / 0.0703 | — | 29.88 | 0/3 | — |
| changjing1/shot_0023 | — | 纯光流 | — | — | 27.85 / 0.0518 | — | 29.89 | — | — |
| changjing1/shot_0023 | cnw_cnn_mw | TTO 100 步 | 直接 | 11.9% | 26.99 / 0.0606 | — | 29.10 | 0/3 | 7.41 s |
| changjing1/shot_0023 | cnw_cnn_mw | TTO 100 步 | oracle | 2.0% | 27.75 / 0.0542 | — | 29.81 | 1/3 | 7.41 s |
| changjing1/shot_0023 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 9.7% | 27.25 / 0.0578 | — | 29.69 | 0/3 | — |
| changjing1/shot_0023 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.9% | 27.57 / 0.0547 | — | 29.86 | 0/3 | — |
| changjing1/shot_0023 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.5% | 27.30 / 0.0558 | — | 29.70 | 0/3 | — |
| changjing1/shot_0023 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.1% | 27.56 / 0.0543 | — | 29.86 | 0/3 | — |
| changjing1/shot_0023 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 12.1% | 27.29 / 0.0574 | — | 29.73 | 0/3 | — |
| changjing1/shot_0023 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.0% | 27.67 / 0.0540 | — | 29.86 | 1/3 | — |
| changjing1/shot_0023 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 2.8% | 27.35 / 0.0551 | — | 29.81 | 1/3 | — |
| changjing1/shot_0023 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.1% | 27.62 / 0.0536 | — | 29.86 | 1/3 | — |
| changjing1/shot_0023 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 12.2% | 27.37 / 0.0553 | — | 29.84 | 1/3 | — |
| changjing1/shot_0023 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.0% | 27.64 / 0.0535 | — | 29.86 | 1/3 | — |
| changjing1/shot_0025 | — | 纯光流 | — | — | 27.73 / 0.0449 | — | 30.01 | — | — |
| changjing1/shot_0025 | cnw_cnn_mw | TTO 100 步 | 直接 | 11.5% | 27.44 / 0.0501 | — | 29.77 | 0/3 | 9.03 s |
| changjing1/shot_0025 | cnw_cnn_mw | TTO 100 步 | oracle | 2.4% | 27.90 / 0.0449 | — | 30.00 | 2/3 | 9.03 s |
| changjing1/shot_0025 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 9.1% | 27.27 / 0.0525 | — | 29.84 | 0/3 | — |
| changjing1/shot_0025 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 2.2% | 27.68 / 0.0476 | — | 29.98 | 0/3 | — |
| changjing1/shot_0025 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 2.9% | 27.29 / 0.0491 | — | 29.83 | 0/3 | — |
| changjing1/shot_0025 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 1.2% | 27.64 / 0.0470 | — | 29.98 | 0/3 | — |
| changjing1/shot_0025 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 12.4% | 27.48 / 0.0503 | — | 29.87 | 0/3 | — |
| changjing1/shot_0025 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 2.4% | 27.80 / 0.0463 | — | 30.00 | 0/3 | — |
| changjing1/shot_0025 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 3.2% | 27.48 / 0.0471 | — | 29.93 | 0/3 | — |
| changjing1/shot_0025 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 1.3% | 27.74 / 0.0459 | — | 30.00 | 0/3 | — |
| changjing1/shot_0025 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 12.4% | 27.51 / 0.0481 | — | 29.98 | 0/3 | — |
| changjing1/shot_0025 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.4% | 27.77 / 0.0461 | — | 30.02 | 0/3 | — |
| changjing1/shot_0027 | — | 纯光流 | — | — | 26.26 / 0.0511 | — | 30.26 | — | — |
| changjing1/shot_0027 | cnw_cnn_mw | TTO 100 步 | 直接 | 28.7% | 25.78 / 0.0732 | — | 28.87 | 0/3 | 5.61 s |
| changjing1/shot_0027 | cnw_cnn_mw | TTO 100 步 | oracle | 7.4% | 26.67 / 0.0576 | — | 30.13 | 0/3 | 5.61 s |
| changjing1/shot_0027 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 25.8% | 26.61 / 0.0621 | — | 29.76 | 0/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 7.1% | 27.17 / 0.0539 | — | 30.23 | 1/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 7.7% | 26.63 / 0.0560 | — | 29.90 | 0/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 4.3% | 27.04 / 0.0537 | — | 30.24 | 0/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 27.8% | 26.93 / 0.0595 | — | 29.80 | 0/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 7.2% | 27.34 / 0.0522 | — | 30.21 | 1/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 7.3% | 26.94 / 0.0542 | — | 30.09 | 0/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 4.2% | 27.18 / 0.0517 | — | 30.24 | 1/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 27.8% | 26.99 / 0.0567 | — | 30.01 | 0/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 7.2% | 27.32 / 0.0510 | — | 30.24 | 1/3 | — |
| changjing1/shot_0029 | — | 纯光流 | — | — | 26.36 / 0.0567 | — | 29.73 | — | — |
| changjing1/shot_0029 | cnw_cnn_mw | TTO 100 步 | 直接 | 18.2% | 26.72 / 0.0626 | — | 29.55 | 0/3 | 7.80 s |
| changjing1/shot_0029 | cnw_cnn_mw | TTO 100 步 | oracle | 5.4% | 26.99 / 0.0580 | — | 29.70 | 1/3 | 7.80 s |
| changjing1/shot_0029 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 14.6% | 26.27 / 0.0670 | — | 29.46 | 0/3 | — |
| changjing1/shot_0029 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 5.0% | 26.56 / 0.0613 | — | 29.69 | 0/3 | — |
| changjing1/shot_0029 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 5.8% | 26.35 / 0.0638 | — | 29.51 | 0/3 | — |
| changjing1/shot_0029 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 2.9% | 26.59 / 0.0604 | — | 29.70 | 0/3 | — |
| changjing1/shot_0029 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 18.5% | 26.46 / 0.0643 | — | 29.50 | 0/3 | — |
| changjing1/shot_0029 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 5.3% | 26.71 / 0.0597 | — | 29.70 | 0/3 | — |
| changjing1/shot_0029 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 5.6% | 26.55 / 0.0607 | — | 29.64 | 0/3 | — |
| changjing1/shot_0029 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 2.9% | 26.72 / 0.0586 | — | 29.72 | 0/3 | — |
| changjing1/shot_0029 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 18.6% | 26.66 / 0.0609 | — | 29.72 | 0/3 | — |
| changjing1/shot_0029 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 5.3% | 26.84 / 0.0583 | — | 29.74 | 0/3 | — |
| changjing1/shot_0031 | — | 纯光流 | — | — | 28.23 / 0.0524 | — | 30.01 | — | — |
| changjing1/shot_0031 | cnw_cnn_mw | TTO 100 步 | 直接 | 8.7% | 27.69 / 0.0588 | — | 29.67 | 0/3 | 9.50 s |
| changjing1/shot_0031 | cnw_cnn_mw | TTO 100 步 | oracle | 1.4% | 28.13 / 0.0542 | — | 29.97 | 0/3 | 9.50 s |
| changjing1/shot_0031 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 7.0% | 28.07 / 0.0581 | — | 29.96 | 0/3 | — |
| changjing1/shot_0031 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 1.3% | 28.25 / 0.0544 | — | 30.02 | 0/3 | — |
| changjing1/shot_0031 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 1.5% | 28.04 / 0.0564 | — | 30.00 | 0/3 | — |
| changjing1/shot_0031 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 0.6% | 28.16 / 0.0540 | — | 30.01 | 0/3 | — |
| changjing1/shot_0031 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 9.1% | 28.16 / 0.0574 | — | 29.91 | 0/3 | — |
| changjing1/shot_0031 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 1.6% | 28.35 / 0.0536 | — | 30.01 | 0/3 | — |
| changjing1/shot_0031 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 1.7% | 28.14 / 0.0553 | — | 29.98 | 0/3 | — |
| changjing1/shot_0031 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 0.7% | 28.25 / 0.0532 | — | 30.01 | 0/3 | — |
| changjing1/shot_0031 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 9.2% | 28.29 / 0.0553 | — | 29.99 | 1/3 | — |
| changjing1/shot_0031 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.6% | 28.42 / 0.0524 | — | 30.02 | 1/3 | — |
| changjing1/shot_0032 | — | 纯光流 | — | — | 25.19 / 0.0637 | — | 29.29 | — | — |
| changjing1/shot_0032 | cnw_cnn_mw | TTO 100 步 | 直接 | 33.0% | 25.74 / 0.0813 | — | 28.85 | 0/3 | 7.74 s |
| changjing1/shot_0032 | cnw_cnn_mw | TTO 100 步 | oracle | 10.0% | 26.23 / 0.0669 | — | 29.23 | 1/3 | 7.74 s |
| changjing1/shot_0032 | cnw_cnn_pix2_fsl | 前馈 FF | 直接 | 29.8% | 25.85 / 0.0840 | — | 29.12 | 0/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix2_fsl | 前馈 FF | oracle | 9.7% | 26.56 / 0.0703 | — | 29.26 | 0/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix2_fsl_g | 前馈 FF | 直接 | 10.4% | 25.91 / 0.0777 | — | 29.23 | 0/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix2_fsl_g | 前馈 FF | oracle | 6.3% | 26.50 / 0.0694 | — | 29.29 | 0/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix3n_fsl | 前馈 FF | 直接 | 34.0% | 26.49 / 0.0755 | — | 29.02 | 0/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix3n_fsl | 前馈 FF | oracle | 9.9% | 26.80 / 0.0642 | — | 29.24 | 1/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix3n_fsl_g | 前馈 FF | 直接 | 9.3% | 26.57 / 0.0663 | — | 29.22 | 1/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix3n_fsl_g | 前馈 FF | oracle | 6.1% | 26.72 / 0.0630 | — | 29.27 | 1/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 34.0% | 27.10 / 0.0621 | — | 29.08 | 1/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 9.9% | 27.27 / 0.0589 | — | 29.26 | 2/3 | — |

## 耗时

| 场景 | 设置 | token 变体 | 编码窗口边长 | 编码 | 监督框面积 | TTO 各检查点累计 | 各步骤墙钟时间 |
|---|---|---|---:|---:|---:|---|---|
| changjing/shot_0002 | in035 | cnw_cnn_mw | 597+448+470+536 | 1.30 s | 57% | 25: 1.95s, 50: 3.88s, 100: 7.67s | pixgs 9s, evaluate 50s, validate 2s |
| changjing/shot_0004 | in035 | cnw_cnn_mw | 777+457 | 0.66 s | 66% | 25: 1.37s, 50: 2.76s, 100: 5.50s | pixgs 9s, evaluate 43s, validate 2s |
| changjing/shot_0006 | in035 | cnw_cnn_mw | 448+628+448 | 1.01 s | 31% | 25: 1.28s, 50: 2.55s, 100: 5.06s | pixgs 8s, evaluate 43s, validate 2s |
| changjing/shot_0008 | in035 | cnw_cnn_mw | 1296 | 0.33 s | 64% | 25: 1.87s, 50: 3.77s, 100: 7.49s | pixgs 13s, evaluate 49s, validate 3s |
| changjing/shot_0010 | in035 | cnw_cnn_mw | 1144+448+448 | 0.99 s | 34% | 25: 2.16s, 50: 4.33s, 100: 8.65s | pixgs 11s, evaluate 44s, validate 2s |
| changjing/shot_0012 | in035 | cnw_cnn_mw | 1056+448 | 0.65 s | 61% | 25: 1.97s, 50: 3.95s, 100: 7.90s | pixgs 10s, evaluate 46s, validate 2s |
| changjing1/shot_0002 | in035 | cnw_cnn_mw | 1247 | 0.33 s | 65% | 25: 1.52s, 50: 3.06s, 100: 6.17s | pixgs 12s, evaluate 38s, validate 3s |
| changjing1/shot_0004 | in035 | cnw_cnn_mw | 872 | 0.33 s | 65% | 25: 1.10s, 50: 2.22s, 100: 4.44s | pixgs 9s, evaluate 34s, validate 2s |
| changjing1/shot_0006 | in035 | cnw_cnn_mw | 448+605+472 | 1.01 s | 48% | 25: 1.50s, 50: 3.02s, 100: 6.01s | pixgs 9s, evaluate 47s, validate 2s |
| changjing1/shot_0008 | in035 | cnw_cnn_mw | 579+667+464 | 0.99 s | 57% | 25: 1.68s, 50: 3.40s, 100: 6.81s | pixgs 9s, evaluate 47s, validate 2s |
| changjing1/shot_0010 | in035 | cnw_cnn_mw | 506+1245+448 | 0.99 s | 38% | 25: 1.83s, 50: 3.68s, 100: 7.32s | pixgs 9s, evaluate 48s, validate 2s |
| changjing1/shot_0012 | in035 | cnw_cnn_mw | 1206+509 | 0.67 s | 53% | 25: 1.92s, 50: 3.85s, 100: 7.76s | pixgs 10s, evaluate 48s, validate 3s |
| changjing1/shot_0014 | in035 | cnw_cnn_mw | 459+653+480 | 0.98 s | 61% | 25: 1.58s, 50: 3.17s, 100: 6.33s | pixgs 9s, evaluate 48s, validate 2s |
| changjing1/shot_0016 | in035 | cnw_cnn_mw | 448+817+490 | 0.99 s | 39% | 25: 1.68s, 50: 3.40s, 100: 6.79s | pixgs 9s, evaluate 49s, validate 3s |
| changjing1/shot_0018 | in035 | cnw_cnn_mw | 804+448+448 | 1.04 s | 55% | 25: 2.05s, 50: 4.07s, 100: 8.06s | pixgs 10s, evaluate 47s, validate 2s |
| changjing1/shot_0019 | in035 | cnw_cnn_mw | 556+685+448 | 0.97 s | 56% | 25: 1.76s, 50: 3.56s, 100: 7.12s | pixgs 9s, evaluate 46s, validate 2s |
| changjing1/shot_0021 | in035 | cnw_cnn_mw | 877+475 | 0.66 s | 54% | 25: 1.67s, 50: 3.41s, 100: 6.79s | pixgs 9s, evaluate 46s, validate 2s |
| changjing1/shot_0023 | in035 | cnw_cnn_mw | 859+448+478 | 1.01 s | 48% | 25: 1.84s, 50: 3.70s, 100: 7.41s | pixgs 10s, evaluate 47s, validate 2s |
| changjing1/shot_0025 | in035 | cnw_cnn_mw | 597+945+453 | 1.00 s | 57% | 25: 2.24s, 50: 4.50s, 100: 9.03s | pixgs 10s, evaluate 47s, validate 2s |
| changjing1/shot_0027 | in035 | cnw_cnn_mw | 1296 | 0.34 s | 61% | 25: 1.37s, 50: 2.76s, 100: 5.61s | pixgs 10s, evaluate 47s, validate 2s |
| changjing1/shot_0029 | in035 | cnw_cnn_mw | 539+838+460 | 0.98 s | 50% | 25: 1.94s, 50: 3.91s, 100: 7.80s | pixgs 10s, evaluate 47s, validate 2s |
| changjing1/shot_0031 | in035 | cnw_cnn_mw | 732+558+456+582 | 1.31 s | 60% | 25: 2.36s, 50: 4.74s, 100: 9.50s | pixgs 10s, evaluate 50s, validate 2s |
| changjing1/shot_0032 | in035 | cnw_cnn_mw | 1153+452 | 0.66 s | 53% | 25: 1.92s, 50: 3.87s, 100: 7.74s | pixgs 11s, evaluate 47s, validate 2s |

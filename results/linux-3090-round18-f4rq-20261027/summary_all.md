# 第十七轮汇总（每个目标视点等权；直接 = 不用真值的贴回，oracle = 只贴真值失败区，诊断用）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流。失败区按可见性拆开：两侧可见 = 两个输入视角都看得到（联合优化能约束），单侧可见 = 只有一个输入视角看得到（深度只能靠背景先验）。失败区几栏都是 oracle 贴回的结果。

## 全部场景（18 个目标视点）

| 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 | 失败区 | 失败区·两侧可见 | 失败区·单侧可见 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 纯光流 | 25.96 / 0.0659 | — | — | — | 18.18 / 0.0279 | 18.60 / 0.0304 | 17.80 / 0.0275 |
| cnw_cnn_mw (TTO 100) | 25.94 / 0.0818 | 0/18 | 26.42 / 0.0681 | 3/18 | 19.07 / 0.0282 | 19.78 / 0.0265 | 18.72 / 0.0223 |
| cnw_cnn_pix3_fsl | 26.66 / 0.0708 | 1/18 | 26.89 / 0.0665 | 4/18 | 19.83 / 0.0283 | 21.11 / 0.0191 | 19.22 / 0.0209 |
| f4rq_pix3_fsl | 26.34 / 0.0768 | 1/18 | 26.86 / 0.0678 | 6/18 | 19.76 / 0.0297 | 21.20 / 0.0191 | 18.62 / 0.0218 |
| f4rq_pix3bg_fsl | 26.32 / 0.0775 | 1/18 | 26.85 / 0.0678 | 6/18 | 19.75 / 0.0297 | 21.19 / 0.0191 | 18.61 / 0.0218 |
| f4rq_pix3bg_fsl_g | 26.18 / 0.0739 | 1/18 | 26.66 / 0.0680 | 5/18 | 19.38 / 0.0302 | 20.38 / 0.0216 | 18.43 / 0.0230 |
| f4rq_pix3bg_fsl_s25 | 26.34 / 0.0793 | 0/18 | 26.88 / 0.0677 | 5/18 | 19.80 / 0.0296 | 21.37 / 0.0189 | 18.51 / 0.0224 |
| f4rq_pix3bg_fsl_s50 | 26.32 / 0.0782 | 1/18 | 26.86 / 0.0676 | 6/18 | 19.76 / 0.0296 | 21.27 / 0.0189 | 18.55 / 0.0220 |

## 第七轮试点场景（检测 CNN 未用其训练）（9 个目标视点）

| 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 | 失败区 | 失败区·两侧可见 | 失败区·单侧可见 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 纯光流 | 25.21 / 0.0617 | — | — | — | 17.73 / 0.0269 | 17.69 / 0.0255 | 17.94 / 0.0194 |
| cnw_cnn_mw (TTO 100) | 25.22 / 0.0712 | 0/9 | 25.53 / 0.0638 | 1/9 | 18.36 / 0.0281 | 18.49 / 0.0256 | 18.85 / 0.0168 |
| cnw_cnn_pix3_fsl | 25.58 / 0.0650 | 1/9 | 25.82 / 0.0615 | 2/9 | 18.92 / 0.0270 | 19.72 / 0.0193 | 19.03 / 0.0160 |
| f4rq_pix3_fsl | 25.39 / 0.0716 | 1/9 | 25.93 / 0.0625 | 4/9 | 19.11 / 0.0282 | 20.17 / 0.0195 | 18.23 / 0.0176 |
| f4rq_pix3bg_fsl | 25.36 / 0.0728 | 1/9 | 25.93 / 0.0624 | 4/9 | 19.11 / 0.0283 | 20.17 / 0.0196 | 18.23 / 0.0176 |
| f4rq_pix3bg_fsl_g | 25.25 / 0.0706 | 1/9 | 25.75 / 0.0632 | 2/9 | 18.74 / 0.0294 | 19.38 / 0.0214 | 18.07 / 0.0184 |
| f4rq_pix3bg_fsl_s25 | 25.38 / 0.0755 | 0/9 | 25.94 / 0.0630 | 3/9 | 19.13 / 0.0287 | 20.25 / 0.0198 | 18.11 / 0.0182 |
| f4rq_pix3bg_fsl_s50 | 25.37 / 0.0740 | 1/9 | 25.93 / 0.0626 | 4/9 | 19.12 / 0.0284 | 20.21 / 0.0197 | 18.16 / 0.0178 |

# 六路数据集：局部 GS 验证汇总

token 变体 cnw_cnn_mw, cnw_cnn_pix3_fsl, f4rq_pix3_fsl, f4rq_pix3bg_fsl, f4rq_pix3bg_fsl_g, f4rq_pix3bg_fsl_s25, f4rq_pix3bg_fsl_s50，`_al` 对齐域；PSNR / LPIPS 为各目标视点平均；不差目标数 = fg 的 PSNR 不低于且 LPIPS 不高于纯光流的目标数；贴回区 = 实际贴回面积占前景比例；oracle 只贴 core ∩ 真值失败区（诊断用）。object = 真值中最大的高饱和色块膨胀 40 px（没有彩色物体的场景为空，记为 —）。

## in035：全部场景合计（6 组场景，每个目标视点等权）

| token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| — | 纯光流 | — | — | 25.96 / 0.0659 | — | 30.02 | — |
| cnw_cnn_mw | TTO 100 步 | 直接 | 25.0% | 25.94 / 0.0818 | — | 29.59 | 0/18 |
| cnw_cnn_mw | TTO 100 步 | oracle | 6.0% | 26.42 / 0.0681 | — | 29.97 | 3/18 |
| cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 25.5% | 26.66 / 0.0708 | — | 29.92 | 1/18 |
| cnw_cnn_pix3_fsl | 前馈 FF | oracle | 6.2% | 26.89 / 0.0665 | — | 30.01 | 4/18 |
| f4rq_pix3_fsl | 前馈 FF | 直接 | 38.6% | 26.34 / 0.0768 | — | 29.43 | 1/18 |
| f4rq_pix3_fsl | 前馈 FF | oracle | 7.6% | 26.86 / 0.0678 | — | 29.97 | 6/18 |
| f4rq_pix3bg_fsl | 前馈 FF | 直接 | 38.8% | 26.32 / 0.0775 | — | 29.37 | 1/18 |
| f4rq_pix3bg_fsl | 前馈 FF | oracle | 7.6% | 26.85 / 0.0678 | — | 29.97 | 6/18 |
| f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 9.9% | 26.18 / 0.0739 | — | 29.40 | 1/18 |
| f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 4.6% | 26.66 / 0.0680 | — | 29.96 | 5/18 |
| f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 38.8% | 26.34 / 0.0793 | — | 29.40 | 0/18 |
| f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 7.6% | 26.88 / 0.0677 | — | 29.98 | 5/18 |
| f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 38.8% | 26.32 / 0.0782 | — | 29.36 | 1/18 |
| f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 7.6% | 26.86 / 0.0676 | — | 29.97 | 6/18 |

## in035：第七轮试点场景合计（检测 CNN 未用它们训练，cnw_cnn 只看这一张表）（3 组场景，每个目标视点等权）

| token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| — | 纯光流 | — | — | 25.21 / 0.0617 | — | 29.70 | — |
| cnw_cnn_mw | TTO 100 步 | 直接 | 17.7% | 25.22 / 0.0712 | — | 29.44 | 0/9 |
| cnw_cnn_mw | TTO 100 步 | oracle | 5.5% | 25.53 / 0.0638 | — | 29.67 | 1/9 |
| cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 18.8% | 25.58 / 0.0650 | — | 29.54 | 1/9 |
| cnw_cnn_pix3_fsl | 前馈 FF | oracle | 6.0% | 25.82 / 0.0615 | — | 29.68 | 2/9 |
| f4rq_pix3_fsl | 前馈 FF | 直接 | 30.8% | 25.39 / 0.0716 | — | 28.78 | 1/9 |
| f4rq_pix3_fsl | 前馈 FF | oracle | 7.5% | 25.93 / 0.0625 | — | 29.63 | 4/9 |
| f4rq_pix3bg_fsl | 前馈 FF | 直接 | 31.3% | 25.36 / 0.0728 | — | 28.67 | 1/9 |
| f4rq_pix3bg_fsl | 前馈 FF | oracle | 7.5% | 25.93 / 0.0624 | — | 29.63 | 4/9 |
| f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 8.8% | 25.25 / 0.0706 | — | 28.73 | 1/9 |
| f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 4.2% | 25.75 / 0.0632 | — | 29.62 | 2/9 |
| f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 31.2% | 25.38 / 0.0755 | — | 28.72 | 0/9 |
| f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 7.5% | 25.94 / 0.0630 | — | 29.64 | 3/9 |
| f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 31.2% | 25.37 / 0.0740 | — | 28.68 | 1/9 |
| f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 7.5% | 25.93 / 0.0626 | — | 29.63 | 4/9 |

## in035：逐场景

| 场景 | token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 | TTO 累计耗时 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| changjing/shot_0008 | — | 纯光流 | — | — | 26.12 / 0.1075 | — | 31.07 | — | — |
| changjing/shot_0008 | cnw_cnn_mw | TTO 100 步 | 直接 | 49.2% | 26.53 / 0.1406 | — | 31.09 | 0/3 | 7.49 s |
| changjing/shot_0008 | cnw_cnn_mw | TTO 100 步 | oracle | 8.4% | 27.09 / 0.1069 | — | 31.06 | 1/3 | 7.49 s |
| changjing/shot_0008 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 50.0% | 28.56 / 0.1149 | — | 31.23 | 0/3 | — |
| changjing/shot_0008 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 8.4% | 28.57 / 0.1100 | — | 31.08 | 1/3 | — |
| changjing/shot_0008 | f4rq_pix3_fsl | 前馈 FF | 直接 | 56.9% | 28.59 / 0.1174 | — | 31.28 | 0/3 | — |
| changjing/shot_0008 | f4rq_pix3_fsl | 前馈 FF | oracle | 9.8% | 28.61 / 0.1122 | — | 31.09 | 1/3 | — |
| changjing/shot_0008 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 57.0% | 28.59 / 0.1175 | — | 31.28 | 0/3 | — |
| changjing/shot_0008 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 9.8% | 28.62 / 0.1121 | — | 31.09 | 1/3 | — |
| changjing/shot_0008 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 13.3% | 28.15 / 0.1137 | — | 31.08 | 0/3 | — |
| changjing/shot_0008 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 6.3% | 28.25 / 0.1104 | — | 31.07 | 2/3 | — |
| changjing/shot_0008 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 57.0% | 28.41 / 0.1182 | — | 31.31 | 0/3 | — |
| changjing/shot_0008 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 9.8% | 28.48 / 0.1103 | — | 31.09 | 1/3 | — |
| changjing/shot_0008 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 57.0% | 28.52 / 0.1173 | — | 31.29 | 0/3 | — |
| changjing/shot_0008 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 9.8% | 28.55 / 0.1107 | — | 31.09 | 1/3 | — |
| changjing1/shot_0012 | — | 纯光流 | — | — | 27.76 / 0.0513 | — | 29.67 | — | — |
| changjing1/shot_0012 | cnw_cnn_mw | TTO 100 步 | 直接 | 19.1% | 27.63 / 0.0632 | — | 29.26 | 0/3 | 7.76 s |
| changjing1/shot_0012 | cnw_cnn_mw | TTO 100 步 | oracle | 3.6% | 28.17 / 0.0523 | — | 29.65 | 1/3 | 7.76 s |
| changjing1/shot_0012 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 18.9% | 27.67 / 0.0583 | — | 29.69 | 0/3 | — |
| changjing1/shot_0012 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 3.3% | 28.02 / 0.0538 | — | 29.68 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3_fsl | 前馈 FF | 直接 | 37.8% | 26.85 / 0.0646 | — | 29.47 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3_fsl | 前馈 FF | oracle | 4.7% | 27.62 / 0.0552 | — | 29.67 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 38.0% | 26.81 / 0.0651 | — | 29.44 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 4.7% | 27.59 / 0.0552 | — | 29.66 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 8.1% | 26.77 / 0.0605 | — | 29.38 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 3.1% | 27.48 / 0.0550 | — | 29.65 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 37.9% | 26.96 / 0.0672 | — | 29.39 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 4.7% | 27.72 / 0.0554 | — | 29.65 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 37.9% | 26.85 / 0.0664 | — | 29.40 | 0/3 | — |
| changjing1/shot_0012 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 4.7% | 27.64 / 0.0555 | — | 29.65 | 0/3 | — |
| changjing1/shot_0018 | — | 纯光流 | — | — | 27.69 / 0.0527 | — | 29.90 | — | — |
| changjing1/shot_0018 | cnw_cnn_mw | TTO 100 步 | 直接 | 7.7% | 27.29 / 0.0580 | — | 29.79 | 0/3 | 8.06 s |
| changjing1/shot_0018 | cnw_cnn_mw | TTO 100 步 | oracle | 1.6% | 27.57 / 0.0535 | — | 29.90 | 0/3 | 8.06 s |
| changjing1/shot_0018 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 7.3% | 26.96 / 0.0598 | — | 29.75 | 0/3 | — |
| changjing1/shot_0018 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.5% | 27.41 / 0.0551 | — | 29.90 | 0/3 | — |
| changjing1/shot_0018 | f4rq_pix3_fsl | 前馈 FF | 直接 | 17.6% | 26.97 / 0.0651 | — | 28.77 | 0/3 | — |
| changjing1/shot_0018 | f4rq_pix3_fsl | 前馈 FF | oracle | 2.3% | 27.78 / 0.0553 | — | 29.86 | 1/3 | — |
| changjing1/shot_0018 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 17.6% | 26.95 / 0.0645 | — | 28.75 | 0/3 | — |
| changjing1/shot_0018 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 2.3% | 27.78 / 0.0552 | — | 29.86 | 1/3 | — |
| changjing1/shot_0018 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 3.9% | 26.76 / 0.0624 | — | 28.71 | 0/3 | — |
| changjing1/shot_0018 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 0.8% | 27.51 / 0.0557 | — | 29.82 | 0/3 | — |
| changjing1/shot_0018 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 17.5% | 27.01 / 0.0663 | — | 28.78 | 0/3 | — |
| changjing1/shot_0018 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 2.3% | 27.82 / 0.0552 | — | 29.87 | 1/3 | — |
| changjing1/shot_0018 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 17.5% | 26.97 / 0.0657 | — | 28.75 | 0/3 | — |
| changjing1/shot_0018 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 2.3% | 27.80 / 0.0552 | — | 29.86 | 1/3 | — |
| changjing1/shot_0021 | — | 纯光流 | — | — | 22.74 / 0.0688 | — | 29.91 | — | — |
| changjing1/shot_0021 | cnw_cnn_mw | TTO 100 步 | 直接 | 12.4% | 22.63 / 0.0742 | — | 29.68 | 0/3 | 6.79 s |
| changjing1/shot_0021 | cnw_cnn_mw | TTO 100 步 | oracle | 4.8% | 22.80 / 0.0711 | — | 29.88 | 0/3 | 6.79 s |
| changjing1/shot_0021 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 15.2% | 22.67 / 0.0730 | — | 29.79 | 0/3 | — |
| changjing1/shot_0021 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 6.6% | 22.78 / 0.0703 | — | 29.88 | 0/3 | — |
| changjing1/shot_0021 | f4rq_pix3_fsl | 前馈 FF | 直接 | 31.2% | 22.51 / 0.0848 | — | 28.83 | 0/3 | — |
| changjing1/shot_0021 | f4rq_pix3_fsl | 前馈 FF | oracle | 9.5% | 22.85 / 0.0725 | — | 29.82 | 1/3 | — |
| changjing1/shot_0021 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 32.5% | 22.45 / 0.0892 | — | 28.54 | 0/3 | — |
| changjing1/shot_0021 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 9.5% | 22.85 / 0.0725 | — | 29.81 | 1/3 | — |
| changjing1/shot_0021 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 10.8% | 22.41 / 0.0864 | — | 28.57 | 0/3 | — |
| changjing1/shot_0021 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 4.9% | 22.78 / 0.0736 | — | 29.80 | 1/3 | — |
| changjing1/shot_0021 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 32.4% | 22.53 / 0.0899 | — | 28.63 | 0/3 | — |
| changjing1/shot_0021 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 9.5% | 22.90 / 0.0719 | — | 29.83 | 1/3 | — |
| changjing1/shot_0021 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 32.4% | 22.48 / 0.0900 | — | 28.55 | 0/3 | — |
| changjing1/shot_0021 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 9.5% | 22.87 / 0.0725 | — | 29.80 | 1/3 | — |
| changjing1/shot_0027 | — | 纯光流 | — | — | 26.26 / 0.0511 | — | 30.26 | — | — |
| changjing1/shot_0027 | cnw_cnn_mw | TTO 100 步 | 直接 | 28.7% | 25.78 / 0.0732 | — | 28.87 | 0/3 | 5.61 s |
| changjing1/shot_0027 | cnw_cnn_mw | TTO 100 步 | oracle | 7.4% | 26.67 / 0.0576 | — | 30.13 | 0/3 | 5.61 s |
| changjing1/shot_0027 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 27.8% | 26.99 / 0.0567 | — | 30.01 | 0/3 | — |
| changjing1/shot_0027 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 7.2% | 27.32 / 0.0510 | — | 30.24 | 1/3 | — |
| changjing1/shot_0027 | f4rq_pix3_fsl | 前馈 FF | 直接 | 44.2% | 26.42 / 0.0640 | — | 29.47 | 0/3 | — |
| changjing1/shot_0027 | f4rq_pix3_fsl | 前馈 FF | oracle | 8.7% | 27.12 / 0.0522 | — | 30.19 | 1/3 | — |
| changjing1/shot_0027 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 44.3% | 26.42 / 0.0638 | — | 29.48 | 0/3 | — |
| changjing1/shot_0027 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 8.7% | 27.12 / 0.0522 | — | 30.19 | 1/3 | — |
| changjing1/shot_0027 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 11.4% | 26.44 / 0.0573 | — | 29.74 | 0/3 | — |
| changjing1/shot_0027 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 5.4% | 26.99 / 0.0528 | — | 30.20 | 1/3 | — |
| changjing1/shot_0027 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 44.3% | 26.54 / 0.0636 | — | 29.51 | 0/3 | — |
| changjing1/shot_0027 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 8.7% | 27.24 / 0.0515 | — | 30.21 | 1/3 | — |
| changjing1/shot_0027 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 44.3% | 26.45 / 0.0638 | — | 29.44 | 0/3 | — |
| changjing1/shot_0027 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 8.7% | 27.16 / 0.0517 | — | 30.19 | 1/3 | — |
| changjing1/shot_0032 | — | 纯光流 | — | — | 25.19 / 0.0637 | — | 29.29 | — | — |
| changjing1/shot_0032 | cnw_cnn_mw | TTO 100 步 | 直接 | 33.0% | 25.74 / 0.0813 | — | 28.85 | 0/3 | 7.74 s |
| changjing1/shot_0032 | cnw_cnn_mw | TTO 100 步 | oracle | 10.0% | 26.23 / 0.0669 | — | 29.23 | 1/3 | 7.74 s |
| changjing1/shot_0032 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 34.0% | 27.10 / 0.0621 | — | 29.08 | 1/3 | — |
| changjing1/shot_0032 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 9.9% | 27.27 / 0.0589 | — | 29.26 | 2/3 | — |
| changjing1/shot_0032 | f4rq_pix3_fsl | 前馈 FF | 直接 | 43.7% | 26.68 / 0.0648 | — | 28.75 | 1/3 | — |
| changjing1/shot_0032 | f4rq_pix3_fsl | 前馈 FF | oracle | 10.8% | 27.15 / 0.0597 | — | 29.21 | 2/3 | — |
| changjing1/shot_0032 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 43.8% | 26.68 / 0.0648 | — | 28.74 | 1/3 | — |
| changjing1/shot_0032 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 10.8% | 27.16 / 0.0596 | — | 29.21 | 2/3 | — |
| changjing1/shot_0032 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 11.6% | 26.58 / 0.0631 | — | 28.89 | 1/3 | — |
| changjing1/shot_0032 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 6.9% | 26.96 / 0.0604 | — | 29.23 | 1/3 | — |
| changjing1/shot_0032 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 43.7% | 26.61 / 0.0702 | — | 28.76 | 0/3 | — |
| changjing1/shot_0032 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 10.8% | 27.11 / 0.0618 | — | 29.21 | 1/3 | — |
| changjing1/shot_0032 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 43.7% | 26.65 / 0.0663 | — | 28.74 | 1/3 | — |
| changjing1/shot_0032 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 10.8% | 27.13 / 0.0603 | — | 29.21 | 2/3 | — |

## 耗时

| 场景 | 设置 | token 变体 | 编码窗口边长 | 编码 | 监督框面积 | TTO 各检查点累计 | 各步骤墙钟时间 |
|---|---|---|---:|---:|---:|---|---|
| changjing/shot_0008 | in035 | cnw_cnn_mw | 1296 | 0.33 s | 64% | 25: 1.87s, 50: 3.77s, 100: 7.49s | tokens 10s, pixgs 17s, evaluate 55s, validate 3s |
| changjing1/shot_0012 | in035 | cnw_cnn_mw | 1206+509 | 0.67 s | 53% | 25: 1.92s, 50: 3.85s, 100: 7.76s | tokens 9s, pixgs 14s, evaluate 54s, validate 2s |
| changjing1/shot_0018 | in035 | cnw_cnn_mw | 804+448+448 | 1.04 s | 55% | 25: 2.05s, 50: 4.07s, 100: 8.06s | tokens 9s, pixgs 13s, evaluate 52s, validate 2s |
| changjing1/shot_0021 | in035 | cnw_cnn_mw | 877+475 | 0.66 s | 54% | 25: 1.67s, 50: 3.41s, 100: 6.79s | tokens 9s, pixgs 13s, evaluate 52s, validate 2s |
| changjing1/shot_0027 | in035 | cnw_cnn_mw | 1296 | 0.34 s | 61% | 25: 1.37s, 50: 2.76s, 100: 5.61s | tokens 9s, pixgs 14s, evaluate 52s, validate 2s |
| changjing1/shot_0032 | in035 | cnw_cnn_mw | 1153+452 | 0.66 s | 53% | 25: 1.92s, 50: 3.87s, 100: 7.74s | tokens 9s, pixgs 14s, evaluate 53s, validate 2s |

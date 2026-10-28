# 第十七轮汇总（每个目标视点等权；直接 = 不用真值的贴回，oracle = 只贴真值失败区，诊断用）

不差 = 该目标 fg 的 PSNR 不低于且 LPIPS 不高于纯光流。失败区按可见性拆开：两侧可见 = 两个输入视角都看得到（联合优化能约束），单侧可见 = 只有一个输入视角看得到（深度只能靠背景先验）。失败区几栏都是 oracle 贴回的结果。

## 全部场景（18 个目标视点）

| 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 | 失败区 | 失败区·两侧可见 | 失败区·单侧可见 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 纯光流 | 26.40 / 0.0856 | — | — | — | 18.60 / 0.0427 | 18.84 / 0.0440 | 18.47 / 0.0401 |
| cnw_cnn_mw (TTO 100) | 27.57 / 0.0870 | 4/18 | 27.69 / 0.0775 | 11/18 | 20.62 / 0.0276 | 21.31 / 0.0217 | 20.23 / 0.0209 |
| cnw_cnn_pix3_fsl | 27.08 / 0.0842 | 7/18 | 27.15 / 0.0817 | 8/18 | 19.85 / 0.0334 | 21.11 / 0.0205 | 19.81 / 0.0237 |
| f4rq_pix3_fsl | 27.05 / 0.0894 | 5/18 | 27.26 / 0.0818 | 10/18 | 20.28 / 0.0335 | 21.48 / 0.0194 | 20.07 / 0.0231 |
| f4rq_pix3bg_fsl | 26.98 / 0.0906 | 4/18 | 27.26 / 0.0818 | 9/18 | 20.26 / 0.0335 | 21.49 / 0.0194 | 20.08 / 0.0232 |
| f4rq_pix3bg_fsl_g | 26.75 / 0.0897 | 3/18 | 27.09 / 0.0827 | 8/18 | 19.93 / 0.0375 | 20.64 / 0.0276 | 19.77 / 0.0293 |
| f4rq_pix3bg_fsl_s25 | 27.12 / 0.0892 | 3/18 | 27.44 / 0.0803 | 8/18 | 20.50 / 0.0323 | 21.74 / 0.0188 | 19.98 / 0.0238 |
| f4rq_pix3bg_fsl_s50 | 27.11 / 0.0903 | 3/18 | 27.41 / 0.0812 | 9/18 | 20.45 / 0.0329 | 21.72 / 0.0190 | 20.03 / 0.0234 |

## 第七轮试点场景（检测 CNN 未用其训练）（9 个目标视点）

| 方法 | 直接 fg PSNR / LPIPS | 直接不差 | oracle fg PSNR / LPIPS | oracle 不差 | 失败区 | 失败区·两侧可见 | 失败区·单侧可见 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 纯光流 | 24.75 / 0.1081 | — | — | — | 17.48 / 0.0682 | 17.57 / 0.0704 | 18.57 / 0.0601 |
| cnw_cnn_mw (TTO 100) | 27.07 / 0.1052 | 4/9 | 27.07 / 0.0921 | 7/9 | 20.58 / 0.0397 | 21.24 / 0.0297 | 20.70 / 0.0249 |
| cnw_cnn_pix3_fsl | 26.21 / 0.1016 | 5/9 | 26.18 / 0.0993 | 5/9 | 19.38 / 0.0494 | 20.77 / 0.0296 | 19.71 / 0.0314 |
| f4rq_pix3_fsl | 25.74 / 0.1112 | 3/9 | 25.97 / 0.1009 | 5/9 | 19.17 / 0.0511 | 20.54 / 0.0299 | 19.61 / 0.0319 |
| f4rq_pix3bg_fsl | 25.69 / 0.1122 | 3/9 | 25.97 / 0.1009 | 5/9 | 19.16 / 0.0510 | 20.55 / 0.0299 | 19.60 / 0.0322 |
| f4rq_pix3bg_fsl_g | 25.34 / 0.1125 | 2/9 | 25.73 / 0.1026 | 4/9 | 18.83 / 0.0586 | 19.64 / 0.0435 | 19.33 / 0.0422 |
| f4rq_pix3bg_fsl_s25 | 25.98 / 0.1080 | 3/9 | 26.34 / 0.0976 | 5/9 | 19.64 / 0.0483 | 20.95 / 0.0281 | 19.52 / 0.0328 |
| f4rq_pix3bg_fsl_s50 | 25.95 / 0.1112 | 3/9 | 26.27 / 0.0996 | 5/9 | 19.53 / 0.0498 | 20.94 / 0.0290 | 19.57 / 0.0325 |

# 六路数据集：局部 GS 验证汇总

token 变体 cnw_cnn_mw, cnw_cnn_pix3_fsl, f4rq_pix3_fsl, f4rq_pix3bg_fsl, f4rq_pix3bg_fsl_g, f4rq_pix3bg_fsl_s25, f4rq_pix3bg_fsl_s50，`_al` 对齐域；PSNR / LPIPS 为各目标视点平均；不差目标数 = fg 的 PSNR 不低于且 LPIPS 不高于纯光流的目标数；贴回区 = 实际贴回面积占前景比例；oracle 只贴 core ∩ 真值失败区（诊断用）。object = 真值中最大的高饱和色块膨胀 40 px（没有彩色物体的场景为空，记为 —）。

## in035：全部场景合计（6 组场景，每个目标视点等权）

| token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| — | 纯光流 | — | — | 26.40 / 0.0856 | — | 30.65 | — |
| cnw_cnn_mw | TTO 100 步 | 直接 | 24.0% | 27.57 / 0.0870 | — | 30.81 | 4/18 |
| cnw_cnn_mw | TTO 100 步 | oracle | 5.3% | 27.69 / 0.0775 | — | 30.59 | 11/18 |
| cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 24.2% | 27.08 / 0.0842 | — | 30.91 | 7/18 |
| cnw_cnn_pix3_fsl | 前馈 FF | oracle | 5.1% | 27.15 / 0.0817 | — | 30.64 | 8/18 |
| f4rq_pix3_fsl | 前馈 FF | 直接 | 30.9% | 27.05 / 0.0894 | — | 30.54 | 5/18 |
| f4rq_pix3_fsl | 前馈 FF | oracle | 5.4% | 27.26 / 0.0818 | — | 30.63 | 10/18 |
| f4rq_pix3bg_fsl | 前馈 FF | 直接 | 31.1% | 26.98 / 0.0906 | — | 30.44 | 4/18 |
| f4rq_pix3bg_fsl | 前馈 FF | oracle | 5.4% | 27.26 / 0.0818 | — | 30.62 | 9/18 |
| f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 7.9% | 26.75 / 0.0897 | — | 30.14 | 3/18 |
| f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 4.0% | 27.09 / 0.0827 | — | 30.63 | 8/18 |
| f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 31.1% | 27.12 / 0.0892 | — | 30.34 | 3/18 |
| f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 5.4% | 27.44 / 0.0803 | — | 30.63 | 8/18 |
| f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 31.1% | 27.11 / 0.0903 | — | 30.36 | 3/18 |
| f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 5.4% | 27.41 / 0.0812 | — | 30.62 | 9/18 |

## in035：第七轮试点场景合计（检测 CNN 未用它们训练，cnw_cnn 只看这一张表）（3 组场景，每个目标视点等权）

| token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 |
|---|---|---|---:|---:|---:|---:|---:|
| — | 纯光流 | — | — | 24.75 / 0.1081 | — | 31.74 | — |
| cnw_cnn_mw | TTO 100 步 | 直接 | 38.6% | 27.07 / 0.1052 | — | 32.12 | 4/9 |
| cnw_cnn_mw | TTO 100 步 | oracle | 8.6% | 27.07 / 0.0921 | — | 31.61 | 7/9 |
| cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 39.1% | 26.21 / 0.1016 | — | 32.28 | 5/9 |
| cnw_cnn_pix3_fsl | 前馈 FF | oracle | 8.4% | 26.18 / 0.0993 | — | 31.72 | 5/9 |
| f4rq_pix3_fsl | 前馈 FF | 直接 | 45.3% | 25.74 / 0.1112 | — | 31.64 | 3/9 |
| f4rq_pix3_fsl | 前馈 FF | oracle | 8.9% | 25.97 / 0.1009 | — | 31.69 | 5/9 |
| f4rq_pix3bg_fsl | 前馈 FF | 直接 | 45.7% | 25.69 / 0.1122 | — | 31.54 | 3/9 |
| f4rq_pix3bg_fsl | 前馈 FF | oracle | 8.9% | 25.97 / 0.1009 | — | 31.68 | 5/9 |
| f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 12.6% | 25.34 / 0.1125 | — | 30.96 | 2/9 |
| f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 6.9% | 25.73 / 0.1026 | — | 31.69 | 4/9 |
| f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 45.6% | 25.98 / 0.1080 | — | 31.33 | 3/9 |
| f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 8.9% | 26.34 / 0.0976 | — | 31.69 | 5/9 |
| f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 45.7% | 25.95 / 0.1112 | — | 31.36 | 3/9 |
| f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 8.9% | 26.27 / 0.0996 | — | 31.68 | 5/9 |

## in035：逐场景

| 场景 | token 变体 | 方法 | 贴回 | 贴回区 | fg PSNR / LPIPS | object PSNR / LPIPS | rest PSNR | 不差目标数 | TTO 累计耗时 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|
| changjing/shot_0000 | — | 纯光流 | — | — | 28.76 / 0.0522 | — | 29.88 | — | — |
| changjing/shot_0000 | cnw_cnn_mw | TTO 100 步 | 直接 | 3.0% | 28.38 / 0.0541 | — | 29.81 | 0/3 | 3.12 s |
| changjing/shot_0000 | cnw_cnn_mw | TTO 100 步 | oracle | 0.5% | 28.64 / 0.0527 | — | 29.88 | 1/3 | 3.12 s |
| changjing/shot_0000 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 3.0% | 28.77 / 0.0536 | — | 29.88 | 0/3 | — |
| changjing/shot_0000 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 0.5% | 28.79 / 0.0528 | — | 29.88 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3_fsl | 前馈 FF | 直接 | 6.0% | 28.26 / 0.0621 | — | 29.16 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3_fsl | 前馈 FF | oracle | 0.5% | 28.75 / 0.0534 | — | 29.85 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 7.2% | 28.08 / 0.0663 | — | 28.94 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 0.5% | 28.71 / 0.0537 | — | 29.82 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 1.7% | 28.15 / 0.0601 | — | 29.05 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 0.2% | 28.68 / 0.0532 | — | 29.82 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 7.2% | 28.11 / 0.0650 | — | 28.97 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 0.5% | 28.71 / 0.0538 | — | 29.82 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 7.2% | 28.10 / 0.0654 | — | 28.97 | 0/3 | — |
| changjing/shot_0000 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 0.5% | 28.72 / 0.0537 | — | 29.82 | 0/3 | — |
| changjing/shot_0003 | — | 纯光流 | — | — | 27.80 / 0.0823 | — | 29.29 | — | — |
| changjing/shot_0003 | cnw_cnn_mw | TTO 100 步 | 直接 | 9.1% | 28.05 / 0.0883 | — | 29.29 | 0/3 | 2.03 s |
| changjing/shot_0003 | cnw_cnn_mw | TTO 100 步 | oracle | 2.0% | 28.24 / 0.0800 | — | 29.29 | 3/3 | 2.03 s |
| changjing/shot_0003 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 8.6% | 28.54 / 0.0822 | — | 29.31 | 2/3 | — |
| changjing/shot_0003 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.8% | 28.54 / 0.0795 | — | 29.29 | 3/3 | — |
| changjing/shot_0003 | f4rq_pix3_fsl | 前馈 FF | 直接 | 19.1% | 28.55 / 0.0855 | — | 29.26 | 1/3 | — |
| changjing/shot_0003 | f4rq_pix3_fsl | 前馈 FF | oracle | 2.2% | 28.65 / 0.0790 | — | 29.29 | 3/3 | — |
| changjing/shot_0003 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 19.4% | 28.21 / 0.0891 | — | 28.97 | 0/3 | — |
| changjing/shot_0003 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 2.2% | 28.63 / 0.0791 | — | 29.28 | 3/3 | — |
| changjing/shot_0003 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 3.9% | 28.08 / 0.0875 | — | 28.94 | 0/3 | — |
| changjing/shot_0003 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 1.4% | 28.53 / 0.0791 | — | 29.28 | 3/3 | — |
| changjing/shot_0003 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 19.4% | 28.24 / 0.0916 | — | 28.97 | 0/3 | — |
| changjing/shot_0003 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 2.2% | 28.61 / 0.0790 | — | 29.28 | 3/3 | — |
| changjing/shot_0003 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 19.4% | 28.25 / 0.0899 | — | 28.97 | 0/3 | — |
| changjing/shot_0003 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 2.2% | 28.62 / 0.0789 | — | 29.28 | 3/3 | — |
| changjing1/shot_0001 | — | 纯光流 | — | — | 23.95 / 0.1893 | — | 35.38 | — | — |
| changjing1/shot_0001 | cnw_cnn_mw | TTO 100 步 | 直接 | 93.9% | 28.23 / 0.1834 | — | 36.87 | 1/3 | 2.57 s |
| changjing1/shot_0001 | cnw_cnn_mw | TTO 100 步 | oracle | 15.6% | 27.78 / 0.1503 | — | 35.03 | 3/3 | 2.57 s |
| changjing1/shot_0001 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 96.1% | 27.84 / 0.1649 | — | 37.26 | 3/3 | — |
| changjing1/shot_0001 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 15.4% | 27.48 / 0.1636 | — | 35.36 | 3/3 | — |
| changjing1/shot_0001 | f4rq_pix3_fsl | 前馈 FF | 直接 | 103.2% | 27.76 / 0.1673 | — | 37.20 | 3/3 | — |
| changjing1/shot_0001 | f4rq_pix3_fsl | 前馈 FF | oracle | 16.2% | 27.44 / 0.1635 | — | 35.35 | 3/3 | — |
| changjing1/shot_0001 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 102.9% | 27.77 / 0.1660 | — | 37.21 | 3/3 | — |
| changjing1/shot_0001 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 16.2% | 27.44 / 0.1629 | — | 35.36 | 3/3 | — |
| changjing1/shot_0001 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 21.2% | 26.64 / 0.1775 | — | 35.33 | 2/3 | — |
| changjing1/shot_0001 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 10.8% | 26.75 / 0.1690 | — | 35.37 | 2/3 | — |
| changjing1/shot_0001 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 103.0% | 27.41 / 0.1637 | — | 36.57 | 3/3 | — |
| changjing1/shot_0001 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 16.2% | 27.24 / 0.1637 | — | 35.36 | 3/3 | — |
| changjing1/shot_0001 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 102.9% | 27.62 / 0.1681 | — | 36.73 | 3/3 | — |
| changjing1/shot_0001 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 16.2% | 27.35 / 0.1649 | — | 35.35 | 3/3 | — |
| changjing1/shot_0007 | — | 纯光流 | — | — | 28.35 / 0.0496 | — | 29.69 | — | — |
| changjing1/shot_0007 | cnw_cnn_mw | TTO 100 步 | 直接 | 5.9% | 28.22 / 0.0511 | — | 29.61 | 0/3 | 3.30 s |
| changjing1/shot_0007 | cnw_cnn_mw | TTO 100 步 | oracle | 1.2% | 28.43 / 0.0491 | — | 29.67 | 1/3 | 3.30 s |
| changjing1/shot_0007 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 6.1% | 27.61 / 0.0552 | — | 29.67 | 0/3 | — |
| changjing1/shot_0007 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 1.1% | 27.79 / 0.0524 | — | 29.69 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3_fsl | 前馈 FF | 直接 | 9.3% | 28.09 / 0.0554 | — | 29.37 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3_fsl | 前馈 FF | oracle | 0.8% | 28.41 / 0.0506 | — | 29.66 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 9.3% | 28.12 / 0.0557 | — | 29.40 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 0.8% | 28.43 / 0.0509 | — | 29.68 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 2.3% | 28.10 / 0.0537 | — | 29.40 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 0.5% | 28.40 / 0.0508 | — | 29.67 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 9.2% | 28.08 / 0.0553 | — | 29.40 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 0.8% | 28.41 / 0.0510 | — | 29.68 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 9.2% | 28.10 / 0.0555 | — | 29.41 | 0/3 | — |
| changjing1/shot_0007 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 0.8% | 28.42 / 0.0509 | — | 29.68 | 0/3 | — |
| changjing1/shot_0013 | — | 纯光流 | — | — | 28.02 / 0.0578 | — | 29.74 | — | — |
| changjing1/shot_0013 | cnw_cnn_mw | TTO 100 步 | 直接 | 13.4% | 27.94 / 0.0668 | — | 29.60 | 0/3 | 4.94 s |
| changjing1/shot_0013 | cnw_cnn_mw | TTO 100 步 | oracle | 2.5% | 28.27 / 0.0597 | — | 29.73 | 0/3 | 4.94 s |
| changjing1/shot_0013 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 13.2% | 27.73 / 0.0629 | — | 29.63 | 0/3 | — |
| changjing1/shot_0013 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 2.4% | 28.05 / 0.0603 | — | 29.73 | 0/3 | — |
| changjing1/shot_0013 | f4rq_pix3_fsl | 前馈 FF | 直接 | 20.9% | 28.46 / 0.0618 | — | 29.66 | 1/3 | — |
| changjing1/shot_0013 | f4rq_pix3_fsl | 前馈 FF | oracle | 2.5% | 28.59 / 0.0584 | — | 29.74 | 2/3 | — |
| changjing1/shot_0013 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 21.0% | 28.47 / 0.0620 | — | 29.66 | 1/3 | — |
| changjing1/shot_0013 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 2.5% | 28.59 / 0.0584 | — | 29.74 | 1/3 | — |
| changjing1/shot_0013 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 3.4% | 28.29 / 0.0598 | — | 29.65 | 1/3 | — |
| changjing1/shot_0013 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 1.3% | 28.42 / 0.0584 | — | 29.74 | 1/3 | — |
| changjing1/shot_0013 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 20.9% | 28.48 / 0.0640 | — | 29.68 | 0/3 | — |
| changjing1/shot_0013 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 2.5% | 28.61 / 0.0590 | — | 29.74 | 0/3 | — |
| changjing1/shot_0013 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 20.9% | 28.47 / 0.0629 | — | 29.67 | 0/3 | — |
| changjing1/shot_0013 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 2.5% | 28.60 / 0.0587 | — | 29.74 | 1/3 | — |
| changjing1/shot_0022 | — | 纯光流 | — | — | 21.54 / 0.0828 | — | 29.95 | — | — |
| changjing1/shot_0022 | cnw_cnn_mw | TTO 100 步 | 直接 | 18.8% | 24.59 / 0.0780 | — | 29.68 | 3/3 | 3.52 s |
| changjing1/shot_0022 | cnw_cnn_mw | TTO 100 步 | oracle | 9.9% | 24.80 / 0.0732 | — | 29.94 | 3/3 | 3.52 s |
| changjing1/shot_0022 | cnw_cnn_pix3_fsl | 前馈 FF | 直接 | 18.2% | 22.02 / 0.0862 | — | 29.71 | 2/3 | — |
| changjing1/shot_0022 | cnw_cnn_pix3_fsl | 前馈 FF | oracle | 9.5% | 22.26 / 0.0817 | — | 29.92 | 2/3 | — |
| changjing1/shot_0022 | f4rq_pix3_fsl | 前馈 FF | 直接 | 26.8% | 21.21 / 0.1043 | — | 28.56 | 0/3 | — |
| changjing1/shot_0022 | f4rq_pix3_fsl | 前馈 FF | oracle | 10.1% | 21.73 / 0.0860 | — | 29.87 | 2/3 | — |
| changjing1/shot_0022 | f4rq_pix3bg_fsl | 前馈 FF | 直接 | 26.9% | 21.23 / 0.1044 | — | 28.47 | 0/3 | — |
| changjing1/shot_0022 | f4rq_pix3bg_fsl | 前馈 FF | oracle | 10.1% | 21.76 / 0.0860 | — | 29.88 | 2/3 | — |
| changjing1/shot_0022 | f4rq_pix3bg_fsl_g | 前馈 FF | 直接 | 14.9% | 21.23 / 0.0998 | — | 28.50 | 0/3 | — |
| changjing1/shot_0022 | f4rq_pix3bg_fsl_g | 前馈 FF | oracle | 9.5% | 21.75 / 0.0857 | — | 29.87 | 2/3 | — |
| changjing1/shot_0022 | f4rq_pix3bg_fsl_s25 | 前馈 FF | 直接 | 26.8% | 22.42 / 0.0953 | — | 28.44 | 0/3 | — |
| changjing1/shot_0022 | f4rq_pix3bg_fsl_s25 | 前馈 FF | oracle | 10.1% | 23.08 / 0.0753 | — | 29.88 | 2/3 | — |
| changjing1/shot_0022 | f4rq_pix3bg_fsl_s50 | 前馈 FF | 直接 | 26.8% | 22.11 / 0.1000 | — | 28.40 | 0/3 | — |
| changjing1/shot_0022 | f4rq_pix3bg_fsl_s50 | 前馈 FF | oracle | 10.1% | 22.74 / 0.0800 | — | 29.87 | 2/3 | — |

## 耗时

| 场景 | 设置 | token 变体 | 编码窗口边长 | 编码 | 监督框面积 | TTO 各检查点累计 | 各步骤墙钟时间 |
|---|---|---|---:|---:|---:|---|---|
| changjing/shot_0000 | in035 | cnw_cnn_mw | 617+468+448 | 0.53 s | 49% | 25: 0.80s, 50: 1.58s, 100: 3.12s | tokens 5s, pixgs 5s, evaluate 32s, validate 1s |
| changjing/shot_0003 | in035 | cnw_cnn_mw | 946 | 0.17 s | 69% | 25: 0.53s, 50: 1.03s, 100: 2.03s | tokens 5s, pixgs 7s, evaluate 37s, validate 2s |
| changjing1/shot_0001 | in035 | cnw_cnn_mw | 1058 | 0.17 s | 75% | 25: 0.65s, 50: 1.30s, 100: 2.57s | tokens 5s, pixgs 7s, evaluate 25s, validate 2s |
| changjing1/shot_0007 | in035 | cnw_cnn_mw | 448+648+468 | 0.52 s | 62% | 25: 0.84s, 50: 1.67s, 100: 3.30s | tokens 5s, pixgs 6s, evaluate 37s, validate 2s |
| changjing1/shot_0013 | in035 | cnw_cnn_mw | 905+448+506+448 | 0.69 s | 39% | 25: 1.26s, 50: 2.50s, 100: 4.94s | tokens 5s, pixgs 7s, evaluate 37s, validate 2s |
| changjing1/shot_0022 | in035 | cnw_cnn_mw | 1064+471 | 0.33 s | 58% | 25: 0.89s, 50: 1.77s, 100: 3.52s | tokens 5s, pixgs 7s, evaluate 36s, validate 2s |

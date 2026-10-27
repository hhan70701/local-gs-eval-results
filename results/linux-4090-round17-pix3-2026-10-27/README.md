# linux-4090 round17 pix3

源码标签 [linux-4090-round17-pix3](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-4090-round17-pix3)，提交 `3585842a50d8e26ffa87033dda9f0cfb28d21626`。

使用默认第十七轮参数，只覆盖工作目录为原 work/dataset6_round15_pixgs，复用 aligned、token、flow、AnySplat。
只运行本机 23 组（输入 0/3/5、目标 1/2/4，共 69 个目标视点）：pix2_fsl / _g、pix3n_fsl / _g、pix3_fsl（两真实输入视角联合优化 100 步），以及仅评估的 cnw_cnn_mw TTO100 参照。对应关系固定 FS-L，token 固定 cnw_cnn。全部新高斯变体采用 gsplat。

## 统一统计与核验

- [实验汇总](summary_all.md)：包含 fg、失败区、两侧可见/单侧可见失败区，直接与 oracle 贴回；含全 23 组及未参与 CNN 训练的三组试点统计。
- 23 组验证全部 PASS；69 张主对比图齐全。全部实验完成后统一核验，记录见 [completion_check.json](completion_check.json)。
- 25 项测试通过；实验 872.86 秒，密集计时 109.01 秒。验证警告 4 条，原文保留在完整性记录。
- [运行日志](dataset6_r17.log)、[计时日志](bench_dense.log)、[密集视点计时](bench_dense_linux-4090.md)及[完整计时数据](bench_dense_linux-4090.json)。计时按默认前 6 组，每对 41/60 个视点，比较 pix2/pix3n/pix3；计时前没有其他 GPU 计算进程。
- 本次 timing.json 只含 pixgs/evaluate/validate。旧 AnySplat/TTO 时间来自复用元数据，未在本次重测。
- 计时表的一次性时间已包含联合优化，once_opt_s 单列该部分，合计不含对应关系导出；对应关系的 Windows 3090 导出时间和引用的 token 检测时间见报告。

## 复现与保留

上一轮基线见 [round16a 发布结果](https://github.com/hhan70701/local-gs-eval-results/tree/experiment/linux-4090-round16a-p3h-pix2-2026-10-27/results/linux-4090-round16a-p3h-pix2-2026-10-27)。本机旧 eval、日志、配置、计时与上一轮汇总已归档，当前 eval 从空目录生成。
本轮配置 [base_config.yaml](base_config.yaml)；环境、基线提交与输入记录 [environment_and_inputs.json](environment_and_inputs.json)、environment/。复用的 851 份旧 GS JSON（排除本轮重算的 pix2_fsl）与上一轮发布的哈希相同。
cnw_cnn 泛化结论只看 changjing/shot_0000、changjing1/shot_0001、changjing1/shot_0022；其余场景参与过 CNN 训练。Oracle 只作诊断。
沿用用户授权的半像素矩阵 H_halfpx[i] = T(-0.5,-0.5) @ H_existing[i]；矩阵与生成记录见 calibration/ 及 environment/halfpx-generation.json。
完整输出保留在主机，上传包含评估、日志、配置、GS JSON 及计时报告，不含数据集、权重及 GS 渲染大图。只发布 4090 结果。

# linux-4090 第十三轮：六路数据集，输入 0/3/5

源码标签 [linux-4090-round13](https://github.com/luckyhan-mike/local-gs-eval/tree/linux-4090-round13)，提交 `a5d5cbc0ddd2b0a8143bfdccab456ae417f8cb78`。使用 `configs/dataset6_lean.yaml`，只将输出目录改为 `work/dataset6_round13`，完整参数见 [base_config.yaml](base_config.yaml)。

## 结果入口

- [全部场景汇总](summary_all.md)：rife、rife_w30、rife_w40，前馈及 TTO 25/50/100 步，直接贴回和 oracle 上限。
- [总日志](run.log)、[完整性检查](completion_check.json)、[本轮记录](RUN_NOTES.md)。
- 各场景目录包含 config.yaml、timing.json、poses、logs、完整 eval（指标与对比图）、prepare/prepare.json、tokens/tokens.json 和 GS 各阶段 meta.json。
- 环境和单元测试日志位于 environment/；校准矩阵与半像素生成记录位于 calibration/ 及 environment/halfpx-generation.json。

五组场景、15 个目标视点均完成全部六步，五份结果验证均为 PASS，无验证警告。18 项单元测试通过；15 张主对比图齐全。正式运行耗时 472.13 秒。

## 主要观察

| 方法 | 直接贴回区占前景 | 前景 PSNR ↑ / LPIPS ↓ | 两项均不差于纯光流的目标数 |
|---|---:|---:|---:|
| 纯光流 | — | 25.30 / 0.0974 | — |
| rife，TTO 100 | 36.7% | 25.59 / 0.1237 | 1/15 |
| rife_w30，TTO 100 | 22.2% | 25.52 / 0.1140 | 1/15 |
| rife_w40，TTO 50 | 14.0% | 25.46 / 0.1114 | 2/15 |
| rife_w40，TTO 100 | 14.2% | 25.45 / 0.1103 | 2/15 |

rife_w40 的 TTO 100 步 oracle 为 25.73 / 0.0944，8/15。Oracle 使用真值失败区域，仅为诊断上限。更严格阈值缩小了贴回区，直接贴回仍未稳定超过纯光流。五组编码窗口仍全部为 1296 px。

两档新阈值是在观察过这五组旧结果后确定的，按代码仓库说明，存在对已知场景过拟合的风险。

## 可复现信息

RTX 4090，驱动 580.178.04，Python 3.10.22，torch 2.2.0+cu121，gsplat 1.4.0+pt22cu121。
模型和输入文件校验信息见 [environment_and_inputs.json](environment_and_inputs.json)。输入数据与上一轮相同；沿用经用户授权生成的半像素矩阵：`H_halfpx[i] = T(-0.5,-0.5) @ H_existing[i]`，对应统一裁剪起点 `(192.5,104.5)`。

结果先在主机完成并验证，随后按用户要求发布。原始数据、模型权重及 aligned/flow/gs 大图不包含在本目录；完整输出和 ZIP 保留在主机。run_status.json 保留实验结束时的原始运行状态，发布校验清单以 manifest.json 为准。

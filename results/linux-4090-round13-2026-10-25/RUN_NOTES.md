# linux-4090 第十三轮：本机运行记录

- 源码版本：a5d5cbc0ddd2b0a8143bfdccab456ae417f8cb78，标签 linux-4090-round13。
- 使用 configs/dataset6_lean.yaml 的实验参数；只将 dataset6.work_root 改为 work/dataset6_round13，保存为 base_config.yaml。上一轮 work/dataset6 保留。
- 五组场景、15 个目标视点、三种 token 变体，TTO 25/50/100 步；全流程从 prepare 开始重跑。
- 18 项单元测试通过；五组 validation.json 均为 PASS，无验证警告；15 张主对比图齐全。正式运行约 472.13 秒。
- 使用已有缓存权重，实验进程设置 HF_HUB_OFFLINE=1。数据与上一轮的哈希一致，沿用之前经用户授权生成的 halfpx 矩阵。
- 本轮先在主机保存；随后经用户明确要求，将评估结果、日志和元数据发布到本分支。完整渲染输出和 ZIP 仍保留在主机。

## 结果入口

[全部场景汇总](summary_all.md)、[总运行日志](run.log)、[完整性检查](completion_check.json)、[环境和输入哈希](environment_and_inputs.json)。
各场景下包含配置、timing.json、poses、logs、eval、tokens、prepare 和 GS 前馈/优化输出。

## 初步观察

- 五组场景的编码窗口边长仍均为 1296 px；window_variants: [rife] 已按新版设置执行，但本次没有缩小窗口边长。
- 更严格的 rife_w40 在 TTO 100 步下，实际贴回区平均为前景的 14.2%；原 rife 为 36.7%。
- rife_w40 的 TTO 50/100 步直接贴回有 2/15 个目标的前景 PSNR 和 LPIPS 同时不差于纯光流；尚未稳定超过纯光流。
- 阈值是在观察过这五组场景的旧结果后确定的，按仓库说明，这一比较存在对已知场景过拟合的风险。

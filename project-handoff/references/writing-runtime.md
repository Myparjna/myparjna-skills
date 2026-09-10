# 环境、部署与运维

只阅读本次涉及的文档章节，按项目实际内容填写。

### environment.md（环境变量）
- 以 analysis-report.json 的 `environment_variables` 为准，**一个都不能漏**（verify 会反向校验）
- `used_but_not_declared` 的变量要特别说明：在哪个文件用到（写 `路径:行号`），为什么没在 .env.example 里
- 每个变量写明：用途、示例格式（如 `postgres://...`，不是真实值）、哪些环境需要（本地/CI/生产）
- 高熵值警告中的变量确认后必须标注轮换计划

### deployment.md（部署与 CI/CD）
- 按"从零部署一遍"的顺序写，每步是可直接执行的命令
- CI secrets 写明在 GitHub → Settings → Secrets 中如何配置、值从哪来
- Cloudflare 绑定（KV/D1/R2）写明 ID 对应的资源、是否需要重建
- Kubernetes 部署需写明 kubectl apply 命令和 namespace 配置
- 检测到 Vercel/Netlify/VPS 痕迹时，按 references/deployment-platforms.md 对应章节补齐

### deployment.md 内的基础设施与账号
- 每个外部服务一张表，必填字段：服务名、用途、账号归属、控制台地址、关联的密钥、交接动作
- **账号归属是交接最容易踩坑的地方**。报告中查不到归属信息时一律标 `[需向交接人确认: ...]`

### operations.md（维护与故障处置）
- 常见故障 → 排查路径 → 解决命令
- 没有真实运维经验的不要编故障案例，只写从代码能推断的
- 回滚命令写真实命令不写概念

日常维护部分保留监控日志入口、依赖更新策略及实际需要的例行检查。故障场景仅覆盖项目真实依赖；没有 AI 或数据库时不添加对应故障。


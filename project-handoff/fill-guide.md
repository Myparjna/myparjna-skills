# 交接文档填写指南

> 本指南给负责填写 `handoff/` 下 TODO(AI) 的人（或 AI）使用。
> 填写完成后必须运行 `python scripts/verify_handoff.py` 并通过。

## 核心原则

1. **只写有证据的内容。** 每条信息必须能追溯到：源码、配置文件、`analysis-report.json`、或交接人亲口确认。
2. **不知道就标记，不编造。** 唯一合法写法：`[需向交接人确认: 具体问题]`。
   - ✓ `[需向交接人确认: DEEPSEEK_API_KEY 是个人账号还是团队账号？]`
   - ✗ "应该是团队账号"、"一般情况下…"、"视情况而定"
3. **密钥值绝不写入文档。** 只写密钥的**名称、用途、获取方式、交接渠道**。
   - ✓ "`DATABASE_URL`：Supabase 连接串，在 Supabase Dashboard → Settings → Database 获取，原值通过 1Password 共享库交接"
   - ✗ 任何以 `sk-`、`ghp_`、`AKIA` 开头的真实值
4. **写给"完全不了解此项目的下一任"。** 假设读者没参与过任何讨论，不知道任何口头约定。

## 各文档填写要点

### README.md（项目概览）
- "这是什么"用一句话说清：给谁用、解决什么问题
- 技术栈直接抄 analysis-report.json，不要凭印象写版本号
- 快速启动命令必须逐条验证可行性

### ARCHITECTURE.md（系统架构）
- 架构图用 mermaid，标出数据流向（用户 → CF Pages → Workers → D1/外部 API）
- 目录结构为 5-10 个关键目录各加一行用途说明
- Monorepo 需说明各 workspace 职责划分

### ENVIRONMENT.md（环境变量）
- 以 analysis-report.json 的 `environment_variables` 为准，**一个都不能漏**（verify 会反向校验）
- `used_but_not_declared` 的变量要特别说明：在哪个文件用到（写 `路径:行号`），为什么没在 .env.example 里
- 每个变量写明：用途、示例格式（如 `postgres://...`，不是真实值）、哪些环境需要（本地/CI/生产）
- 高熵值警告中的变量确认后必须标注轮换计划

### DEPLOYMENT.md（部署与 CI/CD）
- 按"从零部署一遍"的顺序写，每步是可直接执行的命令
- CI secrets 写明在 GitHub → Settings → Secrets 中如何配置、值从哪来
- Cloudflare 绑定（KV/D1/R2）写明 ID 对应的资源、是否需要重建
- Kubernetes 部署需写明 kubectl apply 命令和 namespace 配置

### INFRASTRUCTURE.md（基础设施与账号）
- 每个外部服务一张表，必填字段：服务名、用途、账号归属、控制台地址、关联的密钥、交接动作
- **账号归属是交接最容易踩坑的地方**。报告中查不到归属信息时一律标 `[需向交接人确认: ...]`

### AI-SERVICES.md（AI 服务）
- 逐个 SDK 说明在哪个功能中使用、调用处源码位置
- 模型名要写明用于什么功能、能否替换
- 计费和限额向用户问

### DATABASE.md（数据库）
- 画 mermaid ER 图或逐表说明核心表/集合
- 迁移命令依据 ORM 类型写真实命令
- 备份机制如实写（很可能没有）

### API.md（接口文档）— 条件生成
- 以 analysis-report.json 的 `api_routes` 为准，逐个补充用途
- 请求/响应示例从源码中读取真实字段，**禁止编造字段名**
- 数量太多时优先覆盖核心业务接口，其余归类说明
- 鉴权方式从中间件/拦截器源码确认（API key? JWT? session? 无鉴权?）

### DESKTOP.md（桌面端）— 条件生成
- 依据桌面端类型（Electron/Tauri/WinUI/WPF/WinForms）写对应文档
- 开发模式启动和生产构建/打包命令必须区分 Windows/macOS 目标
- 代码签名状态（有无证书、在谁手里）必须写明
- 自动更新机制（有/无，更新服务器在哪）必须说明

### KNOWN-ISSUES.md（已知问题）
- 这是交接中**最有价值**的文档
- 检索源码中的 TODO/FIXME/HACK 注释并逐条核实
- 技术债允许 AI 主动判断，但每条给具体文件位置

### RUNBOOK.md（运维手册）
- 常见故障 → 排查路径 → 解决命令
- 没有真实运维经验的不要编故障案例，只写从代码能推断的
- 回滚命令写真实命令不写概念

## 自查清单（提交前）

- [ ] `python scripts/verify_handoff.py` 退出码为 0
- [ ] 文档中没有任何真实密钥值
- [ ] 所有 `[需向交接人确认: ...]` 已汇总到 README.md 顶部的"待确认问题"区
- [ ] 引用的文件路径都真实存在

## 常见错误

| 错误 | 正确做法 |
|---|---|
| "配置好相关环境变量即可" | 列出每个变量名 + 获取方式 |
| "参考官方文档" | 写出具体步骤，链接只作补充 |
| 把 .env 内容整段贴进文档 | 只贴变量名和格式说明 |
| "此处略" / "等等" | 写完整，或标待确认 |
| 凭记忆写版本号 | 抄 package.json / lock 文件 |
| "应该是团队账号" | 标 `[需向交接人确认: 账号归属]` |

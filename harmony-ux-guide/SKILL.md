---
name: harmony-ux-guide
description: "Generate complete project handoff documentation: architecture overview, deployment guides (Docker/Cloudflare/CI/K8s), environment variables, AI API usage, database, known issues, and operational runbooks. Use when delivering a project to a client, transitioning a codebase between teams or AI agents, onboarding maintainers, or packaging a project for long-term maintenance."
---

# Project Handoff

为项目生成完整的 `handoff/` 交接文档包。本技能由"脚本扫描 + AI 补全 + 脚本验收"三段构成。**你（AI）的核心工作在 Step 4：把骨架中的每一个 `TODO(AI)` 替换为真实内容。**

## 硬性规则（MUST）

1. **禁止跳步。** 必须按 Step 1 → 6 顺序执行。
2. **禁止编造。** 所有内容必须来自：扫描报告 `analysis-report.json`、你实际读过的源码文件、或用户的明确回答。不确定的内容写 `[需向交接人确认: 具体问题]`，不许猜。
3. **禁止留空。** 每个 `TODO(AI)` 必须被处理：要么填入真实内容，要么改写为 `[需向交接人确认: ...]`。
4. **`verify_handoff.py` 不通过，禁止打包。** 这是质量门禁，没有例外。
5. 填写前必须先读 `references/fill-guide.md`，按其中的逐文件标准执行。

## Workflow

### Step 1 — 扫描项目

```bash
python scripts/analyze_project.py
```

生成 `handoff/analysis-report.json`，包含：框架、包管理器、monorepo 配置、语言运行时版本、依赖清单、Docker、Cloudflare(wrangler)、CI/CD（GitHub Actions / GitLab CI / Jenkins）、Kubernetes、AI API 调用、环境变量（声明的 + 源码实际使用的 + 高熵值检测）、数据库、API 路由、Electron/Tauri/WinUI 桌面端、WSL 环境检测、MCP servers 配置、Claude Code skills/commands、开发平台痕迹、局域网启动配置、前端 mock、监控、目录结构、Git 信息。

### Step 2 — 阅读关键文件（不可省略）

打开 `analysis-report.json`，其中 `key_files_to_read` 列出了你必须实际阅读的文件（如 Dockerfile、wrangler.toml、主入口、CI 配置、已有 README）。逐个用 Read 工具阅读。**没读过这些文件就开始写文档，等于编造。**

**完成标准**：你必须能回答以下问题，否则不得进入 Step 3：
- 这个项目的业务目的是什么（给谁用、解决什么问题）
- 每个部署目标的真实命令和流程
- 每个环境变量在源码里的实际用途
- AI API 在哪些功能里被调用、用的什么模型

同时记录你在本次执行过程中实际使用了哪些**工具**，后续写入 ARCHITECTURE.md 的开发工具章节：

- **Skills**：你触发了哪些 skills（通过 `/skill-name` 或关键词自动触发）
- **MCP Servers**：你调用了哪些 MCP server（如 deepwiki、context7 等）
- **Agent 类型**：你委派了哪些子 agent（如 explore、executor 等）

这些信息无法被脚本静态扫描，只有你自己知道。

**验证方式**：在 Step 5 的 verify 中，如果你在文档中引用了 `文件路径:行号` 格式的内容，verify 会检查这些文件是否属于 `key_files_to_read` 列表。引用了未读文件的内容会被标记为 WARN。

### Step 3 — 生成骨架

```bash
python scripts/generate_handoff.py --client-level developer
```

可选级别：`non-technical` / `developer` / `devops`。生成的每份文档里包含 `<!-- TODO(AI): 具体填写指令 -->` 标记，每个标记自带填写说明。

### Step 4 — 补全所有 TODO（核心工作）

1. 读 `references/fill-guide.md`。
2. 逐文件、逐 TODO 处理。每个 TODO 的注释里写了"从哪里取信息、写成什么样"。
3. 写作标准：**具体命令优先于描述**。坏例子："配置环境变量"。好例子："在 Cloudflare Dashboard → Workers → Settings → Variables 中添加 `OPENAI_API_KEY`"。
4. 信息不足时使用 AskUserQuestion 向用户提问（域名、账号归属、联系人、已知问题等扫描不出来的内容），或标记 `[需向交接人确认: ...]`。

### Step 5 — 验收门禁

```bash
python scripts/verify_handoff.py
```

检查：残留 TODO、空章节、占位文本、必需文档缺失、文档数量、覆盖率。输出问题清单和待确认标记汇总。**有任何 FAIL 项就回到 Step 4 修复，循环直到通过。**

### Step 6 — 打包

```bash
python scripts/package_handoff.py
```

内部会先调用 verify，验收不通过会拒绝打包。通过后生成 `handoff/handoff-package.zip`。

## 文档清单

| 文件 | 内容 | 何时生成 |
|---|---|---|
| README.md | 项目是什么、给谁用、核心功能、技术栈、快速启动 | 总是 |
| ARCHITECTURE.md | 架构图(mermaid)、前后端分工、数据流、技术选型理由、monorepo 结构 | 总是 |
| ENVIRONMENT.md | 每个变量：用途/获取方式/必需性/泄露影响、高熵值警告 | 总是 |
| DEPLOYMENT.md | 按平台分章节的完整部署命令与流程（Docker/CF/CI/K8s） | 总是 |
| INFRASTRUCTURE.md | 域名/DNS/Cloudflare/SSL/第三方服务账号清单 | 总是 |
| AI-SERVICES.md | 调用的 AI API、用途、模型、计费、限流、降级 | 检测到 AI SDK/API |
| API.md | 接口清单、鉴权方式 | 检测到 API 路由 |
| DATABASE.md | 数据模型、迁移、备份恢复 | 检测到数据库 |
| DESKTOP.md | Electron/Tauri/WinUI 构建打包发布 | 检测到桌面端 |
| KNOWN-ISSUES.md | 已知问题、技术债、未完成功能 | 总是（主要靠问用户） |
| MAINTENANCE.md | 依赖更新、监控查看、日志位置 | 总是 |
| RUNBOOK.md | 回滚命令、故障→处置对照表、联系人 | 总是 |

## 配置文件

可选的 `.handoff.yml` 可覆盖默认行为：

```yaml
skip_dirs: ["testdata", "fixtures"]  # 追加到默认跳过目录
max_files: 5000                       # 最大扫描文件数
```

详见 `.handoff.yml.example`。

## References

- `references/fill-guide.md` — 每份文档的逐节填写标准与好/坏示例。Step 4 必读。
- `references/client-levels.md` — 三种受众的详略差异。
- `references/deployment-platforms.md` — 各平台部署文档要点。

## Scripts

- `scripts/analyze_project.py` — 扫描，输出 analysis-report.json
- `scripts/generate_handoff.py` — 生成带 TODO(AI) 的骨架
- `scripts/verify_handoff.py` — 质量门禁
- `scripts/package_handoff.py` — 验收后打包 ZIP

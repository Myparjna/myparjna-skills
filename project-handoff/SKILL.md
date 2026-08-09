---
name: project-handoff
description: "Create, inspect, incrementally update, compare, or explicitly rebuild complete project handoff documentation: usage guides, architecture and module maps, regression testing, deployment, environment variables, AI APIs, databases, native/embedded builds, local inference, known issues, and runbooks. Use for project delivery, team or AI-agent transitions, maintainer onboarding, or when the user says: 交接文档, 更新交接文档, 比对交接文档, 重建交接文档, 更新文档, 查看交接文档."
---

# Project Handoff

> 工具版本 3.0.0（schema 3）。为项目创建或增量更新完整的 `ProjectDoc/`。流程由“项目定位 + 事实扫描 + 新旧比对 + AI 语义更新 + 脚本验收”构成。

模式语义必须严格区分：`更新交接文档`/`更新文档` 默认是**增量更新**，先给出比对建议，再原地修改受影响章节；只有用户明确说 `重建交接文档`、`重新生成交接文档` 或同意完全重置时，才能使用 `--mode rebuild`。没有旧文档时使用首次创建模式。

## 硬性规则（MUST）

1. **禁止跳步。** 必须按 Step 0 → 7 顺序执行。
2. **禁止编造。** 所有内容必须来自：扫描报告 `analysis-report.json`、你实际读过的源码文件、或用户的明确回答。不确定的内容写 `[需向交接人确认: 具体问题]`，不许猜。
3. **禁止留空。** 每个 `TODO(AI)` 必须被处理：要么填入真实内容，要么改写为 `[需向交接人确认: ...]`。
4. **`verify_handoff.py` 不通过，禁止交付。** 这是质量门禁，没有例外。
5. 填写前必须先读技能目录下的 `fill-guide.md`，按其中的逐文件标准执行。
6. **增量更新禁止重写未受影响文档。** 旧文档中的人工决策、业务约定和运维经验默认保留。
7. **禁止把“检测到测试”写成“测试通过”。** 只有实际执行并观察结果的测试才能记为通过。

## 运行位置说明

这个 skill 可能是项目内置的，也可能安装在 Claude Code / Codex / Cursor 的全局 skills 目录。**所有脚本都要在目标项目根目录执行**，这样输出才会写入目标项目的 `ProjectDoc/`。

- 如果 skill 已复制到目标项目根目录，可直接运行 `python scripts/<script>.py`。
- 如果 skill 是全局安装的，先确认本 skill 的实际目录（即包含本 `SKILL.md` 的目录），再在目标项目根目录运行：

```bash
python /absolute/path/to/project-handoff/scripts/analyze_project.py
python /absolute/path/to/project-handoff/scripts/compare_handoff.py
python /absolute/path/to/project-handoff/scripts/generate_handoff.py --mode update --client-level developer
python /absolute/path/to/project-handoff/scripts/verify_handoff.py
```

Windows PowerShell 示例：

```powershell
python "C:\absolute\path\to\project-handoff\scripts\analyze_project.py"
```

## Workflow

### Step 0 — 先定位项目根目录和历史交接文档

启动目录不一定就是项目根目录，也可能是包含多个项目的工作区。正式扫描前必须先运行：

```bash
python /absolute/path/to/project-handoff/scripts/discover_project.py --start . --max-depth 3
```

脚本只输出候选，不替 AI 做最终选择。AI 必须检查候选的项目标志、路径、已有 `ProjectDoc`/`project-handoff`/`handoff` 目录、文档数量、`analysis-report.json` 是否存在，以及各目录的最新修改时间，然后选择一个真正的项目根目录：

- 只有一个明显候选时直接选它。
- 旧交接文档的修改时间只能作为线索，不能单独决定覆盖哪个目录。
- 同一工作区有多个项目或多个同名交接目录时，必须向用户确认目标项目，禁止扫描父工作区。
- 选定项目根目录已有 `ProjectDoc/` 时更新它，没有则在该根目录下创建。

选定后，Step 1 至 Step 7 都必须在选定的项目根目录执行。发现报告可以用 `--output` 保存到临时位置，但不能把它当成交接文档。

### Step 1 — 判断模式

- 没有旧 `ProjectDoc/*.md`：`create`。
- 用户说“更新”：`update`，不得清理旧文档。
- 用户明确要求完全重置：`rebuild`；生成器会先备份旧目录到 `TempFiles/ProjectDoc_backup_<时间>/`。

### Step 2 — 扫描项目并保留基线

```bash
python /absolute/path/to/project-handoff/scripts/analyze_project.py
```

生成 `ProjectDoc/analysis-report.json`，包含：框架、包管理器、monorepo 配置、语言运行时版本、依赖清单、Docker、Cloudflare(wrangler)、CI/CD（GitHub Actions / GitLab CI / Jenkins / CircleCI）、Kubernetes、Vercel/Netlify/VPS 部署痕迹、AI API 调用、环境变量（声明的 + 源码实际使用的 + 高熵值检测，真实 env 文件的值自动脱敏）、数据库（含 Cloudflare D1）、API 路由与 OpenAPI/Swagger 规范、Electron/Tauri/WinUI 桌面端、Go/Rust/Java/.NET/C/C++ 构建入口、嵌入式工程线索、本地推理引擎/模型文件、WSL 环境检测、MCP servers 配置、Claude Code skills/commands、AGENTS.md/GEMINI.md 等开发平台痕迹、局域网启动配置、前端 mock、监控、目录结构、Git 信息。

更新时，扫描器以最近一次验收通过的 `ProjectDoc/.handoff/analysis-report.verified.json` 为稳定基线，生成 `analysis-report.previous.json` 后再写入新报告；重复扫描不会推进基线。报告同时记录关键文件 SHA-256，供增量比对。

### Step 3 — 生成并审阅更新建议

```bash
python /absolute/path/to/project-handoff/scripts/compare_handoff.py
```

生成 `TempScr/project-handoff-update-plan.md` 和 `.json`。脚本负责报告字段、关键文件和文档缺失情况的客观比较；AI 必须结合旧文档与源码补充语义影响。先向用户简要展示建议，再继续修改。`preserve` 文档不重写，`review` 文档先判断，`update` 文档只改受影响章节。

### Step 4 — 阅读关键文件和旧文档（不可省略）

打开 `analysis-report.json`，其中 `key_files_to_read` 列出了你必须实际阅读的文件（如 Dockerfile、wrangler.toml、主入口、CI 配置、已有 README）。逐个用 Read 工具阅读。**没读过这些文件就开始写文档，等于编造。**

**完成标准**：你必须能回答以下问题，否则不得进入 Step 5：
- 这个项目的业务目的是什么（给谁用、解决什么问题）
- 每个部署目标的真实命令和流程
- 每个环境变量在源码里的实际用途
- AI API 在哪些功能里被调用、用的什么模型

同时记录你在本次执行过程中实际使用了哪些**工具**，后续写入 ARCHITECTURE.md 的开发工具章节：

- **Skills**：你触发了哪些 skills（通过 `/skill-name` 或关键词自动触发）
- **MCP Servers**：你调用了哪些 MCP server（如 deepwiki、context7 等）
- **Agent 类型**：你委派了哪些子 agent（如 explore、executor 等）

这些信息无法被脚本静态扫描，只有你自己知道。

**验证方式**：在 Step 7 的 verify 中，文档里用反引号引用的源码文件路径必须真实存在，或在 `key_files_to_read` 清单中（兼容相对根写法差异）；引用不存在或编造的路径会被标记为 WARN。

### Step 5 — 创建、补齐或重建骨架

```bash
python /absolute/path/to/project-handoff/scripts/generate_handoff.py --mode update --client-level developer
```

模式：`create` 首次创建；`update` 只创建缺失文档并保留已有文档；`rebuild` 备份后重建所有生成文档；默认 `auto` 会根据是否存在旧文档选择 create/update。可选受众：`non-technical` / `developer` / `devops`。

### Step 6 — 增量修改或补全 TODO（核心工作）

1. 读技能目录下的 `fill-guide.md`。
2. 逐文件、逐 TODO 处理。每个 TODO 的注释里写了"从哪里取信息、写成什么样"。
3. 写作标准：**具体命令优先于描述**。坏例子："配置环境变量"。好例子："在 Cloudflare Dashboard → Workers → Settings → Variables 中添加 `OPENAI_API_KEY`"。
4. 信息不足时，使用当前 agent 环境提供的提问能力向用户确认（例如直接在对话中提问、调用可用的用户输入工具、或按平台约定发起澄清）；如果当前流程不能等待用户回答，就标记 `[需向交接人确认: ...]`。不要写特定平台才有的工具名。

更新模式下，按更新建议直接编辑旧文档的受影响章节；新增文档则补全全部 TODO。不得用重新生成的骨架整体替换旧人工内容。

### Step 7 — 验收门禁

```bash
python /absolute/path/to/project-handoff/scripts/verify_handoff.py
```

检查：残留 TODO、空章节、缺失的骨架核心章节（防删章节绕过）、占位文本、必需文档缺失、文档数量、密钥泄露（示例/掩码值降级为 WARN）、文件引用真实性、覆盖率。输出问题清单和待确认标记汇总。**有任何 FAIL 项就回到 Step 6 修复，循环直到通过。**
通过后直接交付 `ProjectDoc/` 目录中的文档，不再生成 ZIP 包。

## 文档清单

| 文件 | 内容 | 何时生成 |
|---|---|---|
| README.md | 项目是什么、给谁用、核心功能、技术栈、快速启动 | 总是 |
| USAGE.md | 用户角色、入口、核心业务流程、输入输出、权限与常见问题 | 总是 |
| ARCHITECTURE.md | 架构图(mermaid)、前后端分工、数据流、技术选型理由、monorepo 结构 | 总是 |
| MODULES.md | 模块职责、入口、依赖、调用链、共享状态、扩展点 | 总是 |
| ENVIRONMENT.md | 每个变量：用途/获取方式/必需性/泄露影响、高熵值警告 | 总是 |
| DEPLOYMENT.md | 按平台分章节的完整部署命令与流程（Docker/CF/CI/CircleCI/K8s/Vercel/Netlify/VPS） | 总是 |
| INFRASTRUCTURE.md | 域名/DNS/Cloudflare/SSL/第三方服务账号清单 | 总是 |
| AI-SERVICES.md | 调用的 AI API、用途、模型、计费、限流、降级 | 检测到 AI SDK/API |
| API.md | 接口清单、鉴权方式 | 检测到 API 路由 |
| DATABASE.md | 数据模型、迁移、备份恢复 | 检测到数据库 |
| DESKTOP.md | Electron/Tauri/WinUI 构建打包发布 | 检测到桌面端 |
| REGRESSION-TEST.md | 自动化与人工回归范围、命令、结果、证据、测试缺口 | 总是 |
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

- `fill-guide.md` — 每份文档的逐节填写标准与好/坏示例。Step 6 必读。
- `references/client-levels.md` — 三种受众的详略差异。
- `references/deployment-platforms.md` — 各平台部署文档要点。

## Scripts

- `scripts/discover_project.py` — 发现候选项目根目录和历史交接文档，供 AI 决策
- `scripts/analyze_project.py` — 扫描，输出 analysis-report.json
- `scripts/compare_handoff.py` — 比较新旧扫描报告并生成增量更新建议
- `scripts/generate_handoff.py` — 按 create/update/rebuild 模式生成或补齐骨架
- `scripts/verify_handoff.py` — 质量门禁
- `scripts/_handoff_common.py` — 脚本公共工具（UTF-8 控制台等）

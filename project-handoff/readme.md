# project-handoff

为即将交接的项目生成完整、可验证的交接文档。基于源码静态分析提取事实，AI 只负责组织和补充说明，杜绝编造。

当前版本：**3.1.1**（analysis-report schema 3）。

触发词：`交接文档`、`更新交接文档`、`更新文档`、`查看交接文档`、`project handoff`、`handoff docs`。

说明：当前版本默认增量更新。它先保留旧扫描基线、生成新旧比对建议，再原地修改受影响章节；只有明确使用 `--mode rebuild` 才会备份并重建生成文档。

## 适用场景

- 离职 / 换岗前移交个人维护的项目
- 外包项目交付
- 把个人 side project 转给团队
- AI agent 交接项目上下文

## 工作流程（9 步）

```
定位项目 → 判断模式 → 扫描并保留基线 → 生成计划并交用户确认
       → 生成比对建议（含 git 变更） → 阅读旧文档和变更源码
       → 创建/补齐骨架 → AI 原地增量修改 → 质量门禁
```

### 步骤详解

```bash
# 0. 从启动目录发现候选项目和历史 ProjectDoc，先由 AI 选择项目根目录
python /absolute/path/to/project-handoff/scripts/discover_project.py --start . --max-depth 3
# 1. 判断 create/update/rebuild 模式
# 2. 切换到选定的项目根目录后运行分析；旧报告会自动保留为比对基线
# 如果本 skill 是全局安装的，把下面路径替换成 project-handoff skill 的实际目录
python /absolute/path/to/project-handoff/scripts/analyze_project.py
# 产出 ProjectDoc/analysis-report.json

# 3. 生成交接计划：模式判定 + 文档生成/跳过清单 + 每份 focus + 扫描范围
python /absolute/path/to/project-handoff/scripts/plan_handoff.py
# 产出 TempScr/project-handoff-plan.md 和 .json；向用户展示并确认后再继续
# 用户可直接编辑 plan 文件；generate 会自动读取并尊重 skip 决策

# 4. 生成机器差异和文档更新建议（含自上次验收基线以来的 git commit 列表与变更文件统计）
python /absolute/path/to/project-handoff/scripts/compare_handoff.py
# 产出 TempScr/project-handoff-update-plan.md 和 .json

# 5. AI 阅读旧文档和 key_files_to_read 中变化的关键文件（不可省略）
#    理解项目业务目的、部署流程、环境变量用途、AI API 调用方式

# 6. 更新模式只补齐缺失文档；已有文档保持原样
python /absolute/path/to/project-handoff/scripts/generate_handoff.py --mode update --client-level developer

# 7. AI 按更新建议原地修改受影响章节，并补全新增文档中的 TODO(AI)
#    不确定的内容标记为 [需向交接人确认: 具体问题]

# 8. 质量门禁
python /absolute/path/to/project-handoff/scripts/verify_handoff.py
# 退出码 0=通过  1=有 ERROR  2=检测到密钥泄露

# verify 通过后，直接交付 ProjectDoc/ 目录中的文档
```

## 产出文档

| 文件 | 内容 |
|---|---|
| `ProjectDoc/analysis-report.json` | 静态分析事实清单（机器可读） |
| `ProjectDoc/README.md` | 项目概览、技术栈、快速启动、速查卡（30 秒应急速览） |
| `ProjectDoc/USAGE.md` | 用户角色、入口和核心使用流程 |
| `ProjectDoc/ARCHITECTURE.md` | 架构图、目录结构、技术选型 |
| `ProjectDoc/MODULES.md` | 模块职责、入口、依赖和关键调用链 |
| `ProjectDoc/ENVIRONMENT.md` | 全部环境变量说明、高熵值警告 |
| `ProjectDoc/DEPLOYMENT.md` | Docker/Cloudflare/CI/K8s 部署 |
| `ProjectDoc/INFRASTRUCTURE.md` | 域名、账号、第三方服务 |
| `ProjectDoc/KNOWN-ISSUES.md` | 已知 Bug、技术债 |
| `ProjectDoc/MAINTENANCE.md` | 日常维护、监控 |
| `ProjectDoc/RUNBOOK.md` | 故障处置手册 |
| `ProjectDoc/REGRESSION-TEST.md` | 回归范围、执行命令、结果证据和测试缺口 |
| `ProjectDoc/AI-SERVICES.md` | AI API 使用详情（条件生成） |
| `ProjectDoc/API.md` | 接口清单（条件生成） |
| `ProjectDoc/DATABASE.md` | 数据库文档（条件生成） |
| `ProjectDoc/DESKTOP.md` | 桌面端文档（条件生成） |

## 设计原则

1. **事实与解释分离**：脚本负责提取事实（环境变量、依赖、CI secrets、云绑定），AI 只解释和组织。文档中每个关键事实都由 verify 反向校验覆盖率。
2. **不知道 ≠ 编一个**：`[需向交接人确认: ...]` 是唯一合法的存疑写法，门禁对含糊措辞（"视情况而定"、"此处略"、占位符）直接报警。
3. **密钥零容忍**：verify 用高置信度正则扫描真实密钥特征（sk-、ghp_、AKIA、私钥块等），命中即 CRITICAL，禁止交付；示例值/掩码命中时降级为 WARN 供人工确认。同时检测 .env 文件中的高熵值。文档只写密钥的名称、用途、获取方式和交接渠道。
4. **防删章节绕过**：verify 内置骨架核心章节清单，删除章节逃避 TODO 检查会被 ERROR 拦截。
5. **规划先行**：plan_handoff.py 先判定模式、列出文档生成/跳过清单与每份 focus，交用户确认后才生成。小项目可跳过非必需文档，避免被迫产出大量薄文档；大项目的特殊主题（合规、多租户等）记入计划 focus。
6. **git 变更信号**：compare 输出自上次验收基线以来的 commit 列表与变更文件统计（以基线记录的 commit hash 为范围），与报告字段 diff/文件指纹互补，为 AI 语义判断提供素材。

## 支持的技术栈检测

| 类别 | 检测范围 |
|---|---|
| **包管理** | npm / pnpm / yarn / bun / uv / pipenv / poetry |
| **Monorepo** | pnpm-workspace / npm-workspaces / Turborepo / Nx / Lerna |
| **框架** | Next.js / Nuxt / Vite / React / Vue / Svelte / Astro / Express / NestJS / FastAPI / Flask / Django / Streamlit / Gradio |
| **UI 库** | Ant Design / TDesign / Element Plus / Naive UI / MUI / shadcn 等 20+ 种 |
| **桌面端** | Electron / Tauri / WinUI 3 / WPF / WinForms |
| **容器** | Dockerfile / Docker Compose / Kubernetes |
| **CI/CD** | GitHub Actions / GitLab CI / Jenkins / CircleCI |
| **部署平台** | Vercel / Netlify / VPS（systemd/pm2/nginx/supervisor）痕迹 |
| **云服务** | Cloudflare Workers/Pages (KV/D1/R2) |
| **AI 服务** | OpenAI / Anthropic / Gemini / DashScope / 智谱 / DeepSeek / Ollama 等 SDK 和端点 |
| **数据库** | PostgreSQL / MySQL / SQLite / MongoDB / Redis / Cloudflare D1 + Prisma / Drizzle / TypeORM / SQLAlchemy |
| **原生/后端语言** | Go / Rust / Java/JVM / .NET manifest 与构建入口 |
| **C/C++ 构建** | CMake / Makefile / Meson / Bazel 线索、GCC/Clang/交叉编译工具链关键词 |
| **嵌入式** | PlatformIO / STM32CubeMX(.ioc) / Keil(.uvprojx) / IAR(.ewp) / linker script / FreeRTOS / Zephyr / ESP-IDF / CMSIS |
| **本地推理** | YOLO / ONNX Runtime / TensorRT / OpenVINO / ncnn / MNN / TFLite / RKNN / OpenCV DNN / Darknet / TVM / llama.cpp/ggml |
| **环境变量** | .env 系列文件声明 vs 源码使用交叉分析、高熵值检测（真实 env 文件值自动脱敏） |
| **外部资源** | HuggingFace / ModelScope 模型、GitHub 直装依赖、CDN 链接 |
| **API 规范** | OpenAPI / Swagger 规范文件 |
| **WSL** | WSL1/WSL2 版本、发行版检测 |
| **MCP Servers** | Claude Code MCP servers 配置（项目级 + 用户级 + .mcp.json） |
| **AI 开发配置** | Claude Code / Codex(AGENTS.md) / Gemini(GEMINI.md) / Cursor 等痕迹，项目级 skills/commands + 全局 skills（~/.claude/skills、~/.agents/skills） |

## 配置

可选的 `.handoff.yml` 文件可覆盖默认扫描行为：

```yaml
skip_dirs: ["testdata", "fixtures"]  # 追加到默认跳过目录
max_files: 5000                       # 最大扫描文件数（默认 3000）
```

## 局限

- **深度解析仍以 JS/TS + Python + .NET 为主**。Go、Rust、Java、C/C++、嵌入式和本地推理项目会检测 manifest、构建入口、工具链和关键线索，但不会完整解析所有依赖图、编译选项和板卡 BSP
- 静态分析覆盖不到的内容（账号归属、口头约定、历史决策）依赖交接人回答待确认问题
- 动态生成的环境变量名（如 `process.env[key]`）无法检测
- 仅扫描常见密钥格式，verify 通过不代表绝对无泄露，交付前仍建议人工过一遍 ENVIRONMENT 和 INFRASTRUCTURE 文档

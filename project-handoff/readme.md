# project-handoff

为即将交接的项目生成完整、可验证的交接文档。基于源码静态分析提取事实，AI 只负责组织和补充说明，杜绝编造。

## 适用场景

- 离职 / 换岗前移交个人维护的项目
- 外包项目交付
- 把个人 side project 转给团队
- AI agent 交接项目上下文

## 工作流程（6 步）

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ 1. 静态分析       │    │ 2. 阅读关键文件    │    │ 3. 生成骨架        │
│ analyze_project │ →  │ 读 key_files     │ →  │ generate_handoff │
│ → 事实清单(json) │    │ → 理解项目背景     │    │ → 8-12 份带 TODO  │
└─────────────────┘    └──────────────────┘    └────────┬────────┘
                                                        │
┌─────────────────┐    ┌──────────────────┐             ↓
│ 6. 打包交付        │    │ 5. 质量门禁        │    ┌─────────────────┐
│ package_handoff  │ ←  │ verify_handoff  │ ←  │ 4. AI 填写        │
│ → ZIP（含验证）    │    │ → 检查覆盖率      │    │ 按 fill-guide    │
└─────────────────┘    └──────────────────┘    │ 填 TODO(AI)      │
                                                └─────────────────┘
```

### 步骤详解

```bash
# 1. 在目标项目根目录运行分析（只读，不修改项目文件）
# 如果本 skill 是全局安装的，把下面路径替换成 project-handoff skill 的实际目录
python /absolute/path/to/project-handoff/scripts/analyze_project.py
# 产出 ProjectDoc/analysis-report.json

# 2. AI 阅读 key_files_to_read 中列出的关键文件（不可省略）
#    理解项目业务目的、部署流程、环境变量用途、AI API 调用方式

# 3. 生成文档骨架（带 TODO(AI) 标记）
python /absolute/path/to/project-handoff/scripts/generate_handoff.py --client-level developer
# 产出 ProjectDoc/README.md ~ ProjectDoc/RUNBOOK.md

# 4. AI（或人）按 skill 目录下的 fill-guide.md 填写所有 TODO(AI)
#    不确定的内容标记为 [需向交接人确认: 具体问题]

# 5. 质量门禁
python /absolute/path/to/project-handoff/scripts/verify_handoff.py
# 退出码 0=通过  1=有 ERROR  2=检测到密钥泄露

# 6. 打包（内部先验证，不通过则拒绝）
python /absolute/path/to/project-handoff/scripts/package_handoff.py
# 产出 ProjectDoc/ProjectDoc-package.zip
```

## 产出文档

| 文件 | 内容 |
|---|---|
| `ProjectDoc/analysis-report.json` | 静态分析事实清单（机器可读） |
| `ProjectDoc/README.md` | 项目概览、技术栈、快速启动 |
| `ProjectDoc/ARCHITECTURE.md` | 架构图、目录结构、技术选型 |
| `ProjectDoc/ENVIRONMENT.md` | 全部环境变量说明、高熵值警告 |
| `ProjectDoc/DEPLOYMENT.md` | Docker/Cloudflare/CI/K8s 部署 |
| `ProjectDoc/INFRASTRUCTURE.md` | 域名、账号、第三方服务 |
| `ProjectDoc/KNOWN-ISSUES.md` | 已知 Bug、技术债 |
| `ProjectDoc/MAINTENANCE.md` | 日常维护、监控 |
| `ProjectDoc/RUNBOOK.md` | 故障处置手册 |
| `ProjectDoc/AI-SERVICES.md` | AI API 使用详情（条件生成） |
| `ProjectDoc/API.md` | 接口清单（条件生成） |
| `ProjectDoc/DATABASE.md` | 数据库文档（条件生成） |
| `ProjectDoc/DESKTOP.md` | 桌面端文档（条件生成） |

## 设计原则

1. **事实与解释分离**：脚本负责提取事实（环境变量、依赖、CI secrets、云绑定），AI 只解释和组织。文档中每个关键事实都由 verify 反向校验覆盖率。
2. **不知道 ≠ 编一个**：`[需向交接人确认: ...]` 是唯一合法的存疑写法，门禁对含糊措辞（"视情况而定"、"此处略"、占位符）直接报警。
3. **密钥零容忍**：verify 用高置信度正则扫描真实密钥特征（sk-、ghp_、AKIA、私钥块等），命中即 CRITICAL，禁止交付。同时检测 .env 文件中的高熵值。文档只写密钥的名称、用途、获取方式和交接渠道。

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
| **云服务** | Cloudflare Workers/Pages (KV/D1/R2) |
| **AI 服务** | OpenAI / Anthropic / Gemini / DashScope / 智谱 / DeepSeek / Ollama 等 SDK 和端点 |
| **数据库** | PostgreSQL / MySQL / SQLite / MongoDB / Redis + Prisma / Drizzle / TypeORM / SQLAlchemy |
| **原生/后端语言** | Go / Rust / Java/JVM / .NET manifest 与构建入口 |
| **C/C++ 构建** | CMake / Makefile / Meson / Bazel 线索、GCC/Clang/交叉编译工具链关键词 |
| **嵌入式** | PlatformIO / STM32CubeMX(.ioc) / Keil(.uvprojx) / IAR(.ewp) / linker script / FreeRTOS / Zephyr / ESP-IDF / CMSIS |
| **本地推理** | YOLO / ONNX Runtime / TensorRT / OpenVINO / ncnn / MNN / TFLite / RKNN / OpenCV DNN / Darknet / TVM / llama.cpp/ggml |
| **环境变量** | .env 文件声明 vs 源码使用交叉分析、高熵值检测 |
| **外部资源** | HuggingFace / ModelScope 模型、GitHub 直装依赖、CDN 链接 |
| **WSL** | WSL1/WSL2 版本、发行版检测 |
| **MCP Servers** | Claude Code MCP servers 配置（项目级 + 用户级 + .mcp.json） |
| **Claude Skills** | 项目级 skills/commands + 全局 skills（~/.claude/skills、~/.agents/skills） |

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

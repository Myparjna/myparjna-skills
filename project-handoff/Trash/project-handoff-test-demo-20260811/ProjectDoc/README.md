---
document: README.md
generated: 2026-08-11 15:52
client_level: developer
---

# demo-project — 项目交接文档

## 待确认问题

[需向交接人确认：DEEPSEEK 账号归属？]

<!-- TODO(AI): 把本文档集内所有 `[需向交接人确认: ...]` 标记汇总到这里，每条一行；得到答复后同步更新对应正文并保留状态。没有时写'当前无待确认问题'。 -->

## 项目简介

<!-- TODO(AI): 用 2-4 句话说明：这个项目是什么、给谁用、解决什么问题。来源：已有 README、主页面源码、向用户提问。禁止只罗列技术栈。 -->

## 核心功能

<!-- TODO(AI): 列出 3-8 个核心功能点，每个一行。来源：阅读路由/页面结构 + 已有 README。格式：'- 功能名：一句话说明' -->

## 技术栈

**框架**: Vite ^5.0.0, React ^18.3.0

**UI 组件库**: 无

**包管理器**: npm (inferred, no lockfile)

**依赖规模**: Node 6 个 / Python 0 个

<!-- TODO(AI): 补充语言运行时版本要求（Node/Python 具体版本，从 package.json engines、.nvmrc、pyproject 中找；找不到写 [需向交接人确认: Node 版本要求]） -->

## 快速启动

```bash
<!-- TODO(AI): 写出从 git clone 到本地跑起来的完整命令序列，逐条验证可行性（依据 npm_scripts 和 README）。包含：安装依赖、复制 .env、启动命令、访问地址 -->
```

**可用脚本**:
| 命令 | 用途 |
|---|---|
| `dev` | <!-- TODO(AI): 解释用途 --> |
| `build` | <!-- TODO(AI): 解释用途 --> |
| `test` | <!-- TODO(AI): 解释用途 --> |

## 速查卡

| 项目 | 值 | 出处/说明 |
|---|---|---|
| 本地访问地址 | <!-- TODO(AI): 端口和 URL，从启动配置/运行验证中获取 --> | 启动后实际访问入口 |
| 生产访问入口 | <!-- TODO(AI): 生产 URL 或运行位置；未知写 [需向交接人确认: 生产入口] --> | 用户/部署平台 |
| 启动一行命令 | <!-- TODO(AI): 从快速启动中提炼最核心的一条命令 --> | 快速启动 |
| 部署一行命令 | <!-- TODO(AI): 如 wrangler deploy / docker compose up -d / vercel --prod；详见 DEPLOYMENT.md --> | DEPLOYMENT.md |
| 回滚一行命令 | <!-- TODO(AI): 如 wrangler rollback / 重部署上一 tag；详见 RUNBOOK.md --> | RUNBOOK.md |
| 日志/监控入口 | <!-- TODO(AI): 看错误和用量的精确入口路径；详见 MAINTENANCE.md --> | MAINTENANCE.md |

<!-- TODO(AI): 速查卡要求：出事时 30 秒能扫完。每格只放具体值（URL/端口/一行命令/人名），禁止长句和概念描述；细节放对应文档。 -->

## 文档导航

| 文档 | 内容 |
|---|---|
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 架构与技术选型 |
| [USAGE.md](./USAGE.md) | 项目使用说明与业务流程 |
| [MODULES.md](./MODULES.md) | 模块职责、入口与依赖 |
| [REGRESSION-TEST.md](./REGRESSION-TEST.md) | 回归测试范围与验证记录 |
| [ENVIRONMENT.md](./ENVIRONMENT.md) | 环境变量 |
| [DEPLOYMENT.md](./DEPLOYMENT.md) | 部署 |
| [INFRASTRUCTURE.md](./INFRASTRUCTURE.md) | 域名/账号/第三方服务 |
| [KNOWN-ISSUES.md](./KNOWN-ISSUES.md) | 已知问题 |
| [MAINTENANCE.md](./MAINTENANCE.md) | 日常维护 |
| [RUNBOOK.md](./RUNBOOK.md) | 故障处置 |
| [AI-SERVICES.md](./AI-SERVICES.md) | AI API 使用详情 |
| [API.md](./API.md) | 接口清单 |
| [DATABASE.md](./DATABASE.md) | 数据库 |

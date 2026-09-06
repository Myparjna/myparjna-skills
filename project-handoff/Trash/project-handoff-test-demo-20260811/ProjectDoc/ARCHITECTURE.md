---
document: ARCHITECTURE.md
generated: 2026-08-11 15:52
client_level: developer
---

# 系统架构

## 架构总览

```mermaid
<!-- TODO(AI): 画出系统架构图：前端、后端、数据库、外部 AI API、部署平台之间的调用关系。依据 analysis-report 中的 frameworks/docker/cloudflare/ai_services/database -->
```

<!-- TODO(AI): 用一段话解释数据流向：用户请求从哪进来、经过什么、数据存到哪 -->

## 目录结构

```
[DIR] prisma
  [DIR] migrations
    [DIR] 20240101_init
  schema.prisma
[DIR] src
  index.js
AGENTS.md
Dockerfile
README.md
netlify.toml
openapi.json
package.json
wrangler.toml
```

<!-- TODO(AI): 为上面树中 5-10 个关键目录各加一行用途说明 -->

## 技术选型与路线

<!-- TODO(AI): 说明关键技术为什么这么选（如有历史原因或曾经换过方案，向用户提问后记录）。来源：CLAUDE.md、git log、向用户提问。不知道就写 [需向交接人确认: 技术选型背景] -->

## 外部资源依赖

未检测到外部模型/CDN 资源。

<!-- TODO(AI): 核对 external_resources 中的 github_urls 和 huggingface_urls，把属于'运行必需'的资源补进上表，纯文档引用的忽略 -->

## 局域网访问

检测到绑定 0.0.0.0 / --host 的配置：
- package.json: dev = vite --host

<!-- TODO(AI): 说明：哪个命令以局域网模式启动、默认端口、防火墙注意事项、是否仅限开发环境 -->

## AI 工具链

**全局 skills（目录扫描，共 109 个）**: agent-skills, ai-image-prompts, amap-cli-skill, amap-jsapi-skill, amap-lbs-skill, anysearch, app-screenshot-batch-doc, arco-design, better-icons, brainstorming...

<!-- TODO(AI): 你在执行本技能的过程中实际使用了哪些 skills、MCP servers、子 agent？逐个列出名称和用途。这些信息无法被脚本静态扫描，只有执行此技能的 AI 自己知道。格式：'- **skill 名称**: 用途' / '- **MCP server**: 用途' / '- **Agent 类型**: 用途' -->

## 开发环境痕迹

检测到的开发工具: {"Codex / AGENTS.md": ["AGENTS.md"]}

操作系统线索: 不明

<!-- TODO(AI): 说明原开发平台（Windows/macOS/Linux/WSL）和所用 AI 工具，以及接手方是否需要这些配置 -->

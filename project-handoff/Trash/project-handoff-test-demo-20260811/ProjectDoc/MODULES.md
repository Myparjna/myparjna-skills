---
document: MODULES.md
generated: 2026-08-11 15:52
client_level: developer
---

# 模块说明

## 模块总览

```mermaid
<!-- TODO(AI): 画出核心模块依赖图，标明调用方向；不要重复 ARCHITECTURE 的部署架构图。 -->
```

<!-- TODO(AI): 用一段话说明模块边界和主执行链路。 -->

## 模块职责矩阵

| 模块 | 职责 | 入口文件 | 上游 | 下游 | 关键配置 | 测试 |
|---|---|---|---|---|---|---|
| <!-- TODO(AI): 逐个列出核心业务模块，而不是逐文件罗列 --> |  |  |  |  |  |  |

## 关键目录

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

<!-- TODO(AI): 从目录树中选择核心目录，说明其职责、所有权边界以及不能随意修改的约束。 -->

## 关键调用链

<!-- TODO(AI): 按真实源码描述 2-5 条关键调用链，格式：入口 -> 业务模块 -> 数据/外部服务 -> 输出，并给出文件路径。 -->

## 共享状态与数据边界

<!-- TODO(AI): 说明模块之间共享的数据库表、缓存、文件、消息、全局状态或硬件资源；指出并发和生命周期约束。 -->

## 扩展与替换点

<!-- TODO(AI): 说明新增功能通常改哪些模块、已有插件/适配器接口、模型或硬件后端如何替换。没有正式扩展点时如实说明。 -->

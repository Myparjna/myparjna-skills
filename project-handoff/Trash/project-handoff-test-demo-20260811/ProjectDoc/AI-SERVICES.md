---
document: AI-SERVICES.md
generated: 2026-08-11 15:52
client_level: developer
---

# AI 服务

## 使用的 SDK

| SDK | 包 | 用途 |
|---|---|---|
| OpenAI SDK | `openai@^4.50.0` | <!-- TODO(AI): 在哪个功能中使用？读调用处源码 --> |

## API 端点

| 端点 | 出现位置 | 功能 |
|---|---|---|
| `https://api.openai.com/v1/chat/completions` | src/index.js | <!-- TODO(AI): 对应什么功能 --> |

## 模型

源码中出现的模型名: `gpt-4o-mini`

<!-- TODO(AI): 说明每个模型用于什么功能、能否替换为其他模型、替换时要改哪个文件哪一行 -->

## 计费与限额

<!-- TODO(AI): 逐个 AI 服务说明：计费方式（按 token/按次）、当前账号的限流等级、大致月消耗（向用户问）、余额告警在哪设置 -->

## 降级与故障

<!-- TODO(AI): 说明：AI API 不可用时系统表现如何？有无重试/超时/降级逻辑？读调用处源码确认，没有就如实写'无降级逻辑，API 故障时功能 X 不可用' -->

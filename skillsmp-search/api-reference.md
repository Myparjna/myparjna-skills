# SkillsMP API 参考

## 基础信息

- **Base URL**: `https://skillsmp.com/api/v1/skills`
- **认证**: `Authorization: Bearer <API_KEY>`
- **API Key**: 已内置到 search.py（优先读取环境变量 `SKILLSMP_API_KEY`）

## 速率限制

| 访问方式 | 日配额 | 分钟限制 |
|---------|--------|---------|
| 匿名（无 API Key） | 50 次/天 | 10 次/分钟（仅关键字搜索） |
| 认证（API Key） | 500 次/天 | 30 次/分钟（全部端点） |

响应头追踪配额：
- `X-RateLimit-Daily-Limit` — 每日上限
- `X-RateLimit-Daily-Remaining` — 当日剩余

## 端点

### GET /search — 关键字搜索

| 参数 | 类型 | 必需 | 说明 |
|------|------|------|------|
| q | string | ✓ | 搜索关键字 |
| page | number | - | 页码（默认 1） |
| limit | number | - | 每页数量（默认 20，最大 100） |
| sortBy | string | - | `stars` 或 `recent`（默认 recent） |
| category | string | - | 分类 slug（如 data-ai、devops） |
| occupation | string | - | SOC 职业 slug（如 software-developers-151252） |

### GET /ai-search — AI 语义搜索

| 参数 | 类型 | 必需 | 说明 |
|------|------|------|------|
| q | string | ✓ | 自然语言查询 |

## 错误处理

| 错误码 | HTTP | 说明 |
|--------|------|------|
| MISSING_API_KEY | 401 | AI 搜索需要 API Key |
| INVALID_API_KEY | 401 | API Key 无效 |
| MISSING_QUERY | 400 | 缺少 q 参数 |
| DAILY_QUOTA_EXCEEDED | 429 | 超出每日配额 |
| INTERNAL_ERROR | 500 | 服务端内部错误 |

## 常见分类 slug

- `devops` — 运维部署
- `data-ai` — 数据与 AI
- `productivity` — 生产力工具
- `development` — 开发工具
- `design` — 设计类
- `marketing` — 营销类

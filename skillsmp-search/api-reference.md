# SkillsMP API 参考

## 基础信息

- **Base URL**: `https://skillsmp.com/api/v1/skills`
- **认证**: `Authorization: Bearer <API_KEY>`
- **API Key**: 不再内置；优先读取环境变量 `SKILLSMP_API_KEY`，否则读取下述本机配置

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

### ai 兼容入口

`--mode ai` 与 keyword 共用 `/search`，page、limit、排序、筛选参数一致；输出 `mode` 始终为 `keyword`。

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

## 本机配置与错误

凭据读取顺序：非空 `SKILLSMP_API_KEY` 环境变量 → 本机 JSON 配置的 `api_key` 字段。Windows 路径为 `%APPDATA%/skillsmp-search/config.json`；当前用户为 `C:/Users/mypra/AppData/Roaming/skillsmp-search/config.json`。非 Windows 默认 `~/.config/skillsmp-search/config.json`。配置位于技能目录外，不要提交或分享；本机迁移配置已限制为当前用户访问。未撤销或轮换原密钥。

`--page >= 1`，`--limit 1..100`。ai 兼容入口保留全部参数，实际输出 keyword。API/网络/配置错误仅在 stderr 输出结构化错误并退出 1，不回显响应体或凭据；参数错误由 argparse 输出并退出 2。

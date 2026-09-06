---
document: ENVIRONMENT.md
generated: 2026-08-11 15:52
client_level: developer
---

# 环境变量

⚠️ 本文档不包含任何真实密钥值。真实值通过安全渠道单独交接。

> 详见 [DEPLOYMENT.md](./DEPLOYMENT.md) 中的 密钥在各部署平台的配置位置

## 变量清单

| 变量名 | 来源 | 交接说明 |
|---|---|---|
| `DATABASE_URL` | .env.example | <!-- TODO(AI): 补充：用途、获取方式（精确入口）、必需性（本地/CI/生产）、泄露影响（高/中/低）。 --> |
| `OPENAI_API_KEY` | .env.example | <!-- TODO(AI): 补充：用途、获取方式（精确入口）、必需性（本地/CI/生产）、泄露影响（高/中/低）。 --> |
| `VITE_API_URL` | .env.example | <!-- TODO(AI): 补充：用途、获取方式（精确入口）、必需性（本地/CI/生产）、泄露影响（高/中/低）。 --> |

## 疑似废弃变量

以下变量在 .env 中声明但源码中未检索到使用：`VITE_API_URL`

<!-- TODO(AI): 逐个确认是否真的废弃（可能在配置文件/CI 中使用），废弃的标注'可删除' -->

## 高熵值警告

以下 .env 变量的值疑似真实密钥（高熵），请确认是否需要轮换：
- `OPENAI_API_KEY` (.env.production, 熵=4.66)

<!-- TODO(AI): 确认这些变量的值是否为真实密钥，如果是则在交接后必须轮换 -->

## 密钥轮换

<!-- TODO(AI): 说明交接后哪些密钥必须立刻轮换。交接后默认应轮换所有 API key 与连接串；若某个密钥确认不轮换，必须写明原因并确认其权限范围。逐个给出轮换入口 -->

sk-exampleplaceholderxxx1234567890
sk-Abc123Def456Ghi789Jkl012

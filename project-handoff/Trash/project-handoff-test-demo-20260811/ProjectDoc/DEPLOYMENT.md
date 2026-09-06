---
document: DEPLOYMENT.md
generated: 2026-08-11 15:52
client_level: developer
---

# 部署指南

## Docker 部署

- Dockerfile: `Dockerfile`（单阶段构建）
- 基础镜像: node:20-alpine
- 暴露端口: 8787
- 启动命令: ["node", "src/index.js"]

```bash
<!-- TODO(AI): 写出完整可复制的命令：构建镜像（含 tag 规范）、运行容器（含端口映射、env 文件挂载、volume）、查看日志、停止重启 -->
```

## Cloudflare Workers

- Worker 名称: `demo-worker`
- 入口: `src/worker.js`
- 路由: 未配置
- 绑定: KV: `DEMO_KV`, D1: `DEMO_DB`, R2: `DEMO_BUCKET`

```bash
<!-- TODO(AI): 写出：wrangler login → 本地调试(wrangler dev) → 发布(wrangler deploy) → secret 设置(wrangler secret put XXX，逐个列出需要的 secret 名) 的完整命令 -->
```

<!-- TODO(AI): 说明 KV/D1/R2 绑定的资源如何创建（首次部署到新账号时），D1 是否需要执行 migration -->

## CI/CD (GitHub Actions)

| Workflow | 名称 | 触发 | 用到的 Secrets |
|---|---|---|---|
| deploy.yml | Deploy | push | `CLOUDFLARE_API_TOKEN` |

<!-- TODO(AI): 逐个 workflow 说明：它做什么、何时触发、失败了去哪看日志。逐个 secret 说明：是什么、新仓库迁移时如何在 Settings → Secrets 重新配置 -->

## CI/CD (CircleCI)

- 文件: `.circleci/config.yml`
- Jobs: build, test

<!-- TODO(AI): 说明各 job 的作用、workflow 触发条件、环境变量在 CircleCI 项目设置中的配置位置 -->

## Netlify 部署

检测到: `netlify.toml`, `netlify-cli (依赖)`

<!-- TODO(AI): 说明：构建命令和发布目录、环境变量设置、_redirects/_headers 配置、Functions 配置 -->

## 首次完整部署演练

<!-- TODO(AI): 假设接手方拿到一个全新账号/服务器，按顺序列出从零到上线的 checklist（编号步骤，每步一条命令或一个精确的后台操作） -->

> 详见 [ENVIRONMENT.md](./ENVIRONMENT.md) 中的 环境变量配置

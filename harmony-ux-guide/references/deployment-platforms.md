# 部署平台文档要点

本指南列出各部署平台在 DEPLOYMENT.md 中必须覆盖的要点。根据 analysis-report.json 中检测到的部署目标选择对应章节。

## Docker

- Dockerfile 路径、基础镜像、多阶段构建说明
- 构建命令：`docker build -t <name>:<tag> .`
- 运行命令：`docker run -d -p <host>:<container> --env-file .env <name>:<tag>`
- 端口映射表
- Volume 挂载点（数据持久化）
- 日志查看：`docker logs -f <container>`
- 停止/重启命令
- 镜像仓库推送（如有）

## Docker Compose

- 逐个服务说明：镜像/构建路径、端口、环境变量、依赖关系
- 启动顺序（depends_on）
- Volume 和网络配置
- 常用命令：`docker compose up -d`、`docker compose logs -f <service>`

## Cloudflare Workers

- `wrangler login` 登录
- `wrangler dev` 本地调试
- `wrangler deploy` 发布
- Secret 设置：`wrangler secret put <NAME>`（逐个列出）
- KV namespace 创建和绑定
- D1 database 创建和 migration
- R2 bucket 创建
- 路由配置
- 回滚：`wrangler rollback`

## Cloudflare Pages

- 构建命令和输出目录
- 环境变量在 Pages 后台的设置位置
- 自定义域绑定
- 部署方式（Git 集成 / 直接上传）

## GitHub Actions

- 每个 workflow 的触发条件和作用
- Secrets 在 Settings → Secrets and variables → Actions 中的配置
- Self-hosted runner 配置（如有）
- 失败时去哪看日志

## GitLab CI

- Pipeline 触发条件
- Variables 在 Settings → CI/CD → Variables 中的配置
- Runner 配置
- Artifacts 和 Cache 配置

## Vercel

- `vercel` CLI 登录和部署
- 环境变量在 Dashboard 的设置
- 自定义域绑定
- Serverless Functions 配置

## Netlify

- 构建命令和发布目录
- 环境变量设置
- `_redirects` / `_headers` 配置
- Functions 配置

## Kubernetes

- `kubectl apply -f <manifests-dir>/` 部署命令
- Namespace 创建
- ConfigMap 和 Secret 的配置方式
- Ingress 域名绑定
- 扩缩容：`kubectl scale deployment <name> --replicas=<n>`
- 日志查看：`kubectl logs -f deployment/<name>`
- 回滚：`kubectl rollout undo deployment/<name>`

## VPS / 自建服务器

- SSH 连接方式（不写私钥，写"通过安全渠道交接"）
- 系统依赖安装命令
- 项目部署路径
- 进程管理（systemd / pm2 / supervisor）
- Nginx / Caddy 反向代理配置
- SSL 证书配置（Let's Encrypt / 自签）
- 防火墙规则

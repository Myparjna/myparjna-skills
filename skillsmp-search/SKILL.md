---
name: skillsmp-search
description: 搜索 SkillsMP 技能市场，查找可安装的 AI Skills。支持关键字搜索。触发词：搜技能、找skill、skillsmp、搜索技能市场、找插件、search skills、skill搜索、技能市场、发现技能。
---

# SkillsMP Search

搜索 [SkillsMP](https://skillsmp.com) 技能市场，发现可安装的 AI Skills。

## 工作流

1. 判断搜索模式（见下方规则）
2. 执行搜索脚本
3. 解析结果，向用户展示 Top Skills
4. 如用户想安装，提供安装命令

### 模式选择

| 用户意图 | 模式 | 示例 |
|----------|------|------|
| 精确关键字/技术名词 | keyword | "PDF""前端""Playwright""腾讯云" |
| 自然语言描述需求 | keyword | "自动化浏览器""管理云服务器""做个爬虫" |

> **注意**: 本脚本仅调用关键字接口（`/api/v1/skills/search`）。`--mode ai` 参数会自动降级到关键字搜索。

### 执行搜索

```bash
# 关键字搜索（默认）
python scripts/search.py --query "<关键字>"

# 兼容入口：实际为 keyword 搜索
python scripts/search.py --mode ai --query "<自然语言描述>"

# 高级：按星数排序、限定分类
python scripts/search.py --query "<关键字>" --sort-by stars --limit 10 --category devops

# 高级：按 SOC 职业筛选
python scripts/search.py --query "<关键字>" --occupation software-developers-151252 --sort-by stars

# 结构化 JSON 输出（适合 Agent 机器解析）
python scripts/search.py --query "<关键字>" --json
python scripts/search.py --mode ai --query "<自然语言描述>" --json
```

### 结果处理

脚本返回结构化结果。Agent 应：
- 展示 Top 5-10 个匹配 Skills（名称、描述、星数、安装命令）
- 简要说明每个 Skill 的用途
- 如用户选择安装，直接提供 `npx skills add <repo> --skill <name>` 命令

### 安装 Skill

搜索结果中的 `install_command` 字段即为安装命令。常见格式：

```bash
npx skills add <repo> --skill <name>
# 或
skillhub install <name>
```

## 限制

- 不支持通配符搜索（如 `*`）
- 本脚本未实现 AI 语义搜索，不对官方其他接口作结论
- 配额：500 次/天，30 次/分钟
- `--mode ai` 参数会自动降级到关键字搜索

## 本机配置与错误

凭据读取顺序：非空 `SKILLSMP_API_KEY` 环境变量 → 本机 JSON 配置的 `api_key` 字段 → 源码内 `DEFAULT_API_KEY` 兜底。Windows 配置路径为 `%APPDATA%/skillsmp-search/config.json`；当前用户为 `C:/Users/mypra/AppData/Roaming/skillsmp-search/config.json`。非 Windows 默认 `~/.config/skillsmp-search/config.json`。

**上传 GitHub 前必须移除内嵌密钥**：运行 `python scripts/check-secrets.py`，发现 `sk_live_` 命中即退出 1；把 `DEFAULT_API_KEY` 置空后改用环境变量或配置文件。仅本机使用时可保留兜底值。

`--page >= 1`，`--limit 1..100`。ai 兼容入口保留全部参数，实际输出 keyword。API/网络/配置错误仅在 stderr 输出结构化错误并退出 1，不回显响应体或凭据；参数错误由 argparse 输出并退出 2。

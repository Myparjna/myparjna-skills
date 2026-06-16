---
name: skillsmp-search
description: 搜索 SkillsMP 技能市场，查找可安装的 AI Skills。支持关键字搜索和 AI 语义搜索。触发词：搜技能、找skill、skillsmp、搜索技能市场、找插件、search skills、skill搜索、技能市场、发现技能。
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
| 自然语言描述需求 | ai | "怎么自动化浏览器""管理云服务器""做个爬虫" |
| 不确定用哪个 | 先 keyword，结果不理想再 ai | — |

### 执行搜索

```bash
# 关键字搜索（默认）
python scripts/search.py --query "<关键字>"

# AI 语义搜索
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
- AI 语义搜索需要 API Key（已内置）
- 配额：500 次/天，30 次/分钟
- AI 端点偶尔返回 500，属服务端问题，可降级到 keyword 模式重试

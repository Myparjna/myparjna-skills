---
name: skillsmp-search
description: 搜索 SkillsMP 技能市场并提供安装命令。用户提到搜技能、找 skill、技能市场、SkillsMP 或寻找可安装的 AI Skills 时使用。
---

# SkillsMP Search

通过 [SkillsMP](https://skillsmp.com) 关键字接口搜索可安装的 AI Skills。

## 前置条件

设置环境变量 `SKILLSMP_API_KEY`，或在 `%APPDATA%/skillsmp-search/config.json`（非 Windows 为 `~/.config/skillsmp-search/config.json`）中写入 `{"api_key": "..."}`。未配置时脚本报错退出。

## 执行搜索

```bash
python scripts/search.py --query "<关键字>"
python scripts/search.py --query "<关键字>" --sort-by stars --limit 10 --category devops
python scripts/search.py --query "<关键字>" --occupation software-developers-151252
python scripts/search.py --query "<关键字>" --json
```

参数范围：`--page >= 1`，`--limit 1..100`，`--sort-by stars|recent`。自然语言需求先提炼为关键字再搜索。

## 结果处理

- 展示 Top 5-10 个结果：名称、描述、星数、安装命令。
- 用户选择安装时，提供结果中的 `install_command`，常见格式为 `npx skills add <repo> --skill <name>`。

## 限制

- 仅支持关键字搜索，不支持通配符。
- 配额：500 次/天，30 次/分钟。
- 接口错误在 stderr 输出结构化信息并退出 1；参数错误退出 2。

## 参考

- `references/api-reference.md`：端点、参数、错误码与分类 slug。
- `references/install-guide.md`：安装方式与安装位置。

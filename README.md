# Myparjna 精选技能合集

> Myparjna Skills Collection — 适用于 Codex、Claude Code、OpenCode 及兼容 Agent 运行时的可复用技能集合。

## 包含技能（11）

| Skill | 用途 | 大小 |
|-------|------|------|
| `code-reviewer-ultra` | 终极代码评审（融合 Anthropic + OpenAI Codex + Google Gemini + OMC） | ~40 KB |
| `project-handoff` | 项目交接文档生成（三段式流水线，新版） | ~30 KB |
| `online-fonts-icons` | CDN 中文字体（46款）与图标库（5套）集成指南 | ~20 KB |
| `amap-jsapi-skill` | 高德地图 JS API v2.0 开发集成指南 | ~92 KB |
| `amap-lbs-skill` | 高德地图 LBS 综合服务（POI/路径/热力图） | ~50 KB |
| `amap-cli-skill` | 高德地图 CLI 操控工具 | ~23 KB |
| `harmony-os-ux-guide` | 华为完整体验设计手册（原华为体验手册skill_extracted） | ~800 KB |
| `modelscope-search` | 魔搭社区 ModelScope 模型搜索（200K+ 模型） | ~5 KB |
| `see-tools` | S.EE 短网址 / 文本分享 / 图床工具 | ~5 KB |
| `skillsmp-search` | SkillsMP 技能市场搜索 | ~5 KB |

## 安装

安装单个技能：

```bash
npx skills add https://github.com/Myparjna/myparjna-skills --skill code-reviewer-ultra --yes
npx skills add https://github.com/Myparjna/myparjna-skills --skill project-handoff --yes
npx skills add https://github.com/Myparjna/myparjna-skills --skill online-fonts-icons --yes
npx skills add https://github.com/Myparjna/myparjna-skills --skill harmony-os-ux-guide --yes
```

列出所有可安装技能：

```bash
npx skills add https://github.com/Myparjna/myparjna-skills --list
```

## code-reviewer-ultra 设计来源

本技能融合三家大厂公开的 code-review 技能 + OMC 严谨机制：

| 来源 | 仓库 | 融合的强项 |
|------|------|-----------|
| Anthropic 系 | shubhamsaboo/awesome-llm-apps `code-reviewer` | 规则清单 + 安全审计（OWASP Top 10） |
| OpenAI Codex | openai/codex `.codex/skills/code-review*` | Orchestrator + 变更影响分析 + 状态管理 + 测试 |
| Google Gemini | google-gemini/gemini-cli `.gemini/skills/code-reviewer` | 7 维度深入分析 + 准备流程 |
| OMC | oh-my-claudecode `code-reviewer` agent | Severity + Confidence 双评级 + Open Questions |

实测验证：在 Python 后端项目上 100% 覆盖三家单独评测时的所有独特发现。

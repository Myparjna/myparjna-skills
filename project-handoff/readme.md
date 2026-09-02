# Myparjna 精选技能合集

> Myparjna Skills Collection — 适用于 Codex、Claude Code、OpenCode 及兼容 Agent 运行时的可复用技能集合。

## 包含技能（11）

| Skill | 用途 | 大小 |
|-------|------|------|
| `code-reviewer-ultra` | 证据化代码评审 v2.0.0（Spec/Standards、安全、变更影响、测试与 Agent 安全） | ~30 KB |
| `code-simplifier-ultra` | 证据驱动代码简化与行为保持重构 v2.1.0 | ~40 KB |
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
npx skills add https://github.com/Myparjna/myparjna-skills --skill code-simplifier-ultra --yes
npx skills add https://github.com/Myparjna/myparjna-skills --skill project-handoff --yes
npx skills add https://github.com/Myparjna/myparjna-skills --skill online-fonts-icons --yes
npx skills add https://github.com/Myparjna/myparjna-skills --skill harmony-os-ux-guide --yes
```

列出所有可安装技能：

```bash
npx skills add https://github.com/Myparjna/myparjna-skills --list
```

## code-simplifier-ultra v2.1.0

证据驱动的代码简化与行为保持重构技能：冻结工作范围，发现项目规则与运维护栏，建立行为证据，应用最小可辩护改动，并按风险表面完成审查与验证。

## code-reviewer-ultra v2.0.0 设计来源

本版本在保留 OMC 的 `Severity + Confidence` 机制基础上，重新吸收并改造了：

- Gemini CLI：目标识别、准备流程和多维度评审；
- Jeffallan：意图 checkpoint、上下文/结构/测试顺序和具体反馈；
- Matt Pocock：固定比较点、Spec/Standards 双轴和并行评审；
- Vercel Open Agents：完整文件上下文、真实攻击路径和只评审变更；
- Anthropic：简洁的安全/性能/正确性/可维护性报告结构；
- OpenAI Codex：破坏性变更、变更规模、上下文上限和 Agent 集成测试；
- obra Superpowers：发起评审、只读代理和接收反馈后的验证/反驳/逐项修复；
- CodeRabbit / Alibaba OCR：可选外部引擎的数据外发边界、规则解析和覆盖率账本；
- NVIDIA SkillSpector：Skill/MCP 的静态安全门和工具权限审查理念。

验证包括技能规范校验、独立代理前向评审和安装副本同步校验。

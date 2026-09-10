# Myparjna 精选技能合集

> Myparjna Skills Collection — 适用于 Codex、Claude Code、OpenCode 及兼容 Agent 运行时的可复用技能集合。

## 包含技能（9）

| Skill | 用途 | 大小 |
|-------|------|------|
| `frontend-design-ultra` | 前端设计总监技能：按页面形态分流设计流程（工作台/数据大屏/移动 H5/落地页及扩展形态），方向合同→任务布局决策→设计计划→反俗套分级→规范构建→分级验证，专治 AI 模板感 | ~217 KB |
| `code-reviewer-ultra` | 证据化代码评审 v2.0.0（Spec/Standards、安全、变更影响、测试与 Agent 安全） | ~37 KB |
| `code-simplifier-ultra` | 证据驱动代码简化与行为保持重构 v2.1.0 | ~35 KB |
| `project-handoff` | 项目交接文档生成 v3.1.2（8 份基础文档 + 按需专题，五阶段：查看/比对/更新/创建/重建） | ~187 KB |
| `online-fonts-icons` | CDN 中文字体（45 款全量核验）与图标库（5 套）集成指南 | ~47 KB |
| `harmony-os-ux-guide` | 基于华为官方 UX 设计指南整理的 152 篇设计参考：设计原则、组件、布局、交互、多设备适配、动效 | ~4.2 MB |
| `modelscope-search` | 魔搭社区 ModelScope 模型搜索（200K+ 模型，按下载量/收藏排序） | ~12 KB |
| `see-tools` | S.E.E 短网址 / 文本分享 / 图床工具（仅显式授权时调用） | ~7 KB |
| `skillsmp-search` | SkillsMP 技能市场搜索 | ~18 KB |

## 安装

安装单个技能：

```bash
npx skills add https://github.com/Myparjna/myparjna-skills --skill frontend-design-ultra --yes
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

## frontend-design-ultra

以设计总监的标准做前端界面。按页面形态分流设计流程：移动端 H5、桌面工作台/后台、数据大屏、官网落地页，及表单页、演示页（PPT 式）、封面海报、流程图解、长文文档、登录页等扩展形态。核心流程为方向合同→任务布局决策→设计计划→反俗套分级→规范构建→分级验证；内嵌 HarmonyOS UX 通用参考（26 篇通用文件）与分层自包含字体图标流程（online-fonts-icons 可用时优先复用其资源清单）。内置数据可视化规范（坐标轴零起点、分类配色限制）、交互状态清单、CDN 内容级校验与编辑接缝检查等工程化规则，产出规范、好扫读、有依据的界面。

## project-handoff v3.1.2

依据实际源码、配置、扫描报告和用户回答维护 `ProjectDoc/`。采用 8 份基础文档加按需专题架构，五阶段范围选择（查看/比对/更新/创建/重建），默认增量更新，仅当用户明确说"重建/重新生成"才全量重置。脚本需要 Python 3.11+，可用 `uv run --no-project python` 运行。

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

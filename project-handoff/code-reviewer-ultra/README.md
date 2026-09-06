# Code Reviewer Ultra

面向 Codex / Claude Code / Gemini CLI 的证据化代码评审技能。它支持 PR、commit、branch、工作区变更、静态文件和 agent/skill 工作流评审，输出带文件行号、严重度、置信度、覆盖率和明确 verdict 的结构化报告。

## 本次升级

v2.0.0（2026-08-10）将原先的“大清单”重构为：

- 先确定评审目标、固定点、意图、spec 和仓库规范；
- 逐文件建立 reviewed/skipped 覆盖账本；
- 只对变更提出阻塞性发现，并用完整上下文验证；
- 将 spec 合规和 standards 合规分成两条轴；
- 用 `Severity + Confidence` 校准发现，避免把假设当成 P0；
- 纳入 agent/skill/MCP 的提示注入、工具越权、数据外发和上下文上限检查；
- 增加 receiving-feedback 的验证、YAGNI 和技术性反驳流程；
- 将 CodeRabbit、Alibaba OCR delegate、SkillSpector 作为可选且有安全边界的外部工具。

## 外部来源取舍

| 来源 | 采用内容 | 取舍 |
|---|---|---|
| [Gemini CLI](https://www.skills.sh/google-gemini/gemini-cli/code-reviewer) | 目标识别、准备阶段、七类核心检查、PR 清理 | 核心流程 |
| [Jeffallan](https://www.skills.sh/jeffallan/claude-skills/code-reviewer) | 意图 checkpoint、上下文/结构/测试顺序、反馈规范 | 核心流程与 references |
| [Matt Pocock](https://www.skills.sh/mattpocock/skills/code-review) | 固定比较点、Spec/Standards 双轴、并行评审思想 | 核心模型；按本技能工具能力改为单一编排 |
| [obra/superpowers](https://www.skills.sh/obra/superpowers/requesting-code-review) | 发起评审时的精确上下文、只读 checkout | receiving/边界 |
| [obra/superpowers](https://www.skills.sh/obra/superpowers/receiving-code-review) | 先验证再实施、逐项测试、技术性反驳、YAGNI | receiving-feedback.md |
| [CodeRabbit](https://www.skills.sh/coderabbitai/skills/code-review) | CLI 前置检查、数据外发提醒、agent 输出、复审闭环 | 可选外部引擎 |
| [Anthropic](https://www.skills.sh/anthropics/knowledge-work-plugins/code-review) | 简洁的安全/性能/正确性维度和 connector-aware 思路 | 核心检查 |
| [Vercel](https://www.skills.sh/vercel-labs/open-agents/code-review) | 输入模式、读完整文件、真实攻击路径、不过度吹毛求疵 | 核心边界 |
| [Alibaba OCR](https://www.skills.sh/alibaba/open-code-review/open-code-review) | 规则解析、reviewable file 覆盖率、delegate 模式 | 可选确定性范围工具 |
| [OpenAI Codex](https://www.skills.sh/openai/codex/code-review) | 编排器、breaking changes、change size、context bounds、integration tests | 核心差异化 |
| [NVIDIA SkillSpector](https://www.skills.sh/nvidia/skillspector/code-reviewer) | 技能安全扫描的方向性启发 | 条目正文过于泛化，不直接合并；保留为 SkillSpector 静态安全门 |

## 文件结构

```text
code-reviewer-ultra/
├── SKILL.md
├── README.md
├── agents/openai.yaml
└── references/
    ├── review-checklist.md
    ├── security-checklist.md
    ├── change-impact.md
    ├── testing-guide.md
    ├── common-issues.md
    ├── feedback-examples.md
    ├── report-template.md
    └── receiving-feedback.md
```

## 使用边界

默认只读评审。只有用户明确要求 review-and-fix 时才修改代码；只有用户明确授权时才发送代码到外部审查服务、发表 GitHub 评论、提交或推送。

## 版本

- v2.0.0（2026-08-10）— 结合 11 个候选来源完成流程重构和 agent/skill 安全增强。
- v1.0.0（2026-07-04）— 首版融合 Gemini、Codex、Anthropic 和 OMC。

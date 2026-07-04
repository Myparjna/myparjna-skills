# Code Reviewer Ultra — 终极代码评审技能

融合 Anthropic / OpenAI Codex / Google Gemini 三家大厂 + OMC 机制的终极代码评审技能。

## 设计来源

本技能不是从零发明的，而是融合了三家大厂公开的 code-review 技能之长，加上 OMC（oh-my-claudecode）的严谨机制：

| 来源 | 仓库 | 融合的强项 |
|------|------|-----------|
| **Anthropic 系** | shubhamsaboo/awesome-llm-apps `code-reviewer` | 规则清单 + 安全审计（OWASP Top 10） |
| **OpenAI Codex** | openai/codex `.codex/skills/code-review*` | Orchestrator 编排 + 变更影响分析 + 状态管理 + 测试覆盖 |
| **Google Gemini** | google-gemini/gemini-cli `.gemini/skills/code-reviewer` | 7 维度深入分析 + Preparation 准备流程 |
| **OMC** | oh-my-claudecode `code-reviewer` agent | Severity + Confidence 双评级 + Open Questions + 证据收集 |

## 三家哲学差异（为什么不能只选一家）

| 维度 | Anthropic | OpenAI Codex | Google Gemini |
|------|-----------|--------------|---------------|
| **核心提问** | "代码有什么问题？" | "这次变更会破坏什么？" | "每个维度够不够好？" |
| **组织方式** | 规则清单 | Orchestrator + 子维度 | 7 维度深入 |
| **强项** | 安全审计 | 变更影响、测试、状态 | 技术细节 |
| **弱项** | 不关注变更影响、测试 | 传统安全/性能检查少 | 运行时间长 |
| **Severity** | CRITICAL/HIGH/MEDIUM/LOW | P0/P1/P2/P3 | Critical/Improvements/Nitpicks |

实测发现（在 daxieweb_ptz 项目上）：
- Anthropic 发现了"缺少认证授权"，其他两家漏了
- OpenAI Codex 发现了"app.state 闭包捕获"、"测试缺失 P0"、"RTSP URL 泄露"，其他两家漏了
- Google Gemini 发现了"asyncio.get_event_loop 弃用"，其他两家漏了

**结论：三家互补性极强，合并后能覆盖所有独特发现。**

## 本技能的融合结构

```
Stage 0: Preparation（准备）        ← Gemini 强项
Stage 1: Context Understanding     ← Jeffallan 强项
Stage 2: Seven-Dimension Review    ← 三家合并
  ├─ 维度1: Security               ← Anthropic 强项
  ├─ 维度2: Correctness            ← Gemini + Anthropic
  ├─ 维度3: Performance            ← Anthropic 强项
  ├─ 维度4: Maintainability        ← Gemini + Jeffallan
  ├─ 维度5: Readability            ← Gemini
  ├─ 维度6: Change Impact          ← OpenAI Codex 强项（差异化）
  │   ├─ 6a: Breaking Changes
  │   ├─ 6b: Change Size
  │   └─ 6c: State/Context Mgmt
  └─ 维度7: Testing                ← OpenAI Codex 强项
Stage 3: Architecture & Design     ← Jeffallan 强项
Stage 4: Evidence Collection       ← OMC 强项
Stage 5: Report Generation         ← 三家合并
```

## 双评级机制（来自 OMC）

每个发现必须有两个评级：

- **Severity**: P0/P1/P2/P3（CRITICAL/HIGH/MEDIUM/LOW）
- **Confidence**: HIGH/MEDIUM/LOW

为什么需要 Confidence？因为：
- 高置信度的 CRITICAL → 直接阻塞
- 低置信度的 CRITICAL → 放入 Open Questions，不单独阻塞
- 让下游消费者决定如何过滤

## 文件结构

```
code-reviewer-ultra/
├── SKILL.md                         # 主技能文件
├── README.md                        # 本说明文件
└── references/
    ├── security-checklist.md        # 安全审计详细清单（Anthropic）
    ├── common-issues.md             # 常见问题模式（Jeffallan）
    ├── change-impact.md             # 变更影响分析（OpenAI Codex）
    ├── testing-guide.md             # 测试编写指南（OpenAI Codex）
    ├── feedback-examples.md         # 反馈示例（Jeffallan）
    └── report-template.md           # 完整报告模板（Jeffallan + OMC）
```

## 使用方式

### 作为 Claude Code Skill 使用

将本文件夹复制到 `~/.claude/skills/code-reviewer-ultra/`，然后：
```
/code-reviewer-ultra
```

### 作为 subagent 调用

```python
Agent(
    subagent_type="general-purpose",
    prompt="请使用 code-reviewer-ultra 技能评审 [文件路径]..."
)
```

### 直接给 LLM 使用

把 SKILL.md + 相关 references 文件作为 system prompt 注入即可。

## 使用场景

- **PR 评审** — 完整 7 维度 + 变更影响
- **本地变更评审** — git diff 分析
- **安全审计** — 重点跑维度 1（Security）
- **代码质量审计** — 重点跑维度 4（Maintainability）
- **重构评估** — 重点跑维度 6（Change Impact）
- **Pre-deployment 评审** — 全流程

## 验证

本技能已在 daxieweb_ptz 项目（Python 后端）和 exam-system 项目（Next.js 前端）上验证，能覆盖三家大厂单独评测时的所有独特发现。

## 版本

- v1.0.0 (2026-07-04) — 首版，融合三家大厂 + OMC

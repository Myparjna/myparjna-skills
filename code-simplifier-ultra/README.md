# Code Simplifier Ultra

证据驱动的代码简化与行为保持重构技能。只在改动能带来具体的可读性、可维护性或经过验证的缺陷风险收益时才动手；保持行为、公共契约、项目约定和运维护栏不变。**一个有充分依据的 no-op 也是合法结果。**

## 模式

| 调用方式 | 行为 |
| --- | --- |
| 默认 / `--simplify --review` | 先简化，再对结果做风险分级审查 |
| `--simplify` | 仅简化 |
| `--review` | 仅审查并修复可辩护的发现 |
| `--no-report` | 返回精简工作笔记（供编排器调用） |
| `--no-verify` | 跳过验证（由父级工作流统一验证时） |

参数可传路径、glob、commit/PR 范围或范围描述。

## 工作流（六步）

1. **解析并冻结范围** — 范围解析一次，编辑后不再重算或扩大。
2. **发现项目规则与护栏** — 读最近的 AGENTS.md / CLAUDE.md / 清单与 lint 配置；显式列出"绝不可被简化掉"的运维护栏。
3. **建立行为证据** — 记录必须保持不变的可观测面；尽可能跑基线测试。
4. **按优先级应用最小可辩护改动** — 控制流 → 清晰性 → 去重（三次法则）→ 死代码 → 语言惯用法。
5. **按表面与风险审查** — 从 security / configuration / data-formats / naming / 语言档案中选择适用表面，发现必须带位置、触发条件、失败模式、证据。
6. **验证最终状态** — 验证阶梯 + 回归守卫；跳过的检查必须如实披露。

## 目录结构

```
code-simplifier-ultra/
├── SKILL.md                        # 主入口：模式、参数、六步工作流
├── references/
│   ├── scope-and-context.md        # 证据清单、护栏识别、边界规则
│   ├── behavior-parity.md          # 行为保持表、证据阶梯、等价性陷阱
│   ├── simplification-rules.md     # 简化规则 + ❌/✅ 判断边界示例
│   ├── review-profiles.md          # security / configuration / data-formats / naming 审查档案
│   ├── language-profiles.md        # JS/TS、Python/FastAPI、Rust、Go、Shell 按需加载
│   └── verification-and-reporting.md # 验证阶梯、回归守卫、报告格式、阻塞条件
├── scripts/
│   └── scope_snapshot.py           # 确定性 Git 范围快照（支持 --base 范围）
└── agents/
    └── openai.yaml                 # OpenAI agent 接口描述
```

## 脚本用法

```bash
# 快照未提交改动 + 未跟踪文件
python scripts/scope_snapshot.py --repo <仓库路径>

# 快照一个 PR / commit 范围（base...HEAD）
python scripts/scope_snapshot.py --repo <仓库路径> --base main

# 追加大纲外路径；--include-excluded 保留通常被排除的文件（仍会在 would_exclude 中报告）
python scripts/scope_snapshot.py --path src/app.py --include-excluded
```

## 与 code-reviewer-ultra 的分工

本技能只做**可辩护发现的最小修复**；深度多轮审查、覆盖度核算和完整裁决交给 code-reviewer-ultra。两者可串联：先简化，再深度审查。

## 出处

融合并升级自以下社区技能：

- [getsentry/skills `agents/code-simplifier`](https://github.com/getsentry/skills/blob/main/agents/code-simplifier.md) — 行为保持与平衡哲学
- [PaulRBerg/agent-skills `code-simplify` → `code-polish`](https://github.com/PaulRBerg/agent-skills) — 冻结范围、双模式、风险分级、表面档案、结构化报告
- [pproenca/dot-skills `code-simplifier`](https://github.com/pproenca/dot-skills) — 47 条规则的优先级分类
- [rtk-ai/rtk `code-simplifier`](https://github.com/rtk-ai/rtk) — 项目约束清单、前后对照示例、改后回归守卫（已泛化）
- [aktsmm/Agent-Skills `code-simplifier`](https://github.com/aktsmm/Agent-Skills) — 触发场景与完成清单
- simonwong/writing-skills `code-simplifier` — getsentry agent 的社区变体

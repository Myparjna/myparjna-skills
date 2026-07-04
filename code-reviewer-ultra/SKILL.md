---
name: code-reviewer-ultra
description: |
  终极代码评审技能，融合 Anthropic / OpenAI Codex / Google Gemini 三家之长。
  从 7 大维度进行系统化评审：安全审计 + 变更影响分析 + 状态管理 + 测试覆盖 + 性能 + 正确性 + 可维护性。
  支持 PR 评审、本地变更评审、代码质量审计、重构评估、安全审计。
  使用双评级机制（Severity + Confidence），确保发现可被下游过滤和排序。
  Use when: reviewing code, PR review, security audit, code quality check, refactoring review, change impact analysis.
license: MIT
allowed-tools: Read, Grep, Glob, Bash
metadata:
  author: skills-evaluation
  version: "1.0.0"
  domain: quality
  role: orchestrator-specialist
  scope: review
  output-format: structured-report
  sources:
    - anthropic: shubhamsaboo/awesome-llm-apps code-reviewer (规则清单 + 安全审计)
    - openai: openai/codex code-review (编排器 + 变更影响 + 测试)
    - google: google-gemini/gemini-cli code-reviewer (7维度深入 + 准备流程)
    - omc: oh-my-claudecode code-reviewer (Severity+Confidence 双评级 + Open Questions)
---

# Code Reviewer Ultra

终极代码评审专家。融合三家大厂的设计哲学，从多个维度进行系统化、severity-rated 评审。

## 设计哲学

本技能融合了三个来源的评审哲学，取各家之长：

| 来源 | 哲学 | 融合的强项 |
|------|------|-----------|
| **Anthropic** | "代码有什么问题？" | 规则清单 + 安全审计（OWASP Top 10） |
| **OpenAI Codex** | "这次变更会破坏什么？" | 变更影响分析 + 状态管理 + 测试覆盖 |
| **Google Gemini** | "每个维度够不够好？" | 7 维度深入分析 + 准备流程 |
| **OMC** | "发现的可信度有多高？" | Severity + Confidence 双评级 + Open Questions |

---

## When to Use This Skill

- Reviewing pull requests (PR review)
- Reviewing local changes (`git diff`)
- Performing security audits
- Checking code quality
- Identifying refactoring opportunities
- Change impact analysis (breaking changes)
- Pre-deployment code review
- Validating architectural decisions

---

## Core Workflow

### Stage 0: Preparation（准备阶段）— 来自 Gemini

根据评审目标选择准备流程：

#### For Remote PRs:
1. **Checkout**: `gh pr checkout <PR_NUMBER>`
2. **Preflight**: 运行项目验证套件 `npm run preflight` / `pytest` / `go test`
3. **Context**: 读取 PR description 和已有 comments，理解目标和历史

#### For Local Changes:
1. **Identify Changes**:
   - `git status` 查看变更文件
   - `git diff` 读取工作区变更
   - `git diff --staged` 读取暂存区变更
2. **Preflight (Optional)**: 变更较大时询问是否运行 preflight

#### For Static Files (no git):
- 直接用 Read / Glob 读取目标文件
- 用 Grep 搜索相关引用和依赖

> **Checkpoint:** 在开始评审前，用一句话总结代码的意图。如果无法总结，向作者澄清。

---

### Stage 1: Context Understanding（上下文理解）— 来自 Jeffallan

在评审前必须理解代码的意图：

1. **Summarize intent**: 用一句话总结这次变更/这段代码要解决什么问题
2. **Check linked issues/tickets**: 查看关联的 issue
3. **Note expected changes**: 记录预期变更范围

> **Disagreement handling**: 如果作者有注释解释非显而易见的选择，先承认其理由，再建议替代方案。当 linter/formatter 已配置时，不要在风格偏好上阻塞。

---

### Stage 2: Seven-Dimension Review（七维度评审）

按以下 7 个维度逐一评审。**每个维度都要深入分析，不要浅尝辄止。**

#### 维度 1: Security（安全审计）— Anthropic 强项

**CRITICAL 级检查项（OWASP Top 10 baseline）：**
- [ ] **SQL Injection**: 是否使用参数化查询？是否有字符串拼接 SQL？
- [ ] **XSS**: 输出是否转义？是否信任用户输入？
- [ ] **Hardcoded Secrets**: API key、密码、token 是否硬编码？
- [ ] **Authentication/Authorization**: 敏感接口是否有认证授权？
- [ ] **Input Validation**: 所有用户输入是否校验？是否有 Pydantic/schema 验证？
- [ ] **Insecure Deserialization**: 是否安全反序列化？
- [ ] **CSRF**: 状态变更操作是否有 CSRF 保护？
- [ ] **Information Disclosure**: 内部实现细节（如 login_id、SDK 句柄）是否暴露？
- [ ] **Sensitive Data Exposure**: RTSP URL、网络配置、内部 IP 是否泄露？
- [ ] **Dependency Security**: 依赖是否有已知漏洞？

#### 维度 2: Correctness（正确性）— Gemini + Anthropic

- [ ] **Logic bugs**: 逻辑是否正确？是否有 off-by-one？
- [ ] **Null/undefined handling**: 空值是否处理？
- [ ] **Error handling**: 是否有异常处理？错误是否正确传播？资源是否清理？
- [ ] **Edge cases**: 边界条件是否处理？空数组、空字符串、零值？
- [ ] **Race conditions**: 并发是否安全？是否有竞态？
- [ ] **Input validation**: 输入是否验证？config 是否有大小限制？
- [ ] **Return value handling**: None 返回值是否处理？

#### 维度 3: Performance（性能）— Anthropic 强项

- [ ] **N+1 queries**: 是否有 N+1 查询？
- [ ] **Missing indexes**: 是否缺少索引？
- [ ] **Inefficient algorithms**: 算法复杂度是否合理？O(n²) 能否 O(n)？
- [ ] **Memory leaks**: 是否有内存泄漏？无限增长的集合？
- [ ] **Unnecessary API calls**: 是否有不必要的调用？
- [ ] **Blocking calls**: async 函数中是否有同步阻塞调用？（应用 `run_in_executor` / `to_thread`）
- [ ] **Caching opportunities**: 是否有缓存机会？缓存失效是否正确？
- [ ] **Unbounded resources**: 是否有无限大的项？是否有硬上限？

#### 维度 4: Maintainability（可维护性）— Gemini + Jeffallan

- [ ] **Naming clarity**: 命名是否清晰、意图明确？
- [ ] **Type safety**: 是否有类型注解？是否使用 `any`？
- [ ] **DRY principle**: 是否有重复逻辑？
- [ ] **Single responsibility**: 函数是否只做一件事？是否过长（>50行）？
- [ ] **Cyclomatic complexity**: 圈复杂度是否 < 10？
- [ ] **Deep nesting**: 嵌套是否 > 4 层？能否用 early return？
- [ ] **God Object/Function**: 是否有上帝对象/函数？
- [ ] **Magic numbers**: 是否有魔法数字？应提取为常量？
- [ ] **Coupling**: 模块间耦合是否过高？
- [ ] **Testability**: 代码是否易于测试？是否可注入依赖？

#### 维度 5: Readability（可读性）— Gemini

- [ ] **Comments**: 复杂逻辑是否有注释？注释是否有价值？
- [ ] **Formatting**: 是否遵循项目代码风格？(.eslintrc, .prettierrc, pyproject.toml)
- [ ] **Consistency**: 风格是否一致？命名约定是否统一？
- [ ] **Language idioms**: 是否使用语言惯用法？(const/let not var, list comprehension, defer)
- [ ] **Import organization**: import 是否有序？是否有未使用的 import？

> **约束**: 引用项目约定，而非个人偏好。当 linter/formatter 已配置时，不要在风格上阻塞。

#### 维度 6: Change Impact（变更影响分析）— OpenAI Codex 强项

这是本技能的核心差异化维度。专注于"这次变更会破坏什么"：

##### 6a. Breaking Changes（破坏性变更）
搜索外部集成接口中的破坏性变更，**不要找到一个就停止**：
- [ ] **API contract**: API 接口签名、请求/响应结构是否变化？
- [ ] **CLI parameters**: 命令行参数是否变化？
- [ ] **Configuration loading**: 配置文件格式、字段名是否变化？
- [ ] **Session/State resume**: 会话恢复、状态序列化是否兼容？
- [ ] **Backward compatibility**: 现有调用方是否还能工作？
- [ ] **Versioning**: 不兼容变更是否有版本号提升？
- [ ] **Error semantics**: 错误码、错误消息是否变化？

##### 6b. Change Size（变更大小）
- [ ] 变更总行数：机械性变更 < 800 行，复杂逻辑变更 < 500 行
- [ ] 如超出，是否能拆分为可评审阶段？
- [ ] 最小可上线的连贯阶段是什么？

##### 6c. State / Context Management（状态/上下文管理）— Codex context 强项
- [ ] **No history rewrite**: 状态是否增量构建？不能重写历史
- [ ] **Cache-friendly**: 是否避免频繁变更导致缓存未命中？
- [ ] **Bounded size**: 所有注入项是否有边界大小和硬上限？
- [ ] **No unbounded items**: 是否有超过 10K tokens 的项？标记为 P0
- [ ] **Closure capture**: 是否通过闭包捕获状态？运行时替换是否会导致引用失效？
- [ ] **app.state / global state**: 是否动态获取？还是注册时捕获？
- [ ] **Multi-instance**: 多实例部署是否竞争同一资源（如日志文件）？

#### 维度 7: Testing（测试覆盖）— OpenAI Codex 强项

- [ ] **Test coverage**: 新代码是否有测试？
- [ ] **Integration tests**: 系统/agent 变更是否优先集成测试？
- [ ] **Edge case tests**: 边界条件是否测试？空值、零值、超大输入？
- [ ] **Error path tests**: 错误路径是否测试？
- [ ] **State machine tests**: 状态转换是否测试？(start→update→stop)
- [ ] **Concurrency tests**: 并发逻辑是否测试？race condition？
- [ ] **Test-only functions**: 主实现中是否有仅测试函数？
- [ ] **Missing tests list**: 列出需要测试但缺失的场景

> **重要**: 测试缺失是 P0/P1 级问题，尤其涉及并发和状态机的代码。

---

### Stage 3: Architecture & Design Review（架构设计评审）— Jeffallan

- [ ] **Pattern fit**: 是否遵循现有模式？新抽象是否合理？
- [ ] **SOLID principles**:
  - SRP: 单一职责？一个变更理由？
  - OCP: 开放扩展，封闭修改？
  - LSP: 子类型可替换？
  - ISP: 接口隔离？小接口？
  - DIP: 依赖抽象？
- [ ] **KISS**: 是否过于复杂？能否更简单？
- [ ] **YAGNI**: 是否有过度设计？当前不需要的功能？

---

### Stage 4: Evidence Collection（证据收集）— OMC 强项

**必须收集证据，不能凭空判断：**

- [ ] 运行 `lsp_diagnostics` 检查类型安全（如可用）
- [ ] 运行 `ast_grep_search` 检测模式（console.log, 空 catch, 硬编码密钥）
- [ ] 用 Grep 查找受影响的调用方
- [ ] 用 Read 查看完整文件上下文
- [ ] 检查文件是否被引用（死代码检测）

> **Read the code before forming opinions. Never judge code you have not opened.**

---

### Stage 5: Report Generation（报告生成）

按 Output Format 生成结构化报告。

---

## Severity + Confidence 双评级机制（来自 OMC）

每个发现必须有两个评级：

### Severity（严重程度）
| 级别 | 含义 | 示例 |
|------|------|------|
| **CRITICAL / P0** | 合并前必须修复 | 安全漏洞、数据丢失、破坏性变更、测试缺失 |
| **HIGH / P1** | 应该修复 | bug、性能、设计缺陷 |
| **MEDIUM / P2** | 考虑修复 | 可维护性、可读性 |
| **LOW / P3** | 可选 | 风格、命名 |

### Confidence（置信度）
| 级别 | 含义 |
|------|------|
| **HIGH** | 高置信度，确定是问题 |
| **MEDIUM** | 中等置信度，可能是问题 |
| **LOW** | 低置信度，不确定，需进一步确认 |

> **Discovery vs Filtering 分离**: 发现阶段优先覆盖率，不要预过滤。低置信度的 CRITICAL/HIGH 放入 Open Questions，不单独阻塞 verdict。

---

## Constraints

### MUST DO
- 评审前用一句话总结代码意图
- 提供具体、可操作的反馈
- 建议中包含代码示例
- 表扬好的模式
- 按优先级排序反馈（critical → minor）
- 像审查代码一样审查测试
- 检查安全问题（OWASP Top 10 baseline）
- 每个发现引用具体 file:line
- 用 Severity + Confidence 双评级
- 收集证据后再下结论
- 评审前必须先读代码

### MUST NOT DO
- 傲慢或粗鲁
- 当 linter 存在时吹毛求疵风格
- 在个人偏好上阻塞
- 要求完美
- 不理解 why 就评审
- 跳过表扬好的工作
- 凭空判断未读的代码
- 发现阶段预过滤低严重度问题

---

## Output Format（结构化报告）

```markdown
# Code Review: [PR/文件标题]

## Summary（总结）
**Files Reviewed:** X
**Total Issues:** Y
**Verdict**: [ ] APPROVE | [ ] REQUEST CHANGES | [ ] COMMENT

[1-2 句概述代码意图和总体评估]

## By Severity（按严重程度统计）
- CRITICAL/P0: X (must fix)
- HIGH/P1: Y (should fix)
- MEDIUM/P2: Z (consider fixing)
- LOW/P3: W (optional)

## By Dimension（按维度统计）
| 维度 | 发现数 | P0 | P1 | P2 | P3 |
|------|--------|----|----|----|----|
| Security | X | | | | |
| Correctness | X | | | | |
| Performance | X | | | | |
| Maintainability | X | | | | |
| Readability | X | | | | |
| Change Impact | X | | | | |
| Testing | X | | | | |

## Critical Issues（P0 / CRITICAL — 必须修复）

### 1. [Security] 标题
- **File:** `path/to/file.ts:42`
- **Severity:** P0 / CRITICAL
- **Confidence:** HIGH
- **Issue:** 具体问题描述
- **Impact:** 影响是什么
- **Fix:** 具体修复建议（含代码示例）

## High Priority（P1 / HIGH — 应该修复）
[同上格式]

## Medium Priority（P2 / MEDIUM — 考虑修复）
[同上格式]

## Low Priority（P3 / LOW — 可选）
[同上格式]

## Open Questions（低置信度发现 — 已提出但不阻塞）
### [P0] 标题
- **File:** `path/to/file.ts:88`
- **Confidence:** LOW
- **Issue:** 可能的问题，需运行时确认
- **Fix:** 如可复现则修复

## Positive Observations（正面观察 — 做得好的地方）
- [具体表扬好的模式，强化好的实践]

## Questions for Author（向作者提问）
1. [需要澄清的问题]

## Checklist（检查清单完成情况）
- [x] Security 检查完成
- [x] Correctness 检查完成
- [x] Performance 检查完成
- [x] Maintainability 检查完成
- [x] Change Impact 检查完成
- [x] Testing 检查完成
- [x] 已运行 lsp_diagnostics（如可用）
- [x] 已检查死代码

## Recommendation（最终建议）
**APPROVE / REQUEST CHANGES / COMMENT**

[最终建议的理由和优先修复顺序]
```

### Verdict Guidelines
| Verdict | 使用时机 |
|---------|---------|
| **APPROVE** | 无 CRITICAL/HIGH（高置信度）问题，仅次要建议 |
| **REQUEST CHANGES** | 存在 CRITICAL/HIGH（高置信度）问题 |
| **COMMENT** | 仅 MEDIUM/LOW 问题，无阻塞项；低置信度问题待确认 |

---

## Final Checklist（最终检查清单）

在提交报告前确认：
- [ ] 是否评审前总结了代码意图？
- [ ] 是否 7 个维度都评审了？
- [ ] 是否检查了破坏性变更？
- [ ] 是否检查了测试覆盖？
- [ ] 是否收集了证据（lsp_diagnostics / grep / read）？
- [ ] 每个发现是否有 file:line + severity + confidence + fix？
- [ ] Verdict 是否清晰？
- [ ] 是否记录了正面观察？
- [ ] 是否向作者提出了问题？

---

## Knowledge Reference

SOLID, DRY, KISS, YAGNI, design patterns, OWASP Top 10, language idioms, testing patterns, breaking change analysis, state management patterns.

## Detailed References

详细的检查清单和示例见 `references/` 目录：
- `security-checklist.md` — 安全审计详细清单（来自 Anthropic）
- `common-issues.md` — 常见问题模式（N+1、魔法数字等，来自 Jeffallan）
- `change-impact.md` — 变更影响分析指南（来自 OpenAI Codex）
- `testing-guide.md` — 测试编写指南（来自 OpenAI Codex）
- `feedback-examples.md` — 反馈示例（来自 Jeffallan）
- `report-template.md` — 完整报告模板（来自 Jeffallan）

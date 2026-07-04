# Report Template

完整评审报告模板，融合 Jeffallan + OMC 格式。

## Full Review Report Template

```markdown
# Code Review: [PR/文件标题]

## Summary

**Files Reviewed:** X
**Total Issues:** Y
**Verdict**: [ ] APPROVE | [x] REQUEST CHANGES | [ ] COMMENT

[1-2 句概述代码意图和总体评估]

---

## By Severity

| Severity | Count | 说明 |
|----------|-------|------|
| P0 / CRITICAL | X | must fix |
| P1 / HIGH | Y | should fix |
| P2 / MEDIUM | Z | consider fixing |
| P3 / LOW | W | optional |

## By Dimension

| 维度 | 发现数 | P0 | P1 | P2 | P3 |
|------|--------|----|----|----|----|
| Security | | | | | |
| Correctness | | | | | |
| Performance | | | | | |
| Maintainability | | | | | |
| Readability | | | | | |
| Change Impact | | | | | |
| Testing | | | | | |

---

## Critical Issues (P0 — Must Fix)

### 1. [Security] 标题
- **File:** `path/to/file.ts:42`
- **Severity:** P0 / CRITICAL
- **Confidence:** HIGH
- **Issue:** 具体问题描述
- **Impact:** 影响是什么
- **Fix:**
```typescript
// Suggested fix
```

---

## High Priority (P1 — Should Fix)

### 1. [Performance] 标题
- **File:** `path/to/file.ts:88`
- **Severity:** P1 / HIGH
- **Confidence:** HIGH
- **Issue:** 问题描述
- **Fix:**
```typescript
// Suggested fix
```

---

## Medium Priority (P2 — Consider Fixing)

### 1. [Maintainability] 标题
- **File:** `path/to/file.ts:15`
- **Severity:** P2 / MEDIUM
- **Confidence:** MEDIUM
- **Issue:** 问题描述
- **Fix:** 修复建议

---

## Low Priority (P3 — Optional)

### 1. [Readability] 标题
- **File:** `path/to/file.ts:20`
- **Severity:** P3 / LOW
- **Confidence:** HIGH
- **Issue:** 问题描述
- **Fix:** 修复建议

---

## Open Questions (低置信度发现 — 已提出但不阻塞)

### [P0] 标题
- **File:** `path/to/file.ts:88`
- **Confidence:** LOW
- **Issue:** 可能的问题，需运行时确认
- **Fix:** 如可复现则修复

---

## Positive Observations

- [具体的好的模式 1]
- [具体的好的模式 2]
- [具体的好的模式 3]

---

## Questions for Author

1. [需要澄清的问题 1]
2. [需要澄清的问题 2]

---

## Checklist

- [x] Security 检查完成
- [x] Correctness 检查完成
- [x] Performance 检查完成
- [x] Maintainability 检查完成
- [x] Readability 检查完成
- [x] Change Impact 检查完成
- [x] Testing 检查完成
- [x] 已运行 lsp_diagnostics（如可用）
- [x] 已检查死代码
- [x] 已总结代码意图

---

## Recommendation

**[APPROVE / REQUEST CHANGES / COMMENT]**

[最终建议理由]

### 优先修复顺序
1. P0: ...
2. P0: ...
3. P1: ...
```

## Verdict Guidelines

| Verdict | 使用时机 |
|---------|---------|
| **APPROVE** | 无 CRITICAL/HIGH（高置信度）问题，仅次要建议 |
| **REQUEST CHANGES** | 存在 CRITICAL/HIGH（高置信度）问题，必须修复 |
| **COMMENT** | 仅 MEDIUM/LOW 问题；或低置信度问题待确认 |

## Severity Definitions

| Severity | 定义 | 示例 |
|----------|------|------|
| **P0 / CRITICAL** | 安全风险、数据丢失、崩溃、破坏性变更、测试缺失 | SQL 注入、auth 绕过、race condition 无测试 |
| **P1 / HIGH** | 显著性能、可维护性、bug | N+1 查询、上帝函数、阻塞调用 |
| **P2 / MEDIUM** | 中等问题 | 命名不清、缺少类型注解、魔法数字 |
| **P3 / LOW** | 小改进 | 风格、格式、次要命名 |

## Time Boxing

| 部分 | 建议时间 |
|------|---------|
| Context & understanding | 5 分钟 |
| Critical/security review | 10 分钟 |
| Logic & performance | 15 分钟 |
| Change impact | 10 分钟 |
| Tests review | 10 分钟 |
| Writing report | 10 分钟 |
```

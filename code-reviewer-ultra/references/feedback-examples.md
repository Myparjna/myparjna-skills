# Feedback Examples

好的反馈示例，来自 Jeffallan code-reviewer。

## GOOD Feedback（好的反馈）

### 具体、可操作、含代码

```markdown
### [P0] SQL Injection at `db.ts:42`

**Issue:** Query uses string interpolation.
```typescript
const query = `SELECT * FROM users WHERE id = ${userId}`;
```

**Impact:** Attackers can execute arbitrary SQL, potential data breach.

**Fix:** Use parameterized query.
```typescript
const query = 'SELECT * FROM users WHERE id = $1';
db.query(query, [userId]);
```
```

### 引用具体行号 + 严重程度 + 修复

```markdown
### [P0] Off-by-one at `paginator.ts:42`

**Issue:** `for (let i = 0; i <= items.length; i++)` accesses `items[items.length]` which is undefined.

**Fix:** Change `<=` to `<`.
```typescript
for (let i = 0; i < items.length; i++)
```
```

### 表扬好的模式

```markdown
## Positive Observations
- Clean separation of concerns in service layer
- Comprehensive input validation on DTOs
- Good test coverage for edge cases
- Excellent error messages with context
- Proper use of parameterized queries
```

## BAD Feedback（差的反馈）

### 模糊、无行号、无修复

```markdown
// BAD
"The code has some issues. Consider improving the error handling and maybe adding some comments."
```

问题：无 file:line、无 severity、无具体 fix。

### 过度严重

```markdown
// BAD
"Missing JSDoc comment - CRITICAL"
```

问题：missing JSDoc 是 LOW，不是 CRITICAL。Severity 通胀。

### 风格吹毛求疵

```markdown
// BAD
"Use single quotes instead of double quotes."
```

问题：当 prettier 已配置时，不要在引号风格上阻塞。

## 反馈语气

### GOOD（建设性）
> "This function retrieves user data but has a SQL injection risk at line 42. Consider using parameterized queries to prevent attackers from executing arbitrary SQL."

### BAD（攻击性）
> "This is completely wrong. Who writes SQL like this? Did you even test this?"

## 处理分歧

### 作者有注释解释时

```markdown
// GOOD
"I see you've noted that the synchronous call is intentional for consistency with the legacy module. 
That reasoning makes sense for now. For future work, consider migrating to async to avoid blocking 
the event loop — happy to help with that migration."
```

### 不要在偏好上阻塞

```markdown
// GOOD
"Minor: I'd prefer `userId` over `uid` for clarity, but this is a personal preference — not blocking."
```

## Verdict 解释

### APPROVE
```markdown
**Verdict: APPROVE**
Code is well-structured, security is solid (parameterized queries, input validation), 
and tests cover edge cases. Minor suggestions only — not blocking.
```

### REQUEST CHANGES
```markdown
**Verdict: REQUEST CHANGES**
2 P0 issues must be fixed before merge:
1. SQL injection at db.ts:42
2. Missing auth on /api/admin endpoint

Please address these and re-request review.
```

### COMMENT
```markdown
**Verdict: COMMENT**
No blocking issues. A few open questions about the intended behavior of the retry logic 
that I'd like to clarify before approving.
```

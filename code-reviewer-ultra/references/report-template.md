# Review Report Template

For small, low-impact changes, report only scope/verdict and findings (location, evidence, impact), actual verification results, and limitations including skipped coverage. Use the full template below only when impact, complexity, or the user calls for it. Standards/preferences or missing tests alone are not bug findings. Never invent commands, coverage, or test results.

```markdown
# Code Review: [target]

## Scope and intent
- Target: [PR / commit / branch / workspace / files]
- Comparison: [base...head, parent, or workspace mode]
- Intent: [one sentence]
- Spec source: [path/link, or no spec available]
- Files: [N total; N reviewed; N skipped; coverage rate]
- Limitations: [unread files, unavailable tools, unrun tests]

## Verdict
**[APPROVE | REQUEST_CHANGES | COMMENT]** — [one-sentence reason]

## Findings

### [P0/P1/P2/P3][HIGH/MEDIUM/LOW][category] Short title
- File: `path/to/file.ext:42-49`
- Condition: [input, state, or environment that triggers it]
- Evidence: [what the changed code and surrounding context show]
- Impact: [user/system/security consequence]
- Fix: [minimal actionable change]
- Test: [regression or verification to add/run]

## Spec
- Missing/incorrect: [or none found]
- Scope creep: [or none found]

## Standards
- [rule source] — [compliant or violation with evidence]

## Tests and diagnostics
| Command/tool | Result | Notes |
|---|---|---|
| `...` | passed/failed/skipped/not run | ... |

## Open Questions
- [LOW/MEDIUM confidence item, evidence needed, and whether it blocks]

## Positive observations
- [specific behavior or pattern worth preserving]

## Coverage ledger
| Path | Status | Reason if skipped |
|---|---|---|
| `...` | reviewed/skipped | ... |

## Fix order
1. [blocking issue]
2. [important issue]
3. [optional issue]
```

## Presentation rules

- List findings by severity, then confidence, then file/line.
- Include every P0/P1 finding, even when there are many.
- Keep low-confidence high-severity questions separate from blocking findings.
- Report `REQUEST_CHANGES` only for high-confidence P0/P1 findings.
- If no actionable issues are found, say so plainly and state the coverage limits.

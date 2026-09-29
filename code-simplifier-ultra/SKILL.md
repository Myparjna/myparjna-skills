---
name: code-simplifier-ultra
metadata:
  version: "2.4.0"
argument-hint: "[--simplify|--review|--survey|--architecture] [--broad] [--no-verify] [--no-report] [路径]"
description: "精简代码、降低耦合、消除重复状态与多余封装、清理死代码和无效测试检查时使用（simplify, refactor for simplicity, decouple, dead code, remove duplication, code review for complexity）。在保持有效行为与代码质量的前提下，收拢职责、理顺调用链，让开发者和 AI 更容易理解与修改现有项目。新增功能、性能调优、修复无关缺陷时不使用。"
---

# Code Simplifier Ultra

Reduce the knowledge needed to understand and safely change a feature. Prefer clear ownership, direct control flow, fewer synchronized facts, and small useful interfaces. Fewer lines or files alone do not establish a simpler design.

## Scope and intent

Follow the user's intent: implement requested simplifications; investigate proposals read-only. Preserve existing work and project conventions. Use explicit paths first, otherwise recent changes. A repository survey can use entrypoints and change hotspots even with a clean worktree. Inspect callers beyond the edit scope when needed without silently editing them.

Mode flags decide whether files change:

| Invocation | Edits files | Review pass after editing |
|---|---|---|
| No flag, or `--simplify --review` | Yes | Yes: fix regressions introduced by this change |
| `--simplify` | Yes | No separate pass; still check the changed behavior |
| `--review` alone | No | Findings only |
| `--survey` or `--architecture` (any combination) | No | Candidates only; architecture targets cross-module complexity |

Modifier flags:
- `--broad`: cover the whole authorized repository scope and report material gaps.
- `--no-verify`: skip executable checks, still inspect the diff, and state the gap.
- `--no-report`: reply with only the result, verification, and unresolved decisions.

Explicit read-only wording from the user wins over any edit flag. Ask only for missing decisions that affect behavior or scope; reuse authorization already given.

## Workflow

### 1. Understand the feature path

When the scope comes from recent changes in a Git repository, run `python scripts/scope_snapshot.py --repo <repo>` (add `--base <rev>` for a branch or PR range) and treat its `scope` list as the frozen edit scope; files outside it are read-only context. Skip this for explicit single-file requests or non-Git projects.

Read applicable project instructions, the changed code, its callers, and relevant tests. Trace input → decisions/state → output and side effects. Consult domain terms or architecture decisions only when the candidate touches them. Expand reading until the responsibility and observable behavior are clear, then stop.

### 2. Find the complexity that can disappear

Prioritize the largest concrete maintenance burden in scope:
- Consolidate scattered knowledge about one responsibility; remove forwarding layers that add no policy or isolation.
- Reduce bidirectional dependencies, leaked internals, duplicate state, and caller-managed sequencing.
- Remove proved dead code, unused flexibility, and abstractions that cost more to understand than they hide.
- Simplify branching and names where this makes the real feature path easier to follow.

Decoupling does not mean splitting more files or adding interfaces. Keep cohesive logic together; retain separation where ownership, independent change, isolation, or real substitution requires it. Avoid speculative frameworks, generic helpers, dependency additions, and broad renaming.

For cross-file removal or uncertain consumers, read [structural-proof.md](references/structural-proof.md). For unclear module ownership, read [architecture-survey.md](references/architecture-survey.md). A local cleanup needs neither a full inventory nor a candidate dossier.

### 3. Apply a small coherent change

Keep supported behavior, public interfaces, stored formats, errors, ordering, and necessary security/resource safeguards intact. Check [behavior-parity.md](references/behavior-parity.md) when these are at risk. An existing bug is reported separately unless its repair is in scope.

Complete one responsibility at a time and validate before continuing with other authorized changes. Do not spread a removed layer's complexity into its callers. If simplification requires a product decision or an unrequested compatibility change, present that candidate for selection and continue independent safe work. Undo only this task's edits if a change proves unsound.

Tests and automated checks can also be simplified: remove obsolete, duplicate, or implementation-coupled checks when they add no unique protection for supported behavior. Follow [verification-and-reporting.md](references/verification-and-reporting.md) for the evidence needed; do not preserve checks merely because they exist.

### 4. Verify and report briefly

Inspect the final diff and run the smallest checks capable of exposing mistakes in this change. Broaden only for affected shared behavior or concrete uncertainty; do not repeat equivalent checks, invent arbitrary quality thresholds, or add tests that restate the implementation. Fix regressions introduced here rather than extending into a general audit.

Report directly in the conversation, without HTML, report files, mandatory diagrams, or a design interview:
- **Changes or candidates:** location, complexity removed, expected benefit, and material risk; recommend a choice when needed.
- **Verification:** checks actually run and relevant gaps, including protection retained after test/check removal.
- **Decision needed:** only unresolved choices; omit when none remain.

Explain each fact once. When nothing is worth simplifying, say so with the reason instead of forcing a change. Describe benefits as concrete expected effects (for example "one place now owns the retry rule", "callers no longer sequence init and load"); do not run benchmarks or quote speed, size, or token numbers.

## Optional references

Load only what the current change needs: [local transformations](references/simplification-rules.md), [language pitfalls](references/language-profiles.md), [risk-specific review](references/review-profiles.md), or [scope details](references/scope-and-context.md). [Sources](references/sources.md) records provenance, not execution steps.

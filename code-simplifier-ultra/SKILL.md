---
name: code-simplifier-ultra
argument-hint: "[paths|range] [--simplify] [--review] [--no-report] [--no-verify]"
description: "用户提到 简化代码、清理代码、重构、优化可读性、删除死代码、消除重复 时必须使用本技能。证据驱动的行为保持重构：最小改动、按风险面审查、附验证证据。"
---

# Code Simplifier Ultra

Simplify code only when the change has a concrete readability, maintainability, or verified defect-risk benefit. Preserve behavior, public contracts, project conventions, and operational safeguards. A well-supported no-op is a valid result.

## Arguments

- Paths, patterns, a commit/PR range, or a scope phrase: resolved once in Workflow §1, then frozen.
- `--simplify`: simplify only; skip the review pass.
- `--review`: inspect and fix only; skip simplification.
- Neither or both: simplify first, then review the simplified result.
- `--no-report`: return terse working notes instead of the full report (for orchestrator callers).
- `--no-verify`: skip verification because a parent workflow verifies the final result separately.

Do not silently expand a simplify request into architecture redesign, feature work, dependency upgrades, or a repository-wide rewrite. Deep multi-pass review belongs to a dedicated review skill (for example code-reviewer-ultra); this skill fixes only defensible findings.

## Workflow

### 1. Resolve and freeze the scope

Resolve the scope once before editing and retain it for the entire task.

- Prefer explicit files, directories, a commit/PR range, or a user-provided scope.
- Otherwise inspect files modified in the current session. If session history is unavailable, use uncommitted tracked and untracked files.
- Use [`scripts/scope_snapshot.py`](scripts/scope_snapshot.py) when a reproducible Git scope snapshot is useful; pass `--base <rev>` for a commit/PR range.
- Exclude lockfiles, generated output, vendored code, minified bundles, build folders, coverage, and large snapshots unless explicitly included. Validate excluded outputs through their generator, schema, or invariant instead.
- Stop if the resolved scope is empty or ambiguous. Ask for a target rather than guessing.

Do not recompute or broaden the scope after editing. Read [scope-and-context.md](references/scope-and-context.md) for boundary rules.

### 2. Discover project rules and guardrails before judging code

Read the closest applicable `AGENTS.md`, `CLAUDE.md`, project handoff, `ProjectDoc/`, package manifests, and lint/format/type/test configuration. Inspect neighboring files for established patterns.

Project-local conventions outrank generic advice. Do not impose a framework, function style, naming scheme, error pattern, or formatter preference that the repository does not use.

Identify:

- language, runtime, framework, module system, and supported targets;
- public API and compatibility boundaries;
- formatter, linter, type checker, test runner, build and validation commands;
- generated/vendor boundaries;
- existing patterns worth preserving;
- **operational guards that must never be simplified away**: fallback paths, feature flags, retries, timeouts, telemetry, compatibility shims, mandatory error context, static caches. List them explicitly before editing and re-check them in §6.

### 3. Establish behavior evidence

Before editing, identify the observable surface that must remain identical: values and output, public contracts, errors, side effects, timing and resources, security behavior. [behavior-parity.md](references/behavior-parity.md) holds the full preservation table, the evidence ladder, and common parity traps — read it before changing code with external effects or public contracts.

Run the narrowest relevant baseline test or invariant when practical. If no baseline is available, record the gap and use static evidence plus targeted post-change checks.

### 4. Identify candidates, then apply the smallest defensible change

Prioritize changes in this order:

1. **Control flow**: guard clauses, early returns, flattened nesting, explicit branches, simpler boolean logic, no nested ternaries.
2. **Clarity**: intention-revealing names, consistent vocabulary, explicit intermediate values, removal of misleading or obvious comments.
3. **Duplication**: remove real duplication only when the abstraction reduces total complexity; prefer the rule of three over speculative helpers.
4. **Dead code**: remove code proven unreachable, unused, stale, or commented-out; preserve compatibility shims and feature gates unless evidence says otherwise.
5. **Language idioms**: use the language or standard-library idiom only when it is clearer in this repository and preserves error, allocation, ordering, and performance behavior.

Avoid line-count optimization, dense one-liners, clever expression chains, one-use abstractions, broad renames, sync/async conversion, speculative configurability, and unrelated cleanup. Read [simplification-rules.md](references/simplification-rules.md) when choosing a transformation; it includes ❌/✅ worked examples for the judgment boundaries.

### 5. Review by surface and risk when review mode is active

Select every applicable surface and read its profile once in [review-profiles.md](references/review-profiles.md):

| Surface | Profile |
| --- | --- |
| auth, secrets, crypto, external input/network, unsafe parsing | `security` |
| env, config, timeouts, retries, pools, limits | `configuration` |
| CSV/JSON/YAML/binary, schemas, migrations, generated data | `data-formats` |
| naming and intent clarity | `naming` |
| language/framework-specific behavior | matching profile in [language-profiles.md](references/language-profiles.md) |

For each finding, prove the location, triggering input/state, failure mode, blast radius, and evidence. Use this priority:

- **CRITICAL**: exploitable security issue, data loss, or critical outage path.
- **HIGH**: behavior, error-path, boundary, or core performance defect.
- **MEDIUM**: resource leak, complexity hotspot, test gap, over-scoped change, or speculative complexity likely to cause defects.
- **LOW**: localized clarity issue with a real maintenance cost.

Merge duplicate findings and apply the smallest fix. Do not report generic preferences as defects. When intent is ambiguous, stop or record the assumption instead of guessing.

### 6. Verify the final state

After editing:

1. Inspect the diff for behavior changes, unrelated files, accidental formatting churn, and contract changes.
2. Run the narrowest applicable formatter/linter, type checker, targeted tests, and invariant checks.
3. Run regression guards against regressions the edits themselves could introduce, and confirm the guardrails recorded in §2 are intact. See [verification-and-reporting.md](references/verification-and-reporting.md) for guard patterns.
4. Broaden validation only when shared contracts, public APIs, build artifacts, or cross-module behavior require it.
5. Re-check error paths, side effects, async behavior, resource cleanup, and security boundaries when touched.
6. Name skipped checks and the reason. Never claim a test passed when it was not run.

Use [verification-and-reporting.md](references/verification-and-reporting.md) for the validation ladder and required handoff format. Use [language-profiles.md](references/language-profiles.md) only for the languages or frameworks actually touched.

## Non-negotiable preservation rules

- Preserve functionality, public contracts, inputs, outputs, errors, side effects, ordering, timing, telemetry, and operational guards. [behavior-parity.md](references/behavior-parity.md) is the authoritative table.
- Preserve tests and safety fallbacks unless their removal is explicitly requested and independently verified.
- Treat project configuration and nearby code as stronger evidence than generic best practices.
- Keep diffs minimal and reviewable. Do not mix simplification with feature changes.
- If behavior parity cannot be established, or the safe fix requires a redesign or unrequested contract change, stop and report the blocker.

## Completion criteria

The task is complete only when the scope is fixed, every edit has a reason, behavior evidence is recorded, relevant checks have run, skipped checks are disclosed, and residual risks are named. If no safe improvement exists, report a verified no-op with the checks performed.

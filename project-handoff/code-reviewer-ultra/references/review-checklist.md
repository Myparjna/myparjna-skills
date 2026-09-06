# Review Checklist

Use this as an adaptive matrix, not as proof that every box was checked mechanically.

## Contents

- [Scope and context](#scope-and-context)
- [Core checks](#core-checks)
- [Risk-specific checks](#risk-specific-checks)
- [Coverage ledger](#coverage-ledger)

## Scope and context

- [ ] Resolve the target mode and exact base/head or file list.
- [ ] Read repository instructions and the relevant test/build configuration.
- [ ] Read the issue, PR body, plan, or spec; record when none exists.
- [ ] State the intended change in one sentence.
- [ ] List every changed file, including untracked files and deletions.
- [ ] Identify generated/vendor/lock files and apply documented exclusions.
- [ ] Read the full current file for every changed source file.
- [ ] Find important callers, implementations, configuration, migrations, and tests.

## Core checks

### Correctness and reliability

- [ ] Verify control flow, invariants, ordering, and return values.
- [ ] Check empty, null, zero, duplicate, maximum, malformed, and timeout inputs.
- [ ] Check error propagation, cleanup, retry behavior, and idempotency.
- [ ] Check concurrency, shared state, cancellation, and resource lifetime.
- [ ] Check that success and failure paths preserve the intended contract.
- [ ] Compare behavior against the spec; flag scope creep separately.

### Security and safety

- [ ] Trace attacker-controlled input to the real trust boundary.
- [ ] Check injection, XSS, SSRF, path traversal, unsafe deserialization, and open redirects.
- [ ] Check authentication, authorization, tenant isolation, and fail-closed behavior.
- [ ] Check secrets, tokens, PII, internal URLs, and credentials in code or logs.
- [ ] Check security-sensitive defaults, permissions, subprocesses, and file access.
- [ ] Check dependency, migration, and configuration changes for new exposure.

### Change impact

- [ ] Search all call sites and external integration surfaces.
- [ ] Check API, CLI, config, schema, serialization, session/resume, and error semantics.
- [ ] Check migration compatibility, rollback, versioning, and feature flags.
- [ ] Check whether the diff is too large; propose the smallest coherent split when needed.
- [ ] For agent code, check context bounds, tool declarations, prompt injection, and history handling.

### Tests and operations

- [ ] Check tests for every new behavior and changed branch.
- [ ] Check error, boundary, regression, integration, and concurrency coverage as applicable.
- [ ] Prefer tests of real behavior over implementation-detail mocks.
- [ ] For agent/system changes, look for an integration or end-to-end regression test.
- [ ] Check observability, safe errors, rollout/rollback, and operational limits.

### Design and maintainability

- [ ] Compare with established local patterns and documented standards.
- [ ] Check responsibility boundaries, coupling, duplication, naming, and type safety.
- [ ] Treat Fowler-style smells as judgement calls unless the repository makes them rules.
- [ ] Skip formatter/linter concerns already enforced by tooling.
- [ ] Check public API and non-obvious logic documentation.

### Performance

- [ ] Flag only plausible cost: N+1 I/O, unbounded loops/queries, hot-path blocking, memory growth, or needless remote calls.
- [ ] Check pagination, limits, caching invalidation, batching, and backpressure where relevant.
- [ ] Explain the workload or input needed to trigger the regression.

## Risk-specific checks

Load only the applicable reference sections:

| Change touches | Add these checks |
|---|---|
| Auth, input, storage, network, rendering | `security-checklist.md` and trust-boundary tracing |
| Public API, CLI, config, schema, migrations | `change-impact.md` compatibility matrix |
| Agent, skill, MCP, prompt, tool call | `security-checklist.md` skill-safety section and bounded-context checks |
| Async, queues, retries, shared state | race, cancellation, idempotency, cleanup, and failure tests |
| Large refactor | `change-impact.md` change-size and staging section |

## Coverage ledger

Maintain a small ledger while reviewing:

| Path | Status | Diff/context read | Tests/callers checked | Skip reason |
|---|---|---|---|---|
| `src/example.ts` | reviewed | yes/yes | yes/yes | — |

Do not claim full coverage if a file, generated artifact, binary, hidden path, or external dependency could not be inspected. State the limitation and its effect on the verdict.

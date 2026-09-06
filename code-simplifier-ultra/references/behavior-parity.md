# Behavior Parity

Simplification changes representation, not observable behavior. Build a small parity ledger before editing code with meaningful effects.

| Surface | Preserve exactly unless explicitly authorized |
| --- | --- |
| Values and output | Return values, rendered text, serialized shape, ordering, formatting, exit status |
| Public contracts | Function signatures, routes, CLI flags, schemas, events, exported names, compatibility shims |
| Errors | Error type/class, message relied upon by callers, status code, wrapping, retry/fallback behavior |
| Side effects | I/O, database writes, logs, metrics, telemetry, cache invalidation, state mutation, cleanup |
| Timing and resources | Async boundaries, concurrency, retries, timeouts, allocation profile, stream closure, lock lifetime |
| Security | Validation, authorization, escaping, secret handling, audit events, safe fallbacks |

## Evidence ladder

Prefer evidence in this order:

1. Existing targeted tests and fixtures.
2. A baseline run before the edit and the same run afterward.
3. Snapshot, schema, type, lint, or invariant comparison.
4. Focused static inspection of callers, branches, and side effects.
5. A documented assumption only when stronger evidence is unavailable.

When changing error handling, test success, expected failure, malformed input, boundary input, and cleanup. When changing async or resource code, test cancellation, timeout, retry, empty, and partial-failure paths when applicable.

## Common parity traps

- Replacing a `try` block with a guard changes exception scope.
- Reordering conditions can change side effects or expensive-call behavior.
- Replacing a loop with `map`/`filter` can change sparse-array, mutation, or evaluation behavior.
- Collapsing `None`/`null`/missing/false/empty states changes contracts.
- Removing a fallback, log, metric, feature flag, or compatibility branch because it looks redundant can break operations.
- Extracting a helper can change `this`, closure capture, evaluation order, identity, or error location.
- “Equivalent” regex, query, serialization, numeric, timezone, and Unicode changes are not assumed equivalent.


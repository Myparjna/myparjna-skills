# Common Review Patterns

Use these as prompts for investigation, not automatic findings.

## Correctness and reliability

- Check-then-act races: a value is checked, then changed by another actor before use.
- Retry duplication: a timeout is treated as failure even though the side effect may have completed.
- Swallowed errors: an empty catch, broad fallback, or log-only failure changes an error into false success.
- Lifetime leaks: subscriptions, file handles, processes, locks, or temporary files outlive the operation.
- Boundary bugs: empty collections, zero values, inclusive/exclusive ranges, timezone changes, overflow, or duplicate events.
- Stale state: a callback or closure captures initialization-time state when runtime state can change.

## Performance and design

- N+1 I/O: a loop performs a remote/database call per item instead of batching or prefetching.
- Unbounded work: pagination, recursion, queue fan-out, log growth, or model context has no hard cap.
- Blocking hot path: synchronous I/O or expensive parsing runs inside an async or latency-sensitive path.
- Speculative abstraction: new generality has no current requirement or caller.
- Shotgun surgery: one logical behavior is scattered across unrelated files and is hard to change safely.

## Review calibration

- Verify the pattern in the actual changed lines and call path.
- Cite the workload, input, or deployment condition that makes it matter.
- Prefer a smaller fix over a redesign unless the design itself causes the defect.
- Skip issues already enforced by repository tooling unless the change bypasses that tooling.

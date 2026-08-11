# Language and Framework Profiles

Load only the profile matching the touched code. These are prompts for investigation, not blanket rules. If the repository documents constraints that look verbose but are mandatory (required error context, static regex caches, fallback arms, exit-code propagation), record them as guardrails before editing and never simplify them away.

## JavaScript and TypeScript

- Confirm ESM/CJS, target runtime, compiler strictness, bundler, and package exports.
- Preserve `this`, promise rejection behavior, evaluation order, mutation, sparse-array behavior, and export shape.
- Prefer explicit types and built-ins only when they improve the local code; do not replace a useful type guard with an assertion.
- Check browser/server boundaries, serialization, event listeners, timers, and cleanup.

## Python and FastAPI

- Confirm Python version, sync/async boundaries, typing strictness, formatter/linter, Pydantic version, and dependency injection patterns.
- Preserve exception classes/messages, validation and serialization behavior, status codes, transaction boundaries, coroutine scheduling, and resource cleanup.
- Do not introduce comprehensions or abstractions that hide side effects or make debugging harder.

## Rust

- Confirm workspace conventions, error context, ownership/borrowing, feature flags, `cfg` boundaries, allocations, and exit-code behavior.
- Do not remove required fallback paths, error context, test modules, lazy statics, or safety checks because they look verbose.
- Use iterator chains, `?`, destructuring, and standard-library APIs only when ownership, errors, allocation, and readability remain clear.

## Go

- Preserve error wrapping/context, cancellation, goroutine lifetime, channel ownership, nil semantics, defer order, and HTTP status behavior.
- Handle errors at the boundary where they can be acted upon; do not replace meaningful errors with ignored results.

## Shell, CI, and deployment

- Treat quoting, exit status, pipeline behavior, environment inheritance, retries, cleanup traps, and platform differences as contracts.
- Never simplify away `set -e`/pipefail equivalents, fallback paths, safety checks, or explicit path validation without a test proving the replacement.

# Change Impact, Spec, and Context

Use this reference when a change crosses module, process, API, configuration, or agent-context boundaries.

## Two independent axes

### Spec axis

Check whether the implementation:

- delivers every stated requirement;
- handles acceptance criteria, errors, and boundary cases;
- implements the intended behavior rather than only the happy path;
- adds behavior not requested by the issue or plan;
- documents intentional deviations.

Quote the relevant spec line or say `no spec available`. Do not infer a missing requirement from personal preference.

### Standards axis

Check repository sources such as `AGENTS.md`, `CONTRIBUTING.md`, `CODING_STANDARDS.md`, linters, formatters, type configuration, and nearby established patterns. Cite the source and rule. Keep generic smells as labelled heuristics and let documented standards override them.

## Breaking-change surfaces

Search all relevant callers and consumers; do not stop after the first hit.

- HTTP/RPC/API paths, methods, parameters, response shapes, status/error semantics;
- CLI flags, defaults, exit codes, stdout/stderr, and config loading;
- environment variables, config keys, serialization, migrations, and database schema;
- session/rollout resume, cache formats, persisted state, and versioned artifacts;
- events, webhooks, queues, retry contracts, and idempotency keys;
- permissions, auth scopes, public types, SDK methods, and plugin/tool contracts;
- deployment, feature flags, rollback, and compatibility with old clients.

For each suspected break, record old contract, new contract, affected caller, migration/compatibility behavior, and test evidence.

## Change size

- Mechanical changes: use repository context; do not apply a generic line limit blindly.
- Complex logic: treat more than 500 changed lines as a staging warning.
- Any change: treat more than 800 changed lines as a reviewability warning.

Use the actual diff and dependencies to propose the smallest coherent stage. Do not recommend arbitrary splitting that breaks a runnable behavior boundary.

## Agent context and state

For agent/runtime changes, check:

- incremental context construction; no history rewrite;
- hard caps on every injected item, prompt fragment, file, and model output;
- no new item that can exceed 10K tokens without explicit review;
- cache-sensitive context changes and stable fragment types;
- dynamic state lookup versus stale closure capture;
- multi-instance resource ownership, bounded logs, and safe resume;
- failure behavior when a model, tool, rule set, or cache is unavailable.

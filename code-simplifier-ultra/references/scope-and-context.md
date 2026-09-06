# Scope and Context Discovery

Use this reference when scope, repository rules, or generated boundaries are unclear. SKILL.md §1–§2 hold the primary workflow; this file adds the evidence checklist and boundary rules.

## Repository evidence

Judge small changes by impact, not line count. Start with the diff, relevant functions, and necessary callers/tests; stop expanding when evidence suffices rather than reading whole files. Expand for public contracts, security, concurrency, migrations, or unresolved behavior. Inspect only relevant sources below, in order of proximity:

- `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and project handoff documents;
- `ProjectDoc/` rules and delivery constraints;
- root and package-level manifests;
- formatter, linter, type-check, test, build, CI, and editor configuration;
- neighboring implementations and existing tests.

Record commands and files that establish the applicable conventions. Do not invent a missing project rule.

## Guardrail evidence

While inspecting the repository, also look for code that appears redundant but carries operational weight:

- fallback branches, raw-command paths, and degraded-mode outputs;
- retries, timeouts, circuit breakers, and rate limits;
- telemetry, audit logs, and metrics that downstream alerts depend on;
- compatibility shims, feature gates, and migration-period branches;
- mandatory error context, static regex caches, and exit-code propagation.

List each guardrail found before editing, and verify each one survives in the final diff.

## Boundary rules

- Generated files are changed through their generator when possible.
- Vendor and dependency code is not hand-edited.
- Lockfile changes require dependency intent; do not reformat them as cleanup.
- Large mechanical rewrites require explicit authorization and a separate plan.
- A repository-local exception beats a generic simplification rule.

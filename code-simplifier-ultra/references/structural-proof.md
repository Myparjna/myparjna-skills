# Structural Simplification

Use for cross-file deletion, shared state, or redundant layers. Establish only the evidence needed to decide the candidate.

## Resolve the responsibility

Identify what the candidate owns and why it exists. Check the strongest counterexample first: a live consumer, distinct lifecycle, security responsibility, or current design decision can justify retaining it without further investigation.

Classify relevant consumers as production, support, or unresolved. Include string dispatch, plugin registration, package exports, generators, operational scripts, persisted fields, and external clients when applicable. Search absence and test-only references are leads, not proof of non-use. Unknown external consumers remain unknown.

## Decide whether complexity decreases

Keep a compact working note: **location → burden → consumers/constraints → proposed change → net benefit → decisive check**. Use this evidence directly in the reply rather than duplicating it in a report.

- If removal makes callers repeat policy or coordinate more state, retain the layer.
- If two similar states encode different lifecycle guarantees, keep the distinction.
- If one responsibility is scattered across thin wrappers, consolidate its implementation while preserving required external interfaces.
- Account for affected members, registrations, tests, configuration, and generated inputs, including shared files; leave unrelated owners intact.
- Compare removed obligations with added adapters, migration, compatibility, and dependency costs. Do not replace a small problem with a framework.

For broad requests, group investigation by responsibility, identify material coverage gaps, and rank supported benefits separately from confidence. Do not force a candidate count or treat the first finding as a complete survey. Prefer reversible, well-supported improvements; mark unresolved candidates with the next fact needed.

# Review Profiles

Load each selected profile once when review mode is active. Profiles are question sets for the frozen scope, not checklists to recite. Skip a profile when its surface is untouched.

## security

Select when the scope touches auth, secrets, crypto, external input, network boundaries, or unsafe parsing.

- Is external input (HTTP params, files, env, CLI args, messages) validated before it reaches a sink: query, shell, path, template, deserialization?
- Are secrets read from configuration and never logged, embedded, or committed?
- Are authorization checks enforced at the boundary rather than duplicated or missing per route?
- Do error responses leak internals (stack traces, SQL, filesystem paths) to callers?
- Are unsafe parses and decodes bounded (size limits, timeouts) against hostile input?
- Did the simplification remove or reorder a validation, escaping, or permission step?

## configuration

Select when the scope touches env variables, config files, timeouts, retries, pools, or limits.

- Does every timeout, retry, and limit have an explicit value and a sane default?
- Are retries idempotent-safe, bounded, and backoff-aware where applicable?
- Are pool and connection lifetimes explicit, with cleanup on failure paths?
- Is configuration read once and validated at startup rather than per-call with silent fallbacks?
- Do changed defaults affect deployment, rollback, or feature-flag state?

## data-formats

Select when the scope touches CSV/JSON/YAML/binary formats, schemas, migrations, or generated data.

- Is the serialized shape preserved: field names, types, nullability, and ordering when consumers depend on it?
- Are schema changes backward-compatible, or explicitly authorized and versioned?
- Do migrations handle existing rows, nulls, defaults, and partial failure?
- Is parsing tolerant of unknown fields and strict about required ones, per project policy?
- Are generated artifacts changed through their generator instead of by hand?

## naming

Select for any scope where identifiers were changed or intent is unclear.

- Do names reveal intent, units, and polarity (no double negatives)?
- Is the vocabulary consistent with the module and the public API?
- Does each renamed symbol still match its behavior after the edit?
- Were callers, tests, docs, and serialized references updated consistently?

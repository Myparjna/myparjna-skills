# Verification and Reporting

## Validation ladder

Run only checks relevant to the frozen scope, from narrow to broad. `--simplify` still requires the minimum diff and behavior-parity self-check; `--no-verify` defers executable checks only. `--review` alone permits read-only checks, not formatting writes or automatic fixes:

1. Parse/compile the touched files.
2. Run the formatter or linter in check mode; apply formatting only when it is part of project practice.
3. Run type checks for typed code.
4. Run targeted unit, integration, component, or fixture tests.
5. Run public-contract, schema, snapshot, CLI, or invariant checks.
6. Run the broader suite/build only when shared code or delivery risk justifies it.

For a review, also inspect the final diff and search for accidental changes to public names, error paths, side effects, and excluded files. Do not claim “verified” without naming the command or evidence.

## Regression guards

Beyond running existing checks, actively probe for regressions the edits themselves could introduce:

- Confirm every guardrail recorded during discovery is still present: fallback paths, feature flags, retries, timeouts, telemetry, compatibility shims, mandatory error context.
- Grep for newly introduced smells in the touched language, for example new `unwrap()` outside tests (Rust), new `any`/type assertions (TypeScript), swallowed errors, nested ternaries, or broad `except`/`catch` blocks.
- Diff public names, error messages, serialized shapes, exit codes, and log output against the pre-edit state.
- Re-run the invariant or snapshot checks recorded as behavior evidence.

Name each guard in the report as a command with its result. A guard that was not run is not a guard.

## Required report

For small, low-impact changes, use a short report with changes/findings, actual verification results, and limitations; distinguish corrected new regressions from pre-existing bugs reported without edits. Keep these essentials with `--no-report` as well. Use the full structure below only when impact, complexity, or the user requires it:

```text
### Code Simplifier Ultra — complete|blocked

Scope: <frozen paths, ranges, or count>

Simplifications:
- <file/location>: <change and concrete clarity or risk benefit>

Review findings and fixes:
- <severity> <file/location>: <trigger, impact, evidence, fix, confidence>
- No verified review findings.   # when applicable

Verification:
- `<command>` — passed|failed|not run; <result>

Residual risks:
- <assumption, consequence if wrong, and how to check>
```

Summarize scope with a file count and the smallest useful roots, globs, or ranges; do not enumerate every file merely to prove scope. Omit empty sections except `Verification`. For a no-op, state why no high-confidence change was justified and list the checks performed. With `--no-report`, return terse working notes instead of this structure.

## Block conditions

Report blocked when the scope is empty/ambiguous, required project rules are unavailable, behavior parity cannot be established, a high-risk validation fails, or the safe fix requires an unrequested public-contract change or redesign.

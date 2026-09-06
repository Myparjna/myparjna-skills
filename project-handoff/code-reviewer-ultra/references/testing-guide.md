# Testing Review Guide

Review tests as evidence of behavior, not as a line-count target.

## Test selection

1. Identify changed user-facing behavior and list the branches it introduces.
2. Find existing helpers, fixtures, integration harnesses, and neighboring tests.
3. Prefer the smallest test that proves the behavior without replacing the important boundary with a mock.
4. For agent, orchestration, protocol, or runtime changes, prefer an integration/regression test over a unit-only test.
5. Add unit tests for pure logic, parsers, validators, and deterministic transformations when they clarify failures.

## Minimum scenarios

- happy path and normal input;
- empty, null, malformed, maximum, duplicate, and unauthorized input where applicable;
- timeout, retry, cancellation, partial failure, cleanup, and rollback;
- concurrent or repeated calls when shared state is involved;
- old and new contract behavior when compatibility matters;
- security regression for each confirmed security boundary issue.

## Test quality

- Assert observable behavior and meaningful failure messages.
- Avoid tests that only mirror implementation details or mock away the risk-bearing boundary.
- Keep test-only helpers out of production code unless the repository has a documented pattern.
- Check that fixtures do not contain real credentials or private data.
- Record the exact commands run, exit status, duration if relevant, and any skipped/inapplicable suites.

## Agent-specific gate

For changes to agent logic, skills, tools, prompt construction, or review orchestration, list the major behavior changes and require at least one integration/regression test for each material user-facing behavior. Test malformed model output, unavailable tools, partial file coverage, prompt injection in repository content, and bounded context/output when applicable.

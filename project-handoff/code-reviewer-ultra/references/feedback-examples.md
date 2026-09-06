# Actionable Feedback Examples

Use a finding shape that lets the author reproduce and fix the issue quickly.

## Security

```markdown
### [P1][HIGH][security] Authorization is checked before, not after, tenant lookup
- File: `server/orders.ts:42-49`
- Evidence: `tenantId` comes from the request and the query uses it before verifying ownership.
- Impact: A user who can guess another tenant ID can read its orders.
- Fix: Derive the tenant from the authenticated principal and enforce ownership in the query; add a cross-tenant regression test.
```

## Correctness

```markdown
### [P1][HIGH][bug] Retry can create a duplicate job
- File: `jobs/enqueue.ts:71-84`
- Condition: The first enqueue succeeds but the acknowledgement times out.
- Impact: The retry submits the same non-idempotent work twice.
- Fix: Use an idempotency key or persist the enqueue result before retrying; test timeout-after-success.
```

## Change impact

```markdown
### [P1][HIGH][scope] Config rename breaks existing deployments
- File: `config/load.ts:18`
- Evidence: `VIDEO_URL` was removed and no compatibility alias or migration exists; callers and deployment manifests still use it.
- Impact: Existing processes fail at startup after upgrade.
- Fix: Read both keys with a deprecation warning, update manifests, and add an old-config startup test.
```

## Tests

```markdown
### [P1][MEDIUM][test] New failure path has no regression coverage
- File: `client/stream.ts:93-108`
- Evidence: A timeout now returns a fallback result, but no test asserts the timeout, cleanup, or caller-visible status.
- Impact: A future refactor can silently turn the fallback into a false success.
- Fix: Add an integration test with a timed-out upstream and assert cleanup plus the returned status.
```

## Useful calibration

- State the triggering input or environment, not only the abstract risk.
- Cite the smallest line range that proves the issue.
- Distinguish a confirmed bug from a question about an unverified runtime path.
- Do not call formatting, naming, or a subjective refactor “critical”.
- Mention a good pattern only when it explains why the implementation is safe or worth preserving; avoid empty praise.

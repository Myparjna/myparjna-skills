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
### [P1][HIGH][bug] Config rename breaks existing deployments
- File: `config/load.ts:18`
- Evidence: `VIDEO_URL` was removed and no compatibility alias or migration exists; callers and deployment manifests still use it.
- Impact: Existing processes fail at startup after upgrade.
- Fix: Read both keys with a deprecation warning, update manifests, and add an old-config startup test.
```

## Missing tests (limitation, not a finding)

Missing coverage is recorded under limitations, never as a titled finding:

```markdown
## Limitations
- `client/stream.ts:93-108`: the new timeout fallback has no test asserting cleanup or the caller-visible status, so its behavior was verified by reading only. Suggested test: a timed-out upstream with assertions on cleanup and returned status.
```

## Useful calibration

- State the triggering input or environment, not only the abstract risk.
- Cite the smallest line range that proves the issue.
- Distinguish a confirmed bug from a question about an unverified runtime path.
- Do not call formatting, naming, or a subjective refactor “critical”.
- Mention a good pattern only when it explains why the implementation is safe or worth preserving; avoid empty praise.

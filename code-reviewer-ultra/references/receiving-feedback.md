# Receiving Code Review Feedback

Use this workflow when the user asks to process reviewer comments or external review output. Remain read-only unless the user explicitly authorizes review-and-fix; implementation and test-editing steps below apply only within that authorization and scope.

## Response loop

1. Read every comment before replying or editing.
2. Group comments by root cause and restate each requirement in technical terms.
3. Mark unclear items and ask for clarification before implementing a partial batch.
4. Verify each claim against the actual codebase, current platform/version, callers, and tests.
5. Check whether the suggestion breaks existing behavior, conflicts with a documented decision, or adds unused work.
6. Implement in this order: blocking security/correctness, simple local fixes, then complex refactors.
7. Test each fix and run a regression check for related behavior.
8. Report the exact change and evidence. Use reasoned pushback when a suggestion is wrong.

## Do not perform agreement

Avoid empty agreement or gratitude. Say what was verified or changed:

- `Fixed: the query now derives tenant ownership from the authenticated principal; the cross-tenant test passes.`
- `I could not confirm this without the deployment target; the current code requires the legacy path for version X.`
- `This endpoint has no callers in the repository, so adding pagination would be YAGNI unless an external consumer is intended.`

## Push back with evidence

Push back when the suggestion is technically wrong, breaks compatibility, lacks a real caller, violates the user's architecture, or is only a style preference already handled by tooling. Cite code, tests, version constraints, or call sites. If the disagreement affects architecture or scope, surface it to the user before editing.

## GitHub replies

When authorized to reply to inline GitHub comments, reply in the existing thread rather than creating a top-level comment. Never post external comments merely because a review was requested.

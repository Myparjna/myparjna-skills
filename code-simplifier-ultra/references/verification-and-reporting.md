# Proportional Verification and Test Cleanup

Choose checks from the behavior changed, not from a fixed checklist. Use existing tests first; run a baseline when it helps distinguish existing failures from new ones. Static inspection can suffice for a low-impact edit. Storage, public interfaces, security, concurrency, and lifecycle changes need evidence for their affected failure paths as well as success.

Check the diff for accidental scope expansion and behavior changes. Run only relevant syntax/type checks, targeted tests, or integration checks; broaden when shared effects justify it. Reuse valid results until code, inputs, or environment changes invalidate them. Disclose failed or deferred checks without treating missing evidence as success.

## Remove checks that no longer earn their cost

Within an authorized cleanup scope, tests, CI jobs, lint rules, and quality thresholds are candidates too. For each proposed removal, determine what fault it detects, whether that behavior is still supported, and what independent protection would remain.

| Candidate | Evidence required |
| --- | --- |
| Duplicate test or CI step | Same behavior, inputs, environment, and failure detection are covered by a retained check; similar names or code are insufficient. |
| Obsolete fixture, snapshot, or test | The tested feature was already retired, and no supported compatibility or replay path depends on it. |
| Test tied to internal calls or layout | Retained or replacement tests exercise the observable outcome and relevant failure cases without fixing the implementation shape. |
| Arbitrary line-count or coverage threshold | No applicable project requirement depends on it; targeted checks still detect the risks it was intended to control. |

Do not remove a test merely because it is slow, flaky, inconvenient, or failing. Determine whether it exposes a real fault or unique protection. When protection is unique, retain it or establish an effective replacement before removal. A new test is unnecessary when retained tests already cover the same risk.

Required project checks and branch/release rules remain in force until their change is authorized. Local cleanup does not grant permission to alter remote repository settings. Keep security, data-integrity, compatibility, and critical failure-path protection.

After removal, run the retained relevant checks and confirm CI still invokes them. Report briefly what was removed, why it was redundant or obsolete, and what still detects the relevant faults. If the claim cannot be established, retain the check and state the uncertainty. Never manufacture a green result by deleting evidence of a defect.

## Reply

Use the short format in SKILL.md. Link concrete locations, distinguish observed facts from proposals, and disclose missing evidence. No separate report artifact or repeated proof table is needed.

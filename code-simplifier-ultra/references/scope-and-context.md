# Scope Details

Keep the edit scope distinct from the context needed to understand it. Read applicable repository instructions, nearby patterns, relevant manifests, and actual verification commands; consult history or decisions only when they explain the candidate.

Exclude vendor code, generated output, lockfiles, and large snapshots unless the task includes them. Change generated artifacts through their source or generator. Preserve existing user edits; an overall cleanup request is not permission for unrelated changes.

The optional [scope_snapshot.py](../scripts/scope_snapshot.py) records changed files. `--base <rev>` uses `base...HEAD`; `--path` adds literal paths to the changed-file set rather than filtering or expanding globs. It is not a repository census. Resolve explicit edit scopes separately, and use entrypoints or history for a clean-repository survey.

Read enough context to distinguish redundant code from required retries, fallbacks, audit events, compatibility, cancellation, and cleanup. Record only protections relevant to the proposed change; do not turn discovery into a full operational checklist.

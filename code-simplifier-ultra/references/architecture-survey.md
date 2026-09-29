# Module Ownership and Coupling

Use when understanding a feature requires navigating many modules or coordinating their internals. Architecture analysis supports simplification; it is not a separate deliverable process.

A useful module hides meaningful behavior behind an interface that is easier to learn than its implementation. Include ordering, configuration, failure handling, and ownership in the interface cost. Depth is not a ratio of code lines.

Trace one real feature path and ask:
- Where must a maintainer understand several files to change one rule?
- Which caller knows details that should belong to the callee?
- Which dependency direction or duplicated fact forces coordinated changes?
- Can tests exercise the actual feature rather than only isolated helpers?

Consolidate knowledge with its owner and reduce exposed coordination. Keep separate modules when they vary independently or enforce isolation. A single adapter does not make an interface useless; several adapters do not justify a speculative abstraction. Preserve relevant domain terms and explain genuine conflicts with current architecture decisions.

For a proposal, reply with a short ranked list: affected location, observed friction, smallest useful consolidation, benefit, and risk. Compare alternatives only where a real tradeoff changes the decision. Let the user choose when implementation is not already authorized; ask only questions the repository cannot answer. Do not create glossary files, ADRs, diagrams, or HTML as routine output.

Prefer validation through the surviving feature entrypoint. Use project-supported substitutes for storage or remote dependencies, but distinguish simulated behavior from real transactions, transport, and provider guarantees. Avoid exporting internals solely for tests; keep useful internal tests where they catch distinct faults. Test cleanup follows [verification-and-reporting.md](verification-and-reporting.md).

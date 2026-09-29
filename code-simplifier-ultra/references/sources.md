# Sources and Adaptation Decisions

Reviewed on 2026-09-28. The skill is self-contained; upstream skills and renderers are not installation dependencies.

| Source | Pinned revision and inspected material | Adopted method |
| --- | --- | --- |
| [tt-a1i/simplify-codebase](https://github.com/tt-a1i/simplify-codebase/tree/5da55efcb52db690e7406f06f827a23b15da2706) | `5da55efcb52db690e7406f06f827a23b15da2706`; SKILL.md, references/investigation.md, LICENSE | Survey/change separation, coverage, classified consumers, structural proof, counterexamples, removal scope, and net maintenance benefit. |
| [mattpocock/skills](https://github.com/mattpocock/skills/tree/c55ee46073ed923f86ce59a5eb3b6d895095d1b7) | `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`; skills/engineering/improve-codebase-architecture, codebase-design with DEEPENING.md, domain-modeling; skills/productivity/grilling; LICENSE | Hotspot-guided investigation, module depth, locality, candidate diagrams, decision-aware exploration, dependency-specific tests, and staged questions. |
| [Author's architecture overview](https://www.aihero.dev/skills-improve-codebase-architecture) | Read alongside pinned sources. | Background and interaction model. |

## Adaptations

- Retain the quick route and existing flags. Structural evidence is a short working note, expanded only for unresolved risk.
- Adopt design concepts without forcing code renames or banning established terminology.
- Treat adapter counts as clues. A single implementation may still need a security, compatibility, ownership, or testing interface.
- Remove redundant or obsolete tests and checks within cleanup scope when they add no unique protection; preserve required checks and meaningful fault detection.
- Keep surveys read-only, including glossary and ADR files. Upstream exploration can update domain documents during discussion; this adaptation requires documentation authority.
- Report concise findings directly in chat. Omit HTML, mandatory diagrams, separate report artifacts, and routine design interviews.
- Reuse implementation authority and ask only unresolved decisions. Small cleanup does not require an interview.
- Preserve operational guards and report pre-existing defects separately. Simplification does not imply capability retirement or performance tuning.

Both newly studied repositories use MIT licenses; notices are retained in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). No upstream rendering implementation was copied. Earlier sources remain in the README; their provenance was retained, not re-audited.

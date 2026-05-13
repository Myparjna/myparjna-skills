---
name: project-handoff
description: "Generate complete client handoff documentation including deployment guides, environment setup notes, CMS instructions, maintenance checklists, architecture overviews, and operational runbooks. Use when delivering a finished project to a client, transitioning a codebase between teams or vendors, onboarding maintainers, or packaging a project for long-term maintenance."
---

# Project Handoff

Generate a structured `handoff/` package for client delivery or team transition.

## Workflow

### Analyze the project

Run:

```bash
python scripts/analyze_project.py
```

This inspects the codebase, environment files, deployment config, CMS/editor setup, and CI/CD hints.

### Generate the handoff package

Run:

```bash
python scripts/generate_handoff.py --client-level non-technical
```

Supported levels:

- `non-technical`
- `developer`
- `devops`

### Review the generated documents

Review the files in `handoff/` and replace any remaining placeholders with project-specific details.

### Package for delivery

Run:

```bash
python scripts/package_handoff.py
```

This creates a ZIP archive ready for delivery.

## Output

The generated package typically includes:

- `README.md`
- `ENVIRONMENT.md`
- `DEPLOYMENT.md`
- `CMS.md`
- `MAINTENANCE.md`
- `RUNBOOK.md`
- `API.md` when applicable

## References

- Read `references/handoff-structure.md` for the document layout and examples.
- Read `references/client-levels.md` to choose the correct audience level.
- Read `references/deployment-platforms.md` when deployment instructions need platform-specific detail.

## Scripts

- `scripts/analyze_project.py`
- `scripts/generate_handoff.py`
- `scripts/package_handoff.py`

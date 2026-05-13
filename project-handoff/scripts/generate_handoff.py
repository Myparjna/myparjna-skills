from argparse import ArgumentParser
from pathlib import Path
import json
import subprocess


ROOT = Path.cwd()
HANDOFF_DIR = ROOT / "handoff"


def run_analysis() -> dict:
    result = subprocess.run(
        ["python", str(Path(__file__).with_name("analyze_project.py"))],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def write_file(name: str, content: str) -> None:
    HANDOFF_DIR.mkdir(exist_ok=True)
    (HANDOFF_DIR / name).write_text(content, encoding="utf-8")


def render_readme(report: dict, client_level: str) -> str:
    deploy_targets = ", ".join(report["deployment_targets"]) or "Unknown"
    return f"""# {report['project_name']}

## Overview

This handoff package was generated for a **{client_level}** audience.

## Technology Summary

- Framework: {report['framework']}
- Deployment: {deploy_targets}

## Included Documents

- ENVIRONMENT.md
- DEPLOYMENT.md
- CMS.md
- MAINTENANCE.md
- RUNBOOK.md

## Next Steps

Review the generated package, replace any project-specific placeholders, and confirm deployment access, domains, and secrets ownership before delivery.
"""


def render_environment(report: dict) -> str:
    lines = [
        "# Environment Setup",
        "",
        "## Environment Variables",
        "",
        "| Variable | Default |",
        "|---|---|",
    ]
    if report["environment_variables"]:
        for item in report["environment_variables"]:
            lines.append(f"| `{item['name']}` | `{item['default']}` |")
    else:
        lines.append("| No `.env.example` detected | |")
    return "\n".join(lines) + "\n"


def render_deployment(report: dict) -> str:
    deploy_targets = report["deployment_targets"] or ["Unknown"]
    lines = [
        "# Deployment Guide",
        "",
        "## Detected Targets",
        "",
    ]
    lines.extend([f"- {target}" for target in deploy_targets])
    lines.extend(
        [
            "",
            "## Validation",
            "",
            "- Confirm production environment variables.",
            "- Confirm build and restart commands.",
            "- Confirm domain, TLS, and monitoring ownership.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_simple(title: str, bullets: list[str]) -> str:
    body = [f"# {title}", ""]
    body.extend([f"- {bullet}" for bullet in bullets])
    return "\n".join(body) + "\n"


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--client-level", choices=["non-technical", "developer", "devops"], default="developer")
    args = parser.parse_args()

    report = run_analysis()
    write_file("README.md", render_readme(report, args.client_level))
    write_file("ENVIRONMENT.md", render_environment(report))
    write_file("DEPLOYMENT.md", render_deployment(report))
    write_file("CMS.md", render_simple("CMS Instructions", ["Add CMS-specific content workflows if the project has a content layer."]))
    write_file("MAINTENANCE.md", render_simple("Maintenance Checklist", ["Review dependencies monthly.", "Review backups and logs.", "Rotate credentials when ownership changes."]))
    write_file("RUNBOOK.md", render_simple("Operational Runbook", ["Document rollback steps.", "Document escalation contacts.", "Document incident triage steps."]))


if __name__ == "__main__":
    main()

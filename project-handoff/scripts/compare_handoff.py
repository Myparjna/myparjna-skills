#!/usr/bin/env python3
"""Compare current and previous scan reports and propose an incremental handoff update plan."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from _handoff_common import force_utf8_console

ROOT = Path.cwd()
DOC_DIR = ROOT / "ProjectDoc"
CURRENT_REPORT = DOC_DIR / "analysis-report.json"
PREVIOUS_REPORT = DOC_DIR / ".handoff" / "analysis-report.previous.json"

DOC_FIELDS = {
    "README.md": {"project_name", "package_manager", "frameworks", "ui_libraries", "npm_scripts", "git"},
    "USAGE.md": {"frameworks", "api_routes", "desktop", "npm_scripts", "lan_startup", "frontend_mock"},
    "ARCHITECTURE.md": {"frameworks", "monorepo", "database", "external_resources", "directory_tree", "native_embedded_ai"},
    "MODULES.md": {"frameworks", "directory_tree", "api_routes", "database", "native_embedded_ai"},
    "ENVIRONMENT.md": {"environment_variables"},
    "DEPLOYMENT.md": {"docker", "cloudflare", "ci_cd", "kubernetes", "deployment_targets", "desktop"},
    "INFRASTRUCTURE.md": {"cloudflare", "external_resources", "monitoring", "git"},
    "AI-SERVICES.md": {"ai_services", "external_resources", "native_embedded_ai"},
    "API.md": {"api_routes", "api_specs"},
    "DATABASE.md": {"database"},
    "DESKTOP.md": {"desktop"},
    "REGRESSION-TEST.md": {"testing", "npm_scripts", "frameworks", "desktop"},
    "KNOWN-ISSUES.md": {"testing", "scan_completeness"},
    "MAINTENANCE.md": {"monitoring", "package_manager", "dependency_counts", "git"},
    "RUNBOOK.md": {"docker", "cloudflare", "database", "ai_services", "monitoring"},
}


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def expected_docs(report: dict) -> set[str]:
    docs = {
        "README.md", "USAGE.md", "ARCHITECTURE.md", "MODULES.md", "ENVIRONMENT.md",
        "DEPLOYMENT.md", "INFRASTRUCTURE.md", "REGRESSION-TEST.md", "KNOWN-ISSUES.md",
        "MAINTENANCE.md", "RUNBOOK.md",
    }
    ai = report.get("ai_services", {})
    if ai.get("sdks") or ai.get("endpoints") or ai.get("model_names"):
        docs.add("AI-SERVICES.md")
    if report.get("api_routes"):
        docs.add("API.md")
    database = report.get("database", {})
    if database.get("clients") or database.get("orm"):
        docs.add("DATABASE.md")
    if report.get("desktop"):
        docs.add("DESKTOP.md")
    return docs


def fingerprint_changes(previous: dict, current: dict) -> dict:
    old = previous.get("key_file_fingerprints", {})
    new = current.get("key_file_fingerprints", {})
    old_names, new_names = set(old), set(new)
    return {
        "added": sorted(new_names - old_names),
        "removed": sorted(old_names - new_names),
        "modified": sorted(name for name in old_names & new_names
                           if old[name].get("sha256") != new[name].get("sha256")),
    }


def make_plan(previous: dict, current: dict) -> dict:
    changed_fields = sorted(field for field in set(previous) | set(current)
                            if field not in {"generated_at", "tool_version", "key_file_fingerprints"}
                            and previous.get(field) != current.get(field))
    file_changes = fingerprint_changes(previous, current)
    current_docs = {path.name for path in DOC_DIR.glob("*.md")}
    recommendations = []
    for doc in sorted(expected_docs(current)):
        relevant = sorted(DOC_FIELDS.get(doc, set()) & set(changed_fields))
        if doc not in current_docs:
            action = "create"
            reason = "当前 ProjectDoc 中缺少该文档"
        elif relevant:
            action = "update"
            reason = "相关扫描事实发生变化"
        elif any(file_changes.values()) and doc in {"README.md", "USAGE.md", "ARCHITECTURE.md", "MODULES.md", "REGRESSION-TEST.md", "KNOWN-ISSUES.md"}:
            action = "review"
            reason = "关键文件发生变化，需要 AI 判断是否影响本文档"
        else:
            action = "preserve"
            reason = "未发现直接相关的扫描事实变化，保留旧内容"
        recommendations.append({
            "document": doc,
            "action": action,
            "reason": reason,
            "changed_report_fields": relevant,
        })
    return {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(),
        "project_root": str(ROOT),
        "baseline_available": bool(previous),
        "changed_report_fields": changed_fields,
        "key_file_changes": file_changes,
        "recommendations": recommendations,
        "ai_instructions": [
            "先阅读旧文档和 changed key files，再补充语义层面的影响说明。",
            "只原地修改 action=create/update/review 的文档；action=preserve 的文档不得重写。",
            "人工补充、历史决策和运维经验默认保留；只有新证据明确推翻时才修改。",
            "完成后运行 verify_handoff.py，不得把本计划当作已完成的更新。",
        ],
    }


def render_markdown(plan: dict) -> str:
    lines = [
        "# 交接文档增量更新建议",
        "",
        f"- 项目根目录：`{plan['project_root']}`",
        f"- 上次扫描基线：{'存在' if plan['baseline_available'] else '不存在（首次生成或旧报告缺失）'}",
        "",
        "## 关键文件变化",
        "",
    ]
    changes = plan["key_file_changes"]
    for label, key in (("新增", "added"), ("修改", "modified"), ("删除", "removed")):
        values = changes[key]
        lines.append(f"- {label}：" + (", ".join(f"`{value}`" for value in values) if values else "无"))
    lines.extend(["", "## 文档建议", "", "| 文档 | 动作 | 原因 | 变化字段 |", "|---|---|---|---|"])
    for item in plan["recommendations"]:
        fields = ", ".join(f"`{field}`" for field in item["changed_report_fields"]) or "-"
        lines.append(f"| `{item['document']}` | {item['action']} | {item['reason']} | {fields} |")
    lines.extend(["", "## AI 执行要求", ""])
    lines.extend(f"- {item}" for item in plan["ai_instructions"])
    lines.extend(["", "> 这是机器差异建议。AI 必须结合旧文档和源码补充真实影响，不能仅凭修改时间更新文档。", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="TempScr", help="Directory for update-plan JSON and Markdown")
    args = parser.parse_args()
    if not CURRENT_REPORT.exists():
        raise SystemExit("ERROR: 缺少 ProjectDoc/analysis-report.json，请先运行 analyze_project.py")
    current = load_json(CURRENT_REPORT)
    previous = load_json(PREVIOUS_REPORT)
    plan = make_plan(previous, current)
    output_dir = (ROOT / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "project-handoff-update-plan.json"
    md_path = output_dir / "project-handoff-update-plan.md"
    json_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(plan), encoding="utf-8")
    print(f"Update plan written to {md_path}")
    counts = {}
    for item in plan["recommendations"]:
        counts[item["action"]] = counts.get(item["action"], 0) + 1
    print("- " + ", ".join(f"{key}={value}" for key, value in sorted(counts.items())))


if __name__ == "__main__":
    force_utf8_console()
    main()

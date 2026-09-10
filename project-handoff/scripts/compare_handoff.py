#!/usr/bin/env python3
"""Compare current and previous scan reports and propose an incremental handoff update plan."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path

from _handoff_common import force_utf8_console
from _handoff_documents import selected_docs, load_document_plan, LEGACY_DOCS

ROOT = Path.cwd()
DOC_DIR = ROOT / "ProjectDoc"
CURRENT_REPORT = DOC_DIR / "analysis-report.json"
PREVIOUS_REPORT = DOC_DIR / ".handoff" / "analysis-report.previous.json"
VERIFIED_REPORT = DOC_DIR / ".handoff" / "analysis-report.verified.json"

DOC_FIELDS = {
    "readme.md": {"project_name", "package_manager", "frameworks", "ui_libraries", "npm_scripts", "git"},
    "usage.md": {"frameworks", "api_routes", "desktop", "npm_scripts", "lan_startup", "frontend_mock"},
    "architecture.md": {"frameworks", "monorepo", "database", "external_resources", "directory_tree", "native_embedded_ai"},
    "modules.md": {"frameworks", "directory_tree", "api_routes", "database", "native_embedded_ai"},
    "environment.md": {"environment_variables"},
    "deployment.md": {"docker", "cloudflare", "ci_cd", "kubernetes", "deployment_targets", "desktop"},
    "infrastructure.md": {"cloudflare", "external_resources", "monitoring", "git"},
    "ai-services.md": {"ai_services", "external_resources", "native_embedded_ai"},
    "api.md": {"api_routes", "api_specs"},
    "database.md": {"database"},
    "desktop.md": {"desktop"},
    "regression-test.md": {"testing", "npm_scripts", "frameworks", "desktop"},
    "known-issues.md": {"testing", "scan_completeness"},
    "maintenance.md": {"monitoring", "package_manager", "dependency_counts", "git"},
    "runbook.md": {"docker", "cloudflare", "database", "ai_services", "monitoring"},
}


for legacy, target in LEGACY_DOCS.items():
    DOC_FIELDS.setdefault(target, set()).update(DOC_FIELDS.pop(legacy, set()))


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def expected_docs(report: dict) -> set[str]:
    return selected_docs(report, load_document_plan(ROOT))


def fingerprint_changes(previous: dict, current: dict) -> dict:
    old = {**previous.get("key_file_fingerprints", {}), **previous.get("source_file_fingerprints", {})}
    new = {**current.get("key_file_fingerprints", {}), **current.get("source_file_fingerprints", {})}
    old_names, new_names = set(old), set(new)
    return {
        "added": sorted(new_names - old_names),
        "removed": sorted(old_names - new_names),
        "modified": sorted(name for name in old_names & new_names
                           if old[name].get("sha256") != new[name].get("sha256")),
    }


def run_git(args: list[str]) -> str:
    try:
        r = subprocess.run(["git", *args], capture_output=True, timeout=15, cwd=ROOT)
        if r.returncode != 0:
            return ""
        return r.stdout.decode("utf-8", errors="replace").strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def run_git_ok(args: list[str]) -> bool:
    """只看退出码的命令（如 cat-file -e、rev-parse），无 stdout 也能判断成功。"""
    try:
        return subprocess.run(["git", *args], capture_output=True, timeout=15, cwd=ROOT).returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def git_changes_since_baseline(previous: dict) -> dict:
    """自上次验收基线以来的 git 变更：优先用基线记录的 commit hash，其次用基线生成时间。"""
    result = {"available": False, "range": "", "commits": [], "diff_summary": "",
              "changed_files": [], "uncommitted_count": 0}
    if not run_git_ok(["rev-parse", "--is-inside-work-tree"]):
        return result
    base_hash = (previous.get("git") or {}).get("hash", "")
    if base_hash and run_git_ok(["cat-file", "-e", base_hash]):
        result["range"] = f"{base_hash}..HEAD"
    else:
        generated_at = previous.get("generated_at", "")
        if not generated_at:
            return result
        result["range"] = f"--since={generated_at}"
    log_args = ["log", "--date=short", "--format=%h %ad %s", result["range"], "-50"]
    commits = [line for line in run_git(log_args).splitlines() if line.strip()]
    result["commits"] = commits
    result["available"] = True
    if not result["range"].startswith("--since="):
        result["diff_summary"] = run_git(["diff", "--shortstat", result["range"]])
        changed = [line for line in run_git(["diff", "--name-only", result["range"]]).splitlines() if line.strip()]
        result["changed_files"] = changed[:100]
    dirty_files = set(run_git(['diff', '--name-only', 'HEAD']).splitlines()) | set(run_git(['ls-files', '--others', '--exclude-standard']).splitlines())
    dirty_files = {name for name in dirty_files if not name.startswith(('ProjectDoc/', 'TempScr/', 'TempFiles/'))}
    result['changed_files'] = sorted(set(result['changed_files']) | dirty_files)
    result["uncommitted_count"] = len([line for line in run_git(["status", "--porcelain"]).splitlines() if line.strip()])
    return result


def make_plan(previous: dict, current: dict, git_changes=None) -> dict:
    changed_fields = sorted(field for field in set(previous) | set(current)
                            if field not in {"generated_at", "tool_version", "key_file_fingerprints", "source_file_fingerprints", "source_fingerprints_complete"}
                            and previous.get(field) != current.get(field))
    file_changes = fingerprint_changes(previous, current)
    current_docs = {path.name.lower() for path in DOC_DIR.glob("*.md")}
    git_changes = git_changes or {}
    incomplete = not previous.get('source_fingerprints_complete') or not current.get('source_fingerprints_complete')
    needs_review = any(file_changes.values()) or bool(git_changes.get('changed_files') or git_changes.get('uncommitted_count')) or incomplete
    recommendations = []
    for doc in sorted(expected_docs(current)):
        relevant = sorted(DOC_FIELDS.get(doc, set()) & set(changed_fields))
        if doc not in current_docs:
            action = "create"
            reason = "当前 ProjectDoc 中缺少该文档"
        elif relevant:
            action = "update"
            reason = "相关扫描事实发生变化"
        elif needs_review:
            action = "review"
            reason = "源码/Git 发生变化或扫描证据不完整，需要 AI 判断是否影响本文档"
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
            "默认只修改 create/update/review；preserve 表示机器未发现影响，实际源码证据可推翻，须说明原因。",
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
    git = plan.get("git_changes", {})
    lines.extend(["", "## 自上次验收基线以来的 Git 变更", ""])
    if not git.get("available"):
        lines.append("- 未获取到（非 git 仓库、无基线或基线 commit 不在当前历史中）。仅依赖上方的报告字段/指纹差异。")
    else:
        lines.append(f"- 范围：`{git['range']}`" + (f"，另有 {git['uncommitted_count']} 个未提交变更" if git.get("uncommitted_count") else "，无未提交变更"))
        if git.get("diff_summary"):
            lines.append(f"- 变更规模：{git['diff_summary']}")
        if git.get("commits"):
            lines.append("- Commit 列表（最多 50 条）：")
            lines.extend(f"  - `{c}`" for c in git["commits"])
        else:
            lines.append("- Commit 列表：基线以来无新提交")
        if git.get("changed_files"):
            lines.append("- 变更文件（最多 100 个）：" + ", ".join(f"`{f}`" for f in git["changed_files"]))
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
    # git 范围优先以最近一次验收通过的 verified 基线为准，其次才是 previous
    git_baseline = load_json(VERIFIED_REPORT) or previous
    git_changes = git_changes_since_baseline(git_baseline)
    plan = make_plan(previous, current, git_changes)
    plan["git_changes"] = git_changes
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
    git = plan["git_changes"]
    if git.get("available"):
        print(f"- git: {len(git['commits'])} 条新 commit（范围 {git['range']}）"
              + (f"，{git['uncommitted_count']} 个未提交变更" if git["uncommitted_count"] else ""))
    else:
        print("- git: 未获取到基线以来的变更记录")


if __name__ == "__main__":
    force_utf8_console()
    main()

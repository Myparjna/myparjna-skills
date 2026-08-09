#!/usr/bin/env python3
"""生成交接文档计划（handoff-plan）：模式判定 + 文档生成/跳过清单 + 每份 focus + 扫描范围。

在 analyze_project.py 之后、generate_handoff.py 之前运行。
计划写入 TempScr/project-handoff-plan.{json,md}，AI 必须先向用户展示并确认；
用户可直接编辑 plan 文件调整 action/focus，generate_handoff.py 会读取并尊重 skip 决策。
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from _handoff_common import force_utf8_console

ROOT = Path.cwd()
DOC_DIR = ROOT / "ProjectDoc"
REPORT_PATH = DOC_DIR / "analysis-report.json"
CONFIG_PATH = ROOT / ".handoff.yml"

# 门禁强制要求的文档（verify_handoff.py REQUIRED_DOCS），计划中不得跳过
MANDATORY = {"README.md", "USAGE.md", "ARCHITECTURE.md", "MODULES.md",
             "ENVIRONMENT.md", "DEPLOYMENT.md", "REGRESSION-TEST.md"}

# 每份文档的一句话 focus（写进计划，供 AI 填写时聚焦）
FOCUS = {
    "README.md": "30 秒看懂项目 + 快速启动 + 速查卡；待确认问题全部汇总到顶部",
    "USAGE.md": "从真实用户角色出发的核心业务流程，启动不等于使用",
    "ARCHITECTURE.md": "mermaid 架构图、数据流、技术选型理由、AI 工具链痕迹",
    "MODULES.md": "按业务职责划分模块，至少两条真实调用链并引用源码路径",
    "ENVIRONMENT.md": "每个变量的用途/获取方式/必需性/泄露影响，不遗漏、不写真实值",
    "DEPLOYMENT.md": "按检测到的平台分章节写完整可复制的部署命令",
    "INFRASTRUCTURE.md": "域名/DNS/SSL/第三方账号清单与交接动作",
    "AI-SERVICES.md": "AI API 的调用点、模型、计费限额与降级行为",
    "API.md": "接口清单以扫描为准，鉴权方式读源码确认",
    "DATABASE.md": "数据模型、迁移流程、备份恢复命令",
    "DESKTOP.md": "构建打包命令、代码签名与自动更新现状",
    "REGRESSION-TEST.md": "区分检测到/已执行/已通过，写清测试缺口",
    "KNOWN-ISSUES.md": "宁可多写不可隐瞒：Bug、半成品功能、技术债",
    "MAINTENANCE.md": "看日志/看账单/查漏洞的精确入口",
    "RUNBOOK.md": "回滚命令、故障→处置对照表",
}

# 总是生成的基础文档
BASE_DOCS = ["README.md", "USAGE.md", "ARCHITECTURE.md", "MODULES.md", "ENVIRONMENT.md",
             "DEPLOYMENT.md", "INFRASTRUCTURE.md", "REGRESSION-TEST.md", "KNOWN-ISSUES.md",
             "MAINTENANCE.md", "RUNBOOK.md"]


def load_report() -> dict:
    if not REPORT_PATH.exists():
        raise SystemExit("ERROR: 缺少 ProjectDoc/analysis-report.json，请先运行 analyze_project.py")
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def read_config() -> dict:
    """读 .handoff.yml 中用户已配置的扫描范围（与 analyze_project.py 同样的简单解析）。"""
    cfg = {"skip_dirs": [], "max_files": None}
    if not CONFIG_PATH.exists():
        return cfg
    try:
        for line in CONFIG_PATH.read_text(encoding="utf-8").splitlines():
            line = line.split("#", 1)[0].strip()
            if not line or ":" not in line:
                continue
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip()
            if key == "skip_dirs" and val.startswith("["):
                cfg["skip_dirs"] = [s.strip().strip("'\"") for s in val.strip("[]").split(",") if s.strip()]
            elif key == "max_files" and val.isdigit():
                cfg["max_files"] = int(val)
    except OSError:
        pass
    return cfg


def detect_mode(report: dict, intent: str) -> tuple[str, str]:
    """判定 create/update/rebuild，返回 (mode, reason)。"""
    generated_names = set(BASE_DOCS) | {"AI-SERVICES.md", "API.md", "DATABASE.md", "DESKTOP.md"}
    existing = sorted(p.name for p in DOC_DIR.glob("*.md") if p.name in generated_names)
    if intent != "auto":
        reason = f"用户通过 --intent {intent} 显式指定"
        if intent == "create" and existing:
            raise SystemExit(f"ERROR: --intent create 但已存在交接文档（{len(existing)} 份）。"
                             "请使用 update，或经用户明确同意后使用 rebuild。")
        return intent, reason
    if existing:
        return "update", f"检测到 {len(existing)} 份已有交接文档，默认增量更新"
    return "create", "未检测到已有交接文档，首次创建"


def conditional_docs(report: dict) -> list[tuple[str, bool, str]]:
    """条件文档及其检测证据，返回 (name, detected, evidence)。"""
    ai = report.get("ai_services", {})
    ai_hit = bool(ai.get("sdks") or ai.get("endpoints") or ai.get("model_names"))
    ai_evi = ", ".join(s["package"] for s in ai.get("sdks", [])[:3]) or \
        ", ".join(e["value"] for e in ai.get("endpoints", [])[:2]) or "模型名出现"
    db = report.get("database", {})
    db_hit = bool(db.get("clients") or db.get("orm"))
    db_evi = ", ".join(db.get("clients", []) + db.get("orm", []))
    return [
        ("AI-SERVICES.md", ai_hit, ai_evi),
        ("API.md", bool(report.get("api_routes")), f"{len(report.get('api_routes', []))} 条 API 路由"),
        ("DATABASE.md", db_hit, db_evi),
        ("DESKTOP.md", bool(report.get("desktop")),
         ", ".join(d["type"] for d in report.get("desktop", []))),
    ]


def build_plan(report: dict, intent: str, client_level: str) -> dict:
    mode, mode_reason = detect_mode(report, intent)
    documents = []
    for name in BASE_DOCS:
        documents.append({
            "name": name,
            "action": "generate",
            "required": name in MANDATORY,
            "reason": "门禁必需文档" if name in MANDATORY else "基础交接文档",
            "focus": FOCUS[name],
        })
    for name, detected, evidence in conditional_docs(report):
        documents.append({
            "name": name,
            "action": "generate" if detected else "skip",
            "required": False,
            "reason": f"检测到：{evidence}" if detected else "未检测到相关事实，跳过",
            "focus": FOCUS[name],
        })
    completeness = report.get("scan_completeness", {})
    cfg = read_config()
    scope_notes = []
    if completeness.get("truncated"):
        scope_notes.append(
            f"扫描在 {completeness.get('scanned_files')} 个文件处截断（共 "
            f"{completeness.get('total_files')} 个）。如关键配置被截断，可在 .handoff.yml "
            "的 skip_dirs 追加噪音目录后重新运行 analyze_project.py。")
    if cfg["skip_dirs"]:
        scope_notes.append(f"当前 .handoff.yml 额外跳过目录：{', '.join(cfg['skip_dirs'])}")
    if not scope_notes:
        scope_notes.append("扫描完整，无需调整范围。")
    return {
        "schema_version": 1,
        "generated_at": datetime.now().astimezone().isoformat(),
        "project_root": str(ROOT),
        "mode": mode,
        "mode_reason": mode_reason,
        "client_level": client_level,
        "documents": documents,
        "scope": {
            "total_files": completeness.get("total_files"),
            "scanned_files": completeness.get("scanned_files"),
            "truncated": bool(completeness.get("truncated")),
            "skip_dirs_extra": cfg["skip_dirs"],
            "max_files": cfg["max_files"],
            "notes": scope_notes,
        },
        "ai_instructions": [
            "先把本计划展示给用户确认（模式、文档清单、focus、范围），用户可编辑 plan 文件调整后再继续。",
            "generate_handoff.py 会读取本计划并跳过 action=skip 的文档。",
            "required=true 的文档是门禁硬要求，跳过会导致 verify 失败。",
            "update 模式下本计划只判定模式与缺失文档；具体章节影响仍以 compare_handoff.py 的更新建议为准。",
        ],
    }


def render_markdown(plan: dict) -> str:
    lines = [
        "# 交接文档生成计划（handoff-plan）",
        "",
        f"- 项目根目录：`{plan['project_root']}`",
        f"- 模式：**{plan['mode']}**（{plan['mode_reason']}）",
        f"- 受众级别：`{plan['client_level']}`",
        "",
        "## 文档清单",
        "",
        "| 文档 | 动作 | 必需 | 原因 | focus |",
        "|---|---|---|---|---|",
    ]
    for doc in plan["documents"]:
        required = "是" if doc["required"] else ""
        lines.append(f"| `{doc['name']}` | **{doc['action']}** | {required} | {doc['reason']} | {doc['focus']} |")
    scope = plan["scope"]
    lines.extend([
        "",
        "## 扫描范围",
        "",
        f"- 文件总数：{scope['total_files']}，实际扫描：{scope['scanned_files']}"
        + ("（**已截断**）" if scope["truncated"] else ""),
        f"- .handoff.yml 额外跳过目录：{', '.join(scope['skip_dirs_extra']) or '无'}",
    ])
    lines.extend(f"- {note}" for note in scope["notes"])
    lines.extend(["", "## 执行要求", ""])
    lines.extend(f"- {item}" for item in plan["ai_instructions"])
    lines.extend([
        "",
        "> 请用户确认或修改本计划（可直接编辑 project-handoff-plan.json 中的 action/focus），",
        "> 确认后再运行 generate_handoff.py。",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate handoff plan for user review")
    parser.add_argument("--intent", default="auto", choices=["auto", "create", "update", "rebuild"],
                        help="用户已明确的模式意向；auto 按现有文档自动判定")
    parser.add_argument("--client-level", default="developer",
                        choices=["non-technical", "developer", "devops"])
    parser.add_argument("--output-dir", default="TempScr")
    args = parser.parse_args()

    report = load_report()
    plan = build_plan(report, args.intent, args.client_level)
    output_dir = (ROOT / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "project-handoff-plan.json"
    md_path = output_dir / "project-handoff-plan.md"
    json_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(plan), encoding="utf-8")

    generate_count = sum(1 for d in plan["documents"] if d["action"] == "generate")
    skip_count = len(plan["documents"]) - generate_count
    print(f"Handoff plan written to {md_path}")
    print(f"- 模式: {plan['mode']}（{plan['mode_reason']}）")
    print(f"- 文档: 生成 {generate_count} 份，跳过 {skip_count} 份")
    print("下一步: 向用户展示计划并等待确认；确认后运行 generate_handoff.py。")


if __name__ == "__main__":
    force_utf8_console()
    main()

#!/usr/bin/env python3
"""交接文档质量门禁：检查未填 TODO、密钥泄露、编造痕迹、覆盖率。退出码非 0 表示未通过。"""
from pathlib import Path
import json
import re
import sys

ROOT = Path.cwd()
OUT = ROOT / "ProjectDoc"
REPORT_PATH = OUT / "analysis-report.json"

# 必需文档列表
REQUIRED_DOCS = {"README.md", "ENVIRONMENT.md", "DEPLOYMENT.md"}
MIN_DOC_COUNT = 5

# 真实密钥特征（高置信度模式，避免误报变量名）
SECRET_PATTERNS = [
    (r"sk-[a-zA-Z0-9]{20,}", "OpenAI/DeepSeek 风格 API key"),
    (r"sk-ant-[a-zA-Z0-9-]{20,}", "Anthropic API key"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub PAT"),
    (r"github_pat_[a-zA-Z0-9_]{20,}", "GitHub fine-grained PAT"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key"),
    (r"AIza[0-9A-Za-z_-]{35}", "Google API key"),
    (r"xox[baprs]-[a-zA-Z0-9-]{10,}", "Slack token"),
    (r"eyJhbGciOi[a-zA-Z0-9_.-]{40,}", "JWT"),
    (r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----", "私钥"),
    # 中国云厂商
    (r"(?i)(?:LTAI|LTAI)[a-zA-Z0-9]{12,}", "阿里云 AccessKey"),
    (r"(?i)AKID[a-zA-Z0-9]{13,}", "腾讯云 SecretId"),
    (r"(?i)AKSK[a-zA-Z0-9]{13,}", "腾讯云 SecretKey"),
    # Cloudflare
    (r"cf_[a-zA-Z0-9_-]{20,}", "Cloudflare API Token"),
    # Vercel
    (r"(?i)vercel_[a-zA-Z0-9]{20,}", "Vercel Token"),
    # npm / PyPI
    (r"npm_[a-zA-Z0-9]{36}", "npm access token"),
    (r"pypi-[a-zA-Z0-9_-]{20,}", "PyPI token"),
    # 数据库连接串密码
    (r"(?i)(?:postgres|mysql|mongodb|redis)://[^:]+:([^@\s]{8,})@", "数据库连接串密码"),
    # 通用硬编码凭据
    (r"(?i)(password|passwd|secret|token|api_?key)\s*[:=]\s*['\"][^'\"\s]{12,}['\"]", "疑似硬编码凭据"),
]

# 编造/敷衍痕迹
WEASEL_PATTERNS = [
    (r"(?i)\b(it depends|视情况而定)\b", "含糊措辞"),
    (r"(此处|这里)?(略|省略|从略)。?$", "省略未写"),
    (r"(?i)\b(example\.com|your-api-key|your-domain|YOUR_[A-Z_]+|<[a-z-]+-here>)\b", "占位符未替换"),
    (r"等等[。\s]*$", "用'等等'结尾敷衍"),
    (r"(?i)(as an ai|作为(一个)?\s*AI)", "AI 自指泄漏"),
    # 新增敷衍模式
    (r"(?i)^.{0,10}(一般来说|通常来说|通常|一般而言)", "含糊开头"),
    (r"(?i)(建议参考|请参考|详见官方文档)", "敷衍引用"),
    (r"(此处暂不展开|暂不详述|不做展开)", "逃避展开"),
    (r"(后续补充|待后续完善|以后再)", "拖延未写"),
    (r"(?i)(具体取决于|要看具体情况)", "含糊推诿"),
    (r"(?i)(理论上|原则上|应该是)", "不确定表态"),
]

# TODO 变体检测（防止 AI 用变体绕过）
TODO_VARIANTS = re.compile(
    r"<!--\s*(?:TODO|AI_TODO|FIXME|待办|待填写)\s*[:：]",
    re.IGNORECASE,
)

ALLOWED_UNCONFIRMED = re.compile(r"\[需向交接人确认:[^\]]+\]")


def load_report():
    if not REPORT_PATH.exists():
        sys.exit("ERROR: 缺少 ProjectDoc/analysis-report.json")
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def check_doc(path: Path, report):
    issues = []   # (severity, message)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1. 未填 TODO（包括变体）
    for i, line in enumerate(lines, 1):
        if "TODO(AI)" in line:
            issues.append(("ERROR", f"L{i}: 未填写的 TODO(AI)"))
        elif TODO_VARIANTS.search(line):
            issues.append(("WARN", f"L{i}: 疑似 TODO 变体（可能绕过检测）: {line.strip()[:60]}"))

    # 2. 密钥泄露（最高级别）
    for pattern, label in SECRET_PATTERNS:
        for m in re.finditer(pattern, text):
            ln = text[:m.start()].count("\n") + 1
            issues.append(("CRITICAL", f"L{ln}: 疑似泄露真实密钥（{label}）—— 必须移除，改为'通过安全渠道交接'"))

    # 3. 编造/敷衍痕迹
    for pattern, label in WEASEL_PATTERNS:
        for i, line in enumerate(lines, 1):
            if "TODO(AI)" in line:
                continue
            if re.search(pattern, line):
                issues.append(("WARN", f"L{i}: {label} -> {line.strip()[:60]}"))

    # 4. 空章节（标题后直接接下一个标题或文件结尾）
    for i, line in enumerate(lines):
        if line.startswith("## "):
            body = []
            for nxt in lines[i + 1:]:
                if nxt.startswith("## "):
                    break
                if nxt.strip():
                    body.append(nxt)
            if not body:
                issues.append(("ERROR", f"空章节: {line.strip()}"))

    # 5. 文档中引用的文件路径必须真实存在
    for m in re.finditer(r"`([\w./-]+\.(?:py|ts|tsx|js|jsx|json|toml|yaml|yml|env|md|prisma|sql|go|rs|rb|java|kt))`", text):
        ref = m.group(1).lstrip("./")
        if ref.startswith(("ProjectDoc/", "http")) or "*" in ref:
            continue
        if not (ROOT / ref).exists() and not list(ROOT.glob(f"**/{Path(ref).name}")):
            ln = text[:m.start()].count("\n") + 1
            issues.append(("WARN", f"L{ln}: 引用的文件不存在: `{ref}`（确认是否编造）"))

    return issues, text


def check_doc_count(docs):
    """检查文档数量和必需文档。"""
    issues = []
    doc_names = {p.name for p in docs}

    if len(docs) < MIN_DOC_COUNT:
        issues.append(("ERROR", f"文档数量不足：只有 {len(docs)} 份，最少需要 {MIN_DOC_COUNT} 份"))

    for required in REQUIRED_DOCS:
        if required not in doc_names:
            issues.append(("ERROR", f"缺少必需文档: {required}"))

    return issues


def check_residual_docs(docs, report):
    """检查是否有上次运行残留的多余文档。"""
    issues = []
    # 生成器应该产出的文档列表
    expected = {"README.md", "ARCHITECTURE.md", "ENVIRONMENT.md", "DEPLOYMENT.md",
                "INFRASTRUCTURE.md", "KNOWN-ISSUES.md", "MAINTENANCE.md", "RUNBOOK.md"}
    ai = report.get("ai_services", {})
    if ai.get("sdks") or ai.get("endpoints"):
        expected.add("AI-SERVICES.md")
    if report.get("api_routes"):
        expected.add("API.md")
    if report.get("database", {}).get("clients") or report.get("database", {}).get("orm"):
        expected.add("DATABASE.md")
    if report.get("desktop"):
        expected.add("DESKTOP.md")

    actual = {p.name for p in docs}
    residual = actual - expected - {"analysis-report.json", "ProjectDoc-package.zip"}
    if residual:
        issues.append(("WARN", f"发现可能的残留文档: {', '.join(residual)}（上次运行遗留？）"))
    return issues


def check_coverage(report, all_text):
    """扫描报告中的关键事实必须在文档中被覆盖。使用词边界匹配避免误报。"""
    issues = []
    env = report["environment_variables"]
    for v in env["declared"]:
        # 使用词边界匹配，避免短变量名误报
        if not re.search(r"\b" + re.escape(v["name"]) + r"\b", all_text):
            issues.append(("ERROR", f"环境变量 `{v['name']}` 未在任何文档中说明"))
    for name in env["used_but_not_declared"]:
        if not re.search(r"\b" + re.escape(name) + r"\b", all_text):
            issues.append(("ERROR", f"源码中使用的变量 `{name}` 未在任何文档中说明"))
    # CI/CD secrets（新版结构）
    ci = report.get("ci_cd", {})
    for wf in ci.get("github_actions", []):
        for s in wf["secrets_used"]:
            if not re.search(r"\b" + re.escape(s) + r"\b", all_text):
                issues.append(("ERROR", f"CI secret `{s}` 未在文档中说明获取/配置方式"))
    w = report.get("cloudflare", {}).get("wrangler")
    if w:
        for b in w.get("kv_namespaces", []) + w.get("d1_databases", []) + w.get("r2_buckets", []):
            if not re.search(r"\b" + re.escape(b) + r"\b", all_text):
                issues.append(("WARN", f"Cloudflare 绑定 `{b}` 未在文档中说明"))
    for s in report["ai_services"]["sdks"]:
        if not re.search(r"\b" + re.escape(s["sdk"]) + r"\b", all_text) and \
           not re.search(r"\b" + re.escape(s["package"]) + r"\b", all_text):
            issues.append(("WARN", f"AI SDK `{s['package']}` 未在文档中说明用途"))
    return issues


def check_scan_warnings(report):
    """检查扫描完整性警告。"""
    issues = []
    scan = report.get("scan_completeness", {})
    if scan.get("truncated"):
        issues.append(("WARN", f"扫描被截断：项目有 {scan.get('total_files', '?')} 文件，"
                       f"仅扫描了 {scan.get('scanned_files', '?')}（上限 {scan.get('max_files', '?')}）。"
                       "部分技术栈可能未被检测到。"))
    return issues


def collect_unconfirmed(all_text):
    """收集所有 [需向交接人确认:...] 标记。"""
    items = []
    for line in all_text.splitlines():
        if "TODO(AI)" in line:
            continue
        items.extend(ALLOWED_UNCONFIRMED.findall(line))
    return items


def count_unconfirmed(text):
    return len(collect_unconfirmed(text))


def main():
    report = load_report()
    docs = sorted(p for p in OUT.glob("*.md"))
    if not docs:
        sys.exit("ERROR: ProjectDoc/ 下没有文档，先运行 generate_handoff.py")

    total = {"CRITICAL": 0, "ERROR": 0, "WARN": 0}
    all_text = ""

    # 文档数量和必需文档检查
    print("=" * 50)
    print("Project Handoff 质量门禁")
    print("=" * 50)

    # 扫描完整性警告
    print("\n— 扫描完整性 —")
    scan_issues = check_scan_warnings(report)
    for sev, msg in scan_issues:
        total[sev] += 1
        print(f"    [{sev}] {msg}")
    if not scan_issues:
        print("    [OK] 扫描完整")

    print("\n— 文档结构检查 —")
    struct_issues = check_doc_count(docs)
    for sev, msg in struct_issues:
        total[sev] += 1
        print(f"    [{sev}] {msg}")
    if not struct_issues:
        print(f"    [OK] 文档数量 {len(docs)} 份，必需文档齐全")

    # 残留文档检查
    residual_issues = check_residual_docs(docs, report)
    for sev, msg in residual_issues:
        total[sev] += 1
        print(f"    [{sev}] {msg}")

    for doc in docs:
        issues, text = check_doc(doc, report)
        all_text += text
        unconfirmed = count_unconfirmed(text)
        status = "[FAIL]" if any(s in ("CRITICAL", "ERROR") for s, _ in issues) else "[OK]"
        print(f"\n{status} {doc.name}" + (f"  ({unconfirmed} 处待确认标记，允许)" if unconfirmed else ""))
        for sev, msg in issues:
            total[sev] += 1
            print(f"    [{sev}] {msg}")

    print("\n— 覆盖率检查 —")
    cov = check_coverage(report, all_text)
    for sev, msg in cov:
        total[sev] += 1
        print(f"    [{sev}] {msg}")
    if not cov:
        print("    全部关键事实已覆盖")

    # 汇总待确认标记
    unconfirmed_all = collect_unconfirmed(all_text)
    if unconfirmed_all:
        print(f"\n— 待确认标记汇总（{len(unconfirmed_all)} 处） —")
        for item in unconfirmed_all:
            print(f"    - {item}")
        print("    [INFO] 待确认标记是合法交接事项，不阻止打包；请交接人后续逐项确认。")

    print(f"\n汇总: CRITICAL={total['CRITICAL']}  ERROR={total['ERROR']}  WARN={total['WARN']}")
    if total["CRITICAL"]:
        print("结论: 存在密钥泄露风险，禁止交付。")
        sys.exit(2)
    if total["ERROR"]:
        print("结论: 未通过。修复所有 ERROR 后重新运行。")
        sys.exit(1)
    print("结论: 通过。WARN 项建议人工复核一遍。")


if __name__ == "__main__":
    main()

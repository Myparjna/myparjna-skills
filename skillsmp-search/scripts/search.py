#!/usr/bin/env python3
"""SkillsMP Search - 搜索 SkillsMP 技能市场，仅执行关键字搜索；ai 为兼容别名"""

from pathlib import Path
import urllib.error
import urllib.request
import urllib.parse
import json
import argparse
import os
import sys

# Windows 控制台 UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

API_BASE = "https://skillsmp.com/api/v1/skills"
CONFIG_PATH = Path(os.environ.get("APPDATA", Path.home() / ".config")) / "skillsmp-search" / "config.json"

# ⚠️ 本地默认凭据：仅限本机使用。
# 上传 GitHub 或其他公开仓库前，必须先运行 scripts/check-secrets.py 并移除该值。
DEFAULT_API_KEY = ""  # 上传版置空；本机开发版保留，改用环境变量或 config.json


def get_api_key():
    key = os.environ.get("SKILLSMP_API_KEY", "").strip()
    if key:
        return key
    try:
        data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        key = data.get("api_key") if isinstance(data, dict) else None
        if isinstance(key, str) and key.strip():
            return key.strip()
    except FileNotFoundError:
        pass
    except (OSError, ValueError):
        raise RuntimeError("Invalid local credential configuration") from None
    if DEFAULT_API_KEY:
        return DEFAULT_API_KEY
    raise RuntimeError("Set SKILLSMP_API_KEY or configure " + str(CONFIG_PATH))


def _request(url):
    """发起 HTTP GET 请求，返回 (parsed_json, rate_limit_remaining)"""
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {get_api_key()}",
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        remaining = resp.headers.get("X-RateLimit-Daily-Remaining", "?")
        data = json.loads(resp.read().decode("utf-8"))
        return data, remaining


def search_keyword(query, page=1, limit=20, sort_by="recent",
                   category=None, occupation=None):
    """关键字搜索 → (data, remaining)"""
    if page < 1 or not 1 <= limit <= 100:
        raise ValueError("page must be >= 1; limit must be 1..100")
    params = {
        "q": query, "page": page, "limit": min(limit, 100),
        "sortBy": sort_by,
    }
    if category:
        params["category"] = category
    if occupation:
        params["occupation"] = occupation
    url = f"{API_BASE}/search?{urllib.parse.urlencode(params)}"
    return _request(url)


def search_ai(query, page=1, limit=20, sort_by="recent", category=None, occupation=None):
    """Compatibility alias: always executes keyword search."""
    return search_keyword(query, page, limit, sort_by, category, occupation)


def _extract_skills(data):
    """从响应中提取 skills 列表，兼容不同 API 结构"""
    if not data.get("success"):
        return [], 0
    payload = data.get("data", data)
    if not isinstance(payload, dict):
        raise ValueError("Invalid API payload")
    skills = payload.get("skills", payload.get("results", []))
    if not isinstance(skills, list) or not all(isinstance(s, dict) for s in skills):
        raise ValueError("Invalid skills list")
    total = payload.get("total", payload.get("pagination", {}).get("total", payload.get("count", len(skills))))
    return skills, total


def format_human(skills, total, mode_label, remaining):
    """人类可读的格式化输出"""
    if not skills:
        return f"{mode_label}: 未找到匹配的 Skills"

    lines = [
        f"{mode_label}搜索结果（共 {total} 个，显示 {len(skills)} 个）",
        f"   配额剩余: {remaining} 次/天\n",
    ]

    for i, s in enumerate(skills, 1):
        name = s.get("name") or s.get("skill_name") or s.get("title") or "未知"
        desc = s.get("description") or s.get("short_description") or ""
        install = s.get("install_command") or s.get("install") or ""
        stars = s.get("stars") or s.get("github_stars") or s.get("stargazers_count", "")
        author = s.get("author") or s.get("owner") or ""
        cats = s.get("category") or s.get("categories") or ""

        lines.append(f"{'─' * 56}")
        header = f"{i}. {name}"
        if stars:
            header += f"  {stars}"
        lines.append(header)

        if author:
            lines.append(f"   作者: {author}")
        if cats:
            if isinstance(cats, list):
                cats = " / ".join(str(c) for c in cats)
            lines.append(f"   分类: {cats}")
        if desc:
            short = desc[:160] + "..." if len(desc) > 160 else desc
            lines.append(f"   {short}")
        if install:
            lines.append(f"   安装: {install}")

    lines.append(f"{'─' * 56}")
    return "\n".join(lines)


def format_json(skills, total, mode_label, remaining):
    """JSON 格式输出，方便 Agent 机器解析"""
    result = {
        "mode": mode_label,
        "total": total,
        "remaining_quota": int(remaining) if remaining.isdigit() else remaining,
        "skills": skills,
    }
    return json.dumps(result, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="SkillsMP Search - 搜索技能市场",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s -q "前端设计"
  %(prog)s -q "如何自动化浏览器" --mode ai
  %(prog)s -q "automation" --sort-by stars --limit 5
  %(prog)s -q "devops" --json
        """,
    )
    parser.add_argument("--mode", choices=["keyword", "ai"], default="keyword",
                        help="搜索模式 (默认: keyword)")
    parser.add_argument("--query", "-q", required=True, help="搜索关键字或自然语言查询")
    parser.add_argument("--page", type=int, default=1, help="页码 (默认: 1)")
    parser.add_argument("--limit", type=int, default=20, help="每页数量 (默认: 20)")
    parser.add_argument("--sort-by", choices=["stars", "recent"], default="recent",
                        help="排序方式 (默认: recent)")
    parser.add_argument("--category", default=None, help="按分类过滤，传 slug")
    parser.add_argument("--occupation", default=None, help="按 SOC 职业过滤")
    parser.add_argument("--json", dest="json_output", action="store_true",
                        help="输出 JSON 格式")

    args = parser.parse_args()

    if args.page < 1 or not 1 <= args.limit <= 100 or not args.query.strip():
        parser.error("page must be >= 1; limit must be 1..100; query must not be empty")
    try:
        data, remaining = search_keyword(
            args.query, args.page, args.limit,
            args.sort_by, args.category, args.occupation,
        )
        mode_label = "keyword"
        if not isinstance(data, dict) or not data.get("success"):
            raise RuntimeError("API reported an unsuccessful response")

        skills, total = _extract_skills(data)

        if args.json_output:
            print(format_json(skills, total, mode_label, remaining))
        else:
            print(format_human(skills, total, mode_label, remaining))

    except urllib.error.HTTPError as e:
        print(json.dumps({"error": {"code": "HTTP_ERROR", "status": e.code}}), file=sys.stderr)
        sys.exit(1)
    except (urllib.error.URLError, TimeoutError):
        print(json.dumps({"error": {"code": "NETWORK_ERROR"}}), file=sys.stderr)
        sys.exit(1)
    except Exception:
        # Never echo response bodies, request headers or credential values.
        print(json.dumps({"error": {"code": "REQUEST_FAILED", "message": "Check credentials, local config and API response"}}), file=sys.stderr)
        sys.exit(1)



if __name__ == "__main__":
    main()

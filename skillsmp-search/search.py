#!/usr/bin/env python3
"""SkillsMP Search - 搜索 SkillsMP 技能市场，支持关键字搜索和 AI 语义搜索"""

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
API_KEY = os.environ.get(
    "SKILLSMP_API_KEY",
    "sk_live_skillsmp_rzPZyj6RIeJwWje4Ti1ohTmWfbKdZrFfIg8dXiNbqRc"
)


def _request(url):
    """发起 HTTP GET 请求，返回 (parsed_json, rate_limit_remaining)"""
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        remaining = resp.headers.get("X-RateLimit-Daily-Remaining", "?")
        data = json.loads(resp.read().decode("utf-8"))
        return data, remaining


def search_keyword(query, page=1, limit=20, sort_by="recent",
                   category=None, occupation=None):
    """关键字搜索 → (data, remaining)"""
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


def search_ai(query):
    """AI 语义搜索（降级到关键字搜索，因官方无此端点）→ (data, remaining)"""
    # SkillsMP 官方 API 不支持 ai-search 端点，降级到关键字搜索
    params = {"q": query, "limit": 20}
    url = f"{API_BASE}/search?{urllib.parse.urlencode(params)}"
    return _request(url)


def _extract_skills(data):
    """从响应中提取 skills 列表，兼容不同 API 结构"""
    if not data.get("success"):
        return [], 0
    payload = data.get("data", data)
    skills = payload.get("skills", payload.get("results", []))
    total = payload.get("total", payload.get("count", len(skills)))
    return skills, total


def format_human(skills, total, mode_label, remaining):
    """人类可读的格式化输出"""
    if not skills:
        return "📭 未找到匹配的 Skills"

    lines = [
        f"🔍 {mode_label}搜索结果（共 {total} 个，显示 {len(skills)} 个）",
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
            header += f"  ⭐ {stars}"
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
                        help="排序方式 (默认: recent，仅 keyword 模式)")
    parser.add_argument("--category", default=None, help="按分类过滤，传 slug (仅 keyword)")
    parser.add_argument("--occupation", default=None, help="按 SOC 职业过滤 (仅 keyword)")
    parser.add_argument("--json", dest="json_output", action="store_true",
                        help="输出 JSON 格式")

    args = parser.parse_args()

    try:
        if args.mode == "ai":
            data, remaining = search_ai(args.query)
            mode_label = "AI 语义"
        else:
            data, remaining = search_keyword(
                args.query, args.page, args.limit,
                args.sort_by, args.category, args.occupation,
            )
            mode_label = "关键字"

        if not data.get("success"):
            err = data.get("error", {})
            msg = f"❌ 搜索失败: {err.get('message', '未知错误')} (code: {err.get('code', 'N/A')})"
            print(msg, file=sys.stderr)
            sys.exit(1)

        skills, total = _extract_skills(data)

        if args.json_output:
            print(format_json(skills, total, mode_label, remaining))
        else:
            print(format_human(skills, total, mode_label, remaining))

    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        try:
            err = json.loads(body).get("error", {})
            code = err.get("code", "HTTP_ERROR")
            msg = err.get("message", body)
        except (json.JSONDecodeError, AttributeError):
            code = "HTTP_ERROR"
            msg = body
        print(f"❌ API 错误 ({e.code}): [{code}] {msg}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"❌ 网络错误: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ 请求失败: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

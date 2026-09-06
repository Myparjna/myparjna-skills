#!/usr/bin/env python3
"""ModelScope Model Search - discover and compare models on modelscope.cn."""

import argparse
import io
import json
import sys
from urllib.parse import quote


def validate_pagination(page, limit):
    if page < 1 or not 1 <= limit <= 100:
        raise ValueError("page must be >= 1; limit must be 1..100")


def response_data(response):
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, dict) or data.get("Code") != 200 or not isinstance(data.get("Data"), dict):
        raise RuntimeError("Invalid or unsuccessful API response")
    return data["Data"]

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)

API_URL = "https://www.modelscope.cn/api/v1/models/"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (modelscope-search-skill/1.0)",
}


def search_models(query: str, page: int = 1, page_size: int = 20) -> dict:
    """Search models by keyword."""
    validate_pagination(page, page_size)
    body = {"Name": query, "PageNumber": page, "PageSize": page_size}
    r = requests.put(API_URL, json=body, headers=HEADERS, timeout=15)
    return response_data(r)


def get_model_detail(model_id: str) -> dict:
    """Get details for a specific model (org/name format)."""
    parts = model_id.split("/")
    if len(parts) != 2 or any(not p.strip() or p in (".", "..") for p in parts):
        raise ValueError("model must be org/name")
    # Verified against official HubApi.get_model(revision=None), v1.37.1.
    url = API_URL + "/".join(quote(p, safe="") for p in parts)
    return response_data(requests.get(url, headers=HEADERS, timeout=15))


def format_model(m: dict) -> dict:
    """Extract relevant fields from a model dict."""
    # ModelScope can return `Tasks: null` for community checkpoints.
    tasks = m.get("Tasks") or []
    task_names = [t.get("TaskChineseName") or t.get("Task", "") for t in tasks[:3]]
    return {
        "path": f"{m.get('Path', '?')}/{m.get('Name', '?')}",
        "name": m.get("Name", ""),
        "chinese_name": m.get("ChineseName", ""),
        "downloads": (m.get("Downloads") or 0),
        "stars": (m.get("Stars") or 0),
        "license": m.get("License", ""),
        "tags": (m.get("Tags") or [])[:6],
        "tasks": task_names,
        "libraries": m.get("Libraries", []),
    }


def print_table(models: list[dict]):
    """Print models as a formatted table."""
    if not models:
        print("No models found.")
        return
    print(f"{'#':>3}  {'Model':<55} {'Downloads':>12} {'Stars':>6} {'License':<15} Tags")
    print("-" * 120)
    for i, m in enumerate(models, 1):
        path = m["path"]
        dl = f"{m['downloads']:,}"
        stars = str(m["stars"])
        lic = m["license"] or "-"
        tags = ", ".join(m["tags"][:4]) if m["tags"] else "-"
        if len(path) > 54:
            path = path[:51] + "..."
        print(f"{i:3d}  {path:<55} {dl:>12} {stars:>6} {lic:<15} {tags}")


def main():
    parser = argparse.ArgumentParser(description="Search models on ModelScope")
    parser.add_argument("query", nargs="?", help="Search keyword (e.g., 'OCR', 'Qwen')")
    parser.add_argument("--model", help="Get details for a specific model (org/name)")
    parser.add_argument("--sort", choices=["downloads", "stars"], default="downloads", help="Sort by (default: downloads)")
    parser.add_argument("--page", type=int, default=1, help="API page (>=1)")
    parser.add_argument("--limit", type=int, default=15, help="Max results (default: 15)")
    parser.add_argument("--json", action="store_true", dest="json_output", help="Output as JSON")
    args = parser.parse_args()
    if args.page < 1 or not 1 <= args.limit <= 100:
        parser.error("page must be >= 1; limit must be 1..100")

    if args.model:
        m = get_model_detail(args.model)
        if m:
            result = format_model(m)
            if args.json_output:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            else:
                for k, v in result.items():
                    print(f"  {k}: {v}")
        else:
            print(f"Model '{args.model}' not found.", file=sys.stderr)
            sys.exit(1)
        return

    if not args.query:
        parser.error("query or --model is required")

    page_size = min(args.limit * 2, 100)  # fetch extra for sorting
    data = search_models(args.query, page=args.page, page_size=page_size)
    models = data.get("Models", [])
    total = data.get("TotalCount", 0)

    # Format and sort
    formatted = [format_model(m) for m in models]
    sort_key = "downloads" if args.sort == "downloads" else "stars"
    formatted.sort(key=lambda x: x[sort_key], reverse=True)
    formatted = formatted[: args.limit]

    if args.json_output:
        output = {"query": args.query, "total": total, "showing": len(formatted), "sort": args.sort, "sort_scope": "fetched_page_only", "page": args.page, "page_size": page_size, "fetched": len(models), "models": formatted}
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(f"\n  ModelScope Search: '{args.query}' | Total: {total} | Showing: {len(formatted)} | Sort: {args.sort} (fetched page only, not global ranking) | Page: {args.page}\n")
        print_table(formatted)
        print()


# Windows GBK 控制台无法输出 emoji/特殊 Unicode，强制 UTF-8
if sys.platform == "win32":
    for _stream_name in ("stdout", "stderr"):
        _stream = getattr(sys, _stream_name)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
        else:
            setattr(sys, _stream_name, io.TextIOWrapper(_stream.buffer, encoding="utf-8", errors="replace"))

if __name__ == "__main__":
    try:
        main()
    except requests.HTTPError as e:
        status = e.response.status_code if e.response is not None else None
        print(json.dumps({"error": {"code": "HTTP_ERROR", "status": status}}), file=sys.stderr)
        sys.exit(1)
    except requests.RequestException:
        print(json.dumps({"error": {"code": "NETWORK_ERROR"}}), file=sys.stderr)
        sys.exit(1)
    except (ValueError, RuntimeError, TypeError, KeyError, AttributeError):
        print(json.dumps({"error": {"code": "INVALID_RESPONSE_OR_ARGUMENT"}}), file=sys.stderr)
        sys.exit(1)

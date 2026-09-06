#!/usr/bin/env python3
"""上传 GitHub 前的密钥泄露检查。

扫描本技能目录下所有文本文件，发现内嵌 SkillsMP 密钥即报告并返回非零退出码。
用法：python scripts/check-secrets.py            # 检查本技能目录
      python scripts/check-secrets.py <其他目录>  # 检查任意目录
"""

import re
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SECRET_PATTERN = re.compile(r"sk_live_[A-Za-z0-9_\-]{16,}")
TEXT_SUFFIXES = {".py", ".md", ".json", ".js", ".ts", ".toml", ".yaml", ".yml",
                 ".sh", ".ps1", ".txt", ".html", ".css", ".cfg", ".ini"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "Trash", "TempFiles"}


def scan(root: Path) -> list[str]:
    hits: list[str] = []
    if root.is_file():
        files = [root]
    else:
        files = [p for p in root.rglob("*")
                 if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES
                 and not any(part in SKIP_DIRS for part in p.parts)]
    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if SECRET_PATTERN.search(line):
                hits.append(f"{path}:{i}")
    return hits


def main() -> int:
    targets = sys.argv[1:] or [str(Path(__file__).resolve().parents[1])]
    all_hits: list[str] = []
    for target in targets:
        all_hits.extend(scan(Path(target).resolve()))
    if all_hits:
        print("发现内嵌密钥，上传 GitHub 前必须移除：", file=sys.stderr)
        for hit in all_hits:
            print(f"  {hit}", file=sys.stderr)
        print("处理方式：删除 DEFAULT_API_KEY 值，改用环境变量 SKILLSMP_API_KEY 或"
              " %APPDATA%\\skillsmp-search\\config.json", file=sys.stderr)
        return 1
    print("未发现内嵌密钥，可以上传。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

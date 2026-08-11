#!/usr/bin/env python3
"""Emit a deterministic snapshot of a Git simplification scope."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


# Directories that are never hand-edited, at any depth.
ALWAYS_EXCLUDED_PARTS = {".git", "node_modules", "vendor"}
# Generated output directories, matched only at the repository root so a
# legitimate nested directory (for example a package named build) survives.
ROOT_EXCLUDED_PARTS = {"dist", "build", "out", "coverage", ".next", ".turbo", "target"}
# Lockfiles and minified/generated artifacts.
EXCLUDED_SUFFIXES = (".lock", ".min.js", ".min.css", ".js.map", ".css.map")


def run_git(repo: Path, *args: str, nul: bool = False) -> list[str]:
    result = subprocess.run(
        ["git", "-c", "core.quotePath=false", "-C", str(repo), *args],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode:
        message = result.stderr.strip() or "git command failed"
        raise RuntimeError(message)
    separator = "\0" if nul else "\n"
    return [item for item in result.stdout.split(separator) if item]


def is_excluded(path: str) -> bool:
    parts = Path(path).parts
    if not parts:
        return False
    if parts[0] in ROOT_EXCLUDED_PARTS:
        return True
    if ALWAYS_EXCLUDED_PARTS.intersection(parts):
        return True
    return path.endswith(EXCLUDED_SUFFIXES)


def collect_candidates(repo: Path, base: str | None) -> tuple[list[str], str]:
    if base:
        tracked = run_git(
            repo,
            "diff",
            "--name-only",
            "-z",
            "--diff-filter=ACMRTUXB",
            f"{base}...HEAD",
            "--",
            nul=True,
        )
        return tracked, f"git diff {base}...HEAD"

    tracked = run_git(
        repo,
        "diff",
        "--name-only",
        "-z",
        "--diff-filter=ACMRTUXB",
        "HEAD",
        "--",
        nul=True,
    )
    untracked = run_git(
        repo,
        "ls-files",
        "--others",
        "--exclude-standard",
        "-z",
        nul=True,
    )
    return tracked + untracked, "git diff HEAD and untracked files"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--path", action="append", dest="paths", default=[])
    parser.add_argument(
        "--base",
        help="Base revision for a commit/PR range; scope becomes base...HEAD.",
    )
    parser.add_argument(
        "--include-excluded",
        action="store_true",
        help="Keep normally excluded files in scope; they are still reported in would_exclude.",
    )
    args = parser.parse_args()

    repo = args.repo.resolve()
    try:
        run_git(repo, "rev-parse", "--show-toplevel")
        collected, source = collect_candidates(repo, args.base)
    except RuntimeError as exc:
        print(f"scope_snapshot: {exc}", file=sys.stderr)
        return 2

    explicit = {str(Path(p)) for p in args.paths}
    candidates = set(collected) | explicit

    included: list[str] = []
    would_exclude: list[str] = []
    for path in sorted(candidates):
        excluded_by_rule = path not in explicit and is_excluded(path)
        if excluded_by_rule:
            would_exclude.append(path)
            if not args.include_excluded:
                continue
        included.append(path)

    payload = {
        "repository": str(repo),
        "scope": included,
        "excluded": [] if args.include_excluded else would_exclude,
        "would_exclude": would_exclude,
        "scope_frozen": True,
        "source": f"explicit paths plus {source}" if args.paths else source,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

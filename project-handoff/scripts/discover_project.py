#!/usr/bin/env python3
"""Discover project roots and existing handoff documents before scanning."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from _handoff_common import force_utf8_console

DEFAULT_SKIP_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__", "dist", "build",
    "target", "vendor", ".cache", ".next", ".nuxt", "coverage", "ProjectDoc",
}
PROJECT_MARKERS = {
    "package.json", "pyproject.toml", "requirements.txt", "setup.py", "Cargo.toml",
    "go.mod", "pom.xml", "build.gradle", "CMakeLists.txt", "Makefile", "platformio.ini",
    "Dockerfile", "docker-compose.yml", "docker-compose.yaml", "wrangler.toml",
    "*.sln", "*.csproj", "*.vcxproj", "*.uproject", "*.ioc", "*.uvprojx", "*.ewp",
}
HANDOFF_NAMES = {"projectdoc", "project-handoff", "handoff", "handoff-docs", "projectdoc-handoff"}


def iso_time(path: Path) -> str | None:
    try:
        return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).astimezone().isoformat()
    except OSError:
        return None


def has_marker(directory: Path) -> list[str]:
    try:
        names = {entry.name for entry in directory.iterdir() if entry.is_file()}
    except OSError:
        return []
    found = []
    for marker in PROJECT_MARKERS:
        if marker.startswith("*"):
            if any(name.endswith(marker[1:]) for name in names):
                found.append(marker)
        elif marker in names:
            found.append(marker)
    return sorted(found)


def handoff_info(directory: Path) -> dict:
    locations = []
    try:
        matches = [item for item in directory.iterdir()
                   if item.is_dir() and item.name.lower() in HANDOFF_NAMES]
    except OSError:
        matches = []
    for folder in matches:
        try:
            files = list(folder.iterdir())
        except OSError:
            files = []
        locations.append({
            "path": str(folder),
            "markdown_count": sum(item.suffix.lower() == ".md" for item in files),
            "file_count": len(files),
            "latest_modified": max((iso_time(item) for item in files), default=None),
            "has_analysis_report": (folder / "analysis-report.json").exists(),
        })
    return {"found": bool(locations), "locations": locations}


def discover(start: Path, max_depth: int) -> list[dict]:
    start = start.resolve()
    candidates = []
    for current, dirs, _files in os.walk(start):
        current_path = Path(current)
        depth = len(current_path.relative_to(start).parts)
        if depth > max_depth:
            dirs[:] = []
            continue
        dirs[:] = sorted(name for name in dirs
                         if name not in DEFAULT_SKIP_DIRS and not name.startswith("."))
        markers = has_marker(current_path)
        handoff = handoff_info(current_path)
        if not markers and not handoff["found"]:
            continue
        score = len(markers) * 2 + (4 if handoff["found"] else 0)
        if current_path == start:
            score += 1
        candidates.append({
            "path": str(current_path),
            "relative_to_start": "." if current_path == start else str(current_path.relative_to(start)),
            "depth": depth,
            "score": score,
            "project_markers": markers,
            "existing_handoff": handoff,
        })
    return sorted(candidates, key=lambda item: (-item["score"], item["depth"], item["path"].lower()))


def main() -> None:
    parser = argparse.ArgumentParser(description="Find project roots and existing handoff documents before scanning.")
    parser.add_argument("--start", default=".", help="Directory from which to search")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum search depth below start")
    parser.add_argument("--output", help="Optional JSON output path")
    args = parser.parse_args()
    payload = {
        "schema_version": 1,
        "start_directory": str(Path(args.start).resolve()),
        "max_depth": args.max_depth,
        "selection_required": True,
        "selection_rule": "AI must select one project root; do not scan the parent workspace when multiple candidates exist.",
        "candidates": discover(Path(args.start), max(0, args.max_depth)),
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        output = Path(args.output).resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
        print(f"Discovery report written to {output}")
    else:
        print(rendered)


if __name__ == "__main__":
    force_utf8_console()
    main()

"""Shared helpers for project-handoff scripts."""

import io
import sys


def force_utf8_console():
    """Windows GBK 控制台无法输出 emoji/特殊 Unicode，强制 UTF-8。"""
    if sys.platform != "win32":
        return
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
        else:
            setattr(sys, stream_name, io.TextIOWrapper(stream.buffer, encoding="utf-8", errors="replace"))

"""Shared helpers for project-handoff scripts."""

import io
import sys


def read_handoff_config(root):
    """Read the documented single-line YAML subset, preserving quoted # characters."""
    import ast
    config = {'skip_dirs': [], 'include_dirs': [], 'max_files': None}
    path = root / '.handoff.yml'
    if not path.exists():
        return config
    for number, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        quote, escaped, chars = None, False, []
        for char in raw:
            if char == '#' and quote is None:
                break
            chars.append(char)
            if escaped:
                escaped = False
            elif char == '\\' and quote:
                escaped = True
            elif char in ('"', "'"):
                quote = None if quote == char else (char if quote is None else quote)
        line = ''.join(chars).strip()
        if not line:
            continue
        key, sep, value = line.partition(':')
        key, value = key.strip(), value.strip()
        try:
            if not sep or key not in config:
                raise ValueError('未知配置项或缺少冒号')
            if key == 'max_files':
                parsed = int(value)
                if parsed <= 0:
                    raise ValueError('max_files 必须大于 0')
            else:
                try:
                    parsed = ast.literal_eval(value)
                except (SyntaxError, ValueError):
                    if not (value.startswith('[') and value.endswith(']')):
                        raise ValueError('目录必须使用单行数组')
                    parsed = [part.strip() for part in value[1:-1].split(',') if part.strip()]
                if not isinstance(parsed, list) or any(not isinstance(x, str) for x in parsed):
                    raise ValueError('目录必须为字符串列表')
            config[key] = parsed
        except (ValueError, SyntaxError) as exc:
            raise SystemExit(f'ERROR: {path}:{number}: {exc}') from exc
    return config


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


def normalize_doc_names(directory):
    """Back up legacy document names, then normalize names and local links."""
    import re
    import shutil
    from datetime import datetime
    from uuid import uuid4

    from _handoff_documents import BASE_DOCS, TOPIC_DOCS, LEGACY_DOCS
    names = set(BASE_DOCS) | TOPIC_DOCS | set(LEGACY_DOCS)
    files = list(directory.glob('*.md'))
    seen = set()
    for path in files:
        key = path.name.lower()
        if key in names and key in seen:
            raise SystemExit(f'ERROR: 交接文档大小写名称冲突: {key}，未修改任何文档')
        seen.add(key)
    renames = [p for p in files if p.name.lower() in names and p.name != p.name.lower()]
    edits = {}
    # Only same-directory Markdown destinations; source paths and prose are preserved.
    pattern = re.compile(r'(?P<prefix>\]\(<?(?:\./)?|^\s*\[[^]\n]+\]:\s*<?(?:\./)?)(?P<name>[A-Za-z-]+\.md)(?=[#)>\s]|$)', re.MULTILINE)
    for path in files:
        original = path.read_text(encoding='utf-8')
        updated = pattern.sub(lambda m: m['prefix'] + (m['name'].lower() if m['name'].lower() in names else m['name']), original)
        if original != updated:
            edits[path.name.lower() if path.name.lower() in names else path.name] = updated
    if not renames and not edits:
        return
    backup = directory.parent / 'TempFiles' / ('handoff-names-backup-' + datetime.now().strftime('%Y%m%d-%H%M%S-') + uuid4().hex[:8])
    backup.parent.mkdir(exist_ok=True)
    shutil.copytree(directory, backup)
    for path in renames:
        target = path.with_name(path.name.lower())
        temporary = path.with_name('.handoff-rename-' + uuid4().hex)
        path.rename(temporary)
        temporary.rename(target)
    for name, content in edits.items():
        (directory / name).write_text(content, encoding='utf-8')
    print(f'  文档命名已统一，旧文档备份: {backup}')

"""Recoverable migration from separate legacy documents to the balanced layout."""
from datetime import datetime
import re
import shutil
from uuid import uuid4
from _handoff_documents import LEGACY_DOCS


def body_only(text):
    text = re.sub(r'\A---\r?\n.*?\r?\n---\r?\n', '', text, count=1, flags=re.S)
    return re.sub(r'^# [^\n]*\n?', '', text, count=1, flags=re.M).strip()


def combine(primary, *sections):
    return primary.rstrip() + '\n\n' + '\n\n'.join(body_only(section) for section in sections)


def migrate_legacy_docs(directory):
    sources = [p for p in directory.glob('*.md') if p.name.lower() in LEGACY_DOCS]
    if not sources:
        return
    # Back up all manual documents before deleting the redundant legacy files.
    backup = directory.parent / 'TempFiles' / ('handoff-merge-backup-' + datetime.now().strftime('%Y%m%d-%H%M%S-') + uuid4().hex[:8])
    backup.parent.mkdir(exist_ok=True)
    shutil.copytree(directory, backup)
    for source in sorted(sources):
        target = directory / LEGACY_DOCS[source.name.lower()]
        original = target.read_text(encoding='utf-8') if target.exists() else '# 交接说明\n'
        addition = body_only(source.read_text(encoding='utf-8'))
        target.write_text(original.rstrip() + f'\n\n## 历史内容（来自 {source.name}）\n\n' + addition + '\n', encoding='utf-8')
        source.unlink()
    pattern = re.compile(r'(?P<prefix>\]\(<?(?:\./)?|^\s*\[[^]\n]+\]:\s*<?(?:\./)?)(?P<name>[A-Za-z-]+\.md)(?=[#)>\s]|$)', re.M)
    for path in directory.glob('*.md'):
        original = path.read_text(encoding='utf-8')
        updated = pattern.sub(lambda m: m['prefix'] + LEGACY_DOCS.get(m['name'].lower(), m['name']), original)
        if updated != original:
            path.write_text(updated, encoding='utf-8')
    print(f'旧文档已合并，人工内容保留；备份: {backup}')

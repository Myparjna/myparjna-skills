import json
from pathlib import Path
import handlers


def replay(record):
    registry = json.loads(Path(__file__).with_name("registry.json").read_text())
    return getattr(handlers, registry[record["format"]])(record)

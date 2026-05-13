from datetime import datetime
from pathlib import Path
import shutil


ROOT = Path.cwd()
HANDOFF_DIR = ROOT / "handoff"


def main() -> None:
    if not HANDOFF_DIR.exists():
        raise SystemExit("handoff/ does not exist. Run generate_handoff.py first.")
    stamp = datetime.now().strftime("%Y%m%d")
    archive = ROOT / f"handoff-{ROOT.name}-{stamp}"
    shutil.make_archive(str(archive), "zip", HANDOFF_DIR)
    print(f"Created {archive.name}.zip")


if __name__ == "__main__":
    main()

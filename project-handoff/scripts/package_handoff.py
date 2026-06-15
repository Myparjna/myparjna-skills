#!/usr/bin/env python3
"""打包交接文档：先验收，通过后打成 ZIP。"""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path.cwd()
HANDOFF = ROOT / "handoff"
VERIFY_SCRIPT = Path(__file__).parent / "verify_handoff.py"


def run_verify() -> int:
    """运行 verify_handoff.py，返回退出码。"""
    result = subprocess.run(
        [sys.executable, str(VERIFY_SCRIPT)],
        capture_output=False,
    )
    return result.returncode


def package() -> None:
    """将 handoff/ 打成 ZIP，排除 analysis-report.json 和 ZIP 自身。"""
    if not HANDOFF.is_dir():
        sys.exit("ERROR: handoff/ 目录不存在，先运行 generate_handoff.py")

    # 创建临时打包目录
    staging = HANDOFF / "_staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir()

    try:
        # 复制所有 .md 文件到临时目录
        for md_file in sorted(HANDOFF.glob("*.md")):
            shutil.copy2(md_file, staging / md_file.name)

        # 打包
        zip_path = HANDOFF / "handoff-package"
        archive = shutil.make_archive(str(zip_path), "zip", staging)
        print(f"\n打包完成: {archive}")
        print(f"包含 {len(list(staging.glob('*.md')))} 份文档")

        # 列出包内容
        for f in sorted(staging.glob("*.md")):
            size = f.stat().st_size
            print(f"  {f.name:30s} {size:>6,} bytes")

    finally:
        shutil.rmtree(staging, ignore_errors=True)


def main():
    print("=" * 50)
    print("Project Handoff 打包")
    print("=" * 50)

    # Step 1: 运行验收
    print("\n[1/2] 运行质量门禁...")
    exit_code = run_verify()

    if exit_code == 2:
        print("\n[X] 检测到密钥泄露，禁止打包。请修复后重试。")
        sys.exit(2)
    if exit_code == 1:
        print("\n[X] 验收未通过（存在 ERROR）。请修复后重试。")
        sys.exit(1)

    print("\n[OK] 验收通过")

    # Step 2: 打包
    print("\n[2/2] 打包文档...")
    package()

    print("\n" + "=" * 50)
    print("打包完成。可将 handoff-package.zip 交付给接手方。")
    print("=" * 50)


if __name__ == "__main__":
    main()

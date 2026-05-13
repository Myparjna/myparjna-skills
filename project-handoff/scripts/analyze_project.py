from pathlib import Path
import json
import re


ROOT = Path.cwd()


def detect_framework(files: set[str]) -> str:
    if "next.config.js" in files or "next.config.mjs" in files or "next.config.ts" in files:
        return "Next.js"
    if "nuxt.config.ts" in files or "nuxt.config.js" in files:
        return "Nuxt"
    if "vite.config.ts" in files or "vite.config.js" in files:
        return "Vite"
    if "package.json" in files:
        return "Node.js app"
    if "pyproject.toml" in files or "requirements.txt" in files:
        return "Python app"
    return "Unknown"


def parse_env_example() -> list[dict[str, str]]:
    env_file = ROOT / ".env.example"
    if not env_file.exists():
        return []
    variables = []
    for raw_line in env_file.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        variables.append({"name": key.strip(), "default": value.strip()})
    return variables


def detect_deploy_targets(files: set[str]) -> list[str]:
    targets = []
    mapping = {
        "vercel.json": "Vercel",
        "netlify.toml": "Netlify",
        "docker-compose.yml": "Docker Compose",
        "docker-compose.yaml": "Docker Compose",
        "Dockerfile": "Docker",
        ".github": "GitHub Actions",
    }
    for file_name, label in mapping.items():
        if file_name in files:
            targets.append(label)
    return targets


def collect_files() -> set[str]:
    files = set()
    for path in ROOT.iterdir():
        files.add(path.name)
    return files


def main() -> None:
    files = collect_files()
    report = {
        "project_name": ROOT.name,
        "framework": detect_framework(files),
        "deployment_targets": detect_deploy_targets(files),
        "environment_variables": parse_env_example(),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

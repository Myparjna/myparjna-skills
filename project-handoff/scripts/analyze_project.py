#!/usr/bin/env python3
"""Scan the project and emit ProjectDoc/analysis-report.json for handoff doc generation."""
from pathlib import Path
from datetime import datetime, timezone
import json
import math
import re
import subprocess
import sys

ROOT = Path.cwd()
OUT_DIR = ROOT / "ProjectDoc"
TOOL_VERSION = "2.0.0"
SCHEMA_VERSION = 2

# --- 配置（可被 .handoff.yml 覆盖） ---
SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", ".next", ".nuxt", "out",
    "__pycache__", ".venv", "venv", "env", ".turbo", "coverage", ".cache",
    "target", "vendor", ".pytest_cache", ".mypy_cache", "ProjectDoc",
    ".mypy_cache", ".ruff_cache", ".tox", "egg-info",
}
GREP_EXT = {".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".py", ".html",
             ".cjs", ".mjs", ".md", ".toml", ".yml", ".yaml", ".json",
             ".go", ".rs", ".rb", ".java", ".kt", ".swift", ".cs", ".php",
             ".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx",
             ".ino", ".S", ".s", ".cmake", ".mk", ".gradle", ".properties",
             ".xml", ".ld", ".lds"}
GREP_FILENAMES = {
    "Makefile", "makefile", "GNUmakefile", "CMakeLists.txt", "meson.build",
    "platformio.ini", "go.mod", "go.sum", "Cargo.toml", "Cargo.lock",
    "pom.xml", "build.gradle", "build.gradle.kts", "settings.gradle",
    "settings.gradle.kts", "requirements.txt", "pyproject.toml",
}
MAX_FILE_SIZE = 512_000
MAX_GREP_FILES = 3000


def load_config():
    """加载 .handoff.yml 配置（可选）。"""
    global SKIP_DIRS, MAX_GREP_FILES
    config_path = ROOT / ".handoff.yml"
    if not config_path.exists():
        return
    try:
        # 简单 YAML 解析（不依赖 pyyaml）
        content = config_path.read_text(encoding="utf-8")
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, _, val = line.partition(":")
                key = key.strip()
                val = val.strip()
                if key == "skip_dirs" and val.startswith("["):
                    extra = [s.strip().strip("'\"") for s in val.strip("[]").split(",") if s.strip()]
                    SKIP_DIRS = SKIP_DIRS | set(extra)
                elif key == "max_files" and val.isdigit():
                    MAX_GREP_FILES = int(val)
    except Exception:
        pass  # 配置解析失败用默认值


def read_text(path: Path) -> str:
    try:
        if path.stat().st_size > MAX_FILE_SIZE:
            return ""
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def scanner_relative_prefix():
    """Return scanner script path relative to ROOT when the skill is vendored into the project."""
    try:
        return str(Path(__file__).parent.resolve().relative_to(ROOT.resolve())).replace("\\", "/")
    except ValueError:
        return None


def rel_path(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def iter_files():
    stack = [ROOT]
    count = 0
    while stack:
        current = stack.pop()
        try:
            entries = sorted(current.iterdir())
        except OSError:
            continue
        for path in entries:
            if path.is_dir():
                if path.name not in SKIP_DIRS and not path.name.startswith("."):
                    stack.append(path)
            elif path.is_file():
                count += 1
                if count > MAX_GREP_FILES * 3:
                    if sys.stderr.isatty():
                        sys.stderr.write(f"\n[warn] 扫描截断：已扫描 {count} 文件，部分文件未覆盖\n")
                    return
                yield path


def collect_source_texts():
    """(relative_path, content) pairs for grep-based detection."""
    texts = []
    for path in iter_files():
        if path.suffix.lower() in GREP_EXT or path.name in GREP_FILENAMES:
            content = read_text(path)
            if content:
                texts.append((rel_path(path), content))
            if len(texts) >= MAX_GREP_FILES:
                break
    return texts


def grep(texts, pattern, group=0):
    found = {}
    regex = re.compile(pattern)
    for rel, content in texts:
        for match in regex.finditer(content):
            value = match.group(group)
            found.setdefault(value, rel)
    return [{"value": v, "found_in": f} for v, f in sorted(found.items())]


# ---------- manifests ----------

def find_manifests():
    manifests = {
        "package_json": [], "requirements": [], "pyproject": [], "csproj": [],
        "go_mod": [], "cargo": [], "java": [], "native": [], "embedded": [],
    }
    for pattern, key in [("package.json", "package_json"), ("requirements*.txt", "requirements"),
                         ("pyproject.toml", "pyproject"), ("*.csproj", "csproj"),
                         ("go.mod", "go_mod"), ("Cargo.toml", "cargo"),
                         ("pom.xml", "java"), ("build.gradle*", "java"),
                         ("CMakeLists.txt", "native"), ("Makefile", "native"),
                         ("*.mk", "native"), ("meson.build", "native"),
                         ("platformio.ini", "embedded"), ("*.ioc", "embedded"),
                         ("*.uvprojx", "embedded"), ("*.ewp", "embedded")]:
        for depth in ("", "*/", "*/*/"):
            for path in ROOT.glob(depth + pattern):
                if not any(part in SKIP_DIRS for part in path.parts):
                    manifests[key].append(path)
    return manifests


def load_node_deps(package_json_paths):
    all_deps = {}
    scripts = {}
    for path in package_json_paths:
        try:
            data = json.loads(read_text(path) or "{}")
        except json.JSONDecodeError:
            continue
        rel = rel_path(path)
        for key in ("dependencies", "devDependencies"):
            for name, version in (data.get(key) or {}).items():
                all_deps[name] = {"version": version, "dev": key == "devDependencies", "manifest": rel}
        if data.get("scripts"):
            scripts[rel] = data["scripts"]
    return all_deps, scripts


def load_python_deps(req_paths, pyproject_paths):
    deps = {}
    for path in req_paths:
        for line in (read_text(path)).splitlines():
            line = line.strip()
            if line and not line.startswith(("#", "-")):
                name = re.split(r"[=<>!~\[ ]", line)[0].lower()
                if name:
                    deps[name] = {"spec": line, "manifest": rel_path(path)}
    for path in pyproject_paths:
        content = read_text(path)
        for match in re.finditer(r'^\s*"?([A-Za-z0-9_.-]+)\s*[=<>!~"]', content, re.MULTILINE):
            pass  # pyproject parsing kept minimal; requirements cover most cases
        deps.setdefault("__pyproject__", {"spec": "see file", "manifest": rel_path(path)})
    return deps


# ---------- 新增：包管理器检测 ----------

def detect_package_manager():
    """检测项目使用的包管理器。"""
    managers = []
    lockfiles = {
        "pnpm-lock.yaml": "pnpm",
        "yarn.lock": "yarn",
        "bun.lockb": "bun",
        "package-lock.json": "npm",
    }
    for lockfile, manager in lockfiles.items():
        if (ROOT / lockfile).exists():
            managers.append(manager)
    # Python
    if (ROOT / "uv.lock").exists():
        managers.append("uv")
    elif (ROOT / "Pipfile.lock").exists():
        managers.append("pipenv")
    elif (ROOT / "poetry.lock").exists():
        managers.append("poetry")
    # 去重
    return sorted(set(managers)) or ["unknown"]


# ---------- 新增：Monorepo 检测 ----------

def detect_monorepo(node_deps):
    """检测 monorepo 配置。"""
    result = {"type": None, "workspace_count": 0, "tools": []}

    # pnpm workspace
    if (ROOT / "pnpm-workspace.yaml").exists():
        result["type"] = "pnpm-workspace"
        result["tools"].append("pnpm-workspace")
        content = read_text(ROOT / "pnpm-workspace.yaml")
        result["workspace_count"] = len(re.findall(r"-\s+(\S+)", content))

    # package.json workspaces
    for pj in ROOT.glob("package.json"):
        try:
            data = json.loads(read_text(pj) or "{}")
            if "workspaces" in data:
                result["type"] = result["type"] or "npm-workspaces"
                result["tools"].append("npm-workspaces")
                ws = data["workspaces"]
                result["workspace_count"] = len(ws) if isinstance(ws, list) else 1
        except json.JSONDecodeError:
            pass

    # Turborepo
    if (ROOT / "turbo.json").exists():
        result["tools"].append("turborepo")

    # Nx
    if (ROOT / "nx.json").exists():
        result["tools"].append("nx")

    # Lerna
    if (ROOT / "lerna.json").exists():
        result["tools"].append("lerna")

    return result


# ---------- detections ----------

def detect_framework(node_deps, py_deps, files):
    frameworks = []
    node_map = {"next": "Next.js", "nuxt": "Nuxt", "vite": "Vite", "react": "React", "vue": "Vue",
                "svelte": "Svelte", "astro": "Astro", "express": "Express", "koa": "Koa",
                "fastify": "Fastify", "@nestjs/core": "NestJS", "electron": "Electron"}
    for dep, label in node_map.items():
        if dep in node_deps:
            frameworks.append({"name": label, "version": node_deps[dep]["version"]})
    py_map = {"fastapi": "FastAPI", "flask": "Flask", "django": "Django", "streamlit": "Streamlit", "gradio": "Gradio"}
    for dep, label in py_map.items():
        if dep in py_deps:
            frameworks.append({"name": label, "version": py_deps[dep]["spec"]})
    return frameworks


UI_LIB_MAP = {
    "antd": "Ant Design (React)", "@ant-design/icons": "Ant Design Icons",
    "ant-design-vue": "Ant Design Vue",
    "tdesign-react": "TDesign (React)", "tdesign-vue-next": "TDesign (Vue3)", "tdesign-vue": "TDesign (Vue2)",
    "@arco-design/web-react": "Arco Design (React)", "@arco-design/web-vue": "Arco Design (Vue)",
    "element-plus": "Element Plus", "element-ui": "Element UI",
    "naive-ui": "Naive UI", "vant": "Vant", "@mui/material": "MUI",
    "@chakra-ui/react": "Chakra UI", "bootstrap": "Bootstrap",
    "tailwindcss": "Tailwind CSS", "@radix-ui/react-dialog": "Radix UI",
    "vuetify": "Vuetify", "quasar": "Quasar", "primevue": "PrimeVue", "primereact": "PrimeReact",
}


def detect_ui_libraries(node_deps):
    libs = [{"name": label, "package": dep, "version": node_deps[dep]["version"]}
            for dep, label in UI_LIB_MAP.items() if dep in node_deps]
    if (ROOT / "components.json").exists():
        libs.append({"name": "shadcn/ui", "package": "components.json", "version": "n/a"})
    return libs


def detect_desktop(node_deps, csproj_paths):
    desktop = []
    if "electron" in node_deps:
        builders = [d for d in ("electron-builder", "@electron-forge/cli", "electron-packager") if d in node_deps]
        desktop.append({"type": "Electron", "version": node_deps["electron"]["version"],
                        "builder": builders[0] if builders else "unknown"})
    if (ROOT / "src-tauri").exists():
        desktop.append({"type": "Tauri", "config": "src-tauri/tauri.conf.json"})
    for path in csproj_paths:
        content = read_text(path)
        rel = rel_path(path)
        if "Microsoft.WindowsAppSDK" in content or "<UseWinUI>" in content:
            desktop.append({"type": "WinUI 3", "project": rel})
        elif "<UseWPF>true" in content:
            desktop.append({"type": "WPF", "project": rel})
        elif "<UseWindowsForms>true" in content:
            desktop.append({"type": "WinForms", "project": rel})
    return desktop


def detect_docker():
    result = {}
    dockerfile = next((p for p in [ROOT / "Dockerfile", *ROOT.glob("*/Dockerfile")] if p.exists()), None)
    if dockerfile:
        content = read_text(dockerfile)
        result["dockerfile"] = {
            "path": rel_path(dockerfile),
            "base_images": re.findall(r"^FROM\s+(\S+)", content, re.MULTILINE),
            "exposed_ports": re.findall(r"^EXPOSE\s+(.+)", content, re.MULTILINE),
            "cmd": re.findall(r"^(?:CMD|ENTRYPOINT)\s+(.+)", content, re.MULTILINE),
            "multi_stage": len(re.findall(r"^FROM\s", content, re.MULTILINE)) > 1,
        }
    compose = next((ROOT / n for n in ("docker-compose.yml", "docker-compose.yaml", "compose.yml", "compose.yaml")
                    if (ROOT / n).exists()), None)
    if compose:
        content = read_text(compose)
        services = re.findall(r"^\s{2,6}([\w-]+):\s*$", content, re.MULTILINE)
        result["compose"] = {"path": compose.name, "services": services,
                             "ports": re.findall(r'-\s*["\']?(\d+:\d+)', content)}
    return result


def detect_cloudflare():
    result = {}
    wrangler = next((ROOT / n for n in ("wrangler.toml", "wrangler.json", "wrangler.jsonc") if (ROOT / n).exists()), None)
    if wrangler:
        content = read_text(wrangler)
        result["wrangler"] = {
            "path": wrangler.name,
            "name": (re.search(r'name\s*[=:]\s*"([^"]+)"', content) or [None, None])[1],
            "main": (re.search(r'main\s*[=:]\s*"([^"]+)"', content) or [None, None])[1],
            "routes": re.findall(r'(?:route|pattern)\s*[=:]\s*"([^"]+)"', content),
            "kv_namespaces": re.findall(r'\[\[kv_namespaces\]\]\s*\n\s*binding\s*=\s*"([^"]+)"', content),
            "d1_databases": re.findall(r'\[\[d1_databases\]\]\s*\n\s*binding\s*=\s*"([^"]+)"', content),
            "r2_buckets": re.findall(r'\[\[r2_buckets\]\]\s*\n\s*binding\s*=\s*"([^"]+)"', content),
        }
    if (ROOT / "functions").is_dir() and any((ROOT / "functions").rglob("*.js")):
        result["pages_functions"] = True
    if (ROOT / "_headers").exists() or (ROOT / "public" / "_redirects").exists():
        result["pages_config_files"] = True
    return result


# ---------- 新增：CI/CD 扩展 ----------

def detect_ci_cd():
    """检测 CI/CD 配置（GitHub Actions / GitLab CI / Jenkins / CircleCI）。"""
    result = {"github_actions": [], "gitlab_ci": [], "jenkins": [], "circleci": []}

    # GitHub Actions
    wf_dir = ROOT / ".github" / "workflows"
    if wf_dir.is_dir():
        for path in sorted(wf_dir.glob("*.y*ml")):
            content = read_text(path)
            result["github_actions"].append({
                "file": path.name,
                "name": (re.search(r"^name:\s*(.+)", content, re.MULTILINE) or [None, ""])[1].strip(),
                "triggers": re.findall(r"^\s{2}(push|pull_request|workflow_dispatch|schedule|release):", content, re.MULTILINE),
                "secrets_used": sorted(set(re.findall(r"secrets\.([A-Z0-9_]+)", content))),
                "jobs": re.findall(r"^\s{2}([\w-]+):\s*$", content.split("jobs:", 1)[-1], re.MULTILINE)[:10],
            })

    # GitLab CI
    gitlab_ci = ROOT / ".gitlab-ci.yml"
    if gitlab_ci.exists():
        content = read_text(gitlab_ci)
        # 支持 block style 和 flow style stages
        stages_match = re.search(r"stages:\s*\n([\s\S]*?)(?=\n\S|\Z)", content or "")
        if stages_match:
            stages = re.findall(r"^\s*-\s+(\S+)", stages_match.group(1))
        else:
            # flow style: stages: [build, test, deploy]
            flow_match = re.search(r"stages:\s*\[([^\]]+)\]", content or "")
            stages = [s.strip() for s in flow_match.group(1).split(",")] if flow_match else []
        variables = re.findall(r"^  ([A-Z][A-Z0-9_]+):", content, re.MULTILINE)
        result["gitlab_ci"].append({
            "file": ".gitlab-ci.yml",
            "stages": stages[:10],
            "variables": sorted(set(variables))[:20],
        })

    # Jenkins
    jenkinsfile = ROOT / "Jenkinsfile"
    if jenkinsfile.exists():
        content = read_text(jenkinsfile)
        stages = re.findall(r"stage\s*\(\s*['\"]([^'\"]+)", content)
        result["jenkins"].append({
            "file": "Jenkinsfile",
            "stages": stages[:10],
        })

    # CircleCI
    circleci = ROOT / ".circleci" / "config.yml"
    if circleci.exists():
        content = read_text(circleci)
        jobs = re.findall(r"^  (\w+):\s*$", content.split("jobs:", 1)[-1], re.MULTILINE) if "jobs:" in content else []
        result["circleci"].append({
            "file": ".circleci/config.yml",
            "jobs": jobs[:10],
        })

    return result


# ---------- 新增：Kubernetes 检测 ----------

def detect_kubernetes():
    """检测 Kubernetes 配置文件。"""
    result = {"resources": [], "namespaces": set(), "images": set()}
    k8s_dirs = [ROOT / d for d in ("k8s", "deploy", "manifests", ".k8s", "kubernetes", "infra", "ops", "platform") if (ROOT / d).is_dir()]
    # 也扫描根目录和1层子目录下所有含 kind: 的 YAML
    yaml_files = []
    for d in k8s_dirs:
        yaml_files.extend(d.rglob("*.yaml"))
        yaml_files.extend(d.rglob("*.yml"))
    # 额外扫描根目录下的 k8s 相关 YAML
    for p in list(ROOT.glob("*.yaml")) + list(ROOT.glob("*.yml")) + list(ROOT.glob("*/*.yaml")) + list(ROOT.glob("*/*.yml")):
        if p.is_file() and p not in yaml_files:
            content_head = read_text(p)[:500]
            if "kind:" in content_head and ("apiVersion:" in content_head or "metadata:" in content_head):
                yaml_files.append(p)

    for path in yaml_files:
        content = read_text(path)
        if not content:
            continue
        # 检测 kind
        kinds = re.findall(r"^kind:\s*(\S+)", content, re.MULTILINE)
        if kinds:
            for kind in kinds:
                if kind in ("Deployment", "Service", "Ingress", "ConfigMap", "Secret",
                           "StatefulSet", "DaemonSet", "Job", "CronJob", "PersistentVolumeClaim"):
                    result["resources"].append({
                        "kind": kind,
                        "file": rel_path(path),
                        "name": (re.search(r"^\s*name:\s*(\S+)", content, re.MULTILINE) or [None, ""])[1],
                    })
        # 提取容器镜像
        images = re.findall(r"image:\s*(\S+)", content)
        result["images"].update(images)
        # 提取 namespace
        ns = re.findall(r"namespace:\s*(\S+)", content)
        result["namespaces"].update(ns)

    result["namespaces"] = sorted(result["namespaces"])
    result["images"] = sorted(result["images"])
    return result


AI_DEP_MAP = {
    "openai": "OpenAI SDK", "@anthropic-ai/sdk": "Anthropic SDK", "anthropic": "Anthropic SDK (py)",
    "@google/generative-ai": "Google Gemini SDK", "google-generativeai": "Google Gemini SDK (py)",
    "dashscope": "Aliyun DashScope", "zhipuai": "Zhipu AI", "langchain": "LangChain",
    "llamaindex": "LlamaIndex", "llama-index": "LlamaIndex", "ollama": "Ollama",
    "transformers": "HuggingFace Transformers", "modelscope": "ModelScope SDK",
    "@cloudflare/ai": "Cloudflare Workers AI", "litellm": "LiteLLM", "vllm": "vLLM",
}
AI_ENDPOINTS = r"https?://(?:api\.openai\.com|api\.anthropic\.com|api\.deepseek\.com|generativelanguage\.googleapis\.com|dashscope\.aliyuncs\.com|open\.bigmodel\.cn|api\.moonshot\.cn|openrouter\.ai|api\.mistral\.ai|api\.groq\.com|api\.together\.xyz|api\.siliconflow\.cn)[^\s'\"`)]*"
AI_MODEL_NAMES = r"['\"]((?:gpt-4|gpt-3\.5|gpt-4o|o[134](?:-mini)?|claude-[\w.-]+|gemini-[\w.-]+|deepseek-[\w.-]+|qwen[\w.-]*|glm-[\w.-]+|llama[\w.-]*|moonshot[\w.-]*)[^'\"]*)['\"]"


def detect_ai_services(node_deps, py_deps, texts):
    sdks = []
    for dep, label in AI_DEP_MAP.items():
        if dep in node_deps:
            sdks.append({"sdk": label, "package": dep, "version": node_deps[dep]["version"]})
        elif dep in py_deps:
            sdks.append({"sdk": label, "package": dep, "version": py_deps[dep]["spec"]})
    return {
        "sdks": sdks,
        "endpoints": grep(texts, AI_ENDPOINTS),
        "model_names": grep(texts, AI_MODEL_NAMES, group=1)[:30],
    }


def detect_external_resources(node_deps, texts):
    github_deps = [{"package": name, "spec": info["version"]} for name, info in node_deps.items()
                   if isinstance(info.get("version"), str) and ("git+" in info["version"] or info["version"].startswith("github:"))]
    return {
        "huggingface_models": grep(texts, r"from_pretrained\(\s*['\"]([^'\"]+)['\"]", group=1),
        "huggingface_urls": grep(texts, r"https://(?:huggingface\.co|hf-mirror\.com)/[^\s'\"`)]+"),
        "modelscope_models": grep(texts, r"snapshot_download\(\s*['\"]([^'\"]+)['\"]", group=1),
        "modelscope_urls": grep(texts, r"https://(?:www\.)?modelscope\.cn/[^\s'\"`)]+"),
        "github_dependencies": github_deps,
        "github_urls": grep(texts, r"https://github\.com/[\w.-]+/[\w.-]+")[:40],
        "cdn_links": grep(texts, r"https?://(?:cdn\.jsdelivr\.net|unpkg\.com|cdnjs\.cloudflare\.com|fastly\.jsdelivr\.net)[^\s'\"`)]+")[:20],
    }


# ---------- 新增：高熵字符串检测 ----------

def shannon_entropy(s: str) -> float:
    """计算字符串的香农熵。"""
    if not s:
        return 0.0
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    length = len(s)
    return -sum((count / length) * math.log2(count / length) for count in freq.values())


def detect_high_entropy_env_values():
    """扫描 .env 文件中的高熵值（疑似真实密钥）。只输出变量名，不输出值。"""
    high_entropy = []
    # 动态发现所有 .env 变体文件
    env_files = sorted(set(
        rel_path(p) for p in ROOT.glob(".env*")
        if p.is_file() and p.name != ".env.example" and not p.name.startswith(".env.")
        or p.name in (".env.local", ".env.development", ".env.staging",
                       ".env.test", ".env.production", ".env.backup")
    ))
    # 兜底：至少检查这些
    for fallback in (".env", ".env.local", ".env.production"):
        if fallback not in env_files and (ROOT / fallback).exists():
            env_files.append(fallback)
    for name in env_files:
        path = ROOT / name
        if not path.exists():
            continue
        for i, line in enumerate(read_text(path).splitlines(), 1):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip("'\"")
            if len(value) > 16 and shannon_entropy(value) > 4.5:
                high_entropy.append({
                    "variable": key,
                    "source": name,
                    "length": len(value),
                    "entropy": round(shannon_entropy(value), 2),
                })
    return high_entropy


def detect_env_vars(texts):
    declared = {}
    for name in (".env.example", ".env.sample", ".env.template", ".env"):
        path = ROOT / name
        if not path.exists():
            continue
        for line in read_text(path).splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                key = key.strip()
                if key not in declared:
                    declared[key] = {"source": name,
                                     "default": value.strip() if name != ".env" else "<redacted: real .env>"}
    used = set()
    precise_patterns = [
        # JS / TS / Vite / Node
        r"process\.env\.([A-Z0-9_]+)",
        r"process\.env\[['\"]([A-Z0-9_]+)",
        r"import\.meta\.env\.([A-Z0-9_]+)",
        # Python
        r"os\.environ(?:\.get)?\(\s*['\"]([A-Z0-9_]+)",
        r"os\.environ\[['\"]([A-Z0-9_]+)",
        r"os\.getenv\(\s*['\"]([A-Z0-9_]+)",
        # .NET
        r"Environment\.GetEnvironmentVariable\(\s*['\"]([A-Z0-9_]+)",
        r'Configuration\[[\'"]([A-Z0-9_]+)',
        # Go
        r"os\.Getenv\(\s*['\"]([A-Z0-9_]+)",
        r"os\.LookupEnv\(\s*['\"]([A-Z0-9_]+)",
        # Rust
        r"std::env::var\(\s*['\"]([A-Z0-9_]+)",
        r"env::var\(\s*['\"]([A-Z0-9_]+)",
        # Java / Kotlin
        r"System\.getenv\(\s*['\"]([A-Z0-9_]+)",
        # C / C++ / PHP
        r"\bgetenv\(\s*['\"]([A-Z0-9_]+)",
        r"\$_ENV\[['\"]([A-Z0-9_]+)",
    ]
    shell_like_files = (
        ".sh", ".bash", ".zsh", ".ps1", ".bat", ".cmd", ".env", ".yml", ".yaml",
        "Dockerfile", "docker-compose.yml", "docker-compose.yaml", "compose.yml",
        "compose.yaml", "Makefile", "makefile", "GNUmakefile", ".mk",
    )
    shell_patterns = [
        r"\$\{([A-Z][A-Z0-9_]{2,})(?::-[^}]*)?\}",
        r"(?<![A-Za-z0-9_])\$([A-Z][A-Z0-9_]{2,})(?![A-Za-z0-9_])",
    ]
    for rel, content in texts:
        for pattern in precise_patterns:
            used.update(re.findall(pattern, content))
        if rel.endswith(shell_like_files) or Path(rel).name in shell_like_files:
            for pattern in shell_patterns:
                used.update(re.findall(pattern, content))
    declared_keys = set(declared)
    return {
        "declared": [{"name": k, **v} for k, v in sorted(declared.items())],
        "used_in_code": sorted(used),
        "used_but_not_declared": sorted(used - declared_keys),
        "declared_but_not_used": sorted(declared_keys - used),
        "high_entropy_values": detect_high_entropy_env_values(),
    }


def detect_database(node_deps, py_deps):
    result = {"clients": [], "orm": [], "migrations": []}
    client_map = {"pg": "PostgreSQL", "mysql2": "MySQL", "better-sqlite3": "SQLite", "sqlite3": "SQLite",
                  "mongodb": "MongoDB", "mongoose": "MongoDB (Mongoose)", "redis": "Redis", "ioredis": "Redis",
                  "psycopg2": "PostgreSQL", "psycopg2-binary": "PostgreSQL", "pymysql": "MySQL",
                  "pymongo": "MongoDB", "aiosqlite": "SQLite"}
    for dep, label in client_map.items():
        if dep in node_deps or dep in py_deps:
            result["clients"].append(label)
    for dep in ("prisma", "drizzle-orm", "typeorm", "sequelize", "sqlalchemy", "tortoise-orm", "peewee"):
        if dep in node_deps or dep in py_deps:
            result["orm"].append(dep)
    schema = ROOT / "prisma" / "schema.prisma"
    if schema.exists():
        result["prisma_models"] = re.findall(r"^model\s+(\w+)", read_text(schema), re.MULTILINE)
    for name in ("migrations", "alembic", "prisma/migrations"):
        if (ROOT / name).is_dir():
            result["migrations"].append(name)
    result["clients"] = sorted(set(result["clients"]))
    return result


def detect_native_embedded_ai(texts):
    """检测 Go/Rust/Java/.NET/C/C++、嵌入式和本地推理项目线索。"""
    def rel_paths(patterns, limit=20):
        paths = []
        for pattern in patterns:
            for depth in ("", "*/", "*/*/"):
                for path in ROOT.glob(depth + pattern):
                    if path.is_file() and not any(part in SKIP_DIRS for part in path.parts):
                        rel = rel_path(path)
                        if rel not in paths:
                            paths.append(rel)
                            if len(paths) >= limit:
                                return paths
        return paths

    manifests = {
        "go": rel_paths(["go.mod", "go.sum"]),
        "rust": rel_paths(["Cargo.toml", "Cargo.lock"]),
        "java_jvm": rel_paths(["pom.xml", "build.gradle", "build.gradle.kts", "settings.gradle", "settings.gradle.kts"]),
        "dotnet": rel_paths(["*.sln", "*.csproj", "*.fsproj", "*.vbproj"]),
        "native_build": rel_paths(["CMakeLists.txt", "Makefile", "*.mk", "meson.build", "BUILD", "WORKSPACE"]),
        "embedded": rel_paths(["platformio.ini", "*.ioc", "*.uvprojx", "*.ewp", "*.ld", "*.lds"]),
    }

    source_counts = {
        "c": len(rel_paths(["*.c"], limit=2000)),
        "cpp": len(rel_paths(["*.cc", "*.cpp", "*.cxx"], limit=2000)),
        "headers": len(rel_paths(["*.h", "*.hpp", "*.hxx"], limit=2000)),
        "asm": len(rel_paths(["*.S", "*.s"], limit=2000)),
    }

    compiler_patterns = {
        "GCC": r"\b(?:gcc|g\+\+)\b",
        "Clang": r"\b(?:clang|clang\+\+)\b",
        "ARM GCC": r"\barm-none-eabi-(?:gcc|g\+\+)\b",
        "RISC-V GCC": r"\briscv(?:32|64)-[^/\s]*(?:gcc|g\+\+)\b",
        "CMake": r"\bcmake\b",
        "Make/Ninja": r"\b(?:make|ninja)\b",
        "MSVC": r"\b(?:cl\.exe|msbuild)\b",
    }
    embedded_patterns = {
        "FreeRTOS": r"\bFreeRTOS\b",
        "Zephyr": r"\bZephyr\b",
        "ESP-IDF": r"\bESP-IDF\b|\bidf_component_register\b",
        "STM32 HAL/Cube": r"\bSTM32\b|\bHAL_[A-Z][A-Za-z0-9_]+\b",
        "CMSIS": r"\bCMSIS\b|arm_math\.h",
        "Arduino": r"\bArduino\b|\.ino\b",
        "RT-Thread": r"\bRT-Thread\b",
    }
    inference_patterns = {
        "YOLO": r"\bYOLO(?:v\d+)?\b|\byolov\d+\b",
        "ONNX Runtime": r"\bonnx\s*runtime\b|\bonnxruntime\b|Ort::|OrtApi",
        "TensorRT": r"\bTensorRT\b|\bnvinfer\b|NvInfer",
        "OpenVINO": r"\bOpenVINO\b|InferenceEngine",
        "ncnn": r"\bncnn\b",
        "MNN": r"\bMNN\b",
        "TFLite": r"\bTFLite\b|tensorflow/lite|\.tflite\b",
        "RKNN": r"\bRKNN\b|rknn_",
        "OpenCV DNN": r"\bdnn::Net\b|readNetFrom",
        "Darknet": r"\bdarknet\b|\.weights\b",
        "TVM": r"\bTVM\b|tvm::",
        "llama.cpp / ggml": r"\bggml\b|\bllama\.cpp\b",
    }

    def collect_hits(patterns, limit=20):
        hits = []
        for label, pattern in patterns.items():
            regex = re.compile(pattern, re.IGNORECASE)
            for rel, content in texts:
                if regex.search(content):
                    hits.append({"name": label, "found_in": rel})
                    break
            if len(hits) >= limit:
                break
        return hits

    model_files = rel_paths(["*.onnx", "*.engine", "*.plan", "*.trt", "*.rknn", "*.tflite",
                             "*.mnn", "*.param", "*.bin", "*.weights", "*.pt", "*.pth"], limit=40)

    return {
        "manifests": manifests,
        "source_counts": source_counts,
        "compilers_and_build_tools": collect_hits(compiler_patterns),
        "embedded_signals": collect_hits(embedded_patterns),
        "inference_engines": collect_hits(inference_patterns),
        "model_files": model_files,
    }


def detect_api_routes(texts):
    routes = []
    for base in ("app/api", "src/app/api", "pages/api", "src/pages/api"):
        directory = ROOT / base
        if directory.is_dir():
            for path in directory.rglob("*.*"):
                if path.suffix in (".ts", ".js", ".tsx"):
                    routes.append("/" + str(path.relative_to(ROOT / base.split("/")[0])).replace("\\", "/"))
    pattern = re.compile(r"(?:app|router|api_router)\.(get|post|put|delete|patch|route)\(\s*['\"]([^'\"]+)")
    for rel, content in texts:
        if rel.endswith((".py", ".js", ".ts", ".mjs")):
            for method, route in pattern.findall(content):
                if route.startswith("/"):
                    routes.append(f"{method.upper()} {route}  ({rel})")
    return sorted(set(routes))[:80]


def detect_lan_startup(texts, node_scripts):
    hits = []
    for rel, content in texts:
        if re.search(r"['\"]0\.0\.0\.0['\"]|host:\s*(?:true|['\"]0\.0\.0\.0)", content):
            hits.append(rel)
    script_hits = [f"{rel}: {name} = {cmd}" for rel, scripts in node_scripts.items()
                   for name, cmd in scripts.items() if "--host" in cmd or "0.0.0.0" in cmd]
    return {"config_files": sorted(set(hits))[:10], "npm_scripts": script_hits}


def detect_mock(node_deps):
    found = [dep for dep in ("msw", "json-server", "vite-plugin-mock", "mockjs", "@faker-js/faker", "miragejs")
             if dep in node_deps]
    dirs = [name for name in ("mock", "mocks", "__mocks__", "src/mock") if (ROOT / name).is_dir()]
    return {"packages": found, "directories": dirs}


def detect_wsl_dependency(texts):
    """检测项目是否依赖或使用 WSL (Windows Subsystem for Linux)。"""
    result = {
        "uses_wsl": False,
        "evidence": [],
    }

    # 1. 配置文件检测
    wsl_config_files = [".wslconfig", ".wslconfig.local", "wsl.conf"]
    for name in wsl_config_files:
        if (ROOT / name).exists():
            result["uses_wsl"] = True
            result["evidence"].append(f"配置文件: {name}")

    # 2. 脚本中调用 wsl 命令
    wsl_cmd_patterns = [
        (r"\bwsl\s+(?:--\w+\s+)?(?:bash|sh|zsh|apt|yum|dnf)", "脚本中调用 wsl 命令"),
        (r"\bwsl\s+--install", "WSL 安装命令"),
        (r"\bwsl\s+--distribution\b", "指定 WSL 发行版"),
        (r"powershell\.exe.*wsl|wsl\.exe", "通过 PowerShell/直接调用 wsl.exe"),
    ]
    # 排除扫描器自身的文件；全局安装时脚本不在目标项目内，无需排除。
    scanner_dir = scanner_relative_prefix()
    for rel, content in texts:
        if scanner_dir and rel.startswith(scanner_dir):
            continue
        for pattern, label in wsl_cmd_patterns:
            for m in re.finditer(pattern, content, re.IGNORECASE):
                # 排除注释行
                line_start = content.rfind("\n", 0, m.start()) + 1
                line = content[line_start:content.find("\n", m.end())].strip()
                if not line.startswith("#") and not line.startswith("//"):
                    result["uses_wsl"] = True
                    result["evidence"].append(f"{label}: `{rel}` 中 `{m.group()}`")
                    break

    # 3. 文档/README 中提到 WSL
    doc_wsl_patterns = [
        (r"(?i)\bwsl\b.{0,30}(?:required|需要|必须|推荐|recommended)", "文档中说明需要 WSL"),
        (r"(?i)(?:run|execute|启动).{0,30}\bwsl\b", "文档中提到在 WSL 下运行"),
        (r"(?i)windows\s+subsystem\s+for\s+linux", "文档中提及 Windows Subsystem for Linux"),
        (r"(?i)\bwsl\s+2?\b.{0,20}(?:ubuntu|debian|发行版)", "文档中指定 WSL 发行版"),
    ]
    scanner_dir = scanner_relative_prefix()
    for rel, content in texts:
        if scanner_dir and rel.startswith(scanner_dir):
            continue
        # 只检查文档和配置文件
        if not rel.endswith((".md", ".txt", ".rst", ".adoc")):
            continue
        for pattern, label in doc_wsl_patterns:
            for m in re.finditer(pattern, content):
                result["uses_wsl"] = True
                ctx_start = max(0, m.start() - 20)
                ctx_end = min(len(content), m.end() + 20)
                ctx = content[ctx_start:ctx_end].replace("\n", " ").strip()
                result["evidence"].append(f"{label}: `{rel}` 中 ...{ctx}...")
                break  # 每个文件每种模式只报一次

    # 4. Dev Container 配置中指定 WSL 相关
    devcontainer = ROOT / ".devcontainer" / "devcontainer.json"
    if devcontainer.exists():
        content = read_text(devcontainer)
        if "wsl" in content.lower() or "remoteAuthority" in content:
            result["uses_wsl"] = True
            result["evidence"].append("devcontainer.json 中包含 WSL 相关配置")

    # 5. package.json scripts 中引用 wsl
    for rel, content in texts:
        if scanner_dir and rel.startswith(scanner_dir):
            continue
        if rel.endswith("package.json"):
            try:
                data = json.loads(content)
                for name, cmd in (data.get("scripts") or {}).items():
                    if "wsl" in cmd.lower():
                        result["uses_wsl"] = True
                        result["evidence"].append(f"package.json script `{name}` 调用 wsl")
            except json.JSONDecodeError:
                pass

    # 去重
    result["evidence"] = sorted(set(result["evidence"]))
    return result


def detect_mcp_servers():
    """检测 MCP (Model Context Protocol) servers 配置。"""
    servers = []

    # 项目级配置
    project_settings = ROOT / ".claude" / "settings.json"
    # 用户级配置
    home = Path.home()
    user_settings = home / ".claude" / "settings.json"

    for settings_path in [project_settings, user_settings]:
        if not settings_path.exists():
            continue
        try:
            data = json.loads(read_text(settings_path))
            mcp = data.get("mcpServers", {})
            for name, config in mcp.items():
                server_info = {
                    "name": name,
                    "scope": "project" if settings_path == project_settings else "user",
                    "command": None,
                    "args": [],
                    "url": None,
                }
                if isinstance(config, dict):
                    # stdio 类型
                    if "command" in config:
                        server_info["command"] = config["command"]
                        server_info["args"] = config.get("args", [])[:5]
                    # sse/http 类型
                    if "url" in config:
                        server_info["url"] = config["url"]
                servers.append(server_info)
        except (json.JSONDecodeError, OSError):
            continue

    # .mcp.json（另一种常见配置格式）
    mcp_json = ROOT / ".mcp.json"
    if mcp_json.exists():
        try:
            data = json.loads(read_text(mcp_json))
            mcp = data.get("mcpServers", data.get("servers", {}))
            for name, config in mcp.items():
                if isinstance(config, dict):
                    server_info = {
                        "name": name,
                        "scope": "project (.mcp.json)",
                        "command": config.get("command"),
                        "args": config.get("args", [])[:5],
                        "url": config.get("url"),
                    }
                    servers.append(server_info)
        except (json.JSONDecodeError, OSError):
            pass

    return servers


def detect_dev_platform():
    traces = {}
    checks = {
        ".vscode": "VS Code", ".idea": "JetBrains IDE",
        "CLAUDE.md": "Claude Code", ".claude": "Claude Code",
        ".cursorrules": "Cursor", ".cursor": "Cursor",
        ".windsurfrules": "Windsurf", ".trae": "Trae",
        ".github/copilot-instructions.md": "GitHub Copilot",
        ".devcontainer": "Dev Container",
        ".agents": "Claude Agents (global)",
    }
    for name, label in checks.items():
        if (ROOT / name).exists():
            traces.setdefault(label, []).append(name)

    # Claude Code skills（项目级 + 用户全局级）
    skills_dir = ROOT / ".claude" / "skills"
    project_skills = [p.name for p in skills_dir.iterdir() if p.is_dir()] if skills_dir.is_dir() else []
    commands_dir = ROOT / ".claude" / "commands"
    project_commands = [p.name for p in commands_dir.glob("*.md")] if commands_dir.is_dir() else []

    # 用户全局 skills
    home = Path.home()
    global_skills_dir = home / ".claude" / "skills"
    global_skills = [p.name for p in global_skills_dir.iterdir() if p.is_dir()] if global_skills_dir.is_dir() else []
    # ~/.agents/skills（另一种全局位置）
    agents_skills_dir = home / ".agents" / "skills"
    agents_skills = [p.name for p in agents_skills_dir.iterdir() if p.is_dir()] if agents_skills_dir.is_dir() else []

    all_skills = sorted(set(project_skills + global_skills + agents_skills))

    os_hints = []
    if list(ROOT.glob("*.bat")) or list(ROOT.glob("*.ps1")):
        os_hints.append("Windows (bat/ps1 scripts)")
    if list(ROOT.glob("*.sh")):
        os_hints.append("Unix-like (sh scripts)")

    return {
        "tools": traces,
        "claude_skills": {
            "project": project_skills,
            "global": global_skills,
            "agents_dir": agents_skills,
            "all": all_skills,
        },
        "claude_commands": project_commands,
        "os_hints": os_hints,
    }


def detect_monitoring(node_deps, py_deps):
    found = []
    monitor_map = {"@sentry/node": "Sentry", "@sentry/react": "Sentry", "@sentry/nextjs": "Sentry",
                   "sentry-sdk": "Sentry (py)", "posthog-js": "PostHog", "posthog": "PostHog",
                   "dd-trace": "Datadog", "prom-client": "Prometheus", "prometheus-client": "Prometheus",
                   "winston": "winston (logging)", "pino": "pino (logging)", "loguru": "loguru (logging)"}
    for dep, label in monitor_map.items():
        if dep in node_deps or dep in py_deps:
            found.append({"package": dep, "service": label})
    return found


def git_info():
    def run(args):
        try:
            r = subprocess.run(["git", *args], capture_output=True, timeout=10)
            return r.stdout.decode("utf-8", errors="replace").strip()
        except (OSError, subprocess.SubprocessError):
            return ""
    return {
        "remote": run(["remote", "get-url", "origin"]),
        "branch": run(["rev-parse", "--abbrev-ref", "HEAD"]),
        "last_commit": run(["log", "-1", "--format=%h %ad %s", "--date=short"]),
        "commit_count": run(["rev-list", "--count", "HEAD"]),
        "contributors": run(["shortlog", "-sn", "--no-merges", "HEAD"]).splitlines()[:10],
    }


def dir_tree(max_depth=2):
    lines = []
    def walk(directory, depth):
        if depth > max_depth:
            return
        try:
            entries = sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name))
        except OSError:
            return
        for path in entries:
            if path.name in SKIP_DIRS or path.name.startswith("."):
                continue
            lines.append("  " * depth + ("[DIR] " if path.is_dir() else "") + path.name)
            if path.is_dir():
                walk(path, depth + 1)
    walk(ROOT, 0)
    return lines[:150]


def build_key_files(report):
    candidates = ["README.md", "readme.md", ".env.example", "Dockerfile", "docker-compose.yml",
                  "wrangler.toml", "wrangler.jsonc", "prisma/schema.prisma",
                  "src-tauri/tauri.conf.json", "CLAUDE.md", "next.config.js", "next.config.ts",
                  "vite.config.ts", "vite.config.js", "nuxt.config.ts",
                  "pnpm-workspace.yaml", "turbo.json", "nx.json", "lerna.json",
                  ".gitlab-ci.yml", "Jenkinsfile", ".circleci/config.yml",
                  ".handoff.yml", ".mcp.json", "go.mod", "Cargo.toml", "pom.xml",
                  "build.gradle", "build.gradle.kts", "CMakeLists.txt", "Makefile",
                  "meson.build", "platformio.ini",
                  ".claude/settings.json", ".claude/skills", ".claude/commands"]
    files = []
    seen = set()
    for name in candidates:
        path = ROOT / name
        if path.exists():
            rel = str(path.relative_to(ROOT)).replace("\\", "/")
            key = rel.lower()
            if key not in seen:
                files.append(rel)
                seen.add(key)
    # CI/CD 文件
    ci = report.get("ci_cd", {})
    for wf in ci.get("github_actions", []):
        f = f".github/workflows/{wf['file']}"
        if f.lower() not in seen:
            files.append(f)
            seen.add(f.lower())
    # Docker
    docker = report.get("docker", {}).get("dockerfile")
    if docker and docker["path"].lower() not in seen:
        files.append(docker["path"])
        seen.add(docker["path"].lower())
    # k8s
    for res in report.get("kubernetes", {}).get("resources", [])[:5]:
        if res["file"].lower() not in seen:
            files.append(res["file"])
            seen.add(res["file"].lower())
    native = report.get("native_embedded_ai", {})
    manifests = native.get("manifests", {})
    for key in ("go", "rust", "java_jvm", "dotnet", "native_build", "embedded"):
        for path in manifests.get(key, [])[:5]:
            if path.lower() not in seen:
                files.append(path)
                seen.add(path.lower())
    for path in native.get("model_files", [])[:5]:
        if path.lower() not in seen:
            files.append(path)
            seen.add(path.lower())
    return files


def main() -> None:
    load_config()

    # 统计文件总数（用于扫描完整性报告）
    total_files = sum(1 for _ in ROOT.rglob("*") if _.is_file() and not any(p in SKIP_DIRS for p in _.parts))

    texts = collect_source_texts()
    scanned_count = len(texts)
    truncated = scanned_count >= MAX_GREP_FILES

    manifests = find_manifests()
    node_deps, node_scripts = load_node_deps(manifests["package_json"])
    py_deps = load_python_deps(manifests["requirements"], manifests["pyproject"])

    report = {
        "schema_version": SCHEMA_VERSION,
        "tool_version": TOOL_VERSION,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "project_name": ROOT.name,
        "package_manager": detect_package_manager(),
        "monorepo": detect_monorepo(node_deps),
        "frameworks": detect_framework(node_deps, py_deps, texts),
        "ui_libraries": detect_ui_libraries(node_deps),
        "desktop": detect_desktop(node_deps, manifests["csproj"]),
        "docker": detect_docker(),
        "cloudflare": detect_cloudflare(),
        "ci_cd": detect_ci_cd(),
        "kubernetes": detect_kubernetes(),
        "ai_services": detect_ai_services(node_deps, py_deps, texts),
        "external_resources": detect_external_resources(node_deps, texts),
        "environment_variables": detect_env_vars(texts),
        "database": detect_database(node_deps, py_deps),
        "native_embedded_ai": detect_native_embedded_ai(texts),
        "api_routes": detect_api_routes(texts),
        "lan_startup": detect_lan_startup(texts, node_scripts),
        "frontend_mock": detect_mock(node_deps),
        "dev_platform": detect_dev_platform(),
        "mcp_servers": detect_mcp_servers(),
        "wsl_dependency": detect_wsl_dependency(texts),
        "monitoring": detect_monitoring(node_deps, py_deps),
        "npm_scripts": node_scripts,
        "dependency_counts": {"node": len(node_deps), "python": len(py_deps)},
        "git": git_info(),
        "directory_tree": dir_tree(),
        "scan_completeness": {
            "total_files": total_files,
            "scanned_files": scanned_count,
            "truncated": truncated,
            "max_files": MAX_GREP_FILES,
        },
    }
    report["key_files_to_read"] = build_key_files(report)

    report_str = json.dumps(report, indent=2, ensure_ascii=False)

    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / "analysis-report.json"
    out.write_text(report_str, encoding="utf-8")

    print(f"Report written to {out.relative_to(ROOT)}")
    print(f"- Package manager: {report['package_manager']}")
    print(f"- Monorepo: {report['monorepo']['type'] or 'no'}")
    print(f"- Frameworks: {[f['name'] for f in report['frameworks']] or 'none detected'}")
    print(f"- UI libraries: {[u['name'] for u in report['ui_libraries']] or 'none'}")
    print(f"- Desktop: {[d['type'] for d in report['desktop']] or 'none'}")
    print(f"- CI/CD: GitHub={len(report['ci_cd']['github_actions'])}, GitLab={len(report['ci_cd']['gitlab_ci'])}, Jenkins={len(report['ci_cd']['jenkins'])}")
    print(f"- K8s resources: {len(report['kubernetes']['resources'])}")
    print(f"- AI SDKs: {[s['sdk'] for s in report['ai_services']['sdks']] or 'none'}")
    print(f"- Env vars declared/used: {len(report['environment_variables']['declared'])}/{len(report['environment_variables']['used_in_code'])}")
    print(f"- High entropy env values: {len(report['environment_variables']['high_entropy_values'])}")
    native = report["native_embedded_ai"]
    native_manifest_count = sum(len(v) for v in native["manifests"].values())
    print(f"- Native/embedded manifests: {native_manifest_count}; inference engines: {[h['name'] for h in native['inference_engines']] or 'none'}")
    print(f"- MCP servers: {[s['name'] for s in report['mcp_servers']] or 'none'}")
    print(f"- WSL dependency: {report['wsl_dependency']['uses_wsl']} ({len(report['wsl_dependency']['evidence'])} evidence)")
    print(f"- Claude skills: {report['dev_platform']['claude_skills']['all'] or 'none'}")
    print(f"- Scan: {scanned_count}/{total_files} files" + (" (TRUNCATED)" if truncated else ""))
    print(f"- MUST READ files: {report['key_files_to_read']}")


if __name__ == "__main__":
    main()

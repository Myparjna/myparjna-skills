#!/usr/bin/env python3
"""Generate handoff doc skeletons from analysis-report.json. Each TODO(AI) carries fill instructions."""
from pathlib import Path
import argparse
import json
import shutil
import sys
from datetime import datetime

from _handoff_common import force_utf8_console

ROOT = Path.cwd()
OUT = ROOT / "ProjectDoc"
REPORT_PATH = OUT / "analysis-report.json"
DEFAULT_PLAN_PATH = ROOT / "TempScr" / "project-handoff-plan.json"


def load_plan(plan_path: Path | None) -> dict:
    """读取 handoff-plan（plan_handoff.py 产物），不存在时返回空计划。"""
    path = plan_path or (DEFAULT_PLAN_PATH if DEFAULT_PLAN_PATH.exists() else None)
    if path is None:
        return {}
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        print(f"[WARN] 计划文件 {path} 解析失败，忽略该计划。")
        return {}
    print(f"已读取交接计划: {path}")
    return plan


def todo(instruction: str) -> str:
    return f"<!-- TODO(AI): {instruction} -->"


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def section(title, *body):
    return f"## {title}\n\n" + "\n\n".join(part for part in body if part)


def frontmatter(doc_name: str, level: str) -> str:
    """生成 YAML frontmatter。"""
    return f"""---
document: {doc_name}
generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}
client_level: {level}
---"""


def cross_ref(target: str, label: str) -> str:
    """生成交叉引用链接。"""
    return f"> 详见 [{target}](./{target}) 中的 {label}"


# ---------- documents ----------

def doc_readme(r, level):
    fw = ", ".join(f"{f['name']} {f['version']}" for f in r["frameworks"]) or "未检测到"
    ui = ", ".join(f"{u['name']} ({u['package']}@{u['version']})" for u in r["ui_libraries"]) or "无"
    pm = ", ".join(r.get("package_manager", ["unknown"]))
    audience_note = "面向非技术读者：避免术语，每个步骤给出截图位置或精确点击路径。" if level == "non-technical" else ""
    # 导航表含条件文档，与 main() 的生成条件保持一致
    nav_rows = [
        ["[ARCHITECTURE.md](./ARCHITECTURE.md)", "架构与技术选型"],
        ["[USAGE.md](./USAGE.md)", "项目使用说明与业务流程"],
        ["[MODULES.md](./MODULES.md)", "模块职责、入口与依赖"],
        ["[REGRESSION-TEST.md](./REGRESSION-TEST.md)", "回归测试范围与验证记录"],
        ["[ENVIRONMENT.md](./ENVIRONMENT.md)", "环境变量"],
        ["[DEPLOYMENT.md](./DEPLOYMENT.md)", "部署"],
        ["[INFRASTRUCTURE.md](./INFRASTRUCTURE.md)", "域名/账号/第三方服务"],
        ["[KNOWN-ISSUES.md](./KNOWN-ISSUES.md)", "已知问题"],
        ["[MAINTENANCE.md](./MAINTENANCE.md)", "日常维护"],
        ["[RUNBOOK.md](./RUNBOOK.md)", "故障处置"],
    ]
    ai = r.get("ai_services", {})
    if ai.get("sdks") or ai.get("endpoints") or ai.get("model_names"):
        nav_rows.append(["[AI-SERVICES.md](./AI-SERVICES.md)", "AI API 使用详情"])
    if r.get("api_routes"):
        nav_rows.append(["[API.md](./API.md)", "接口清单"])
    if r.get("database", {}).get("clients") or r.get("database", {}).get("orm"):
        nav_rows.append(["[DATABASE.md](./DATABASE.md)", "数据库"])
    if r.get("desktop"):
        nav_rows.append(["[DESKTOP.md](./DESKTOP.md)", "桌面端"])
    return "\n\n".join([
        frontmatter("README.md", level),
        f"# {r['project_name']} — 项目交接文档",
        section("待确认问题",
                todo("把本文档集内所有 `[需向交接人确认: ...]` 标记汇总到这里，每条一行；得到答复后同步更新对应正文并保留状态。没有时写'当前无待确认问题'。")),
        section("项目简介",
                todo("用 2-4 句话说明：这个项目是什么、给谁用、解决什么问题。来源：已有 README、主页面源码、向用户提问。禁止只罗列技术栈。" + audience_note)),
        section("核心功能",
                todo("列出 3-8 个核心功能点，每个一行。来源：阅读路由/页面结构 + 已有 README。格式：'- 功能名：一句话说明'")),
        section("技术栈",
                f"**框架**: {fw}",
                f"**UI 组件库**: {ui}",
                f"**包管理器**: {pm}",
                f"**依赖规模**: Node {r['dependency_counts']['node']} 个 / Python {r['dependency_counts']['python']} 个",
                todo("补充语言运行时版本要求（Node/Python 具体版本，从 package.json engines、.nvmrc、pyproject 中找；找不到写 [需向交接人确认: Node 版本要求]）")),
        section("快速启动",
                "```bash\n" + todo("写出从 git clone 到本地跑起来的完整命令序列，逐条验证可行性（依据 npm_scripts 和 README）。包含：安装依赖、复制 .env、启动命令、访问地址") + "\n```",
                f"**可用脚本**:\n{table(['命令', '用途'], [[f'`{k}`', todo('解释用途')] for s in r['npm_scripts'].values() for k in s][:12]) if r['npm_scripts'] else '无 npm scripts'}"),
        section("速查卡",
                table(["项目", "值", "出处/说明"], [
                    ["本地访问地址", todo("端口和 URL，从启动配置/运行验证中获取"), "启动后实际访问入口"],
                    ["生产访问入口", todo("生产 URL 或运行位置；未知写 [需向交接人确认: 生产入口]"), "用户/部署平台"],
                    ["启动一行命令", todo("从快速启动中提炼最核心的一条命令"), "快速启动"],
                    ["部署一行命令", todo("如 wrangler deploy / docker compose up -d / vercel --prod；详见 DEPLOYMENT.md"), "DEPLOYMENT.md"],
                    ["回滚一行命令", todo("如 wrangler rollback / 重部署上一 tag；详见 RUNBOOK.md"), "RUNBOOK.md"],
                    ["日志/监控入口", todo("看错误和用量的精确入口路径；详见 MAINTENANCE.md"), "MAINTENANCE.md"],
                ]),
                todo("速查卡要求：出事时 30 秒能扫完。每格只放具体值（URL/端口/一行命令/人名），禁止长句和概念描述；细节放对应文档。")),
        section("文档导航",
                table(["文档", "内容"], nav_rows)),
    ])


def doc_architecture(r):
    tree = "\n".join(r["directory_tree"])
    ext = r["external_resources"]
    ext_rows = []
    for key, label in [("huggingface_models", "HuggingFace 模型"), ("modelscope_models", "ModelScope 模型"),
                       ("github_dependencies", "GitHub 直装依赖"), ("cdn_links", "CDN 外链")]:
        for item in ext.get(key, []):
            value = item.get("value") or item.get("package", "")
            ext_rows.append([label, f"`{value}`", todo("说明用途、是否需要预下载、国内访问是否需要镜像")])
    lan = r["lan_startup"]
    lan_text = ""
    if lan["config_files"] or lan["npm_scripts"]:
        lan_text = section("局域网访问",
                           f"检测到绑定 0.0.0.0 / --host 的配置：\n- " + "\n- ".join(lan["config_files"] + lan["npm_scripts"]),
                           todo("说明：哪个命令以局域网模式启动、默认端口、防火墙注意事项、是否仅限开发环境"))
    mock = r["frontend_mock"]
    mock_text = ""
    if mock["packages"] or mock["directories"]:
        mock_text = section("前端 Mock",
                            f"检测到 mock 工具: {', '.join(mock['packages']) or '无包'}；mock 目录: {', '.join(mock['directories']) or '无'}",
                            todo("说明：mock 如何开启/关闭（环境变量？构建模式？）、哪些接口被 mock、上线前是否需要移除"))
    platform = r["dev_platform"]
    mcp = r.get("mcp_servers", [])
    wsl = r.get("wsl_dependency", {})

    # Monorepo 信息
    mono = r.get("monorepo", {})
    mono_text = ""
    if mono.get("type"):
        mono_text = section("Monorepo 结构",
                            f"- 类型: {mono['type']}\n- 工具: {', '.join(mono.get('tools', []))}\n- workspace 数量: {mono.get('workspace_count', '未知')}",
                            todo("说明各 workspace 的职责划分、依赖关系、构建顺序"))

    # Native / embedded / local inference 信息
    native = r.get("native_embedded_ai", {})
    native_text = ""
    if native:
        manifests = native.get("manifests", {})
        manifest_lines = []
        for key, label in [("go", "Go"), ("rust", "Rust"), ("java_jvm", "Java/JVM"),
                           ("dotnet", ".NET"), ("native_build", "C/C++ 构建"),
                           ("embedded", "嵌入式工程")]:
            paths = manifests.get(key, [])
            if paths:
                manifest_lines.append(f"- {label}: " + ", ".join(f"`{p}`" for p in paths[:8]))
        signal_lines = []
        for key, label in [("compilers_and_build_tools", "编译/构建工具"),
                           ("embedded_signals", "嵌入式线索"),
                           ("inference_engines", "本地推理引擎")]:
            hits = native.get(key, [])
            if hits:
                signal_lines.append(f"- {label}: " + ", ".join(f"{h['name']} (`{h['found_in']}`)" for h in hits))
        model_files = native.get("model_files", [])
        if model_files:
            signal_lines.append("- 模型/权重文件: " + ", ".join(f"`{p}`" for p in model_files[:12]))
        if manifest_lines or signal_lines:
            native_text = section("原生/嵌入式/本地推理",
                                  "\n".join(manifest_lines + signal_lines),
                                  todo("如果项目包含 C/C++/Go/Rust/Java/.NET、嵌入式固件或 YOLO/ONNX/TensorRT/RKNN 等本地推理，请说明：目标平台、交叉编译工具链、构建命令、模型文件来源、运行依赖、硬件加速要求和最小验证命令。不确定的硬件/板卡/驱动版本写 [需向交接人确认: ...]"))

    # WSL 信息
    wsl_text = ""
    if wsl.get("uses_wsl"):
        evidence_list = "\n".join(f"- {e}" for e in wsl.get("evidence", []))
        wsl_text = section("WSL 依赖",
                           f"检测到项目使用/依赖 WSL：\n{evidence_list}",
                           todo("说明：项目为什么需要 WSL（如依赖 Linux-only 的包/工具/服务），接手方在纯 Windows 或纯 Linux 下能否运行，如果必须 WSL 则给出安装和配置步骤"))

    # MCP servers 信息
    mcp_text = ""
    if mcp:
        mcp_rows = [[s["name"], s["scope"], s.get("command") or s.get("url") or "未知", todo("用途？")]
                    for s in mcp]
        mcp_text = section("MCP Servers",
                           table(["名称", "作用域", "命令/URL", "用途"], mcp_rows),
                           todo("说明每个 MCP server 的用途、是否需要额外安装、接手方是否需要配置"))

    # Skills / MCP / Agents 信息（需 AI 自报，脚本只能扫描目录结构）
    skills = platform.get("claude_skills", {})
    if isinstance(skills, dict):
        project_skills = skills.get("project", [])
        global_skills = skills.get("global", [])
    else:
        project_skills = skills if isinstance(skills, list) else []
        global_skills = []

    skills_parts = []
    if project_skills:
        skills_parts.append(f"**项目级 skills（目录扫描）**: {', '.join(project_skills)}")
    if global_skills:
        skills_parts.append(f"**全局 skills（目录扫描，共 {len(global_skills)} 个）**: {', '.join(global_skills[:10])}{'...' if len(global_skills) > 10 else ''}")
    if platform.get("claude_commands"):
        skills_parts.append(f"**Commands（目录扫描）**: {', '.join(platform['claude_commands'])}")

    skills_text = section("AI 工具链",
                          "\n\n".join(skills_parts) if skills_parts else "未扫描到 skills/commands 目录。",
                          todo("你在执行本技能的过程中实际使用了哪些 skills、MCP servers、子 agent？逐个列出名称和用途。"
                               "这些信息无法被脚本静态扫描，只有执行此技能的 AI 自己知道。"
                               "格式：'- **skill 名称**: 用途' / '- **MCP server**: 用途' / '- **Agent 类型**: 用途'"))

    return "\n\n".join(filter(None, [
        frontmatter("ARCHITECTURE.md", "developer"),
        "# 系统架构",
        section("架构总览",
                "```mermaid\n" + todo("画出系统架构图：前端、后端、数据库、外部 AI API、部署平台之间的调用关系。依据 analysis-report 中的 frameworks/docker/cloudflare/ai_services/database") + "\n```",
                todo("用一段话解释数据流向：用户请求从哪进来、经过什么、数据存到哪")),
        section("目录结构", f"```\n{tree}\n```", todo("为上面树中 5-10 个关键目录各加一行用途说明")),
        mono_text,
        native_text,
        wsl_text,
        section("技术选型与路线",
                todo("说明关键技术为什么这么选（如有历史原因或曾经换过方案，向用户提问后记录）。来源：CLAUDE.md、git log、向用户提问。不知道就写 [需向交接人确认: 技术选型背景]")),
        section("外部资源依赖", table(["类型", "资源", "说明"], ext_rows) if ext_rows else "未检测到外部模型/CDN 资源。",
                todo("核对 external_resources 中的 github_urls 和 huggingface_urls，把属于'运行必需'的资源补进上表，纯文档引用的忽略")),
        lan_text,
        mock_text,
        mcp_text,
        skills_text,
        section("开发环境痕迹",
                f"检测到的开发工具: {json.dumps(platform['tools'], ensure_ascii=False)}\n\n"
                f"操作系统线索: {platform['os_hints'] or '不明'}",
                todo("说明原开发平台（Windows/macOS/Linux/WSL）和所用 AI 工具，以及接手方是否需要这些配置")),
    ]))


def doc_environment(r):
    env = r["environment_variables"]
    rows = [[f"`{v['name']}`", v["source"], todo("补充：用途、获取方式（精确入口）、必需性（本地/CI/生产）、泄露影响（高/中/低）。")]
            for v in env["declared"]]
    rows += [[f"`{name}`", "**仅源码中使用，未在 .env.example 声明**", todo("补充：源码用途、是否应加入 .env.example、获取方式、必需性、泄露影响。")]
             for name in env["used_but_not_declared"]]
    unused = ""
    if env["declared_but_not_used"]:
        unused = section("疑似废弃变量",
                         "以下变量在 .env 中声明但源码中未检索到使用：" + ", ".join(f"`{n}`" for n in env["declared_but_not_used"]),
                         todo("逐个确认是否真的废弃（可能在配置文件/CI 中使用），废弃的标注'可删除'"))

    # 高熵值警告
    high_entropy = ""
    if env.get("high_entropy_values"):
        he_list = "\n".join(f"- `{h['variable']}` ({h['source']}, 熵={h['entropy']})" for h in env["high_entropy_values"])
        high_entropy = section("高熵值警告",
                               f"以下 .env 变量的值疑似真实密钥（高熵），请确认是否需要轮换：\n{he_list}",
                               todo("确认这些变量的值是否为真实密钥，如果是则在交接后必须轮换"))

    return "\n\n".join(filter(None, [
        frontmatter("ENVIRONMENT.md", "developer"),
        "# 环境变量",
        "⚠️ 本文档不包含任何真实密钥值。真实值通过安全渠道单独交接。",
        cross_ref("DEPLOYMENT.md", "密钥在各部署平台的配置位置"),
        section("变量清单", table(["变量名", "来源", "交接说明"], rows) if rows else "未检测到环境变量。"),
        unused,
        high_entropy,
        section("密钥轮换", todo("说明交接后哪些密钥必须立刻轮换。交接后默认应轮换所有 API key 与连接串；若某个密钥确认不轮换，必须写明原因并确认其权限范围。逐个给出轮换入口")),
    ]))


def doc_deployment(r, level):
    parts = [frontmatter("DEPLOYMENT.md", level), "# 部署指南"]
    docker = r["docker"]
    if docker.get("dockerfile"):
        d = docker["dockerfile"]
        parts.append(section("Docker 部署",
                             f"- Dockerfile: `{d['path']}`（{'多阶段' if d['multi_stage'] else '单阶段'}构建）\n"
                             f"- 基础镜像: {', '.join(d['base_images'])}\n"
                             f"- 暴露端口: {', '.join(d['exposed_ports']) or '未声明'}\n"
                             f"- 启动命令: {'; '.join(d['cmd']) or '未声明'}",
                             "```bash\n" + todo("写出完整可复制的命令：构建镜像（含 tag 规范）、运行容器（含端口映射、env 文件挂载、volume）、查看日志、停止重启") + "\n```"))
    if docker.get("compose"):
        c = docker["compose"]
        parts.append(section("Docker Compose",
                             f"- 文件: `{c['path']}`\n- 服务: {', '.join(c['services'])}\n- 端口映射: {', '.join(c['ports']) or '无'}",
                             todo("逐个服务说明其作用、依赖顺序、数据持久化位置（volume 在哪）")))
    cf = r["cloudflare"]
    if cf.get("wrangler"):
        w = cf["wrangler"]
        bindings = []
        for key, label in [("kv_namespaces", "KV"), ("d1_databases", "D1"), ("r2_buckets", "R2")]:
            bindings += [f"{label}: `{b}`" for b in w.get(key, [])]
        parts.append(section("Cloudflare Workers",
                             f"- Worker 名称: `{w['name']}`\n- 入口: `{w['main']}`\n"
                             f"- 路由: {', '.join(w['routes']) or '未配置'}\n- 绑定: {', '.join(bindings) or '无'}",
                             "```bash\n" + todo("写出：wrangler login → 本地调试(wrangler dev) → 发布(wrangler deploy) → secret 设置(wrangler secret put XXX，逐个列出需要的 secret 名) 的完整命令") + "\n```",
                             todo("说明 KV/D1/R2 绑定的资源如何创建（首次部署到新账号时），D1 是否需要执行 migration")))
    if cf.get("pages_functions") or cf.get("pages_config_files"):
        parts.append(section("Cloudflare Pages", todo("说明 Pages 项目的构建配置（构建命令、输出目录）、自定义域绑定、环境变量在 Pages 后台的设置位置")))

    # CI/CD（新版结构）
    ci = r["ci_cd"]
    if ci.get("github_actions"):
        rows = [[wf["file"], wf["name"], ", ".join(wf["triggers"]), ", ".join(f"`{s}`" for s in wf["secrets_used"]) or "无"]
                for wf in ci["github_actions"]]
        parts.append(section("CI/CD (GitHub Actions)",
                             table(["Workflow", "名称", "触发", "用到的 Secrets"], rows),
                             todo("逐个 workflow 说明：它做什么、何时触发、失败了去哪看日志。逐个 secret 说明：是什么、新仓库迁移时如何在 Settings → Secrets 重新配置")))
    if ci.get("gitlab_ci"):
        for wf in ci["gitlab_ci"]:
            parts.append(section("CI/CD (GitLab CI)",
                                 f"- 文件: `{wf['file']}`\n- Stages: {', '.join(wf.get('stages', [])) or '未检测到'}\n- Variables: {', '.join(wf.get('variables', [])) or '无'}",
                                 todo("说明各 stage 的作用、变量如何配置、CI/CD pipeline 的触发条件")))
    if ci.get("jenkins"):
        for wf in ci["jenkins"]:
            parts.append(section("CI/CD (Jenkins)",
                                 f"- 文件: `{wf['file']}`\n- Stages: {', '.join(wf.get('stages', [])) or '未检测到'}",
                                 todo("说明 Jenkins pipeline 的构建流程和触发条件")))
    if ci.get("circleci"):
        for wf in ci["circleci"]:
            parts.append(section("CI/CD (CircleCI)",
                                 f"- 文件: `{wf['file']}`\n- Jobs: {', '.join(wf.get('jobs', [])) or '未检测到'}",
                                 todo("说明各 job 的作用、workflow 触发条件、环境变量在 CircleCI 项目设置中的配置位置")))

    # Vercel / Netlify / VPS 部署痕迹
    targets = r.get("deployment_targets", {})
    if targets.get("vercel"):
        parts.append(section("Vercel 部署",
                             f"检测到: {', '.join(f'`{t}`' for t in targets['vercel'])}",
                             todo("说明：vercel CLI 登录和部署命令、环境变量在 Dashboard 的设置、自定义域绑定、Serverless Functions 配置")))
    if targets.get("netlify"):
        parts.append(section("Netlify 部署",
                             f"检测到: {', '.join(f'`{t}`' for t in targets['netlify'])}",
                             todo("说明：构建命令和发布目录、环境变量设置、_redirects/_headers 配置、Functions 配置")))
    if targets.get("vps"):
        parts.append(section("VPS / 自建服务器",
                             "\n".join(f"- {t}" for t in targets["vps"]),
                             todo("说明：SSH 连接方式（不写私钥，写'通过安全渠道交接'）、系统依赖安装、部署路径、进程管理（systemd/pm2/supervisor）、反向代理与 SSL 配置、防火墙规则")))

    # Kubernetes
    k8s = r.get("kubernetes", {})
    if k8s.get("resources"):
        parts.append(section("Kubernetes 部署",
                             f"- 资源数: {len(k8s['resources'])}\n- 命名空间: {', '.join(k8s.get('namespaces', [])) or 'default'}\n- 镜像: {', '.join(k8s.get('images', [])) or '未检测到'}",
                             todo("说明 k8s 部署流程：kubectl apply 命令、namespace 创建、ConfigMap/Secret 配置、Ingress 域名绑定")))

    for desktop in r["desktop"]:
        parts.append(section(f"桌面端 — {desktop['type']}", "详见 [DESKTOP.md](./DESKTOP.md)"))
    if not any([docker, cf.get("wrangler"), ci.get("github_actions"), ci.get("gitlab_ci"),
                ci.get("jenkins"), ci.get("circleci"), k8s.get("resources"),
                targets.get("vercel"), targets.get("netlify"), targets.get("vps")]):
        parts.append(section("部署方式", todo("未检测到 Docker/CF/CI/K8s/Vercel/Netlify/VPS 配置。向用户询问当前的实际部署方式并记录完整步骤，或写 [需向交接人确认: 部署方式]")))
    parts.append(section("首次完整部署演练", todo("假设接手方拿到一个全新账号/服务器，按顺序列出从零到上线的 checklist（编号步骤，每步一条命令或一个精确的后台操作）" + ("。读者非技术人员，每步注明在哪个网页点什么。" if level == "non-technical" else ""))))
    parts.append(cross_ref("ENVIRONMENT.md", "环境变量配置"))
    return "\n\n".join(parts)


def doc_infrastructure(r):
    return "\n\n".join([
        frontmatter("INFRASTRUCTURE.md", "developer"),
        "# 基础设施与账号",
        section("域名与 DNS", todo("列出所有域名、注册商、DNS 托管位置（是否在 Cloudflare）、SSL 证书来源。来源：wrangler routes、CI 配置、向用户提问")),
        section("第三方服务账号清单",
                table(["服务", "用途", "账号归属", "交接动作"],
                      [[todo("逐个列出：Cloudflare/GitHub/AI API 平台/数据库托管/监控等"), "", "", "转移所有权或重新注册"]]),
                todo("依据 analysis-report 的 cloudflare/ai_services/monitoring/git.remote 推断服务清单，账号归属向用户确认")),
        section("服务器/托管资源", todo("如有 VPS/云服务器：IP、提供商、SSH 访问方式（不写私钥，写'通过安全渠道交接'）。没有则写'无，全部使用 serverless/托管平台'")),
    ])


def doc_ai_services(r):
    ai = r["ai_services"]
    sdk_rows = [[s["sdk"], f"`{s['package']}@{s['version']}`", todo("在哪个功能中使用？读调用处源码")] for s in ai["sdks"]]
    ep_rows = [[f"`{e['value']}`", e["found_in"], todo("对应什么功能")] for e in ai["endpoints"]]
    models = ", ".join(f"`{m['value']}`" for m in ai["model_names"]) or "未检测到"
    return "\n\n".join([
        frontmatter("AI-SERVICES.md", "developer"),
        "# AI 服务",
        section("使用的 SDK", table(["SDK", "包", "用途"], sdk_rows) if sdk_rows else "未检测到 AI SDK。"),
        section("API 端点", table(["端点", "出现位置", "功能"], ep_rows) if ep_rows else "未检测到直连端点。"),
        section("模型", f"源码中出现的模型名: {models}", todo("说明每个模型用于什么功能、能否替换为其他模型、替换时要改哪个文件哪一行")),
        section("计费与限额", todo("逐个 AI 服务说明：计费方式（按 token/按次）、当前账号的限流等级、大致月消耗（向用户问）、余额告警在哪设置")),
        section("降级与故障", todo("说明：AI API 不可用时系统表现如何？有无重试/超时/降级逻辑？读调用处源码确认，没有就如实写'无降级逻辑，API 故障时功能 X 不可用'")),
    ])


def doc_api(r):
    routes = "\n".join(f"- `{route}`" for route in r["api_routes"])
    parts = [
        frontmatter("API.md", "developer"),
        "# API 文档",
        section("接口清单（扫描所得）", routes or "未检测到",
                todo("逐个补充：用途、请求/响应示例（读源码获取真实字段，禁止编造字段名）。数量太多时优先覆盖核心业务接口，其余归类说明")),
    ]
    if r.get("api_specs"):
        parts.append(section("OpenAPI / Swagger 规范",
                             "\n".join(f"- `{spec}`" for spec in r["api_specs"]),
                             todo("说明规范文件与实现的同步方式（手写/代码生成），访问入口（如 /docs 或 /swagger），字段定义以哪个为准")))
    parts.append(section("鉴权", todo("说明 API 的鉴权方式（API key? JWT? session? 无鉴权?），读中间件/拦截器源码确认。如果发现无鉴权的敏感接口，在 KNOWN-ISSUES.md 中记录")))
    return "\n\n".join(parts)


def doc_database(r):
    db = r["database"]
    models = ""
    if db.get("prisma_models"):
        models = "Prisma 模型: " + ", ".join(f"`{m}`" for m in db["prisma_models"])
    return "\n\n".join([
        frontmatter("DATABASE.md", "developer"),
        "# 数据库",
        section("概况",
                f"- 类型: {', '.join(db['clients']) or '未检测到客户端'}\n- ORM: {', '.join(db['orm']) or '无'}\n- 迁移目录: {', '.join(db['migrations']) or '无'}\n{models}",
                todo("说明数据库部署位置（本地文件/托管服务/D1？）、连接串对应哪个环境变量")),
        section("数据模型", todo("画 mermaid ER 图或逐表说明核心表/集合的用途和关键字段。来源：schema 文件、模型定义源码")),
        section("迁移", "```bash\n" + todo("写出执行迁移的命令（依据 ORM 类型），以及新增字段时的标准流程") + "\n```"),
        section("备份与恢复", todo("说明当前备份机制（很可能没有——如实写），并给出手动备份和恢复的具体命令")),
    ])


def doc_desktop(r):
    parts = [frontmatter("DESKTOP.md", "developer"), "# 桌面端"]
    for desktop in r["desktop"]:
        parts.append(section(desktop["type"],
                             f"配置: {json.dumps(desktop, ensure_ascii=False)}",
                             "```bash\n" + todo("写出：开发模式启动、生产构建/打包命令（区分 Windows/macOS 目标）、产物输出位置") + "\n```",
                             todo("说明：代码签名状态（有无证书、在谁手里）、自动更新机制（有/无，更新服务器在哪）、安装包分发渠道")))
    return "\n\n".join(parts)


def doc_known_issues():
    return "\n\n".join([
        frontmatter("KNOWN-ISSUES.md", "developer"),
        "# 已知问题与技术债",
        "> 这是交接中最有价值的文档。宁可多写，不可隐瞒。",
        section("已知 Bug", todo("向用户提问收集；同时检索源码中的 TODO/FIXME/HACK 注释并逐条核实记录（格式：现象 → 影响 → 临时绕过方法 → 相关文件）")),
        section("未完成功能", todo("向用户提问：有哪些做了一半的功能？对应哪些代码？接手方应该继续还是删掉？")),
        section("技术债", todo("基于你阅读源码的观察如实记录：重复代码、缺测试、硬编码、过期依赖等。这部分允许 AI 主动判断，但每条要给出具体文件位置")),
        section("安全注意项", todo("记录扫描和读码中发现的安全隐患：无鉴权接口、密钥硬编码、依赖漏洞等。没有就写'未发现明显问题，但未做专业安全审计'")),
    ])


def doc_maintenance(r):
    monitoring = "\n".join(f"- {m['service']} (`{m['package']}`)" for m in r["monitoring"]) or "未检测到监控/日志组件。"
    return "\n\n".join([
        frontmatter("MAINTENANCE.md", "developer"),
        "# 日常维护",
        section("监控与日志", monitoring,
                todo("说明：去哪看错误（Sentry 项目地址？CF Dashboard 的 Workers 日志？容器 docker logs？）、去哪看用量/账单，逐个给出入口路径")),
        section("依赖更新", todo("给出安全更新的检查命令（npm audit / pip-audit）和更新策略建议（哪些依赖锁版本不要乱升，依据 KNOWN-ISSUES 中的坑）")),
        section("例行检查清单", todo("给一个每月维护 checklist：证书有效期、API 余额、备份、依赖漏洞，每项附检查方法")),
    ])


def doc_runbook(level):
    return "\n\n".join([
        frontmatter("RUNBOOK.md", level),
        "# 运维手册 (Runbook)",
        section("回滚", "```bash\n" + todo("按部署平台写出具体回滚命令：CF Workers 用 wrangler rollback / Dashboard 版本回退；Docker 用上一个 tag 重新部署；写真实命令不写概念") + "\n```"),
        section("常见故障处置",
                table(["症状", "可能原因", "处置步骤"],
                      [[todo("覆盖至少：服务完全不可用 / AI 功能报错 / 部署失败 / 数据库连不上，每条给可执行的排查命令"), "", ""]])),
        section("密钥失效处理", todo("逐个关键密钥说明：失效时的现象、去哪重新生成、更新到哪里（env? CF secret? GitHub secret?）")),
    ])


def doc_usage(r, level):
    return "\n\n".join([
        frontmatter("USAGE.md", level),
        "# 项目使用说明",
        section("适用角色与入口",
                todo("说明谁使用本项目、每类角色从哪里进入（网址、桌面程序、CLI 或设备入口）、需要什么前置权限。入口必须来自源码、配置或实际运行验证。")),
        section("核心使用流程",
                todo("按真实业务顺序写 2-6 条典型流程。每条包含：前置条件、操作步骤、输入、预期输出、失败表现。界面项目需依据真实浏览器/软件操作验证。")),
        section("启动与停止",
                todo("分别写开发和生产环境的启动、访问、健康检查、停止命令；说明默认端口和进程关系。不得只引用 README。")),
        section("数据与文件",
                todo("说明用户需要准备的输入数据/文件格式、输出位置、命名规则、保留周期和清理方式。没有文件输入输出时如实说明。")),
        section("权限与安全边界",
                todo("说明登录、角色权限、局域网/公网边界、敏感操作和不可在生产环境执行的操作。源码无法确认时标记待确认。")),
        section("常见使用问题",
                todo("记录真实可复现的常见问题及解决步骤。没有实际证据时写未收集到，不得编造案例。")),
    ])


def doc_modules(r):
    tree = "\n".join(r.get("directory_tree", []))
    return "\n\n".join([
        frontmatter("MODULES.md", "developer"),
        "# 模块说明",
        section("模块总览",
                "```mermaid\n" + todo("画出核心模块依赖图，标明调用方向；不要重复 ARCHITECTURE 的部署架构图。") + "\n```",
                todo("用一段话说明模块边界和主执行链路。")),
        section("模块职责矩阵",
                table(["模块", "职责", "入口文件", "上游", "下游", "关键配置", "测试"],
                      [[todo("逐个列出核心业务模块，而不是逐文件罗列"), "", "", "", "", "", ""]])),
        section("关键目录",
                f"```\n{tree}\n```",
                todo("从目录树中选择核心目录，说明其职责、所有权边界以及不能随意修改的约束。")),
        section("关键调用链",
                todo("按真实源码描述 2-5 条关键调用链，格式：入口 -> 业务模块 -> 数据/外部服务 -> 输出，并给出文件路径。")),
        section("共享状态与数据边界",
                todo("说明模块之间共享的数据库表、缓存、文件、消息、全局状态或硬件资源；指出并发和生命周期约束。")),
        section("扩展与替换点",
                todo("说明新增功能通常改哪些模块、已有插件/适配器接口、模型或硬件后端如何替换。没有正式扩展点时如实说明。")),
    ])


def doc_regression_test(r):
    testing = r.get("testing", {})
    scripts = testing.get("test_scripts", [])
    script_rows = [[f"`{item['name']}`", f"`{item['command']}`", item["source"], todo("说明覆盖范围和预期结果")]
                   for item in scripts]
    evidence = (
        f"- 测试配置: {', '.join(f'`{item}`' for item in testing.get('config_files', [])) or '未检测到'}\n"
        f"- 测试目录: {', '.join(f'`{item}`' for item in testing.get('test_directories', [])) or '未检测到'}\n"
        f"- 测试文件数: {testing.get('test_file_count', 0)}"
    )
    return "\n\n".join([
        frontmatter("REGRESSION-TEST.md", "developer"),
        "# 回归测试说明",
        section("测试现状", evidence,
                table(["命令", "实际命令", "来源", "覆盖范围"], script_rows) if script_rows else "未检测到 package test scripts。",
                todo("阅读测试配置和测试代码，说明现有自动化测试真实覆盖了什么、没有覆盖什么。")),
        section("回归范围",
                table(["业务流程/模块", "风险", "验证方式", "通过标准", "证据位置"],
                      [[todo("覆盖 USAGE.md 的核心流程和 MODULES.md 的高风险模块"), "", "", "", ""]])),
        section("自动化测试",
                "```bash\n" + todo("列出已实际执行的单元、集成、端到端、构建或静态检查命令；每条写运行目录和必要环境。未执行的命令明确标注未执行。") + "\n```",
                todo("记录执行日期、结果、失败项和日志/报告位置。禁止把仅发现的脚本写成已通过。")),
        section("人工与真实软件验证",
                todo("列出必须用真实浏览器、桌面程序、CLI、设备或硬件验证的步骤。写清操作、预期结果、实际结果和截图/日志路径；不适用时说明原因。")),
        section("测试数据与环境",
                todo("说明测试账号、测试数据、fixture、模型、设备、浏览器/系统版本和外部依赖。不得写真实密码或密钥。")),
        section("发布前最小回归清单",
                todo("给出可逐项勾选的最小回归清单，至少覆盖启动、核心流程、数据持久化、异常路径、部署/构建和回滚。")),
        section("已知测试缺口",
                todo("记录缺少自动化、无法复现、依赖专用硬件或外部账号的测试项，并说明风险和补测建议。")),
    ])


# ---------- main ----------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client-level", default="developer", choices=["non-technical", "developer", "devops"])
    parser.add_argument("--mode", default="auto", choices=["auto", "create", "update", "rebuild"],
                        help="auto: existing docs use incremental update; rebuild: replace generated docs")
    parser.add_argument("--plan", default=None,
                        help="handoff-plan JSON 路径；默认自动读取 TempScr/project-handoff-plan.json")
    parser.add_argument("--ignore-plan", action="store_true",
                        help="忽略 handoff-plan，按默认检测逻辑生成全部文档")
    args = parser.parse_args()

    if not REPORT_PATH.exists():
        sys.exit("ERROR: 先运行 scripts/analyze_project.py 生成 analysis-report.json")
    r = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    # schema 版本检查
    schema_ver = r.get("schema_version", 0)
    if schema_ver < 3:
        print(f"[WARN] analysis-report.json 的 schema_version={schema_ver}，当前工具 3.1.1 需要 schema_version>=3。"
              "建议重新运行 analyze_project.py。")

    OUT.mkdir(exist_ok=True)

    docs = {
        "README.md": doc_readme(r, args.client_level),
        "USAGE.md": doc_usage(r, args.client_level),
        "ARCHITECTURE.md": doc_architecture(r),
        "MODULES.md": doc_modules(r),
        "ENVIRONMENT.md": doc_environment(r),
        "DEPLOYMENT.md": doc_deployment(r, args.client_level),
        "INFRASTRUCTURE.md": doc_infrastructure(r),
        "KNOWN-ISSUES.md": doc_known_issues(),
        "MAINTENANCE.md": doc_maintenance(r),
        "REGRESSION-TEST.md": doc_regression_test(r),
        "RUNBOOK.md": doc_runbook(args.client_level),
    }
    if r["ai_services"]["sdks"] or r["ai_services"]["endpoints"] or r["ai_services"]["model_names"]:
        docs["AI-SERVICES.md"] = doc_ai_services(r)
    if r["api_routes"]:
        docs["API.md"] = doc_api(r)
    if r["database"]["clients"] or r["database"]["orm"]:
        docs["DATABASE.md"] = doc_database(r)
    if r["desktop"]:
        docs["DESKTOP.md"] = doc_desktop(r)

    # 尊重 handoff-plan 的 skip 决策（用户已确认的计划）
    if not args.ignore_plan:
        plan = load_plan(Path(args.plan) if args.plan else None)
        skips = {d["name"] for d in plan.get("documents", []) if d.get("action") == "skip"}
        for name in sorted(skips & set(docs)):
            del docs[name]
            print(f"  {name:22s} 按 handoff-plan 跳过")

    generated_names = set(docs) | {"AI-SERVICES.md", "API.md", "DATABASE.md", "DESKTOP.md"}
    existing_generated = {path.name for path in OUT.glob("*.md") if path.name in generated_names}
    mode = args.mode
    if mode == "auto":
        mode = "update" if existing_generated else "create"
    if mode == "create" and existing_generated:
        sys.exit("ERROR: 已存在交接文档。请使用 --mode update 增量补齐，或经用户明确同意后使用 --mode rebuild。")
    if mode == "rebuild":
        backup = ROOT / "TempFiles" / f"ProjectDoc_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        backup.parent.mkdir(exist_ok=True)
        shutil.copytree(OUT, backup)
        print(f"  已备份旧文档到 {backup.relative_to(ROOT)}")
        for name in generated_names:
            path = OUT / name
            if path.exists():
                path.unlink()

    written = 0
    preserved = 0
    for name, content in docs.items():
        path = OUT / name
        if mode == "update" and path.exists():
            preserved += 1
            print(f"  {name:22s} 保留，等待 AI 按更新建议原地修改")
            continue
        path.write_text(content + "\n", encoding="utf-8")
        written += 1
        todo_count = content.count("TODO(AI)")
        print(f"  {name:22s} {todo_count} 个 TODO 待填写")

    print(f"\n模式: {mode}; 新写入 {written} 份，保留 {preserved} 份。")
    if mode == "update":
        print("下一步：读取 TempScr/project-handoff-update-plan.md、旧文档和变更源码，只原地修改受影响章节。")
    else:
        print("下一步：按 skill 目录下的 fill-guide.md 逐个消除 TODO(AI)，然后运行 verify_handoff.py。")


# Windows GBK 控制台处理统一收拢到公共模块
force_utf8_console()

if __name__ == "__main__":
    main()

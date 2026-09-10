---
name: project-handoff
description: "用户提到 交接文档、更新交接文档、重建交接文档、比对交接文档、查看交接文档、更新文档、项目交付、交接给同事或 AI 时必须使用本技能；想把项目整理成一套完整文档时也使用。创建、增量更新、比对或重建项目交接文档。默认增量更新，仅当用户明确说“重建/重新生成”才全量重置。"
---

# Project Handoff

依据实际源码、配置、扫描报告和用户回答维护 `ProjectDoc/`。采用 8 份基础文档加按需专题。脚本需要 Python 3.11+，可用 `uv run --no-project python` 运行。

## 按请求选择范围

| 请求 | 执行范围 |
|---|---|
| 查看、解释 | 只读相关文档和必要源码，不扫描、不生成、不运行会推进基线的验收 |
| 比对 | 定位、扫描、差异建议；不改交接正文、不推进验收基线 |
| 更新 | 增量改受影响章节，补缺失文档，保留人工内容 |
| 首次创建 | 无旧文档时创建并补全适用文档 |
| 明确重建、重新生成 | 备份后 rebuild；不得把“更新”理解为重建 |

下列 5 阶段用于完整创建和更新，不要求所有请求执行全部阶段。明确且核实过的根目录可直接采用；查看请求完成阅读即可结束。

## 必须保留的要求

- 内容必须来自扫描报告、实际读过的源码/配置或用户回答。不确定写 `[需向交接人确认: 具体问题]`。
- 机器检测不等于业务事实。核对部署、变量用途、接口和模型调用；扫描不完整时补读。
- 处理所有 TODO(AI)，不为凑数量编写功能、流程、目录或调用链。
- 区分检测到测试、实际执行、执行通过；只有观察结果才写通过。
- 保留人工决策、业务约定、运维经验。preserve 表示机器未发现影响，新源码证据可推翻并注明原因。
- 创建、更新、重建后必须验收，修复 ERROR/CRITICAL 后再交付；查看与只做比对不运行验收。

## 阶段 1：定位项目和模式

仅在位置不明、多项目或首次探索时运行：

```bash
python /absolute/path/to/project-handoff/scripts/discover_project.py --start . --max-depth 3
```

检查项目标志和已有交接目录，不能只凭修改时间选目录。单一明确目标直接采用；多个目标且用户意图不明时询问，禁止扫描整个父工作区。之后在选定项目根目录运行脚本。

无旧文档 create；已有文档默认 update；仅明确同意完全重置时 rebuild。

## 阶段 2：收集事实

```bash
python /absolute/path/to/project-handoff/scripts/analyze_project.py
```

生成 `ProjectDoc/analysis-report.json`。`.handoff/analysis-report.verified.json` 为稳定验收基线，重复扫描不推进它。报告包含重点文件和已扫描文本指纹；扫描范围有限，不能替代源码阅读。

## 阶段 3：计划与影响检查

```bash
python /absolute/path/to/project-handoff/scripts/plan_handoff.py --intent update
```

按实际模式替换 intent。计划写入 `TempScr/project-handoff-plan.md/.json`，快速检查文档、focus 和扫描范围后自动继续，不增加例行确认。

更新或比对时再运行 `scripts/compare_handoff.py`（使用技能绝对路径），产出 `TempScr/project-handoff-update-plan.md/.json`。简要告知受影响内容后继续已授权工作。首次创建无需新旧比对。

专题很简单时可在计划中 skip，并在对应基础文档写清内容；8 份基础文档保留。计划只提供机器证据，不能禁止有源码依据的语义更新。

## 阶段 4：按需阅读与编写

先读受影响旧文档、必要源码及变更文件。完整首次创建核对 `key_files_to_read`；增量更新优先阅读变化与受影响路径，必要时扩展。应能解释业务目的、实际部署、变量用途和适用的 AI 调用。

填写前读 [fill-guide.md](fill-guide.md) 公共规则，再只加载本次涉及的指南：

- 概览、使用、架构与模块：`references/writing-core.md`。
- 环境、部署、资源、维护与故障：`references/writing-runtime.md`。
- 测试、已知问题、API、数据库、AI、桌面：`references/writing-topics.md`。
- 非默认受众或受众变化：`references/client-levels.md`。
- 具体部署平台：`references/deployment-platforms.md` 中对应章节。

```bash
python /absolute/path/to/project-handoff/scripts/generate_handoff.py --mode update --client-level developer
```

create 首次创建；update 只补缺失文档；rebuild 备份后重建。根据实际模式执行。生成器尊重计划的专题选择，导航与验收使用相同集合。AI 补齐新文档，并原地修改旧文档受影响章节。

旧版 modules/infrastructure/maintenance/runbook 先备份，再迁入对应文档，保留人工原文与链接。AI 根据证据整理迁入的历史内容，消除重复和冲突，不能用骨架覆盖人工说明。

架构的 AI 工具链章节仍记录实际使用的 skills、MCP 和 agents；不能声称使用未运行的工具。

## 阶段 5：检查与交付

```bash
python /absolute/path/to/project-handoff/scripts/verify_handoff.py
```

检查实际文档集合、核心章节、TODO、密钥模式、本地文档链接、文件引用及事实覆盖。有错误则修复后复验。静态校验通过不等于业务测试全部完成；如实记录未执行项。通过后推进基线，直接交付 `ProjectDoc/`，不生成 ZIP。

## 平衡版文档

| 文件 | 职责 |
|---|---|
| readme.md | 项目概览、快速启动、速查卡、导航 |
| usage.md | 角色、实际业务流程、输入输出、权限和使用问题 |
| architecture.md | 系统架构、模块职责、目录、调用链、扩展点 |
| environment.md | 环境变量及配置说明 |
| deployment.md | 部署、CI/CD、域名、账号与托管资源 |
| operations.md | 日常维护、日志、实际适用的故障与回滚 |
| regression-test.md | 验证范围、状态、结果证据和缺口 |
| known-issues.md | 已知问题、未完成事项、技术债 |

`api.md`、`database.md`、`ai-services.md`、`desktop.md` 按实际需要独立；只改一个主题时不重写其他文档。

## 命名与配置

文档小写，多词连字符。保留 `SKILL.md`、Python 下划线脚本名和 `ProjectDoc/`。旧大写名称备份后迁移，大小写同名冲突停止并报告。

`.handoff.yml` 支持带注释的单行 skip_dirs/include_dirs 数组及正整数 max_files；无效配置报告位置。详见 `.handoff.yml.example`。

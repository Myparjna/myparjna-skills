# Project Handoff

依据项目源码、配置与扫描结果，创建、查看、比对、增量更新或重建 `ProjectDoc/` 交接文档的技能。执行规则以 SKILL.md 为准。

## 流程

1. `discover_project.py`：定位项目根目录与已有交接目录。
2. `analyze_project.py`：扫描项目，输出 `ProjectDoc/.handoff/analysis-report.json`。
3. `plan_handoff.py`、`compare_handoff.py`：生成文档计划与更新建议，写入 `TempScr/`。
4. `generate_handoff.py`：生成或补齐文档骨架，由 AI 依据证据填写。
5. `verify_handoff.py`：校验文档集合、章节、密钥模式与链接，通过后推进验收基线。

## 安全说明

- 模板环境文件中疑似密钥的默认值、MCP 配置中的 URL 查询参数与密钥参数、Git 远程地址中的用户信息均在写入报告前脱敏。
- 默认只扫描项目级配置；用户目录下的 MCP 配置与全局技能列表需显式传入 `--include-user-config` 才会读取。

## 测试

```bash
uv run --no-project --with pytest python -m pytest tests -q
```

## 版本

- v3.2.0（2026-09-29）：扫描报告迁入 `ProjectDoc/.handoff/`；增加密钥脱敏与用户级配置开关；修复非 UTF-8 配置、pyproject 解析失败导致中止、符号链接循环等问题；补充 evals 与脱敏测试。
- v3.1.2：平衡版 8 份基础文档加按需专题。

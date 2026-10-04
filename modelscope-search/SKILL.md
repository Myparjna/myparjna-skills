---
name: modelscope-search
description: "在 ModelScope（魔搭社区）搜索 AI 模型并查看详情，覆盖 OCR、NLP、CV、语音等方向，支持按下载量或收藏排序。用户提到魔搭、ModelScope、搜模型、找模型、模型对比或模型下载时使用。"
---

# ModelScope 模型搜索

## 前置条件

- Python 3.9+，依赖 `requests`（`uv pip install requests`）。
- 下载模型需另行安装 ModelScope SDK：`uv pip install modelscope`（要求 Python 3.10+）。

## 命令

```bash
python <skill_dir>/scripts/search_models.py "OCR"                      # 关键词搜索，默认按下载量排序
python <skill_dir>/scripts/search_models.py "OCR" --sort stars         # 按收藏排序
python <skill_dir>/scripts/search_models.py "Qwen" --limit 5 --page 2  # 数量 1..100，页码 >= 1
python <skill_dir>/scripts/search_models.py "OCR" --json               # JSON 输出
python <skill_dir>/scripts/search_models.py --model PaddlePaddle/PaddleOCR-VL  # 模型详情
```

## 输出字段

| 字段 | 说明 |
|------|------|
| `path` | `org/model-name`，可直接用于 `modelscope download --model` |
| `downloads` / `stars` | 下载量 / 收藏数 |
| `license` | 许可证 |
| `tags` / `tasks` | 标签 / 支持任务 |

## 工作流

1. 搜索：`python search_models.py "OCR" --limit 10`
2. 从结果中选定模型，例如 `deepseek-ai/DeepSeek-OCR`
3. 下载：`modelscope download --model 'deepseek-ai/DeepSeek-OCR' --local_dir ./models`

## 说明

- 搜索按模型名模糊匹配；排序仅在当前抓取页内进行，抓取量为 min(limit × 2, 100)，JSON 中的 `sort_scope`、`page`、`page_size`、`fetched` 字段标明范围。
- 请求失败时 stderr 输出 JSON 错误并退出 1；参数错误退出 2。
- 接口细节见 `references/api-notes.md`。

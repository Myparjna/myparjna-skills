---
name: modelscope-search
description: "用户提到 魔搭、ModelScope、搜模型、找模型、模型对比、模型下载 时必须使用本技能。在 ModelScope（魔搭社区）搜索 AI 模型，覆盖 OCR、NLP、CV、语音等方向，支持关键词搜索与按下载量、收藏排序。"
---

# ModelScope Model Search

Search and discover AI models on [ModelScope](https://modelscope.cn) — China's largest open-source model platform with 200K+ models.

## When to Use

- User asks to find models on ModelScope (e.g., "search OCR models on 魔搭")
- User wants to compare models for a specific task
- User needs model IDs for downloading via `modelscope download`
- User asks "what models are available for X on ModelScope"

## Prerequisites

- Python 3.9+（脚本使用 `list[dict]`；当前 PyPI ModelScope SDK 另要求 Python 3.10+）
- `requests` library (`uv pip install requests`)
- **仅搜索功能**：不需要安装 modelscope CLI，搜索脚本只依赖 `requests`
- **下载模型**（搜索后的下一步）：需要 `pip install modelscope`

## Commands

### Basic Search

```bash
python <skill_dir>/scripts/search_models.py "OCR"
```

### Sort by Downloads (default) or Stars

```bash
python <skill_dir>/scripts/search_models.py "OCR" --sort downloads
python <skill_dir>/scripts/search_models.py "OCR" --sort stars
```

### Limit Results

```bash
python <skill_dir>/scripts/search_models.py "Qwen" --limit 5
```

### JSON Output (for Agent parsing)

```bash
python <skill_dir>/scripts/search_models.py "OCR" --limit 10 --json
```

### Get Model Details

```bash
python <skill_dir>/scripts/search_models.py --model PaddlePaddle/PaddleOCR-VL
```

## Output Fields

| Field | Description |
|-------|-------------|
| `path` | `org/model-name` format, usable directly with `modelscope download --model` |
| `downloads` | Total download count |
| `stars` | Community stars |
| `license` | License type (MIT, Apache-2.0, etc.) |
| `tags` | Model tags (e.g., ocr, vision, nlp) |
| `tasks` | Supported tasks |

## Example Workflow

1. Search: `python search_models.py "OCR" --limit 10`
2. Pick a model from results (e.g., `deepseek-ai/DeepSeek-OCR`)
3. Download: `modelscope download --model 'deepseek-ai/DeepSeek-OCR' --local_dir ./models`

## Notes

- The search API uses an undocumented ModelScope endpoint discovered via SDK source analysis
- Results are sorted only within the fetched API page, NOT globally. Fetch size is min(limit × 2, 100); `--page` selects that API page. `--page >= 1`, `--limit 1..100`. JSON reports `sort_scope`, `page`, `page_size`, and `fetched`.
- Search calls the HTTP API directly through requests, not the SDK or CLI. Detail uses exact `GET /api/v1/models/{org}/{name}`, verified against official SDK v1.37.1 `HubApi.get_model(revision=None)`.
- Request failures emit a stable JSON error on stderr and exit 1; argparse errors exit 2.
- Search is fuzzy matching on model name
- See `references/api-notes.md` for API details

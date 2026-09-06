---
name: modelscope-search
description: "Search and discover AI models on ModelScope (魔搭社区). Use when the user wants to find, compare, or explore models for OCR, NLP, CV, audio, or other AI tasks on modelscope.cn. Supports keyword search, download/star sorting, and JSON output."
---

# ModelScope Model Search

Search and discover AI models on [ModelScope](https://modelscope.cn) — China's largest open-source model platform with 200K+ models.

## When to Use

- User asks to find models on ModelScope (e.g., "search OCR models on 魔搭")
- User wants to compare models for a specific task
- User needs model IDs for downloading via `modelscope download`
- User asks "what models are available for X on ModelScope"

## Prerequisites

- Python 3.6+
- `requests` library (`pip install requests`)
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
- Results are sorted locally (API does not support server-side sorting)
- Search is fuzzy matching on model name
- See `references/api-notes.md` for API details

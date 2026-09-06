# ModelScope Search API Notes

## Endpoint

```
PUT https://www.modelscope.cn/api/v1/models/
Content-Type: application/json
```

This endpoint is **undocumented** — discovered by reading the ModelScope Python SDK source (`modelscope.hub.api.HubApi.list_models`).

## Request Body

```json
{
  "Name": "OCR",
  "PageNumber": 1,
  "PageSize": 20
}
```

| Field | Type | Description |
|-------|------|-------------|
| `Name` | string | Fuzzy search on model name. Only parameter that filters results. |
| `Path` | string | Filter by org/owner (e.g., "Qwen"). Returns 0 if combined with Name. |
| `PageNumber` | int | Page number (1-based) |
| `PageSize` | int | Results per page (max ~100) |

**Important**: `Name` and `Path` are mutually exclusive for search purposes. Use `Name` for keyword search, `Path` for listing all models in an organization.

## Response

```json
{
  "Code": 200,
  "Data": {
    "TotalCount": 888,
    "Models": [...]
  },
  "Message": "success",
  "Success": true
}
```

## Key Model Fields

| Field | Type | Description |
|-------|------|-------------|
| `Path` | string | Organization name |
| `Name` | string | Model name |
| `ChineseName` | string | Chinese display name |
| `Downloads` | int | Total download count |
| `Stars` | int | Community stars |
| `License` | string | License identifier |
| `Tags` | list[string] | Model tags |
| `Tasks` | list[object] | Supported tasks (with TaskChineseName) |
| `Libraries` | list[string] | Framework support (pytorch, tensorflow, etc.) |
| `Language` | list[string] | Supported languages |
| `ModelType` | list[string] | Model architecture type |
| `StorageSize` | int | File size in bytes |

## Known Limitations

1. **No server-side sorting** — must sort locally after fetching
2. **Fuzzy search only** — no exact match, no boolean operators
3. **Name vs Path conflict** — cannot combine keyword search with org filter
4. **Pagination** — `TotalCount` reflects filtered count, but large offsets may be slow
5. **Rate limiting** — no documented rate limits, but excessive requests may be throttled

## SDK Reference

The official Python SDK (`pip install modelscope`) provides:
- `HubApi.list_models(owner_or_group)` — list by org (no search)
- `HubApi.get_model(model_id)` — get single model info
- `modelscope download --model 'org/name'` — CLI download

This skill fills the gap: **keyword search** which the SDK does not expose.

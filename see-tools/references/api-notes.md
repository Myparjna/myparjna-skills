# S.EE API Notes

Base URL:

```text
https://s.ee
```

Authentication:

- Send the API key in the `Authorization` header.

Useful endpoints:

- `POST /api/v1/shorten`
- `POST /api/v1/text`
- `POST /api/v1/file/upload`

Script behavior:

- Bash: connect timeout 10s; total timeout 60s for short URL/text, 300s for upload. HTTP 4xx/5xx keeps the response body and exits non-zero. JSON bodies are serialized with Python's standard `json` module (no jq or pip packages).
- PowerShell 7+: timeout 60s / 300s; HTTP errors terminate execution. JSON uses built-in `ConvertTo-Json`.

The official docs also provide SDKs for PHP, TypeScript, Go, Python, Java, Rust, and Zig, plus an official MCP server:

- SDK docs: https://s.ee/docs/zh-CN/developers/sdk/
- API overview: https://s.ee/docs/zh-CN/developers/api/
- MCP server: https://github.com/sdotee/cli-mcp-server

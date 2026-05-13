---
name: see-tools
description: "Manage S.EE short URLs, text sharing, and file uploads with SEE_API_KEY. Use when creating short links, sharing snippets, uploading files or images, checking S.EE API workflows, or preparing a future MCP-based integration around S.EE services."
---

# S.EE Tools

Use this skill for direct S.EE API workflows when a full MCP integration is not required.

## Prerequisites

Set `SEE_API_KEY` in the current shell or environment before running the scripts.

PowerShell:

```powershell
$env:SEE_API_KEY="your-api-key"
```

Bash:

```bash
export SEE_API_KEY="your-api-key"
```

## Available Scripts

- `scripts/create-short-url.ps1`
- `scripts/create-short-url.sh`
- `scripts/create-text-share.ps1`
- `scripts/create-text-share.sh`
- `scripts/upload-file.ps1`
- `scripts/upload-file.sh`

## Workflow

### Create a short URL

PowerShell:

```powershell
./scripts/create-short-url.ps1 -TargetUrl "https://example.com" -Domain "s.ee"
```

Bash:

```bash
./scripts/create-short-url.sh "https://example.com" "s.ee"
```

### Create a text share

PowerShell:

```powershell
./scripts/create-text-share.ps1 -Title "Deploy Notes" -Content "Release checklist" -TextType markdown
```

Bash:

```bash
./scripts/create-text-share.sh "Deploy Notes" "Release checklist" markdown
```

### Upload a file

PowerShell:

```powershell
./scripts/upload-file.ps1 -FilePath ".\\demo.png"
```

Bash:

```bash
./scripts/upload-file.sh "./demo.png"
```

## References

- Read `references/api-notes.md` for endpoint and header conventions.
- Prefer the official SDKs or MCP server for larger integrations.

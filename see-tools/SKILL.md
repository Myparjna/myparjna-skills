---
name: see-tools
description: "仅在用户明确指定或认可使用 S.EE 服务时调用，用于创建短网址、文本分享或上传文件。普通短链、图床或分享请求不自动调用。需 SEE_API_KEY。"
---

# S.EE Tools

## 调用范围与授权

仅在用户指定或认可 S.EE 后使用。目标网址、分享标题与正文、上传文件将发送到第三方 S.EE，返回的分享链接可能被他人访问。用户已明确授权将指定内容发送到 S.EE 时直接执行，无需重复确认；未授权时先说明第三方传输并征得同意。不得自行上传密钥或其他未授权内容。

## Prerequisites

- Bash：需要 `curl >= 7.76.0`；两个 JSON 脚本使用 `python` 命令（Python 3）的标准库 `json` 序列化，无需 pip 包或 jq。
- PowerShell：使用 `pwsh` 7+（不是 Windows PowerShell 5.1），JSON 使用内置 `ConvertTo-Json`。
- Bash 请求连接超时 10 秒，短链/文本总超时 60 秒，文件上传 300 秒；HTTP 4xx/5xx 保留响应正文并非零退出。PowerShell 对应超时 60/300 秒，HTTP 错误终止执行。脚本不自动重试发布操作。
- 仅在已授权的实际操作中运行以下示例；验证脚本应使用本地 mock，不发布测试内容。

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

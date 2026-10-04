---
name: see-tools
description: "仅在用户明确指定或认可使用 S.EE 服务时调用，用于创建短网址、文本分享或上传文件。普通短链、图床或分享请求不自动调用。需 SEE_API_KEY。"
---

# S.EE Tools

## 调用范围与授权

仅在用户指定或认可 S.EE 后使用。目标网址、分享内容与上传文件将发送到第三方 S.EE，返回的链接可被他人访问。用户已授权发送指定内容时直接执行；未授权时先说明第三方传输并征得同意。禁止自行上传密钥或其他未授权内容。

## 环境准备

运行前设置 `SEE_API_KEY`：

```powershell
$env:SEE_API_KEY="your-api-key"
```

```bash
export SEE_API_KEY="your-api-key"
```

Bash 脚本需要 `curl >= 7.76.0` 与 Python 3；PowerShell 脚本需要 `pwsh` 7+。超时与错误处理说明见 `references/api-notes.md`。

## 命令

| 操作 | PowerShell | Bash |
|------|-----------|------|
| 短网址 | `./scripts/create-short-url.ps1 -TargetUrl "https://example.com" -Domain "s.ee"` | `./scripts/create-short-url.sh "https://example.com" "s.ee"` |
| 文本分享 | `./scripts/create-text-share.ps1 -Title "Deploy Notes" -Content "Release checklist" -TextType markdown` | `./scripts/create-text-share.sh "Deploy Notes" "Release checklist" markdown` |
| 上传文件 | `./scripts/upload-file.ps1 -FilePath ".\demo.png"` | `./scripts/upload-file.sh "./demo.png"` |

脚本不自动重试发布操作。验证脚本时使用本地 mock，禁止发布测试内容。

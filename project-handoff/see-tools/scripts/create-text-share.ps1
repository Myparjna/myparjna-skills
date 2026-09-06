param(
    [Parameter(Mandatory = $true)][string]$Title,
    [Parameter(Mandatory = $true)][string]$Content,
    [ValidateSet("plain_text", "source_code", "markdown")][string]$TextType = "plain_text"
)

if (-not $env:SEE_API_KEY) {
    throw "SEE_API_KEY is not set."
}

$body = @{
    title = $Title
    content = $Content
    text_type = $TextType
}

Invoke-RestMethod `
    -Method Post `
    -Uri "https://s.ee/api/v1/text" `
    -Headers @{ Authorization = $env:SEE_API_KEY } `
    -ContentType "application/json" `
    -Body ($body | ConvertTo-Json -Depth 3)

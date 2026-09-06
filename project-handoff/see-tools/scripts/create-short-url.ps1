param(
    [Parameter(Mandatory = $true)][string]$TargetUrl,
    [string]$Domain = "s.ee",
    [string]$CustomSlug = ""
)

if (-not $env:SEE_API_KEY) {
    throw "SEE_API_KEY is not set."
}

$body = @{
    domain = $Domain
    target_url = $TargetUrl
}

if ($CustomSlug) {
    $body.custom_slug = $CustomSlug
}

Invoke-RestMethod `
    -Method Post `
    -Uri "https://s.ee/api/v1/shorten" `
    -Headers @{ Authorization = $env:SEE_API_KEY } `
    -ContentType "application/json" `
    -Body ($body | ConvertTo-Json)

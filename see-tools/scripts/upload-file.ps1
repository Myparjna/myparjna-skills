#Requires -Version 7.0
param(
    [Parameter(Mandatory = $true)][string]$FilePath
)

if (-not $env:SEE_API_KEY) {
    throw "SEE_API_KEY is not set."
}

if (-not (Test-Path -LiteralPath $FilePath -PathType Leaf)) {
    throw "File not found: $FilePath"
}

$file = Get-Item -LiteralPath $FilePath
$form = @{
    file = $file
}

Invoke-RestMethod `
    -Method Post `
    -TimeoutSec 300 `
    -ErrorAction Stop `
    -Uri "https://s.ee/api/v1/file/upload" `
    -Headers @{ Authorization = $env:SEE_API_KEY } `
    -Form $form

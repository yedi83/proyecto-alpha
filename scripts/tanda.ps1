# tanda.ps1 — commit y push de una tanda de trabajo en un solo comando.
# Uso:  .\scripts\tanda.ps1 "docs: mensaje del commit"
param(
    [Parameter(Mandatory = $true)][string]$Mensaje
)

$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo

git add -A

$staged = git diff --cached --name-only
if (-not $staged) {
    Write-Host "Nada que commitear: working tree limpio." -ForegroundColor Yellow
    exit 0
}

Write-Host "Archivos incluidos:" -ForegroundColor Cyan
$staged | ForEach-Object { Write-Host "  $_" }

git commit -m $Mensaje
if ($LASTEXITCODE -ne 0) { Write-Host "Commit fallo." -ForegroundColor Red; exit 1 }

git push
if ($LASTEXITCODE -ne 0) { Write-Host "Push fallo. El commit local existe; reintenta con 'git push'." -ForegroundColor Red; exit 1 }

Write-Host "Tanda subida. Ultimos commits:" -ForegroundColor Green
git log --oneline -3

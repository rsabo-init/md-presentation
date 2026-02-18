# PowerShell script to sync presentation.md content into presentation.html
# Run this after editing presentation.md to update the HTML file

$mdFile = "presentation.md"
$htmlFile = "presentation.html"

if (-not (Test-Path $mdFile)) {
    Write-Host "Error: presentation.md not found!" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $htmlFile)) {
    Write-Host "Error: presentation.html not found!" -ForegroundColor Red
    exit 1
}

Write-Host "Reading presentation.md..." -ForegroundColor Cyan
$markdownContent = Get-Content $mdFile -Raw -Encoding UTF8

# Escape backticks and dollar signs for JavaScript
$escapedContent = $markdownContent -replace '`', '\`' -replace '\$', '\$'

Write-Host "Reading presentation.html..." -ForegroundColor Cyan
$htmlContent = Get-Content $htmlFile -Raw -Encoding UTF8

# Find and replace the MARKDOWN_CONTENT constant
$pattern = '(?s)(const MARKDOWN_CONTENT = `).*?(`;\s*$)'
$replacement = "`${1}$escapedContent`${2}"

if ($htmlContent -match $pattern) {
    Write-Host "Updating embedded content..." -ForegroundColor Cyan
    $updatedHtml = $htmlContent -replace $pattern, $replacement
    
    Set-Content -Path $htmlFile -Value $updatedHtml -Encoding UTF8 -NoNewline
    Write-Host "✓ Presentation synced successfully!" -ForegroundColor Green
    Write-Host "You can now open presentation.html in your browser." -ForegroundColor Yellow
} else {
    Write-Host "Error: Could not find MARKDOWN_CONTENT in HTML file!" -ForegroundColor Red
    exit 1
}

# SCADA Presentation Server Launcher
# Starts a local Python HTTP server for the presentation

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "  SCADA Presentation Server" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to script directory
Set-Location $PSScriptRoot

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python." -ForegroundColor Red
    Write-Host "  Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host ""
Write-Host "Starting server..." -ForegroundColor Yellow
Write-Host "Server URL: http://localhost:8000" -ForegroundColor Green
Write-Host "Presentation: http://localhost:8000/presentation.html" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Start the server
try {
    # Open browser automatically
    Start-Sleep -Seconds 1
    Start-Process "http://localhost:8000/presentation.html"
    
    # Start Python server
    python -m http.server 8000
} catch {
    Write-Host "Error starting server: $_" -ForegroundColor Red
    pause
}

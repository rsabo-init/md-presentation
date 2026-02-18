@echo off
echo Starting SCADA Presentation Server...
echo.
echo Server will be available at: http://localhost:8000
echo Press Ctrl+C to stop the server
echo.
cd /d "%~dp0"
python -m http.server 8000

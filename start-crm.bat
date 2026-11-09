@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  echo Python 3 is required to run the CRM server.
  echo Install Python from https://www.python.org/downloads/ and try again.
  pause
  exit /b 1
)
start "Community CRM server" /min py -3 server.py
timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:8765
endlocal

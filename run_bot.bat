@echo off

echo Waiting for internet...

:internet
ping www.google.com -n 1 >nul
if errorlevel 1 (
    timeout /t 5 /nobreak >nul
    goto internet
)

:restart
echo Starting PDF Viewer Bot...

cd /d "%~dp0"

python bot.py

echo.
echo Bot stopped. Restarting in 30 seconds...
timeout /t 30 /nobreak >nul
goto restart
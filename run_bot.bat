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
cd /d D:\Downloads\pdf_viewer_bot

python bot.py

echo.
echo Bot stopped. Restarting in 30 seconds...
timeout /t 30 /nobreak >nul
goto restart
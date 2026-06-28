@echo off
title PDF Viewer Bot

echo ==========================================
echo        PDF Viewer Bot
echo         Created by Dipson
echo ==========================================
echo.

echo Waiting for internet connection...

:internet
ping www.google.com -n 1 >nul
if errorlevel 1 (
    timeout /t 5 /nobreak >nul
    goto internet
)

cd /d "%~dp0"

start "" pythonw.exe bot.py

exit
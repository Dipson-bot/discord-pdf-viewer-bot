@echo off
title Discord PDF Viewer Bot

echo ======================================
echo Discord PDF Viewer Bot
echo Created by Dipson
echo ======================================
echo.

echo Waiting for internet connection...

:internet
ping www.google.com -n 1 >nul
if errorlevel 1 (
    timeout /t 5 /nobreak >nul
    goto internet
)

echo Internet detected.
echo.

:restart
cd /d "%~dp0"

echo Starting PDF Viewer Bot...
python bot.py

echo.
echo Bot stopped or crashed.
echo Restarting in 30 seconds...
timeout /t 30 /nobreak >nul
goto restart
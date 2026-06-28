@echo off
title PDF Viewer Bot Startup Installer

echo ==========================================
echo      PDF Viewer Bot Installer
echo         Created by Dipson
echo ==========================================
echo.

:: Check if Python is installed
where pythonw >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python was not found.
    echo.
    echo Please install Python and make sure
    echo "Add Python to PATH" was enabled.
    echo.
    pause
    exit /b
)

:: Get the folder where this installer is located
set "BOT_DIR=%~dp0"
set "BATFILE=%BOT_DIR%run_bot.bat"

:: Check if startup task already exists
schtasks /Query /TN "PDF Viewer Bot" >nul 2>nul

if %errorlevel%==0 (
    echo Existing startup task detected.
    echo Updating it to the current folder...
    echo.
) else (
    echo No existing startup task found.
    echo Creating a new one...
    echo.
)

:: Create or update the scheduled task
schtasks /Create ^
 /TN "PDF Viewer Bot" ^
 /SC ONLOGON ^
 /RL LIMITED ^
 /F ^
 /TR "\"%BATFILE%\""

if errorlevel 1 (
    echo.
    echo ==========================================
    echo Installation Failed
    echo ==========================================
    echo.
    echo Windows could not create the startup task.
    echo.
    pause
    exit /b
)

echo.
echo ==========================================
echo Installation Successful!
echo ==========================================
echo.
echo Startup has been enabled.
echo.
echo The bot will automatically start whenever
echo you log into Windows.
echo.
echo Current installation:
echo %BOT_DIR%
echo.
echo If you move this folder later,
echo simply run:
echo.
echo   uninstall_startup.bat
echo   install_startup.bat
echo.
echo to update the startup task.
echo.
pause
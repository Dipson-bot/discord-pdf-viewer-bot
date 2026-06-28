@echo off
title Remove PDF Viewer Startup

echo ==========================================
echo Removing startup task...
echo ==========================================
echo.

schtasks /Delete /TN "PDF Viewer Bot" /F

echo.
echo Startup task removed successfully.
echo.
pause
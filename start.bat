@echo off
echo ============================================
echo   Land Visualizer Pro - Starting...
echo ============================================
echo.
echo [1/2] Starting Flask Backend on port 5000...
start "Land Visualizer Backend" cmd /k "cd /d "%~dp0backend" && python app.py"
timeout /t 2 /nobreak >nul
echo [2/2] Opening Frontend in browser...
start "" "%~dp0frontend\index.html"
echo.
echo ============================================
echo  Backend : http://localhost:5000
echo  Frontend: Opens in your default browser
echo ============================================
echo.
echo Press any key to stop the backend server...
pause >nul
taskkill /FI "WINDOWTITLE eq Land Visualizer Backend" /F >nul 2>&1

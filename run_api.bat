@echo off
echo ========================================
echo Face Recognition API Launcher
echo ========================================
echo.

REM Check if conda is available
where conda >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Conda is not in PATH
    echo Please activate conda first or add it to PATH
    pause
    exit /b 1
)

echo Activating conda environment: face-checkin
call conda activate face-checkin
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to activate conda environment
    echo Please check if environment 'face-checkin' exists
    pause
    exit /b 1
)

echo.
echo Checking Python...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found in conda environment
    pause
    exit /b 1
)

echo.
echo ========================================
echo Starting Face Recognition API...
echo ========================================
echo API will run at http://localhost:8000
echo Press Ctrl+C to stop
echo ========================================
echo.

python api.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ========================================
    echo ERROR: API failed to start
    echo ========================================
    echo Please check the error messages above
    pause
)

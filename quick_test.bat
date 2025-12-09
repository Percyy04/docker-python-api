@echo off
echo Quick Test - Checking API setup...
echo.

call conda activate face-checkin
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Cannot activate conda environment
    pause
    exit /b 1
)

echo Running test script...
python test_api.py

echo.
echo If all tests passed, you can run: python api.py
pause

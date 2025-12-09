@echo off
echo ========================================
echo Installing Dependencies
echo ========================================
echo.

call conda activate face-checkin
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Cannot activate conda environment 'face-checkin'
    echo Please create the environment first
    pause
    exit /b 1
)

echo Installing from requirements.txt...
pip install -r requirements.txt

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo You can now run:
echo   python test_api.py  (to test setup)
echo   python api.py        (to start API)
echo.
pause

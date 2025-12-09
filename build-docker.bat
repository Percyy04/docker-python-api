@echo off
REM Build Docker image for Face Check-in API
echo Building Docker image: gala-face-checkin...

docker build -t gala-face-checkin:latest .

if %errorlevel% equ 0 (
    echo.
    echo Build successful!
    echo.
    echo To run the container:
    echo   docker run -d -p 8000:8000 --name gala-face-checkin gala-face-checkin:latest
    echo.
    echo Or use docker-compose:
    echo   docker-compose up -d
) else (
    echo.
    echo Build failed!
    exit /b 1
)



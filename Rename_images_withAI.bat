@echo off
echo AI Image Recognition and Naming Tool
echo ====================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in your PATH.
    echo Please install Python 3.7 or higher from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

:: Check if required packages are installed
echo Checking required packages...
python -c "import transformers, torch, PIL" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required packages...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install required packages.
        pause
        exit /b 1
    )
)

echo.
echo This tool will:
echo 1. Use AI to analyze your images
echo 2. Create a "Renamed with AI" subfolder
echo 3. Save copies of your images with descriptive names based on their content
echo.
echo Your original files will remain untouched.
echo.

set /p choice="Do you want to continue? (Y/N): "
if /i "%choice%" neq "Y" (
    echo Operation cancelled.
    pause
    exit /b 0
)

echo.
echo Running AI image recognition...
echo.

:: Run the Python script
python Rename_images_withAI.py

echo.
echo Process completed.
echo.
pause 
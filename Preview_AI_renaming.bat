@echo off
echo AI Image Recognition and Naming Tool - PREVIEW MODE
echo =================================================
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
echo PREVIEW MODE: This will show you what the tool would do without making any changes.
echo.
echo The tool would:
echo 1. Use AI to analyze your images
echo 2. Create a "Renamed with AI" subfolder
echo 3. Save copies of your images with descriptive names based on their content
echo.
echo Press any key to start the preview...
pause >nul

echo.
echo Running AI image recognition in preview mode...
echo.

:: Run the Python script in dry-run mode
python Rename_images_withAI.py --dry-run

echo.
echo Preview completed. To actually process your files, run Rename_images_withAI.bat
echo.
pause 
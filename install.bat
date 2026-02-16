@echo off
REM Installation script for Windows

echo Installing Akula Python CLI...
echo.

REM Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python 3.7 or higher from https://python.org
    pause
    exit /b 1
)

REM Display Python version
echo Python version check:
python --version
echo.

REM Install the package
echo Installing package...
if exist requirements.txt (
    python -m pip install -r requirements.txt
)

python -m pip install -e .

REM Verify installation
echo.
echo Verifying installation...
where akula >nul 2>&1
if %errorlevel% equ 0 (
    echo Installation successful!
    echo.
    echo Run 'akula --help' to get started
    akula --version
) else (
    echo Warning: 'akula' command not found in PATH
    echo Try running: python -m akula_cli.cli --help
)

echo.
pause

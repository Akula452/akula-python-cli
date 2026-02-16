@echo off
REM Example usage script for Akula CLI on Windows

echo === Akula CLI Example Usage ===
echo.

echo 1. Display help:
akula --help
echo.

echo 2. Show version:
akula --version
echo.

echo 3. Say hello (default):
akula hello
echo.

echo 4. Say hello to a specific person:
akula hello --name "Windows User"
echo.

echo 5. Display system information:
akula sysinfo
echo.

echo 6. Echo a message:
akula echo "Hello from Windows!"
echo.

echo 7. Show version with details:
akula version
echo.

echo === All examples completed ===
pause

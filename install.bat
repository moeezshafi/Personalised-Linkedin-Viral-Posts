@echo off
echo ========================================
echo MSZ - LinkedIn Content Generator
echo Installation Script
echo ========================================
echo.

echo [1/3] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install Python packages
    pause
    exit /b 1
)
echo.

echo [2/3] Installing Playwright browser...
playwright install chromium
if errorlevel 1 (
    echo ERROR: Failed to install Playwright
    pause
    exit /b 1
)
echo.

echo [3/3] Creating database...
python -c "from database import engine, Base; Base.metadata.create_all(bind=engine); print('Database created successfully')"
echo.

echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo To start the application:
echo   - Web Interface: python main.py
echo   - CLI Interface: python cli.py
echo.
echo Then open: http://localhost:8000
echo.
pause

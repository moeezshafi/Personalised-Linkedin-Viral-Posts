@echo off
echo ========================================
echo MSZ - Push to GitHub
echo ========================================
echo.

echo Step 1: Initializing Git...
git init

echo.
echo Step 2: Adding all files...
git add .

echo.
echo Step 3: Creating commit...
git commit -m "Initial commit: MSZ LinkedIn Content Generator"

echo.
echo ========================================
echo IMPORTANT: Replace YOUR_USERNAME below!
echo ========================================
echo.
set /p username="Enter your GitHub username: "

echo.
echo Step 4: Connecting to GitHub...
git remote add origin https://github.com/%username%/msz-content-generator.git

echo.
echo Step 5: Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo ========================================
echo Done! Check your GitHub repo!
echo ========================================
pause

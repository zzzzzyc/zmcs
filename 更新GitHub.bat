@echo off
chcp 65001 >nul
echo ========================================
echo   更新 GitHub 仓库
echo ========================================
echo.

git add .
git commit -m "Update: %date% %time%"
git push

echo.
echo ========================================
echo   更新完成！
echo ========================================
pause


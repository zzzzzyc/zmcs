@echo off
chcp 65001 >nul
echo ========================================
echo   上传到 GitHub 仓库
echo ========================================
echo.
echo 仓库地址: https://github.com/zzzzzyc/zmcs/
echo.
echo 执行步骤：
echo   1. 初始化 Git 仓库
echo   2. 添加所有文件
echo   3. 提交到本地
echo   4. 推送到 GitHub
echo.
echo 按任意键开始，Ctrl+C 取消...
pause >nul
echo.

REM 初始化 Git
echo [1/4] 初始化 Git 仓库...
git init
echo.

REM 添加远程仓库
echo [2/4] 添加远程仓库...
git remote add origin https://github.com/zzzzzyc/zmcs.git
echo.

REM 添加所有文件
echo [3/4] 添加文件...
git add .
git commit -m "Initial commit: Minecraft Market Analyzer with full data"
echo.

REM 推送到 GitHub
echo [4/4] 推送到 GitHub...
git branch -M main
git push -u origin main --force
echo.

echo ========================================
echo   上传完成！
echo ========================================
echo.
echo 访问: https://github.com/zzzzzyc/zmcs/
echo.
pause

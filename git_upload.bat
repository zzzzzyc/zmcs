@echo off
chcp 65001 >nul
echo ========================================
echo   准备上传到 GitHub
echo ========================================
echo.
echo 目标仓库: https://github.com/zzzzzyc/zmcs/
echo.
echo 选择上传方式:
echo   1 - 上传完整数据 (data.json 包含 3285 条记录)
echo   2 - 只上传示例数据 (data.sample.json 10条示例) [推荐]
echo   3 - 取消
echo.
set /p choice="请选择 (1/2/3): "

if "%choice%"=="1" goto full_data
if "%choice%"=="2" goto sample_data
if "%choice%"=="3" goto cancel

:full_data
echo.
echo [选择] 上传完整数据
echo.
echo 提示: data.json 文件约 1.5 MB，包含 3285 条真实交易数据
echo       确定要公开这些数据吗？
echo.
set /p confirm="确认上传？(y/n): "
if /i not "%confirm%"=="y" goto cancel

rem 不排除 data.json
type nul > .gitignore.temp
goto upload

:sample_data
echo.
echo [选择] 只上传示例数据
echo.
echo 将使用 data.sample.json 作为演示
echo 用户可以自己生成 data.json
echo.

rem 确保排除 data.json
if not exist .gitignore (
    echo data.json > .gitignore
    echo data*.json >> .gitignore
)

rem 复制示例数据
copy /Y data.sample.json data.json.example
echo.
echo [OK] 已创建 data.json.example (示例文件)
goto upload

:upload
echo.
echo ========================================
echo   开始上传...
echo ========================================
echo.

rem 初始化 Git (如果还没有)
if not exist .git (
    echo [1/6] 初始化 Git 仓库...
    git init
    echo.
)

rem 设置远程仓库
echo [2/6] 设置远程仓库...
git remote remove origin 2>nul
git remote add origin https://github.com/zzzzzyc/zmcs.git
echo.

rem 添加文件
echo [3/6] 添加文件...
git add .
echo.

rem 查看将要提交的文件
echo [4/6] 将要提交的文件:
git status --short
echo.
pause

rem 提交
echo [5/6] 提交更改...
git commit -m "Add Minecraft Market Analyzer - Full project upload"
echo.

rem 推送
echo [6/6] 推送到 GitHub...
git branch -M main
git push -u origin main --force
echo.

echo ========================================
echo   上传完成！
echo ========================================
echo.
echo 访问: https://github.com/zzzzzyc/zmcs/
echo.
goto end

:cancel
echo.
echo 已取消上传
echo.

:end
pause


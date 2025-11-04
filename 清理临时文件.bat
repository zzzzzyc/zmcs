@echo off
chcp 65001 >nul
echo ========================================
echo   清理临时文件和大数据文件
echo ========================================
echo.
echo 将删除以下文件：
echo   - data.json (保留 data.sample.json)
echo   - data*.json 临时文件
echo   - JSON.json 原始文件
echo   - signfinder_export_*.json
echo   - output.csv
echo.
echo 按任意键继续，Ctrl+C 取消...
pause >nul

del /Q data.json 2>nul
del /Q data1.json 2>nul
del /Q data2.json 2>nul
del /Q data3.json 2>nul
del /Q JSON.json 2>nul
del /Q signfinder_export_*.json 2>nul
del /Q output.csv 2>nul
rmdir /S /Q __pycache__ 2>nul

echo.
echo ========================================
echo   清理完成！
echo ========================================
echo.
echo 提示：
echo   - data.sample.json 已保留（用于GitHub演示）
echo   - 工具脚本已保留
echo   - 网页文件已保留
echo.
pause


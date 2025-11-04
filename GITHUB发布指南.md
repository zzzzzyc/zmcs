# 🚀 GitHub 发布指南

## 📦 需要上传的文件

### ✅ 必须上传：
```
index.html          # 主页面
style.css           # 样式
app.js              # 逻辑
json_to_data.py     # 转换工具
merge_data.py       # 合并工具
LICENSE             # 许可证
.gitignore          # Git忽略规则
README.md           # 中文说明（原有）
README_EN.md        # 英文说明（新建）
```

### ❌ 不要上传：
```
data.json           # 数据文件太大
data*.json          # 临时数据
JSON.json           # 原始扫描数据
signfinder_export_*.json  # 扫描文件
output.csv          # CSV文件
*.pyc               # Python缓存
__pycache__/        # 缓存目录
```

`.gitignore` 已经帮你排除这些了！

---

## 🎯 发布步骤

### 1. 初始化 Git 仓库

```bash
cd C:\Users\zzzzz\Desktop\findjiage

# 初始化仓库
git init

# 添加所有文件（.gitignore会自动排除不需要的）
git add .

# 第一次提交
git commit -m "Initial commit: Minecraft Market Analyzer"
```

### 2. 在 GitHub 创建仓库

1. 访问 https://github.com/new
2. 仓库名建议：`minecraft-market-analyzer`
3. 描述：`A powerful web tool for Minecraft marketplace data analysis`
4. 设为 Public（公开）
5. 不要勾选"Initialize with README"（我们已经有了）
6. 点击"Create repository"

### 3. 推送到 GitHub

```bash
# 添加远程仓库（替换成你的用户名）
git remote add origin https://github.com/zzzzzyc/minecraft-market-analyzer.git

# 推送代码
git branch -M main
git push -u origin main
```

### 4. 完善 GitHub 页面

在仓库页面设置：

1. **About** 区域：
   - Description: `⛏️ Minecraft marketplace data analyzer - Real-time search, price comparison, data visualization`
   - Website: 你的网站地址
   - Topics（标签）: `minecraft`, `marketplace`, `data-analysis`, `javascript`, `python`, `web-app`

2. **README**：
   - 自动显示 README.md（中文版）
   - 可以在顶部加个语言切换链接

---

## 📄 README 优化建议

在 `README.md` 顶部添加：

```markdown
# ⛏️ Minecraft 交易市场分析工具

[English](README_EN.md) | 简体中文

[![License](https://img.shields.io/badge/license-WTFPL-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/zzzzzyc/minecraft-market-analyzer.svg)](https://github.com/zzzzzyc/minecraft-market-analyzer/stargazers)

![Demo Screenshot](screenshot.png)
```

---

## 📸 添加截图（可选）

1. 打开你的网站
2. 截图主要功能：
   - 市场交易表格
   - 数据分析图表
   - 价格对比
3. 保存为 `screenshot.png`
4. 添加到仓库：
   ```bash
   git add screenshot.png
   git commit -m "Add demo screenshot"
   git push
   ```

---

## 🌟 启用 GitHub Pages（可选）

如果想用 GitHub 免费托管网站：

1. 进入仓库 Settings
2. 找到"Pages"
3. Source 选择 `main` 分支
4. 点击 Save
5. 访问：`https://zzzzzyc.github.io/minecraft-market-analyzer/`

**注意**：需要创建一个小的示例 `data.json` 用于演示（别用真实的大文件）

---

## 🔄 后续更新

当你修改代码后：

```bash
# 查看改动
git status

# 添加改动
git add .

# 提交
git commit -m "你的更新说明"

# 推送
git push
```

---

## 💡 项目亮点（写在 GitHub）

强调这些特色：

- ✅ **纯静态**：无需后端，上传即用
- ✅ **智能合并**：多次扫描自动去重
- ✅ **移动友好**：响应式设计
- ✅ **数据可视化**：Chart.js 图表
- ✅ **位置显示**：直接看坐标传送
- ✅ **开源免费**：WTFPL 许可证

---

## 🎨 Badges（徽章）

可以添加这些徽章到 README：

```markdown
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
```

---

## 📝 填写 Topics（标签）

建议添加：
- `minecraft`
- `marketplace`  
- `data-analysis`
- `web-application`
- `javascript`
- `python`
- `static-site`
- `data-visualization`
- `chart-js`
- `datatables`

---

**准备好了就开始发布吧！** 🚀


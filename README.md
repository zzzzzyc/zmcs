# 🎮 Minecraft 交易市场分析工具 (ZMCS)

**Z Market Comprehensive Statistics**

[English](README_EN.md) | 简体中文

[![License](https://img.shields.io/badge/license-WTFPL-blue.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-zzzzzyc%2Fzmcs-181717?logo=github)](https://github.com/zzzzzyc/zmcs)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

一个功能强大的纯静态网页应用，用于分析和展示 Minecraft 服务器的交易数据。

## ✨ 主要特性

### 🛒 市场交易
- **智能搜索**: 实时搜索玩家名、物品名
- **高级筛选**: 按价格区间、数量范围筛选
- **数据排序**: 支持多列排序（价格、数量等）
- **分页显示**: 每页25条记录，流畅浏览

### 📈 数据分析
- **热门物品 TOP 10**: 查看最受欢迎的交易物品
- **活跃卖家 TOP 10**: 最勤劳的卖家排行
- **最贵物品排行**: 土豪物品一览
- **价格分布图**: 直观了解市场价格区间分布
- **详细排行榜**: 大卖家和高价物品的完整排名

### 🔍 价格对比
- **多卖家对比**: 输入物品名，一键查看所有卖家价格
- **最低价标识**: 自动高亮显示最优惠价格
- **位置显示**: 显示商店的 Minecraft 坐标（x, y, z）
- **模糊搜索**: 支持部分匹配搜索

### 💎 其他亮点
- ✅ 纯前端实现，无需服务器运行环境
- ✅ 响应式设计，支持手机和平板访问
- ✅ 现代化 UI 设计，紫色渐变背景
- ✅ 流畅的动画效果
- ✅ 数据可视化图表

## 📦 文件结构

```
zmcs/
│
├── 网页文件 (上传到服务器)
│   ├── index.html          # 主页面
│   ├── style.css           # 样式表
│   ├── app.js              # JavaScript 逻辑
│   └── data.json           # 数据文件
│
├── 工具脚本 (本地使用)
│   ├── json_to_data.py     # JSON 转换工具
│   ├── merge_data.py       # 多文件合并工具
│   ├── csv_to_json.py      # CSV 转换工具（旧版）
│   └── main.py             # 命令行显示工具
│
├── 文档
│   ├── README.md           # 中文说明
│   ├── README_EN.md        # 英文说明
│   ├── LICENSE             # WTFPL 许可证
│   └── GITHUB发布指南.md   # 发布教程
│
└── 示例数据
    └── data.sample.json    # 示例数据文件

```

## 🚀 使用方法

### 方式一：直接使用（推荐）

1. 确保所有文件都在同一目录下
2. 直接用浏览器打开 `index.html`
3. 开始探索数据！

### 方式二：托管到静态服务器

上传以下文件到你的虚拟主机：
- `index.html`
- `style.css`
- `app.js`
- `data.json`

就这么简单！不需要 PHP、Python 或任何后端环境。

## 🔄 更新数据

当你有新的交易数据时：

### 方式 1：从原始 JSON 更新（推荐，包含位置信息）
1. 替换 `JSON.json` 文件
2. 运行转换脚本：
   ```bash
   python json_to_data.py
   ```
3. 新的 `data.json` 会自动生成（包含坐标位置）
4. 刷新网页即可看到最新数据

### 方式 2：从 CSV 更新（不含位置信息）
1. 替换 `output.csv` 文件
2. 运行转换脚本：
   ```bash
   python csv_to_json.py
   ```
3. 新的 `data.json` 会自动生成（不包含位置）
4. 刷新网页即可看到最新数据

## 📊 数据统计

当前数据概览：
- **总交易数**: 1,356 条
- **独立玩家**: 208 人
- **物品种类**: 521 种
- **价格范围**: $0.10 ~ $23,333,333,333,333,332,000

## 🛠️ 技术栈

- **HTML5** - 页面结构
- **CSS3** - 现代化样式（渐变、动画、毛玻璃效果）
- **Vanilla JavaScript** - 纯 JS 逻辑
- **jQuery** - DOM 操作
- **DataTables.js** - 强大的表格功能
- **Chart.js** - 数据可视化图表

## 🎨 特色设计

- 紫色渐变背景（#667eea → #764ba2）
- 毛玻璃效果（backdrop-filter blur）
- 平滑动画过渡
- 响应式网格布局
- 卡片式设计
- 悬停效果增强交互体验

## 💡 使用提示

1. **市场交易页**: 
   - 使用顶部搜索框快速查找
   - 点击列标题进行排序
   - 使用高级筛选精确定位
   - 位置列显示商店坐标（可复制到游戏中传送）

2. **数据分析页**: 
   - 查看图表了解市场趋势
   - 滚动查看完整排行榜

3. **价格对比页**: 
   - 输入物品名（至少2个字）
   - 系统会列出所有匹配物品
   - 最低价自动高亮显示（绿色背景 + 💎标记）
   - 显示每个商店的坐标位置

## 🌟 与竞品的区别

相比于简单的静态表格，本工具提供：
- ✅ 实时搜索和筛选
- ✅ 数据可视化分析
- ✅ 价格智能对比
- ✅ 美观的现代化界面
- ✅ 移动端友好
- ✅ 丰富的统计信息

## 📝 开发者信息

- **开发语言**: Python (数据处理) + JavaScript (前端)
- **兼容性**: Chrome, Firefox, Safari, Edge (现代浏览器)
- **响应式**: 支持桌面、平板、手机

## 🔮 未来计划

- [ ] 添加数据导出功能（CSV/Excel）
- [ ] 价格走势图（如果有时间戳）
- [ ] 收藏夹功能
- [ ] 暗黑/明亮主题切换
- [ ] 更多数据可视化图表

## 📧 联系方式

- **Email**: zzzzzyc@hotmail.com
- **GitHub**: [@zzzzzyc](https://github.com/zzzzzyc)
- **项目地址**: https://github.com/zzzzzyc/zmcs

## 🤝 贡献

欢迎提交 Issues 和 Pull Requests！

## 📄 许可证

本项目采用 [WTFPL](LICENSE) 许可证 - 做你想做的事！

## ⭐ 支持项目

如果这个项目对你有帮助，请给个 Star ⭐！

---

**Made with ❤️ | 让数据分析变得简单而美观**

**ZMCS** - Z Market Comprehensive Statistics


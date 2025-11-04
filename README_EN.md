# ⛏️ Minecraft Market Analyzer (ZMCS)

**Z Market Comprehensive Statistics**

English | [简体中文](README.md)

[![License](https://img.shields.io/badge/license-WTFPL-blue.svg)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

A powerful static web application for analyzing Minecraft server marketplace data.

## ✨ Features

### 🛒 Market Trading
- Real-time search by player/item name
- Advanced filtering (price range, quantity)
- Multi-column sorting
- Pagination display
- Location coordinates for each shop

### 📈 Data Analysis
- Top 10 popular items
- Top 10 active sellers  
- Most expensive items ranking
- Price distribution charts
- Detailed leaderboards

### 🔍 Price Comparison
- Multi-seller comparison
- Automatic lowest price highlighting
- Coordinates display for easy teleporting
- Fuzzy search support

### 💎 Highlights
- ✅ Pure frontend (no backend required)
- ✅ Responsive design (mobile-friendly)
- ✅ Modern UI with gradient backgrounds
- ✅ Data visualization with charts
- ✅ Multi-scan data merging with deduplication

## 🚀 Quick Start

### Deploy to Static Hosting

Upload these 4 files to your web server:
```
index.html
style.css
app.js
data.json
```

No PHP, Python, or backend environment needed!

### Local Testing

```bash
python -m http.server 8000
```

Visit: http://localhost:8000

## 🔄 Data Processing

### Single Scan

```bash
python json_to_data.py your_scan.json data.json
```

### Multiple Scans (Merge & Deduplicate)

```bash
# Convert each scan
python json_to_data.py scan1.json data1.json
python json_to_data.py scan2.json data2.json
python json_to_data.py scan3.json data3.json

# Merge all
python merge_data.py
```

Deduplication key: position (x,y,z) + player + item

## 📦 File Structure

```
Web Files (upload to server):
├── index.html      # Main page
├── style.css       # Styles
├── app.js          # JavaScript logic
└── data.json       # Data file

Tools (local use):
├── json_to_data.py # Convert scanner output
├── merge_data.py   # Merge multiple scans
└── LICENSE         # WTFPL license
```

## 🛠️ Tech Stack

- HTML5 / CSS3 / Vanilla JavaScript
- jQuery + DataTables.js (table features)
- Chart.js (data visualization)
- Pure frontend, zero dependencies on backend

## 📊 Data Format

```json
{
  "license": "WTFPL",
  "exportTime": "2025-11-04 19:41:33",
  "totalRecords": 3285,
  "data": [
    {
      "player": "PlayerName",
      "quantity": 10,
      "item": "Diamond",
      "price": 100.0,
      "priceFormatted": "$100",
      "position": { "x": 100, "y": 64, "z": 200 }
    }
  ]
}
```

## 💡 Tips

1. **Version Control**: Change version numbers in index.html when updating
   ```html
   <script src="app.js?v=2.1"></script>
   ```

2. **CDN Cache**: Clear Cloudflare cache after updates

3. **Price Filter**: Items >= $9,000,000 are filtered as "vault prices"

## 📝 License

WTFPL - Do What The Fuck You Want To Public License

Free to use, modify, and distribute!

## 🤝 Contributing

Issues and PRs welcome!

## 📧 Contact

- **Email**: zzzzzyc@hotmail.com
- **GitHub**: [@zzzzzyc](https://github.com/zzzzzyc)
- **Project**: https://github.com/zzzzzyc/zmcs

## ⭐ Support

If this project helps you, please give it a Star ⭐!

---

**Made with ❤️ for Minecraft community**

**ZMCS** - Z Market Comprehensive Statistics


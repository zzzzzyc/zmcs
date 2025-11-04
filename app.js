let allData = [];
let marketTable;

document.addEventListener('DOMContentLoaded', function() {
    loadData();
});

// Load and parse data
async function loadData() {
    try {
        const response = await fetch('data.json');
        const jsonData = await response.json();
        
        // 兼容新旧格式
        let rawData, exportTime;
        if (jsonData.data && Array.isArray(jsonData.data)) {
            // 新格式：包含元数据
            rawData = jsonData.data;
            exportTime = jsonData.exportTime || '';
        } else if (Array.isArray(jsonData)) {
            // 旧格式：直接是数组
            rawData = jsonData;
            exportTime = new Date().toLocaleString('zh-CN');
        }
        
        // 过滤掉价格超过900万的"保险柜"商品
        const MAX_REASONABLE_PRICE = 666666; // 900万
        allData = rawData.filter(item => item.price < MAX_REASONABLE_PRICE);
        
        const filteredCount = rawData.length - allData.length;
        if (filteredCount > 0) {
            console.log(`🔒 已过滤 ${filteredCount} 个保险柜价格（>= $${MAX_REASONABLE_PRICE.toLocaleString()}）`);
            // 显示过滤提示
            document.getElementById('filterNotice').style.display = 'block';
            document.getElementById('filteredCount').textContent = filteredCount;
        }
        
        initializeApp();
        updateStatistics();
        initializeMarketTable();
        initializeCharts();
        
        // 设置真实的数据导出时间
        document.getElementById('updateTime').textContent = exportTime;
    } catch (error) {
        console.error('数据加载失败:', error);
        alert('数据加载失败，请确保 data.json 文件存在！');
    }
}

function initializeApp() {
    console.log(`Data loaded: ${allData.length} records`);
}

// Update statistics cards
function updateStatistics() {
    const totalTrades = allData.length;
    const uniquePlayers = new Set(allData.map(item => item.player)).size;
    const uniqueItems = new Set(allData.map(item => item.item)).size;
    
    const validPrices = allData.filter(item => item.price > 0).map(item => item.price);
    const avgPrice = validPrices.length > 0 
        ? (validPrices.reduce((a, b) => a + b, 0) / validPrices.length)
        : 0;
    
    document.getElementById('totalTrades').textContent = totalTrades.toLocaleString();
    document.getElementById('totalPlayers').textContent = uniquePlayers.toLocaleString();
    document.getElementById('totalItems').textContent = uniqueItems.toLocaleString();
    document.getElementById('avgPrice').textContent = '$' + avgPrice.toFixed(2).toLocaleString();
}

// Initialize market table
function initializeMarketTable() {
    const tableData = allData.map(item => {
        const pos = item.position || { x: 0, y: 0, z: 0 };
        const posStr = `📍 ${pos.x}, ${pos.y}, ${pos.z}`;
        return [
            item.player,
            item.item,
            item.quantity.toLocaleString(),
            item.priceFormatted,
            '$' + (item.price * item.quantity).toFixed(2).toLocaleString(),
            posStr
        ];
    });
    
    marketTable = $('#marketTable').DataTable({
        data: tableData,
        pageLength: 25,
        order: [[3, 'desc']],
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/zh-CN.json'
        },
        columnDefs: [
            {
                targets: [2, 3, 4],
                className: 'dt-right'
            }
        ]
    });
}

// Apply filters
function applyFilters() {
    const minPrice = parseFloat(document.getElementById('minPrice').value) || 0;
    const maxPrice = parseFloat(document.getElementById('maxPrice').value) || Infinity;
    const minQty = parseInt(document.getElementById('minQty').value) || 0;
    const maxQty = parseInt(document.getElementById('maxQty').value) || Infinity;
    
    const filtered = allData.filter(item => 
        item.price >= minPrice && 
        item.price <= maxPrice &&
        item.quantity >= minQty &&
        item.quantity <= maxQty
    );
    
    const tableData = filtered.map(item => {
        const pos = item.position || { x: 0, y: 0, z: 0 };
        const posStr = `📍 ${pos.x}, ${pos.y}, ${pos.z}`;
        return [
            item.player,
            item.item,
            item.quantity.toLocaleString(),
            item.priceFormatted,
            '$' + (item.price * item.quantity).toFixed(2).toLocaleString(),
            posStr
        ];
    });
    
    marketTable.clear();
    marketTable.rows.add(tableData);
    marketTable.draw();
}

// Reset filters
function resetFilters() {
    document.getElementById('minPrice').value = '';
    document.getElementById('maxPrice').value = '';
    document.getElementById('minQty').value = '';
    document.getElementById('maxQty').value = '';
    
    const tableData = allData.map(item => {
        const pos = item.position || { x: 0, y: 0, z: 0 };
        const posStr = `📍 ${pos.x}, ${pos.y}, ${pos.z}`;
        return [
            item.player,
            item.item,
            item.quantity.toLocaleString(),
            item.priceFormatted,
            '$' + (item.price * item.quantity).toFixed(2).toLocaleString(),
            posStr
        ];
    });
    
    marketTable.clear();
    marketTable.rows.add(tableData);
    marketTable.draw();
}

// Switch tabs
function switchTab(tabName) {
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
    event.target.classList.add('active');
    document.getElementById(tabName + '-tab').classList.add('active');
}

// Initialize charts
function initializeCharts() {
    createTopItemsChart();
    createTopPlayersChart();
    createExpensiveItemsChart();
    createPriceDistributionChart();
    createRankings();
}

// Top items chart
function createTopItemsChart() {
    const itemCounts = {};
    allData.forEach(item => {
        itemCounts[item.item] = (itemCounts[item.item] || 0) + 1;
    });
    
    const sorted = Object.entries(itemCounts)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10);
    
    const ctx = document.getElementById('topItemsChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: sorted.map(item => item[0].length > 15 ? item[0].substring(0, 15) + '...' : item[0]),
            datasets: [{
                label: '交易次数',
                data: sorted.map(item => item[1]),
                backgroundColor: 'rgba(76, 175, 80, 0.7)',
                borderColor: 'rgba(76, 175, 80, 1)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// Top sellers chart
function createTopPlayersChart() {
    const playerCounts = {};
    allData.forEach(item => {
        playerCounts[item.player] = (playerCounts[item.player] || 0) + 1;
    });
    
    const sorted = Object.entries(playerCounts)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10);
    
    const ctx = document.getElementById('topPlayersChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: sorted.map(item => item[0]),
            datasets: [{
                label: '出售数量',
                data: sorted.map(item => item[1]),
                backgroundColor: 'rgba(33, 150, 243, 0.7)',
                borderColor: 'rgba(33, 150, 243, 1)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// Most expensive items chart
function createExpensiveItemsChart() {
    const sorted = [...allData]
        .filter(item => item.price > 0)
        .sort((a, b) => b.price - a.price)
        .slice(0, 10);
    
    const ctx = document.getElementById('expensiveItemsChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: sorted.map(item => item.item.length > 20 ? item.item.substring(0, 20) + '...' : item.item),
            datasets: [{
                label: '价格 ($)',
                data: sorted.map(item => item.price),
                backgroundColor: 'rgba(255, 152, 0, 0.7)',
                borderColor: 'rgba(255, 152, 0, 1)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            indexAxis: 'y',
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: { beginAtZero: true }
            }
        }
    });
}

// Price distribution chart
function createPriceDistributionChart() {
    const ranges = {
        '0-100': 0,
        '100-1000': 0,
        '1000-5000': 0,
        '5000-10000': 0,
        '10000-50000': 0,
        '50000+': 0
    };
    
    allData.forEach(item => {
        const price = item.price;
        if (price < 100) ranges['0-100']++;
        else if (price < 1000) ranges['100-1000']++;
        else if (price < 5000) ranges['1000-5000']++;
        else if (price < 10000) ranges['5000-10000']++;
        else if (price < 50000) ranges['10000-50000']++;
        else ranges['50000+']++;
    });
    
    const ctx = document.getElementById('priceDistChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: Object.keys(ranges),
            datasets: [{
                data: Object.values(ranges),
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)'
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'right'
                }
            }
        }
    });
}

// Create rankings
function createRankings() {
    // 大卖家排行榜
    const playerCounts = {};
    allData.forEach(item => {
        if (!playerCounts[item.player]) {
            playerCounts[item.player] = { count: 0, totalValue: 0 };
        }
        playerCounts[item.player].count += 1;
        playerCounts[item.player].totalValue += item.price * item.quantity;
    });
    
    const topSellers = Object.entries(playerCounts)
        .sort((a, b) => b[1].count - a[1].count)
        .slice(0, 15);
    
    const sellerHTML = topSellers.map((seller, index) => `
        <div class="ranking-item">
            <div class="ranking-number">#${index + 1}</div>
            <div class="ranking-info">
                <div class="ranking-name">${seller[0]}</div>
                <div class="ranking-detail">
                    出售次数: ${seller[1].count} | 总价值: $${seller[1].totalValue.toFixed(2).toLocaleString()}
                </div>
            </div>
        </div>
    `).join('');
    
    document.getElementById('sellerRanking').innerHTML = sellerHTML;
    
    // 高价物品排行榜
    const expensiveItems = [...allData]
        .filter(item => item.price > 0)
        .sort((a, b) => b.price - a.price)
        .slice(0, 15);
    
    const expensiveHTML = expensiveItems.map((item, index) => `
        <div class="ranking-item">
            <div class="ranking-number">#${index + 1}</div>
            <div class="ranking-info">
                <div class="ranking-name">${item.item}</div>
                <div class="ranking-detail">
                    卖家: ${item.player} | 价格: ${item.priceFormatted}
                </div>
            </div>
        </div>
    `).join('');
    
    document.getElementById('expensiveRanking').innerHTML = expensiveHTML;
}

// Search item for price comparison
function searchItemForComparison() {
    const searchTerm = document.getElementById('itemSearch').value.toLowerCase().trim();
    const resultsContainer = document.getElementById('comparisonResults');
    
    if (searchTerm.length < 2) {
        resultsContainer.innerHTML = '<div class="no-results">请输入至少2个字符进行搜索</div>';
        return;
    }
    
    // 按物品名分组
    const itemGroups = {};
    allData.forEach(item => {
        if (item.item.toLowerCase().includes(searchTerm)) {
            if (!itemGroups[item.item]) {
                itemGroups[item.item] = [];
            }
            itemGroups[item.item].push(item);
        }
    });
    
    if (Object.keys(itemGroups).length === 0) {
        resultsContainer.innerHTML = '<div class="no-results">😔 没有找到匹配的物品</div>';
        return;
    }
    
    // 生成HTML
    let html = '';
    for (const [itemName, items] of Object.entries(itemGroups)) {
        const sorted = items.sort((a, b) => a.price - b.price);
        const minPrice = sorted[0].price;
        
        html += `
            <div class="comparison-result">
                <h4>📦 ${itemName}</h4>
                <div class="price-list">
                    ${sorted.map(item => {
                        const pos = item.position || { x: 0, y: 0, z: 0 };
                        return `
                        <div class="price-item ${item.price === minPrice ? 'best-price' : ''}">
                            <div class="seller-info">
                                <span class="seller-name">${item.player}</span>
                                <span class="seller-qty">(数量: ${item.quantity})</span>
                                <div class="seller-location">📍 ${pos.x}, ${pos.y}, ${pos.z}</div>
                            </div>
                            <div class="price-value">${item.priceFormatted}</div>
                        </div>
                    `;
                    }).join('')}
                </div>
            </div>
        `;
    }
    
    resultsContainer.innerHTML = html;
}


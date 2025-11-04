import csv
import json

def convert_csv_to_json(csv_file, json_file):
    """
    将CSV文件转换为优化的JSON格式，便于前端使用
    """
    data = []
    
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            # 清理价格数据，去掉逗号和美元符号，转换为数字
            price_str = row['单价'].replace('$', '').replace(',', '')
            try:
                price = float(price_str)
            except:
                price = 0
            
            # 清理数量数据
            try:
                quantity = int(row['数量'])
            except:
                quantity = 0
            
            data.append({
                'player': row['玩家'],
                'quantity': quantity,
                'item': row['物品'],
                'price': price,
                'priceFormatted': row['单价']  # 保留原始格式化的价格用于显示
            })
    
    # 写入JSON文件
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Successfully converted {len(data)} records")
    print(f"[OK] JSON file saved: {json_file}")
    
    # 生成一些统计信息
    print("\n[Statistics]")
    print(f"   - Total trades: {len(data)}")
    print(f"   - Unique players: {len(set(item['player'] for item in data))}")
    print(f"   - Unique items: {len(set(item['item'] for item in data))}")
    
    if data:
        valid_prices = [item['price'] for item in data if item['price'] > 0]
        if valid_prices:
            print(f"   - Max price: ${max(valid_prices):,.2f}")
            print(f"   - Min price: ${min(valid_prices):,.2f}")
            print(f"   - Avg price: ${sum(valid_prices)/len(valid_prices):,.2f}")

if __name__ == "__main__":
    convert_csv_to_json('output.csv', 'data.json')


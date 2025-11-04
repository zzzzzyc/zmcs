import json
import re

def convert_json_to_data(input_json, output_json):
    """Convert JSON export to data.json with position info"""
    with open(input_json, 'r', encoding='utf-8') as f:
        source_data = json.load(f)
    
    export_time = source_data.get('exportTime', '')
    pattern = re.compile(r"^(.+?)\s出售\s(\d+)\s(.+?)\s单价：(.*)$")
    
    data = []
    for item in source_data.get('results', []):
        full_text = item.get('fullText')
        if not full_text:
            continue
        
        match = pattern.match(full_text)
        if match:
            player = match.group(1).strip()
            quantity = match.group(2).strip()
            item_name = match.group(3).strip()
            price_str = match.group(4).strip()
            
            # 清理价格数据
            price_clean = price_str.replace('$', '').replace(',', '')
            try:
                price = float(price_clean)
            except:
                price = 0
            
            # 清理数量数据
            try:
                qty = int(quantity)
            except:
                qty = 0
            
            # 获取位置信息
            pos = item.get('pos', {})
            position = {
                'x': pos.get('x', 0),
                'y': pos.get('y', 0),
                'z': pos.get('z', 0)
            }
            
            data.append({
                'player': player,
                'quantity': qty,
                'item': item_name,
                'price': price,
                'priceFormatted': price_str,
                'position': position
            })
    
    output_data = {
        'license': 'WTFPL - Do What The Fuck You Want To Public License',
        'website': 'https://github.com/zzzzzyc',
        'copyright': 'zzzzzyc@2025 - Free to use, modify, and distribute',
        'exportTime': export_time,
        'totalRecords': len(data),
        'data': data
    }
    
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"[OK] Successfully converted {len(data)} records")
    print(f"[OK] JSON file saved: {output_json}")
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
    import sys
    
    if len(sys.argv) >= 3:
        input_file, output_file = sys.argv[1], sys.argv[2]
        print(f"[INPUT]  {input_file}")
        print(f"[OUTPUT] {output_file}\n")
        convert_json_to_data(input_file, output_file)
    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
        print(f"[INPUT]  {input_file}")
        print(f"[OUTPUT] data.json (default)\n")
        convert_json_to_data(input_file, 'data.json')
    else:
        print("[INPUT]  JSON.json (default)")
        print("[OUTPUT] data.json (default)\n")
        convert_json_to_data('JSON.json', 'data.json')


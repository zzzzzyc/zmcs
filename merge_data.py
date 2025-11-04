import json
import os
from datetime import datetime

def merge_json_files(input_files, output_file='data_merged.json'):
    """
    Merge multiple data.json files and deduplicate
    Dedup key: position (x,y,z) + player + item
    """
    all_records = []
    latest_export_time = ''
    
    print("=" * 60)
    print("[MERGE] Starting to merge JSON files...")
    print("=" * 60)
    
    for file_path in input_files:
        if not os.path.exists(file_path):
            print(f"[WARN] File not found, skipping: {file_path}")
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if isinstance(data, dict) and 'data' in data:
                records = data['data']
                export_time = data.get('exportTime', '')
            elif isinstance(data, list):
                records = data
                export_time = ''
            else:
                print(f"[WARN] Invalid file format, skipping: {file_path}")
                continue
            
            all_records.extend(records)
            
            if export_time and (not latest_export_time or export_time > latest_export_time):
                latest_export_time = export_time
            
            print(f"[OK] Loaded: {file_path} ({len(records)} records)")
            
        except Exception as e:
            print(f"[ERROR] Failed to read file: {file_path}")
            print(f"        Error: {str(e)}")
            continue
    
    if not all_records:
        print("\n[ERROR] No valid data found!")
        return
    
    print(f"\n[STATS] Total loaded: {len(all_records)} records")
    print("[DEDUP] Starting deduplication...")
    
    unique_records = {}
    for record in all_records:
        pos = record.get('position', {})
        key = (pos.get('x', 0), pos.get('y', 0), pos.get('z', 0),
               record.get('player', ''), record.get('item', ''))
        if key not in unique_records:
            unique_records[key] = record
    
    merged_data = list(unique_records.values())
    duplicates = len(all_records) - len(merged_data)
    
    print(f"[OK] Deduplication completed!")
    print(f"   - Original records: {len(all_records)}")
    print(f"   - Duplicate records: {duplicates}")
    print(f"   - Unique records: {len(merged_data)}")
    
    output_data = {
        'license': 'WTFPL - Do What The Fuck You Want To Public License',
        'website': 'https://github.com/zzzzzyc (or your site)',
        'copyright': 'zzzzzyc@2025 - Free to use, modify, and distribute',
        'exportTime': latest_export_time or datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'totalRecords': len(merged_data),
        'mergedFrom': len(input_files),
        'data': merged_data
    }
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n[SAVE] Merge result saved: {output_file}")
    print("\n" + "=" * 60)
    print("[STATS] Merged Statistics:")
    print("=" * 60)
    print(f"   - 总交易数: {len(merged_data)}")
    print(f"   - 独立玩家: {len(set(r['player'] for r in merged_data))}")
    print(f"   - 物品种类: {len(set(r['item'] for r in merged_data))}")
    
    valid_prices = [r['price'] for r in merged_data if r.get('price', 0) > 0]
    if valid_prices:
        print(f"   - 最高价格: ${max(valid_prices):,.2f}")
        print(f"   - 最低价格: ${min(valid_prices):,.2f}")
        print(f"   - 平均价格: ${sum(valid_prices)/len(valid_prices):,.2f}")
    
    print("=" * 60)
    print("[DONE] Merge completed successfully!")
    print("=" * 60)


def main():
    """Scan and merge all data*.json files in current directory"""
    print("\n[SCAN] Scanning current directory...")
    
    import glob
    json_files = glob.glob('data*.json')
    json_files = [f for f in json_files if not f.startswith('data_merged')]
    
    if not json_files:
        print("[ERROR] No data*.json files found!")
        print("\n使用方法：")
        print("  1. 将多个 JSON 文件放在同一目录下")
        print("  2. 文件命名如: data1.json, data2.json, data_area1.json 等")
        print("  3. 运行此脚本")
        print("\n或者手动指定文件：")
        print("  merge_json_files(['file1.json', 'file2.json'], 'output.json')")
        return
    
    print(f"[OK] Found {len(json_files)} files:")
    for f in json_files:
        print(f"   - {f}")
    
    print()
    merge_json_files(json_files, 'data.json')


if __name__ == "__main__":
    main()
    # Or manually: merge_json_files(['data1.json', 'data2.json'], 'data.json')


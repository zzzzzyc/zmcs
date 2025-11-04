import json
import re
import csv

def parse_and_export_to_csv(json_file, csv_file):
    """
    解析Minecraft销售JSON文件，并将结果导出到CSV文件。
    此函数使用正则表达式从 fullText 字段提取信息。

    Args:
        json_file (str): 输入的JSON文件名。
        csv_file (str): 输出的CSV文件名。
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"错误: 文件 '{json_file}' 未找到。请确保它和脚本在同一个目录下。")
        return
    except json.JSONDecodeError:
        print(f"错误: 文件 '{json_file}' 的JSON格式无效。")
        return

    # 正则表达式与之前相同
    pattern = re.compile(r"^(.+?)\s出售\s(\d+)\s(.+?)\s单价：(.*)$")

    sales_data = []
    for item in data.get('results', []):
        full_text = item.get('fullText')
        if not full_text:
            continue

        match = pattern.match(full_text)
        if match:
            # 从匹配结果中提取分组
            player = match.group(1).strip()
            quantity = match.group(2).strip()
            item_name = match.group(3).strip()
            price = match.group(4).strip()
            sales_data.append([player, quantity, item_name, price])
        else:
            print(f"警告: 无法解析此行 -> '{full_text}'")

    # 如果没有解析到数据，则不创建文件
    if not sales_data:
        print("没有找到可以导出的销售信息。")
        return

    # --- 将数据写入CSV文件 ---
    try:
        # 'w' 表示写入模式
        # newline='' 防止写入CSV时出现多余的空行
        # encoding='utf-8-sig' 确保包含中文字符的CSV文件能被Excel正确识别
        with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
            # 创建一个csv写入器
            writer = csv.writer(f)
            
            # 1. 写入表头 (Header)
            headers = ["玩家", "数量", "物品", "单价"]
            writer.writerow(headers)
            
            # 2. 写入所有数据行
            writer.writerows(sales_data)
            
        print(f"成功！数据已导出到文件 '{csv_file}'")

    except IOError:
        print(f"错误: 无法写入文件 '{csv_file}'。请检查文件夹权限。")


if __name__ == "__main__":
    input_json_file = 'JSON.json'
    output_csv_file = 'output.csv'  # 定义输出文件名
    parse_and_export_to_csv(input_json_file, output_csv_file)
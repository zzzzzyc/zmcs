import json
import re

def parse_minecraft_sales(json_file):
    """
    解析Minecraft销售JSON文件，并以表格形式打印结果。
    此函数使用正则表达式从 fullText 字段提取信息。
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

    # 正则表达式，用于从 fullText 中捕获四个关键部分：
    # 1. (.+?)       - 玩家名 (非贪婪匹配，直到遇到' 出售 ')
    # 2. (\d+)        - 数量 (一个或多个数字)
    # 3. (.+?)       - 物品名 (非贪婪匹配，直到遇到' 单价：')
    # 4. (.*)         - 单价 (匹配剩余的所有字符)
    pattern = re.compile(r"^(.+?)\s出售\s(\d+)\s(.+?)\s单价：(.*)$")

    parsed_results = []
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
            parsed_results.append([player, quantity, item_name, price])
        else:
            print(f"警告: 无法解析此行 -> '{full_text}'")

    # 打印表格
    if parsed_results:
        print_table(parsed_results)
    else:
        print("没有找到可以解析的销售信息。")

def print_table(data):
    """
    将处理好的数据格式化为美观的表格并打印。
    """
    headers = ["玩家", "数量", "物品", "单价"]
    
    # 计算每列的最大宽度，以便对齐
    # 首先使用表头的宽度作为初始值
    column_widths = [len(header) for header in headers]
    for row in data:
        for i, cell in enumerate(row):
            # 考虑到中文字符通常占两个显示宽度，这里做一个简单的宽度估算
            # 对于纯ASCII，len()即可；对于混合文本，len()是字符数，不是显示宽度
            # 为简单起见，我们直接用字符长度，对于大多数终端也够用
            if len(cell) > column_widths[i]:
                column_widths[i] = len(cell)
    
    # 打印表头
    header_line = " | ".join(f"{headers[i]:<{column_widths[i]}}" for i in range(len(headers)))
    print(header_line)

    # 打印分隔线
    separator_line = "-+-".join("-" * width for width in column_widths)
    print(separator_line)

    # 打印数据行
    for row in data:
        # 玩家和物品名左对齐，数量和单价右对齐
        formatted_row = (
            f"{row[0]:<{column_widths[0]}} | "
            f"{row[1]:>{column_widths[1]}} | "
            f"{row[2]:<{column_widths[2]}} | "
            f"{row[3]:>{column_widths[3]}}"
        )
        print(formatted_row)

if __name__ == "__main__":
    parse_minecraft_sales('JSON.json')
"""
    json.dumps() : 将python字典转化成json字符串
    json.loads() : 将json字符串转化成python字典
"""

import json
from pathlib import Path

path = Path('user_info.json')

user = {}
user['name'] = input("请输入姓名：")
user['age'] = int(input("请输入年龄："))

# 1. 字典 -> json字符串
contents = json.dumps(user)

path.write_text(contents, encoding='utf-8')
print(f'信息已记录到{path}文件中!')

########################################

pro_path = Path("products.json")
text = pro_path.read_text()

# 2. json字符串 -> 字典
pro_info = json.loads(text)

print(pro_info)
print(type(pro_info))
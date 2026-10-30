import json
from pathlib import Path

path = Path('user_info.json')

# 如果json文件存在，读取json数据
if path.exists():
    text = path.read_text()
    user_dict = json.loads(text)
    print(f"用户:{user_dict['name']}")
    print(f"年龄:{user_dict['age']}")
          
# 如果json文件不存在，让用户填写信息，并写入
else:
    user_info = {}
    user_info['name'] = input("请输入姓名：")
    user_info['age'] = int(input("请输入年龄："))
    text = json.dumps(user_info)
    path.write_text(text)
    
    
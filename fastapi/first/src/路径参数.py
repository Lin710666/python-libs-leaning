from fastapi import FastAPI

app = FastAPI()

# 你可以使用与 Python 字符串格式化相同的语法声明路径“参数”或“变量”
## 路径参数 item_id 的值会作为参数 item_id 传递给你的函数
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
## FastAPI会利用类型注解自动进行类型转换
## FastAPI也会利用类型注解实现数据校验
## 比如/items/foo ,因为foo是str类型所以会返回错误信息

# 顺序很重要
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

## 这个顺序的话，/users/me就永远匹配不到了
## 你访问/users/me，FastAPI会把me传给上面的user_id
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

# 枚举类型
from enum import Enum

class Color(Enum):  # Color是一个枚举类
    RED = 1     # Color.RED是一个枚举成员
    GRENN = 2
    BLUE = 3

print(type(Color.RED))  # 一个枚举成员是一个Color的实例
'''输出得到：<enum 'Color'>'''

# 预设值
class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# 路径转换器
## OpenAPI 不支持声明内部包含路径的路径参数，因为这会导致测试和定义更加困难
## 直接使用 Starlette 的路径转换器，就可以用如下 URL 声明包含路径的路径参数
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
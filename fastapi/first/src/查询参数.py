## 声明的参数不是路径参数时，
## 路径操作函数会把该参数自动解释为“查询”参数
## 只要参数不是路由{}中的路径
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

## skip=0, limit=10就是在设置默认参数
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip+limit]

## 也可以用None设置可选参数
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
## 访问/items/22    返回：{"item_id": "22"}
## 访问/items/22?q=1    返回：{"item_id": "22", "q": "1"}

# Mixed
## 其中没有默认值的是"必选参数"
## 有默认值的是"可选参数"
@app.get("/pandq/{path}")
async def get_info(path: str, q1: int, q2: int|None = None):
    if q2:
        return {"path": path, "q1": q1, "q2": q2}
    return {"path": path, "q1": q1}
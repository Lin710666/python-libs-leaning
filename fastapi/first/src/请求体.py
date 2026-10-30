# "请求体"是客户端发送给你的 API 的数据
# "响应体"是你的 API 发送给客户端的数据
## 你的 API 几乎总是需要发送响应体。
## 但客户端不一定总是要发送请求体，
## 有时它们只请求某个路径，可能带一些查询参数，但不会发送请求体
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str|None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/{item_id}")
async def create_item(item: Item):
    return item

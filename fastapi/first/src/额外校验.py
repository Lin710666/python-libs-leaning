from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_item(q: Annotated[str|None, Query(min_length=3,max_length=50)] = None):
    results = {"item": [{"item": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 查询参数列表/多个值
@app.get("/itemlist")
async def read_items(q: Annotated[list[str]|None ,Query()] = ["foo","bar"]):
    return {"q": q}
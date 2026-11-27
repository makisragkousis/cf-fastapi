"""
Path + Query + Body

fastapi dev ch3/06_path_query_body.py
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.put("/items/{item_id}")
async def update_item(
        item_id: int,           # path param
        item: Item,             # body
        q: str | None = None    # query param
):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result["q"] = q
    return result
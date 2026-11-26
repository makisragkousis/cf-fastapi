"""
Path parameters

fastapi dev ch2/01_path_parameters.py
"""

from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:8000/items/55
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
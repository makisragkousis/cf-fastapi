"""
Nested Models

fastapi dev ch3/04_nested_models.py
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# {
#   "name": "Laptop",
#   "price": 999.99,
#   "images": [
#     {"url": "https://example.com/front.jpg", "name": "front"},
#     {"url": "https://example.com/back.jpg", "name": "back"}
#   ]
# }

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    price: float
    images: list[Image] = []

@app.post("/items/")
async def create_item(item: Item):
    return item
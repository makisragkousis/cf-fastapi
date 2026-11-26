"""
Basic Model

"""

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float| None = None

item = Item(name="Laptop", price=10)
print(item.name)
print(item.price)
print(item.model_dump())

item_second = Item(name="Ram", price="20")
print(item_second.model_dump())
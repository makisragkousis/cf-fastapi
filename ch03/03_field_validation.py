"""
Field Validation
"""

from pydantic import BaseModel, Field, ValidationError

class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float= Field(gt=0, description="greater than 0")
    tax: float | None = Field(default=None, ge=0)
    tags: list[str] = Field(default=[], max_length=10)

# item=Item(name="Laptop", price=10)
# print(item.model_dump())

# Validation Error
try:
    Item(name="", price=-10)
except ValidationError as e:
    print(e)
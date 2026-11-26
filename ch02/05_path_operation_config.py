"""
Path Operation Configuration
"""

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post(
    "/items/",
    status_code=status.HTTP_201_CREATED,
    tags=["items"],
    summary="Create a new item",
    description="Creates an item and returns it",
    response_description="Item Created",
    responses={
        404: {"description": "Not found"},
        422: {"description": "Validation Error"},
    },
)

async def create_item(item: Item):
    return {"id": 1, **item.model_dump()}
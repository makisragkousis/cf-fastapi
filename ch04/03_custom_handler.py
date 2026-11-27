"""
Custom Exception Handler

fastapi dev ch4/03_custom_handler.py
"""

from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id

@app.exception_handler(ItemNotFoundError)
async def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": f'Item {exc.item_id} not found'}
    )

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 0:
        raise ItemNotFoundError(item_id)
    return {"item_id": item_id}
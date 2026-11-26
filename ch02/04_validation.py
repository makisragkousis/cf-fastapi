"""
Validation

fastapi dev ch2/04_validation.py
"""
from typing import Annotated
from fastapi import FastAPI, Path, Query, HTTPException

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(
        item_id: Annotated[int, Path(ge=0, description="Item ID")],
        q: Annotated[str | None, Query(
            min_length=3,
            max_length=10,
            description="Query string")],
):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q}
"""
Annotated + Depends

fastapi dev ch5/06_annotated.py
"""

from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

def get_pagination(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(pagination: Annotated[dict, Depends(get_pagination)]):
    return pagination
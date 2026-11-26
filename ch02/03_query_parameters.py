"""
Query parameters

fastapi dev ch2/03_query_parameters.py
"""

from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:8000/items/?skip=1&limit=20&q=Laptop
@app.get("/items/")
async def read_items(
        skip: int = 0,
        limit: int = 10,
        q: str | None = None,
):
    return {"skip": skip, "limit": limit, "q": q}


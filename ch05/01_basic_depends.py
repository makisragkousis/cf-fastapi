"""
Basic Dependency

fastapi dev ch5/01_basic_depends.py
"""

from fastapi import FastAPI, Depends

app = FastAPI()

def get_query(q: str | None = None):
    return q

@app.get("/items/")
async def read_items(q: str | None = Depends(get_query)):
    return {"q": q}
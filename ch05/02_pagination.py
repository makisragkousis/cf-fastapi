"""
Pagination Dependency


"""

from fastapi import FastAPI, Depends

app = FastAPI()

def get_pagination(skip: int = 0, limit: int = 20):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(pagination: dict = Depends(get_pagination)):
    return pagination

@app.get("/users/")
async def read_users(pagination: dict = Depends(get_pagination)):
    return pagination

@app.get("/clients/")
async def read_clients(pagination: dict = Depends(get_pagination)):
    return pagination
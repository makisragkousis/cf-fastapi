"""
Route Order

fastapi dev ch2/02_route_order.py
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"username": "current user"}

@app.get("/users/{username}")
async def read_user(username: str):
    return {"username": username}
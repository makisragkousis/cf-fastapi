#main.py

from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def home():
    return {"message": "Hello, Coding Factory"}
"""
Yield DB

fastapi dev ch5/03_yield_db.py
"""

from fastapi import FastAPI, Depends

app = FastAPI()

class FakeSession():
    def query(self, model):
        return self
    def all(self):
        return [{"id": 1, "name": "Laptop"},{"id": 2, "name": "PC"}]
    def close(self):
        print("Session closed")

def get_db():
    db = FakeSession()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
async def get_items(db = Depends(get_db)):
    return db.query(None).all()
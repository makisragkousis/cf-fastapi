"""
main.py
"""
from fastapi import FastAPI
from routers.items import router as items_router
app = FastAPI()

app.include_router(
    items_router,
    prefix="/api/v1",
)


"""
routers/items.py
"""
from fastapi import APIRouter

router= APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

# http://127.0.0.1:8000/items/api/v1/?skip=1&limit=10
@router.get("/",)
async def read_items(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}

# http://127.0.0.1:8000/api/v1/items/10
@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
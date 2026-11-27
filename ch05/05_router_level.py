"""
Router level Dependency

fastapi dev ch5/05_router_level.py
"""

from fastapi import FastAPI, APIRouter, Depends, Header, HTTPException

app = FastAPI()

def verify_token(token: str = Header(alias="X-Token")):
    if token != "secret":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return token

router = APIRouter(
    prefix="/admin",
    dependencies=[Depends(verify_token)],
)

@router.get("/stats")
async def stats():
    return {"stats": {"count": 1, "items": 1}}

app.include_router(router)
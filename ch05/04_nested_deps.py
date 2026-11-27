"""
Nested Dependencies

fastapi dev ch5/04_nested_deps.py
"""

from fastapi import FastAPI, Depends, Header, HTTPException, status

app = FastAPI()

def verify_user(token: str = Header(alias="X-Token")):
    if token != "secret":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"username": "Nick", "active": True}

def get_current_active_user(user: dict = Depends(verify_user)):
    if not user.get("active"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Inactive user")
    return user

@app.get("/me")
async def read_me(user=Depends(get_current_active_user)):
    return user
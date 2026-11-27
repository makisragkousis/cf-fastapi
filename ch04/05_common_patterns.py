"""
Common Patterns

"""

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/users")
async def create_user(email: str):
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid email")
    if email == "exist@example.com":
        raise HTTPException(status_code=409, detail="User already exists")
    return {"email": email}

@app.delete("/admin/users/{user_id}")
async def delete_user(user_id: int, is_admin: bool = False):
    if not is_admin:
        raise HTTPException(status_code=403, detail="Not allowed")
    return {"deleted": user_id}
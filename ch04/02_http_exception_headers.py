"""
HTTP Exception with Headers

fastapi dev ch4/02_http_exception_headers.py
"""

from fastapi import FastAPI ,HTTPException, status

app = FastAPI()

@app.get("/protected")
async def protected():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated....",
        headers={"WWW-Authenticate": "Bearer"},
    )
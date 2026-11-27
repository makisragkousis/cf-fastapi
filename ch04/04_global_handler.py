"""
Global Handler

fastapi dev ch4/04_global_handler.py
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)},
    )

@app.get("/crash")
async def crash():
    raise ValueError("Something went wrong")

@app.get("/crash-again")
async def crash_again():
    raise ValueError("Something went wrong again")
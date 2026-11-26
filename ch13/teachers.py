from enum import StrEnum

from fastapi import FastAPI

app = FastAPI(title="TeacherAPI")

teachers = {
    "123456": {
        "vat": "12345689",
        "name": "Maria",
        "email": "maria@email.gr",
        "city": "athens",
    },
    "789123": {
        "vat": "92345681",
        "name": "George",
        "email": "george@email.gr",
        "city": "Patra"
    },
}

class Role(StrEnum):
    teacher = "teacher"
    employee = "employee"

@app.get("/teachers/count")
def count_teachers():
    return {"count": len(teachers)}


@app.get("/teachers/{city}")
def get_teacher(city: str) -> dict:
    result = teachers.get(city)
    return result

@app.get("/teachers")
def list_teachers(
        limit: int = 10,
) -> list[dict]:
    result = list(teachers.values())
    return result[:limit]

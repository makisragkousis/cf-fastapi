
from fastapi import FastAPI

app = FastAPI(title="TeacherAPI")

teachers = {
    "123456" : {
        "name": "Maria",
        "email": "maria@gmail.gr",
        "city": "Athens"
    },
    "7891234" : {
        "name": "George",
        "email": "george@gmail.gr",
        "city": "Patra"
    },
}

@app.get("/teachers/count")
def count_teachers():
    return {"count": len(teachers)}


@app.get("/teachers/{city}")
def get_teacher(city: str):
    return teachers[city]


@app.get("/teachers/")
def list_teachers(
        limit: int = 10,
) -> list[dict]:
    result = list(teachers.values())
    return result[:limit]
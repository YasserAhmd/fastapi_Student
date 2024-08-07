from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger =logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)

class Student(BaseModel):
    id:int
    name:str
    grade:int

students = [
    Student(id=1,name="Karim Ali",grade=5),
    Student(id=2,name="Samira Mousa",grade=3)
]

@app.get("/")
def main_page():
    return {"Greeting":"Students Management System"}

@app.get("/students/")
def read_students():
    return students

@app.post("/students/")
def create_student(new_student:Student):
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id:int,updated_student:Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"Error":"Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message":"Student deleted"}
    return {"Error":"Student not found"}

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    name: str
    email: str
    age: int
    Roll_number:str
    Department:str


@app.get("/")
def read_root():
    return {"Hello": "World"}

class StudentResponse(Student):
    id: int
   

@app.get("/")
def read_root():
    return {"Hello": "World"}

def create_student(student:Student)->StudentResponse:
    student.id=student_id["current"]
    return student


def read_student(id:int)->StudentResponse:
    return StudentResponse(id=id, **student.dict())


def update_student(id:int,student:Student)->StudentResponse:
    return StudentResponse(id=id, **student.dict())

def delete_student(id:int):
    return StudentResponse(id=id, **student.dict())


@app.post("/students")
def create_student_api(student:Student):
    return create_student(student)

@app.get("/students/{id}")
def read_student_api(id:int):
    return read_student(id)

@app.put("/students/{id}")
def update_student_api(id:int,student:Student):
    return update_student(id,student)

@app.delete("/students/{id}")
def delete_student_api(id:int):
    return delete_student(id)


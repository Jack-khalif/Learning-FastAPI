from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

# endpoint is the final bit of a communication channel
#GET, POST, PUT, DELETE are the most common HTTP methods
#GET is used to retrieve data from the server
#POST is used to send data to the server
#PUT is used to update data on the server
#DELETE is used to delete data from the server
@app.get("/") # this is the root endpoint
def index():
    return {"name": "First Data"}
#using /docs to access the documentation of the API
#eendpoint parameter is used to define the endpoint of the API
students = {

    1: {"name": "John", "age": 20,"class": "A"},
    2: {"name": "Jane", "age": 22,"class": "B"},
}

class Student(BaseModel):
    name: str
    age: int
    year: str
class updateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
#using get method to get all students

@app.get("/get-students/{student_id}") # this is the endpoint to get a student by id
def get_student(student_id: int = Path( description="The ID of the student you want to get",gt=0,lt=5,ge=1,le=5)):
    if student_id not in students:
        return {"error": "Student not found"}
    return students[student_id]
#gt,lt,ge,le are used to define the range of the age of the student
#using query parameters to filter the data
#difference betwween query parameters and path parameters is that query parameters are optional and path parameters are mandatory
@app.get("/get-by-name/")
def get_student(name:str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"error": "Student not found"}
#combining path and query parameters
@app.get("/get-by-name/{student_id}")
def get_student_by_name(student_id:int, name:str):
    if student_id not in students:
        return {"error": "Student not found"}
    if students[student_id]["name"] != name:
        return {"error": "Student not found"}
    return students[student_id]
#using POST method to create a new student
@app.post("/create-student/{student_id}")
def create_student(student_id:int, student: Student):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = student
    return students[student_id]
#using PUT method to update a student
@app.put("/update-student/{student_id}")
def update_student(student_id:int, student: updateStudent):
    if student_id not in students:
        return {"error": "Student not found"}
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.year != None:
        students[student_id]["year"] = student.year
    return students[student_id]
#using delete method to delete a student
@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted successfully"}
"""api creation for student database"""

from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    branch: str

student_database = {}


@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    try:
        if student_id not in student_database :
            raise HTTPException(status_code=404, detail="Student not found")
        return student_database[student_id] 
    except Exception as e:
        return (e.args)

@app.post("/add-student/{student_id}")
def add_student(student_id:int , student: Student):
    try:
        if student_id in student_database :
            return {"error":"Student already exist"}
        student_database[student_id] = student.dict()
        return {"message":"Student added successfully!"}
    except Exception as e:
        return (e.args)

@app.put("/update-student/{student_id}")
def update_student(student_id:int , student: Student):
    try:
        if student_id not in student_database :
            raise HTTPException(status_code=404, detail="Student does not exist")
        student_database[student_id].update(student.dict())
        return {"message":"Student data updated successfully!"}
    except Exception as e:
        return (e.args)
@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    try:
        if student_id not in student_database :
            raise HTTPException(status_code=404, detail="Student does not exist")
        student_database.pop(student_id)
        return {"message": "Student deleted successfully!!"}
    except Exception as e:
        return (e.args)

if __name__ == "__main__":
    uvicorn.run(app="tutorial:app", reload=True)
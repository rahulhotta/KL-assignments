"""api creation for student database"""


from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
import uvicorn
app = FastAPI()

student_client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")

student_db = student_client.interns_b2_23
student_inventory = student_db.Rahul_hotta


class Student(BaseModel):
    id: int
    name: str
    age: int
    branch: str

test_data = {
    "id":2,
    "name":"chinu",
    "age":22,
    "branch":"CSE"
}

# student_inventory.insert_one(test_data)
# student_database = {}
# print(list(student_inventory.find()))
# print(student_inventory.find_one({"id":1}))


"""Get all student data"""


@app.get("/view-all-students")
def view_students():
    try:
        # if list(student_inventory.find()) == []:
        #     return {"message":"Your DB is empty"}
        # return list(student_inventory.find())
        students = student_inventory.find()
        students_list = []
        for student in students:
            del student["_id"]
            students_list.append(student)
        return students_list
    except Exception as e:
        return (e.args)




"""Add a student to the db"""


@app.post("/add-student/{student_id}")
def add_student(student_id: int, student: Student):
    try:
        if list(student_inventory.find({"id": student_id})) != []:
            return {"error": "Student already exist"}
        student_inventory.insert_one(student.dict())
        return {"message": "Student added successfully!"}
    except Exception as e:
        return (e.args)


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: Student):
    try:
        if  list(student_inventory.find({"id": student_id})) == []:
            raise HTTPException(
                status_code=404, detail="Student does not exist")
        student_inventory.update_one({"id": student_id}, {"$set": student.dict()})
        return {"message": "Student data updated successfully!"}
    except Exception as e:
        return (e.args)


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    try:
        if  list(student_inventory.find({"id": student_id})) == []:
            raise HTTPException(
                status_code=404, detail="Student does not exist")
        student_inventory.delete_one({"id": student_id})
        return {"message": "Student deleted successfully!!"}
    except Exception as e:
        return (e.args)


if __name__ == "__main__":
    uvicorn.run(app="tutorial:app", reload=True)

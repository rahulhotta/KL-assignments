from fastapi import APIRouter
from scripts.core.handlers.student_info_handler import Student_handler
from scripts.constants.app_constants import Student
from scripts.core.handlers.email_handler import email_object, Email
import logging 
from scripts.logging.log_config import getLogger

getLogger()
student_router = APIRouter()


@student_router.get("/send_email")
def send_an_email(email: Email):
    try:
        student_object = Student_handler()
        avg_age = student_object.calculate_avg_age()
        message = f"Average age of all the students is {avg_age}"
        email_object.send_email(message,email)
        # email_object.send_email(email)
        return {"Message":"email sent!!"}
    except Exception as e:
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}


@student_router.get("/view-all-students")
def view_students():
    try:
        student_object = Student_handler()
        all_students = student_object.view_all_student()
        return all_students
    except Exception as e:
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}



@student_router.post("/add-student/{student_id}")
def add_student(student_id: int, student: Student):
    try:
        student_object = Student_handler()
        response = student_object.add_new_student(student_id, student)
        return response
    except Exception as e:
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}


@student_router.put("/update-student/{student_id}")
def update_a_student(student_id: int, student: Student):
    try:
        student_object = Student_handler()
        response = student_object.update_student(student_id, student)
        return response
    except Exception as e:
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}
@student_router.delete("/delete-student/{student_id}")
def delete_a_student(student_id : int):
    try:
        student_object = Student_handler()
        response = student_object.delete_student(student_id)
        return response
    except Exception as e:
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}
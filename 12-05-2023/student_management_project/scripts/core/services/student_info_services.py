from fastapi import APIRouter
from scripts.core.handlers.student_info_handler import Student_handler
from scripts.constants.app_constants import Student
from scripts.core.handlers.email_handler import email_object, Email
from scripts.logging.log_config import getLogger
import json
import pandas as pd
from json2html import *

logger = getLogger()
student_router = APIRouter()


@student_router.get("/send_email")
def send_an_email(email: Email):
    try:
        student_object = Student_handler()
        all_students_list_json = student_object.view_all_student()
        # all_students_str = str(json.dumps(all_students_list_json, default=str, indent=2))
        # pd_object = pd.read_json(all_students_str )
        # table = pd.DataFrame(pd_object)
        table = json2html.convert(json = all_students_list_json)        
        email_object.send_email(table, email)
        return {"Message": "email sent!!"}
    except Exception as e:
        logger.error({"status": "failed", "error": str(e.args)})
        return {"status": "failed", "error": str(e.args)}


@student_router.get("/view-all-students")
def view_students():
    try:
        student_object = Student_handler()
        all_students = student_object.view_all_student()
        return all_students
    except Exception as e:
        logger.error({"status": "failed", "error": str(e.args)})
        return {"status": "failed", "error": str(e.args)}


@student_router.post("/add-student/{student_id}")
def add_student(student_id: int, student: Student):
    try:
        student_object = Student_handler()
        response = student_object.add_new_student(student_id, student)
        return response
    except Exception as e:
        logger.error({"status": "failed", "error": str(e.args)})
        return {"status": "failed", "error": str(e.args)}


@student_router.put("/update-student/{student_id}")
def update_a_student(student_id: int, student: Student):
    try:
        student_object = Student_handler()
        response = student_object.update_student(student_id, student)
        return response
    except Exception as e:
        logger.error({"status": "failed", "error": str(e.args)})
        return {"status": "failed", "error": str(e.args)}


@student_router.delete("/delete-student/{student_id}")
def delete_a_student(student_id: int):
    try:
        student_object = Student_handler()
        response = student_object.delete_student(student_id)
        return response
    except Exception as e:
        logger.error({"status": "failed", "error": str(e.args)})
        return {"status": "failed", "error": str(e.args)}

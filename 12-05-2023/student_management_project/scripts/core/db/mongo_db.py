from pymongo import MongoClient
from scripts.utility.mongo_utility import MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME
from scripts.constants.app_constants import Student
import logging
from scripts.logging.logger import logger

try:
    student_client = MongoClient(MONGO_URI)
except Exception as e:
    logger.info({"status": "failed","error":str(e.args)})

try:
    student_db = student_client[MONGO_DB_NAME]
except Exception as e:
    logger.info({"status": "failed","error":str(e.args)})
    logging.error({"status": "failed","error":str(e.args)})

try:
    student_inventory = student_db[MONGO_COLLECTION_NAME]
except Exception as e:
    logger.info({"status": "failed","error":str(e.args)})
    logging.error({"status": "failed","error":str(e.args)})



class Student_database:
    def view_all_student(self):
        try:
            students = student_inventory.find()
            students_list = []
            for student in students:
                del student["_id"]
                students_list.append(student)
            return students_list
        except Exception as e:
            logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

    def add_student_to_db(self,student_id: int, student: Student):
        try:
            if list(student_inventory.find({"id": student_id})) != []:
                return {"error": "Student already exist"}
            student_inventory.insert_one(student.dict())
            return {"message": "Student added successfully!"}
        except Exception as e:
            logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

    def update_student_in_db(self,student_id: int, student: Student):
        try:
            if  list(student_inventory.find({"id": student_id})) == []:
                return {"Error":"Studnet does not exist"}
            student_inventory.update_one({"id": student_id}, {"$set": student.dict()})
            return {"message": "Student data updated successfully!"}
        except Exception as e:
            logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}
    def delete_student_from_db(self,student_id: int):
        try:
            if  list(student_inventory.find({"id": student_id})) == []:
                return {"Error":"Student not found!"}
            
            student_inventory.delete_one({"id": student_id})
            return {"message": "Student deleted successfully!!"}
        except Exception as e:
            logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

student_database_object = Student_database()
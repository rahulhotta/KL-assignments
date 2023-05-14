from pymongo import MongoClient
from scripts.utility.mongo_utility import MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME
from scripts.constants.app_constants import Student
import logging
# from scripts.logging.logger import logger

try:
    student_client = MongoClient(MONGO_URI)
except Exception as e:
    # logger.info({"status": "failed","error":str(e.args)})
    logging.error({"status": "failed", "error": str(e.args)})

try:
    student_db = student_client[MONGO_DB_NAME]
except Exception as e:
    # logger.info({"status": "failed", "error": str(e.args)})
    logging.error({"status": "failed", "error": str(e.args)})
    # print({"status": "failed", "error": str(e.args)})

try:
    student_inventory = student_db[MONGO_COLLECTION_NAME]
except Exception as e:
    # logger.info({"status": "failed", "error": str(e.args)})
    logging.error({"status": "failed", "error": str(e.args)})
    # print({"status": "failed", "error": str(e.args)})


class Student_database:
    def view_all_data(self):
        try:
            students = student_inventory.find()
            students_list = []
            for student in students:
                del student["_id"]
                students_list.append(student)
            return students_list
        except Exception as e:
            # logger.info({"status": "failed", "error": str(e.args)})
            logging.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}
    def find_by_id(self,id):
        try: 
            found_student = student_inventory.find(id)
            student_list = []
            for student in found_student:
                del student["_id"]
                student_list.append(student)
            return student_list
        except Exception as e:
            logging.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def add_data_to_db(self, student: Student):
        try:
            student_inventory.insert_one(student.dict())
        except Exception as e:
            # logger.info({"status": "failed", "error": str(e.args)})
            logging.error({"status": "failed", "error": str(e.args)})
            # return {"status": "failed", "error": str(e.args)}

    def update_data_in_db(self, student_id: int, student: Student):
        try:
            student_inventory.update_one(
                {"id": student_id}, {"$set": student.dict()})
        except Exception as e:
            # logger.info({"status": "failed", "error": str(e.args)})
            logging.error({"status": "failed", "error": str(e.args)})
            # return {"status": "failed", "error": str(e.args)}

    def delete_data_from_db(self, student_id: int):
        try:
            student_inventory.delete_one({"id": student_id})
        except Exception as e:
            # logger.info({"status": "failed", "error": str(e.args)})
            logging.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}


student_database_object = Student_database()

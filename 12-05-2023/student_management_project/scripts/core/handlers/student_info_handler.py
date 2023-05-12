from scripts.core.db.mongo_db import student_database_object
from scripts.constants.app_constants import Student
from scripts.logging.logger import logger
import logging

class Student_handler:

    def view_all_student(self):
        try :
            return student_database_object.view_all_student()
        except Exception as e:
            logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

        
    def add_new_student(self,student_id:int, student: Student ):
        try:
            return student_database_object.add_student_to_db(student_id, student)
        except Exception as e:
            logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}
        
    def update_student(self,student_id:int, student: Student):
        try:
            return student_database_object.update_student_in_db(student_id, student)
        except Exception as e:
            logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

        
    def delete_student(self,student_id:int):
        try:
            return student_database_object.delete_student_from_db(student_id)
        except Exception as e:
            logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}



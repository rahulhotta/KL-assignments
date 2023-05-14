from scripts.core.db.mongo_db import student_database_object
from scripts.constants.app_constants import Student
# from scripts.logging.logger import logger
import logging

class Student_handler:
    def view_all_student(self):
        try :
            all_students = student_database_object.view_all_data()
            if all_students == []:
                return {"status": "Success","Message":"No students found"}
            return all_students 
        except Exception as e:
            # logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

        
    def add_new_student(self,student_id:int, student: Student ):
        try:
            if student_database_object.find_by_id({"id":student_id}) != []:
                return {"status": "failed","error":"Student already exist"}
            student_database_object.add_data_to_db( student)
            return {"status":"Success","Message":"Student added successfully"}
        except Exception as e:
            # logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}
        
    def update_student(self,student_id:int, student: Student):
        try:
            if student_database_object.find_by_id({"id":student_id}) == []:
                return {"status": "failed","error":"Student does not exist"}
            student_database_object.update_data_in_db(student_id, student)
            return {"status":"Success","Message":"Student data updated successfully"}
        except Exception as e:
            # logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}

        
    def delete_student(self,student_id:int):
        try:
            if student_database_object.find_by_id({"id":student_id}) == []:
                return {"status": "failed","error":"Student does not exist"}
            student_database_object.delete_data_from_db(student_id)
            return {"status":"Success","Message":"Student deleted successfully"}
        except Exception as e:
            # logger.info({"status": "failed","error":str(e.args)})
            logging.error({"status": "failed","error":str(e.args)})
            return {"status": "failed","error":str(e.args)}



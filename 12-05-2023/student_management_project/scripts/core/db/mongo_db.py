from pymongo import MongoClient
from scripts.utility.mongo_utility import MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME
import logging
from scripts.logging.log_config import getLogger

getLogger()
class Mongo_database:
    def __init__(self):
        try:
            self.client = MongoClient(MONGO_URI)
        except Exception as e:
            logging.error({"status": "failed", "error": str(e.args)})
        try:
            self.db = self.client[MONGO_DB_NAME]
        except Exception as e:
            logging.error({"status": "failed", "error": str(e.args)})
        try:
            self.inventory = self.db[MONGO_COLLECTION_NAME]
        except Exception as e:
            logging.error({"status": "failed", "error": str(e.args)})
    def view_all_data(self):
        try:
            inventory_data = self.inventory.find()
            data_list = []
            for student in inventory_data:
                del student["_id"]
                data_list.append(student)
            return data_list
        except Exception as e:
            logging.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}
    def find_by_id(self,id):
        try: 
            found_data = self.inventory.find(id)
            data_list = []
            for student in found_data:
                del student["_id"]
                data_list.append(student)
            return data_list
        except Exception as e:
            logging.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def add_data_to_db(self, data):
        try:
            self.inventory.insert_one(data.dict())
        except Exception as e:
            logging.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def update_data_in_db(self, obj_id: int, data):
        try:
            self.inventory.update_one(
                {"id": obj_id}, {"$set": data.dict()})
        except Exception as e:
            logging.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}

    def delete_data_from_db(self, obj_id: int):
        try:
            self.inventory.delete_one({"id": obj_id})
        except Exception as e:
            logging.error({"status": "failed", "error": str(e.args)})
            return {"status": "failed", "error": str(e.args)}


student_database_object = Mongo_database()

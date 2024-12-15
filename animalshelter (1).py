from pymongo import MongoClient

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        self.client = MongoClient("mongodb://noahkhomer:noahkhomerpassword@nv-desktop-services.apporto.com:32917/AAC")
        self.database = self.client["AAC"]

    def create(self, data):
        try:
            self.database.animals.insert_one(data)
            return True
        except Exception as e:
            print(f"Error inserting data: {e}")
            return False

    def read(self, query):
        try:
            results = self.database.animals.find(query)
            return list(results)
        except Exception as e:
            print(f"Error reading data: {e}")
            return []

    def update(self, query, update_data):
        try:
            result = self.database.animals.update_many(query, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            print(f"Error updating data: {e}")
            return 0

    def delete(self, query):
        try:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting data: {e}")
            return 0

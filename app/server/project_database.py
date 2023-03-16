from pymongo import MongoClient
from bson.objectid import ObjectId

CONNECTION_STRING = "mongodb://localhost:27017/"
client = MongoClient(CONNECTION_STRING)
db = client['projects']
  

project_collection=db["project_collection"]

def project_helper(project) -> dict:
    return {
        "id": str(project["_id"]),
        "name": project["name"],
        "start_date": project["start_date"],
        "description": project["description"],
    }

async def get_projects() -> dict:
    project_list=[]
    for project in project_collection.find():
        project_list.append(project_helper(project))
    return project_list

async def add_project(project_data: dict) -> dict:
    project = project_collection.insert_one(project_data)
    new_project = project_collection.find_one({"_id": project.inserted_id})
    return project_helper(new_project)

async def get_project(name: str) -> dict:
    project = project_collection.find_one({"name": name})
    if project:
        return project_helper(project)

async def update_project(name: str, data: dict):
    if len(data)<1:
        return False
    project = project_collection.find_one({"name": name})
    if project:
        updated_project = project_collection.update_one({"name": name}, {"$set": data})
        if updated_project:
            return True
        return False

async def delete_project(name: str):
    project = project_collection.find_one({"name": name})
    if project:
        project_collection.delete_one({"name": name})
        return True
    return False
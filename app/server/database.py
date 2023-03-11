import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_HOST = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_HOST)
database = client.projects

project_collection = database.get_collection("project_collection")

def project_helper(project) -> dict:
    return {
        "id": str(project["_id"]),
        "name": project["name"],
        "start_date": project["start_date"],
        "description": project["description"],
    }

async def get_projects():
    projects=[]
    async for project in project_collection.find():
        projects.append(project_helper(project))
    return projects

async def add_project(project_data: dict) -> dict:
    project = await project_collection.insert_one(project_data)
    new_project = await project_collection.find_one({"_id": project.inserted_id})
    return project_helper(new_project)

async def get_project(id: str) -> dict:
    project = await project_collection.find_one({"_id": ObjectId(id)})
    if project:
        return project_helper(project)

async def update_project(id: str, data: dict):
    if len(data)<1:
        return False
    project = await project_collection.find_one({"_id": ObjectId(id)})
    if project:
        updated_project = await project_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        if updated_project:
            return True
        return False

async def delete_project(id: str):
    project = await project_collection.find_one({"_id": ObjectId(id)})
    if project:
        await project_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
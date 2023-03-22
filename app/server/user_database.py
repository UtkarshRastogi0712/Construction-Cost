from pymongo import MongoClient
from bson.objectid import ObjectId

def db_init():
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    db = client['users']
    user_collection=db["user_collection"]
    return user_collection

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"],
        "hashed_password": user["hashed_password"],
        "disabled": user["disabled"],
    }

async def get_users() -> dict:
    user_collection = db_init()
    users=[]
    for user in user_collection.find():
        users.append(user_helper(user))
    return users

async def add_user(user_data: dict) -> dict:
    user_collection = db_init()
    user = user_collection.insert_one(user_data)
    new_user = user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

async def get_user(id: str) -> dict:
    user_collection = db_init()
    user = user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

'''
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
    return False'''
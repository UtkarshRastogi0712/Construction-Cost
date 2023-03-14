import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_HOST = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_HOST)
database = client.users

user_collection = database.get_collection("user_collection")

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"],
        "hashed_password": user["full_name"],
        "disabled": user["disabled"],
    }

async def get_users():
    users=[]
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

async def get_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
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
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi import Depends
from server.models.user import UserSchema
from server.helper.login import *

from server.project_database import(
    get_projects,
    get_project,
    add_project,
    delete_project,
    update_project,
)

from server.models.project import(
    ErrorResponseModel,
    ResponseModel,
    ProjectSchema,
    UpdateProjectModel,
)

router = APIRouter()

@router.post("/add", response_description="Project data added to the database")
async def add_project_data(project: ProjectSchema = Body(...), current_user: UserSchema = Depends(get_current_user)):
    project.creator=current_user.username
    project = jsonable_encoder(project)
    new_project = await add_project(project)
    return ResponseModel(new_project, "Project added successfully.")

@router.get("/showall", response_description="Projects retrieved")
async def get_all_projects():
    projects = await get_projects()
    if projects:
        return ResponseModel(projects, "Projects retrieved successfully")
    return ResponseModel(projects, "Empty list returned")

@router.get("/showone", response_description="Project retrieved")
async def get_one_project(name: str):
    project = await get_project(name)
    if project:
        return ResponseModel(project, "Project retrieved successfully")
    return ErrorResponseModel("An error occured", 404, "Project doesnt exist")

@router.put("/update", response_description="Project details updated")
async def update_one_project(name: str, req: UpdateProjectModel = Body(...)):
    req = {k:v for k,v in req.dict().items() if v is not None}
    updated_project = await update_project(name, req)
    if updated_project:
        return ResponseModel(
            "Project with name {name} updated succesfully",
            "Project updated"
        )
    return ErrorResponseModel(
        "An error occured",
        404,
        "There was an error updating the project",
    )

@router.delete("/delete", response_description="Project data deleted")
async def delete_one_project(name: str):
    deleted_project = await delete_project(name)
    if deleted_project:
        return ResponseModel(
            "Project with name {name} deleted successfully",
            "Project deleted"
        )
    return ErrorResponseModel(
        "An error occured",
        404,
        "There was an error deleting the project"
    )

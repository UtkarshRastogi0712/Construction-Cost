from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

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
async def add_project_data(project: ProjectSchema = Body(...)):
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

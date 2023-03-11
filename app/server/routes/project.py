from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import(
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

@router.post("/", response_description="Project data added to the database")
async def add_project_data(project: ProjectSchema = Body(...)):
    project = jsonable_encoder(project)
    new_project = await add_project(project)
    return ResponseModel(new_project, "Project added successfully.")
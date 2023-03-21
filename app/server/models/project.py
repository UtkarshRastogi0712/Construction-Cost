from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class ProjectSchema(BaseModel):
    name: str=Field(...)
    start_date: str=Field(...)
    creator: str=Field(...)
    description: str=Field(...)
    class Config:
        orm_mode=True
        schema_example = {
            "example": {
                "name": "Something",
                "start_date": "Something",
                "creator": "Something",
                "description": "Something",
            }
        }

class UpdateProjectModel(BaseModel):
    name: Optional[str]
    description: Optional[str]

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
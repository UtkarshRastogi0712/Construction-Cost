from typing import Optional, Literal
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class Item(BaseModel):
    name: str=Field(...)
    price: float=Field(...)
    quantity: int=Field(...)
    category: Literal['Construction','Electrical','Plumbing','Labour','Flooring and Tiling','Miscellaneous']

class ProjectSchema(BaseModel):
    name: str=Field(...)
    start_date: datetime
    creator: str
    description: str=Field(...)
    items: list[Item]
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
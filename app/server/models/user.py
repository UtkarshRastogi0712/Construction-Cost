from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    username: str=Field(...)
    email: str=Field(...)
    full_name: str=Field(...)
    hashed_password: str=Field(...)
    disabled: str

class Token(BaseModel):
    access_token: str=Field(...)
    token_type: str=Field(...)

class TokenData(BaseModel):
    username: Optional[str]
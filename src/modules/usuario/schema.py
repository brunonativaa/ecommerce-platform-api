from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
from datetime import date
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    senha: str = field_validator(min_length= 8, max_length=100)
    data_cadastro = date

class UserResponse(BaseModel):
    id_usuario: int
    email: EmailStr

    class Config:
        from_attributes = True


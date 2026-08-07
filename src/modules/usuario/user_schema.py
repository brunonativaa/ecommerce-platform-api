from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from datetime import date
from typing import Optional


class TipoUsuarioEnum(str, Enum):
    CLINTE = "CLIENTE"
    VENDEDOR = "VENDEDOR"
    AMBOS = "AMBOS"

class CreateUserInput(BaseModel):
    email: EmailStr
    senha: str = Field(..., min_length=8, max_length=100)
    data_cadastro: Optional[date] = None
    tipo_usuario: TipoUsuarioEnum = TipoUsuarioEnum.CLINTE


class ClienteResponseSchema(BaseModel):
    id_cliente: int
    nome: str
    cpf: str

    class Config:
        from_attributes = True

class VendedorResponseSchema(BaseModel):
    id_vendedor: int
    nome_loja: str
    cnpj: str

    class Config:
        from_attributes: True

class UserResponse(BaseModel):
    id_usuario: int
    email: EmailStr
    data_cadastro: date
    tipo_usuario: TipoUsuarioEnum

    cliente: Optional[ClienteResponseSchema] = None
    vendedor: Optional[VendedorResponseSchema] = None

    class Config:
        from_attributes = True
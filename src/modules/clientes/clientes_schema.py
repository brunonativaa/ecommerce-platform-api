from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator, PastDate
from datetime import date
from typing import Optional
import re



class ClienteBase(BaseModel):
    nome: str
    cpf: str = Field(..., min_length=11, max_length=11)
    sexo: Optional[str] = None
    data_nascimento: date 

    
    @field_validator("data_nascimento")
    def validar_idade(cls, value):
        idade = (date.today() - value).days // 365
        if idade < 18:
            raise ValueError("Cliente deve ter 18 anos ou mais")
        return value

    @field_validator("cpf")
    def validar_cpf(cls, value: str) -> str:
        cpf_limpo = re.sub(r'\D', '', value)
        if len(cpf_limpo) != 11:
            raise ValueError("CPF deve conter exatamente 11 digítos")
        return cpf_limpo


class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id_cliente: int
    id_usuario: int

class ClienteOutput(BaseModel):
    id: int
    nome: str
    cpf: str
    

    class Config:
        from_attributes = True

class VendedorBase(BaseModel):
    nome_loja: str
    cnpj: str 

class VendedorCreate(VendedorBase):
    pass 

class VendedorResponse(VendedorBase):
    id_vendedor: int
    id_usuario: int

    class config:
        from_attributes = True
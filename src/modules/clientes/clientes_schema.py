from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator, PastDate
from datetime import date
from typing import Optional
import re


class ClienteCreateInput(BaseModel):
    nome: str
    cpf: str = Field(..., min_length=11, max_length=11)
    data_nascimento: date
    email: EmailStr
    cep: str = Field(..., min_length=8, max_length=9)
    numero: int = Field(..., gt=0)
    complemento: Optional[str] = None

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


class ClienteOutput(BaseModel):
    id: int
    nome: str
    cpf: str
    email: EmailStr
    logradouro: str
    bairro: str
    cidade: str
    uf: str
    numero: int
    complemento: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

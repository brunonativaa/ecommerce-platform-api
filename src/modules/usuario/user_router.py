from fastapi import APIRouter, status
from src.modules.usuario.user_schema import (
    CreateUserInput, UserResponse
)


router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post( "/", response_model=UserResponse,
            status_code=status.HTTP_201_CREATED,
            summary="Cadastrar um novo usuário")


def criar_usuario(usuario: CreateUserInput):
    return {
        "id_usuario": 1,
        "email": usuario.email,
        "tipo_usuario": usuario.tipo_usuario,
        "data_cadastro": usuario.data_cadastro,
        "cliente": None,
        "vendedor": None
    }
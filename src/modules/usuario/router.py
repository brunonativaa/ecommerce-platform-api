from fastapi import APIRouter, status, HTTPException
from src.modules.usuario.schema import UserCreate, UserResponse

router = APIRouter(tags=["user"])

@router.post("/produtos/criar", status_code=status.HTTP_201_CREATED)

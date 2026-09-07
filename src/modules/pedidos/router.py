from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database import get_db



router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.post("/", response_model=OrderResponse, status_code=status.HTPP_201_CREATED)

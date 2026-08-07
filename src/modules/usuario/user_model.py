from datetime import datetime, timezone
from sqlalchemy import Column, String, Date, Integer
from src.core.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)
    data_cadastro = Column(Date, default=lambda: datetime.now(timezone.utc).date(), nullable=False)
    tipo_usuario = Column(String(20), default="CLIENTE", nullable=False)
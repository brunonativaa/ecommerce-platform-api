from datetime import datetime, timezone
from sqlalchemy import Column, String, Date, Integer
from sqlachemy.orm import relationship, declarative_base
from src.core.database import Base


class UsuarioModel(Base):

    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)
    data_cadastro = Column(Date, default=lambda: datetime.now(timezone.utc).date(), nullable=False)

    profile_cliente = relationship("ClienteModel", uselist=False, back_populates="usuario")
    profile_vendedor = relationship("VendedorModel", uselist=False, back_populates="usuario")
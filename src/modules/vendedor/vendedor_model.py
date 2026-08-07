from typing import Optional
from sqlalchemy import Column, String, Integer, ForeignKey, unique
from src.core.database import Base


class VendedorBase(Base):
    __tablename__ = 'vendedor'

    id_vendedor = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, unique, ForeignKey("usuario.id_usuario"), nullable=False)
    nome_loja = Column(String(100), nullable=False)
    cnpj = Column(String(18), unique, nullable=False)
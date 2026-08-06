from typing import Optional
from sqlalchemy import Column, Integer, String, Date, CHAR, ForeignKey
from src.core.database import Base


class ClienteModel(Base):
    __tablename__ = 'cliente'

    id_cliente = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullabe=False, unique=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    sexo =  Column(CHAR(1))
    data_nascimento = Column(Date, nullable=False)
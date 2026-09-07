from datetime import datetime
import enum 
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Decimal
from sqlalchemy.sql import func
from src.core.database import Base


class TypeProductEnum(str, enum.Enum):
    ALIMENTOS = 'ALIMENTOS' 
    bELEZA = 'BELEZA'
    ROUPAS = 'ROUPAS'
    ELETRONICOS = 'ELETRONICOS'
    BRINQUEDOS ='BRINQUEDOS'

class ProductModel(Base):
    __tablename__ = "produto"

    id_produto = Column(Integer, primary_key=True, index=True)
    id_vendedor = Column(Integer, ForeignKey("vendedor.id_vendedor"), nullabe=False)
    nome = Column(String(30), nullabe=False)
    descricao = Column(String(100), nullabe=False)
    categoria = Column (
        Enum(TypeProductEnum, name="categoria"),
        nullabe=False,
        server_defaut=TypeProductEnum.ALIMENTOS.value
    )
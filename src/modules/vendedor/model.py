from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from src.core.database import Base



class VendedorModel(Base):
    __tablename__ = "vendedor"

    id_vendedor = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), unique=True, nullable=False)
    nome_loja = Column(String(100), nullable=False)
    cnpj = Column(String(18), Unique =True, nullable=False )

    usuario = relationship("UsuarioModel", back_populates="profile_vendedor")

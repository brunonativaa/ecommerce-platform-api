from datetime import datetime
import enum
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from src.core.database import Base



class StatusOrderEnum(str, enum.Enum):
        PENDENTE = "PENDENTE"
        PAGO = "PAGO"
        ENVIADO = "ENVIADO"
        ENTREGUE = "ENTREGUE"


class OrderModel(Base):
    __tablename__ = "pedido"

    id_pedido = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullabe=False)
    id_endereco_entrega = Column(Integer, nullabe=False, )
    data_hora = Column(DateTime(timezone=True), nullabe=False, server_defaul=func.now())
    status_geral = Column (
          Enum(StatusOrderEnum, name="status_pedido"),
          nullabe=False,
          server_default=StatusOrderEnum.PENDENTE.value
    )
from datetime import datetime 
from typing import Optional
from pydantic import BaseModel, ConfigDict
from src.modules.pedidos.model import StatusOrderEnum


class OrderBase(BaseModel):
    id_usuario: int
    id_endereco_entrega: int

class OrderCreate(OrderBase):
    status_geral: Optional[StatusOrderEnum] = StatusOrderEnum.PENDENTE


class OrderResponse(OrderBase):
    id_pedido: int
    data_hora: datetime
    status_geral: StatusOrderEnum

    model_config = ConfigDict(from_attributes=True)
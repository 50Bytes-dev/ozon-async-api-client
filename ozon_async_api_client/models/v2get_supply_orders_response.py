from typing import *

from pydantic import BaseModel, Field

from .v2order import V2order
from .v2warehouse import V2warehouse


class V2getSupplyOrdersResponse(BaseModel):
    """
    object model
    """

    orders: Optional[List[Optional[V2order]]] = Field(alias="orders", default=None)

    warehouses: Optional[List[Optional[V2warehouse]]] = Field(alias="warehouses", default=None)

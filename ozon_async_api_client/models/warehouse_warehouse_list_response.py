from typing import *

from pydantic import BaseModel, Field

from .warehouse_list_response_warehouse import WarehouseListResponseWarehouse


class WarehouseWarehouseListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[WarehouseListResponseWarehouse]]] = Field(alias="result", default=None)

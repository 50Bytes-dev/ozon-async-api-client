from typing import *

from pydantic import BaseModel, Field


class V1supplyWarehouse(BaseModel):
    """
    None model

    Склады для поставки.
    """

    address: Optional[str] = Field(alias="address", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

from typing import *

from pydantic import BaseModel, Field


class V2warehouse(BaseModel):
    """
    object model

    Склад поставки.
    """

    address: Optional[str] = Field(alias="address", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    warehouse_id: Optional[int] = Field(alias="warehouse_id", default=None)

from typing import *

from pydantic import BaseModel, Field


class V1supplyOrderContentUpdateRequestItem(BaseModel):
    """
    None model
    """

    quant: Optional[int] = Field(alias="quant", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

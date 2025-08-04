from typing import *

from pydantic import BaseModel, Field


class ValueItem(BaseModel):
    """
    None model
    """

    barcode: Optional[str] = Field(alias="barcode", default=None)

    expires_at: Optional[str] = Field(alias="expires_at", default=None)

    quant: Optional[int] = Field(alias="quant", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

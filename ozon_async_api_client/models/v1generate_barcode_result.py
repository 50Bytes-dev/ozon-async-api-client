from typing import *

from pydantic import BaseModel, Field


class V1generateBarcodeResult(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    error: Optional[str] = Field(alias="error", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

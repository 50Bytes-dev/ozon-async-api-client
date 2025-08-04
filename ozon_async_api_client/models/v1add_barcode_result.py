from typing import *

from pydantic import BaseModel, Field


class V1addBarcodeResult(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    error: Optional[str] = Field(alias="error", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

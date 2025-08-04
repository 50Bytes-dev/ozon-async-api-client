from typing import *

from pydantic import BaseModel, Field


class V1giveoutGetBarcodeResponse(BaseModel):
    """
    None model
    """

    barcode: Optional[str] = Field(alias="barcode", default=None)

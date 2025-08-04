from typing import *

from pydantic import BaseModel, Field


class ProductV1quantInfoResponseResultItemsQuantInfoQuantsBarcodesExtended(BaseModel):
    """
    object model
    """

    barcode: Optional[str] = Field(alias="barcode", default=None)

    error: Optional[str] = Field(alias="error", default=None)

    status: Optional[str] = Field(alias="status", default=None)

from typing import *

from pydantic import BaseModel, Field


class V3barcodes(BaseModel):
    """
    object model

    Штрихкоды отправления.
    """

    lower_barcode: Optional[str] = Field(alias="lower_barcode", default=None)

    upper_barcode: Optional[str] = Field(alias="upper_barcode", default=None)

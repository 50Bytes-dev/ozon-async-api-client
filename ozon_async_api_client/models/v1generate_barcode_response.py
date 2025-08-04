from typing import *

from pydantic import BaseModel, Field

from .v1generate_barcode_result import V1generateBarcodeResult


class V1generateBarcodeResponse(BaseModel):
    """
    object model
    """

    errors: Optional[List[Optional[V1generateBarcodeResult]]] = Field(alias="errors", default=None)

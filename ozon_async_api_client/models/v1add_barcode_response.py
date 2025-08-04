from typing import *

from pydantic import BaseModel, Field

from .v1add_barcode_result import V1addBarcodeResult


class V1addBarcodeResponse(BaseModel):
    """
    object model
    """

    errors: Optional[List[Optional[V1addBarcodeResult]]] = Field(alias="errors", default=None)

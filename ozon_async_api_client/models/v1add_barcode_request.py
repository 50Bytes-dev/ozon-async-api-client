from typing import *

from pydantic import BaseModel, Field

from .v1barcode import V1barcode


class V1addBarcodeRequest(BaseModel):
    """
    object model
    """

    barcodes: List[V1barcode] = Field(alias="barcodes")

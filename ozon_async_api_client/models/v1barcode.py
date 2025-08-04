from typing import *

from pydantic import BaseModel, Field


class V1barcode(BaseModel):
    """
    object model
    """

    barcode: str = Field(alias="barcode")

    sku: int = Field(alias="sku")

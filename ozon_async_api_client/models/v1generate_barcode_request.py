from typing import *

from pydantic import BaseModel, Field


class V1generateBarcodeRequest(BaseModel):
    """
    object model
    """

    product_ids: List[str] = Field(alias="product_ids")

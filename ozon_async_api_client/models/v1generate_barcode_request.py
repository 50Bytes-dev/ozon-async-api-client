from typing import *

from pydantic import BaseModel, Field


class V1generateBarcodeRequest(BaseModel):
    """
    object model
    """

    product_ids: List[int] = Field(alias="product_ids")

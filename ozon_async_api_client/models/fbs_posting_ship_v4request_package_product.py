from typing import *

from pydantic import BaseModel, Field


class FbsPostingShipV4requestPackageProduct(BaseModel):
    """
    object model
    """

    product_id: int = Field(alias="product_id")

    quantity: int = Field(alias="quantity")

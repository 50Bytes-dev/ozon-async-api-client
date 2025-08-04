from typing import *

from pydantic import BaseModel, Field


class V4fbsPostingShipPackageV4requestProduct(BaseModel):
    """
    None model
    """

    exemplarsIds: Optional[List[int]] = Field(alias="exemplarsIds", default=None)

    product_id: int = Field(alias="product_id")

    quantity: int = Field(alias="quantity")

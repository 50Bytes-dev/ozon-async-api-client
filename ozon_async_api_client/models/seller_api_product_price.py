from typing import *

from pydantic import BaseModel, Field


class SellerApiProductPrice(BaseModel):
    """
    object model
    """

    product_id: float = Field(alias="product_id")

    action_price: float = Field(alias="action_price")

    stock: Optional[float] = Field(alias="stock", default=None)

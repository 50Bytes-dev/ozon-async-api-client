from typing import *

from pydantic import BaseModel, Field

from .seller_api_product_price import SellerApiProductPrice


class SellerApiActivateProductV1request(BaseModel):
    """
    object model
    """

    action_id: float = Field(alias="action_id")

    products: List[SellerApiProductPrice] = Field(alias="products")

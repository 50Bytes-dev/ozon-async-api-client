from typing import *

from pydantic import BaseModel, Field


class SellerApiProductV1responseProduct(BaseModel):
    """
    object model
    """

    product_id: Optional[float] = Field(alias="product_id", default=None)

    reason: Optional[str] = Field(alias="reason", default=None)

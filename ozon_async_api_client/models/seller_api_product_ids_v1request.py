from typing import *

from pydantic import BaseModel, Field


class SellerApiProductIDsV1request(BaseModel):
    """
    object model
    """

    action_id: float = Field(alias="action_id")

    product_ids: List[float] = Field(alias="product_ids")

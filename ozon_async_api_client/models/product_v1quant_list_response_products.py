from typing import *

from pydantic import BaseModel, Field


class ProductV1quantListResponseProducts(BaseModel):
    """
    object model
    """

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

    quants: Optional[Any] = Field(alias="quants", default=None)

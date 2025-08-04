from typing import *

from pydantic import BaseModel, Field


class ProductGetProductInfoDescriptionRequest(BaseModel):
    """
    object model
    """

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    product_id: Optional[int] = Field(alias="product_id", default=None)

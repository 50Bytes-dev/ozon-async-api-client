from typing import *

from pydantic import BaseModel, Field


class V1postingUnpaidLegalProductListResponseProducts(BaseModel):
    """
    object model
    """

    product_id: Optional[int] = Field(alias="product_id", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    image_url: Optional[str] = Field(alias="image_url", default=None)

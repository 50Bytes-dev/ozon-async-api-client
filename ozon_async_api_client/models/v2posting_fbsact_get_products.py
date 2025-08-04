from typing import *

from pydantic import BaseModel, Field


class V2postingFBSActGetProducts(BaseModel):
    """
    object model
    """

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

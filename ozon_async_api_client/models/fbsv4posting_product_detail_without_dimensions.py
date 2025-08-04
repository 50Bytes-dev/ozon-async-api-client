from typing import *

from pydantic import BaseModel, Field


class Fbsv4postingProductDetailWithoutDimensions(BaseModel):
    """
    object model
    """

    mandatory_mark: Optional[Any] = Field(alias="mandatory_mark", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

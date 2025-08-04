from typing import *

from pydantic import BaseModel, Field


class V2postingProduct(BaseModel):
    """
    object model
    """

    digital_codes: Optional[Any] = Field(alias="digital_codes", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    is_marketplace_buyout: Optional[bool] = Field(alias="is_marketplace_buyout", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

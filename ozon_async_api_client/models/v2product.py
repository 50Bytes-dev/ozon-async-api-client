from typing import *

from pydantic import BaseModel, Field


class V2product(BaseModel):
    """
    object model

    Данные о товаре.
    """

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

from typing import *

from pydantic import BaseModel, Field


class V3fbsPostingProduct(BaseModel):
    """
    object model
    """

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[str] = Field(alias="offer_id", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    is_blr_traceable: Optional[bool] = Field(alias="is_blr_traceable", default=None)

    is_marketplace_buyout: Optional[bool] = Field(alias="is_marketplace_buyout", default=None)

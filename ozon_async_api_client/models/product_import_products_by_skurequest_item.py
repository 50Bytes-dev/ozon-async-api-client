from typing import *

from pydantic import BaseModel, Field


class ProductImportProductsBySKURequestItem(BaseModel):
    """
    object model
    """

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    old_price: Optional[str] = Field(alias="old_price", default=None)

    price: Optional[str] = Field(alias="price", default=None)

    sku: int = Field(alias="sku")

    vat: Optional[str] = Field(alias="vat", default=None)

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

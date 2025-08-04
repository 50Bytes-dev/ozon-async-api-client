from typing import *

from pydantic import BaseModel, Field


class PriceIndexesIndexSelfData(BaseModel):
    """
    object model

    Цена вашего товара на других площадках.
    """

    min_price: Optional[str] = Field(alias="min_price", default=None)

    min_price_currency: Optional[str] = Field(alias="min_price_currency", default=None)

    price_index_value: Optional[float] = Field(alias="price_index_value", default=None)

from typing import *

from pydantic import BaseModel, Field


class PriceIndexesIndexDataOzon(BaseModel):
    """
    object model

    Цена товара у конкурентов на Ozon.
    """

    minimal_price: Optional[str] = Field(alias="minimal_price", default=None)

    minimal_price_currency: Optional[str] = Field(alias="minimal_price_currency", default=None)

    price_index_value: Optional[float] = Field(alias="price_index_value", default=None)

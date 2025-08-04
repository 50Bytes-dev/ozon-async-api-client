from typing import *

from pydantic import BaseModel, Field


class SellerReturnsv1moneyWithoutCommission(BaseModel):
    """
    object model

    Стоимость товара без комиссии.
    """

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    price: Optional[float] = Field(alias="price", default=None)

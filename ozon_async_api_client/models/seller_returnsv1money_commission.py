from typing import *

from pydantic import BaseModel, Field


class SellerReturnsv1moneyCommission(BaseModel):
    """
    object model

    Информация о комиссии.
    """

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    price: Optional[float] = Field(alias="price", default=None)

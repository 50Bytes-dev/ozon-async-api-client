from typing import *

from pydantic import BaseModel, Field


class SellerReturnsv1moneyUtilization(BaseModel):
    """
    object model

    Стоимость утилизации.
    """

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    price: Optional[float] = Field(alias="price", default=None)

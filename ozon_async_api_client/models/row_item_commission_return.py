from typing import *

from pydantic import BaseModel, Field


class RowItemCommissionReturn(BaseModel):
    """
    object model

    Комиссия за возврат товара.
    """

    amount: Optional[float] = Field(alias="amount", default=None)

    bonus: Optional[float] = Field(alias="bonus", default=None)

    commission: Optional[float] = Field(alias="commission", default=None)

    compensation: Optional[float] = Field(alias="compensation", default=None)

    price_per_instance: Optional[float] = Field(alias="price_per_instance", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    standard_fee: Optional[float] = Field(alias="standard_fee", default=None)

    bank_coinvestment: Optional[float] = Field(alias="bank_coinvestment", default=None)

    stars: Optional[float] = Field(alias="stars", default=None)

    pick_up_point_coinvestment: Optional[float] = Field(alias="pick_up_point_coinvestment", default=None)

    total: Optional[float] = Field(alias="total", default=None)

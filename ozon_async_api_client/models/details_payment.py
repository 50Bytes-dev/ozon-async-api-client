from typing import *

from pydantic import BaseModel, Field


class DetailsPayment(BaseModel):
    """
    object model

    Выплачено за период.
    """

    currency_code: Optional[str] = Field(alias="currency_code", default=None)

    payment: Optional[float] = Field(alias="payment", default=None)

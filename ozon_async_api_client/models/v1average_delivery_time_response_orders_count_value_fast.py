from typing import *

from pydantic import BaseModel, Field


class V1averageDeliveryTimeResponseOrdersCountValueFast(BaseModel):
    """
    None model

    Нормативное время доставки до покупателя не больше 29 часов.
    """

    percent: Optional[int] = Field(alias="percent", default=None)

    value: Optional[int] = Field(alias="value", default=None)

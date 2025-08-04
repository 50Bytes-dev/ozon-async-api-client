from typing import *

from pydantic import BaseModel, Field


class V1averageDeliveryTimeResponseMetricsOrdersCountValueLong(BaseModel):
    """
    None model

    Нормативное время доставки до покупателя от 50 часов и больше.
    """

    percent: Optional[int] = Field(alias="percent", default=None)

    value: Optional[int] = Field(alias="value", default=None)

from typing import *

from pydantic import BaseModel, Field


class V1averageDeliveryTimeResponseMetricsOrdersCountValueMedium(BaseModel):
    """
    None model

    Нормативное время доставки до покупателя от 30 до 49 часов.
    """

    percent: Optional[int] = Field(alias="percent", default=None)

    value: Optional[int] = Field(alias="value", default=None)

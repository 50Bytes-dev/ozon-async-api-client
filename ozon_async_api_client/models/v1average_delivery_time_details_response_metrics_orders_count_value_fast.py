from typing import *

from pydantic import BaseModel, Field


class V1averageDeliveryTimeDetailsResponseMetricsOrdersCountValueFast(BaseModel):
    """
    None model

    Быстрое нормативное время доставки.
    """

    percent: Optional[int] = Field(alias="percent", default=None)

    value: Optional[int] = Field(alias="value", default=None)

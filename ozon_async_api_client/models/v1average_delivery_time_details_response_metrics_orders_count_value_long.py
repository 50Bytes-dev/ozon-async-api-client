from typing import *

from pydantic import BaseModel, Field


class V1averageDeliveryTimeDetailsResponseMetricsOrdersCountValueLong(BaseModel):
    """
    None model

    Долгое нормативное время доставки.
    """

    percent: Optional[int] = Field(alias="percent", default=None)

    value: Optional[int] = Field(alias="value", default=None)

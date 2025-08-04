from typing import *

from pydantic import BaseModel, Field


class V1averageDeliveryTimeDetailsResponseMetricsOrdersCountValueMedium(BaseModel):
    """
    None model

    Среднее нормативное время доставки.
    """

    percent: Optional[int] = Field(alias="percent", default=None)

    value: Optional[int] = Field(alias="value", default=None)

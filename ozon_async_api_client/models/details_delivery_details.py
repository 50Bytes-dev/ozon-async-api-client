from typing import *

from pydantic import BaseModel, Field

from .details_services import DetailsServices


class DetailsDeliveryDetails(BaseModel):
    """
    object model

    Заказы.
    """

    total: Optional[float] = Field(alias="total", default=None)

    amount: Optional[float] = Field(alias="amount", default=None)

    delivery_services: Optional[DetailsServices] = Field(alias="delivery_services", default=None)

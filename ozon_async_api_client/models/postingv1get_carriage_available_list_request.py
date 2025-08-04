from typing import *

from pydantic import BaseModel, Field


class Postingv1getCarriageAvailableListRequest(BaseModel):
    """
    object model
    """

    delivery_method_id: int = Field(alias="delivery_method_id")

    departure_date: Optional[str] = Field(alias="departure_date", default=None)

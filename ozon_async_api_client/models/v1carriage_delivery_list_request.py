from typing import *

from pydantic import BaseModel, Field


class V1carriageDeliveryListRequest(BaseModel):
    """
    object model
    """

    delivery_method_id: Optional[int] = Field(alias="delivery_method_id", default=None)

    departure_date: Optional[str] = Field(alias="departure_date", default=None)

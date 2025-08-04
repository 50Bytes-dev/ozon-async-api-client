from typing import *

from pydantic import BaseModel, Field


class V1getSupplyOrderTimeslotsRequest(BaseModel):
    """
    object model
    """

    supply_order_id: int = Field(alias="supply_order_id")

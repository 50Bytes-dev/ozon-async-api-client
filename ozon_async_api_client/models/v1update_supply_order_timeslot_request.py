from typing import *

from pydantic import BaseModel, Field

from .v1supply_order_timeslot import V1supplyOrderTimeslot


class V1updateSupplyOrderTimeslotRequest(BaseModel):
    """
    None model
    """

    supply_order_id: int = Field(alias="supply_order_id")

    timeslot: V1supplyOrderTimeslot = Field(alias="timeslot")

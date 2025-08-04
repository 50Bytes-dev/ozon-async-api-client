from typing import *

from pydantic import BaseModel, Field

from .v1supply_order_timeslot import V1supplyOrderTimeslot


class V1getSupplyOrderTimeslotsResponse(BaseModel):
    """
    None model
    """

    timeslots: Optional[List[Optional[V1supplyOrderTimeslot]]] = Field(alias="timeslots", default=None)

    timezone: Optional[Any] = Field(alias="timezone", default=None)

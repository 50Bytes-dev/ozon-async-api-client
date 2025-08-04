from typing import *

from pydantic import BaseModel, Field

from .v1get_supply_order_timeslot_status_response_status import V1getSupplyOrderTimeslotStatusResponseStatus
from .v1update_timeslot_error import V1updateTimeslotError


class V1getSupplyOrderTimeslotStatusResponse(BaseModel):
    """
    object model
    """

    errors: Optional[List[Optional[V1updateTimeslotError]]] = Field(alias="errors", default=None)

    status: Optional[V1getSupplyOrderTimeslotStatusResponseStatus] = Field(alias="status", default=None)

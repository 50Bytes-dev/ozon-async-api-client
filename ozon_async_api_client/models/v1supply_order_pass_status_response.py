from typing import *

from pydantic import BaseModel, Field

from .v1set_vehicle_error import V1setVehicleError
from .v1supply_order_pass_status_response_status import V1supplyOrderPassStatusResponseStatus


class V1supplyOrderPassStatusResponse(BaseModel):
    """
    object model
    """

    errors: Optional[List[Optional[V1setVehicleError]]] = Field(alias="errors", default=None)

    result: Optional[V1supplyOrderPassStatusResponseStatus] = Field(alias="result", default=None)

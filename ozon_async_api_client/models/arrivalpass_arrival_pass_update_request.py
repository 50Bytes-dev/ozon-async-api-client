from typing import *

from pydantic import BaseModel, Field

from .arrivalpass_arrival_pass_update_request_arrival_pass import ArrivalpassArrivalPassUpdateRequestArrivalPass


class ArrivalpassArrivalPassUpdateRequest(BaseModel):
    """
    None model
    """

    arrival_passes: List[ArrivalpassArrivalPassUpdateRequestArrivalPass] = Field(alias="arrival_passes")

from typing import *

from pydantic import BaseModel, Field

from .arrivalpass_arrival_pass_create_request_arrival_pass import ArrivalpassArrivalPassCreateRequestArrivalPass


class ArrivalpassArrivalPassCreateRequest(BaseModel):
    """
    None model
    """

    arrival_passes: List[ArrivalpassArrivalPassCreateRequestArrivalPass] = Field(alias="arrival_passes")

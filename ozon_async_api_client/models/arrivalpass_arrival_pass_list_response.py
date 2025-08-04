from typing import *

from pydantic import BaseModel, Field

from .arrivalpass_arrival_pass_list_response_arrival_pass import ArrivalpassArrivalPassListResponseArrivalPass


class ArrivalpassArrivalPassListResponse(BaseModel):
    """
    None model
    """

    arrival_passes: Optional[List[Optional[ArrivalpassArrivalPassListResponseArrivalPass]]] = Field(
        alias="arrival_passes", default=None
    )

    cursor: Optional[str] = Field(alias="cursor", default=None)

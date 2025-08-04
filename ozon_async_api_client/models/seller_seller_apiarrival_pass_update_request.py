from typing import *

from pydantic import BaseModel, Field

from .seller_seller_apiarrival_pass_update_request_arrival_pass import \
    SellerSellerAPIArrivalPassUpdateRequestArrivalPass


class SellerSellerAPIArrivalPassUpdateRequest(BaseModel):
    """
    None model
    """

    arrival_passes: List[SellerSellerAPIArrivalPassUpdateRequestArrivalPass] = Field(alias="arrival_passes")

    carriage_id: int = Field(alias="carriage_id")

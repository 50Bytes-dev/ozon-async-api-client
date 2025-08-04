from typing import *

from pydantic import BaseModel, Field

from .seller_seller_apiarrival_pass_create_request_arrival_pass import \
    SellerSellerAPIArrivalPassCreateRequestArrivalPass


class SellerSellerAPIArrivalPassCreateRequest(BaseModel):
    """
    object model
    """

    arrival_passes: List[SellerSellerAPIArrivalPassCreateRequestArrivalPass] = Field(alias="arrival_passes")

    carriage_id: int = Field(alias="carriage_id")

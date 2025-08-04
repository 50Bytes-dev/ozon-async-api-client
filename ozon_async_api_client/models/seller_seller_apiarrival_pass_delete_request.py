from typing import *

from pydantic import BaseModel, Field


class SellerSellerAPIArrivalPassDeleteRequest(BaseModel):
    """
    None model
    """

    arrival_pass_ids: List[int] = Field(alias="arrival_pass_ids")

    carriage_id: int = Field(alias="carriage_id")

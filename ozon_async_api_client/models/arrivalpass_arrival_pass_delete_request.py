from typing import *

from pydantic import BaseModel, Field


class ArrivalpassArrivalPassDeleteRequest(BaseModel):
    """
    None model
    """

    arrival_pass_ids: List[str] = Field(alias="arrival_pass_ids")

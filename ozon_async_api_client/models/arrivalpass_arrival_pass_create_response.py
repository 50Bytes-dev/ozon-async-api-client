from typing import *

from pydantic import BaseModel, Field


class ArrivalpassArrivalPassCreateResponse(BaseModel):
    """
    None model
    """

    arrival_pass_ids: Optional[List[str]] = Field(alias="arrival_pass_ids", default=None)

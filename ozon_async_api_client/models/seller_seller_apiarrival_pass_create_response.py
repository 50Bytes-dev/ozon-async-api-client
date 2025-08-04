from typing import *

from pydantic import BaseModel, Field


class SellerSellerAPIArrivalPassCreateResponse(BaseModel):
    """
    object model

    Результат запроса.
    """

    arrival_pass_ids: Optional[List[int]] = Field(alias="arrival_pass_ids", default=None)

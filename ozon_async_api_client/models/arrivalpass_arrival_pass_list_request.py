from typing import *

from pydantic import BaseModel, Field

from .arrival_pass_list_request_filter import ArrivalPassListRequestFilter


class ArrivalpassArrivalPassListRequest(BaseModel):
    """
    None model
    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    filter: Optional[ArrivalPassListRequestFilter] = Field(alias="filter", default=None)

    limit: int = Field(alias="limit")

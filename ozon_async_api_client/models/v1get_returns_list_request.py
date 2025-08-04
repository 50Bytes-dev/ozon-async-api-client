from typing import *

from pydantic import BaseModel, Field

from .get_returns_list_request_filter import GetReturnsListRequestFilter


class V1getReturnsListRequest(BaseModel):
    """
    object model
    """

    filter: Optional[GetReturnsListRequestFilter] = Field(alias="filter", default=None)

    limit: int = Field(alias="limit")

    last_id: Optional[int] = Field(alias="last_id", default=None)

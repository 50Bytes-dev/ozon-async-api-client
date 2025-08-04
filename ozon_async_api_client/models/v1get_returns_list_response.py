from typing import *

from pydantic import BaseModel, Field

from .get_returns_list_response_returns_item import GetReturnsListResponseReturnsItem


class V1getReturnsListResponse(BaseModel):
    """
    object model
    """

    returns: Optional[List[Optional[GetReturnsListResponseReturnsItem]]] = Field(alias="returns", default=None)

    has_next: Optional[bool] = Field(alias="has_next", default=None)

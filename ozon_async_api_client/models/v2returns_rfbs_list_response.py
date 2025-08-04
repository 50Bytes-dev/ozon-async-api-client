from typing import *

from pydantic import BaseModel, Field

from .returns_rfbs_list_response_returns import ReturnsRfbsListResponseReturns


class V2returnsRfbsListResponse(BaseModel):
    """
    object model
    """

    returns: Optional[ReturnsRfbsListResponseReturns] = Field(alias="returns", default=None)

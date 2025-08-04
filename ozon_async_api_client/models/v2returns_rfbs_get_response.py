from typing import *

from pydantic import BaseModel, Field

from .returns_rfbs_get_response_returns import ReturnsRfbsGetResponseReturns


class V2returnsRfbsGetResponse(BaseModel):
    """
    object model
    """

    returns: Optional[ReturnsRfbsGetResponseReturns] = Field(alias="returns", default=None)

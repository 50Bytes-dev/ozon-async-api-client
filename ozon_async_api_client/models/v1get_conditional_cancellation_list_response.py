from typing import *

from pydantic import BaseModel, Field

from .get_conditional_cancellation_list_response_counters import GetConditionalCancellationListResponseCounters


class V1getConditionalCancellationListResponse(BaseModel):
    """
    object model
    """

    result: Optional[Any] = Field(alias="result", default=None)

    total: Optional[int] = Field(alias="total", default=None)

    counters: Optional[GetConditionalCancellationListResponseCounters] = Field(alias="counters", default=None)

from typing import *

from pydantic import BaseModel, Field

from .v1approve_decline_discount_tasks_response_result import V1approveDeclineDiscountTasksResponseResult


class V1approveDeclineDiscountTasksResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1approveDeclineDiscountTasksResponseResult] = Field(alias="result", default=None)

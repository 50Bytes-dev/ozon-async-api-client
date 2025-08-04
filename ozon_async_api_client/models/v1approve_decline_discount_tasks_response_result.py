from typing import *

from pydantic import BaseModel, Field

from .approve_decline_discount_tasks_response_fail_detail import ApproveDeclineDiscountTasksResponseFailDetail


class V1approveDeclineDiscountTasksResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    fail_details: Optional[List[Optional[ApproveDeclineDiscountTasksResponseFailDetail]]] = Field(
        alias="fail_details", default=None
    )

    success_count: Optional[int] = Field(alias="success_count", default=None)

    fail_count: Optional[int] = Field(alias="fail_count", default=None)

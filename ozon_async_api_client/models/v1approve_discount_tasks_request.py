from typing import *

from pydantic import BaseModel, Field

from .v1approve_discount_tasks_request_task import V1approveDiscountTasksRequestTask


class V1approveDiscountTasksRequest(BaseModel):
    """
    object model
    """

    tasks: List[V1approveDiscountTasksRequestTask] = Field(alias="tasks")

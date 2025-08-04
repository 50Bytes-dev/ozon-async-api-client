from typing import *

from pydantic import BaseModel, Field

from .v1decline_discount_tasks_request_task import V1declineDiscountTasksRequestTask


class V1declineDiscountTasksRequest(BaseModel):
    """
    object model
    """

    tasks: List[V1declineDiscountTasksRequestTask] = Field(alias="tasks")

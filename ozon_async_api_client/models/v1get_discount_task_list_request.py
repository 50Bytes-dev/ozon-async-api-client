from typing import *

from pydantic import BaseModel, Field

from .v1discount_task_status import V1discountTaskStatus


class V1getDiscountTaskListRequest(BaseModel):
    """
    object model
    """

    status: V1discountTaskStatus = Field(alias="status")

    page: Optional[int] = Field(alias="page", default=None)

    limit: int = Field(alias="limit")

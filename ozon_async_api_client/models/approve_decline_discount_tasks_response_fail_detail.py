from typing import *

from pydantic import BaseModel, Field


class ApproveDeclineDiscountTasksResponseFailDetail(BaseModel):
    """
    object model
    """

    task_id: Optional[int] = Field(alias="task_id", default=None)

    error_for_user: Optional[str] = Field(alias="error_for_user", default=None)

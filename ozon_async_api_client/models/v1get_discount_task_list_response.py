from typing import *

from pydantic import BaseModel, Field

from .v1get_discount_task_list_response_task import V1getDiscountTaskListResponseTask


class V1getDiscountTaskListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[V1getDiscountTaskListResponseTask]]] = Field(alias="result", default=None)

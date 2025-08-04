from typing import *

from pydantic import BaseModel, Field

from .v1order_state import V1orderState


class V1supplyOrderStatusCounterResponseItem(BaseModel):
    """
    object model
    """

    count: Optional[int] = Field(alias="count", default=None)

    order_state: Optional[V1orderState] = Field(alias="order_state", default=None)

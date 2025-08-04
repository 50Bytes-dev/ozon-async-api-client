from typing import *

from pydantic import BaseModel, Field

from .v1supply_order_status_counter_response_item import V1supplyOrderStatusCounterResponseItem


class V1supplyOrderStatusCounterResponse(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[V1supplyOrderStatusCounterResponseItem]]] = Field(alias="items", default=None)

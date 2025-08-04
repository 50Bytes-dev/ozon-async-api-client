from typing import *

from pydantic import BaseModel, Field

from .v1supply_order_content_update_request_item import V1supplyOrderContentUpdateRequestItem


class V1supplyOrderContentUpdateRequest(BaseModel):
    """
    None model
    """

    items: Optional[List[Optional[V1supplyOrderContentUpdateRequestItem]]] = Field(alias="items", default=None)

    order_id: Optional[int] = Field(alias="order_id", default=None)

    supply_id: Optional[int] = Field(alias="supply_id", default=None)

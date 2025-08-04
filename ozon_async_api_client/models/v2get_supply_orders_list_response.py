from typing import *

from pydantic import BaseModel, Field


class V2getSupplyOrdersListResponse(BaseModel):
    """
    object model
    """

    last_supply_order_id: Optional[int] = Field(alias="last_supply_order_id", default=None)

    supply_order_id: Optional[List[int]] = Field(alias="supply_order_id", default=None)

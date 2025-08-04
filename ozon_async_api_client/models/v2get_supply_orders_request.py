from typing import *

from pydantic import BaseModel, Field


class V2getSupplyOrdersRequest(BaseModel):
    """
    object model
    """

    order_ids: List[int] = Field(alias="order_ids")

from typing import *

from pydantic import BaseModel, Field


class V2getSupplyOrdersRequest(BaseModel):
    """
    object model
    """

    order_ids: List[str] = Field(alias="order_ids")

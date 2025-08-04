from typing import *

from pydantic import BaseModel, Field


class V1supplyOrderCancelRequest(BaseModel):
    """
    None model
    """

    order_id: int = Field(alias="order_id")

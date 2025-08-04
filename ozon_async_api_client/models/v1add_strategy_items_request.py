from typing import *

from pydantic import BaseModel, Field


class V1addStrategyItemsRequest(BaseModel):
    """
    object model
    """

    product_id: List[str] = Field(alias="product_id")

    strategy_id: str = Field(alias="strategy_id")

from typing import *

from pydantic import BaseModel, Field


class V1addStrategyItemsRequest(BaseModel):
    """
    object model
    """

    product_id: List[int] = Field(alias="product_id")

    strategy_id: Union[str, int] = Field(alias="strategy_id")

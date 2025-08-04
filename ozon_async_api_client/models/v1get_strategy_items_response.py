from typing import *

from pydantic import BaseModel, Field

from .v1get_strategy_items_response_result import V1getStrategyItemsResponseResult


class V1getStrategyItemsResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1getStrategyItemsResponseResult] = Field(alias="result", default=None)

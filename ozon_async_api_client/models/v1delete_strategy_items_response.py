from typing import *

from pydantic import BaseModel, Field

from .v1delete_strategy_items_response_result import V1deleteStrategyItemsResponseResult


class V1deleteStrategyItemsResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1deleteStrategyItemsResponseResult] = Field(alias="result", default=None)

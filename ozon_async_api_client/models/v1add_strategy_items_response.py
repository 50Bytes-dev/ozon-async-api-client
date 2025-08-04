from typing import *

from pydantic import BaseModel, Field

from .v1add_strategy_items_response_result import V1addStrategyItemsResponseResult


class V1addStrategyItemsResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1addStrategyItemsResponseResult] = Field(alias="result", default=None)

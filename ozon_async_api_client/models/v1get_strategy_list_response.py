from typing import *

from pydantic import BaseModel, Field

from .get_strategy_list_response_strategy import GetStrategyListResponseStrategy


class V1getStrategyListResponse(BaseModel):
    """
    object model
    """

    strategies: Optional[List[Optional[GetStrategyListResponseStrategy]]] = Field(alias="strategies", default=None)

    total: Optional[int] = Field(alias="total", default=None)

from typing import *

from pydantic import BaseModel, Field

from .v1get_strategy_item_info_response_result import V1getStrategyItemInfoResponseResult


class V1getStrategyItemInfoResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1getStrategyItemInfoResponseResult] = Field(alias="result", default=None)

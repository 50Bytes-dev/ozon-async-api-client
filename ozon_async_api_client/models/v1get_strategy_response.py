from typing import *

from pydantic import BaseModel, Field

from .v1get_strategy_response_result import V1getStrategyResponseResult


class V1getStrategyResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1getStrategyResponseResult] = Field(alias="result", default=None)

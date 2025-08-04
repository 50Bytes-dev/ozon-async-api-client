from typing import *

from pydantic import BaseModel, Field

from .v1create_pricing_strategy_response_result import V1createPricingStrategyResponseResult


class V1createPricingStrategyResponse(BaseModel):
    """
    object model
    """

    result: Optional[V1createPricingStrategyResponseResult] = Field(alias="result", default=None)

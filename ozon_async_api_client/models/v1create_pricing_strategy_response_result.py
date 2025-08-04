from typing import *

from pydantic import BaseModel, Field


class V1createPricingStrategyResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    strategy_id: Optional[str] = Field(alias="strategy_id", default=None)

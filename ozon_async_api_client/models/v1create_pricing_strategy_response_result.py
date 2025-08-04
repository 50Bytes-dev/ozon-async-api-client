from typing import *

from pydantic import BaseModel, Field


class V1createPricingStrategyResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    strategy_id: Optional[Union[str, int]] = Field(alias="strategy_id", default=None)

from typing import *

from pydantic import BaseModel, Field

from .v1competitor import V1competitor


class V1updatePricingStrategyRequest(BaseModel):
    """
    object model
    """

    competitors: List[V1competitor] = Field(alias="competitors")

    strategy_id: Union[str, int] = Field(alias="strategy_id")

    strategy_name: str = Field(alias="strategy_name")

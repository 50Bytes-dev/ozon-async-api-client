from typing import *

from pydantic import BaseModel, Field

from .v1competitor import V1competitor


class V1createPricingStrategyRequest(BaseModel):
    """
    object model
    """

    competitors: List[V1competitor] = Field(alias="competitors")

    strategy_name: str = Field(alias="strategy_name")

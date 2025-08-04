from typing import *

from pydantic import BaseModel, Field


class V1updateStatusStrategyRequest(BaseModel):
    """
    object model
    """

    enabled: Optional[bool] = Field(alias="enabled", default=None)

    strategy_id: Union[str, int] = Field(alias="strategy_id")

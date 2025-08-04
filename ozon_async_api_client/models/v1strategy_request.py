from typing import *

from pydantic import BaseModel, Field


class V1strategyRequest(BaseModel):
    """
    object model
    """

    strategy_id: str = Field(alias="strategy_id")

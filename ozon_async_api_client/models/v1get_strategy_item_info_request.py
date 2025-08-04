from typing import *

from pydantic import BaseModel, Field


class V1getStrategyItemInfoRequest(BaseModel):
    """
    object model
    """

    product_id: int = Field(alias="product_id")

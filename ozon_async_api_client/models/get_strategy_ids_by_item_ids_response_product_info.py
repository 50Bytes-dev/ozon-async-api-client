from typing import *

from pydantic import BaseModel, Field


class GetStrategyIDsByItemIDsResponseProductInfo(BaseModel):
    """
    object model
    """

    product_id: Optional[int] = Field(alias="product_id", default=None)

    strategy_id: Optional[Union[str, int]] = Field(alias="strategy_id", default=None)

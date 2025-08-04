from typing import *

from pydantic import BaseModel, Field


class V1getStrategyItemsResponseResult(BaseModel):
    """
    object model

    Список товаров.
    """

    product_id: Optional[List[int]] = Field(alias="product_id", default=None)

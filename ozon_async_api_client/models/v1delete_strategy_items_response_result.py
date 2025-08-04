from typing import *

from pydantic import BaseModel, Field


class V1deleteStrategyItemsResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    failed_product_count: Optional[int] = Field(alias="failed_product_count", default=None)

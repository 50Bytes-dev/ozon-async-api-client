from typing import *

from pydantic import BaseModel, Field

from .sorting_order import SortingOrder


class AnalyticsSorting(BaseModel):
    """
    object model
    """

    key: Optional[str] = Field(alias="key", default=None)

    order: Optional[SortingOrder] = Field(alias="order", default=None)

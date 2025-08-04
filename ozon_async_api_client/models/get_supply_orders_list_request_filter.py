from typing import *

from pydantic import BaseModel, Field


class GetSupplyOrdersListRequestFilter(BaseModel):
    """
    object model

    Фильтр.
    """

    states: Optional[List[str]] = Field(alias="states", default=None)

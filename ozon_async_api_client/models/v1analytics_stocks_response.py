from typing import *

from pydantic import BaseModel, Field

from .v1analytics_stocks_response_item import V1analyticsStocksResponseItem


class V1analyticsStocksResponse(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[V1analyticsStocksResponseItem]]] = Field(alias="items", default=None)

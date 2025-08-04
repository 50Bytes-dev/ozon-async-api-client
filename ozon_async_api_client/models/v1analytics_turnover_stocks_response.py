from typing import *

from pydantic import BaseModel, Field

from .v1analytics_turnover_stocks_response_item import V1analyticsTurnoverStocksResponseItem


class V1analyticsTurnoverStocksResponse(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[V1analyticsTurnoverStocksResponseItem]]] = Field(alias="items", default=None)

from typing import *

from pydantic import BaseModel, Field

from .v1analytics_manage_stocks_response_item import V1analyticsManageStocksResponseItem


class V1analyticsManageStocksResponse(BaseModel):
    """
    object model
    """

    items: Optional[List[Optional[V1analyticsManageStocksResponseItem]]] = Field(alias="items", default=None)

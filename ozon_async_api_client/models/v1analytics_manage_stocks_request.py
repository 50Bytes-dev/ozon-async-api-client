from typing import *

from pydantic import BaseModel, Field

from .v1analytics_manage_stocks_request_filter import V1analyticsManageStocksRequestFilter


class V1analyticsManageStocksRequest(BaseModel):
    """
    object model
    """

    filter: Optional[V1analyticsManageStocksRequestFilter] = Field(alias="filter", default=None)

    limit: Optional[int] = Field(alias="limit", default=None)

    offset: Optional[int] = Field(alias="offset", default=None)

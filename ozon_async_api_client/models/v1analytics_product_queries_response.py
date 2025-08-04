from typing import *

from pydantic import BaseModel, Field

from .analytics_product_queries_response_analytics_period import AnalyticsProductQueriesResponseAnalyticsPeriod
from .v1analytics_product_queries_response_item import V1analyticsProductQueriesResponseItem


class V1analyticsProductQueriesResponse(BaseModel):
    """
    None model
    """

    analytics_period: Optional[AnalyticsProductQueriesResponseAnalyticsPeriod] = Field(
        alias="analytics_period", default=None
    )

    items: Optional[List[Optional[V1analyticsProductQueriesResponseItem]]] = Field(alias="items", default=None)

    page_count: Optional[int] = Field(alias="page_count", default=None)

    total: Optional[int] = Field(alias="total", default=None)

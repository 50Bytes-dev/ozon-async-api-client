from typing import *

from pydantic import BaseModel, Field

from .analytics_product_queries_details_response_query import AnalyticsProductQueriesDetailsResponseQuery
from .v1analytics_product_queries_details_response_analytics_period import \
    V1analyticsProductQueriesDetailsResponseAnalyticsPeriod


class V1analyticsProductQueriesDetailsResponse(BaseModel):
    """
    None model
    """

    analytics_period: Optional[V1analyticsProductQueriesDetailsResponseAnalyticsPeriod] = Field(
        alias="analytics_period", default=None
    )

    page_count: Optional[int] = Field(alias="page_count", default=None)

    queries: Optional[List[Optional[AnalyticsProductQueriesDetailsResponseQuery]]] = Field(
        alias="queries", default=None
    )

    total: Optional[int] = Field(alias="total", default=None)

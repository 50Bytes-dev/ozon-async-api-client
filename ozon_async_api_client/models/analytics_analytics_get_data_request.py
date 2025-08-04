from typing import *

from pydantic import BaseModel, Field

from .analytics_filter import AnalyticsFilter
from .analytics_metric import AnalyticsMetric
from .analytics_sorting import AnalyticsSorting
from .seller_serviceanalytics_dimension import SellerServiceanalyticsDimension


class AnalyticsAnalyticsGetDataRequest(BaseModel):
    """
    object model
    """

    date_from: str = Field(alias="date_from")

    date_to: str = Field(alias="date_to")

    dimension: List[SellerServiceanalyticsDimension] = Field(alias="dimension")

    filters: Optional[List[Optional[AnalyticsFilter]]] = Field(alias="filters", default=None)

    limit: int = Field(alias="limit")

    metrics: List[AnalyticsMetric] = Field(alias="metrics")

    offset: Optional[int] = Field(alias="offset", default=None)

    sort: Optional[List[Optional[AnalyticsSorting]]] = Field(alias="sort", default=None)

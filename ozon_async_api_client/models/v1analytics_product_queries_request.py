from typing import *

from pydantic import BaseModel, Field

from .analytics_product_queries_request_sort_by import AnalyticsProductQueriesRequestSortBy
from .analytics_product_queries_request_sort_dir import AnalyticsProductQueriesRequestSortDir


class V1analyticsProductQueriesRequest(BaseModel):
    """
    None model
    """

    date_from: str = Field(alias="date_from")

    date_to: Optional[str] = Field(alias="date_to", default=None)

    page: Optional[int] = Field(alias="page", default=None)

    page_size: int = Field(alias="page_size")

    skus: List[str] = Field(alias="skus")

    sort_by: Optional[AnalyticsProductQueriesRequestSortBy] = Field(alias="sort_by", default=None)

    sort_dir: Optional[AnalyticsProductQueriesRequestSortDir] = Field(alias="sort_dir", default=None)

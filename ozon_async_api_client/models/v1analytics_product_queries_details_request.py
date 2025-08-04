from typing import *

from pydantic import BaseModel, Field

from .v1analytics_product_queries_details_request_sort_by import V1analyticsProductQueriesDetailsRequestSortBy
from .v1analytics_product_queries_details_request_sort_dir import V1analyticsProductQueriesDetailsRequestSortDir


class V1analyticsProductQueriesDetailsRequest(BaseModel):
    """
    None model
    """

    date_from: str = Field(alias="date_from")

    date_to: Optional[str] = Field(alias="date_to", default=None)

    limit_by_sku: int = Field(alias="limit_by_sku")

    page: Optional[int] = Field(alias="page", default=None)

    page_size: int = Field(alias="page_size")

    skus: List[int] = Field(alias="skus")

    sort_by: Optional[V1analyticsProductQueriesDetailsRequestSortBy] = Field(alias="sort_by", default=None)

    sort_dir: Optional[V1analyticsProductQueriesDetailsRequestSortDir] = Field(alias="sort_dir", default=None)

from typing import *

from pydantic import BaseModel, Field


class AnalyticsProductQueriesDetailsResponseQuery(BaseModel):
    """
    None model
    """

    currency: Optional[str] = Field(alias="currency", default=None)

    gmv: Optional[float] = Field(alias="gmv", default=None)

    order_count: Optional[int] = Field(alias="order_count", default=None)

    position: Optional[float] = Field(alias="position", default=None)

    query: Optional[str] = Field(alias="query", default=None)

    query_index: Optional[int] = Field(alias="query_index", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    unique_search_users: Optional[int] = Field(alias="unique_search_users", default=None)

    unique_view_users: Optional[int] = Field(alias="unique_view_users", default=None)

    view_conversion: Optional[float] = Field(alias="view_conversion", default=None)

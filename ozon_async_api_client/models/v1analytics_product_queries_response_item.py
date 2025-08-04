from typing import *

from pydantic import BaseModel, Field


class V1analyticsProductQueriesResponseItem(BaseModel):
    """
    None model
    """

    category: Optional[str] = Field(alias="category", default=None)

    currency: Optional[str] = Field(alias="currency", default=None)

    gmv: Optional[float] = Field(alias="gmv", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    offer_id: Optional[Union[str, int]] = Field(alias="offer_id", default=None)

    position: Optional[float] = Field(alias="position", default=None)

    sku: Optional[int] = Field(alias="sku", default=None)

    unique_search_users: Optional[int] = Field(alias="unique_search_users", default=None)

    unique_view_users: Optional[int] = Field(alias="unique_view_users", default=None)

    view_conversion: Optional[float] = Field(alias="view_conversion", default=None)

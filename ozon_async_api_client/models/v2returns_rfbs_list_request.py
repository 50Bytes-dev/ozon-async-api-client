from typing import *

from pydantic import BaseModel, Field

from .v2returns_rfbs_filter import V2returnsRfbsFilter


class V2returnsRfbsListRequest(BaseModel):
    """
    object model
    """

    filter: Optional[V2returnsRfbsFilter] = Field(alias="filter", default=None)

    last_id: Optional[int] = Field(alias="last_id", default=None)

    limit: int = Field(alias="limit")

from typing import *

from pydantic import BaseModel, Field

from .v2posting_fbsact_list_filter import V2postingFBSActListFilter


class V2postingFBSActListRequest(BaseModel):
    """
    object model
    """

    filter: Optional[V2postingFBSActListFilter] = Field(alias="filter", default=None)

    limit: int = Field(alias="limit")

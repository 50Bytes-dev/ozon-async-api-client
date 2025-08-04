from typing import *

from pydantic import BaseModel, Field

from .get_conditional_cancellation_list_request_filters import GetConditionalCancellationListRequestFilters
from .get_conditional_cancellation_list_request_with import GetConditionalCancellationListRequestWith


class V1getConditionalCancellationListRequest(BaseModel):
    """
    object model
    """

    filters: Optional[GetConditionalCancellationListRequestFilters] = Field(alias="filters", default=None)

    limit: int = Field(alias="limit")

    offset: Optional[int] = Field(alias="offset", default=None)

    with_: Optional[GetConditionalCancellationListRequestWith] = Field(alias="with", default=None)

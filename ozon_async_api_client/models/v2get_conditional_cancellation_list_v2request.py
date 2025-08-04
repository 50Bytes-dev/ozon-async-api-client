from typing import *

from pydantic import BaseModel, Field

from .get_conditional_cancellation_list_v2request_filters import GetConditionalCancellationListV2requestFilters
from .get_conditional_cancellation_list_v2request_with import GetConditionalCancellationListV2requestWith


class V2getConditionalCancellationListV2request(BaseModel):
    """
    object model
    """

    filters: Optional[GetConditionalCancellationListV2requestFilters] = Field(alias="filters", default=None)

    last_id: Optional[int] = Field(alias="last_id", default=None)

    limit: int = Field(alias="limit")

    with_: Optional[GetConditionalCancellationListV2requestWith] = Field(alias="with", default=None)

from typing import *

from pydantic import BaseModel, Field


class GetConditionalCancellationListRequestFilters(BaseModel):
    """
    object model

    Фильтры.
    """

    cancellation_initiator: Optional[Any] = Field(alias="cancellation_initiator", default=None)

    posting_number: Optional[List[str]] = Field(alias="posting_number", default=None)

    state: Optional[str] = Field(alias="state", default=None)

from typing import *

from pydantic import BaseModel, Field


class GetConditionalCancellationListResponseCounters(BaseModel):
    """
    object model

    Cчётчик заявок в разных статусах.
    """

    on_approval: Optional[int] = Field(alias="on_approval", default=None)

    approved: Optional[int] = Field(alias="approved", default=None)

    rejected: Optional[int] = Field(alias="rejected", default=None)

from typing import *

from pydantic import BaseModel, Field

from .v2cancellation_initiator_enum import V2cancellationInitiatorEnum
from .v2cancellation_state_enum_filters import V2cancellationStateEnumFilters


class GetConditionalCancellationListV2requestFilters(BaseModel):
    """
    None model

    Фильтры.
    """

    cancellation_initiator: Optional[List[Optional[V2cancellationInitiatorEnum]]] = Field(
        alias="cancellation_initiator", default=None
    )

    posting_number: Optional[List[str]] = Field(alias="posting_number", default=None)

    state: Optional[V2cancellationStateEnumFilters] = Field(alias="state", default=None)

from typing import *

from pydantic import BaseModel, Field

from .get_conditional_cancellation_list_v2response_cancellation_reason import \
    GetConditionalCancellationListV2responseCancellationReason
from .get_conditional_cancellation_list_v2response_state import GetConditionalCancellationListV2responseState
from .v2cancellation_initiator_enum import V2cancellationInitiatorEnum


class GetConditionalCancellationListV2responseResult(BaseModel):
    """
    None model
    """

    approve_comment: Optional[str] = Field(alias="approve_comment", default=None)

    approve_date: Optional[str] = Field(alias="approve_date", default=None)

    auto_approve_date: Optional[str] = Field(alias="auto_approve_date", default=None)

    cancellation_id: Optional[int] = Field(alias="cancellation_id", default=None)

    cancellation_initiator: Optional[V2cancellationInitiatorEnum] = Field(alias="cancellation_initiator", default=None)

    cancellation_reason: Optional[GetConditionalCancellationListV2responseCancellationReason] = Field(
        alias="cancellation_reason", default=None
    )

    cancellation_reason_message: Optional[str] = Field(alias="cancellation_reason_message", default=None)

    cancelled_at: Optional[str] = Field(alias="cancelled_at", default=None)

    order_date: Optional[str] = Field(alias="order_date", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    source_id: Optional[int] = Field(alias="source_id", default=None)

    state: Optional[GetConditionalCancellationListV2responseState] = Field(alias="state", default=None)

    tpl_integration_type: Optional[str] = Field(alias="tpl_integration_type", default=None)

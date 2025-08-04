from typing import *

from pydantic import BaseModel, Field

from .conditional_cancellation_cancellation_reason import ConditionalCancellationCancellationReason
from .conditional_cancellation_state import ConditionalCancellationState


class V1conditionalCancellation(BaseModel):
    """
    object model

    Результат запроса.
    """

    cancellation_id: Optional[int] = Field(alias="cancellation_id", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    cancellation_reason: Optional[ConditionalCancellationCancellationReason] = Field(
        alias="cancellation_reason", default=None
    )

    cancelled_at: Optional[str] = Field(alias="cancelled_at", default=None)

    cancellation_reason_message: Optional[str] = Field(alias="cancellation_reason_message", default=None)

    tpl_integration_type: Optional[str] = Field(alias="tpl_integration_type", default=None)

    state: Optional[ConditionalCancellationState] = Field(alias="state", default=None)

    cancellation_initiator: Optional[str] = Field(alias="cancellation_initiator", default=None)

    order_date: Optional[str] = Field(alias="order_date", default=None)

    approve_comment: Optional[str] = Field(alias="approve_comment", default=None)

    approve_date: Optional[str] = Field(alias="approve_date", default=None)

    auto_approve_date: Optional[str] = Field(alias="auto_approve_date", default=None)

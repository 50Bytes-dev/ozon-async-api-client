from typing import *

from pydantic import BaseModel, Field


class V3cancellation(BaseModel):
    """
    object model

    Информация об отмене.
    """

    affect_cancellation_rating: Optional[bool] = Field(alias="affect_cancellation_rating", default=None)

    cancel_reason: Optional[str] = Field(alias="cancel_reason", default=None)

    cancel_reason_id: Optional[int] = Field(alias="cancel_reason_id", default=None)

    cancellation_initiator: Optional[str] = Field(alias="cancellation_initiator", default=None)

    cancellation_type: Optional[str] = Field(alias="cancellation_type", default=None)

    cancelled_after_ship: Optional[bool] = Field(alias="cancelled_after_ship", default=None)

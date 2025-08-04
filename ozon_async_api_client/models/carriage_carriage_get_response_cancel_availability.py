from typing import *

from pydantic import BaseModel, Field


class CarriageCarriageGetResponseCancelAvailability(BaseModel):
    """
    object model

    Возможность отмены.
    """

    is_cancel_available: Optional[bool] = Field(alias="is_cancel_available", default=None)

    reason: Optional[str] = Field(alias="reason", default=None)

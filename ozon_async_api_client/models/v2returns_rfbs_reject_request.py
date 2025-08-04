from typing import *

from pydantic import BaseModel, Field


class V2returnsRfbsRejectRequest(BaseModel):
    """
    object model
    """

    return_id: int = Field(alias="return_id")

    comment: Optional[str] = Field(alias="comment", default=None)

    rejection_reason_id: int = Field(alias="rejection_reason_id")

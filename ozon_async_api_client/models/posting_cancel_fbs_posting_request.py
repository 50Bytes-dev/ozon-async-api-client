from typing import *

from pydantic import BaseModel, Field


class PostingCancelFbsPostingRequest(BaseModel):
    """
    object model
    """

    cancel_reason_id: Optional[int] = Field(alias="cancel_reason_id", default=None)

    cancel_reason_message: Optional[str] = Field(alias="cancel_reason_message", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

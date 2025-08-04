from typing import *

from pydantic import BaseModel, Field

from .posting_cancel_reason import PostingCancelReason


class PostingCancelReasonListResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[PostingCancelReason]]] = Field(alias="result", default=None)

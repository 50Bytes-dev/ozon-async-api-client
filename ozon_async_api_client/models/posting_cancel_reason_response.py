from typing import *

from pydantic import BaseModel, Field

from .related_posting_cancel_reason import RelatedPostingCancelReason


class PostingCancelReasonResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[RelatedPostingCancelReason]]] = Field(alias="result", default=None)

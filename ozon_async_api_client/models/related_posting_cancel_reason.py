from typing import *

from pydantic import BaseModel, Field

from .related_posting_cancel_reasons import RelatedPostingCancelReasons


class RelatedPostingCancelReason(BaseModel):
    """
    object model
    """

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    reasons: Optional[List[Optional[RelatedPostingCancelReasons]]] = Field(alias="reasons", default=None)

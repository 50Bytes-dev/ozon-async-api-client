from typing import *

from pydantic import BaseModel, Field


class PostingCancelReasonRequest(BaseModel):
    """
    object model
    """

    related_posting_numbers: List[str] = Field(alias="related_posting_numbers")

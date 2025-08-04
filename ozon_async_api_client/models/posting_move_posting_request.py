from typing import *

from pydantic import BaseModel, Field


class PostingMovePostingRequest(BaseModel):
    """
    object model
    """

    posting_number: List[str] = Field(alias="posting_number")

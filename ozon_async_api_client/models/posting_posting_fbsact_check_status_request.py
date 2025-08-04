from typing import *

from pydantic import BaseModel, Field


class PostingPostingFBSActCheckStatusRequest(BaseModel):
    """
    object model
    """

    id: int = Field(alias="id")

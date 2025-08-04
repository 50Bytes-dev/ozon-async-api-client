from typing import *

from pydantic import BaseModel, Field


class PostingPostingFBSGetActRequest(BaseModel):
    """
    object model
    """

    id: int = Field(alias="id")

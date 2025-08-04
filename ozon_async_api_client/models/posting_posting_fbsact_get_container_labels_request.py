from typing import *

from pydantic import BaseModel, Field


class PostingPostingFBSActGetContainerLabelsRequest(BaseModel):
    """
    object model
    """

    id: int = Field(alias="id")

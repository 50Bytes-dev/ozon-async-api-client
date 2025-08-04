from typing import *

from pydantic import BaseModel, Field

from .posting_fbsact_create_response_act import PostingFBSActCreateResponseAct


class PostingPostingFBSActCreateResponse(BaseModel):
    """
    object model
    """

    result: Optional[PostingFBSActCreateResponseAct] = Field(alias="result", default=None)

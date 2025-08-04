from typing import *

from pydantic import BaseModel, Field

from .posting_fbsact_check_status_response_status import PostingFBSActCheckStatusResponseStatus


class PostingPostingFBSActCheckStatusResponse(BaseModel):
    """
    object model
    """

    result: Optional[PostingFBSActCheckStatusResponseStatus] = Field(alias="result", default=None)

from typing import *

from pydantic import BaseModel, Field

from .fbs_posting_move_status_response_move_status import FbsPostingMoveStatusResponseMoveStatus


class PostingFbsPostingMoveStatusResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[FbsPostingMoveStatusResponseMoveStatus]]] = Field(alias="result", default=None)

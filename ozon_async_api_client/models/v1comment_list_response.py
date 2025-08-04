from typing import *

from pydantic import BaseModel, Field

from .comment_list_response_comment import CommentListResponseComment


class V1commentListResponse(BaseModel):
    """
    None model
    """

    comments: Optional[List[Optional[CommentListResponseComment]]] = Field(alias="comments", default=None)

    offset: Optional[int] = Field(alias="offset", default=None)

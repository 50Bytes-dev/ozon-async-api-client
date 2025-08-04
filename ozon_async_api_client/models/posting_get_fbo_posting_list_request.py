from typing import *

from pydantic import BaseModel, Field

from .posting_fbo_posting_with_params import PostingFboPostingWithParams
from .posting_get_fbo_posting_list_request_filter import PostingGetFboPostingListRequestFilter


class PostingGetFboPostingListRequest(BaseModel):
    """
    object model
    """

    dir: Optional[str] = Field(alias="dir", default=None)

    filter: PostingGetFboPostingListRequestFilter = Field(alias="filter")

    limit: int = Field(alias="limit")

    offset: Optional[int] = Field(alias="offset", default=None)

    translit: Optional[bool] = Field(alias="translit", default=None)

    with_: Optional[PostingFboPostingWithParams] = Field(alias="with", default=None)

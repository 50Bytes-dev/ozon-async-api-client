from typing import *

from pydantic import BaseModel, Field

from .posting_fbo_posting_with_params import PostingFboPostingWithParams


class PostingGetFboPostingRequest(BaseModel):
    """
    object model
    """

    posting_number: str = Field(alias="posting_number")

    translit: Optional[bool] = Field(alias="translit", default=None)

    with_: Optional[PostingFboPostingWithParams] = Field(alias="with", default=None)

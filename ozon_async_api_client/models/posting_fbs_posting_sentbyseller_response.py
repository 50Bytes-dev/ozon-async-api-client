from typing import *

from pydantic import BaseModel, Field

from .posting_fbs_posting_sentbyseller_response_item import PostingFbsPostingSentbysellerResponseItem


class PostingFbsPostingSentbysellerResponse(BaseModel):
    """
    object model
    """

    result: Optional[List[Optional[PostingFbsPostingSentbysellerResponseItem]]] = Field(alias="result", default=None)

from typing import *

from pydantic import BaseModel, Field

from .v3fbs_posting import V3fbsPosting


class Postingv3getFbsPostingUnfulfilledListResponseResult(BaseModel):
    """
    object model

    Результат запроса.
    """

    count: Optional[int] = Field(alias="count", default=None)

    postings: Optional[List[Optional[V3fbsPosting]]] = Field(alias="postings", default=None)

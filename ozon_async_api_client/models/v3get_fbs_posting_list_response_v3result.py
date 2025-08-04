from typing import *

from pydantic import BaseModel, Field

from .v3fbs_posting import V3fbsPosting


class V3getFbsPostingListResponseV3result(BaseModel):
    """
    object model

    Массив отправлений.
    """

    has_next: Optional[bool] = Field(alias="has_next", default=None)

    postings: Optional[List[Optional[V3fbsPosting]]] = Field(alias="postings", default=None)

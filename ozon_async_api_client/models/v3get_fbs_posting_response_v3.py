from typing import *

from pydantic import BaseModel, Field

from .v3fbs_posting_detail import V3fbsPostingDetail


class V3getFbsPostingResponseV3(BaseModel):
    """
    object model
    """

    result: Optional[V3fbsPostingDetail] = Field(alias="result", default=None)

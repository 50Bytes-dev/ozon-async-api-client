from typing import *

from pydantic import BaseModel, Field

from .v3get_fbs_posting_list_response_v3result import V3getFbsPostingListResponseV3result


class V3getFbsPostingListResponseV3(BaseModel):
    """
    object model
    """

    result: Optional[V3getFbsPostingListResponseV3result] = Field(alias="result", default=None)

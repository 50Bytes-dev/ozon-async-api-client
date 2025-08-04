from typing import *

from pydantic import BaseModel, Field

from .postingv3get_fbs_posting_unfulfilled_list_response_result import \
    Postingv3getFbsPostingUnfulfilledListResponseResult


class Postingv3getFbsPostingUnfulfilledListResponse(BaseModel):
    """
    object model
    """

    result: Optional[Postingv3getFbsPostingUnfulfilledListResponseResult] = Field(alias="result", default=None)

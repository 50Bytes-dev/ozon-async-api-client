from typing import *

from pydantic import BaseModel, Field

from .postingv3fbs_posting_with_params import Postingv3fbsPostingWithParams
from .postingv3get_fbs_posting_list_request_filter import Postingv3getFbsPostingListRequestFilter


class Postingv3getFbsPostingListRequest(BaseModel):
    """
    object model
    """

    dir: Optional[str] = Field(alias="dir", default=None)

    filter: Postingv3getFbsPostingListRequestFilter = Field(alias="filter")

    limit: int = Field(alias="limit")

    offset: int = Field(alias="offset")

    with_: Optional[Postingv3fbsPostingWithParams] = Field(alias="with", default=None)

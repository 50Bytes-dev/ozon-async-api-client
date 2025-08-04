from typing import *

from pydantic import BaseModel, Field

from .dir_enum import DirEnum
from .list_posting_codes_request_filter import ListPostingCodesRequestFilter
from .list_posting_codes_request_with_params import ListPostingCodesRequestWithParams


class V1listPostingCodesRequest(BaseModel):
    """
    None model
    """

    dir: Optional[DirEnum] = Field(alias="dir", default=None)

    filter: Optional[ListPostingCodesRequestFilter] = Field(alias="filter", default=None)

    limit: Optional[int] = Field(alias="limit", default=None)

    offset: Optional[int] = Field(alias="offset", default=None)

    with_: Optional[ListPostingCodesRequestWithParams] = Field(alias="with", default=None)

from typing import *

from pydantic import BaseModel, Field

from .v1question_list_request_filter import V1questionListRequestFilter


class V1questionListRequest(BaseModel):
    """
    object model
    """

    filter: Optional[V1questionListRequestFilter] = Field(alias="filter", default=None)

    last_id: Optional[Union[str, int]] = Field(alias="last_id", default=None)

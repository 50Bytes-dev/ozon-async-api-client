from typing import *

from pydantic import BaseModel, Field

from .v3chat_list_request_filter import V3chatListRequestFilter


class V3chatList(BaseModel):
    """
    object model
    """

    filter: Optional[V3chatListRequestFilter] = Field(alias="filter", default=None)

    limit: int = Field(alias="limit")

    cursor: Optional[str] = Field(alias="cursor", default=None)

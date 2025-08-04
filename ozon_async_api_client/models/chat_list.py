from typing import *

from pydantic import BaseModel, Field

from .chat_list_request_filter import ChatListRequestFilter


class ChatList(BaseModel):
    """
    object model
    """

    filter: Optional[ChatListRequestFilter] = Field(alias="filter", default=None)

    limit: int = Field(alias="limit")

    offset: Optional[int] = Field(alias="offset", default=None)

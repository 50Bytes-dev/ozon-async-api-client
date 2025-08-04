from typing import *

from pydantic import BaseModel, Field


class V2chatListResponse(BaseModel):
    """
    object model
    """

    chats: Optional[Any] = Field(alias="chats", default=None)

    total_chats_count: Optional[int] = Field(alias="total_chats_count", default=None)

    total_unread_count: Optional[int] = Field(alias="total_unread_count", default=None)

from typing import *

from pydantic import BaseModel, Field


class ChatListRequestFilter(BaseModel):
    """
    object model

    Фильтр по чатам.
    """

    chat_status: Optional[str] = Field(alias="chat_status", default=None)

    unread_only: Optional[bool] = Field(alias="unread_only", default=None)

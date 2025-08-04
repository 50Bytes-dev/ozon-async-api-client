from typing import *

from pydantic import BaseModel, Field


class ChatInfo(BaseModel):
    """
    object model

    Данные чата.
    """

    chat_id: Optional[str] = Field(alias="chat_id", default=None)

    chat_status: Optional[str] = Field(alias="chat_status", default=None)

    chat_type: Optional[str] = Field(alias="chat_type", default=None)

    created_at: Optional[str] = Field(alias="created_at", default=None)

    first_unread_message_id: Optional[int] = Field(alias="first_unread_message_id", default=None)

    last_message_id: Optional[int] = Field(alias="last_message_id", default=None)

    unread_count: Optional[int] = Field(alias="unread_count", default=None)

from typing import *

from pydantic import BaseModel, Field

from .v3chat_details_info import V3chatDetailsInfo


class V3chatInfo(BaseModel):
    """
    None model
    """

    chat: Optional[V3chatDetailsInfo] = Field(alias="chat", default=None)

    first_unread_message_id: Optional[int] = Field(alias="first_unread_message_id", default=None)

    last_message_id: Optional[int] = Field(alias="last_message_id", default=None)

    unread_count: Optional[int] = Field(alias="unread_count", default=None)

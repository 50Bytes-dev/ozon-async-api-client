from typing import *

from pydantic import BaseModel, Field


class ChatRead(BaseModel):
    """
    object model
    """

    chat_id: str = Field(alias="chat_id")

    from_message_id: Optional[int] = Field(alias="from_message_id", default=None)

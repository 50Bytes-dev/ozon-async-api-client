from typing import *

from pydantic import BaseModel, Field


class ChatHistory(BaseModel):
    """
    object model
    """

    chat_id: str = Field(alias="chat_id")

    direction: Optional[str] = Field(alias="direction", default=None)

    from_message_id: Optional[int] = Field(alias="from_message_id", default=None)

    limit: int = Field(alias="limit")

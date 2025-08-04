from typing import *

from pydantic import BaseModel, Field


class ChatChatSendMessageRequest(BaseModel):
    """
    ChatSendMessage model
    """

    chat_id: str = Field(alias="chat_id")

    text: str = Field(alias="text")

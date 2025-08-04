from typing import *

from pydantic import BaseModel, Field


class ChatChatSendMessageRequest(BaseModel):
    """
    ChatSendMessage model
    """

    chat_id: Union[str, int] = Field(alias="chat_id")

    text: str = Field(alias="text")

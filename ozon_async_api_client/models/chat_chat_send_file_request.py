from typing import *

from pydantic import BaseModel, Field


class ChatChatSendFileRequest(BaseModel):
    """
    ChatSendFile model
    """

    base64_content: Optional[str] = Field(alias="base64_content", default=None)

    chat_id: Union[str, int] = Field(alias="chat_id")

    name: Optional[str] = Field(alias="name", default=None)

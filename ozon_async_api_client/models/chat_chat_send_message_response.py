from typing import *

from pydantic import BaseModel, Field


class ChatChatSendMessageResponse(BaseModel):
    """
    object model
    """

    result: Optional[str] = Field(alias="result", default=None)

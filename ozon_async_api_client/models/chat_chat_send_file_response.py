from typing import *

from pydantic import BaseModel, Field


class ChatChatSendFileResponse(BaseModel):
    """
    object model
    """

    result: Optional[str] = Field(alias="result", default=None)

from typing import *

from pydantic import BaseModel, Field

from .chat_start_response_result import ChatStartResponseResult


class ChatChatStartResponse(BaseModel):
    """
    object model
    """

    result: Optional[ChatStartResponseResult] = Field(alias="result", default=None)

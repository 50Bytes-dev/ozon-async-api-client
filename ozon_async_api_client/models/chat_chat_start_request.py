from typing import *

from pydantic import BaseModel, Field


class ChatChatStartRequest(BaseModel):
    """
    ChatStart model
    """

    posting_number: str = Field(alias="posting_number")

from typing import *

from pydantic import BaseModel, Field


class ChatChatStartRequest(BaseModel):
    """
    ChatStart model
    """

    posting_number: Union[str, int] = Field(alias="posting_number")

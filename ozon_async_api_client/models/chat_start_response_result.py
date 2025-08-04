from typing import *

from pydantic import BaseModel, Field


class ChatStartResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    chat_id: Optional[str] = Field(alias="chat_id", default=None)

from typing import *

from pydantic import BaseModel, Field


class ChatHistoryRequestFilter(BaseModel):
    """
    None model

    Фильтр по сообщениям.
    """

    message_ids: Optional[List[str]] = Field(alias="message_ids", default=None)

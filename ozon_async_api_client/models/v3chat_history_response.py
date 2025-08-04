from typing import *

from pydantic import BaseModel, Field

from .v3chat_message import V3chatMessage


class V3chatHistoryResponse(BaseModel):
    """
    None model
    """

    has_next: Optional[bool] = Field(alias="has_next", default=None)

    messages: Optional[List[Optional[V3chatMessage]]] = Field(alias="messages", default=None)

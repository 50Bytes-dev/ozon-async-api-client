from typing import *

from pydantic import BaseModel, Field

from .chat_history_request_filter import ChatHistoryRequestFilter


class V3chatHistoryRequest(BaseModel):
    """
    None model
    """

    chat_id: Union[str, int] = Field(alias="chat_id")

    direction: Optional[Union[str, int]] = Field(alias="direction", default=None)

    filter: Optional[ChatHistoryRequestFilter] = Field(alias="filter", default=None)

    from_message_id: Optional[int] = Field(alias="from_message_id", default=None)

    limit: Optional[int] = Field(alias="limit", default=None)

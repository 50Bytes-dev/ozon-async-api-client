from typing import *

from pydantic import BaseModel, Field


class V3chatListResponse(BaseModel):
    """
    object model
    """

    chats: Optional[Any] = Field(alias="chats", default=None)

    total_unread_count: Optional[int] = Field(alias="total_unread_count", default=None)

    cursor: Optional[str] = Field(alias="cursor", default=None)

    has_next: Optional[bool] = Field(alias="has_next", default=None)

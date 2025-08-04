from typing import *

from pydantic import BaseModel, Field

from .v2user import V2user


class V2chatMessage(BaseModel):
    """
    object model
    """

    created_at: Optional[str] = Field(alias="created_at", default=None)

    data: Optional[Any] = Field(alias="data", default=None)

    is_read: Optional[bool] = Field(alias="is_read", default=None)

    messageId: Optional[int] = Field(alias="messageId", default=None)

    user: Optional[V2user] = Field(alias="user", default=None)

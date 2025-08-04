from typing import *

from pydantic import BaseModel, Field


class V2chatHistoryResponse(BaseModel):
    """
    object model
    """

    has_next: Optional[bool] = Field(alias="has_next", default=None)

    messages: Optional[Any] = Field(alias="messages", default=None)

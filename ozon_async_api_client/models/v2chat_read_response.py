from typing import *

from pydantic import BaseModel, Field


class V2chatReadResponse(BaseModel):
    """
    object model
    """

    unread_count: Optional[int] = Field(alias="unread_count", default=None)

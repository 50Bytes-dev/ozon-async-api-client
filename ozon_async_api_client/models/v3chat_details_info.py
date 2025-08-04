from typing import *

from pydantic import BaseModel, Field


class V3chatDetailsInfo(BaseModel):
    """
    None model

    Информация о чате.
    """

    created_at: Optional[str] = Field(alias="created_at", default=None)

    chat_id: Optional[Union[str, int]] = Field(alias="chat_id", default=None)

    chat_status: Optional[str] = Field(alias="chat_status", default=None)

    chat_type: Optional[str] = Field(alias="chat_type", default=None)

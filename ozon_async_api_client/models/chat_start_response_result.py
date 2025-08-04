from typing import *

from pydantic import BaseModel, Field


class ChatStartResponseResult(BaseModel):
    """
    object model

    Результат работы метода.
    """

    chat_id: Optional[Union[str, int]] = Field(alias="chat_id", default=None)

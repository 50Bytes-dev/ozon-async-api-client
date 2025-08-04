from typing import *

from pydantic import BaseModel, Field


class PostingExemplarInfoExemplarError(BaseModel):
    """
    None model
    """

    key: Optional[str] = Field(alias="key", default=None)

    message: Optional[str] = Field(alias="message", default=None)

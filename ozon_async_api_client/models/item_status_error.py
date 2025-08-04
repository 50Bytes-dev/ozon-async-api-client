from typing import *

from pydantic import BaseModel, Field


class ItemStatusError(BaseModel):
    """
    None model
    """

    code: Optional[str] = Field(alias="code", default=None)

    message: Optional[str] = Field(alias="message", default=None)

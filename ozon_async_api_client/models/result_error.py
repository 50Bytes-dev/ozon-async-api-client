from typing import *

from pydantic import BaseModel, Field


class ResultError(BaseModel):
    """
    object model
    """

    code: Optional[str] = Field(alias="code", default=None)

    status: Optional[str] = Field(alias="status", default=None)

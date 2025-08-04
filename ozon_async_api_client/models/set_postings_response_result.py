from typing import *

from pydantic import BaseModel, Field


class SetPostingsResponseResult(BaseModel):
    """
    object model
    """

    error: Optional[str] = Field(alias="error", default=None)

    posting_number: Optional[str] = Field(alias="posting_number", default=None)

    result: Optional[bool] = Field(alias="result", default=None)

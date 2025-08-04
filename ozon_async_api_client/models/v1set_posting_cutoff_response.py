from typing import *

from pydantic import BaseModel, Field


class V1setPostingCutoffResponse(BaseModel):
    """
    object model
    """

    result: Optional[bool] = Field(alias="result", default=None)

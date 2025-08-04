from typing import *

from pydantic import BaseModel, Field


class PostingPostingProductChangeResponse(BaseModel):
    """
    object model
    """

    result: Optional[str] = Field(alias="result", default=None)

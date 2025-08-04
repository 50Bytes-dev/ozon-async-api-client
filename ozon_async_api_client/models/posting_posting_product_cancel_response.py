from typing import *

from pydantic import BaseModel, Field


class PostingPostingProductCancelResponse(BaseModel):
    """
    object model
    """

    result: Optional[str] = Field(alias="result", default=None)

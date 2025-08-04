from typing import *

from pydantic import BaseModel, Field


class PostingPostingProductChangeResponse(BaseModel):
    """
    object model
    """

    result: Optional[Union[str, int]] = Field(alias="result", default=None)

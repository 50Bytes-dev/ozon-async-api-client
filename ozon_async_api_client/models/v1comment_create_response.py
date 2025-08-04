from typing import *

from pydantic import BaseModel, Field


class V1commentCreateResponse(BaseModel):
    """
    None model
    """

    comment_id: Optional[str] = Field(alias="comment_id", default=None)

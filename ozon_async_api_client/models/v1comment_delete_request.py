from typing import *

from pydantic import BaseModel, Field


class V1commentDeleteRequest(BaseModel):
    """
    None model
    """

    comment_id: str = Field(alias="comment_id")

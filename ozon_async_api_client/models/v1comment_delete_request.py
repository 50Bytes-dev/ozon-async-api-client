from typing import *

from pydantic import BaseModel, Field


class V1commentDeleteRequest(BaseModel):
    """
    None model
    """

    comment_id: Union[str, int] = Field(alias="comment_id")

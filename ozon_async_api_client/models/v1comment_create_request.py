from typing import *

from pydantic import BaseModel, Field


class V1commentCreateRequest(BaseModel):
    """
    None model
    """

    mark_review_as_processed: Optional[bool] = Field(alias="mark_review_as_processed", default=None)

    parent_comment_id: Optional[str] = Field(alias="parent_comment_id", default=None)

    review_id: str = Field(alias="review_id")

    text: str = Field(alias="text")

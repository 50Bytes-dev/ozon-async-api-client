from typing import *

from pydantic import BaseModel, Field


class CommentListResponseComment(BaseModel):
    """
    None model
    """

    id: Optional[Union[str, int]] = Field(alias="id", default=None)

    is_official: Optional[bool] = Field(alias="is_official", default=None)

    is_owner: Optional[bool] = Field(alias="is_owner", default=None)

    parent_comment_id: Optional[Union[str, int]] = Field(alias="parent_comment_id", default=None)

    published_at: Optional[str] = Field(alias="published_at", default=None)

    text: Optional[str] = Field(alias="text", default=None)

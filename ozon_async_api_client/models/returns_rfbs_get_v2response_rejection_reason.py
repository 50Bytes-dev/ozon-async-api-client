from typing import *

from pydantic import BaseModel, Field


class ReturnsRfbsGetV2responseRejectionReason(BaseModel):
    """
    object model
    """

    hint: Optional[str] = Field(alias="hint", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    is_comment_required: Optional[bool] = Field(alias="is_comment_required", default=None)

    name: Optional[str] = Field(alias="name", default=None)

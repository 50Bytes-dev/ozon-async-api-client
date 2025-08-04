from typing import *

from pydantic import BaseModel, Field


class PostingCancelReason(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    is_available_for_cancellation: Optional[bool] = Field(alias="is_available_for_cancellation", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    type_id: Optional[str] = Field(alias="type_id", default=None)

from typing import *

from pydantic import BaseModel, Field


class RelatedPostingCancelReasons(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    type_id: Optional[str] = Field(alias="type_id", default=None)

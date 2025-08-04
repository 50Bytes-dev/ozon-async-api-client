from typing import *

from pydantic import BaseModel, Field


class PostingPostingFBSActCreateRequest(BaseModel):
    """
    object model
    """

    containers_count: Optional[int] = Field(alias="containers_count", default=None)

    delivery_method_id: int = Field(alias="delivery_method_id")

    departure_date: Optional[str] = Field(alias="departure_date", default=None)

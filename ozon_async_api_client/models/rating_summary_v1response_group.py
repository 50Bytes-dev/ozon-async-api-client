from typing import *

from pydantic import BaseModel, Field


class RatingSummaryV1responseGroup(BaseModel):
    """
    object model
    """

    group_name: Optional[str] = Field(alias="group_name", default=None)

    items: Optional[Any] = Field(alias="items", default=None)

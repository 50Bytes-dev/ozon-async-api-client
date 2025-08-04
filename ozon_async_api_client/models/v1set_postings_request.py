from typing import *

from pydantic import BaseModel, Field


class V1setPostingsRequest(BaseModel):
    """
    object model
    """

    carriage_id: Optional[int] = Field(alias="carriage_id", default=None)

    posting_numbers: Optional[List[str]] = Field(alias="posting_numbers", default=None)

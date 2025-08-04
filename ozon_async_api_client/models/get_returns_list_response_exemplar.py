from typing import *

from pydantic import BaseModel, Field


class GetReturnsListResponseExemplar(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

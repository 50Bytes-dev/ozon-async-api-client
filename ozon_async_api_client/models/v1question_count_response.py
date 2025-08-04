from typing import *

from pydantic import BaseModel, Field


class V1questionCountResponse(BaseModel):
    """
    object model
    """

    all: Optional[int] = Field(alias="all", default=None)

    new: Optional[int] = Field(alias="new", default=None)

    processed: Optional[int] = Field(alias="processed", default=None)

    unprocessed: Optional[int] = Field(alias="unprocessed", default=None)

    viewed: Optional[int] = Field(alias="viewed", default=None)

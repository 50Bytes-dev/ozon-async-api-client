from typing import *

from pydantic import BaseModel, Field


class ReviewInfoResponsePhoto(BaseModel):
    """
    None model
    """

    height: Optional[int] = Field(alias="height", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    width: Optional[int] = Field(alias="width", default=None)

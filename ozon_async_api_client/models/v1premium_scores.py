from typing import *

from pydantic import BaseModel, Field


class V1premiumScores(BaseModel):
    """
    object model
    """

    rating: Optional[str] = Field(alias="rating", default=None)

    scores: Optional[Any] = Field(alias="scores", default=None)

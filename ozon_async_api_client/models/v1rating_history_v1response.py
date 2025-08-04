from typing import *

from pydantic import BaseModel, Field


class V1ratingHistoryV1response(BaseModel):
    """
    object model
    """

    premium_scores: Optional[Any] = Field(alias="premium_scores", default=None)

    ratings: Optional[Any] = Field(alias="ratings", default=None)

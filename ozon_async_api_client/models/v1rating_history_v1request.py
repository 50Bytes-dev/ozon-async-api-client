from typing import *

from pydantic import BaseModel, Field


class V1ratingHistoryV1request(BaseModel):
    """
    object model
    """

    date_from: str = Field(alias="date_from")

    date_to: str = Field(alias="date_to")

    ratings: Any = Field(alias="ratings")

    with_premium_scores: Optional[bool] = Field(alias="with_premium_scores", default=None)

from typing import *

from pydantic import BaseModel, Field


class PremiumScoresScore(BaseModel):
    """
    object model
    """

    date: Optional[str] = Field(alias="date", default=None)

    rating_value: Optional[float] = Field(alias="rating_value", default=None)

    value: Optional[int] = Field(alias="value", default=None)

from typing import *

from pydantic import BaseModel, Field


class RatingItemChange(BaseModel):
    """
    object model

    Изменение рейтинга: отношение предыдущего значения к текущему.

    """

    direction: Optional[str] = Field(alias="direction", default=None)

    meaning: Optional[str] = Field(alias="meaning", default=None)

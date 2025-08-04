from typing import *

from pydantic import BaseModel, Field


class V1rating(BaseModel):
    """
    object model
    """

    danger_threshold: Optional[float] = Field(alias="danger_threshold", default=None)

    premium_threshold: Optional[float] = Field(alias="premium_threshold", default=None)

    rating: Optional[str] = Field(alias="rating", default=None)

    values: Optional[Any] = Field(alias="values", default=None)

    warning_threshold: Optional[float] = Field(alias="warning_threshold", default=None)

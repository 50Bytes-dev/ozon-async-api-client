from typing import *

from pydantic import BaseModel, Field

from .v1rating_status import V1ratingStatus


class RatingValue(BaseModel):
    """
    object model
    """

    date_from: Optional[str] = Field(alias="date_from", default=None)

    date_to: Optional[str] = Field(alias="date_to", default=None)

    status: Optional[V1ratingStatus] = Field(alias="status", default=None)

    value: Optional[float] = Field(alias="value", default=None)

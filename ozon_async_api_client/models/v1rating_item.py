from typing import *

from pydantic import BaseModel, Field

from .rating_item_change import RatingItemChange


class V1ratingItem(BaseModel):
    """
    object model
    """

    change: Optional[RatingItemChange] = Field(alias="change", default=None)

    current_value: Optional[float] = Field(alias="current_value", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    past_value: Optional[float] = Field(alias="past_value", default=None)

    rating: Optional[str] = Field(alias="rating", default=None)

    rating_direction: Optional[str] = Field(alias="rating_direction", default=None)

    status: Optional[str] = Field(alias="status", default=None)

    value_type: Optional[str] = Field(alias="value_type", default=None)

from typing import *

from pydantic import BaseModel, Field


class V1ratingStatus(BaseModel):
    """
    object model

    Статус рейтинга.
    """

    danger: Optional[bool] = Field(alias="danger", default=None)

    premium: Optional[bool] = Field(alias="premium", default=None)

    warning: Optional[bool] = Field(alias="warning", default=None)

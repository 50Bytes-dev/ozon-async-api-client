from typing import *

from pydantic import BaseModel, Field


class MarketingAction(BaseModel):
    """
    object model
    """

    date_from: Optional[str] = Field(alias="date_from", default=None)

    date_to: Optional[str] = Field(alias="date_to", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    value: Optional[str] = Field(alias="value", default=None)

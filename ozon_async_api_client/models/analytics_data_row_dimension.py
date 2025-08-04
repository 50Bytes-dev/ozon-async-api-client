from typing import *

from pydantic import BaseModel, Field


class AnalyticsDataRowDimension(BaseModel):
    """
    object model
    """

    id: Optional[Union[str, int]] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

from typing import *

from pydantic import BaseModel, Field


class V1giveoutIsEnabledResponse(BaseModel):
    """
    None model
    """

    enabled: Optional[bool] = Field(alias="enabled", default=None)

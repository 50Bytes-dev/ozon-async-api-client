from typing import *

from pydantic import BaseModel, Field


class V1productActionTimerStatusResponse(BaseModel):
    """
    None model
    """

    statuses: Optional[Any] = Field(alias="statuses", default=None)

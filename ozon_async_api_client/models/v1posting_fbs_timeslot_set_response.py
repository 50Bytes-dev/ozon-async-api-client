from typing import *

from pydantic import BaseModel, Field


class V1postingFbsTimeslotSetResponse(BaseModel):
    """
    object model
    """

    result: Optional[bool] = Field(alias="result", default=None)

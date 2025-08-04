from typing import *

from pydantic import BaseModel, Field


class V1carriageCreateResponse(BaseModel):
    """
    object model
    """

    carriage_id: Optional[int] = Field(alias="carriage_id", default=None)

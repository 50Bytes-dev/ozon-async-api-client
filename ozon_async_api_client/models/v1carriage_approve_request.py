from typing import *

from pydantic import BaseModel, Field


class V1carriageApproveRequest(BaseModel):
    """
    object model
    """

    carriage_id: int = Field(alias="carriage_id")

    containers_count: Optional[int] = Field(alias="containers_count", default=None)

from typing import *

from pydantic import BaseModel, Field


class V1conditionalCancellationMoveRequest(BaseModel):
    """
    object model
    """

    cancellation_id: int = Field(alias="cancellation_id")

    comment: Optional[str] = Field(alias="comment", default=None)

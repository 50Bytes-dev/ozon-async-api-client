from typing import *

from pydantic import BaseModel, Field


class V2conditionalCancellationMoveV2request(BaseModel):
    """
    None model
    """

    cancellation_id: int = Field(alias="cancellation_id")

    comment: Optional[str] = Field(alias="comment", default=None)

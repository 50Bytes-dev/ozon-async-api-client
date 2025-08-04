from typing import *

from pydantic import BaseModel, Field


class V1getConditionalCancellationRequest(BaseModel):
    """
    object model
    """

    cancellation_id: int = Field(alias="cancellation_id")

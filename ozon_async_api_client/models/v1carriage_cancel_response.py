from typing import *

from pydantic import BaseModel, Field


class V1carriageCancelResponse(BaseModel):
    """
    object model
    """

    error: Optional[str] = Field(alias="error", default=None)

    carriage_status: Optional[str] = Field(alias="carriage_status", default=None)

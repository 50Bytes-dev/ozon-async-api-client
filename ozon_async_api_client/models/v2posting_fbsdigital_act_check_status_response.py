from typing import *

from pydantic import BaseModel, Field


class V2postingFBSDigitalActCheckStatusResponse(BaseModel):
    """
    object model
    """

    id: Optional[int] = Field(alias="id", default=None)

    status: Optional[str] = Field(alias="status", default=None)

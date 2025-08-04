from typing import *

from pydantic import BaseModel, Field


class V2postingFBSDigitalActCheckStatusRequest(BaseModel):
    """
    object model
    """

    id: int = Field(alias="id")

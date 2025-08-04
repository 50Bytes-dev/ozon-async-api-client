from typing import *

from pydantic import BaseModel, Field


class V2returnsRfbsReceiveReturnRequest(BaseModel):
    """
    object model
    """

    return_id: int = Field(alias="return_id")

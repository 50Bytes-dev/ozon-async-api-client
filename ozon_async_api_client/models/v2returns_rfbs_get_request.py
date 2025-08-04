from typing import *

from pydantic import BaseModel, Field


class V2returnsRfbsGetRequest(BaseModel):
    """
    object model
    """

    return_id: int = Field(alias="return_id")

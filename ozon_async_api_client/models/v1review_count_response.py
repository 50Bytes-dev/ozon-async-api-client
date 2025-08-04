from typing import *

from pydantic import BaseModel, Field


class V1reviewCountResponse(BaseModel):
    """
    None model
    """

    processed: Optional[int] = Field(alias="processed", default=None)

    total: Optional[int] = Field(alias="total", default=None)

    unprocessed: Optional[int] = Field(alias="unprocessed", default=None)

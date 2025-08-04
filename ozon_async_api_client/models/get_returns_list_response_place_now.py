from typing import *

from pydantic import BaseModel, Field


class GetReturnsListResponsePlaceNow(BaseModel):
    """
    object model

    Склад, где находится возврат.
    """

    id: Optional[int] = Field(alias="id", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    address: Optional[str] = Field(alias="address", default=None)

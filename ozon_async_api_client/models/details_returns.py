from typing import *

from pydantic import BaseModel, Field


class DetailsReturns(BaseModel):
    """
    object model

    Плата за возвраты и отмены.
    """

    total: Optional[float] = Field(alias="total", default=None)

    items: Optional[List[Any]] = Field(alias="items", default=None)

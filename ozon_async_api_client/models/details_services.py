from typing import *

from pydantic import BaseModel, Field


class DetailsServices(BaseModel):
    """
    object model

    Плата за обработку и доставку.
    """

    total: Optional[float] = Field(alias="total", default=None)

    items: Optional[List[Any]] = Field(alias="items", default=None)

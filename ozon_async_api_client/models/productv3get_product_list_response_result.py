from typing import *

from pydantic import BaseModel, Field


class Productv3getProductListResponseResult(BaseModel):
    """
    object model

    Результат.
    """

    items: Optional[Any] = Field(alias="items", default=None)

    last_id: Optional[str] = Field(alias="last_id", default=None)

    total: Optional[int] = Field(alias="total", default=None)

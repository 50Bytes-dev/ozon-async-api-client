from typing import *

from pydantic import BaseModel, Field


class Productv5getProductInfoPricesV5response(BaseModel):
    """
    object model
    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    items: Optional[Any] = Field(alias="items", default=None)

    total: Optional[int] = Field(alias="total", default=None)

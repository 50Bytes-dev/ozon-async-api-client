from typing import *

from pydantic import BaseModel, Field

from .productv5filter import Productv5filter


class Productv5getProductInfoPricesV5request(BaseModel):
    """
    object model
    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    filter: Productv5filter = Field(alias="filter")

    limit: int = Field(alias="limit")

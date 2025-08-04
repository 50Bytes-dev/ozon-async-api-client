from typing import *

from pydantic import BaseModel, Field


class V1getProductInfoDiscountedResponse(BaseModel):
    """
    object model
    """

    items: Optional[Any] = Field(alias="items", default=None)
